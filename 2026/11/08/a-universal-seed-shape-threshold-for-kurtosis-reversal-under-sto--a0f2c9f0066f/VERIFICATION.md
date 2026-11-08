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

Execute `python3 verify.py` using Python 3's standard library. It performs 577 exact-rational and finite numerical diagnostic assertions. Its independent renewal quadrature verifies the first two nontrivial even stationary moments on six parameter triples against the direct stationary-generator recurrence. It also checks sign and zero predictions for representative parameter values.

The proof in `RESULT.md` establishes the full infinite-parameter result. Reproducible finite checks are not an independent proof or an independent scientific audit. No higher-moment, nonsymmetric-seed, or nonlinear-confinement assertion was tested.
