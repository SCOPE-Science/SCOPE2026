---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational reproducibility and limits

Run `python3 check_chord.py` and `python3 check_field4.py` in a directory containing both files, using Python 3.9 or later and no third-party libraries.

`check_chord.py` constructs each chorded cube independently from bit-labelled vertices, checks ranks of successive matrix powers and fixed spaces for dimensions three to seven and every chord distance, then exhaustively evolves all binary configurations for dimensions three and four. The required checks all passed.

`check_field4.py` uses the two-dimensional binary representation of the additive group of `F4` to exhaustively evolve all 65,536 configurations for each of the two nonedge distances in dimension three. It checks the full least-period population; both cases passed.

The proof in `RESULT.md` supplies the infinite-family argument and explains the limits `d>=3`, one nonedge, characteristic two. Exhaustive tests are finite supporting checks; they neither prove an infinite theorem independently nor assess historical priority.
