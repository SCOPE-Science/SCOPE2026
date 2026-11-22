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

# Finite-field-independent verification of associator fibers

The proof is the exact eight-sector symbolic multiplication table in `RESULT.md`. The accompanying standard-Python checker computes all group commutator fibers directly, then computes the associator in the full double by comparing both products and solving a left-quotient equation. It checks (a) every displayed sector identity for every triple; (b) every individual target fiber in each parity sector; and (c) the summed total for each target.

The recorded checks include cyclic groups of orders 2 and 3, dihedral groups of orders 6 and 8, quaternion group of order 8, symmetric groups of orders 6 and 24, and alternating group of order 12. Run `python3 verify_associators.py` from the directory containing the two files. No third-party library, network service, random seed, or external certificate is needed.

The checker exhausts only the listed finite groups; it cannot establish the general theorem without the symbolic proof. The theorem does not determine a distribution for alternate, right-valued associator conventions. Published prior work already gives the identity-fiber specialization. An independent mathematical audit has not been performed.
