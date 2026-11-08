# Scientific review of the Hamming RK4 positivity classification

## Correctness (C): PASS

The result specifies all integer dimensions \(d\ge3\), alphabet sizes \(q\ge3\), and real nonnegative step sizes. The adjacency-walk recurrence is valid for all Hamming distances, the entries of the degree-four RK4 matrix are computed explicitly, and every possible distance is accounted for. The strict positivity of the diagonals follows from positive definiteness of the even fourth-order exponential Taylor polynomial on the nonnegative spectrum. The Bernstein coefficient identities show positivity of the edge and distance-two entries through the distance-three cutoff for \(d\ge4\), and show a unique earlier edge root precisely for \(d=3,q\ge13\). The independent direct sparse-Laplacian and exact-radial verification replay returned `VERIFY_OK 6556 exact coefficient/shell/Bernstein checks` on the extracted standalone program. The all-parameter claim relies on displayed exact algebra, not finite sampling.

Risk: An algebraic transcription error in one of the displayed certificates would matter; the identities are algebraically simple enough for independent expansion, and the included checker reproduces all coefficients across many exact instances. Independent audit has not been performed.

## Originality (O): PASS on inspected evidence, not a priority guarantee

The relevant antecedents were checked by *implication and domain*: Gottlieb--Shu--Tadmor (2001) establish generic SSP conditions for high-order time discretizations, but do not classify this RK4 Hamming graph family; Horváth (2005), inspected across all 16 pages, treats general RK positivity thresholds and spectral invariant cones, but does not supply the exact nonbinary Hamming shell or the \(q=13\) edge-versus-distance-three transition. Lóczi--Ketcheson (2013) primarily studies absolute-monotonicity radii of rational functions, a different general problem. Related graph-specific calculations on bipartite and triangular graph families imply neither this full nonbinary classification nor the dimension-specific switch.

Public mathematical-record semantic searches for Hamming graph RK4 positivity, fourth-order Markov kernel distance-three barriers and graph diffusion stability returned related numerical positivity records but no covering claim. Relevant closest recorded identifiers and all four implication comparisons are preserved in AUDIT.json. Risk: further specialist or poorly indexed sources may exist, so an independent literature-priority assessment remains necessary.

## Value (V): PASS

Positivity of a diffusion end-step is independent of its scalar spectral stability, and the q-ary Cartesian product of complete graphs is a canonical association-scheme family with applications to product-state diffusion and structured Markov networks. The result supplies the sharp timestep for every network in the specified infinite two-parameter class, distinguishes the actual sign-failing matrix entry, and exhibits the unexpected discrete alphabet cutoff between 12 and 13 in dimension three; no such cutoff occurs in higher dimensions. Its exact Bernstein certificate makes the result reproducible and potentially useful for choosing a positivity-safe step, beyond a generic SSP lower bound. It does not assert all-stage positivity, weighted generalization, or general error-control conclusions.

Self-review: passed. Independent audit: not yet performed.
