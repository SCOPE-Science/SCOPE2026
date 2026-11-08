# Scientific review

## Correctness — PASS

The statement exactly quantifies over every integer cycle size \(n\ge3\), every nonnegative dimensionless timestep \(h\), and all nonnegative initial vectors; its equality boundaries are included. The proof expands the degree-four RK4 polynomial into exactly nine Laurent powers, reducing every cycle (including all lengths larger than the stencil) to an explicit finite residue sum. Positive coefficient factorizations, three strictly monotone cubic isolators, and the fixed unaliased distance-three term give necessary and sufficient conditions with no extrapolation from samples. The independent four-stage rational evaluation in the included `verify.py` verifies algebraic implementation, not universal quantification. The spectral statement follows from the complete periodic Fourier spectrum and a positive scalar stability polynomial. No unproved claim is needed for the theorem.

## Originality — PASS under searched prior art, with residual risk

The research comparison checked actual claims, not just titles. The 2005 Horváth full text (pages 1–16) proves general RK positivity threshold theory and treats a *Dirichlet* heat operator with theta/Lobatto/Radau methods; it does not classify classical RK4 on cycles. The 2022 Omle–Askar–Kovács full-text paper studies positivity-preserving explicit methods and different heat tests, not the same fixed fourth-order method and all finite periodic sizes. The 2020 Nüßlein–Ranocha–Ketcheson full text concerns adaptive RK weights, and the specific mentions of RK4 do not imply this cycle phase diagram. Related published research on CN resolvents, BE-filtered CN positivity and fourth-order Padé Markov steps likewise uses distinct stability functions. The complete \(n=3,4,5,6,7\) exceptions and uniform \(n\ge8\) cutoff are not immediate consequences of the generic framework without the new Laurent alias calculation. A specialized older exact stencil computation could dominate this result and remains a genuine priority risk. Search failure alone was not treated as proof of novelty.

## Value — PASS

The natural finite-cycle family is a standard spatial discretization of mass-preserving diffusion. A complete sharp endpoint positivity classification, including surprising reversals \(c_5>c_4\) and \(c_7>c_6\), gives useful numerical-maximum-principle benchmarks and explicitly demonstrates that numerical \(\ell^2\)-stability need not preserve physical positivity. These are precise conditions on an important method and the whole nonnegative cone, rather than isolated toy arithmetic or an arbitrary graph slice. The theorem also proves exactly when increasing mesh size eliminates the small-cycle wrap-around benefit.

## Closest work and limitations

See Omle–Askar–Kovács (2022), https://doi.org/10.28919/jmcs/7407; Nüßlein–Ranocha–Ketcheson (2020), https://arxiv.org/abs/2005.06268; Horváth (2005), https://doi.org/10.1016/j.apnum.2004.08.026. Their concepts and established general positivity results are fully credited. This is only exact endpoint nonnegativity for scalar uniform one-dimensional periodic heat systems; no multi-dimensional or arbitrary Markov extension is asserted. Specialist historical priority and independent mathematical verification remain unresolved.

Self-review: passed. Independent audit: not yet performed.
