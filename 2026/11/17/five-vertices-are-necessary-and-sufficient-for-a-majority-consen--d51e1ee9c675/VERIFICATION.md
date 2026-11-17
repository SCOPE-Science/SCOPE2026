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

The included `verify_all_labelled.cpp` enumerated all simple labelled graphs on each of two, three, four and five vertices; checked connectivity before and after each present-edge deletion; and computed every consensus basin by reverse reachability in the full binary functional graph. It returned \(0,0,0,240\) qualifying marked pairs at these orders, with \(120\) labelled pairs in each of two order-five types.

`verify_independent.py` independently enumerated the same finite domain, computed basin membership by explicit forward trajectory detection (unanimity or cycle), and classified all qualifying pairs under the full permutation group. It returned exactly two marked isomorphism classes, with the same basin sizes and counts. The exact observed standard outputs are included. The textual graph-state witnesses can also be checked directly from the stated majority update equation.

The enumeration is exhaustive for orders at most five, not for larger graphs. A successful finite computation alone does not constitute independent external validation. The scientific claim is limited to the smallest order and its complete classification; no external audit has been performed.
