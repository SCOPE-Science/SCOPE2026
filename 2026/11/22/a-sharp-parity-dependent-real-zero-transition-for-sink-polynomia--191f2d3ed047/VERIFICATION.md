---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two central-edge orientations contribute (1+z)^2[(1+z)^b+z-1] and the swapped expression. With u=1+z and d=b-2, the residual factor is F_b(u)=2u^b+(u-2)(1+u^d); F_b(0)≠0 and F'_b(1)=b+4, giving the stipulated multiplicities. Comparing u^b to u^d and (2-u)(1+u^d) to 2u^d settles signs on (0,1) and (1,2); u≥2 is positive. For even b the negative-u polynomial has a single sign change, including b=2, and its sign at t=-u=1 is negative. For odd b the roots must be in 1<t<ρ, where H_d(t)=t^d(-2t²+t+2)-(t+2) increases with d. Independently recomputed the d=11 certificate: the coefficients through degree four of -H_11(1+x) are 2,-7,-20,22,275 and all higher ones are positive; its quartic on [0,1/4] has Bernstein coefficients 2,25/16,11/12,19/128,107/256, and at 1/4 its value, first and second derivatives are positive with second derivative increasing thereafter. The exact d=13 value at t=6/5 is 6829302128/30517578125>0. With negative endpoint signs and the two-sign-change bound, this gives exactly two simple zeros above the odd threshold. Pointwise eventual positivity inside (1,ρ) forces the two t-roots to the interval endpoints; z=-1-t reverses their order. Degree b+2 then gives real-rootedness only at b=2. Inspected the finite verifier and its documentation but did not execute the uploaded program. The exact certificate can be replayed via binomial expansion and the Bernstein basis conversion in RESULT.md lines 52–65.

## originality

PASS

The supported distinct claim is the all-b real-root census on the actual double-star tree, especially the exact last-failing odd b=13 and first-succeeding b=15. The known sink enumerator and elementary polynomial evaluation are not the novelty claim. The most similar line-graph theorem has different graph and hypotheses, and the nearest distinct Resultary records have different graph families. This is a bounded assessment, not a priority certificate.

## value

PASS

The family gives a simple branching-tree boundary case for sink-polynomial real-rootedness outside the known claw-free scope. The result is not just a small-parameter list: it fixes both parities for every b, exhibits a finite creation threshold with simple roots, and determines limiting positions. The threshold requires genuinely more than obtaining the polynomial or bounding its possible real zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
