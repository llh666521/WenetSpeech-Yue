# WenetSpeech-Yue: A Large-scale Cantonese Speech Corpus with Multi-dimensional Annotation
[![arXiv](https://img.shields.io/badge/arXiv-Paper-COLOR.svg)]()  [![hf](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Dataset-yellow)]()  [![GitHub](https://img.shields.io/badge/GitHub-Repo-green)]()  
This is the official repository 👑 for the WenetSpeech-Yue dataset and the source code for WenetSpeech-Pipe speech data preprocessing pipeline.
<div align="center"><img width="800px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/WenetSpeech-Pipe.svg" /></div>

## Download

## Leaderboard

## Dataset
### WenetSpeech-Yue Overview
* Contains 21,800 hours of large-scale Cantonese speech corpus with rich annotations, the largest open-source resource for Cantonese speech research.
* Stores metadata in a single JSON file, including audio path, duration, text confidence, speaker identity, SNR, DNSMOS, age, gender, and character-level timestamps. Additional metadata tags may be added in the future.
* Covers ten domains: Storytelling, Entertainment, Drama, Culture, Vlog, Commentary, Education, Podcast, News, and Others.
<div align="center"><img width="800px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/data_distribution.png" /></div>

## Benchmark
### ASR Benchmark

### TTS Benmark

## WenetSpeech-Pipe
### Audio Collection
Audio Collection includes domain definition, audio crawling and VAD.
### Speaker Attribute Annotation
Speaker Attribute Annotation includes speaker diarization, age and gender annotation.
### Speech Quality Annotation
Speech Quality Annotation includes bandwidth detection, SNR and MOS prediction. 
### Automatic Speech Recognition
We select three models with the best performance on Cantonese to perform multi-system labeling: SenseVoice, TeleASR, and Whisper. For each audio file, we obtain the corresponding multi-system transcription.
### Text Postprocessing
Each ASR transcription system produces outputs in different formats. To standardize these formats, we introduce a text post-processing module, which includes punctuation removal, traditional-to-simplified Chinese conversion, and text normalization. The detailed code can be found in `text_postprocessing.py`.
<div align="center"><img width="300px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/text_processing.svg" /></div>

### Recognizer Output Voting
<div align="center"><img width="500px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/LLM_Corrector.svg" /></div>
