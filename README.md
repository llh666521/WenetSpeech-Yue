# WenetSpeech-Yue: A Large-scale Cantonese Speech Corpus with Multi-dimensional Annotation
[![arXiv](https://img.shields.io/badge/arXiv-Paper-COLOR.svg)]()  [![hf](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Dataset-yellow)]()  [![GitHub](https://img.shields.io/badge/GitHub-Repo-green)]()  
This is the official repository 👑 for the WenetSpeech-Yue dataset and the source code for WenetSpeech-Pipe speech data preprocessing pipeline.
<div align="center"><img width="800px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/WenetSpeech-Pipe.svg" /></div>

## Download

## Leaderboard
| Model                      | #Params (M) |   In-House   |         |       Open-Source        |       |       |          |          |   WSYue-ASR-eval   |        |
|----------------------------|-------------|--------------|---------|--------------------------|-------|-------|----------|----------|--------------------|--------|
|                            |             | Dialogue     | Reading | yue                      | zh-HK | MDCC  | Daily_Use| Commands | Short              | Long   |
| **w/o LLM**                |             |              |         |                          |       |       |          |          |                    |        |
| Paraformer~[1]             | 220         | 83.22        | 51.97   | 70.16                    | 68.49 | 47.67 | 79.31    | 69.32    | 73.64              | 89.00  |
| SenseVoice-small~[2]       | 234         | 21.08        | __6.52__| 8.05                     | **7.34** | 6.34 | 5.74    | __6.65__ | 6.69               | 9.95   |
| Dolphin-small~[3]          | 372         | 59.20        | 7.38    | 39.69                    | 51.29 | 26.39 | 7.21     | 9.68     | 32.32              | 58.20  |
| **U2pp-Conformer-Yue**     | 130         | **16.57**    | 7.82    | 7.72                     | 11.42 | 5.73  | 5.73     | 8.97     | __5.05__           | 8.89   |
| TeleASR~[4]                | 700         | 37.18        | 7.27    | 7.02                     | __7.88__ | 6.25 | 8.02    | **5.98** | 6.23               | 11.33  |
| Whisper-medium~[5]         | 769         | 75.50        | 68.69   | 59.44                    | 62.50 | 62.31 | 64.41    | 80.41    | 80.82              | 50.96  |
| **Whisper-medium-Yue**     | 769         | 18.69        | 6.86    | __6.86__                 | 11.03 | __5.49__ | __4.70__ | 8.51     | __5.05__           | __8.05__ |
| FireRedASR-AED-L~[6]       | 1100        | 73.70        | 18.72   | 43.93                    | 43.33 | 34.53 | 48.05    | 49.99    | 55.37              | 50.26  |
| Whisper-large-v3~[5]       | 1550        | 45.09        | 15.46   | 12.85                    | 16.36 | 14.63 | 17.84    | 20.70    | 12.95              | 26.86  |
| **w/ LLM**                 |             |              |         |                          |       |       |          |          |                    |        |
| Qwen2.5-Omni-3B~[7]        | 3000        | 72.01        | 7.49    | 12.59                    | 11.75 | 38.91 | 10.59    | 25.78    | 67.95              | 88.46  |
| Kimi-Audio~[8]             | 7000        | 68.65        | 24.34   | 40.90                    | 38.72 | 30.72 | 44.29    | 45.54    | 50.86              | 33.49  |
| FireRedASR-LLM-L~[6]       | 8300        | 73.70        | 18.72   | 43.93                    | 43.33 | 34.53 | 48.05    | 49.99    | 49.87              | 45.92  |
| **U2pp-Conformer-LLM-Yue** | 4200        | __17.22__    | **6.21**| **6.23**                 | 9.52  | **4.35** | **4.57** | 6.98     | **4.73**           | **7.91** |


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
