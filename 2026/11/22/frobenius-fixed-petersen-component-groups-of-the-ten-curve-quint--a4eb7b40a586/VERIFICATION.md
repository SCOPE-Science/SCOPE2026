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

# Exact verification and limits

Run `python verify_petersen_frobenius.py` using Python 3 and no third-party dependencies. The certificate reconstructs the Petersen graph, checks all fifteen edges, computes the exact reduced determinant 2000, verifies an explicit integral inverse multiple, verifies descent of the five-label permutation actions to the quotient, and establishes all fourteen augmented ranks. Its observed final marker was `PETERSEN_FROBENIUS_COMPONENT_GROUPS_EXACT_OK`.

Run `python verify_petersen_enumeration.py` using Python 3 and SymPy. It independently enumerates all 2000 elements of the reduced critical group through a Hermite normal form transversal, computes each permutation's fixed classes and their two- and five-annihilators, and obtains all seven stated groups. Its observed final marker was `PETERSEN_FROBENIUS_HERMITE_ENUMERATION_OK`.

This finite exact proof establishes the group classification, not the existence of arbitrary smoothings. The arithmetic Néron interpretation additionally invokes classical semistable component-group theory with thickness one; no independent mathematical audit is claimed.
