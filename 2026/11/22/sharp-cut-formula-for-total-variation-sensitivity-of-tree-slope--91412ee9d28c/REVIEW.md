# Scientific review — sharp tree slope-band variation sensitivity

## Correctness (PASS)

The single claim is the exact, attained two-input variation modulus in the theorem. The weighted quadratic objective has a unique minimizer for every input, since finite tree edge-difference bounds are jointly feasible and all observation masses are positive. A nondegenerate active face is a forest; its projection derivative is precisely positive mass averaging over active connected components. Every forest can be realized with strict complementarity and strict slack, ensuring that taking a maximum over all forests produces an attained local Lipschitz constant, not merely an upper bound. Since tree edge-cut indicators form an exact \(\ell^1\) basis of differences, the norm of each such derivative is the largest variation of a single projected edge-cut indicator. Counting only boundary edges of its active component gives the stated \((b_A M_C+b_C M_A)/(M_A+M_C)\) expression. Every block/edge term is realizable. The path, star, six-node, and caterpillar calculations follow by direct substitution. The attached checker independently evaluates finite masks, cut vectors, star masses, active-face KKT conditions and specified examples with rational arithmetic. Generality is established analytically, not by finite enumeration.

## Originality (PASS, subject to historical risk)

The closest original primary source is Yeganova–Wilbur (2009), which solves weighted Lipschitz-constrained *path* regression by an LPAV algorithm. Its open full text gives the box-constrained quadratic objective but neither the tree-wide two-input BV Lipschitz norm nor the sharp connected-subtree formula. Kolmogorov–Pock–Rolinek (2015 preprint; 2016 paper) instead considers *penalized* graph total variation with separable unary loss and does not calculate the response of a hard difference-band metric projection.

The closest published mathematical record on tree heat flow already determines the edge-local *contraction threshold* for its heat semigroup. That threshold implies the nonexpansive tree/mass cases here through a heat-flow limit on active subforests. These threshold consequences are therefore NOT treated as independently new. What remains different and not supplied by the heat theorem is the exact finite *amplification magnitude* of the hard-band fit map for all masses and trees, including genuine connected-block effects: a six-vertex modulus of \(5/3\) versus largest two-site block gain \(3/2\), and unbounded gains at degree at most three. Cyclic-cover isotonic regression treats a different feasible cone and graph family; its contraction classification does not imply the present cut formula. A published-finding corpus search by object, equivalent formulation, and parameters, plus accessible ledger claims, found no mathematically dominating exact formula. Inaccessible or unindexed historical source material remains a priority risk; no independence or absolute novelty is claimed.

## Mathematical value (PASS)

Slope-banded approximation is a standard way to enforce monotonicity and discrete Lipschitz constraints. The exact BV response to perturbations is a natural stability quantity not determined by ordinary Hilbert nonexpansivity. The theorem supplies a computable sharp combinatorial invariant for *every* finite tree and mass distribution, invariant under changes of constraint widths. Its 6-node example demonstrates why purely local edge tests do not quantify the worst gain; the bounded-degree caterpillar construction shows an arbitrarily large global penalty without high-degree vertices. This is a structural statement, not a routine parameter substitution or just a single small example.

## Sources and residual limitations

- Yeganova and Wilbur, *Isotonic Regression under Lipschitz Constraint*, DOI 10.1007/s10957-008-9477-0; original open-access PDF inspected (objective, assumptions and algorithm).
- Kolmogorov, Pock and Rolinek, *Total variation on a tree*, arXiv:1502.07770; original open preprint inspected (distinct penalized objective and algorithm).
- Published tree heat-flow variation criterion, published-finding corpus identifier `2026/10/26/SCOPE-a-conductance-independent-contraction-criterion-for-weighted-tre--9fedb9294a7c`; full statement and proof read to check the *covered* contraction consequences and the limits of its implications.
- Published cyclic-cover isotonic-regression variation result, published-finding corpus identifier `2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803`; full statement/proof read.
- Historical overlap checks included the accessible prior constrained convex-regression and weighted convex-minorant claims, without rereviewing their correctness.

The theorem assumes finite trees, strictly positive observation masses, finite nondegenerate edge intervals, quadratic fidelity, and unweighted edge total variation. It makes no claim for cyclic graphs, infinite trees, degenerate bands or other losses. Mathematical literature coverage is necessarily incomplete.

Self-review: passed. Independent audit: not yet performed.
