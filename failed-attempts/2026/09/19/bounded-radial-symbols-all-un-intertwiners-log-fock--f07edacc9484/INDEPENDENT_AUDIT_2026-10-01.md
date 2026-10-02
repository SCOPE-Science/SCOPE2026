# Independent scientific audit — SCOPE-20260919-f07edacc9484

Audited at: 2026-10-01T12:12:53.903497Z

Disposition: **failed**

## Correctness — PASS

The logarithmic moment kernels concentrate on pairwise disjoint saddle annuli with tail masses tending uniformly to zero. Therefore the step-symbol map gives an operator on \(\ell^\infty\) equal to the identity plus a compact operator, so its range is closed and finite-codimensional and is contained in the radial moment range. The preadjoint from \(\ell^1\) is injective by the entire-function moment argument. Closed-range duality and Hahn-Banach then yield surjectivity, and finite-dimensional Fredholm complements give a bounded linear right inverse. The homogeneous multiplicity-free decomposition identifies the resulting sequence map with the full \(U(n)\)-commutant.

## Originality — FAIL

Two already-published SCOPE results for the same logarithmic Fock weight jointly imply the central surjectivity claim. The earlier Calkin-corona record constructs the same shell embedding with a uniform tail estimate, which means the associated sequence operator is identity plus compact and hence makes the radial moment range closed. The later norm-saturation record proves that the same radial moment range is norm dense in all of \(\ell^\infty\). A linear subspace that is both closed and dense is all of \(\ell^\infty\). Thus exact bounded-symbol surjectivity is already a direct corollary of the published pair; the bounded linear right inverse then follows from the explicit finite-codimensional/Fredholm splitting used here.

### Equivalent formulations

The conjunction of those published statements is equivalent to surjectivity once the shell estimate is recognized as a compact perturbation of the identity.

### Broader coverage

Together the prior SCOPE results dominate the new exact range statement even though neither title says 'surjective'.

### Exact database or table

This is decisive positive prior-art evidence, not an unsuccessful novelty search.

### Claim versus prior implication

The central surjectivity conclusion follows immediately from the two already-published SCOPE results.

## Value — FAIL

Exact single-symbol realization is mathematically stronger than norm density and modulo-compacts interpolation, but after both ingredients have already been published for the same weight, the upgrade is the routine closed-plus-dense range observation. The extra right-inverse statement is standard finite-codimensional/Fredholm functional analysis and does not supply a separate substantive gap.

## Sources inspected

- Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation — https://arxiv.org/abs/2609.20652. COVERING_INGREDIENT: The paper supplies the analytic shell concentration and moment framework but does not itself state exact bounded-symbol surjectivity.
- A logarithmic Fock weight has the full diagonal Calkin corona — https://github.com/the semantic research index/2026/tree/main/2026/9/18/SCOPE-maximal-radial-toeplitz-calkin-corona--7e7e4a2f84f3. COVERING_INGREDIENT: For every bounded target sequence it constructs a bounded shell symbol whose eigenvalues differ by a null sequence, with a uniform tail estimate.
- Norm saturation of radial Toeplitz quantization for a logarithmic Fock weight — https://github.com/the semantic research index/2026/tree/main/2026/9/19/SCOPE-radial-toeplitz-norm-saturation-small-fock--11f9996dd07d. COVERING_INGREDIENT: It proves the norm closure of the radial single-symbol moment range is all of ell-infinity.

## Checked sources

- https://arxiv.org/abs/2609.20652
- https://github.com/the semantic research index/2026/tree/main/2026/9/18/SCOPE-maximal-radial-toeplitz-calkin-corona--7e7e4a2f84f3
- https://github.com/the semantic research index/2026/tree/main/2026/9/19/SCOPE-radial-toeplitz-norm-saturation-small-fock--11f9996dd07d
- https://arxiv.org/abs/1505.07906
- semantic research-index search

## Residual risks

- No decisive correctness defect was found; the failure is prior implication from published SCOPE results.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The surjectivity proof itself is valid.
- The original package should be preserved intact in the designated failed-attempt archive.
