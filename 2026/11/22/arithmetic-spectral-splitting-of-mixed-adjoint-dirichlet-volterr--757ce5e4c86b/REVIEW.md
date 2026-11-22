# Mathematical review

## Correctness — PASS

For the Hardy coefficient basis, direct evaluation gives \(V_ce_n=(\log c/\log(cn))e_{cn}\). Applying the adjoints in the stated order yields a partial permutation with disjoint output columns and two exact weight branches indexed by \(\gcd(a,b)\). The cubic branch is positive after taking absolute values and strictly decreasing. Its inverse threshold has an expansion through the constant term, giving the full stretched-exponential prefactor. The quadratic branch has an exact lattice count. Both branches decay but none is in a finite Schatten class. The accompanying standalone checker passed 16,166 finite arithmetic, monotonicity and singular-list checks; infinite conclusions come from the proof, not the tests.

## Originality — PASS, qualified

The closest published exact singular-spectrum record concerns the **unstarred** Dirichlet–Volterra commutator \([V_a,V_b]\). Its coefficient map goes from \(e_n\) to \(e_{abn}\), and vanishes when \(a=b\); this statement does not imply the present mixed-adjoint gcd splitting, nonzero self-commutator and two counting scales. Papers on individual Dirichlet–Volterra operators by Bommier-Hato (2020), Gómez-Cabello–Lefèvre–Queffélec (2024), and Brevig–Perfekt–Seip (2016) treat boundedness/compactness or Schatten nonmembership, not mixed-adjoint spectral branch counts. A prior sharp logarithmic law for polynomial-symbol Volterra operators is a single-operator result and does not imply the present two-operator commutator theorem. Residual priority risks are general weighted-partial-permutation formulas and unindexed specialized operator-commutator literature. Negative searches are not proof of uniqueness.

## Mathematical value — PASS

The mixed adjoint commutator is a canonical test of relative nonnormality for Dirichlet–Volterra generators. Its singular spectrum changes decay order from inverse-cubic to inverse-quadratic logarithmic at precisely the arithmetic condition \(\gcd(a,b)>1\), while the cubic branch survives as a separable second spectral scale. The result provides exact all-rank singular data, sharp stretched-exponential counting constants, and a signed self-commutator spectral classification for every integer pair, rather than a routine fixed-parameter bound.

## Limitations

The results apply only to individual integer monomial symbols on the unweighted Hardy coefficient Hilbert space. No claim is made about arbitrary Dirichlet-polynomial symbols, general Bergman weights or independent verification. The 2016 work is background only; the first motivating arXiv source for this classification is the 2020 paper.

Self-review: passed. Independent audit: not yet performed.
