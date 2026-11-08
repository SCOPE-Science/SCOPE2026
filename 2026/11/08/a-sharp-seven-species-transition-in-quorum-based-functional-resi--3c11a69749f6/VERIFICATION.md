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

# Exact verification instructions

Execute `python3 verify.py` with Python 3.8 or newer. The script uses only the standard library and reconstructs both the guild reliability polynomials and the independent survivor-subset distributions through seven species. It verifies the three factorizations needed for the sharp lower-bound and crossover proof and checks the sign/exponent inequalities for 294 larger integer budgets.

The bounded numerical checks do not certify the infinite-budget statement. The proof there uses six explicit polynomial identities in the residue of the species count modulo six and an asymptotic exponent comparison. All assumptions require independent equal-probability survival and disjoint guilds; no statement about heterogeneous risks or correlated losses has been checked.
