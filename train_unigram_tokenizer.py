import sentencepiece as spm
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--fpath", type=str, default="doc.txt")
parser.add_argument("--vocab_size", type=int, default=65536) # vocab size that ccnet uses
parser.add_argument("--model_prefix", type=str, default="sp")
parser.add_argument("--experiment", type=str, default="trial")
args = parser.parse_args()

fpath = args.fpath
vocab_size = args.vocab_size
model_prefix = args.model_prefix
experiment = args.experiment

fpath = f"{experiment}/{fpath}"
model_prefix = f"{experiment}/{model_prefix}"
encoded_fpath = f"{experiment}/encoded.txt"

spm.SentencePieceTrainer.train(input=fpath, model_prefix=model_prefix, vocab_size=vocab_size)

model = spm.SentencePieceProcessor(model_file=f"{model_prefix}.model")
with open(encoded_fpath, "w") as fout:
    with open(fpath, "r") as fin:
        content = fin.read()
        for line in content.split("\n"):
            if not line:
                continue
            encoded = model.encode(line, out_type=str)
            fout.write(" ".join(encoded))
            fout.write("\n")
