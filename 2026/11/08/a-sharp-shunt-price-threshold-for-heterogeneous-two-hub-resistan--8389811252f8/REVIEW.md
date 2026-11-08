# Scientific review: sharp bridge-price threshold for heterogeneous two-hub networks

## Correctness — PASS

The result is global over independent conductances on all \(2m+1\) edges. Strict convexity of trace inverse together with graph-edge injectivity proves uniqueness; hub exchange then forces equal conductances in each mirrored spoke pair. The symmetry-sector effective-resistance identities reduce the full problem to \(A\sum_i x_i^{-1}+C/(\sum_i x_i+2y)\). A unique monotone root, KKT boundary inequality, an activated-regime square-root solution and the positive-bridge feasibility test prove the complete threshold. Budget exhaustion, the threshold equality case and the equal-price limit are treated explicitly. A standalone checker passed 2035 supplementary checks, including fully asymmetric competitors, but the infinite theorem rests on the displayed proof.

## Originality — PASS on inspected evidence, qualified

The closest primary source is Ghosh–Boyd–Saberi (2006 conference; 2008 full journal text), which proves the general resistance-allocation convex program and develops tree, wheel and barbell examples. Neither inspected section gives a heterogeneous \(K_{1,1,m}\) price-activation threshold or both exact optimizer regimes. Yang (2012) evaluates unit-weight bipartite graph indices and extremal graph families, not cost-constrained conductance allocation. Bhoite et al. (2026) studies a distinct cardinality-constrained augmentation problem on a fixed weighted base and numerical relaxations; it does not state the present explicit optimizer. Actual published-finding corpus searches returned other graph and optimization findings, but no matching statement. Residual risk: unindexed or differently named two-terminal network optimization literature may imply this result; no database nonmatch proves uniqueness of publication.

## Value — PASS

The theorem completely solves a natural conductance-sizing problem with heterogeneous costs, gives an exact *support-change decision* for whether a direct inter-hub shunt should be funded, quantifies its sharp price threshold independently of budget, and reveals a quadratic decay of economic usefulness as parallel routes proliferate. It is not a mere recalculation of a fixed-weight Kirchhoff index: it optimizes every edge independently and resolves both an interior regime and a boundary-support regime.

## Scientific limitations

The result assumes positive, mirrored leaf-pair prices and linear cost with no degree caps. The inactive regime is specified by a unique monotone root. The comparison cannot exclude all equivalent unindexed literature; the 2006 conference version predates the complete paper's verified electronic release date without a verified exact public-release day. Independent mathematical validation is not represented as performed.

Self-review: passed. Independent audit: not yet performed.
