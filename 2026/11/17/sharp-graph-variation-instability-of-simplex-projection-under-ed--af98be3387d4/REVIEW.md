# Scientific review: sharp graph-variation instability of simplex projection

## Correctness — PASS

The claim is for finite connected simple unit-weight graphs, Euclidean simplex projection, positive simplex mass, and two-input graph total variation. Strict KKT support cells yield exactly the coordinate-centering matrices; the graph layer-cake identity gives the exact cut test. Cross-cut contributions are bounded by the input cut size, and active–inactive internal edges by \(ab(n-k)/k\). The exact maximization of \(\lfloor k^2/4floor(n-k)/k\) gives the displayed parity formula. For every \(n\ge4q\), two cliques with \(q\) matching active-to-active edges have edge connectivity exactly \(q\) and yield equality with actual nearby inputs. The standard-library rational checker was rerun from this package, with complete small graphs, randomized larger instances and exact nonlinear witnesses. Infinite statements rest on the proof, not enumerations.

## Originality — PASS, qualified

Duchi et al. (2008), Condat (2014) and Martins–Astudillo (2016) supply algorithmic threshold and active-set Jacobian machinery, not graph-edge variation constants. Lellmann et al. (2009) investigate spatial TV for multi-class image labeling, not this two-input scalar network quotient. The closely relevant public cyclic-variation simplex projection manuscript treats the same map but only one cycle, obtaining linear-in-dimension sharp growth and not implying the new arbitrary-graph quadratic connectivity envelope. Nearby complete-graph and graph-TV denoiser claims concern restricted graphs or a different nonlinear map. published-finding corpus and primary-literature searches found no dominating equivalent theorem. Residual risks are an unindexed equivalent general graph seminorm theorem or an implicit projection-norm result in older analysis literature. This qualified assessment is not a certification of worldwide priority.

## Mathematical value — PASS

The graph TV modulus governs sensitivity of mass-conserving, nonnegative vertex projections, and the exact cut formula enables graph-specific comparisons. The sharp connectivity-dependent \(1+F_n/q\) envelope demonstrates a structural instability hierarchy, attained on explicit simple graphs and growing quadratically at connectivity one, even though each signal's TV contracts. The precise cutoff \(n\ge4q\) and no-weight restriction are disclosed.

## Scope and limitations

Real Euclidean simplex projection, positive mass, simple connected unweighted finite graphs. No sharp fixed-order connectivity envelope is claimed for \(n<4q\), and no weighted or non-Euclidean generalization is proved. Finite checker output cannot establish an infinite-dimensional statement. Independent scrutiny is outstanding.

Self-review: passed. Independent audit: not yet performed.
