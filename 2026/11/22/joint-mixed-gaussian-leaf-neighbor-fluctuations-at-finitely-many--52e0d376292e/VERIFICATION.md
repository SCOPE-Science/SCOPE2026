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

Run `python3 verify.py` with Python 3's standard library. It performs exact rational transition and conditional moment checks for the marked-root process through size \(22\), independent weighted enumeration of complete preferential-attachment histories through eight vertices, and all nonleaf two-mark nonsimultaneity checks on those histories. It reports finite-size diagnostics of the ratio \(\mathbb E[(L-D/2)^2]/\mathbb E D\) at sizes \(50,150,350\), which approach \(1/4\).

The conditional transition probabilities and nonsimultaneous-increment identity are the only aspects subject to exhaustive finite checks. Infinitary positivity of the Yule limits, convergence of normalized predictable brackets, and stable multivariate Gaussian convergence are proven analytically in `RESULT.md`, not certified by the bounded experiment. Full historical priority and independent mathematical audit remain unverified.
