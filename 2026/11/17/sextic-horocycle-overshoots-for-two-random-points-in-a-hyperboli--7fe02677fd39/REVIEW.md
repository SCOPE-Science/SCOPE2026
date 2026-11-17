# Self-review of the horocycle overshoot theorem

## Correctness — PASS

The statement fixes curvature, quotient, sampling measure, intrinsic minimizing geodesic, level \(H\), and independent marks. The upper semicircle apex criterion is proved by the strictly increasing horizontal-span function of its radius, including the boundary case of an apex outside the segment. The positive height-to-offset Jacobian gives the exact integral. Both coefficients follow from explicitly evaluated simplex integrals; the remainder follows from a uniform expansion on a compact domain. After an exact change of variables, the marked density converges uniformly after normalization to a beta–Dirichlet product with \(O_w(H^{-2})\) total-variation bound. The independent sign and initial phase follow from quotient translation symmetry. A standalone standard-library checker verifies the geometry and corroborates finite-threshold integrals. Numerical samples and quadrature are not treated as proofs.

## Originality — PASS, with residual historical risk

The closest full mathematical record on **the same truncated cusp** determines the *two-point intrinsic geodesic distance* distribution, not the maximum height of the connecting geodesic subject to endpoints below a high horocycle. Its result does not imply the exact sextic excursion law or the marked total-variation law. A second full record treats distances of points in ideal hyperbolic polygons, a different random geometry. Haas (arXiv:0709.0313) and Gadre (arXiv:1408.5812) investigate excursions of a typical long geodesic or ray, not an independently area-sampled finite endpoint pair. Borthwick (arXiv:1006.5478) studies spectral resonance estimates and gives background cusp coordinates. Searches using terms for horocycle height, endpoint-below-threshold events, geometric overshoots, Dirichlet marks, and geodesic cusp excursions returned no equivalent claim. No failed search is interpreted as proof of uniqueness; obscure earlier geometric-probability or cusp excursion literature remains a genuine priority risk.

## Mathematical value — PASS

The event is geometrically canonical: a shortest segment enters a deeper horocycle even though neither endpoint lies there. Its sixth-order rarity is a non-obvious effect of a **double near-tangency constraint** and its sharp positive constant recovers the original boundary horocycle's circumference. The second asymptotic term and universal conditional beta–Dirichlet structure quantify how an exceptional segment achieves the excursion. This is an intrinsic finite-chord statistic, not a routine restatement of a known distance tail, a synthetic exercise, or an unmotivated parameter slice. It can be used for inverse identification of cusp width and for models that condition geodesic chords on deep excursions.

## Limitations and closest sources

The theorem concerns a fixed-width standalone cusp with curvature \(-1\), independent uniform-area endpoints and shortest geodesics. It does not treat the geodesic flow's stationary excursion process, other sampling measures, unbounded width-to-height ratios, or ambient shortcuts through an enlarged surface. The available older sources were materially read in relevant full-text sections, and the two closest published mathematical records were read in their complete result documents. Historical indexing may be incomplete; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
