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

The proof consists of an exact incidence inequality and an explicit local block replacement, together with published existence theorems for Kirkman and factor-critical Steiner triple systems. `CHECK.py` uses only Python's standard library and checks the supplied length-three code at orders \(q=3,7,9,13\), including the exact prescribed size, the full set of \(q^2\) received words and each maximum inverse-list size. It checks the Steiner pair property and matching disjointness in the generated systems. It also enumerates all length-three words for alphabet sizes \(2\le q\le9\) to verify the shadow-cardinality classification.

Run `python3 CHECK.py` and compare with `CHECK_OUTPUT.txt`. These finite checks do not establish existence for arbitrary admissible alphabet sizes and do not replace the combinatorial proof. The current claim does not encompass alphabet sizes outside the two specified residue classes. Independent audit has not been performed.
