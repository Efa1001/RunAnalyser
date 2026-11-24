# Run Analyser

A Python script that analyses my own running data: 100 km logged kilometre by kilometre over 28 runs (Oct–Nov 2026).

## What it does
Reads `data.csv` and prints:
- Fastest and slowest kilometre, and average pace
- Average pace grouped by listening (music / podcast / silence), weather, time of day and energy level

## How to run
python3 run_analyser.py

## Findings
- **Podcast runs were the fastest:** 5.83 min/km, about 20–23 s/km faster than music or silence.
- **Energy matters:** energy-5 km averaged 6.02 min/km vs 6.28 at energy 3 (about 16 s/km faster).
- **Rain slowed me down:** 6.18 min/km in rain vs 6.03 in sun (about 9 s/km).
- **Fastest km:** 5:19, on 22 Oct, listening to a podcast.

**Caveat:** podcast runs were mostly sunny, high-energy mornings, so these are correlations, not proof of cause.

## What I learned
- Reading and parsing a CSV without libraries
- Writing one reusable `group_by(column)` function instead of repeating code
- Converting pace strings like `6:10` into numbers I can average

## Next steps
- Charts with matplotlib