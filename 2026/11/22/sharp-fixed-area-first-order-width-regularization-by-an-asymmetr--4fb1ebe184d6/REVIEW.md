# Scientific review: sharp fixed-area triangular-corner width response

## Correctness — PASS

The statement concerns exactly one vertex of a unit equilateral triangle, with cut-arm lengths \(s=\varepsilon\sqrt r\) and \(t=\varepsilon/\sqrt r\) for a **fixed** positive ratio \(r\). The proof derives the width change from the four oriented edges, integrates the pair correlation of projected edge lengths, and converts the perimeter-normalized first variation into the displayed coefficient \(C(r)\). The sine-rule conversion between direction and fixed removed area is explicit. The resulting one-variable objective is positive in the open sector, vanishes at both limiting parallel directions, and is uniquely maximized: the derivative numerator \(F\) has exactly one root in \((0,\pi/6)\), proved for the entire real interval using a seventh-term Taylor sign certificate and a uniform tenth-derivative bound. The reflection comparison excludes the other half of the sector. The included verifier checked all symbolic identities, derivative inequalities, endpoint signs, and direct polygon-width quadratures. Finite quadratures are only cross-checks, not the continuous proof.

## Originality — PASS with residual priority risk

Akiyama–Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1 (January 18, 2022), Section 6, establishes the **sign** of the response to parallel and nonparallel truncations, with the underlying edge-correlation formulas. It does not compare the responses of differently oriented cuts at **the same removed area**, and it gives no unique maximizing arm ratio or all-angle uniqueness proof. An accessible geometric-width saddle result for squares concerns a different baseline and infinitesimal deformation space; a known finite-dimensional width-fluctuation optimum for spatial truncations concerns a different random-width functional. Targeted mathematical-index and literature searches found no stronger statement implying the present exact fixed-area optimum. This is evidence of a concrete gap, not a proof of global priority. There remains risk of an unindexed shape-derivative calculation or subsequent treatment of equal-area cuts.

## Mathematical value — PASS

The paper's surprising qualitative observation—an oblique cut improves width uniformity while an equal-arm parallel cut does not—leaves a natural experimental-design question: for a fixed small amount of discarded triangle area, which cut improves the isotropy of projection widths most efficiently? The theorem answers it sharply and uniquely: unequal tip-arm lengths in the ratio \(2.2806265621\ldots\), together with their reflections, yield the maximal order-\(\sqrt{\Delta A}\) gain. The explicit analytic root, nontrivial global sector comparison, and all-angle positivity proof make this a motivated structural optimization, not a renamed sign calculation or arbitrary point evaluation. The result does not claim the global minimizing quadrilateral or finite-size optimality.

## Closest literature and scientific limits

Reference: Akiyama and Kamae, arXiv:2201.06736v1, especially Theorem 1, Lemmas 3 and 6, and Theorem 8 (full accessible text at https://arxiv.org/html/2201.06736v1). The 2024 journal article with DOI:10.1007/s00454-023-00545-6 is the later form of the same work, not a second independent discovery. The theorem here is restricted to one-corner, fixed-ratio asymptotics and does not assert uniformity in a ratio that depends on the cut size. Literature coverage cannot exclude inaccessible or unindexed equivalent prior optimizations.

Self-review: passed. Independent audit: not yet performed.
