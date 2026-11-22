# Scientific review — normal-line distance of coaxial ellipses

## Correctness — PASS

The support-point identity \(x=h n+h't\) identifies the signed offset of the normal line with the angular support derivative. Thus the normal-line pseudometric equals half the total variation of the support difference, using precisely the factor \(1/2\) from the defining paper. For two concentric coaxial ellipses this reduces to twice the variation of \(H(u)=\sqrt{b^2+Au}-\sqrt{d^2+Cu}\) on \([0,1]\). Squaring two nonnegative terms shows that the sign of \(H'\) is controlled by one affine polynomial. Its endpoint signs give an exhaustive regime partition, including circle cases, degenerate transition equalities, and exactly one interior stationary point when the signs differ. Elimination at that stationary point proves the stated radical. The strict inequality then follows from genuine reversal of monotonicity. The exact nested example is independently checked in rational arithmetic. A standalone seeded quadrature test agrees with the analytic formula on 252 configurations, including 40 interior switches; it is not a substitute for the proof.

**Residual correctness risk:** None identified in the stated co-axial domain. The result does not address translated or independently rotated ellipses, and no finite numerical test establishes the universal claim.

## Originality — PASS (subject to independent priority review)

Akopyan–Glazyrin, arXiv:2308.16340v1, define the normal-line pseudometric and derive the normal-offset integration mechanism in Lemma 2.6. The definition, pseudometric property and elementary support-variation conversion are prior tools, not new claims. The paper contains no four-parameter ellipse distance law, axis-derivative sign test, interior-switch radical, or equal-gap nested example. Cieślak–Martini–Mozgawa, *On Holditch's theorem*, DOI:10.1007/s00022-020-00536-5, treat extremal chords and intersecting normals of individual ellipses, which do not imply the pairwise normal-line distance formula. Additional literature and semantic-index queries under support-function variation, paired ellipses, and normal-line distances yielded no directly covering statement. Other ellipse-pair studies of *Minkowski-sum area under rotation* concern a different functional, not this distance; the objects overlap but the functional and conclusion do not. The evaluated special family requires the complete sign and stationary-point analysis rather than simply a stated special case of the defining paper.

**Residual originality risks:** A classical total-variation or support-function calculation might implicitly contain this ellipse evaluation under a different name. The general normal-line representation is already known and should not itself be presented as a discovery. Semantic retrieval is not a proof of uniqueness.

## Mathematical value — PASS

A geometry paper introduced a natural pseudometric precisely to compare normal-line bundles of convex boundaries. Its exact behavior on the canonical four-parameter family of centered coaxial ellipses is a motivated calibration question. The formula is a complete classification across all positive semiaxes, with a sharp algebraic phase boundary, an exact strictly positive correction in the switching regime, and a concrete nested counterexample to the appealing one-parameter semiaxis-gap prediction. The general kernel observation clarifies exactly which differences this pseudometric ignores. The content is more than numerical approximation or a custom parameter slice; it distinguishes first-order normal geometry from endpoint axis disparities and is relevant for interpreting or computing the distance.

**Value limits:** No global comparison across arbitrary rotations or translations, and no additional disjoint-perimeter theorem, is claimed. The basic variation identity is elementary background; the new value resides in the complete ellipse phase law and its geometric separation phenomenon.

## Closest literature and limits

- A. Akopyan and A. Glazyrin, *On the total perimeter of disjoint convex bodies*, arXiv:2308.16340v1 (30 August 2023), especially Definition 2.1, Proposition 2.3 and Lemma 2.6.
- W. Cieślak, H. Martini and W. Mozgawa, *On Holditch's theorem*, *Journal of Geometry* 111, article 24 (2020), DOI:10.1007/s00022-020-00536-5, especially the ellipse normal-chord analysis.

Self-review: passed. Independent audit: not yet performed.
