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

# Numerical verification and analytical boundary

Run `python verify_polar_nematic.py` with NumPy and SciPy. The script checks the exact conditional Rademacher second and fourth moments for all \(2^N\) sign configurations with \(3\le N\le8\) and five deterministic angle vectors at each size (30 exact finite sums). It also tests one-dimensional Hubbard–Stratonovich quadratures at \(N=64,256,1024,4096\), using the *finite-size corrected* coupling \(c_N=2(N-2)/N\). The resulting values of \(\sqrt N\,\mathbb E|m_N|^2\) are approximately \(0.96057199,1.03480120,1.07879370,1.10283115\), approaching \(2/\sqrt\pi\approx1.12837917\). Four independently discretized angular integrals verify the nonzero-director Bessel characteristic function.

Finite quadrature and enumeration do **not** establish an infinite-dimensional theorem or exclude other prior results. Those require the exact Rademacher moment algebra, radial Bessel monotonicity, Hubbard–Stratonovich concentration and quartic Laplace estimates supplied in `RESULT.md`. The critical full law assumes \(N\to\infty\) at fixed \(k_BT=J/8\) and no external field. No independent audit has been performed.
