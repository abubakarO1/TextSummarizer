# Smart AI Summarizer

**Smart AI Summarizer** is a web application that allows users to summarize text, documents, and speech effortlessly. It utilizes **Whisper AI** for real-time speech-to-text transcription and **TextRank** for text summarization.

## 🚀 Features

- 🎙 **Audio-to-Text & Summarization**
  - Record audio directly in the app.
  - Upload MP3 or WAV files for transcription.
  - Summarize transcribed text into Quick, Standard, or Detailed summaries.

- 📄 **Document Summarization**
  - Upload `.docx` files for text extraction.
  - Summarize extracted content into different levels of detail.

- ⏬ **Downloadable Summaries**
  - Users can download the generated summaries as `.txt` files.

## 🛠️ Installation

### Prerequisites:
- Python 3.8 or later
- pip (Python package manager)

### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/yourusername/smart-ai-summarizer.git
cd smart-ai-summarizer
```

### 2️⃣ Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application:
```bash
streamlit run app.py
```

## 📦 Dependencies (requirements.txt)
```txt
streamlit
openai-whisper
torch
numpy
sumy
python-docx
streamlit-mic-recorder
```

## 📜 How It Works

1. **Audio Summarization:**
   - Click **Start Recording** or upload an audio file.
   - The app transcribes the speech using **Whisper AI**.
   - Choose a summary type (Quick, Standard, Detailed).
   - View the transcript and summarized version.
   - Download the summary as a text file.

2. **Document Summarization:**
   - Upload a `.docx` file.
   - The app extracts text from the document.
   - Choose a summary type.
   - View and download the summarized content.

## 💡 Technologies Used

- **Streamlit**: Frontend framework for interactive web applications.
- **Whisper AI**: Speech-to-text transcription.
- **TextRank (Sumy)**: Text summarization.
- **Python-docx**: Extracting text from Word documents.
- **Torch & NumPy**: Required for Whisper AI.

## 🔧 Troubleshooting

- **Whisper AI not working?** Ensure `torch` is installed properly with:
  ```bash
  pip install torch torchvision torchaudio
  ```
- **App not launching?** Ensure you're running:
  ```bash
  streamlit run app.py
  ```

## 📜 License

This project is licensed under the **MIT License**.
