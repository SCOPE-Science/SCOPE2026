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

The claim has a self-contained analytic proof. Run the dependency-free checker with `python3 CHECK.py`. Its finite assertions test exact finite-prefix Fourier identities on uniform and nonuniform iid digit processes, reversible and nonreversible Markov chains with stationary distributions, comparison with longer reversed prefixes, and the asymptotic fixed-point equality case.

Expected success signature: `CHECK_OK finite_assertions=749 prime_alphabets=2,3,5`. The checker enumerates only finitely many words and thus does not prove a theorem for arbitrary infinite stationary processes or all denominator exponents. The infinite-stationary-law result follows instead from stationary extension, equality of finite-block distributions, deterministic digit-tail bounds, uniqueness of circle Fourier coefficients, and the sharp atomic witness.

No independent audit, formal proof assistant certificate, or external certification has been performed.
