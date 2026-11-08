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

# Verification

Run the standalone exact-integer diagnostic with `python checker.py`; it reports `PASS: 5667 exact finite assertions`. The test covers the Pascal convolution identity, Vandermonde Gram identities, binomial row masses, first-difference total variation and one-step operator bounds. It does not establish asymptotics or infinite-dimensional dynamics. Those depend on the Fourier rescaling, uniform tail and Gaussian derivative independence in the proof, finite-dimensional dual quotient lifting, and the Hypercyclicity Criterion. A separate non-Hilbert infinite-dimensional verification has not been carried out.

The precise domain is complex weighted \(\ell^p\) for \(1\le p<\infty\), and weighted \(c_0\) for \(p=\infty\). Source arXiv:2609.34308 covers the Hilbert specialization already; it is not claimed as a new discovery. The result gives order-sharp transfer moduli, not optimal constants, and requires radial bounded-ratio weights. Independent audit is not performed.
