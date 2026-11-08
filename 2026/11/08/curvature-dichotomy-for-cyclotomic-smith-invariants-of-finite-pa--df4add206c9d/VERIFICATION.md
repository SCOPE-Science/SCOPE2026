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

# Verification and limitations

The exact standalone checker `verify.py` uses only Python's standard library and runs with `python3 verify.py` in the extracted package directory. It constructs each Fourier matrix modulo \(\pi^{m+1}\), where \(m=(p-1)/2\). Since \(v_\pi(p)=p-1\ge m+1\), the truncated cyclotomic ring here is represented faithfully by \(\mathbb F_p[\pi]/(\pi^{m+1})\). The checker independently performs valuation-minimal pivot operations and compares the resulting Smith exponents with the theorem.

Tested primes: \(3,5,7,11,13,17,19\). Tested nonzero curvature products: \(c\in\{1,2,-1\}\), yielding 20 distinct cases. Actual checker termination: `PARABOLIC_LOCAL_SMITH_PASS`. These are finite corroborations, not an exhaustive check of all primes. The complete proof of the nontrivial-character valuations and the two-dimensional block is in `RESULT.md`.

The flat boundary's exponents use an independent exact Newton-Vandermonde argument; testing it with the characteristic-\(p\) truncated model at degree \(p-1\) would exceed that model's valid precision. No such inference is made. No independent mathematical audit has been performed. Historical priority cannot be established by failed search alone; the closest source comparisons and remaining risk are documented in the scientific review.
