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

# Verification and reproducibility

The complete proof of the infinite claim is in RESULT.md. It uses a Fourier-orbit covering argument on the rigidity side and an explicitly constructed two-sided Riesz product on the nonrigidity side. The strict frequency separation is controlled by \(\log(eta/(eta-2))\), with \(p\) an even positive integer; equality for closed intervals is handled only on the rigidity side. Independence, ergodicity, and higher-dimensional assertions have not been established.

The accompanying `verify.py` checks one concrete cat-map instance with 2,186 nonzero signed-frequency combinations of seven consecutive indices. It uses high-precision mpmath and exact integer matrix arithmetic. Passing finite tests does not certify an unbounded Fourier construction; those steps are justified analytically in RESULT.md. No external proof checker or independent audit has been performed.
