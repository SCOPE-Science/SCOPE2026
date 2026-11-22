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

Run `python3 verify_infinity.py` from the same directory. It uses standard Python 3 only and checks admissible values of the parameters, the absence of support points on or below the two prescribed Newton edges, the proposed genus and delta identities, and both conductor orders and canonical-degree formulas. It checks 35 cases across seven odd primes and five values of the family parameter, including exact worked examples at \((p,n)=(3,2)\) and \((5,2)\). Successful execution prints `VERIFY_OK`.

The general proof is the symbolic valuation, Newton polygon and adjunction calculation in `RESULT.md`. This script cannot test infinitely many pairs or substitute for the proof of irreducibility, tame Newton-Puiseux uniqueness, or the geometric conductor formula. Maximality of the smooth normalization is cited from the initiating source, and no independent external validation is asserted.
