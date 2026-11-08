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
# Reproducibility and scope

Run `python3 verify_max_degree.py` from the directory containing this file and `RESULT.md`. It performs exact rational state-space computations of individual and joint recruiter counts over small tree sizes, tests their normalization and negative-upper-tail correlation, and independently evaluates the closed saddle and frontier identities numerically. Observed output: `PASS: 11030 exact rational and numerical assertions`.

These finite calculations test the nonstandard dependence lemma on small examples and the algebraic parameter identities. The analytic proof in `RESULT.md`, including exponential tilting and concentration, establishes the asymptotic claims; no finite enumeration is presented as exhaustive over all tree sizes. Neither external expert review nor independent audit was performed. An inaccessible full primary manuscript leaves a documented priority risk.
