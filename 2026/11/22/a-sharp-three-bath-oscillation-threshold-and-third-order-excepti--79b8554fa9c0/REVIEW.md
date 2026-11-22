# Self-review

## Correctness — PASS

The physical spin-flip generator closes exactly on one-site magnetizations, with no approximation or hierarchy closure. The three-by-three Bloch characteristic equation follows by determinant, and its explicitly factored discriminant settles all parameter ranges. The repeated-root geometric multiplicity is proved by a nonzero minor; the order-three nilpotent Jordan form is checked by direct matrix identities. The oscillatory uniform-mode formula follows by a two-dimensional matrix exponential with admissible initial spin means. The standalone verifier reproduces 10 symbolic checks, 5,016 exact generator identities and 15 numerical finite-ring spectral tests. Risks: floating checks alone cannot prove the continuum theorem, hence its determinant/Jordan proof is essential; no full Markov spectrum is claimed.

## Originality — PASS on examined evidence, provisional

The 2004 Mobilia–Zia–Schmittmann two-bath solution already gives exact magnetization closure and oscillatory opposite-sign baths. The 2004/2005 reaction-diffusion extension covers two alternating baths, while Schmittmann–Schmüser's 2002 work concerns two-bath stationary correlations. The closely related archived period-three finding proves a stationary four-spin factorization obstruction at positive bath parameters, not the negative-bath relaxation phase diagram. None of those examined materials states or directly implies the \(1/8\) threshold, full Bloch discriminant, or the third-order special modes; a broader periodic-rate solvability result could nonetheless subsume the specialization. The value and novelty judgments are subject to independent historical-priority verification.

## Mathematical value — PASS

This result identifies a finite antagonist-strength threshold absent in alternating baths, a momentum-dependent coexistence of oscillatory and purely decaying modes, and an exceptional point of higher order in an irreducible stochastic spin system. The phase diagram applies to infinitely many finite rings and includes a realizable magnetization response and its square-root onset. It is a structural, parameter-sharp classification of a motivated three-reservoir generalization, not a routine numerical invariant. It remains intentionally restricted to one-spin observables.

## Closest literature and limitations

- Mobilia, Zia, and Schmittmann (2004), arXiv:cond-mat/0405375: exact two-bath kinetic magnetization dynamics; opposite-sign oscillations.
- Mobilia, Schmittmann, and Zia (2004), arXiv:cond-mat/0412576: alternating two-bath reaction-diffusion duality.
- Schmittmann and Schmüser (2002), arXiv:cond-mat/0212616: two-bath stationary correlations.
- Archived period-three four-spin factorization result: a stationary, all-positive-temperature question, not this negative-temperature spectral problem.

Potential coverage by a broad uninspected periodic kinetic-Ising spectral theorem remains the main originality risk. The proof does not cover higher-order spin modes, and the third-order exceptional point requires a finite-size commensurability condition.

Self-review: passed. Independent audit: not yet performed.
