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
# Verification
The standalone file `verify_vamos.py` uses only the Python standard library and computes from the displayed nonbases. Execute `python3 verify_vamos.py` to reproduce `verification_output.txt`.

The code exhaustively checks the matroid basis-exchange property and all \(8!\) permutations of the eight ground elements, yielding exactly 64 automorphisms. It reconstructs the face vector \((8,28,56,65)\), checks augmented boundary ranks \((1,7,21,35)\) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_{101}\), and checks equality of two independently implemented character calculations for all 64 group elements. Exact finite sums over both order-eight factors give the displayed tensor-product multiplicities. Independently constructed invariant oriented face-orbit chains produce top quotient ranks \((0,1,0)\) modulo 101, confirming the rational trace averages.

The proof of the integral exact sequence is in `RESULT.md`. Modulo-prime rank agreements alone are neither an integral Smith normal form computation nor a proof of the integral homology statement; the boundary-of-five-element-set construction supplies the required integral surjectivity. The quotient assertions concern rational cohomology, not the homotopy type or integral quotient torsion. No external or independent audit has been carried out.
