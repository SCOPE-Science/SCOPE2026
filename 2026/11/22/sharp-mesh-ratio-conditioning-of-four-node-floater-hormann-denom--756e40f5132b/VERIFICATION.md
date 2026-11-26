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

For the three specified local-window terms, clearing the positive common denominator in the first gap x=x_1−q gives numerator −[q²+bq+(a+b)(b+c)] for their sum, while the only positive term gives numerator q(a−q). This gives the reported formula; reflection gives the right gap, all terms are positive in the middle, and the nodal limits are 1. In an outer gap of length L the derivative has sign LC−2Cq−(L+b)q², strictly decreasing through one zero in (0,L). At the shorter gap's interior maximizer, the larger gap gives a strictly larger value if their lengths differ. Scale the least gap to 1 and put L=max(a,c), s=min(a,c). Then C=(L+b)(s+b)≥2(L+1), b≥1 and L≤μ. The envelope 2q(L−q)/[q²+q+2(L+1)] increases strictly with L at a fixed interior q. At L=μ its maximum occurs at the positive root of q²+4q−2μ=0. The factor there is (q+1)²/(2q+1), giving the bound and its limit after division by sqrt(μ). The strict inequalities force b=s=1, L=μ, and that q for equality, including both reflected points when μ=1. For two or three nodes there are respectively one or two local terms, with no opposite signs on any interior cell. This is a continuous-extension and exact-arithmetic result, not an assertion about a different grouping of barycentric terms.

## originality

PASS

The local denominator factor and mesh-ratio bounding problem are established in Fuda–Campagna–Hormann. Their primary Eq. (26) concerns the same grouped terms, but their general Theorem 3 yields 1+μ²/2 at d=1 and does not give the sharp four-node factor or equality pattern. The available distinct indexed result is for a different invariant. Credit is limited to the attained four-node envelope, its location and equality classification, and the precise onset of cancellation for the grouped degree-one terms.

## value

PASS

The first-barycentric denominator summation factor is motivated by first-form stability, and four nodes are the first degree-one configuration where cancellation is possible. The exact worst case reveals sqrt(μ) growth at that cutoff and pinpoints the mesh and evaluation points responsible; a general O(μ²) guarantee cannot supply that benchmark. This identifies sensitivity of a specified computation, not a universal lower bound on errors of all implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
