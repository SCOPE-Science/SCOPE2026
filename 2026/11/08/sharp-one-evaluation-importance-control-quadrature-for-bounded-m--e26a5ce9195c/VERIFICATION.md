---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For nondecreasing measurable f:[0,1]->[0,1] and one sampled X~p with estimator f(X)/p(X)+h(X), E[p h]=0, the proposed density p*=1/(2sqrt((x-1/2)^2+c)), c=(4sinh²1)^(-1), normalizes and h*=1-x-sqrt((x-1/2)^2+c) is centered. For each step f_theta, 2h*+1/p*=2(1-x) makes variance identically V*=(coth1-1)/4. Every bounded monotone f is a convex mixture of unit steps (including endpoint constants), so no f has larger risk. For the adversarial step law with F=1/2+(x-1/2)p*, endpoint atoms and interior density, F(1-F)=c p*². The complete-square prior average and Cauchy–Schwarz lower bound force risk>=V* for every admissible (p,h), with equality iff p=p* and h=h* a.e. This proves global minimax and uniqueness within the explicitly stated estimator class. Independent midpoint integration with 30,000 panels gave V* within 6.49e-11.

## originality

PASS

PASS best-of-knowledge: Basak–Bect–Vazquez proved uniform one-evaluation ramp-control variance 1/12 and discussed the open wider nonsequential question; their inspected paper does not provide simultaneous importance-density/control saddle V*. Novak reviews broad integration complexity without this exact restricted one-evaluation saddle. Resultary returned same current result plus separate stratified and antithetic settings, not a stronger one-sample importance-control minimax theorem. The current estimator class is deliberately narrower than all unbiased nonlinear single-query procedures; novelty is asserted only within this class.

## value

PASS

PASS: exact one-query minimax risk with a unique explicit nonuniform sampling density, equalizing control, and a least-favorable step-function distribution solves a natural optimal experimental design problem. It strictly reduces the established uniform-control worst-case variance 1/12 by ~6.09%, which is a motivated sharp improvement with a useful variational characterization rather than an arbitrary constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
