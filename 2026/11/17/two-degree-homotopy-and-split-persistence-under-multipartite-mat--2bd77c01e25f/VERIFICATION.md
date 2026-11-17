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

# Verification record

The mathematical proof is in `RESULT.md`; the unrestricted integral conclusions follow from the explicit primitive attaching-basis argument and the resulting sphere-wedge cell attachments.

Run `python3 verify_matching_clique.py` with Python 3 standard library. The script reconstructs the graph independently, enumerates all nonempty vertex subsets for four parameter families and thirteen filtration stages, checks the direct forbidden-clique predicate against the structural face criterion, computes exact mod-two boundary ranks, and checks that each added matched edge contributes precisely the predicted \(\binom{s}{q-2}\) new facets.

The recorded local execution terminated with `MATCHING_DEFECT_CLIQUE_FREE_FINITE_PASS`. The program and complete recorded output are embedded alongside this document. The enumerations do not prove the unrestricted integer statement or detect all possible integral torsion; those are handled by the explicit primitive basis in the written proof.

Scientific limitations: no equivariant classification, no intersecting edge defects, and no additional multi-vertex shores beyond the two specified ones. Independent mathematical audit has not been performed.
