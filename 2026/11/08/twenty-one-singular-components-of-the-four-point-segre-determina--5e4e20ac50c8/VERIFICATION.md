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
# Reproducible checks and limitations

Run `python segredet_singularity_verify.py` using Python 3. SymPy is optional but required to replay the characteristic-zero Hessian witnesses.

The verifier checks all \(9^4=6561\) ordered four-tuples in \((\mathbb P^1(\mathbb F_2)\times\mathbb P^1(\mathbb F_2))^4\); at each tuple it computes matrix rank and every tangent derivative of the \(4\times4\) determinant over \(\mathbb F_2\). Counts: \(4617\) determinant-zero, \(1161\) singular, split into \(729\) rank-at-most-two and \(432\) singular rank-three tuples. The geometric classification agrees exactly on all these tuples.

Over characteristic zero, SymPy differentiates the explicit affine determinant symbolically, and evaluates four exact rational witnesses: ruling; two values in a \(1+3\) partition; two values in a \(2+2\) partition; repeated pair with the other two values on opposite tangent rulings. The exact Hessian ranks are respectively \(3,4,4,4\). The script certifies an explicit nonzero integral Hessian minor in each case.

The global classification is proved geometrically in `RESULT.md`; a finite enumeration does not establish the theorem for infinitely many complex points. Openness of nonzero minors combined with smoothness of the generic component and the analytic Morse–Bott lemma establishes the generic quadratic types. No characterization of the nonreduced singular scheme or of singularities where components meet is attempted. Independent validation is not performed.
