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

## Reproduction

Run `python3 verify.py` using Python 3 and the standard library. The script verifies the degree-eight homogeneous parts of the eighth iterate, exhaustively traverses the functional graphs over \(\mathbb F_2[t]/(t^m)\) for \(1\le m\le10\), and uses a separate polynomial multiplication routine to count the fixed points of the first five dyadic iterates in the periodic core at \(m=10\). It checks the explicit witness \((1+t,t^2)\) with eighth and sixteenth iterates and compares its exact output with the included `verification_output.txt`.

## Logical scope

The symbolic jet certificate, combined with the valuation argument in the proof, verifies the cutoff through \(m=9\); a finite scan alone would not establish an unrestricted statement. The full numerical census over \(R_{10}^2\) covers all \(1048576\) graph vertices and yields \(6144\) primitive sixteen-cycles. The all-length periodic-core theorem and unbounded dyadic periods follow from the separate algebraic proof, not from finite extrapolation. Self-review was completed; independent review has not been performed.
