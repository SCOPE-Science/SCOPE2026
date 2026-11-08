# Scientific review: minimum positive exact Fock sampling

## Correctness — PASS

The exact Hilbert norm is fixed by the three normalized monomials. The proposed origin/three-root-of-unity design has exact diagonal matrix \(\operatorname{diag}(1,1,1)\) and all cross terms vanish. For three nodes, positivity and exact tightness make a square evaluation matrix unitary. This forces the three pairwise quadratic kernel values to vanish. Their roots are exactly \(-1\pm i\), and the associated phase differences \(\pm3\pi/4\) cannot sum around an odd three-cycle to zero modulo \(2\pi\). One and two nodes have insufficient rank. The proof does not rely on numerical checks; `CHECK.py` passed 28 supplementary assertions in the actual package.

## Originality — PASS relative to available evidence

The full text of Bownik–Yu's 2026 work on *infinite-dimensional nearly tight* frame discretization was inspected; its results do not give a finite exact positive quadrature cardinality. An earlier published one-circle Fock frame-conditioning result excludes tight sampling on one ring for degree two but allows no inference about two-radius tightness or the optimal number of nodes. Search comparisons against exact Gaussian cubature, four-node coherent frames and positive moment quadrature returned no directly identical construction or minimum-cardinality classification. Published scientific records with similar Fock and Fourier sampling titles concerned other sets, dimensions or constraints. Classical Fock kernel identities and the rank argument are prior mathematical machinery. Residual risk: the precise four-node formula may have been noticed in older Gaussian cubature/coherent-state literature without an indexed abstract. Independent publication-priority validation has not been performed.

## Mathematical value — PASS

Minimal positive coherent measurement count is a natural finite design invariant of the lowest nontrivial three-dimensional Fock truncation. The sharp impossibility result distinguishes exact tightness from mere spanning and from nearly tight sampling. The explicit four-node two-radius design resolves the gap left by single-circle impossibility. This gives a reproducible exact energy-preserving finite measurement rule at the first nonlinear polynomial degree, without claiming a broader asymptotic theorem.

## Limitations

Only degree two, complex dimension one and positive scalar point-evaluation weights are covered. Full Fock space, all higher polynomial degrees, and the classification of all four-node designs remain open here. Global novelty is assessed against accessible relevant literature, not mathematically certified by absence from search results.

Self-review: passed. Independent audit: not yet performed.
