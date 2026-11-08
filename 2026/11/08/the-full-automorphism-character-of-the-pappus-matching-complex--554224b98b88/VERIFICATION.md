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
# Computational verification and limitations

The two included scripts are complete finite checkers for the specified graph, with no downloaded data or files from other packages. `verify_rational_concentration.py` requires Python 3.9+ and only its standard library. `verify_pappus.py` requires Python 3.9+ and NetworkX 3.x. Run both programs from any working directory and compare their printed outputs to the two embedded `.stdout` files.

The former enumerates all matching masks, explicitly constructs each augmented mod-two simplicial boundary, and checks every boundary rank, mod-two Betti number and reduced Euler characteristic. The latter generates all graph automorphisms, computes all induced edge permutations and their conjugacy classes, then obtains every degree-five character value both by invariant-edge-orbit selection and a separate signed fixed-simplex enumeration. It verifies all 216 equalities, exact group and subgroup averages, and the character inner product.

The mathematical inference from these integer calculations is the rational Hopf trace theorem together with the rational homology concentration derived from binary ranks and Euler characteristic. Modular ranks alone do not prove integral torsion-freeness or integral homotopy classification, and no such new integral claim is made. No independent mathematical audit has been performed.
