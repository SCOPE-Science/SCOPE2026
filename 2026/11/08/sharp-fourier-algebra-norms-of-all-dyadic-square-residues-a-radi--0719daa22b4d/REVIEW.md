# Self-review

## Correctness — PASS

The complete square set modulo \(2^k\) is exactly the disjoint union of its odd-square coset and four times the complete square set at depth \(k-2\). Additive orthogonality localizes the extra Fourier transform to eight frequencies. The two real residues from the prior depth are the cardinality \(c_k\) and the alternating count \(d_k\); all eight eighth-root phases have been evaluated, yielding the exact norm recurrence. The proof verifies the base cases separately, and the operator norm is attained on a point mass or a phase-aligned bounded function. The limiting formula follows from explicit ratios and a Lipschitz estimate, giving a quantified remainder. The standalone checker independently constructs all square sets and Fourier transforms for depths \(1\) through \(12\), and tests the recurrence at further depths. Finite verification supports but does not establish the all-depth proof.

## Originality — PASS (bounded historical comparison)

Green–Sanders (arXiv:math/0611286v1) proves quantitative coset structure from a Fourier-algebra norm bound, but does not determine the norm of the complete dyadic square set. Stangl (1996) gives its cardinality, not an identified operator-norm evaluation; the original full text was inaccessible, so this is a bounded comparison. Malikiosis (2022) studies spectral/tiling properties and cyclotomic zeros of general cyclic subsets, rather than sharp absolute Fourier sums of the stated sets. A distinct norm calculation for all square residues at odd prime powers expressly excludes characteristic two and does not imply the eight-frequency dyadic formula. Searches for aliases involving Wiener norm, complete quadratic residues, dyadic Fourier projections, and cyclic square spectra returned no statement covering the nested radicals, exact depth recurrence, or two separated parity offsets. This is evidence of noncoverage among inspected materials, not exhaustive proof of historical uniqueness.

## Mathematical value — PASS

The finite Fourier-algebra norm is the exact endpoint amplification factor of the idempotent multiplier. Complete modular square sets are a canonical arithmetic family and include singular nonunits. The characteristic-two completion is structurally different from the odd-prime calculation: the odd squares form one additive coset modulo eight, so exactly eight exceptional characters at each two-level step control the entire norm. The resulting nested radical, effective linear-growth constant, and two genuinely distinct parity offsets are not obtained from the classical cardinality formula or standard coarse idempotent bounds. The result determines a motivated invariant for all dyadic depths without requiring an unrelated downstream application.

## Limitations and priority risks

No intermediate-exponent operator norms or arbitrary composite moduli are proved. Originality is bounded by available primary texts and searches; Stangl's full original article was unavailable, although its known counting formula was consulted through a secondary mathematical source. General Fourier-algebra or dyadic quadratic-residue results not found in the examined searches could conceivably cover this special case. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
