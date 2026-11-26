---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the unnormalized discovered weight in operational time A=lambda*t/H_N, the mean is F_N. Splitting the infinite mean at floor(A) gives log A+2 gamma+O(1/A); the omitted catalogue tail is A/N+O(A/N^2+(A/N)^2). Bracketing at fixed multiples of B_N first gives A_N/B_N -> 1. The root equation then gives log(A_N/B_N)=A_N/N+O(1/B_N+(B_N/N)^2+1/N); exponentiation and substitution yield (3). For (7) use the already proved derivative estimate (do not differentiate an undifferentiated big-O): V_N=F'_N(A)-F'_N(2A), and the difference of the two omitted tails is O(A/N^2) by 1-exp(-A/i) <= A/i. For the CLT, scaled summands with i>sqrt(A)/epsilon are bounded by epsilon, while the sum of their smaller-index counterparts' scaled variances is O(A exp(-epsilon sqrt(A))). At A=A_N+h sqrt(A_N), the mean shifts by h/sqrt(A_N)+o(1/sqrt(A_N)); the exact inversion event is S_N(A)>theta H_N, and its limiting normal has no atom. In the last proof paragraph, the relative 1+o(1) on the drift does not follow from (3) below or at theta=1/2. What is needed and follows is the additive error O(B_N^(-1/2)+(B_N^(3/2)/N)(B_N/N+1/B_N)): it is o(1) below 2/3, o(1) at 2/3, and o(B_N^(3/2)/N) above 2/3. This establishes (4) without a stronger relative estimate. An independent finite check of the actual mean root, derivative, variance and drift in branches/review_zipf_crosscheck.py was consistent with the result (at N=10^6, theta=2/3, A_N V_N=0.4999892, drift 0.3170964 versus limiting 0.3152368); it is not a proof.

## originality

FAIL

A distinct indexed result states and proves the same exact-root Gaussian and the entire explicit-centering trichotomy, with the same root expansion. Normalizations, strict threshold, aligned harmonic weights and fixed parameter range all agree. This is established equivalent coverage, not an inference about authorial dependence or who proved it first. The indexed match carries a later catalogue label than the assigned path; their labels do not establish the order or independence of the mathematical work. No distinct scientific content remains after comparing the actual statements.

## value

PASS

As a mathematical statement the coincidence of the catalogue bias and the fluctuation scale produces a genuine threshold at 2/3 and a nonvanishing Gaussian shift exactly there. This refines the first-order law in a way useful for applying an explicit centering. The value of the theorem as such does not give value to publishing a second equivalent finding or overcome the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
