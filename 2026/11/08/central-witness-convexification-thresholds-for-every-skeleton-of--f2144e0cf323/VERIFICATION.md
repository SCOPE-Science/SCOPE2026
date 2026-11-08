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

# Reproduction

Run `python verify.py` in a directory containing this file and the supplied standalone `verify.py`. Python 3 standard library is sufficient; no downloaded data or third-party dependencies are required. Expected output:

`VERIFY_OK 1380 exact rational instances; 350 centroid witness checks; support allocations and index minimizations`

The program independently enumerates coordinate subsets satisfying a unit-mass capacity requirement in small simplex products and compares them with the universal ceiling test, checks the center witness in nonconvex cases, and computes the separately stated finite threshold minimum. All arithmetic is exact through `fractions.Fraction`.

# Scope of verification

A finite computer run does not prove the all-dimensional theorem, and absence of a counterexample in a finite search is not an impossibility proof. The full mathematical proof is the barycentric support-budget argument and the largest-coordinate sum inequality in `RESULT.md`. Source-comparison and historical-priority conclusions are provisional; no independent audit or external certification has been performed.
