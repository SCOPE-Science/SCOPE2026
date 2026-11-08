# Review of the square-zero symplectic centralizer rank distribution

## Correctness

**PASS.** Every centralizer solution has the explicit block form with \(A\) skew-adjoint and \(B\) symmetric. The square-zero equations are exact. Nonzero \(A\) has rank two and totally isotropic image; split four-spaces admit \(2(q+1)\) such planes and nonsplit four-spaces none. Each split plane supports \(q-1\) nonzero alternating maps. For each \(A\), a six-dimensional linear space of compatible \(B\) is derived in an adapted basis and the resulting \(8\times8\) element has rank four. The remaining block is an arbitrary symmetric matrix, with rank counts derived through Gaussian coefficients and orthogonal stabilizers. The standalone executable replays the checks enumerating cases over prime fields and exhaustive \(q=3\) compatible pairs. The statement is restricted to odd characteristic, and no finite search is used as an infinite-field proof.

## Originality

**PASS, provisional historical priority.** Yakimova (arXiv:0803.0285) gives centralizer structure, not the finite-field square-zero rank fibers; Reid (arXiv:1403.3112) gives nilpotent orbit varieties, not these counts; Britnell--Wildon (arXiv:1001.0811) classifies commuting general-linear classes, not symplectic fiber multiplicities. Fulman--Guralnick (arXiv:1611.05499) gives aggregate symplectic commuting nilpotent-pair generating functions but does not resolve the fixed \((2^4)\) rational-orbit split, square-zero partner restriction, and rank strata. A general-linear maximal square-zero centralizer rank law available in related records counts a larger unrestricted space and does not directly imply the orthogonal-Witt discriminant distinction. The concrete original aspect is the entire distribution and the strictly rank-four split/nonsplit gap. Full historical priority is not certified; a broad unpublished orbit-incidence formula remains a residual risk.

## Value

**PASS.** Rational nilpotent orbits of classical groups can share the same geometric partition. The formula distinguishes the two rational orbits by a natural commuting-square-zero fiber invariant and explains the difference via existence of maximal isotropic planes in a four-dimensional quadratic multiplicity space. Any nonzero skew-adjoint square-zero endomorphism has even rank at least two and rank at most half the multiplicity-space dimension; dimension four is the first possible case. This is therefore a motivated first structural boundary, not an arbitrarily selected finite-field numerical table. The complete five-rank distribution, positive gap and uniform odd-prime-power proof give a quantitative refinement of orbit-incidence geometry.

## Limits and verification

The proof covers every odd prime power but only maximal-rank square-zero elements in \(\mathfrak{sp}_8\). Finite enumeration was performed over prime fields of orders \(3,5,7\); full compatible-pair and symmetric-block enumeration was performed over \(\mathbb F_3\). The \(q=9\) checks are purely polynomial arithmetic. No characteristic-two claim, extension-field exhaustive check, or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
