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

# Mathematical verification and limits

The standalone `verify.py` requires Python 3, NumPy, SciPy and SymPy. From the directory containing the files, execute `python verify.py`. The program evaluates exact Vandermonde cancellations, the degrees and coprimality in dimensions two through four, and rational evaluations of the residue formula. In dimensions two through five, it builds intrinsic central sections from intersections of cross-polytope edges and verifies the convex-hull volumes against the derived section formula for independent random directions. In the recorded execution, all 250 assertions passed.

The finite checks do **not** prove the formula or irreducibility in every dimension. The general proof is analytic: coarea and Fourier inversion give the section formula; the alternating numerator is divisible by the Vandermonde; a nonzero pole residue at every pair-sum hyperplane proves numerator–denominator coprimality; and a primitive homogeneous linear-in-one-variable equation proves irreducibility. The statement includes no certification of independently verified mathematics.
