# Self-review

## Correctness — PASS

The claim is a universal equality for all ambient polynomials of total degree at most five and all \(0<t<1\), plus a full two-eigenvalue spectrum on the real five-dimensional harmonic-quadratic space. Its proof uses the exact polar cap moment identity, signed-permutation moment reduction, a factored Legendre obstruction, and direct independent evaluation of the two eigenvalues. \(t=0\) and \(t=1\) are not part of the quantified theorem. The sixth-degree Legendre obstruction is nonzero at the unique interior exactness threshold. The supplied standard-library checker tests all 56 degree-at-most-five monomials in exact rational number-field arithmetic. The general-radius spectral polynomials, trace relation, and Legendre averages were checked coefficientwise with the included exact rational-polynomial verifier. Limit: exact arithmetic checks support, but do not replace, the analytic derivation.

## Originality — PASS, with residual access risk

The closest source is Simons, Dahlen and Wieczorek's general spherical concentration treatment, including polar caps (arXiv:math/0408424). It does not give the six octahedral multiplicity-weighted window formula, its degree-five exactness condition or the sharp conditioning crossover. Brauchart and Dick's spherical QMC method (arXiv:1101.5450) concerns point-node integration. The accessible prior two-cap quadratic-harmonic result optimizes separation for two disjoint caps, a different operator. Keast and Diaz's fully symmetric surface quadrature paper (DOI 10.1137/0720029) is an important plausible comparison, but its full text was inaccessible: no categorical claim is made about everything it might contain. Exact novelty is assessed at the statement/implication level, not from missing keyword hits; unindexed continuous-window equivalents remain possible.

## Mathematical value — PASS

The six octahedral windows constitute a natural symmetric measurement layout. Their positive, nonconstant overlap-counting measure gives an exact continuous cubature rule through a maximal specified degree, while the same unique radius is an optimally conditioned sensing geometry for every real quadratic spherical harmonic. The full eigenvalue formulas and strict ordering crossover explain which types of quadrupole modes become least stable as a cap narrows; the sharp sixth-degree failure separates exactness from a trivial all-degree reconstruction.

## Scientific limitations

The formula is specific to equal antipodal-axis caps on \(\mathbb S^2\) with multiplicity weighting; it does not extend to unions counted once, arbitrary cap sets, higher harmonic bands or higher dimensions. The discovered radius is unique only in this natural one-parameter family. No independent mathematical audit has yet been performed.

Self-review: passed. Independent audit: not yet performed.
