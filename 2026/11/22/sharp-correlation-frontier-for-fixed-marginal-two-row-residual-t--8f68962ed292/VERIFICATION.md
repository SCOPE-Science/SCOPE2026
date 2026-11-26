---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The result concerns iid pre-update cached residual tracking on A=(1,1)^T, fixed positive unnormalized h and arbitrary finite deterministic starts. The update gives conditional mean estimator 2e and each tracker is replaced with probability 1/2, independent of the past. A separate symbolic reconstruction from the update verified the four state maps, the moment operator on (E e²,2E et,E t²,E d²), det(I−T)=−hF with F=3h²+3uh+u−1, and the conditional energy drift 2F e². It also checked the (e,t) principal-minor identities: the bracket in the determinant is concave in h and strictly positive at 0 and h_*, and a is positive there in the stated limiting sense. The energy is nonnegative even at u=1/2, when the d coefficient vanishes. Below the root summability forces E e²→0, and E z_i,next²=(E e²+E z_i²)/2 gives joint convergence. At equality det(I−T)=0; above, the monic characteristic polynomial is negative at 1 and positive for sufficiently large argument, giving a real eigenvalue λ>1. A real left eigenvector defines a nonzero quadratic functional on initial states (the four coordinate monomials are linearly independent); choose a deterministic start with nonzero value. Its expectation scales by λ^k while its absolute value in expectation is bounded by a constant times E(e²+t²+d²). This proves failure at λ=1 and a uniform exponential lower bound for the chosen start at λ>1. Implicit differentiation and exact substitutions verify the threshold ordering and three constants, including the fixed-marginal endpoints. Replay: independent_check.py and independent_check.txt under /workspace/branches/8e414a4a-bf90-404e-9757-14a39b7bc5bd/; the frozen verify.py was inspected, not executed. Recorded 709 checks are ancillary and no Lean or expert certification is asserted.

## originality

PASS

The distinct claim is the exact all-u stability frontier at common marginals and common expected row count, including a witnessed loss of stability, not invention of the arbitrary-sampling tracker, covariance method or the uniform-singleton ceiling.

## value

PASS

Holding both per-row marginals and expected batch size fixed isolates the effect of co-inclusion in a minimal cached estimator. The exact decreasing ceiling and existence of unstable starts quantify a failure of marginal information to determine stability; this is useful as a benchmark for arbitrary-sampling stepsize bounds, not as a rate or runtime optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
