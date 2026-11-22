---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The 64-point Hamming scale-two Rips complex is Ind(K4×K4×K4), previously proved homotopy equivalent to a wedge of 405 3-spheres; the source proof and actual verify_full.py finite matching/acyclicity certificates were reconstructed. Independent enumeration got 508 maximal simplex candidates, 830101 faces, 414848 matched pairs and 405 unmatched tetrahedra (finite complete count), and source code performs full Hasse acyclicity topological sort. For each translation in C4^3, invariant simplices correspond to independent sets in a compatibility graph of nonadjacent translation orbits of the forbidden distance-three graph. Reduced Lefschetz and orientations give trace = I(H,-1), because invariant orbit lengths are 1,2,4 and the alternating fixed-simplex sum matches the orbit-set inclusion signs. Independently computed all 64 integer traces by an independent-set deletion recurrence, recovering ten class values (405,9,9,-3,-3,45,1,1,1,1). Exact Gaussian-integer Fourier sums give nonnegative multiplicities 9 seven times,6 thirty times,8 nine times,5 eighteen times, summing 405. Trace averages 576/64=9 and 568/8=71 prove stated rational quotient invariant ranks by barycentric-transfer, not torsion claims. Complete finite enumeration is exhaustive for this fixed finite object, subject to ordinary implementation correctness.

## originality

PASS

PASS best-of-knowledge for complete C4^3 trace/Fourier classification, with underlying wedge-405 sphere count explicitly prior. Prior analogous ternary C3^3 characters and binary hyperoctahedral Rips work do not imply order-two/order-four quaternary trace split or quotient ranks.

## value

PASS

A fixed natural 64-point Hamming complex has previously known nonequivariant homology, but its full symmetry character distinguishes order-two from order-four translations and computes all 64 multiplicities. The complete C4³ action and the 9 and 71 rational quotient dimensions are genuine new exact invariants of a natural finite classification, not a random slice or a recomputation of 405.

The dated certificate retains the supplied scientific assessment, sources and limitations.
