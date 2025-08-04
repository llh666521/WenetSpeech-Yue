import re
import argparse
from opencc import OpenCC
from tqdm import tqdm
import cn2an
import pangu

cc = OpenCC('t2s')

def an2cn(text):
    text = cn2an.transform(text, "an2cn")
    return text

def remove_punctuation(text):
    text = re.sub(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])', r'\1\2', text)
    text = re.sub(r'(?<![a-zA-Z])\s+(?![a-zA-Z])', '', text)
    text = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5' ]", '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'([\u4e00-\u9fa5])\s+([a-zA-Z0-9])', r'\1\2', text)
    text = re.sub(r'([a-zA-Z0-9])\s+([\u4e00-\u9fa5])', r'\1\2', text)
    return text

def remove_sensevoice_tags(text):
    # Remove all <|...|> tags
    return re.sub(r'<\|.*?\|>', '', text)

def normalize_text(text):
    text = remove_sensevoice_tags(text)
    text = cc.convert(text)
    text = an2cn(text)
    text = remove_punctuation(text)
    text = text.upper()
    text = pangu.spacing(text)
    return text

def main():
    parser = argparse.ArgumentParser(description='Text normalization script')
    parser.add_argument('--input', required=True, help='Input file path')
    parser.add_argument('--output', required=True, help='Output file path')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()

    with open(args.output, 'w', encoding='utf-8') as fout:
        for line in tqdm(lines, desc="Processing"):
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                uid, text = parts
                text = normalize_text(text)
                fout.write(f"{uid} {text}\n")
