---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Canonical coordinate representatives use two wrap bits at each step and are covered by the 512 closed itinerary cells. For B(s)=[[1,s],[1,1+s]], det(I−B(s)^3)=−s(s+3)^2 and det(I−B(s)^2B(t))=−(s+3)(2s+(1+s)t). Substitution of the slopes gives the four stated factors and finiteness off η=1/3. A separately written and executed exact-rational replay, /workspace/branches/214277fe-0dd4-44e7-9abc-8cb7c20996b3/independent_replay.py, checked all 512 resonant cells. Exactly four rank-zero cells have compatible translations, each reducing to a singleton by the rotation-center argument; twelve positive-length rank-one pieces survive. Their pairwise intersections modulo the lattice and their endpoint incidence give six disjoint maximal segments, with two each of squared lengths 4/81, 8/81 and 20/81. The only H-fixed torus points are (0,0) and (0,2/3), neither on those segments. H must permute the components in cycles of length dividing three, and an invariant interval would be pointwise fixed since an interval homeomorphism of order dividing three is the identity. Thus the six components form two three-cycles. Isolated points contribute zero length; the replay did not count all such points. The uploaded verifier was not executed.

## originality

FAIL

A distinct indexed record, 89b5051ec434, gives the same full-torus non-isolated locus, same unique parameter, same length, and off-resonance finiteness. Its eight closed-square pieces become exactly the six maximal torus segments after two seam joins; this is equivalent coverage, not a contradictory count. The later catalog label does not establish who first obtained the result; this finding is not distinct from the indexed mathematics as reviewed. The earlier Myers Hill–Sturman–Wilson paper supplies the parameter and mechanism but is not the basis of this exact-coverage decision.

## value

FAIL

The exceptional geometry and length are natural invariants at a mixing-family resonance; neither finiteness nor narrow scope is a defect. The frozen result does not add a distinct unknown invariant to the independently indexed complete arc locus: the quotient component lengths and two-cycle decomposition into orbits of length three follow by seam joins and the interval argument. Its independent replay corroborates the mathematics but does not create an additional result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
