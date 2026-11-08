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

# Verification of the rational character

Run `python3 verify_octahedral_morse_character.py` in a directory containing the standalone code. It requires the Python standard library only. The recorded output is `verification_output.txt`, beginning with `OCTAHEDRAL_MORSE_FULL_CHARACTER_PASS`.

Checks actually implemented and executed:

- Reconstructs 24 incidence arrows from the twelve edges of the octahedron. Independently enumerates valid simplices by all subsets of up to five arrows and all 15625 vertex-tail assignments; the exact face sets agree (6125 including the empty face).
- Matches 2724 complete face-poset cover pairs, checks all 25176 nonempty-face incidences by topological sorting of the directed Hasse graph, and finds one critical vertex plus 675 critical fourth-dimensional faces. Thus a finite acyclic matching establishes the previously known wedge decomposition.
- Enumerates the complete 48-element hyperoctahedral graph automorphism group and checks every image of each enumerated face remains a face. Computes all signed oriented fixed-face traces (not unsigned face counts).
- Checks constant character on each of ten signed-cycle conjugacy classes and calculates all ten irreducible inner products from induced Specht character formulas without a precomputed character table. Verifies integer multiplicities, total dimension 675, full-group fixed multiplicity 11, and central inversion trace -25.

The signed Lefschetz calculation is exact because all nonzero reduced rational homology is in degree four. The orbit-space ring follows from rational invariant cohomology for a finite group and the absence of degree-eight classes. The finite checks do not establish priority over inaccessible literature, an integral representation lattice, or independent mathematical review.
