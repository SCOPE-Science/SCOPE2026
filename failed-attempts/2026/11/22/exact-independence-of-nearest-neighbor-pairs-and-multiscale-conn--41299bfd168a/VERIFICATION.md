---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Rotate a uniformly marked sampled site to the origin. The other n-1 positions remain iid uniform relative to it, so their ordered positions give the Dirichlet(1,...,1) indexed gap vector. Its density is symmetric, and the rank permutation is uniform conditional on the entire increasing gap vector. At any vertex, a shortest route toward another site starts across one of two incident gaps; the smaller incident gap is at most 1/2, reaches a neighbor, and no other endpoint is closer. Hence reciprocal pairs are precisely strict cyclic minima of the gaps, including configurations with a gap above 1/2. For r<1/2, any geometric edge has a short arc of length at most r, so it can be replaced by a path across consecutive gaps each at most r. Conversely each consecutive gap at most r gives an edge. Thus the components are exactly those of a cycle with Q_r long-gap edges removed, numbering max(1,Q_r); the formula has the stated singleton and connected limits at r=0 and r>=1/2. The entire path is therefore a measurable function of the sorted gaps and independent of the rank-only pair count. Each minimum indicator has mean 1/3. For n>=5 adjacent minima are incompatible, two indices at distance two are jointly minima with probability 2/15 (for example, integrate 2*(1-x)^2*(x-x^2/2) for x in [0,1] over five independent continuous ranks), and disjoint rank neighborhoods are independent. This gives variance n*(2/9-2/9+2/45)=2n/45. For n=3 the minimum is unique, and for n=4 there are two minima exactly when the bottom two ranks lie opposite, with probability 1/3. The supplied verification and checker were inspected, not run; rank permutations at n=3 through 8 and the three tested profiles do not replace the process-level proof. None of this establishes independence from the component sizes or isolate count.

## originality

FAIL

The main claim is mechanically covered by the exact prior rank argument for the very same circle model and reciprocal-pair count. Resultary bcec85e2394a, dated 2026-10-18, explicitly identifies the count with cyclic local minima and conditions the uniform rank assignment on the entire increasing gap vector, not just on one threshold count. The variance for n>=5 also follows by summation of the already published cyclic local-minimum covariance kernel fb83bca256ed. The simple cycle-cut identity and the two elementary boundary moments do not supply a distinct substantive remainder of the submitted claim. This is affirmative evidence of coverage, not a failure to access external literature.

## value

FAIL

Distinguishing component count from isolate count is a useful exposition of why cyclic placement matters. But for this narrow invariant the whole-path conclusion follows immediately by applying the already established same-model conditional rank lemma to a symmetric gap-count path, via the elementary cycle-cut rule. The stated variance is already determined by the cyclic covariance kernel for n>=5. The remaining n=3 and n=4 checks are elementary exceptional counts without a separate substantive motivation. There is no nonroutine surviving exact fact in this submission that independently justifies acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
