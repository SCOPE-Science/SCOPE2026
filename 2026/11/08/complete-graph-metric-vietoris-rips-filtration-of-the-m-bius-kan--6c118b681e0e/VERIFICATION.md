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

# Standalone verification and limits

Run `python3 verify.py` in a directory containing only the embedded package files. It requires Python 3 and no third-party modules. A reference run is contained in `verification-output.txt` and ends with `MK_RIPS_COMPLETE_FILTRATION_INTEGRAL_HOMOTOPY_VERIFIED`.

The verifier reconstructs the full \(\operatorname{GP}(8,3)\) graph and checks an independent isomorphic incidence-graph representation. It calculates all 16-by-16 graph distances and checks all 65,536 vertex subsets against two alternative clique enumerations; radius-two faces by dimensions \((-1,0,1,2,3)\) number \((1,16,72,112,48)\). It constructs two different complete augmented acyclic Morse matchings with 119 matched pairs and 688 checked Hasse incidences each, leaves critical faces \((9,2)\) in dimensions \((2,3)\), performs all integral unit-pivot cancellations in both directions and checks that the residual \(9\times2\) integer matrices are identically zero. The unaltered simplicial boundary ranks for primes two, three and five each equal \((15,57,46)\), independently confirming reduced Betti ranks. It verifies diameter four, exactly eight disjoint radius-three forbidden pairs, and 24 overlapping six-cycles (as many as six through one edge).

The radius-zero/radius-one/radius-three/radius-four homotopy deductions are elementary graph and cross-polytope arguments; radius-two uses a finite but **exhaustive** check of the entire specified complex, not extrapolation to arbitrary graphs. The Morse-to-CW interpretation is the standard acyclic matching theorem; attaching degrees suffice because its two-skeleton is a wedge of simply connected two-spheres. No external independent scientific audit or universally quantified graph-family claim is made.
