---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For alpha,s in (0,1), monotone common-uniform coupling of Bernoulli(X) makes the state separation shrink in expectation by c=1-alpha(1-s)<1, hence unique invariant distribution in W1. Stationary conditional mean gives 1/2 and conditional variance gives V=alpha*s^2/(4(2(1-s)-alpha(1-2s))). Under affine Y=(X-(1-s)/2)/s, both update similarities have ratio r=1-alpha and positive probability >=(1-s)/2, so support is whole interval when r>=1/2 and Cantor attractor when r<1/2. At alpha=1/2 the stationary reversed action process codes Y_0 as sum 2^-j B_-j; its entropy rate is E H(X_0)<log2. Standard ergodic SMB typical cylinders of total Lebesgue length tending to 0 give singularity and dimension <=h/log2; Pinsker and the exact V produce the displayed strict dimension defect. Each individual coding has probability <=(1-a)^n so no atoms at critical or separated alpha. Independently exact rational recurrences at (alpha,s)=(1/2,1/2),(1/3,1/4),(3/4,2/3) confirm stationary variances 1/32,1/256,1/11 and contraction c=3/4. No claim of absolute continuity alpha<1/2.

## originality

PASS

Existing random-action opinion literature with one stubborn agent converges to that agent, not a stationary law under two opposed stubborn actions. Cao-Cortez equal-mean mean-field persuasion has iid, fixed-bias branch choices, yielding a uniform critical law, whereas here branch probabilities depend on current X and make the critical interval law singular. Standard place-dependent IFS and entropy results supply proof methods, not the exact two-zealot feedback model, stationary V or quantitative critical singularity. Best-of-knowledge novelty with source-model and literature risks.

## value

PASS

A full-support yet singular invariant opinion measure at the exact overlap threshold is a structural counterexample to inferring density from support. The quantified entropy-dimension deficit reveals a mechanism specific to endogenous action feedback and distinguishes it from iid Bernoulli convolutions. Natural three-agent model is small but the phenomenon is genuinely dynamical and not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
