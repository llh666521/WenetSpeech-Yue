# WenetSpeech-Yue: A Large-scale Cantonese Speech Corpus with Multi-dimensional Annotation
[![arXiv](https://img.shields.io/badge/arXiv-Paper-COLOR.svg)]()  [![hf](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Dataset-yellow)]()  [![GitHub](https://img.shields.io/badge/GitHub-Repo-green)]()  
This is the official repository 👑 for the WenetSpeech-Yue dataset and the source code for WenetSpeech-Pipe speech data preprocessing pipeline.
<div align="center"><img width="800px" src="https://github.com/llh666521/WenetSpeech-Yue/blob/main/figs/WenetSpeech-Pipe.svg" /></div>

## Download

## Leaderboard
<table border="1" cellspacing="0" cellpadding="4">
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">#Params (M)</th>
    <th colspan="2">In-House</th>
    <th colspan="5">Open-Source</th>
    <th colspan="2">WSYue-ASR-eval</th>
  </tr>
  <tr>
    <th>Dialogue</th>
    <th>Reading</th>
    <th>yue</th>
    <th>zh-HK</th>
    <th>MDCC</th>
    <th>Daily_Use</th>
    <th>Commands</th>
    <th>Short</th>
    <th>Long</th>
  </tr>

  <!-- w/o LLM -->
  <tr><td colspan="11"><b>w/o LLM</b></td></tr>

  <tr bgcolor="#f2f2f2">
    <td>Paraformer</td><td>220</td><td>83.22</td><td>51.97</td><td>70.16</td><td>68.49</td><td>47.67</td><td>79.31</td><td>69.32</td><td>73.64</td><td>89.00</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>SenseVoice-small</td><td>234</td><td>21.08</td><td><u>6.52</u></td><td>8.05</td><td><b>7.34</b></td><td>6.34</td><td>5.74</td><td><u>6.65</u></td><td>6.69</td><td>9.95</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>Dolphin-small</td><td>372</td><td>59.20</td><td>7.38</td><td>39.69</td><td>51.29</td><td>26.39</td><td>7.21</td><td>9.68</td><td>32.32</td><td>58.20</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td><b>U2pp-Conformer-Yue</b></td><td>130</td><td><b>16.57</b></td><td>7.82</td><td>7.72</td><td>11.42</td><td>5.73</td><td>5.73</td><td>8.97</td><td><u>5.05</u></td><td>8.89</td>
  </tr>

  <tr bgcolor="#f2f2f2">
    <td>TeleASR</td><td>700</td><td>37.18</td><td>7.27</td><td>7.02</td><td><u>7.88</u></td><td>6.25</td><td>8.02</td><td><b>5.98</b></td><td>6.23</td><td>11.33</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>Whisper-medium</td><td>769</td><td>75.50</td><td>68.69</td><td>59.44</td><td>62.50</td><td>62.31</td><td>64.41</td><td>80.41</td><td>80.82</td><td>50.96</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td><b>Whisper-medium-Yue</b></td><td>769</td><td>18.69</td><td>6.86</td><td><u>6.86</u></td><td>11.03</td><td><u>5.49</u></td><td><u>4.70</u></td><td>8.51</td><td><u>5.05</u></td><td><u>8.05</u></td>
  </tr>

  <tr bgcolor="#f2f2f2">
    <td>FireRedASR-AED-L</td><td>1100</td><td>73.70</td><td>18.72</td><td>43.93</td><td>43.33</td><td>34.53</td><td>48.05</td><td>49.99</td><td>55.37</td><td>50.26</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>Whisper-large-v3</td><td>1550</td><td>45.09</td><td>15.46</td><td>12.85</td><td>16.36</td><td>14.63</td><td>17.84</td><td>20.70</td><td>12.95</td><td>26.86</td>
  </tr>

  <!-- w/ LLM -->
  <tr><td colspan="11"><b>w/ LLM</b></td></tr>

  <tr bgcolor="#f2f2f2">
    <td>Qwen2.5-Omni-3B</td><td>3000</td><td>72.01</td><td>7.49</td><td>12.59</td><td>11.75</td><td>38.91</td><td>10.59</td><td>25.78</td><td>67.95</td><td>88.46</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>Kimi-Audio</td><td>7000</td><td>68.65</td><td>24.34</td><td>40.90</td><td>38.72</td><td>30.72</td><td>44.29</td><td>45.54</td><td>50.86</td><td>33.49</td>
  </tr>
  <tr bgcolor="#f2f2f2">
    <td>FireRedASR-LLM-L</td><td>8300</td><td>73.70</td><td>18.72</td><td>43.93</td><td>43.33</td><td>34.53</td><td>48.05</td><td>49.99</td><td>49.87</td><td>45.92</td>
  </tr>
  <tr bgcolor="#d9ead3">
    <td><b>U2pp-Conformer-LLM-Yue</b></td><td>4200</td><td><u>17.22</u></td><td><b>6.21</b></td><td><b>6.23</b></td><td>9.52</td><td><b>4.35</b></td><td><b>4.57</b></td><td>6.98</td><td><b>4.73</b></td><td><b>7.91</b></td>
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
