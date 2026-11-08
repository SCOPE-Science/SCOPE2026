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

Run `python3 checker.py` with Python 3.9 or later from this directory. No third-party dependencies are needed. The code enumerates every Prüfer sequence on \(n=2,3,4,5\), all thresholds \(2\le h\le n\), every edge cut, and each retained-edge bond state; checks componentwise minimization of all exact integer coefficients for at least one edge; checks the complete five-edge six-vertex risk polynomials against exact rational coefficients; and checks the algebraic differences and boundary point at \(p=3/5\). Expected counts for the exhaustive smaller-tree/threshold cases are \(1,6,48,500\), respectively.

The source provides reproducible *finite* exhaustive certificates and exact symbolic identities. It is not a proof about all larger trees, about general dependent-edge SIR transmission, or about empirical intervention impact. All analytic inferences from the coefficients, including positivity and uniqueness of the crossing, are given in `RESULT.md`. No independent audit has been performed.
