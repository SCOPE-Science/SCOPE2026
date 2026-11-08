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

Run `python verify_preorders.py` in a standard Python 3 environment, without third-party dependencies. The checker constructs every poset on up to eight points, generates all positive-weight quotient expansions of each relevant total order, groups binary relational color-refinement signatures, and tests graph isomorphism by complete backtracking.

The recorded execution output is in `verify_output.txt`. Expected terminal line: `VERIFY_OK preorders_8=35979 c2_classes_8=35977`. The eight-point line reports `40877` weighted descriptions, `35979` nonisomorphic preorders, `35977` \(C^2\) equivalence classes and two two-member exceptions; each pair has only weight-one quotient points. The published preorder and poset counts provide independent enumeration cross-checks but not independent logical certification.

Two exact witnesses are printed as strict-relation bitmask tuples with all class weights one. The first pair differs in connected components of the comparability graph, and the second in the number of covering relations. These are finite checked certificates of nonisomorphism; shared global color signatures establish the counting-logic equivalence.

No claims are made about orders greater than eight. No independent audit has been performed.
