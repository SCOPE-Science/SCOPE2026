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

# Verification scope
The proof uses the complete Hankel-minor ideal of the rational-normal curve and a full two-chart computation of the scheme of lines. On the first chart, the coefficient equations impose exactly \(u^2=0\) and \(b_j=j t^{j-1}u\); on the second chart the intrinsic nilpotent coordinate transforms by \(w=-t^{d-2}u\). The transition class is \(\mathcal O_{\mathbb P^1}(d-2)\), which is nontrivial for \(d\ge3\). Hilbert-characteristic computations use the square-zero exact sequence and \(\chi(\mathbb P^1,\mathcal O(m))=m+1\).

The standalone `verify.py` uses exact SymPy polynomial arithmetic. It checks all Hankel minors after the theoretical chart substitution in degrees \(2\) through \(11\), including reductions of coefficients modulo \(2,3,5,7\), verifies that the first quadratic relation enforces \(u^2=0\), checks the overlap transformation, and checks the Hilbert-polynomial arithmetic. Independently, for degrees \(3,4,5\) and characteristics \(0,2,3,5\), it constructs every coefficient of every universal Hankel minor with unknown deformation parameters and verifies by two-way Gröbner ideal containment that the resulting scheme ideal equals the predicted affine-chart ideal. Run `python3 verify.py` in a Python environment with SymPy installed; compare with `verification_output.txt`.

These finite checks do not verify the theorem for unbounded degree on their own. The general coefficient and basis-change arguments are written in `RESULT.md`. Publisher-version comparison and independent mathematical review have not been performed.
