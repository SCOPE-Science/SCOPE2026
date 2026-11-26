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

The images of the proposed bands are exactly each other: the left segment of the lower band already covers the upper band, the lower-band right endpoint maps within it, and the upper-to-lower passage is the decreasing affine bijection. Thus each band has mass one-half; the upper conditional law is the reflection of the lower one. Composing in the proposed coordinates gives R_s with slopes -2s and s² and turning point a_s=1/(2s). Two right visits give R_s²≤1341/4096<4/9≤a_s, so the inducing and uniform bounded-return assertion holds. The branch that vanishes as s→1 requires care: bounded distortion alone does not justify uniform BV estimates. Independently, rescale the induced base to [0,1]. Its two full decreasing branches have domain lengths p1=1/(2s), p2=1/(2s³), and its leftmost short branch has length σ=1-p1-p2, inverse slope p3=1/(2s⁵) and image [0,d] with d=σ/p3. For s close to 1, σ<d<σ+p2. The twice-iterated induced transfer operator has the sum of restrictions' interior variations bounded by (1/4)Var(f), since all inverse slopes for two steps are at most 1/4. There are four additional endpoint contributions from non-full images: one at an input trace near each of 1/2 and 1, and two near 0. Indeed each full branch pulls back the short branch once, and the short branch's image cuts only itself and the middle branch. Estimate these traces by Var on three disjoint fixed neighborhoods of 0, 1/2 and 1 plus the L1 average on each neighborhood. The maximal multiplicity is two, giving Var(P_s² f)≤(3/4)Var(f)+C||f||_1 uniformly near 1. Iterating and using L1-contractive approximation by BV functions bounds the variation of all invariant densities. On continuous test densities the two full inverse maps converge uniformly and the short-domain contribution tends to zero in L1; L1 contraction extends this operator convergence to all L1. BV compactness and the two onto slope-2 branches of the limit identify the unique normalized limit (constant on the induced base). The bounded-return lift converges in L1 by its finite affine pushforward formula (the disappearing branch has vanishing mass). In unrescaled base coordinates its normalized first-return law is density 2 and the return-time mean is 3/2; the stationary lower density is 4/3 on the first half and 2/3 on the second. Its mean is 5/12. Substituting both affine coordinates into the balanced band means gives 3/4-ε/2+2ε²m_s exactly and hence coefficient 5/6. At ε=0 every positive orbit enters the involution interval; its empirical law is that of its individual one- or two-cycle, and each such orbit law has only countably many initial points. The exceptional point 0 also has zero-measure basin. This verifies the boundary assertion independently of the expanding argument. I inspected VERIFICATION.md and verify.py as finite rational diagnostics, not as a proof of the stability step.

## originality

PASS

Pass is for the microscopic invariant measures along the collapsing band pair and the consequent second-order mean asymptotic. The underlying band geometry and the stationary density of the reflected static limiting return map are covered and are not independent originality claims. The decisive further step concerns a parameter-dependent normalized return system with a disappearing branch; the stronger looking band classifications and static Markov laws do not supply it.

## value

PASS

This addresses a genuine singular stationary-law question: two bands collapse onto neutral period-two data, while the limiting map has no physical law selecting that orbit. The microscopic density separates stationary mass across the two halves in a way the support endpoints do not determine, and yields the first nontrivial stationary-mean coefficient beyond the geometric first-order term. The value is in that selection and quantitative correction, not the known static plateau solution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
