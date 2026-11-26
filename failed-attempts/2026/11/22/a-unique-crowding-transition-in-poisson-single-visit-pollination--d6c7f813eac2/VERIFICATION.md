---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Under the stipulated Poisson marginal law, the single-visit probability really is x e^{-x}; optimizing the expected count does not need independence beyond those marginals. Compactness attains the maximum, but f'(0)=1>f'(x) for x>0 excludes any boundary point by transfer. Equality of derivatives yields at most two branch values, and positive second variation for transfer between two coordinates above 2 excludes more than one overloaded coordinate. The lower coordinate is in (1,2) because the high branch derivative is negative. At n=2 the derivative along the feasible difference is proportional to sinh(t)[B/2−1−t coth(t)], with t coth(t) strictly increasing on t>0; the unique asymmetric critical point for B>4 is feasible. Its Taylor expansion gives the claimed continuous onset. At any n the log of the ratio to the uniform objective is a log-mgf in B for fixed shares, so its maximum over shares is convex and nonnegative. The set of budgets of uniform global optimality is a closed interval from zero, bounded above by comparison with n−1 visits fixed at mean one. Strict convexity for unequal positive shares excludes any early tie (an optimizer is interior). At n≥3 the feasible one-high perturbation at B=2n has a strictly positive cubic gain, giving B_c<2n. Compactness yields a threshold co-optimizer from above, which cannot be the uniform point by strict concavity in a common neighborhood of its coordinates; thus the gap is bounded away from zero just above the threshold and the co-optimizer (n−1)y+x with y>1,x>2 gives B_c>n+1. The large-budget limit then follows from f'(y)=f'(x)→0 as x→∞. Independent replay: python /workspace/independent_checks.py (pollination routine), parameterizing the stationary pair by r=x−y and y=1+r/(exp(r)−1), finds the equal-value solution on the increasing budget branch B=n y+r at n=3: B=5.774313471725124760 and r=1.397499519593884473. This is numerical corroboration, not an all-n argument or an interval certificate. The submitted notes and checker were read without executing the submitted script.

## originality

FAIL

Direct mathematical coverage is established by distinct same-day catalogue records, especially Steele photoinhibition 904d722bd814 and first-order Ricker recruitment 7678a45b7053. Both state the identical fixed-sum optimization for all real positive budgets and all n≥2, the very same two-site continuous threshold and the same many-site discontinuous threshold; both actually characterize the co-optimizers more precisely. The sharper-looking lower bound n+1 is immediate from their stated threshold co-optimizer. Their explicit branch formula implies the hyperbolic n=2 formula and its expansion, and the high-budget behavior. Different application language and a different proof of interval-shaped optimality do not make a new mathematical theorem. This is demonstrated duplicate coverage, not an inference about which same-day record was first, authorship, or attribution.

## value

FAIL

The global symmetry-breaking phenomenon would be structurally valuable as a new theorem. Here it is already available for the identical objective with stronger optimizer information. Restating it as flower viability adds no new constraint, empirical validation, or mathematical phenomenon, and the printed n+1 refinement and critical expansion are immediate from the existing optimizer formulas. The proof's log-mgf argument is a useful alternate exposition, but the frozen result offers no distinct scientific consequence from it. There is no substantial surviving repaired claim on this evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
