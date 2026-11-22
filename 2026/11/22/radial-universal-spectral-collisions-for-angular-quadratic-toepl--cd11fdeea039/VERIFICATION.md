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

# Verification record

Analytical steps checked from the explicit proof: the unit-sphere factorial moment identity and cancellation of radial moments; the \(d+3\) operator normalization including diagonal \(\operatorname{tr}A\); triangularization and induced symmetric-power eigenvalues without assuming normality; the unique occupation normal form for coprime \(p,q\); exact first collision and the generating series in every distinct-eigenvalue case.

Run `python check.py` from the extracted package. It finished successfully with `PASS: 4499 finite exact assertions; not an infinite proof`, testing exact spherical moment ratios, 3-by-3 nonnormal matrices, complete small coprime primitive parameters, and Jordan/repeated-eigenvalue sanity checks. The checker uses Python and SymPy and does not depend on files from another record.

Finite testing cannot rule out an undiscovered historical equivalent or substitute for the displayed infinite proof. No independent audit or independent validation has been performed.
