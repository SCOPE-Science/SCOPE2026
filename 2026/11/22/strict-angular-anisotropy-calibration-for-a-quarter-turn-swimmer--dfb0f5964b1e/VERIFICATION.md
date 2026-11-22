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

# Mathematical and computational verification

The proof independently establishes the correct angular transformation, the exact beta-ratio expectation, symmetric unimodality of its log-ratio distribution for the full positive parameter domain, the independent beta-factor coupling, and strict decrease under convolution. Endpoint laws and the exactly computable case \(a=1\) supply independent normalization checks.

`CHECK.py` requires Python 3.10+, NumPy and SciPy. Running `python CHECK.py` on the exact bundled file returned:

```
PASS: 38 analytic-anchor, positivity, monotonicity, quadrature, and asymptotic checks
a=  0.125, Q=0.645018512
a=   0.25, Q=0.456945057
a=    0.5, Q=0.273238021
a=      1, Q=0.141591131
a=      2, Q=0.068581955
a=      4, Q=0.033010207
a=     10, Q=0.012800035
a=     30, Q=0.004199304
a=    100, Q=0.001251372
```

The tensor Gauss--Jacobi quadrature and Sobol inverse-beta integration are independent numerical representations. The small discrepancy at \(a=1\) in the latter is finite quadrature error relative to \(\pi-3\). The tests are finite and do not certify an infinite-domain claim; the analytic argument in `RESULT.md` carries that burden. No external independent scientific audit has been performed. No finite-sample estimation guarantees are claimed.
