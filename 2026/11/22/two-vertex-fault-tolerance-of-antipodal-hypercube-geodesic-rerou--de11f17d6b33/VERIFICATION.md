---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A length-n antipodal path adds each coordinate once, and changing one internal vertex exchanges the two coordinates on either side of that vertex. The computational Q4 base was independently reproduced directly in cube-path coordinates for all 106 fault sets of size 0–2, including the ten tabulated pair types; every allowed graph is nonempty and connected. In the induction, any first letter not itself forbidden leaves nonempty proper suffix faults only from the original sets containing that letter; induction gives a nonempty connected fiber. A proposed bridge uses the same suffix after (s,t) and (t,s); its two singleton sets and common doubleton are allowed. Each further forbidden set can exclude at most a 1/(n-2) proportion of suffixes, since its residual size lies between 1 and n-3. Thus two faults cannot block the bridge for n>=5. The fiber graph has at least n-2 vertices and loses fewer edges than its minimum complete-graph cut, so the connected fibers join into one component. In Q3 the only two remaining paths after forbidding {0} and {1,2} differ in both internal vertices; the independent enumeration confirmed exactly this obstruction.

## originality

PASS

The known fault-free permutahedral representation and the one-fault result are not claimed as novel. The inspected sources do not cover connectivity after two arbitrary internal faults, for which the missing bridges must be controlled simultaneously and Q3 has a genuine counterexample.

## value

PASS

The result guarantees that all currently feasible shortest antipodal routes can be transformed into one another without sacrificing optimal length or traversing either fault. This is stronger than existence of one survivor and is not inherited from fault-free sorting. A small counterexample identifies the exact minimum dimension for the guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
