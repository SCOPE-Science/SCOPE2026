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

Run `python3 verify.py`. The program uses standard-library exact fractions and independently enumerates spanning trees to calculate each edge's effective resistance as its inclusion probability in a uniformly random spanning tree. It tests the local triangle-codegree inequality, the sharp simplicial bound, and the *if and only if* equality criterion on every connected labelled graph at orders two through five (counts respectively 1, 4, 38, 728). It also checks clique-with-pendant-path equality for all possible smaller clique degrees at orders three through seven, and shows that the noncomplete two-connected chordal diamond has unequal local curvatures. Output ends in `VERIFY_OK` on success.

The proof for arbitrary orders is mathematical and not inferred from finite enumeration. The current script does not test positive nonunit edge weights, disconnected graphs, or independently verify historical novelty. This is a self-reviewed result, with no independent audit performed.
