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

# Verification and limits

Run `python3 verify.py` from the same extracted package. The verifier uses only Python's standard library, reconstructs induced partial maps through permutations, independently generates extendible maps by restricting all full automorphisms, and checks every coefficient against the closed formulas for all 30 partitions through six points. For the 13 unequal partitions of seven points it checks the sharp first-defect formula using direct induced-map enumeration. A successful run prints `ALL_CHECKS_OK`; the observed run also reported `EXHAUSTIVE_FORMULAS_AND_GLOBAL_RESTRICTIONS_OK 30` and `TOP_DEFECTS_SIZE_SEVEN_OK 13`.

Finite enumeration is supporting evidence, not a proof of the general result. The all-size assertion follows from the explicitly stated class-intersection matching criterion, which also proves the first-defect classification and count. Independent mathematical validation and historical priority certification have not been performed.
