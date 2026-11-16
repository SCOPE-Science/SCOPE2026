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

The proof is finite-dimensional but applies to every odd \(N\ge3\). Its critical independently reconstructible steps are (i) the full Fourier diagonalization and two strictly ordered spectral branches, (ii) the mixed-collision determinant \((z-1)(z^{-1}-1)(z^{-1}-z)\ne0\) for nontrivial odd-order roots, (iii) the 3-by-2 tensor-site Fourier separation, and (iv) the time Vandermonde inversion for at most \(N+1\) distinct eigenvalues. Each appears in `RESULT.md` and does not rely on computational extrapolation.

The script `CHECK.py`, with dependency `requirements.txt`, was run from the actual package directory and passed **1,020 parameter cases and 28,210 finite assertions**. It compares Fourier block dimensions and rank on all enumerated positive resonance ratios, on ordinary positive coupling values, and builds selected complete time-space measurement matrices. Floating-point rank tolerances and the finite length cutoff are limitations of these checks. The mathematical classification does not rely on these numerical assertions.

Independent mathematical auditing and independently certified publication-priority verification have not been performed.
