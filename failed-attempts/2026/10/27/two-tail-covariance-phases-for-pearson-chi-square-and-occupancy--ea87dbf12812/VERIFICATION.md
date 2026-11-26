---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The covariance formulas, signs, Pell parametrization, and limit are correct, but the Finding's inference of ‘zero dependence’ at its arithmetic zeros is false if read literally: these are zeros of covariance, not independence. At (m,n)=(3,3) one has M_2=1 exactly when X²=2; this event has probability 2/3, despite zero covariance. In fact at every listed Pell zero, n>2, all balls in one box attain the maximum X² and force M_2=0, whereas an occupancy with a doubleton has positive probability. For the exact formulas, condition the collision count on N_1=r: its mean becomes binom(r,2)+binom(n-r,2)/(m-1). Subtract the unconditional mean, multiply by 2m/n and by m times the binomial mass, and simplify to (2). Alternatively, for one fixed pair conditioned to collide, the tagged box contributes f(B+2) and all other boxes contribute f(B); comparing with two independent Bernoulli contributions gives (1). The upward quadratic is negative at its vertex inside (0,n) and positive at both endpoints; the constant sum of the M_r forces at least one negative covariance. The r=2 substitution gives a discriminant of 2(2m−1)²−1; multiplication by 3−2√2 descends the positive negative-Pell solutions to (1,1). Fixed-r Poisson point-mass convergence in the second difference gives (3). An independent bounded enumeration of labelled throws and arithmetic spot checks are replayable with /workspace/branches/independent_small_checks.py. The packaged VERIFY.py was inspected, not executed.

## originality

FAIL

Two distinct earlier findings cover the principal claims, including the exact all-score identity and the finite two-tail spectrum. The Poisson limit and the remaining doubleton computation are direct deductions of the covered spectrum and classical binomial convergence and negative-Pell theory; no direct match for their explicit wording was established or is needed to establish the overlap.

## value

FAIL

The natural Pearson–frequency question has a meaningful answer, but its exact spectrum is already recorded. The remaining work is a fixed-index binomial limit and a doubleton substitution followed by the textbook negative-Pell solution, with no further structural consequence established here. Removing the false independence gloss would not leave a separately supported, valuable new finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
