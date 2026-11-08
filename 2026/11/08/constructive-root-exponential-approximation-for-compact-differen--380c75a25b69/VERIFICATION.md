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

# Reproduction and verification

The provided `check_differential_hilbert.py` is standalone Python 3 (standard library only). Executing it after extraction from this package prints exactly `DIFFERENTIAL_HILBERT_DYADIC_EXACT_OK 14947` when the finite tests pass.

The checker verifies exact rational finite geometric-remainder identities and factor expansions, the shell relative ratio, a normalized Bergman moment recurrence for selected rational weights, and sampled matrix entries. Finite sampled column sums are heuristic checks, not an exhaustion of infinitely many coordinates. The proof of the tail bound and the universal singular-value estimate are contained in `RESULT.md` and do not depend on finite computation.

Li–Zhou's normalized monomial formula and parameter threshold were read from the primary mathematical source arXiv:2610.05672, §§2–4. Beckermann–Townsend's finite Cauchy-matrix approximation theorem and Peláez–Seco's generalized-Hilbert class result were compared at their respective scope. The result is not independently validated; no external formal or expert certification is asserted.
