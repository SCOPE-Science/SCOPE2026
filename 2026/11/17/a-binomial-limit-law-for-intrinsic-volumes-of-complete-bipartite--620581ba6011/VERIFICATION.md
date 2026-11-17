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
# Reproducibility and scientific limits

Run `python k2q_intrinsic_verify.py` in a Python 3.10+ environment containing SymPy, NumPy, and SciPy. The script independently reconstructs the full ambient Euclidean incidence columns; enumerates edge subsets; forms exact integer Gram matrices; computes Gram determinants by the Bareiss algorithm; and groups each independent-subset parallelepiped by rank and squared volume. It compares all 4,445 enumerated cases for \(1\le q\le6\) with the claimed closed-form shell multiplicities. Optional numerical hull checks at \(q=2,3\) validate the top coefficient independently. Weighted binomial comparisons are sanity checks.

Only the displayed general combinatorial and probabilistic arguments establish the infinite family and Gaussian approximation. No formal theorem prover or external validation was used. This document records reproducibility; it makes no claim of an independent audit.
