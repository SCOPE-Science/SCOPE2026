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

For the proper part of the noncrossing lattice, the shellability theorem gives a wedge in dimension two. Rank-preserving relabeling stabilizes each setwise fixed chain pointwise, so quotient open cells and signs are correctly obtained from chain orbits. Nonidentity rotations cannot fix a proper partition: an invariant equivalence for the transitive prime cyclic action is a coset partition. Each reflection fixes a two-element block consisting of an adjacent swapped pair. Armstrong's theorem thus gives fundamental group C5 for rotations and trivial groups for the reflection and full dihedral quotients. Independently regenerated the four orbit cell vectors (40,150,125), (24,81,65), (8,30,25), (8,21,15) from binary equivalence relations (replay: python3 /workspace/branches/independent_topology.py). Euler characteristic and simply connected Whitehead give the identity, reflection and full-dihedral wedge counts. The cyclic quotient needs attaching words, not just homology. Contracting a tree is valid for a contractible CW subcomplex. Each of 22 eliminations retracts the edge plus its once-traversing 2-cell onto the other edges, then substitutes this retraction into the remaining attaching maps. The frozen verifier's signed triangle ordering is a cyclic permutation of ab·bc·(ac)^−1. In a different ordering my exact reduction leaves the same inverse fifth power twice and one empty word; after the first degree-five cell, the second identical attachment is nullhomotopic, so this is the claimed Moore space plus two spheres. Another fresh enumeration yielded one fifth power and two empty words directly. In the lift, the Moore 2-cell boundary is the norm, with kernel the augmentation ideal; the spheres lift to two free integral deck summands. This is the module of the universal cover, not quotient H2. The supplied verifier was inspected and not executed.

## originality

PASS

The supported distinct claim is the ordinary quotient classification for geometric relabeling of proper NC5, especially the exact cyclic 2-cell homotopy and integral deck lattice. The unquotiented wedge and general topology tools are prior input. Nearby exact results vary the action or change the lattice; their date or abstract resemblance is not evidence of implication.

## value

PASS

The first pentagonal dihedral noncrossing example gives a natural complete subgroup comparison: free rotations produce torsion and nontrivial fundamental group, while reflection-containing quotients are simply connected. Distinguishing the exact Moore-space splitting and integral module from mere cell-orbit counts or rational characters makes the finite example a reusable test case for stronger quotient claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
