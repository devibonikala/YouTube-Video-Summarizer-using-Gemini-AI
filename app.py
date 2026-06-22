import streamlit as st
from dotenv import load_dotenv
import os
from google import genai  # Modern, updated Google GenAI SDK
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GEMINI_API_KEY / GOOGLE_API_KEY not found in .env file")
    st.stop()

# Initialize the modern Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# -----------------------------
# Prompt
# -----------------------------
PROMPT = """
You are an expert YouTube video summarizer.

Analyze the transcript and provide:

1. Brief Summary
2. Important Key Points
3. Conclusion

Keep the response within 250 words.
"""

# -----------------------------
# Extract Video ID (Fixed to return a raw string)
# -----------------------------
def get_video_id(url):
    try:
        parsed_url = urlparse(url)

        # Handle shortened URLs like youtu.be/abc123xyz
        if parsed_url.hostname == "youtu.be":
            return parsed_url.path[1:]

        # Handle standard URLs like ://youtube.com
        if parsed_url.hostname in [
            "www.youtube.com",
            "youtube.com",
            "m.youtube.com"
        ]:
            query_params = parse_qs(parsed_url.query)
            if "v" in query_params and query_params["v"]:
                # Crucial Fix: get the first item from the list string wrapper
                return query_params["v"][0]

        return None

    except Exception:
        return None

# -----------------------------
# Fetch Transcript (Fully Updated for Modern Objects)
# -----------------------------
def get_transcript(video_id):
    try:
        # 1. Initialize instance and pull transcript object
        api_instance = YouTubeTranscriptApi()
        transcript_data = api_instance.fetch(video_id)
        
        # 2. Extract text using dot notation (.text) because it is an object
        transcript = " ".join(item.text for item in transcript_data)
        return transcript

    except Exception as e:
        # Fallback to check if a specific language collection is required
        try:
            transcript_list = YouTubeTranscriptApi().list(video_id)
            transcript_obj = transcript_list.find_transcript(['en'])
            transcript_data = transcript_obj.fetch()
            
            # Extract using dot notation here as well
            transcript = " ".join(item.text for item in transcript_data)
            return transcript
        except Exception as fallback_error:
            st.error(f"Transcript Error: {str(fallback_error)}")
            return None

# -----------------------------
# Gemini Summary 
# -----------------------------
def generate_summary(transcript):
    try:
        # Using active production model "gemini-2.5-flash"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=PROMPT + "\n\nTranscript:\n" + transcript,
        )

        return response.text

    except Exception as e:
        st.error(f"Gemini Error: {str(e)}")
        return None

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Video Summarizer")
st.write("Paste a YouTube video link and generate a summary using Gemini AI.")

youtube_url = st.text_input(
    "Enter YouTube Video URL"
)

if youtube_url:
    video_id = get_video_id(youtube_url)

    if video_id:
        # Fixed: video_id is now a clean string, constructing the image path correctly
       st.image(
    f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
    use_container_width=True
     )
    else:
        st.warning("Invalid YouTube URL")

if st.button("Generate Summary"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL")
        st.stop()

    video_id = get_video_id(youtube_url)

    if not video_id:
        st.error("Invalid YouTube URL")
        st.stop()

    with st.spinner("Fetching Transcript..."):
        transcript = get_transcript(video_id)

    if transcript:
        with st.spinner("Generating Summary..."):
            summary = generate_summary(transcript)

        if summary:
            st.success("Summary Generated Successfully")

            st.subheader("📄 Video Summary")
            st.write(summary)

            with st.expander("📜 Full Transcript"):
                st.write(transcript)
