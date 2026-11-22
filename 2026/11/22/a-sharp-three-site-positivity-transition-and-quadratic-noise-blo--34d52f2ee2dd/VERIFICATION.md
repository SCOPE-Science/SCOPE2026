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

# Reproduction and limits

Run `python check.py` with Python 3.9 or later; only standard-library modules are used. The program recomputes the cosecant-based exact quadrature weights, checks normalized Fourier moment exactness against every frequency in the specified interpolation band for a suite of odd grid lengths, verifies the unique positivity transition and exact total-variation/noise norm, and compares the large-grid and fixed-grid asymptotic formulas with numerical evaluations.

Actual program output during preparation:

```
PASS 7820 numerical assertions across odd Fourier grids, exactness, positivity, critical point and blowup
```

As an independent computational route, selected odd dimensions \(3,5,7,9,17,31\) were also tested by solving the full Fourier-Vandermonde moment system directly and comparing the resulting weights to the analytic formula; observed discrepancies were below \(3\times10^{-9}\) in these tests. This second route is described for transparency and does not depend on any unprovided generated numerical data.

The claim that the formulas hold for *every* odd dimension is supported by the analytic Fourier interpolation and strict-convexity argument in `RESULT.md`, not by finite tests. In particular no finite computation certifies a large-grid asymptotic, exclusion of all other negative weights, or historical originality. Exactly coalesced sites are outside the theorem. No independent mathematical audit has been performed.
