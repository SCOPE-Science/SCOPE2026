# Scientific assessment

## Correctness — PASS
The statement quantifies over all positive clique sizes, all nonnegative convex filters normalized at zero, and all nonnegative timesteps. The proof derives exact orthogonal projectors at Laplacian eigenvalues 0, 1, each \(p_i+1\), and \(n\). These yield the apex entry \((1-f(nh))/n\), the cross-blade Jensen residual, and the within-blade secant-slope comparison. Convexity controls both residuals, while nonnegativity of the scalar filter makes every diagonal strictly positive. Every even Taylor symbol is positive and strictly convex on the positive half-line; the unique scalar level-one crossing is rigorously established. The included checker passed 3,556 exact matrix instances and 182,728 entry equalities. A finite checker does not substitute for the proof.

## Originality — PASS on inspected evidence, qualified
The full 2001 Gottlieb--Shu--Tadmor paper establishes general SSP linear formulas and CFL theory; it does not state this graph-specific necessary-and-sufficient apex criterion. The full 2005 Horváth paper establishes general positivity thresholds but does not develop clique-windmill Laplacian projectors or this criterion. The 2014/2015 Horváth--Song--Terlaky abstract and the published Kooij generalized-windmill spectrum treatment were also compared for implications; one full relevant manuscript was inaccessible. Preexisting results for complete multipartite graphs and selected other network classes overlap at stars and complete graphs, but their hypotheses do not cover the heterogeneous multiple-clique windmills with nontrivial blades. General background cannot by itself settle publication priority; unindexed specialist coverage is the main residual risk.

## Mathematical value — PASS
The exact condition applies to an infinite family of unequal-size clique-block networks and to every nonnegative convex spectral filter, not just one Runge--Kutta polynomial. It reduces an entrywise matrix-function question to a single scalar inequality, identifies a universal sharp even-order Taylor horizon, and proves all cross-clique entries remain positive despite the eventual loss at the apex. This is a structural classification for a natural graph family, rather than a recomputation of a known table or an arbitrary numeric instance.

## Boundaries
No extension to weighted networks, arbitrary base graphs, odd-order Taylor symbols outside their convex region, intermediate Runge--Kutta stage positivity, or nonlinear systems is claimed. Theoretical correctness is from the proof; program checks are finite corroboration. A specialist full-text comparison remains unresolved, and independent mathematical validation remains to be performed.

Self-review: passed. Independent audit: not yet performed.
