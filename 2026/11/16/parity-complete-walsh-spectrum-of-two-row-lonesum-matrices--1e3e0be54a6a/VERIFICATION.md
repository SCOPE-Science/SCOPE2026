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

The self-contained `verify_lonesum_walsh.py` evaluates every coefficient by an exact fast Walsh–Hadamard transform for one through eight columns, and separately computes the three-product inclusion–exclusion formula. It checks the full histogram, even-weight support, attained spectral gap, and maximal coefficient. Through five columns it also constructs the directed graph and tests acyclicity by topological source removal, independently of the forbidden-column criterion. Additional deterministic frequency checks use much larger column counts.

Run: `python3 verify_lonesum_walsh.py`.

Observed output:

```text
LONESUM_WALSH_EXACT_PASS n=1..8; 87380 exact Walsh coefficients; graph cycle checks n<=5
```

All computations are exact-integer checks, not exhaustive infinite verification. The all-length proof is the factorization of Cartesian-product character sums, followed by a prime-factorization nonvanishing argument. The Moore–Penrose and projection statements use the unnormalized convolution convention and Fourier diagonalization. Independent mathematical validation has not been performed.
