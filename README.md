# YouTube-Video-Summarizer-using-Gemini-AI
AI-powered YouTube Video Summarizer built with Python, Streamlit, Google Gemini AI, and YouTube Transcript API. Extracts video transcripts and generates concise summaries with key points and conclusions through an interactive web interface. 🚀
# 🎥 YouTube Video Summarizer using Gemini AI

## 📌 Project Overview

This project is an AI-powered YouTube Video Summarizer that extracts transcripts from YouTube videos and generates concise summaries using Google's Gemini AI model. Users can quickly understand the content of a video without watching the entire video.

---

## 🚀 Features

- Extracts YouTube Video ID from URL
- Fetches Video Transcript Automatically
- Displays YouTube Video Thumbnail
- Generates AI-Powered Summary
- Provides Key Points and Conclusion
- Shows Full Transcript
- Handles Invalid URLs and Errors

---

## 🛠️ Tools & Technologies Used

- Python
- Streamlit
- Google Gemini API (Gemini 2.5 Flash)
- YouTube Transcript API
- python-dotenv
- urllib.parse
- VS Code

---

## 📂 Project Workflow

### Step 1: Set Up the Project

Created a Python project and installed required libraries:

```bash
pip install streamlit
pip install google-genai
pip install youtube-transcript-api
pip install python-dotenv
```

### Step 2: Configure Gemini API

- Created a Gemini API key from Google AI Studio.
- Stored the API key securely in a `.env` file.

Example:

```env
GOOGLE_API_KEY=your_api_key_here
```

### Step 3: Build the User Interface

Used Streamlit to create:

- Project Title
- YouTube URL Input Box
- Generate Summary Button
- Summary Display Section
- Transcript Display Section

### Step 4: Extract YouTube Video ID

Used Python's `urllib.parse` module to:

- Read the YouTube URL
- Extract the Video ID
- Support both normal and shortened YouTube URLs

### Step 5: Display Video Thumbnail

Generated the thumbnail URL using the extracted video ID and displayed it in Streamlit.

Example:

```python
thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
```

### Step 6: Fetch Video Transcript

Used YouTube Transcript API to:

- Retrieve subtitles/transcripts
- Combine transcript text into a single string
- Handle transcript-related exceptions

### Step 7: Create AI Prompt

Designed a custom prompt instructing Gemini AI to generate:

- Brief Summary
- Important Key Points
- Conclusion

### Step 8: Generate Summary Using Gemini AI

Sent the transcript to Gemini 2.5 Flash model and received a summarized response.

### Step 9: Display Results

Displayed:

- Generated Summary
- Full Transcript
- Success/Error Messages

### Step 10: Error Handling

Implemented handling for:

- Invalid URLs
- Missing API Keys
- Transcript Retrieval Failures
- Gemini API Errors

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Output

1. Enter YouTube Video URL
2. Thumbnail Appears
3. Click "Generate Summary"
4. AI Summary is Generated
5. Full Transcript is Displayed

---

## 🎯 Learning Outcomes

- Streamlit Web Application Development
- API Integration
- Generative AI Applications
- Prompt Engineering
- Environment Variable Management
- Error Handling in Python
- Working with YouTube Data

---

## 👨‍💻 Author

Devi
