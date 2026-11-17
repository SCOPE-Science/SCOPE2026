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

The standalone `verify.py` recomputes all four initial chip vectors, deterministic parallel firing orbits through exact first repeats, maximal simultaneous firing sets, their full simplicial complexes, and their cover nerves. It then verifies complete deterministic elementary collapses (7, 45, 37 and 19 pairs), followed for the exceptional shift by an explicit globally acyclic matching that leaves one vertex and two triangles. Direct-complex and nerve mod-two boundary matrices are independently reduced and checked for agreement. The executable results are recorded in `verification_output.txt`.

The proof of the claimed **integral homotopy types** uses nerve lemma and discrete Morse theory; a mod-two Betti calculation alone would not certify those types. All finite vertex/face enumerations are exhaustive for the nine-vertex graph. The code uses only Python 3 standard-library modules, no external theorem prover or network connection. No infinite-family statement is inferred from these finite checks.
