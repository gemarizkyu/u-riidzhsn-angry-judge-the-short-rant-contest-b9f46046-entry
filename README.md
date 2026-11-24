# Angry Judge: The Short Rant Contest

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](main.py)

Entry for the make.fun bounty
[Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).

## What it does

`main.py` writes one short, funny, original rant about an everyday
annoyance — a self-checkout accusing a shopper of smuggling a goose over
one bag of rice — to `/output/entry.txt`.

The rant is 332 characters, inside the competition's 1–400 character gate.

## How it works

- The rant is a fixed original text stored in `main.py`; the program is
  fully deterministic — no clock, no randomness, no network, no model
  calls, nothing read from outside the repository.
- `main.py` validates the text (non-empty, at most 400 characters, no
  leading/trailing whitespace), creates `/output` if needed, and writes
  exactly the rant, with no trailing newline.

## Run it

```sh
python3 main.py
# wrote 332 characters to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
