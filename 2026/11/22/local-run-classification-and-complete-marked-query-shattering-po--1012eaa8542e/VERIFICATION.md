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
# Verification

Run `python check_cycle_marks.py` using Python 3 standard library. The checker independently generates all proper three-colourings on every cycle of orders three through eight, enumerates all supports containing at most one query per vertex, and compares the *complete set* of binary traces to the run classification. Separately, it counts every valid marked support via the closed binomial sum and compares coefficients. The saved output in `checks_output.txt` terminates with `ALL_MARKED_CYCLE_CHECKS_PASS`. The formula's highest nonzero degree is also checked for each order nine through forty, and the alternating-position maximal-face corollary is checked for even cycle orders six through twelve.

The package paths are self-contained; there are no external input files. Universal correctness relies on the extension lemma, the forbidden-run witness and the rooted cyclic enumeration proved in RESULT.md. Exhaustive tests at finite orders do not certify universality or independent mathematical correctness. The closest published dimension theorems were inspected as scientific comparisons, not mechanically reproduced. The alternating-position maximal-face claim follows from the local obstruction and the standard three-colour cycle chromatic polynomial.
