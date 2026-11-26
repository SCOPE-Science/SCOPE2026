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

For λ>0 the Gaussian posterior on the unobserved coordinates has inverse principal precision. A gap of g edges gives a Dirichlet path on g−1 vertices (g=1 contributes an empty determinant-one block). The determinant recurrence gives sinh(gθ)/sinh θ, differentiation in λ gives the displayed Fθ, and the smallest path eigenvalue yields the stated increasing function of the longest gap. Up to reflection, the gaps are (t,t,3d−2t). Both d±1 are coprime to 3d since 3 divides d, whereas d is excluded. For h=Fθ or −log sinh(θ·), strict convexity makes 2h(t)+h(3d−2t) decrease up to d and increase thereafter. For the trace, the third derivative of x coth x has sign opposite to H(2x), where H(y)=y(cosh y+2)−3 sinh y and H and its first two derivatives vanish at 0 with H'''(y)=y sinh y>0. The negative log-sinh third derivative is also strictly negative. Hence the centered second difference strictly decreases; subtracting the two nearest primitive costs gives Δ²h(d+1)−Δ²h(d−1)<0. The maximum gaps are d+2 and d+1 respectively and any other primitive t has maximum at least d+2. The reflected optimal sets are distinct: a distinct step representing the same set would have to exchange its two nonzero sites with their doubles, forcing 3s=0. Jensen and the maximum-gap bound independently settle unrestricted optima, uniquely up to rotation. At fixed d, Fθ(g) has constant term (g²−1)/6 and θ² coefficient −(g⁴−1)/90−(g²−1)/36. The left and right candidates have equal squared-gap sums and fourth-power sums differing by 48d, giving −8dλ/15+O_d(λ²); the left-versus-balanced squared-gap excess is 6, giving the unit limiting premium. The λ=0 prior is not invoked. The n=9 exact rational example agrees with the path determinants 3,21,55 for block sizes 1,3,4 at λ=1. The checker was inspected, not rerun; it is supplementary, and the observable coordinate shift orbit concerns nominal observability, not forced-state reconstruction.

## originality

PASS

The supported distinct claim is the opposite exact restricted optimizer for spectral norm versus trace and determinant across all masses and these cycle sizes. Unrestricted balanced gap extremizers and their explicit trace costs are closely covered and not new; the closest indexed comparison does not settle the orientation of the restricted gap imbalance. Same-day catalogue dates do not establish priority.

## value

PASS

A generator step is the natural exact condition for a single coordinate to traverse the entire nominal shift orbit. It forbids the free optimum and makes optimizing average or volume uncertainty incompatible with optimizing the worst direction, for every positive mass in an infinite family. The sharp optimizer and loss formulas are usable exact design information, not another statement of equispacing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
