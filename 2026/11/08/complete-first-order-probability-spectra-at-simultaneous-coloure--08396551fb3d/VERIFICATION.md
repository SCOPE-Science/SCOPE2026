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

# Verification and scope

The independently executable standard-library file `checker.py` verifies 312 exact one-colour falling-factorial moment identities and 3168 product identities for two independent colours. It compares two finite-size rare-fibre mean values with their predicted Poisson intensity, documenting slow finite-size convergence for positive occupancy levels; finite checks are **not** proof of limiting laws or all first-order sentences.

The analytic proof in `RESULT.md` establishes the exact moment formula, the joint Poisson limit, the abundance/vanishing of other finite fibre sizes, negligible multicolour low-fibre collisions, a deterministic rank-bounded Ehrenfeucht–Fraïssé invariant, and the converse first-order definability of each capped-Poisson event. All assumptions and unproved extensions are specified there.

Run `python3 checker.py`. The expected success marker is `CRITICAL_COLOURED_FIBRE_CHECKS_OK`.

Independent audit was not performed.
