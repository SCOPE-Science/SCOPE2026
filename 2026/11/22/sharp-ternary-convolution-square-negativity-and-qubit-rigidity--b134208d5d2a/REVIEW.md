# Self-review

## Correctness — PASS

The matrix effect factorization \(X=S^{1/2}YS^{1/2}\), with \(-I\preceq Y\preceq I\) and \(0\preceq S\preceq I\), rigorously implies \(X^2\preceq S\) without assuming commutativity. The exact identity \(AB+BA+C^2+I/24=(S-X^2)/2+3(C-I/6)^2/2\) proves the bound. A rational-radical \(2\times2\) witness attains the lower eigenvalue, and the two positive summands force an invariant qubit corner at each equality vector. Scalar and two-cycle cases are addressed directly. The included checker tests exact identities and independent finite numerical instances; the analytic inequalities, not finite experiments, establish the infinite-parameter claim.

## Originality — PASS against accessible evidence, with a material residual risk

The closest new source is Jabbari, arXiv:2611.09755 (submitted November 6, 2026), which treats positive convolution-idempotent measures and proves their commutativity. That assumption excludes the non-idempotent sharp negative extremizer; its qualitative observation that convolution can lose positivity does not determine an optimal spectral bound or equality classification. Chunyuan Deng (2013) treats Jordan/sequential operator products and special projection relations, not a three-atom convolution-square bound. Girard–Plávala–Sikora (2020/2021) concern compatibility of quantum channels. Published-result searches for matrix-valued convolution, three POVM effects, anticommutator extrema, the exact constant and equivalent formulations did not identify stronger covering results. **Residual risk:** the full 2024 Guo–Luo article on POVM Jordan negativity remained inaccessible after attempts to obtain an open version and through authorized library access; only the publisher abstract could be inspected. No global priority or independent novelty certification is claimed.

## Value — PASS

This is a complete sharp all-dimensional quantitative solution of the first cyclic setting where positive matrix convolution can acquire a negative eigenvalue. The exact best constant, complete two-dimensional contact rigidity and proof of simultaneous group-size and coefficient-dimension minimality are mathematically motivated by the failure of positivity identified in the matrix-convolution literature. This is more informative than a single counterexample or a routine restatement of the idempotent classification.

## Scope and limits

No claim is made about longer finite groups, general nonabelian groups, higher convolution powers, or other mass normalizations. Numerical experiments are supplementary to the proof. The 2024 inaccessible primary article is a specific outstanding bibliographic comparison; no independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
