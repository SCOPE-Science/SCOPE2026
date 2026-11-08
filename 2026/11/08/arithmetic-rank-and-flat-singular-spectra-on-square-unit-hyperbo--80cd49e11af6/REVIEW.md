# Mathematical review

## Correctness

**PASS.** Multiplicative Fourier diagonalization converts the square hyperbola Fourier matrix into character sums on the subgroup of unit squares. The split group structure modulo a prime square gives a *complete* stationary-phase calculation, with no neglected residue classes. The only potential cancellation arises from the paired stationary points \(x\) and \(-x^{-1}\); their phase quotient has a primitive \(p^2\)-part and cannot equal the negative of a tame-character root. Counting the resulting involution orbits yields the exact rank in all three congruence classes. When \(p\equiv3\pmod4\), every surviving term has modulus \(p\), so the claimed singular-value multiplicities follow. The proof handles every primitive additive character, not those of conductor \(p\). Numerical direct Fourier matrices were checked at five primes and two allowable additive characters apiece; these finite checks are not a proof of the infinite statement.

## Originality

**PASS, subject to historical-priority risk.** Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162, Section 2, provides the elementary stationary-phase formula for the **full unit-group** multiplicative-character twists. This classical ingredient is openly acknowledged, rather than claimed new. The current result is a rank and partial-isometry classification for the **index-two square-unit hyperbola self-Fourier matrix**. Unlike the full-unit character-sum formula, the rank classification requires the square-subgroup stationary fiber map, its noncancellation analysis, and a modulo-eight orbit count. Hickman and Wright, arXiv:1801.03176, study analytic restriction inequalities over residue rings and do not identify this finite self-sampling matrix spectrum in the sections inspected. Related existing finite-field hyperbola and torus results differ in their modulus and stationary-fiber geometry. This evidence does not establish global uniqueness; an equivalent formulation may survive in earlier literature.

## Value

**PASS.** Squares of units form the canonical index-two multiplicative subgroup, and modulus \(p^2\) is the first nonfield stage of a prime-power ring. For this natural partial hyperbola the Fourier self-sampling rank is sharply noninjective and changes according to \(p\pmod8\); at half the odd primes every nonzero singular value is exactly \(p\). This is a complete arithmetic recovery-capacity classification with a sharp stability statement on the recoverable subspace, not an isolated computation or an arbitrary numerical slice.

## Evidence and limits

The critical proof identity and the orbit count are stated in `RESULT.md`. `checker.py` directly builds the unnormalized Fourier matrix and tests \(p\in\{3,5,7,11,13\}\) with permissible primitive characters, plus the exact stationary-map cardinalities up to \(p=41\). Mathematical use of the numerical checks is corroborative only. The result does not imply injectivity, phaseless reconstruction, larger conductor cases, or universal nonzero singular values for \(p\equiv1\pmod4\). A historically equivalent rank statement remains possible.

Self-review: passed. Independent audit: not yet performed.
