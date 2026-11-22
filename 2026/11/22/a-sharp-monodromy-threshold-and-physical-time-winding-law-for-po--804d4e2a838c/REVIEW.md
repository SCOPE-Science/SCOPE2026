# Review of the polynomial angular-bottleneck finding

## Correctness

**PASS.** The Cartesian vector field has the exact polar form \(\dot r=-ar^{2k+1}\) and \(\dot\theta=br^2\sin^2\theta+cr^4\). The radial solution is explicit, forward complete, and globally attracted to the origin. At \(k=1\), the logarithmic-radius angular equation is \(d\theta/ds=A\sin^2\theta+Be^{-s}\). An explicit scalar supersolution prevents a second half-turn crossing after any sufficiently late crossing, and the angular limit must be a multiple of \(\pi\). At integer \(k\ge2\), \(\int_0^\infty r^4dt=\infty\) forces infinite turning. The frozen angular period has the exact integral \(2\pi/[r^3\sqrt{c(b+cr^2)}]\). Radial relative change during one turn is \(O(r^{2k-3})\), so the inverse-radius-power increment per turn converges to \(2\pi(2k-3)a/\sqrt{bc}\). This proves the all-initial-data sharp coefficient and exponent. Exact symbolic checks for four orders and numerical checks at four turning parameter choices and eight finite-winding choices passed. Finite experiments are not relied on as infinite proofs.

## Originality

**PASS on inspected evidence, with residual historical-priority risk.** The 2026 García–Giné motivating full text (introduction, main results, examples, proofs) assumes monodromy and derives a generalized first-return linear coefficient; it does not state this explicit order threshold or time-dependent winding law. The 2024 García–Giné full text studies generalized Poincaré-map expansions under the absence of zero-angular-speed curves and does not give the same polynomial family or time-count formula. The 2025 García–Giné paper is relevant conceptually, but its accessible abstract gives analyticity and invariant-curve relations, not a physical-time count; the full paper could not be inspected. A published result concerning a specific nilpotent non-Morse oscillator has an unrelated winding law, and other indexed results address homogeneous spiral flows or complex-time winding; none presently implies the stated all-order polynomial family. Exact uniqueness is not established by these searches; the residual source-access and classical asymptotic-method risks remain.

## Mathematical value

**PASS.** The hypothesis of no curves of zero angular speed, central to the motivating literature, is logically separate from monodromy. The explicit polynomial family demonstrates both types of behavior under identical strong positive angular drift and global radial attraction, and supplies the sharp transition and quantitative physical-time scaling for arbitrary parameters and integer orders. The frozen-angle bottleneck calculation is structural rather than a numerical fit or an arbitrary finite cutoff. It may be used as a test family for classifications of characteristic directions and for the interpretation of finite-time winding data. The proof claims no theorem for arbitrary analytic vector fields or arbitrary perturbations.

## Closest primary literature and limitations

1. García and Giné, *Stability of analytic monodromic singularities without curves of zero angular speed*, arXiv:2611.15233v1, 11 November 2026. Full HTML inspected: assumptions, main theorem, examples and proofs. Distinction: return-map coefficients under monodromy, not a monodromy threshold despite positive angular velocity or a physical-time winding coefficient.
2. García and Giné, *Principal Bautin ideal of monodromic singularities with inverse integrating factors*, arXiv:2412.09205v1, 12 December 2024. Full HTML inspected: hypotheses and return-map expansion results. Distinction: not the claimed explicit family/limiting winding law.
3. García and Giné, *Monodromic singularities without curves of zero angular speed*, AIMS Mathematics 10 (2025), 1488–1500, DOI:10.3934/math.2025069. Abstract inspected; full text not available through the tried accessible source. Residual overlap risk, not a claim of complete noncoverage of the unread article.
4. Published mathematical-result records on a nilpotent oscillator's winding clock and on homogeneous-star-node cycles. Indexed summaries inspected; neither reports this radial-order transition or its limiting coefficient, but summaries alone cannot rule out results contained in their full papers.

The originality assessment is evidence-limited. The all-time analytic argument is explicitly self-contained; the numerical tests do not certify any infinitary statement. No perturbation robustness, generalized return-map analyticity, or universal monodromy classification is claimed.

Self-review: passed. Independent audit: not yet performed.
