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

# Reproducibility notes

The result is proved symbolically in `RESULT.md`. It uses the actual source startup rule followed by a fixed \(\ell\)-term geometric mean, with \(0<a<1\) and \(x_0=(s,0)\), \(s\ne0\). The initial one-term ratio and every later ratio are strictly positive.

Run `python verify.py` with Python 3 and NumPy. The script performs finite fixed-window trajectories and characteristic-polynomial spectral computations; it also checks exact rational identities for \(a=1/4,1/2,3/4\). It tests but does not replace the proof of global convergence and all-\(\ell\) spectral bounds. In particular, numerical convergence does not imply the global assertion, and a 50-window finite matrix is not an asymptotic \(\ell\to\infty\) argument.

The mathematical boundaries are fixed history length, a single invariant eigenspace, and exact arithmetic. The feedback spectral radius governs the linearization and is not asserted to be the observed trajectory rate for all starts. No independently audited mathematical certificate is supplied.
