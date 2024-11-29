#!/bin/bash

kenlm_path=/home/s7/chanwoopark/korean-cc/kenlm/build/bin
PATH=$kenlm_path:$PATH

mode=$1
if [ -z "$mode" ]; then
    mode=trial
fi

python train_unigram_tokenizer.py \
    --experiment $mode \

lmplz -o 5 < $mode/encoded.txt > $mode/encoded.arpa

build_binary $mode/encoded.arpa $mode/encoded.bin

ls -alh $mode