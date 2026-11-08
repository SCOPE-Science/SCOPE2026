# Scientific review: three even pair-distance moments of triangles

## Correctness — PASS

The claim is for two independent area-uniform points in every nondegenerate Euclidean triangle. The Dirichlet factorial identity and squared-distance polarization formula lead to three exact symmetric polynomials, checked by an independent rational-polynomial expansion in `verify.py`. Their triangular inverse is algebraically explicit. Heron's identity gives the area formula and the exact strict feasibility boundary. At fixed first two moments, the squared-side solutions form a circle lying wholly inside the positive orthant; Lagrange extrema of the third elementary symmetric polynomial occur at isosceles triangles, and connectedness gives the full interval. The endpoint examples show that three even moments are necessary in general. Random sampling checks supplement, not prove, these claims. The proof does not concern noisy empirical reconstruction.

## Originality — PASS, with historical-priority limits

The 2013 triangle point-distance paper and the 2016 polygonal extension compute forward distance laws. The 2017 *Moments of volumes of lower-dimensional random simplices are not monotone*, Proposition 4, already computes arbitrary pair-distance moments, so **forward moment formulas are prior content, not a novelty claim**. Li and Qiu (2016) study a *fixed vertex to one random interior point*, a distinct sampling model. The new proposition concerns the exact minimal inverse, two-moment recovery of area, and the complete conditioned range of the sixth moment, with sharp isosceles endpoint geometries. Inspected statements in the complete accessible 2017 and Li–Qiu articles do not establish this finite moment-region classification. The accessible 2013 manuscript representation did not supply the full document; uninspected sections and unindexed earlier inverse-moment work remain genuine priority risks. Search failure alone does not certify uniqueness in the literature.

## Mathematical value — PASS

The observable is a natural unlabeled distance between two uniform interior points. Its full distribution has an established geometric-probability role; replacing inversion of a piecewise distance distribution by **exactly three low-order even moments** is a concrete finite inverse theorem. The complete feasible moment region distinguishes admissible data from impossible triples and identifies the sharp ambiguity left by two moments. Notably, those first two moments already determine triangle area while failing to determine triangle shape. This is not a special-case evaluation of the known full moment formula: the inverse and conditional endpoint classification require additional global geometry and an attainment argument. The result is exact but does not claim statistical robustness or a higher-dimensional generalization.

## Closest sources and limitations

F. Tong, M. Ahmadi and J. Pan, arXiv:1312.2498 (2013); F. Tong and J. Pan, arXiv:1602.03407 (2016); *Moments of volumes of lower-dimensional random simplices are not monotone*, DOI:10.1007/s00605-017-1077-3, Proposition 4 (2017); H. Li and X. Qiu, DOI:10.1155/2016/8371750. The 2017 result explicitly dominates all **forward** moment evaluations, but not, in its inspected statement, the finite inverse/attainable-region conclusion. A complete bibliographic-priority search cannot be guaranteed. The theorem supplies a proof and reproducible check; no independent audit or noisy-data stability theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
