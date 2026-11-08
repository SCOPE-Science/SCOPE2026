# Scientific review

## Correctness

**PASS.** A conditional joint-transcript likelihood computation is exact for the heterogeneous scalar-quadratic model: all unchanged agents coincide under a common transcript, and the changed agent follows a deterministic two-dimensional signed sensitivity recurrence. The invariant cone removes all absolute-value ambiguity, Laplace density-ratio maxima are simultaneously attainable over finite prefixes, and an explicit two-root spectral calculation gives both finite-privacy sufficiency and divergence necessity. The boundary \(t\ge1\) is handled separately. The standalone exact-rational verification tests the recurrences, conditional executions and an explicit certificate; it does not replace the infinite-series proof.

## Originality

**PASS, subject to historical-access limitations.** The motivating 2026 algorithm publishes a sufficient nonnegative comparison-matrix bound, not the exact full-transcript budget or the necessary-and-sufficient heterogeneous scalar-quadratic threshold. Its sufficient spectral condition fails at the explicit instance \(t=1/2\), \(r=4/5\), where the new exact privacy loss is finite and equal to \(84/19\). Searches of mathematical research records, accessible historical claims, and related primary literature found no statement dominating this sharp criterion. Earlier state/direction perturbation work is closely related in motivation but concerns other recursion structures; the complete IEEE text could not be inspected. Missing indexing and inaccessible full texts remain priority risks, not evidence of uniqueness.

## Value

**PASS.** Infinite-horizon differential privacy depends critically on conditional sensitivity decay relative to noise decay. A sufficient comparison-matrix test can rule out large, useful parameter regions. This finding solves the exact full-transcript parameter-calibration problem for arbitrary positive-curvature scalar quadratic networks and shows feasibility all the way up to the strict step boundary \(\alpha h_i<1\), versus the source's general sufficient bound \(\alpha h_i<(\sqrt{17}-3)/4\). It is a mathematical phase boundary, not merely a recomputation of a reported privacy table or a claim of faster optimization.

## Closest literature and limitations

- Maithripala, Qiu and Lin (2026), arXiv:2610.04854v1, Algorithm 1 and Theorem 3: same mechanism and adjacency, general sufficient privacy bound but no sharp quadratic classification in the material inspected.
- Ding et al. (2022), DOI 10.1109/TAC.2021.3059427: related direction/state perturbations, different named algorithm; publisher full-text unavailable.
- Xuan and Wang (2022), arXiv:2212.05364: noisy gradient tracking and privacy–accuracy tradeoffs; no verified implication to the present alternating mechanism.

The theorem is limited to heterogeneous positive-curvature real scalar quadratics, independent Laplace channels, fixed parameters and complete released transcripts. Independent literature verification and mathematical audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
