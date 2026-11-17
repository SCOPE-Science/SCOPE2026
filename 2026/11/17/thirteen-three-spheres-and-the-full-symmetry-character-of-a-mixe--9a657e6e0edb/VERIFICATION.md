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

# Reproducibility

Run `python3 verify_mixed_cactus.py` with Python 3's standard library. The program enumerates all 40320 permutations of eight graph vertices and constructs the downward-closed strong-Morse matching complex from first principles. It checks 345 generator incidence sets; 492 nonempty faces; the f-vector (20,108,220,144); and an explicitly fixed 239-pair matching.

For every cover relation in the entire nonempty face poset, the program directs unmatched relations downward and matched relations upward. A topological sort visits every one of 492 nodes, so the matching is acyclic. There is exactly one critical 0-face and thirteen critical 3-faces, and no other critical faces. Forman's discrete Morse theorem proves the integral homotopy type as a wedge of thirteen 3-spheres. This is a finite exhaustive argument, not extrapolation.

As independent consistency checks the program calculates complete mod-two simplicial boundary ranks (19,89,131) and verifies preservation of the graph by all sixteen automorphisms. For every automorphism it computes the **signed** simplicial Lefschetz number by summing fixed-face orientation signs, and checks the full ten-class rational top-homology character. `verification_output.txt` contains a replay transcript. The code is a sufficient executable combinatorial certificate but has not undergone external independent validation.

# Limits

No infinite-family, equivariant homotopy, or integral group-module classification is established. The complete mathematical proof additionally uses standard Forman discrete Morse theory and the Hopf trace formula.
