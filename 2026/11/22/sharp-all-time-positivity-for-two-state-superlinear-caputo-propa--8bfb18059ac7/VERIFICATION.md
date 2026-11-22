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

# Verification record

The two-state generator obeys \(A^2=-(u+v)A\). The Caputo solution is explicitly reconstructed from the zero and negative spectral projectors; direct substitution verifies the matrix equation and both initial conditions. The formula \(P=\Pi+f(I-\Pi)\) reduces all-time entrywise positivity to the two diagonal inequalities. The Fourier-Laplace calculation explicitly normalizes its nonnegative frequency density to one, proving the strict scalar amplitude bound, while the classical Mittag–Leffler asymptotic supplies a negative attained minimum. Endpoint proofs use characteristic-function total-variation convergence and the uniformly convergent Mittag–Leffler series. These are analytic arguments and do not rely on the finite checker.

`CHECK.py` is a self-contained standard-library diagnostic; run with `python CHECK.py`. Its comparisons use representative rational rates and fractional orders, column sums, determinant identities and a strict negativity witness. The checker samples only finitely many times and does not certify global minimum values, exact priority, continuous-time Markov impossibility, or infinite-time universal theorems.

Scientific limitations and all sources are documented in RESULT.md and REVIEW.md. Independent assessment was not performed.
