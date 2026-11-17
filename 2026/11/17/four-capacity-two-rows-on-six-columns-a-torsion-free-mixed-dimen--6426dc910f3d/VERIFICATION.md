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

# Verification record

## Reproducibility

Run `python verify.py` in the same directory after installing `requirements.txt`. The program is a complete stand-alone exact enumerator. It reconstructs the simplicial faces from row/column choices, the vertex-toggle matching, all codimension-one incidences, and the full directed Hasse graph. A successful topological sort certifies no alternating cycles. Signed boundary elimination produces the exact integral Morse matrix, whose Smith normal form is computed over the integers. Three independent finite-field boundary reductions test the resulting Betti ranks.

## Checks actually executed

The packaged program was executed and its complete textual output is embedded in `verification_output.txt`. It reports \(9564\) nonempty faces, \(4727\) matched pairs, \(42960\) oriented Hasse cover edges, one critical vertex, \(96\) critical four-cells, \(13\) critical five-cells, and eight unit Smith pivots. Over the finite fields of orders two, three, and five, the complete six boundary ranks agree; the only nonzero reduced Betti numbers are \(88\) in degree four and \(5\) in degree five. The exact certificate is stronger than finite-field agreement.

## Limits

The certificate is a finite exhaustive mathematical computation for the specified board and uses SymPy for the exact Smith form. It is not a mechanized proof in a proof assistant and does not determine any equivariant or broader-width homotopy type. No independent audit has been performed.
