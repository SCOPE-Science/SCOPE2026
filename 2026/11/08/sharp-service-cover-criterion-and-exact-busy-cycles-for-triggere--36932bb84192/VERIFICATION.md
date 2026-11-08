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

# Verification details and limits

The source package includes standalone `verify.py` using Python 3 standard-library exact rational arithmetic. The script creates 700 independently seeded finite arrival-cluster configurations, each of which satisfies the cumulative service-cover criterion. It compares the exact busy intervals with those of the simultaneously batched queue. It also checks equality at the single-trigger boundary, strict failure beyond the boundary, a multitrigger example whose last trigger exceeds the primary service time, and Borel probability normalization and mean at four subcritical traffic intensities. Expected printed output: `711 checks passed: exact rational busy/idle coupling, sharpness, Borel normalization/mean`.

These finitely many checks cannot establish the all-schedule pathwise statement or the Poisson limit. The proof instead relies on the deterministic isolated-cluster criterion, the absence of pending jobs at clearing times, and classical Poisson busy-period branching. The probabilities and transform require the independence, finiteness and subcriticality hypotheses in the theorem. Historical priority, independent proof review and independent computational validation have not been performed.
