---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

In the separated affine similarity model, the finite-alphabet dimension s_N is the unique root a^{q s_N} sum_{j<=N} j^{-q s_N}=1. At s=1/q sign is exactly sign(a H_N-1). The strict integer crossing has log N_*=1/a-gamma+o(1), and zeta(1+epsilon)=epsilon^{-1}+gamma+O(epsilon) yields the stated exp(1/(lambda epsilon))(lambda epsilon)^{1/lambda} prefactor. Write e=q s-1 and expand log pressure: log P(0)=a t+o(a), first derivative=-1/(2a)+O(log(1/a)), variance O(a^{-2}) in e=O(a^2), hence e/a^2->2t uniformly on bounded t. Unshifted cutoff has t=(log(1/epsilon))/lambda+O(1), still a*t->0, giving 2lambda epsilon^2 log(1/epsilon). Exact harmonic/pressure and mpmath high-precision tests at lambda=.4,.6, epsilon=.02,.03 and t=±1 agree with sign and scaling; finite numerics do not prove limits.

## originality

PASS

PASS. Exact same Zipf-normalized affine model was published October 11, 2026 and establishes the first-order exponential alphabet crossover, but expressly leaves sign and second-order behavior at tau=1/lambda open. The new Euler–Mascheroni threshold prefactor, O(a^2) critical-window profile and log-enhanced signed boundary displacement are not consequences of the earlier first-order statement and are supported by a separate near-pole expansion. Classical pressure equations and first-order phase are not new.

## value

PASS

The earlier paper leaves its critical boundary mathematically unresolved: the exact integer threshold, polynomial prefactor, scaled critical-window profile and strict positive-side asymptotic determine the previously indeterminate transition. This is a motivated sharp boundary refinement with a definite sign, not a vacuous expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
