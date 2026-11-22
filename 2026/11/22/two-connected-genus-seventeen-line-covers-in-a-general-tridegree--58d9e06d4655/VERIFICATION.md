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

# Reproducibility and limits

Run `python verify.py` with SymPy. It checks that a deterministic integral coefficient specialization modulo \(101\) gives a smooth \((2,2,2)\) K3 branch divisor in all eight affine charts, smooth \((4,4)\) discriminants for both rulings in all four charts, transverse eight-point intersections for each pair of quadratic coefficient sections in all four charts, and exactly the same squarefree degree-\(24\) discriminant-of-discriminant for both ruling projections. Expected final output: `PASS`.

The full proof is in `RESULT.md`: the anticanonical-degree argument accounts for all lines, the connectedness of each degree-two lift is obtained by a two-torsion/Koszul argument, and the genus and ramification counts use adjunction and Riemann–Hurwitz. Exact finite-field checks validate that required geometric genericity conditions are nonempty; they are neither a census of all characteristic-zero varieties nor substitutes for the conceptual proof. Originality is subject to the cited literature comparison and the stated historical-priority risk. Independent audit has not been performed.
