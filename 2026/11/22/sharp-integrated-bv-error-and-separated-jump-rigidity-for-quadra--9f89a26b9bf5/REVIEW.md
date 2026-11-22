# Scientific assessment

## Correctness — PASS
For every \(n\ge2\), the explicit two-piece quadratic response of a unit step at each interior Greville gap has integrated error \(h(1/3+v^2-|v|^3/3)\), maximized at \(13h/24\). The boundary gaps have coefficient no more than \(h/3\). The finite signed-measure representation of right-continuous \(BV\) gives the universal bound. Exact residual support signs prove the complete equality class: atomic derivative at interior Greville nodes with pairwise nonconsecutive indices. The independently implemented rational checker passed 1,710 step tests, all tested sharp site values, and partition/affine identities. Risk: numerical checks are finite and do not independently certify the universal proof; the pointwise BV representative condition is essential.

## Originality — PASS (qualified)
The full arXiv HTML of Nagler–Kähler (2013) and the full available treatment of Nagler–Cerejeiras–Forster (2014) concern continuous-data moduli and operator spectra, rather than the sharp sampled \(BV\)-to-integrated-\(L^1\) identity-defect. Levin–Gruberger (2025) treat adapted discontinuity-aware spline quasi-interpolation rather than this fixed positive quadratic operator's norm. The closest published quadratic cardinal B-spline result establishes total-variation amplification of a *different* corrected bi-infinite operator; reading its RESULT.md confirms the differing output seminorm, correction parameter and domain. The 2002 Beutel et al. quantitative-inequality paper was only partially accessible, so older equivalent results remain a priority risk. Searches and comparisons are recorded in AUDIT.json; absence of a search hit does not prove uniqueness.

## Value — PASS
The exact coefficient is a natural stability metric for positive \(C^1\) spline smoothing of discontinuous one-dimensional signals. It quantifies the cost of the extra spline smoothness against canonical piecewise-linear interpolation, namely an exact \(1/12\) increase in worst integrated BV error, and classifies precisely when multiple jumps preserve sharpness. It is not an arbitrary fixed mesh enumeration: the coefficient and equality geometry hold for every uniform mesh size \(n\ge2\). The claim is restricted to right-continuous representatives, not arbitrary \(L^1\) classes.

## Closest literature and limitations
Nagler–Kähler, arXiv:1312.5546; Nagler–Cerejeiras–Forster, arXiv:1402.2403; Beutel–Gonska–Kacsó–Tachev (2002, complete text not verified); Levin–Gruberger (2025); and the published 2026 quadratic cardinal spline variation theorem. Nonuniform knots, higher degrees and integral-sampling operators remain outside the theorem. Independent historical-priority and mathematical audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
