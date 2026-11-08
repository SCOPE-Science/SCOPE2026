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

The reproducible calculation uses only Python 3's standard library: `python3 verify.py`. Every asserted finite enumeration is exhaustive.

The enumerator checks 70 induced four-vertex subgraphs, 26 facets, 111 faces including the empty face, and the nonempty face vector \((8,28,48,26)\). Two different pivot orders each give 53 matched nonempty-face pairs, one critical vertex, two critical triangles, and one critical tetrahedron. Full topological sorting checks acyclicity over 304 directed Hasse incidences. Both integer Morse top boundary vectors are \((-1,1)\), so they are primitive. An independent \(26\times26\) subdeterminant of the simplicial top boundary is \(+1\). Mod-two simplicial boundary ranks are \((7,21,26)\).

The eight oriented octahedral facets are checked to form a cycle; its Morse projection is \((1,0)\), representing a primitive generator modulo the Morse differential. All sixteen dihedral automorphisms and their orientation-signed Hopf traces are checked. The source code's complete assertions produce the last line `WAGNER_FOURCUT_SPHERE_CHARACTER_VERIFIED` on success, as recorded in `verification_output.txt`.

These checks do not construct an equivariant map from the full complex onto a two-sphere and do not address other graphs, cut parameters, or independent validation.
