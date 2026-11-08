# Review: Exact four-mode diagonal preconditioning for two-community correlation matrices

## Correctness

PASS. The Loewner-sandwich equivalence makes within-community symmetrization valid for **unrestricted positive diagonal** optimization, not only for the restricted ansatz. The invariant-subspace split produces two fluctuation eigenvalues and two quotient eigenvalues. Strict monotonicity of the three competing ratios and the two characteristic-polynomial collisions prove the clipped rule for all stated parameters. In the rational four-coordinate test, the resulting spectrum is exactly \(\{2/5,2/5,3/5,81/35\}\). The standalone script checks determinant identities and 3,000 parameter cases; only the written proof supplies the universal result.

## Originality

PASS, with publication-precedence qualifications. General diagonal preconditioning is old: Jambulapati et al. (2020) and Qu et al. (2022) give general optimization machinery, and Kolotilina (2002) gives broader block-optimality characterizations. Kolotilina (2006) completely treats quasireal three-by-three matrices; the present family contains at least four genuine spectral modes because both communities have at least two coordinates, and the three-by-three classification does not itself state the clipped four-mode formula. No exact two-community all-parameter optimizer or the three competing transition mechanisms was found in the reviewed sources or published record searches. The older block-characterization literature and inaccessible material could offer a non-obvious implicit derivation; an independent precedence audit is still needed.

## Value

PASS. Two-community compound symmetry is a natural structured positive-definite matrix model. A direct, dimension-independent condition-number-optimal diagonal scaling rule is useful as a reproducible test case for optimization-based preconditioners. The least eigenvalue can switch among a quotient mode and two community-fluctuation modes, so analyzing the quotient alone gives the wrong answer. Even the four-coordinate example improves over uniform Jacobi normalization by an exact, verifiable amount. No downstream solver-speed theorem is asserted.

## Limitations

The theorem is restricted to strictly positive correlations and strictly positive definite matrices. It proves existence of a block-constant optimum, plus uniqueness only of that relative block scale; it does not classify all unrestricted optima. Some historical primary sources were available only through abstracts; a full literature audit could change the originality assessment.

Self-review: passed. Independent audit: not yet performed.
