# Scientific review

## Correctness — PASS

The claim is restricted to Franel output residues modulo eleven and gives a theorem for every full digit block and every cutoff. Lucas's theorem proves the digit factorization directly. The eleven one-digit integer sums, the logarithmic multiplicity vector, the ten-term cyclic autocorrelation, and its four monic cyclotomic remainders are independently calculated in `check.py`. Character orthogonality and Parseval turn these exact identities into the displayed variance, while aligned digit-block decomposition proves the arbitrary-cutoff upper bound. The variance gives a rigorous lower bound of \(11^{r/2}/5\) for at least one unit residue at each depth; finite tests are not substituted for these deductions.

## Originality — PASS, with limits

The nearest primary work by Z.-W. Sun, *Congruences for Franel numbers* (arXiv:1112.1034, Theorem 1.1), concerns weighted prime-square sums of Franel values. Z.-H. Sun's 2017 *Congruences for sums involving Franel numbers* similarly concerns finite weighted prime sums. Henningsen–Straub's 2021 Lucas-congruence framework supplies general digital multiplicativity, but not the special eleven-digit autocorrelation remainder \(Q\equiv11\pmod{\Phi_{10}}\), the exact variance, or its sharp arbitrary-cutoff consequence. OEIS A000172 supplies the sequence rather than a matching output-frequency spectrum. Related known archival Franel results at primes five and three address distinct residue characters, correlations, or nondivisibility index supports. Searches of related published records and primary-literature aliases found no direct implication matching the full formula. This is a qualified priority assessment, not a uniqueness certificate; an unindexed digital-Fourier specialization remains possible.

## Mathematical value — PASS

For a binomial-cube sum of longstanding arithmetic interest, eleven is the first prime after five and seven at which no one-digit Franel value is divisible by the prime. This makes the exact distribution among *all* unit values a natural question. The theorem provides each complete-block frequency by an explicit group-ring formula and an unexpectedly simple closed variance, then proves a sharp square-root law for all initial intervals. The primitive tenth-root spectral cancellation is the structural point that makes exponent \(1/2\), rather than a generic digit-mixing exponent, exact. These are reusable benchmarks for digital congruence distributions, not an isolated unchecked finite table.

## Scope and residual risk

There is no claim for Franel residues modulo higher powers of eleven, nor of independent validation. The closest sources were inspected for theorem content and searched for residue-distribution vocabulary, but the full historical literature cannot be exhaustively excluded.

Self-review: passed. Independent audit: not yet performed.
