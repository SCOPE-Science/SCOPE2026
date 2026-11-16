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

Run `python3 check_theta.py` using Python's standard library. It builds labeled simple theta graphs independently of the symbolic proof and enumerates their spanning trees by a connectivity test on every candidate edge subset of the correct size. It then uses an integer Walsh–Hadamard transform to check all coefficients, not sampled coefficients, in 24 parameter pairs \(2\le a,b\le6\), \(a+b\le11\). It compares the exact rational endpoint norm to the formula in `RESULT.md` and checks the full signed-tree transform identity.

The locally executed checker completed with marker `THETA_ALL_WALSH_CERTIFICATES_PASS 24`. The checker does not prove unbounded parameters. The proof rests instead on the exact tree parameterization, the integer absolute-value lemma, binomial identities, and the integer factorization determining the Fourier zeros. The independent audit status above refers to external validation and has not been changed by this check.
