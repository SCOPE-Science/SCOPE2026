# Scientific review of the two-collision \(\Lambda(4)\) plateau

## Correctness — PASS

The claim is a precise sharp fourth-power \(L^4\)-to-coefficient-\(\ell^2\) bound for every compact abelian group and every finite spectrum with exactly two pair-product collision fibers, each consisting of two disjoint off-diagonal pairs; the quartets share one character. Parseval on \(F^2\) yields exactly two interference terms. Squared-modulus balancing and the derivative sign in the split parameter show that the upper bound reduces to either a one-quartet boundary or a balanced two-quartet branch. The former has exact maximum \(9/4\); the latter is strictly lower by the displayed positive sum-of-squares identity. Equality is exhausted by one aligned quartet with four equal coefficients. Exact arithmetic enumerates every two-sum collision for positive cubes through index 23. The standalone checker reports `VERIFY_OK finite_prefixes=23 unordered_pairs=2300 exact_moment_checks=700 equality_witnesses=2 sos_identity=1`. The proof, not finite sampling, establishes the universal statement.

## Originality — PASS relative to inspected evidence

The closest published note, *Sharp \(\Lambda(4)\) constants for a single pair-product collision* (2026-10-11), assumes exactly one nonsingleton pair-product fiber and expressly excludes multiple simultaneous collisions. Its \(9/4\) single-quartet theorem does not imply that introducing a second quartet overlapping in one character preserves that bound. The 2023 Gabdullin–Konyagin paper (arXiv:2311.14937) treats short intervals of cubic frequencies, the taxicab obstruction and qualitative fourth-moment estimates, but not the sharp two-resonance interval or equality classification. Vasilyev's 2026 preprint (arXiv:2608.19132, first public August 19) concerns bounds under nonincreasing coefficient magnitudes, not these unrestricted complex extremals. Targeted exact-phrase, alias, collision-type and polynomial-spectrum searches did not identify an equivalent theorem. A differently indexed additive-energy or \(B_2\) theorem remains a residual bibliographic risk.

## Mathematical value — PASS

The theorem resolves the first genuinely interacting two-resonance extension of the basic \(\Lambda(4)\) collision principle. It identifies a sharp norm plateau and proves all optimizers suppress one of the two resonances, rather than simply adding their contributions. The canonical cube-frequency example provides a natural arithmetic threshold: the sharp constant is exactly \(9/4\) from the first resonance at index 12 through index 23, despite another at index 16. This exact interval and rigidity are meaningful structural information, not a routine numerical restatement. No result is claimed beyond the stated collision incidence or range.

## Closest literature and residual limitations

- I. Vasilyev, *Norm bounds on Fourier series with polynomial spectra and constrained coefficients*, arXiv:2608.19132, 2026-08-19.
- M. R. Gabdullin and S. V. Konyagin, *Trigonometric polynomials with frequencies in the set of cubes*, arXiv:2311.14937, 2023-11-25.
- *Sharp \(\Lambda(4)\) constants for a single pair-product collision*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-4-constants-for-a-single-pair-product-collision--b11b0dc59997.

The broad primary 2026 source was reviewed via indexed text/abstract where direct full-text access could not be restored. Older equivalent results using different terminology cannot be ruled out. Analytic correctness is distinct from historical novelty; independent mathematical review is still necessary.

Self-review: passed. Independent audit: not yet performed.
