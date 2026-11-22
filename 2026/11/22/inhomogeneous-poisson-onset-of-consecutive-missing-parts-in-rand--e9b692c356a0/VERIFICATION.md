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

The self-contained standard-library program `verify.py` enumerates partitions by two independent methods. Run `python verify.py` from the extracted folder. It checks 600 exact equality assertions across \(0\le n\le24\), \(1\le r\le4\), \(1\le m\le6\). A second section compares exact finite-size survival proportions at \(n=300,1000,3000\) and \(r=2,3,4\) with the limiting formula. Slow finite-size convergence is expected, and these comparisons are not an infinite proof.

The analytic argument is self-contained in `RESULT.md`: exact conditioning, a growing-window lattice local central limit theorem with Fourier bounds, total-variation transfer, and factorial-moment Poisson convergence. Checks and proof address one fixed \(r\) at a time; no parameter-uniform estimate or asymptotic of unbounded moments is claimed. Independent scientific verification has not been performed.
