---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS. The finite dyadic Haar signed transform has at a leaf x an exact row-kernel partition by the first branching depth. Putting b_0=1 and b_(j+1)=(b_j+sigma_j)/2 gives exact row norm sum_j(1-sigma_j b_j)/2+|b_d|. The Bellman recursion F_0(b)=|b| and F_h(b)=max_sigma[(1-sigma*b)/2+F_(h-1)((b+sigma)/2)] preserves F_h=a_h+c_h|b| with a_h=a_(h-1)+(1+c_(h-1))/2, c_h=(1-c_(h-1))/2. It proves U_d=2d/3+5/9+(4/9)(-1/2)^d for all d>=0, and kernel sign choices attain each maximal row. Independent brute-force path optimization through d=9 gives 1,1,2,5/2,13/4,31/8,73/16,167/32,377/64,839/128; these are checks, not the all-depth proof.

## originality

FAIL

FAIL on best available mathematical-priority evidence: two independently published stronger November 8 results directly cover the complete fair dyadic depth law. Sharp endpoint unconditionality on biased binary filtrations gives an exact formula for every product splitting probability and explicitly states the fair r=1/2 case is previously known and not new. Depth-only endpoint unconditionality and exact dimension spectrum of adaptive Haar trees gives U(T)=F_H for every finite fair proper binary tree and calls the full complete-depth formula the already-known baseline; its full balanced tree specializes identically. Although all three records share November 8 and the sub-day public ordering was not independently established, both stronger texts positively identify the exact candidate formula as a pre-existing input rather than a novel open classification. No standalone original remainder is demonstrated by this submission.

## value

FAIL

FAIL as distinct new research: the exact signed Haar endpoint norm is a mathematically natural and correctly proved baseline, but the submitted complete-depth value and optimizing-path rule are subsumed by stronger published fair-tree and biased-product classifications treating it as established. As submitted it recomputes the known boundary, without another unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
