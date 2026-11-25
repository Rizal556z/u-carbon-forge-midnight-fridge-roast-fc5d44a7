# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/Rizal556z/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/Rizal556z/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

A one-line roast of a smart fridge that refuses to open after midnight, built for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on [make.fun](https://make.fun).

## The entry

> My fridge locks at midnight like the leftovers filed a restraining order — mate, I bought you, and I bought everything inside you.

## How it works

`main.py` (pure Python standard library, no network, no secrets) writes the roast to `/output/entry.txt` — exactly one line, 1–200 characters, validated by a gate in the program itself before writing.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
