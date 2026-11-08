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
# Finite reproducibility checks

Execute `python3 verify.py` using Python 3.9 or later and no third-party packages.

The code compares three independently implemented representations: (i) direct sets of distinct subsequences of the alternating host, (ii) two-state transfer polynomial coefficients, and (iii) positive run-composition binomial sums. It additionally checks the claimed support threshold, full-class saturation, total unweighted ball size, and parity-skew formula.

Observed successful run: direct-set fixed-weight comparisons **1,122** (all host lengths up to 17), independent transfer/run coefficient tables **64** (all output lengths up to 64), total-count checks **2,336**, and parity/support comparisons **100,096**. No randomness or external package is used. Computational tests address finite instances only; the infinite statements are established by the argument in `RESULT.md`.

The proof and verifier concern the left-phase alternating word beginning with zero; complementing the source exchanges zero and one weights. Independent audit has not been performed.
