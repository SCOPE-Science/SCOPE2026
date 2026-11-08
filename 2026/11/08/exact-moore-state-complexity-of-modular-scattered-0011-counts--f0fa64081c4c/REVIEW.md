# Scientific review: modular scattered \(0011\) Moore complexity

## Correctness — PASS

The theorem is quantified over every integer modulus \(m\ge2\) with binary inputs and outputs in \(\mathbb Z/m\mathbb Z\). Its four counters obey explicit and correct last-symbol recursions. Because the first two depend only on the number of zeros, the binomial shift identity gives exactly \(m\gcd(m,2)\) first-two-coordinate phases. The word \(W=1^{m-1}0010^{2m-2}\) acts on the zero phase as translation of the third coordinate; the letter \(1\) acts as a shear of the last coordinate. These actions generate all \(m^2\) fibers, and final zeros realize every first-two-coordinate phase. Four suffix outputs recover all four coordinates, establishing minimality. This proves the exact state count for all moduli, rather than assuming that a naive product construction is minimal. Independent finite-word counting, reachable-state enumeration, explicit witness checks and Moore minimization were reproduced from the included checker.

Risk and scope: the computational tests cover finite ranges only, and the result does not specify minimal Boolean acceptor sizes or arbitrary scattered patterns. Neither limitation affects the stated symbolic proof.

## Originality — PASS, with historical-priority risk

The closest 2026 source publicly identifies subsequence universality, binary Parikh classes and probability approximation as its aims, not an exact modular output-state formula. The 2024 generalized Parikh-matrix paper supplies a broad formalism for subsequence statistics, but the accessible descriptions do not contain a minimal Moore-state formula for \(0011\). Prior exact modular output complexity for the different pattern \(010\) is not a specialization: its dependent-counter relation and state count differ. Current database searches for the exact formula, modular scattered-subsequence automata, aliases and general matrix coverage returned no directly equivalent claim. This is a positive novelty assessment under the inspected evidence, **not** a proof of historical uniqueness. Full texts of the two especially relevant arXiv papers were inaccessible, so stronger implicit coverage in their general results remains a risk requiring independent literature verification.

## Value — PASS

Counting noncontiguous embeddings modulo \(m\) is a natural finite-state streaming problem; the minimum number of distinct output residuals is its exact finite-memory invariant. The \(0011\) pattern is the first balanced two-run binary pattern with two identical symbols in each run, so its prefix counters exhibit a nontrivial dependence: the \(00\) statistic is controlled by \(\binom t2\), producing a parity-sensitive restriction on reachable states. The theorem classifies this invariant for every modulus and shows that all constrained counter combinations are reachable and distinguishable. The exact odd/even transition is not implied by the standard four-counter construction, which only gives the loose upper bound \(m^4\), and differs qualitatively from the alternating triple pattern. The result supplies both an optimal streaming construction and an explicit minimality certificate.

## Sources and remaining limitations

Fazekas–Huang–Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices* (arXiv:2610.06717, first public 2026-10-05); Fazekas–Huang, *Generalized Parikh Matrices For Tracking Subsequence Occurrences* (arXiv:2407.04462); Rigo–Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (2015). Accessible primary abstracts and metadata were examined, but not their full texts. The result remains restricted to deterministic modular-residue output of \(0011\) and its letter complement. Historical priority and independent verification are not established.

Self-review: passed. Independent audit: not yet performed.
