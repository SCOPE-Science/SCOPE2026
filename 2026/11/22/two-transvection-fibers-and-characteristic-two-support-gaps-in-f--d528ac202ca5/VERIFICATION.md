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

Each root direction has q−1 transvections. Equal-direction factors add their parameters, giving q−2 for each nontrivial rank-one output; independent directions give a rank-two operator by independence of their covectors. Every symplectic rank-one correction is a transvection and higher rank is impossible. For rank two, ker(g−I)=W_g^⊥ makes the Wall diagonal well-defined. For each line with Q_g(w)≠0 and w=(g−I)x, the unique first transvection with direction w cancelling the correction at x is T_{w,1/Q_g(w)}; the remainder fixes ker(g−I) and x and is nonidentity of rank one. Conversely, evaluating a factorization on a vector fixed by the second but not the first recovers this line and coefficient. A nondegenerate image yields an SL₂(q) block with no 1-eigenline, and the zero lines of the Wall diagonal correspond exactly to its eigenlines. Independently, fixing trace t counts q(q−1)+q s matrices in SL₂, where s is the number of roots of X²−tX+1: for each upper-left entry a, count pairs with bc=a(t−a)−1. Pairing distinct reciprocal eigenvalues in the split or norm-one torus gives the displayed regular counts, while t=−2 in odd characteristic yields q² matrices including scalar −I. For an isotropic image the quotient by W_g^⊥ pairs perfectly with W_g, yielding a bijection with invertible symmetric binary forms; there are q²(q−1) such forms (subtract q² singular triples from q³). For an odd-q zero line, fixing it allows q(q−1) invertible forms, with two zero lines per split form. In even characteristic there are q−1 invertible alternating forms; a nonzero diagonal is a squared linear form over the perfect field and has one zero line. Counting ordered bases of the two plane types gives D_m and I_m; unique image planes and the rank-one condition q>2 give the two support sizes. Independent complete planar enumeration included zero fibers at seven prime orders.

## originality

PASS

The Wall-line shortening criterion and classical rank-two block classification are prior tools, and there is direct same-day coverage of the dimension-two case in the general-linear convolution. The supported distinct contribution is the full symplectic arbitrary-rank, all-characteristic evaluation by image-plane type, in particular the totally isotropic strata and their zero-fiber contribution to support. No priority is assigned within the same day, and no novelty is credited to the SL₂ values taken in isolation.

## value

PASS

The square of the full transvection sum is a natural first class-algebra convolution. Beyond counting the known local SL₂ blocks, the result separates rank-two targets by the geometry of their image, gives exact multiplicities and support in all field sizes and ranks, and isolates two distinct characteristic-two failures of support: nontrivial rank one at q=2 and alternating Wall forms on isotropic planes. These are useful exact distinctions for factorization or convolution questions, not just verification of a rank bound or root-group normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
