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

# Reproducibility and verification

The exact proof is in `RESULT.md`; `CHECK.py` uses only Python's `fractions.Fraction` and `math` modules. Execute `python3 CHECK.py` in the extracted artifact directory. It prints `PASS: 3867 exact arithmetic and endpoint checks`. The tests check the ellipse-moment identities, strict positivity of the degree-two variance, quartic coefficient reduction, sharp nonnegative sum-of-squares formula for both phases, interiority, and the rational critical configuration \((\alpha,R)=(2/3,3/2)\). The final numeric check concerns the decimal presentation of the unweighted ellipse threshold.

Exact arithmetic checks over finite rational examples are not infinite proofs; the analytic universal argument uses positivity of coefficients, the sign of the unique positive root of the threshold quadratic, and two explicit polynomial square identities. No external or independent mathematical audit was performed.
