---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: the submitted child-angle sorting recurrences are correct for every 0<y<=x<=1, with three left and two right order regions. For a=1/2,b=x,c=y, H-1=[max(a,b,c)-min(a,b,c)]/min(a,b,c). Each child cannot decrease the minimum coordinate (checked analytically from each halved-largest raw angle and the other entries). On each of the exact piecewise-affine initial-spread / first-child / second-child regions, max affine minus min affine is convex; independent exact rational polygon vertex enumeration checks both mixed orders, all 31 nonempty cells and 61 vertices, giving maximum V2-(3/4)V0=0, and V1<=V0. Since minima are nondecreasing, H(mixed)-1<=3/4(H(parent)-1) and individual child is nonexpanding. For x=y=t∈(0,1/2), exact RL ratio is 3/4, establishing sharpness in nondegenerate shapes. Disjoint pairs plus independent child choices produce expected factor 1-p(1-p)/2 per pair and 7/8 at p=1/2; Markov gives the full-tree tail bound. Independently replicated exact rational certificate, not mere samples.

## originality

PASS

PASS, with close same-object comparison: Michaud's November 4 2026 paper establishes the same LAB shape normalization, one-step Lyapunov nonincrease, strict mixed-step decrease, qualitative almost-sure convergence and full-level concentration. These older statements are not credited as new and do not quantify a uniform sharp 3/4 mixed-block contraction or explicit (7/8)^floor(n/2) finite-level bound. Its conclusion expressly identifies quantitative convergence estimates as future work. Earlier 2019/July 2026 LAB studies concern nondegeneracy and diameter decay. Thus the mathematically distinct sharp quantitative estimate survives, qualified by possible undiscovered estimates.

## value

PASS

PASS: The exact two-step contraction factor is a sharp structural quantitative strengthening of an existing natural triangle-refinement dynamical system, and yields an explicit exponential finite-depth shape-quality tail bound. It measures convergence rate of the entire binary refinement tree rather than restating qualitative almost-sure right-isosceles convergence. The 7/8 factor is only a valid guaranteed rate, not claimed asymptotically optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
