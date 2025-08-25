# WenetSpeech-Yue: A Large-scale Cantonese Speech Corpus with Multi-dimensional Annotation
[![arXiv](https://img.shields.io/badge/arXiv-Paper-COLOR.svg)]()  [![hf](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Dataset-yellow)]()  [![GitHub](https://img.shields.io/badge/GitHub-Repo-green)]()  
This is the official repository 👑 for the WenetSpeech-Yue dataset and the source code for WenetSpeech-Pipe speech data preprocessing pipeline.
<div align="center"><img width="800px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/WenetSpeech-Pipe.svg" /></div>

## Download

## Leaderboard
<table border="0" cellspacing="0" cellpadding="6">
  <tr>
    <th align="left" rowspan="2" style="width:200px;">Model</th>
    <th align="center" rowspan="2">#Params (M)</th>
    <th align="center" colspan="2">In-House</th>
    <th align="center" colspan="5">Open-Source</th>
    <th align="center" colspan="2">WSYue-ASR-eval</th>
  </tr>
  <tr>
    <th align="center">Dialogue</th>
    <th align="center">Reading</th>
    <th align="center">yue</th>
    <th align="center">zh-HK</th>
    <th align="center">MDCC</th>
    <th align="center">Daily_Use</th>
    <th align="center">Commands</th>
    <th align="center">Short</th>
    <th align="center">Long</th>
  </tr>

  <tr><td align="left" colspan="11"><b>w/o LLM</b></td></tr>

  <tr bgcolor="#f2f2f2">
    <td align="left">Paraformer</td><td align="center">220</td><td align="center">83.22</td><td align="center">51.97</td><td align="center">70.16</td><td align="center">68.49</td><td align="center">47.67</td><td align="center">79.31</td><td align="center">69.32</td><td align="center">73.64</td><td align="center">89.00</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">SenseVoice-small</td><td align="center">234</td><td align="center">21.08</td><td align="center"><u>6.52</u></td><td align="center">8.05</td><td align="center"><b>7.34</b></td><td align="center">6.34</td><td align="center">5.74</td><td align="center"><u>6.65</u></td><td align="center">6.69</td><td align="center">9.95</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">Dolphin-small</td><td align="center">372</td><td align="center">59.20</td><td align="center">7.38</td><td align="center">39.69</td><td align="center">51.29</td><td align="center">26.39</td><td align="center">7.21</td><td align="center">9.68</td><td align="center">32.32</td><td align="center">58.20</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td align="left"><b>U2pp-Conformer-Yue</b></td><td align="center">130</td><td align="center"><b>16.57</b></td><td align="center">7.82</td><td align="center">7.72</td><td align="center">11.42</td><td align="center">5.73</td><td align="center">5.73</td><td align="center">8.97</td><td align="center"><u>5.05</u></td><td align="center">8.89</td>
  </tr>

  <tr bgcolor="#f2f2f2">
    <td align="left">TeleASR</td><td align="center">700</td><td align="center">37.18</td><td align="center">7.27</td><td align="center">7.02</td><td align="center"><u>7.88</u></td><td align="center">6.25</td><td align="center">8.02</td><td align="center"><b>5.98</b></td><td align="center">6.23</td><td align="center">11.33</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">Whisper-medium</td><td align="center">769</td><td align="center">75.50</td><td align="center">68.69</td><td align="center">59.44</td><td align="center">62.50</td><td align="center">62.31</td><td align="center">64.41</td><td align="center">80.41</td><td align="center">80.82</td><td align="center">50.96</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td align="left"><b>Whisper-medium-Yue</b></td><td align="center">769</td><td align="center">18.69</td><td align="center">6.86</td><td align="center"><u>6.86</u></td><td align="center">11.03</td><td align="center"><u>5.49</u></td><td align="center"><u>4.70</u></td><td align="center">8.51</td><td align="center"><u>5.05</u></td><td align="center"><u>8.05</u></td>
  </tr>

  <tr bgcolor="#f2f2f2">
    <td align="left">FireRedASR-AED-L</td><td align="center">1100</td><td align="center">73.70</td><td align="center">18.72</td><td align="center">43.93</td><td align="center">43.33</td><td align="center">34.53</td><td align="center">48.05</td><td align="center">49.99</td><td align="center">55.37</td><td align="center">50.26</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">Whisper-large-v3</td><td align="center">1550</td><td align="center">45.09</td><td align="center">15.46</td><td align="center">12.85</td><td align="center">16.36</td><td align="center">14.63</td><td align="center">17.84</td><td align="center">20.70</td><td align="center">12.95</td><td align="center">26.86</td>
  </tr>

  <tr><td align="left" colspan="11"><b>w/ LLM</b></td></tr>

  <tr bgcolor="#f2f2f2">
    <td align="left">Qwen2.5-Omni-3B</td><td align="center">3000</td><td align="center">72.01</td><td align="center">7.49</td><td align="center">12.59</td><td align="center">11.75</td><td align="center">38.91</td><td align="center">10.59</td><td align="center">25.78</td><td align="center">67.95</td><td align="center">88.46</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">Kimi-Audio</td><td align="center">7000</td><td align="center">68.65</td><td align="center">24.34</td><td align="center">40.90</td><td align="center">38.72</td><td align="center">30.72</td><td align="center">44.29</td><td align="center">45.54</td><td align="center">50.86</td><td align="center">33.49</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td align="left">FireRedASR-LLM-L</td><td align="center">8300</td><td align="center">73.70</td><td align="center">18.72</td><td align="center">43.93</td><td align="center">43.33</td><td align="center">34.53</td><td align="center">48.05</td><td align="center">49.99</td><td align="center">49.87</td><td align="center">45.92</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td align="left"><b>U2pp-Conformer-LLM-Yue</b></td><td align="center">4200</td><td align="center"><u>17.22</u></td><td align="center"><b>6.21</b></td><td align="center"><b>6.23</b></td><td align="center">9.52</td><td align="center"><b>4.35</b></td><td align="center"><b>4.57</b></td><td align="center">6.98</td><td align="center"><b>4.73</b></td><td align="center"><b>7.91</b></td>
  </tr>
</table>








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
