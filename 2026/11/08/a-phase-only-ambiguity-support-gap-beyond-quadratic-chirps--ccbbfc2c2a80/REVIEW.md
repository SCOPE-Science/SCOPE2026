# Scientific review: a phase-only ambiguity support gap beyond quadratic chirps

## Correctness — PASS
The theorem quantifies over all unimodular complex-valued sequences on prime cyclic groups of order at least five. The key new lemma excludes Fourier support cardinalities two and three for any unimodular function on these groups: a two-/three-point Fourier support has an ordered difference represented uniquely, contradicting constancy of the squared modulus. For three points, the six directed differences cannot all have multiplicity two because nonzero differences occur in opposite pairs, and multiplicity three would make the three-set invariant under a generator. Every delay quotient is unimodular; a singleton quotient is a character, and the prime-order recurrence forces a quadratic chirp. The remaining rows each contribute at least four nonzero entries. The five-point root-of-unity impulse perturbation is computed algebraically, has precisely one zero per nonzero-delay Doppler row, and attains 17 entries. The exact computational checker passes 3443 conditions, including exhaustive five-phase prime-5 codes, but is not used as an infinite proof.

## Originality — PASS, provisional historical priority
Nicola (2022), Theorem 1.2, already gives the minimum \(p\) and identifies its equality cases; this older result is explicitly not treated as new. Krahmer–Pfander–Rashkov (2006), Proposition 4.4, supplies general support lower bounds but specializes to only \(p\) for two fully supported inputs. A separate published all-pairs support-gap theorem gives either \(p\) or at least \(2p\), attained in general with non-unimodular/non-self signal-window pairs; it does not cover the conditional threshold \(4p-3\). Benedetto–Benedetto–Woodworth (2011) study amplitude estimates for selected phase codes rather than counting the nonzero entries of every nonchirp ambiguity function. Search coverage for equivalent phase-coded, CAZAC, STFT, difference-sequence and cyclic Gabor language found no dominating theorem, but absence of an identified source is not novelty proof. A broadly stated unimodular Fourier-support theorem may imply the elementary row lemma, and unindexed periodic radar literature is a remaining priority risk.

## Mathematical value — PASS
The result is a natural structural boundary for phase-only coded periodic ambiguity: adding the physical constraints that the window equal the signal and every sample have unit amplitude separates all quadratic-chirp p-sample optimizers from nonchirps by a gap increasing linearly with prime length. It is not just another threshold for invertibility: every nontrivial delay has at least four nonzero Doppler harmonics, and the first admissible prime admits an explicit sharp witness. This is a motivated exact-support invariant for time-frequency concentration, with a precise all-prime scope and a meaningful finite endpoint. The theorem does not claim optimal support for all larger primes, magnitude stability, or noise robustness.

## Closest sources and limitations
- F. Nicola, arXiv:2204.14176v1 (2022), complete theorem and proof; the exact-p equality case is established prior work.
- F. Krahmer, G. E. Pfander, P. Rashkov, arXiv:math/0611493 (2006), Proposition 4.4 and finite STFT support discussion.
- J. J. Benedetto, R. L. Benedetto, J. T. Woodworth, arXiv:1107.1887 (2011), periodic ambiguity of unimodular Björck sequences and amplitude estimates.
- A sharp support gap above the odd-prime short-time Fourier uncertainty minimum (2026), published mathematical record; general p-to-2p support gap, logically weaker within the new constrained class.

The result is exactly about zero/nonzero cardinality. It makes no claim about near-zeros, higher-order spectra, composite moduli or global optimality of the bound for primes above five. Independent validation has not been carried out.

Self-review: passed. Independent audit: not yet performed.
