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

# Reproducibility

The proof uses 2-adic valuation identities and residue-class counting. It does not require an external computer algebra system.

Run `python3 check_factors.py` to generate the period-doubling prefix by direct substitution, enumerate all length-e·m factors for dyadic block lengths m=1 through 256 and exponents e=2 through 5, compare actual Abelian-power sets against all rotations of the prescribed ordinary powers, and check a non-dyadic Abelian fourth-power counterexample. This is finite verification.

Run `python3 check_arithmetic.py` to derive the same word independently from exact 2-adic valuations and verify that moving 2^k positions changes at most one bit for k=0 through 10, with Parikh equivalence exactly equivalent to word equality for tested adjacent pairs and starting positions.

Both scripts were executed successfully in the preparation environment. Neither script is an all-length proof: the full unbounded result is proved in the accompanying mathematical text. Independent external validation has not been performed.
