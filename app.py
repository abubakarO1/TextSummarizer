import streamlit as st
import whisper
import os
import tempfile
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from docx import Document
from streamlit_mic_recorder import mic_recorder

# Page Setup
st.set_page_config(page_title="Smart AI Summarizer", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #0055A4;'>Smart AI Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>Summarize text, documents, and speech effortlessly.</p>", unsafe_allow_html=True)

# Load Whisper Model
ai_transcriber = whisper.load_model("small")

# Summarization Function (TextRank)
def generate_summary(content, level):
    if not content.strip():
        return "No valid text found."

    try:
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        sentence_count = {"Quick": 2, "Standard": 4, "Detailed": 6}[level]
        summary = summarizer(parser.document, sentence_count)
        return " ".join([str(sentence) for sentence in summary])
    except Exception as error:
        return f"Summarization failed: {str(error)}"

# Tabs for different functionalities (Audio first, then Document)
sections = st.tabs(["🎙️ Audio to Text", "📄 Document Summarizer"])

# === AUDIO TRANSCRIPTION & SUMMARIZATION ===
with sections[0]:
    st.subheader("🎙️ Record or Upload Audio")

    # Record Audio
    recorded_clip = mic_recorder(start_prompt="🎤 Start Recording", stop_prompt="🛑 Stop")

    # Upload Audio File
    uploaded_audio_file = st.file_uploader("Upload MP3 or WAV", type=["mp3", "wav"])
    audio_summary_level = st.radio("Choose Summary Type:", ["Quick", "Standard", "Detailed"], horizontal=True)

    temp_audio_path = None

    if recorded_clip:
        audio_data = recorded_clip["bytes"]
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp_audio.write(audio_data)
        temp_audio.close()
        temp_audio_path = temp_audio.name

    elif uploaded_audio_file:
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_audio.write(uploaded_audio_file.getbuffer())
        temp_audio.close()
        temp_audio_path = temp_audio.name

    if temp_audio_path:
        st.audio(temp_audio_path)

        # Transcription Process
        try:
            with st.spinner("Processing Audio..."):
                transcript_result = ai_transcriber.transcribe(temp_audio_path)
                transcript_text = transcript_result["text"]
            
            if transcript_text:
                st.success("Transcription:")
                st.text_area("Converted Text:", transcript_text, height=120)

                # Summarization of Transcript
                final_summary = generate_summary(transcript_text, audio_summary_level)
                st.success("Summarized Speech:")
                st.text_area("Summary:", final_summary, height=100)
                st.download_button("Download Summary", final_summary, file_name="speech_summary.txt")
        except Exception as err:
            st.error(f"Error processing audio: {str(err)}")

    # Clean Up
    if temp_audio_path and os.path.exists(temp_audio_path):
        os.remove(temp_audio_path)

# === FILE SUMMARIZER ===
with sections[1]:
    st.subheader("📄 Upload a Document (.docx)")
    uploaded_doc = st.file_uploader("Select a Word file", type=["docx"])
    summary_type = st.radio("Select Summary Type:", ["Quick", "Standard", "Detailed"], horizontal=True)

    def extract_text(doc_file):
        try:
            doc = Document(doc_file)
            return "\n".join([p.text for p in doc.paragraphs if p.text])
        except:
            return None

    if uploaded_doc:
        doc_text = extract_text(uploaded_doc)
        if doc_text:
            st.text_area("Extracted Text:", doc_text, height=150)
            if st.button("Generate Summary"):
                summarized_output = generate_summary(doc_text, summary_type)
                st.success("Summarized Text:")
                st.text_area("Summary:", summarized_output, height=100)
                st.download_button("Download Summary", summarized_output, file_name="summary.txt")
        else:
            st.error("Unable to extract text from the document.")
