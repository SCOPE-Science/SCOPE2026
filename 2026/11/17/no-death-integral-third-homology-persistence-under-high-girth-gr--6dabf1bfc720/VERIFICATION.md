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

Run `python3 verify_chord.py` using Python 3 standard library; compare with `verification_output.txt`. This rebuilds all simplices from the forbidden independent-triple predicate, computes mod-two boundary ranks, and compares exact old and new links with their independently derived graph formulas. The checked cycle chord distances are at least six on both cycle arcs, for 28 cases over cycle orders 12–18. The additional barbell graph has 19 vertices and a rank-three relative prediction. The actual executable emits `LONG_CHORD_CHECK_PASS`.

The unrestricted integral proof uses a relative graph incidence matrix, whose cokernel vanishes because each relative vertex has a path to the old link. The resulting integral kernel is free of rank \(b(F)+1\). The mod-two experiments do not certify infinite ranges, integer torsion, or a canonical splitting. The theorem's proof supplies those statements. Independent audit is not performed.
