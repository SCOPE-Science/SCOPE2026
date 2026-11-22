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

# Reproducibility

Run `python3 verify_nor_seam.py` with Python 3.10 or newer; no third-party modules or inputs are required. The accompanying `verification_output.txt` is the actual recorded output from that program.

The program constructs a local 16-state transfer for total domination using pairwise adjacent rung states, and also constructs a row-swap seam involution. It compares ordinary and twisted matrix trace counts with the independent cubic-root-sum recurrences for integer rungs 3 through 40. Additionally it constructs both labelled graphs directly, evaluates all binary configurations on each graph for 3 through 9 rungs, checks the universal two-cycle basin against matrix counts, and verifies \(F^3=F\) on every enumerated configuration. This amounts to \(\sum_{n=3}^9 2\cdot4^n=699{,}008\) individually checked configurations (count calculated from the specified loops).

Checks are finite. The proof of generality, parity decomposition, and irrational rotation is in `RESULT.md`. The code does not mathematically certify Galois or asymptotic arguments by itself. No external independent audit has been undertaken.
