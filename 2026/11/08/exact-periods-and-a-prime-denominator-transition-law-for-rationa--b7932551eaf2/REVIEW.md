# Review of exact rational floor-polynomial coprimality

## Correctness — PASS

For \(p\nmid n\), division by \(p\) shows that the gcd of \(n\) with \(\lfloor an^k/p\rfloor\) equals \(\gcd(n,t_{n\bmod p})\); for \(p\mid n\) and \(k\ge2\) it exceeds one. The CRT proves the exact period candidate and the residue-fiber density. The least-period proof separately forces every prime factor of the period via explicit CRT counterexamples to any omitted prime. Power-coset invariance and numerator averaging are finite-group identities. A multiplicative-character decomposition and the Pólya–Vinogradov inequality establish the stated uniform convergence with constant depending only on \(k\). Boundary cases \(p=2\), \(t_r=1\), and \(n=1\) are included. Direct exact checks of 33 parameter triples and 120 coset/average combinations were executed successfully; they supplement rather than replace the proof.

## Originality — PASS, qualified

Champagne (arXiv:2607.27533v1, July 30, 2026) and Banks–Shparlinski (arXiv:2205.00253v1, April 30, 2022) treat irrational-coefficient polynomial-floor gcd statistics, not exact periodicity for rational prime denominators. Watson's 1953 rational-coefficient result and Sykora's 2014 computations concern \(k=1\), whereas the present theorem requires \(k\ge2\). Chatterjee (arXiv:2611.04345v1, November 3, 2026) establishes the quadratic irrational-coefficient case, with no rational prime-denominator least-period formula. Searches for the exact gcd-floor sequence, periodicity, power-residue coset densities, and stronger rational-polynomial formulas found no result with an implication covering all four claims. Relevant nearby work on unrelated finite-field characters, polynomial-value gcds, and totient densities was also compared by objects and hypotheses. Historical-priority uncertainty remains, notably potential unindexed rational-slope work and the unavailable full 2014 rational-linear paper.

## Mathematical value — PASS

This is a complete structural classification, for every prime denominator and every fixed monomial degree at least two, of the *least* period and exact rational density of a natural coprimality indicator. The same mechanism identifies a finite power-residue-coset spectrum, an exact coefficient mean, and a quantitative uniform transition to the classical irrational-slope constant. These features are meaningful for comparing rational and irrational floor-polynomial gcd statistics and are not supplied by merely enumerating small cases. The estimate does not claim a uniform error when \(k\) grows, nor does it solve composite denominators.

## Closest literature and unresolved risk

The motivating source's hypotheses exclude rational coefficients; the closest older polynomial paper likewise uses irrational Diophantine hypotheses, while the older rational references focus on linear floors. Classical character bounds are incorporated but not new. An independently authored mathematical proof review and an exhaustive historical-priority investigation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
