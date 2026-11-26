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

Independently reconstructed the mean by first exit from the bulk and then renewal at the attached states. The two-heading exit equations with outward absorbing states give right-exit probability 1/2+h/A from the unbiased start and first-exit mean L/(2v)+alpha*x*(L-x)/v^2. After inward release at either wall the crossing probability is 1/A and the excursion mean is L/v. Thus the attached means solve (kappa_j+beta/A)W_j-(beta/A)W_other=B, with determinant kappa_0*kappa_L+beta*K/A>0 even at the endpoint allocations. Each released excursion has a uniformly positive probability of reaching the reactive wall and killing there on that visit; holding and exit times have bounded means for fixed parameters. This gives finite mean and validates the renewal system, including boundary starts. Weighting its solution by the exit probabilities reproduces the boxed mean. The derivative numerator G in RESULT.md is strictly increasing since c+h*delta is positive, and inserting the extreme allowed h at +/-K gives the stated strict endpoint signs. The rationalized quadratic picks the unique interior root, zero exactly at the midpoint. Dividing by K yields beta*(h+A*t)+(AK/4)*(h*(1+t^2)+A*t)=0, monotone in t. For h>0 the root is below -h/A, making the K derivative of the left side positive there and t strictly decreasing; reflection treats h<0. The small- and large-budget root equations give the claimed limits. The large-budget limiting root lies strictly inside (-1,1), so the time quotient may be expanded uniformly around it and gives the stated K^-1 coefficient. At the left wall h=-(A-1)/2 reproduces the positive distant share. Inspected checker.py and its reported 1,440 cases; did not rerun it or use records of finite tests as proof.

## originality

PASS

The process, boundary kinetics and first-passage framework are established and the mean is derivable from them. The supported distinct claim is the global physical-rate allocation theorem, its budget crossover and the distant-wall strong-budget limit. Neither the strongest same-process comparison nor the closest fixed-budget analogues inspected supplies that claim.

## value

PASS

A linear budget of two physical killing rates is a natural design constraint, unlike an arbitrary parameter slice. The law resolves whether one should concentrate or split at all launch locations and budgets. A positive remote allocation fraction even for a wall launch meaningfully distinguishes the fixed finite-speed large-budget regime from the corresponding Robin diffusion regime. This is not a uniform joint Brownian/strong-budget limit, a result about passage-time variance, or an empirical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
