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

# Verification evidence and limits

The proof establishes the exact valuations for every positive integer index; no infinite conclusion is inferred from a finite program run. The two delicate steps are (i) the pairing congruence for the odd-reciprocal sum, yielding \(\nu_2(H_m^{\mathrm{odd}})=2\nu_2(m)\), and (ii) the strict gap between the quadratic and all higher even terms in the formal exponential expansion, which excludes cancellation.

The accompanying standalone Python verifier uses only the standard library. Running `python3 verify.py` successfully returned:

```text
VERIFY_OK delannoy_n=1024 binomial_n=128 coefficient_n=64 harmonic_cases=64 max_harmonic_m=1920
```

It reconstructs central Delannoy numbers independently by their standard integer three-term recurrence and then checks the signed sum identity and both exact valuation laws through \(n=1024\); it additionally compares the binomial-sum and coefficient definitions and checks \(64\) odd-reciprocal-sum instances using modular inverses. All computations are finite corroboration, not machine certification of the proof. Independent mathematical audit: not performed.
