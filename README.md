# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/4orky/deadpan-forecasts/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/4orky/deadpan-forecasts/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

A program that writes one deadpan weather forecast for a city that does
not exist — one line, at most 160 characters — to `/output/entry.txt`.

Entry for the [Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) bounty on [make.fun](https://make.fun).

## How it works

`main.py` holds 12 hand-written candidate forecasts, each scored 0–10 on
the judge's five criteria in order of weight (on-topic forecast, funnier,
more vivid, believable broadcast tone, good use of characters). The
highest total wins; ties go to the shorter text. The winning line went
through a real second-pass revision: its draft tail ("Flooding is not
expected; falling is.") was grammatically strained, so it was replaced
with official advice to stay grounded — same deadpan register, a second
quiet pun, and a landing on advice rather than a wobble.

The winning forecast (149 characters):

> In Flotsam, rain falls upward at 30 miles per hour after midnight, so hold your umbrella underneath you. Officials advise residents to stay grounded.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with `OUTPUT_PATH`), then reads it
back and verifies it byte-for-byte, printing the character count, the
craft score and the SHA-256 of the output. Running it twice produces
identical bytes.

## License

MIT — see [LICENSE](LICENSE).
