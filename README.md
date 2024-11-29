# easy-use-kenlm
How to use KenLM with SentencePiece Tokenizer(Unigram Tokenizer)

## Setup

- Installing sentencepiece: `pip install sentencepiece`
- Installing kenlm:
    - Refer to [link](https://github.com/kpu/kenlm/blob/master/BUILDING)
    - Make sure you install dependencies
- Locate `bin` directory of kenlm build to the `routine.sh` script

## Howto

- Per experiment directory, place `doc.txt` file that contains lines to train tokenizer and lm model.
- The script will return `sp.model` for tokenizer and `encoded.bin` for lm model.
