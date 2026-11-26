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

The incidence map on a tree is onto edge coordinates and has independent rows, so prescribing active upper differences and strict interior values elsewhere defines a feasible potential. On a fixed face the tangent space is constant on active forest components, hence the derivative of weighted projection is mass-weighted averaging there. For every forest F, choose all active multipliers strictly positive at y=u+M^{-1}D_F^Tλ. The affine face solution and its multipliers depend continuously on y; strict slack and positivity give an open cell with that derivative. The global Lipschitz constant equals the maximum of the resulting local norms by finite piecewise affinity and continuity along segments, and arbitrary small finite perturbations realize the local ratios. In vertex space modulo constants the indicators of the two sides of each original edge cut, with one side chosen per edge, give the ℓ¹ edge-gradient basis. Thus the norm is the greatest output TV of one such indicator. For an inactive cut it is unchanged; for an active cut its only output jumps are on the boundary of its active block B, where the common average is M_A/(M_A+M_C). Counting jumps on each side gives the stated b_A M_C+b_C M_A numerator. Any connected B and internal cut occurs by taking exactly its internal edges active. The empty forest gives baseline 1. Paths have at most one external edge per cut half; for a star the block consisting of the center and one leaf maximizes each corresponding term. In the six-vertex example the total boundary of B is at most three and each cut side has at most two external edges. Boundary three forces B⊆{0,1,2}, with maximum 5/3 realized by all three and the cut 01. If the boundary is at most two, unit masses and |B|≤6 bound the ratio by 2(1−1/6)=5/3. Both spine halves in the caterpillar have q−1 external leaves when the whole spine is active, giving the stated lower bound.

## originality

FAIL

The mathematical finding is correct, but the exact invariant and its advertised examples do not establish a distinct result over the published local cut calculus. The closest tree-isotonic finding gives the same exact formula and attainability for counting masses, and the bounded-slope finding already carries that calculus to hard symmetric bands by showing that every active forest occurs. The arbitrary-mass cut calculation is mechanically implied by that prior local formula via vertex replication, not just analogous to it. For rational-proportional masses replace each vertex v by a connected tree of p_v vertices with p_v proportional to m_v, retaining one connecting edge for each original tree edge. Activate all edges within each fiber and the edges corresponding to the original active forest. Lift an original edge-cut indicator to be constant on fibers: it is precisely the corresponding connecting-edge cut indicator on the inflated tree. Arithmetic active-block averages on that tree are the original mass averages; both input and output TV are unchanged because no within-fiber edge contributes. Thus the prior per-forest, per-edge formula gives every weighted column, not only an upper bound from a potentially larger inflated-tree maximum. Continuity of finitely many mass ratios extends this to real masses. For the fitting map, shifting by a tree potential with edge increments equal to the band midpoints centers arbitrary bands, and the existing strict-face construction works verbatim with each edge's own radius and with M^{-1} applied to the normals. This does not assert that an earlier source states the weighted nonlinear fit itself, or that one-sided isotonic regression and slope-band regression are the same map. It shows that the claimed exact invariant is a direct consequence of the existing calculus on the unchanged family of active forests. The separate weighted-star result already contains the claimed star constant; the equal-mass examples are evaluations of the known cut formula.

## value

PASS

The sensitivity question is meaningful: weighted least squares is nonexpansive in its native norm, which does not control amplification of differences in tree variation. An attained cut expression and a subcubic family with unbounded gain are useful for diagnosing that distinction in hard-band fits. This is value of the mathematical result and its application, not credit for the cut calculus or instability phenomena as new contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
