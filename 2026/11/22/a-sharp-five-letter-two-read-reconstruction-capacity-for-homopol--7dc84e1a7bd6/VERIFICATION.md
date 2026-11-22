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

The capacity proof reduces each exact-support class to a finite basis with support size at most five. `verify_direct.py` uses deletion-output sets as its primary edge construction, checks exhaustive two-colouring and perfect matchings for all exact-support graphs at lengths two through four and for support sizes two, four and five at length five. It also checks a nineteen-word independent set and a dual covering certificate on all 42 exact-support ternary words of length five: twelve edges, six genuine seven-cycles, rational doubled weights, coverage of each vertex by two doubled units, and doubled right-hand side 39. These imply an integer upper bound of nineteen and agree with the witness. The seven-cycle at five letters is checked against the exact deletion graph.

`verify_structural.py` constructs edges independently from opposite-phase alternating changed intervals and compares the entire unordered edge set with direct deletion-output intersections for all \(2\leq q\leq5\), \(2\leq n\leq5\). It checks the all-alphabet edge formula at those cases and the exhaustive support-five basis counts. Both scripts were executed from these exact package paths and succeeded. These finite computations certify the universal capacity result **only in conjunction with** the mathematical support-invariance argument; they are not claimed to explore infinitely many alphabets or lengths.

Independent mathematical audit and external formal proof certification have not been performed. Longer-length code capacities and general odd girth are not established.
