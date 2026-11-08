# Scientific review

## Correctness — PASS

The mass/stiffness normalization is explicit; the exact Laguerre matrix expansion is absolutely convergent because the scaled stiffness spectrum lies inside the unit disk. Matrix bandwidth isolates the first nonzero coefficient at each distance, with correct parity. Laguerre orthogonality supplies simple positive zeros, and an analytic perturbation argument transports them to the physical propagator. The far-end entry is an \(n\)-term exponential polynomial with distinct decay rates, so the \(n-1\)-zero bound together with the simple zero at time zero proves the exact count and excludes further positive zero crossings. The three-node conclusion follows from an exact spectral decomposition and strict convexity. Standalone symbolic/numerical checks pass (431 assertions); they are corroboration, not infinite proof.

## Originality — PASS (qualified)

The existing literature already proves the broad loss of positivity at short times when the mass matrix is nondiagonal, and in appropriate cases eventual positivity. This work does not claim that qualitative phenomenon. The assessed incremental claim is a one-parameter partially lumped P1 heat operator whose near-lumped boundary layer is governed by generalized Laguerre polynomials, producing exactly \(n-2\) far-end time sign reversals and an explicit hierarchy of crossing locations. Actual database, related-source and exact-parameter searches found no directly covering result. The closest readable 2015 Jin–Lazarov–Thomée–Zhou manuscript discusses short/large-time positivity thresholds but not the present Laguerre crossing count. Omle–Askar–Kovács (2022) addresses positivity of explicit heat time integrators instead. The high-relevance 2015 Chatzipantelidis–Horváth–Thomée full article remained inaccessible; only its abstract was available, leaving a nontrivial residual priority risk. These limits qualify the assessment; the review does not establish publication priority or independent originality.

## Value — PASS

The number of transient negative/positive episodes grows with the number of interior mesh nodes despite the mixture approaching the fully lumped positivity-preserving discretization. This supplies a mathematically motivated, exact spectral boundary-layer classification and warning that a single observed restoration cannot establish permanent positivity. The crossing constants are intrinsic Laguerre roots, not arbitrary computed cutoffs. The three-node result gives an exact all-fraction benchmark. Restriction to one-dimensional uniform P1 elements and small mixing fractions for the all-dimensional crossing theorem is material.

## Closest sources and limitations

Omle–Askar–Kovács (2022), https://doi.org/10.28919/jmcs/7407 (full-text introduction, discretization and methods read); Chatzipantelidis–Horváth–Thomée (2015), https://doi.org/10.1515/cmam-2015-0018 (abstract only, full text access unavailable); Jin–Lazarov–Thomée–Zhou (2015), https://arxiv.org/abs/1510.02825 (open-access full manuscript sections on semidiscrete positivity and experiments inspected). More obscure earlier analytic zero-count work is not excluded by negative searches. The finite checker does not certify an infinite quantifier or novelty.

Self-review: passed. Independent audit: not yet performed.
