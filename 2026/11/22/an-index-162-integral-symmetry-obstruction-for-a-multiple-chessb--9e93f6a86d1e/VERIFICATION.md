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

# Verification of the integral equivariant comparison

Run `python3 verify.py` with Python 3.9 or newer, using only standard-library modules. The accompanying `verification_output.json` is the captured output from the supplied source, not a substituted file. Its `status` is `PASS` after every assertion.

The checker enumerates exactly \(1440\) top-dimensional faces, generates all \(3600\) oriented signed top-boundary rows, and reconstructs an integral kernel basis from \(1435\) unit pivots. For the unsigned three-subset-to-two-subset incidence map it calculates rank \(15\) and proves the kernel basis is integral. It reconstructs the complete adjacent column-transposition matrices for both five-dimensional lattices, checks all Coxeter relations, and confirms triviality of the three adjacent row actions. It solves the full \(125\)-equation rational intertwiner system, verifies rank \(24\), and independently checks the primitive integral generator and its determinant. Gcds of **every** minor in all five sizes yield the Smith diagonal \((1,3,3,3,6)\). No exhaustive search over possible homomorphisms is assumed: the exact linear system proves completeness.

The principal mathematical inference is that the free-coordinate bases are genuinely integral, the kernel of a top simplicial boundary is the top integral homology when no higher simplices exist, and a primitive generator of a one-dimensional rational intertwiner space spans all integral intertwiners. The unit, rational-rank, and gcd-minor checks implement those inferences. The comparison only certifies the explicit lattice pair and does not establish an equivariant homotopy type, a general capacity classification, external priority, or independent scholarly validation.
