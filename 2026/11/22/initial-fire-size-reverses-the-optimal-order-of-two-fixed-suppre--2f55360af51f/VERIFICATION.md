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

## Exact proof checks
The mathematical identity is obtained by calculating the two transient generators, their exact commutator, and the two-by-two Cayley–Hamilton decomposition of both semigroups. The discriminant \((\lambda+m-d)^2+4\lambda(d+s)\) is strictly positive for every positive birth and natural-death rate, ensuring that the semigroup coefficient \(b_s(t)\) is strictly positive at each positive duration. The final sign therefore depends only on the initial mixture and the difference of natural death rates. The proof also classifies equality and the single-transient-state limit.

## Reproduction
Run `python verify.py` in an environment with NumPy, SciPy and SymPy installed. The checker uses direct symbolic identities and numerical matrix exponentials for 1,800 deterministic-seed positive-parameter trials. Its completed run reported `PASSED 7208 checks; exemplar survival differences [-0.007741914776, 0.007741914776].` These are reproducibility diagnostics, not an exhaustive test of the universal theorem.

## Remaining limitations
The death hazards, fixed suppression episodes, hard capacity of two, absorbing extinction, and finite terminal deadline are necessary to the stated claim. The calculation is not a field validation, does not optimize total burned area, and does not justify late deployment in practice. Historical literature priority is provisional.
