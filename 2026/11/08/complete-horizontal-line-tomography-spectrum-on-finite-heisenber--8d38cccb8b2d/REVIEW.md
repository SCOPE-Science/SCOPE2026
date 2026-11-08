# Mathematical review

## Correctness

**PASS.** Pairwise common-horizontal-line counts give the exact Gram kernel, including the diagonal correction \(c=D-1\). The central Fourier transform reduces it to one rank-one all-ones block and \(q-1\) symplectic Fourier blocks. Each nonzero block is Hermitian, squares to \(q^{2n}I\), and has trace \(q^{2n}\), fixing all eigenvalues and multiplicities. The critical rank-one zero eigenvalue, higher-rank strict positivity, and explicit inverse are consequences with no unverified analytic steps. A direct finite incidence construction and numerical spectrum comparison pass 86,391 assertions for the three small cases stated in the result.

## Originality

**PASS relative to checked evidence.** The two 2026 horizontal-Heisenberg papers work with maximal selection by spatial/refined directions and estimates for rich directions; they do not calculate the all-line linear operator's singular spectrum. Kong–Tamo analyze a graph-variety incidence family, which does not contain the complete horizontal-line family as an immediate case of their stated hypotheses. Actual database searches for Heisenberg all-line tomography, central symplectic Fourier blocks, eigenvalue tables, and rank transitions returned no exact coverage; finite cyclic abelian Radon and constrained Fourier sampling results are not the same operator. Residual risk: equivalent general finite-Heisenberg association-scheme/incidence spectral calculations may be indexed under different terminology.

## Value

**PASS.** The result gives a complete natural tomography invariant in a noncommutative finite group, identifies a sharp and unexpected transition between nonrecovery at rank one and recovery at every larger rank, and supplies exact stable reconstruction operators and condition numbers. The two regimes are not consequences of knowing merely that individual horizontal lines intersect in at most one point.

## Limitations and sources

The conclusions require all distinct lines counted once, odd prime-power fields, and unaveraged line sums. The proof does not extend to arbitrary direction subfamilies, general nonlinear maximal operators, or characteristic two. The relevant primary papers are arXiv:2603.02111, arXiv:2608.14059 and the incidence comparison arXiv:2408.10977; an unindexed stronger covering statement remains possible.

Self-review: passed. Independent audit: not yet performed.
