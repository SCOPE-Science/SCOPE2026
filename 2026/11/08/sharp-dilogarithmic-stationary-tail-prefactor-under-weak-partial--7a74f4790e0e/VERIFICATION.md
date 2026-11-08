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

# Reproducibility

The self-contained numerical check is `checks/verification.py`. Run `python3 checks/verification.py` with Python 3, NumPy and SciPy; no input data or network connection is required.

The checker verifies 48 numerical assertions: the dilogarithmic cumulant curvature, an Euler–Maclaurin geometric-product identity at four frequencies and four contraction scales, the exact product self-similarity, two small-displacement and two remote-displacement rate expansions, and independently evaluated Fourier-integral tail ratios. Observed ratios at \(h=0.25,0.12,0.06\) were approximately \(0.757291,0.845672,0.906978\) for \(y=1\), and \(0.901135,0.945342,0.970386\) for \(y=2\). The final line was `PASS: 48 deterministic identity and asymptotic assertions`.

The geometric product is truncated when the remaining weights are below the prescribed tolerance; the Fourier integral is numerically truncated and checked with integration-error bounds. Neither finite truncation nor finite precision establishes a large-deviation limit; `RESULT.md` contains the separate full analytic proof, including an explicit Fourier majorant and exact exponential tilting. No independent audit has taken place.
