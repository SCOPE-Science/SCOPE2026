# Self-review

## Correctness — PASS

The exact finite-state generator, orbit counting, elimination, and factorization are given in `RESULT.md`. The positive coefficients of \(H(\gamma,w)\), the factors \(\gamma+2\) and \(w^2-4\), and positivity of \(D\) prove the sign throughout the declared domain, not just in sampled cases. The Gibbs-ratio logic and three-cycle minimality argument use full stationary symmetry and flux balance. The symbolic checker and three independently constructed exact 32-state generators all passed. The high-rate coefficient follows from dominant polynomial powers and a logarithmic expansion.

## Originality — PASS (qualified)

The closest exact public result is [the four-spin switching-rate energy theorem](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-switching-rate-reversal-on-a-four-spin-ising-plaquette--b8870460e67a), whose full `RESULT.md` and generator were compared. Its mean-energy classification is credited and not presented as new. The all-rate non-Gibbs orbit-weight sign, its exact factorization and temperature-mismatch coefficient, and the triangle minimality comparison are distinct mathematical assertions not established by a mean-energy formula alone. The [Dutta–Sarkar–Basu study](https://arxiv.org/abs/2509.00494) studies effective-temperature fits and the infinite-fast-switching Gibbs limit, not this exact finite-rate inequality. Spatially alternating temperature chains and Gibbs-preserving tempering algorithms use different protocols. Literature indexing is not complete; an unindexed stronger theorem or implicit exact stationary solution remains a priority risk.

## Value — PASS

The question whether fluctuating-bath steady states admit one exact equilibrium temperature is physically motivated. The theorem identifies the smallest simple-cycle obstruction and proves that approximate Gibbs behavior at arbitrarily fast finite switching is never exact, with a quantitative \(1/\gamma\) mismatch. This is a structural benchmark for interpreting observable-dependent effective-temperature fits, not merely a numerical orbit table. The scope is deliberately finite and does not claim a thermodynamic-limit transition.

## Limitations and source comparison

The hotter bath is exactly infinite-temperature and the spin rates are exponential detailed-balance rates; standard logistic Glauber rates and larger systems are not covered. The original publication date is 30 August 2025, not the later journal publication date. The closest published four-spin result uses the same generator, so independent publication-priority examination is particularly important. Details of searched equivalences, source inspections and remaining risks appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
