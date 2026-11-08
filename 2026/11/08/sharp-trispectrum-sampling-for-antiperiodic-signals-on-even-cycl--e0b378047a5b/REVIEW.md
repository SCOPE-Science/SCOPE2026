# Scientific review

## Correctness — PASS

The polyspectrum identity is obtained directly by exchanging finite sums with the stated unnormalized transform. For two real signals with equal power spectrum, the nonzero odd-frequency coefficient ratios have unit modulus and conjugate symmetry. The sampled trispectrum relations force their successive phases to be powers of the first ratio. The final relation and conjugation, treated separately for the two congruence classes of the even length, force an \(N\)-th root of unity and therefore an exact translation. The converse is translation invariance. The phase-torus argument proves the lower bound without relying on finite enumeration. The independent standalone script checks exact exponent determinants for 99 even orders, finitely enumerates phase fibers at five small orders, and computes the actual fourth-order autocorrelation Fourier transform at five orders.

## Originality — PASS relative to inspected sources

Agulnick–Busick-Warner give general higher-autocorrelation sufficiency statements, not an explicit least number of individual fourth-spectrum entries in the all-odd-nonzero regime. Grünbaum–Moore (1995) assume rational cyclic signals with a nonzero mean, excluding the antiperiodic class whose mean is identically zero, and do not quantify minimal fourth-order individual entries. Casper–Orozco treat rational data and demonstrate a different sparse-support obstruction; their counterexample for order six has zeros at the self-conjugate odd frequency and hence does not cover the stated class. Bendory–Edidin–Kreymer's few *generic linear measurements* of high-order spectra are neither fixed individual trispectrum entries nor the same real anti-periodic class. Search comparisons against the connected mathematical-results index showed the closest bispectral sample-count theorem for asymmetric frequency bands, which makes different support and order assumptions and does not imply the present fourth-order theorem. An unindexed equivalent derivation in invariant theory remains possible; novelty is relative to the searched evidence, not mathematically certified by absence of a hit.

## Value — PASS

This family has complete loss of all odd-order autocorrelations, making ordinary bispectral phase recovery impossible. Determining exactly how much fourth-order data repairs that obstruction, **for every signal in the class**, is a well-motivated finite sampling problem. The constructive recurrence achieves the information-theoretic nonadaptive lower bound of \(\lfloor N/4\rfloor\) complex entries with exact translation ambiguity. The result is an exact optimal sampling specification, not a routine reparameterization of a generic sufficiency criterion.

## Closest literature and limitations

The 1995 classical cyclotomic invariant article, 2026 general autocorrelation bounds, 2025 rational reconstruction/counterexamples, and 2021 generic high-order spectrum compression paper are compared in RESULT.md. The full odd-frequency nonvanishing condition, real signals, known power spectrum, and nonadaptive *individual* complex trispectrum entries are essential scope restrictions. Perturbation stability and arbitrary functionals are not addressed. There has been no independent external assessment.

Self-review: passed. Independent audit: not yet performed.
