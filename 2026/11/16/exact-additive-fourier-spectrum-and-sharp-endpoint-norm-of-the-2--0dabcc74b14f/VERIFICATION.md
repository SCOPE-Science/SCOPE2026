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

# Verification of finite-field Segre Fourier formulas

The source `check_spectrum.py` was executed against the actual embedded research implementation. Its run enumerates the entire decomposable-tensor subset of \(\mathbb F_q^8\) and the Fourier transforms for \(q=2,3,4,5\). Integer Walsh--Hadamard arithmetic is used for the extension field \(\mathbb F_4\), and numerical Fourier output for the prime fields is rounded only after its imaginary and real residuals are checked below the specified tolerance. The exact integer multiset and rational norm are then compared against the symbolic formulas, as are the zeroth and second moments.

Separately, the script enumerates all two-dimensional subspaces of \(\mathbb F_q^4\) in reduced-row-echelon form and all projective hyperplanes at \(q=2,3,5,7\), counting intersections with the nondegenerate hyperbolic quadric; the exact section counts match the proposed algebraic formula. The final marker is `SEGRE_FULL_SPECTRUM_AND_ENDPOINT_CHECKS_PASS`. A complete representative output is supplied in `checks.txt`.

To reproduce, install the declared `numpy` version range from `requirements.txt` and run `python check_spectrum.py` in the directory containing those two files. The \(q=4\) arithmetic is the binary representation of \(\mathbb F_2[t]/(t^2+t+1)\); a full additive character basis is implemented by its binary coordinate Walsh transform.

**Limits:** The computer checks do not exhaust all finite fields; universal correctness depends on the projective incidence proof in `RESULT.md`. No external mathematical certification or independent validation has been performed.
