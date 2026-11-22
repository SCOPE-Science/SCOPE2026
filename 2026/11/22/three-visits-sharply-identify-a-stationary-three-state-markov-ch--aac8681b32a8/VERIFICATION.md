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

The result is proved by four exact steps: reconstruction of stationarity and diagonal transitions from one-state count moments; reconstruction of undirected stationary flows from three balanced node sums; reconstruction of pair products from count patterns of multiplicity \((2,1)\); and use of the one-dimensional circulation space on a triangle to leave only reversal. A strictly positive one-parameter family establishes minimality.

The accompanying `checker.py` is standalone, uses Python standard-library exact `fractions.Fraction` arithmetic, constructs a finite suite of rational stationary three-state flows, enumerates all three-position paths, reproduces the reconstruction equations, and checks both admissible reversal-related matrices. It also enumerates two-position paths to test the claimed sharpness example. Direct command: `python3 checker.py`.

Observed checker output: `PASS: 1368 exact-rational assertions`.

The finite checker cannot establish the all-chain statement, is not an exhaustive enumeration of three-state stochastic matrices, and does not constitute independent review. The proof in `RESULT.md` supplies the unrestricted quantifiers. No external validation or independent audit has been performed.
