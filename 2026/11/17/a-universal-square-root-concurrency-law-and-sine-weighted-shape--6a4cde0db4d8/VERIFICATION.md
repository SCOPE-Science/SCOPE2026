---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: Normalize the base triangle by an invertible affine map. Independent uniform arclength fractions stay iid uniform on (0,1), and area fraction is invariant. Direct affine-cevian algebra gives Z=T^2/Q with T=H(w-w0), H=uv+(1-u)(1-v)>0, w0=(1-u)(1-v)/H, and positive Q=(1-u+uv)(1-w+uw)(1-v+vw)<=1. Therefore a one-dimensional sqrt-epsilon tube around the Ceva surface contributes 2 sqrt(Q0)/H for each (u,v); the global bound 2/H is integrable (linear corner singularities only) and proves dominated-convergence asymptotic. Barycentric coordinates of the first intersection P obey u=b/(b+c),v=c/(a+c). The measured Jacobian from a,b to auxiliary triangle angles was independently finite-differenced at three generic/equilateral points and equals A′B′C′/2, giving sqrt(Q0)/H du dv=(sin alpha+sin beta+sin gamma)/8 d alpha d beta. Integration yields 3pi/8 and thus 3pi/4 sqrt-epsilon. On compact parameter sets the signed normalized defect s=sgn(T)sqrt(Z/epsilon) changes coordinates smoothly with locally uniformly convergent densities; dominance controls boundary tails, proving joint L1/total-variation convergence. Resulting angular density is (sin alpha+sin beta+sin(alpha+beta))/(6pi) on angular simplex times s in (-1,1), and acute auxiliary probability 1/pi. Independent 300k-sample Monte Carlo ratios at epsilon .02/.005/.001 were 2.140/2.250/2.314 approaching 3pi/4=2.356; those finite experiments do not prove the asymptotic.

## originality

PASS

PASS best-of-knowledge: classical Routh/Ceva area identities and the generalized deterministic formula are known. Full primary Bényi–Ćurgus (2012) explains those deterministic ratios; the published 2026 fixed-product envelope is also deterministic. Neither states the exact probability from independently and uniformly sampling one point on EACH of three sides, nor the sine-weighted marked total-variation law of the auxiliary intersection-angle triangle. Generic geometric probability tube formulas do not imply the evaluated 3pi/4 coefficient and explicit angle bias without this model-specific Jacobian. Unindexed older probability papers remain a genuine historical uncertainty.

## value

PASS

PASS: Random near-concurrency is a geometrically natural singular event and the square-root law plus its universal coefficient is an exact invariant of affine-uniform cevian sampling. The full conditional angular law, the uniform signed defect, Beta half exponent and 1/pi acute probability are nontrivial predictive shape information useful beyond a classical deterministic Routh identity. Both a precise rare-event asymptotic and complete marked conditional limiting distribution are motivated by Ceva degeneracy; not a routine random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
