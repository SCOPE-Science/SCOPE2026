# Self-review

## Correctness — PASS

The supplied proof checks negative type with the unnormalized Walsh transform. It derives the Krawtchouk telescoping identity directly from its generating function; it does not infer a universal statement from finite samples. For four-cap dimensions at least eight, the nonconstant Fourier spectrum is governed by a cubic in \(z=n+1-2s\). The difference from its parity value factors as \((z+n-1)R(z)\), where \(R\) has the explicit positive lower bound in RESULT.md. The parity root is unique by a strict derivative comparison. The centered Gram rank gives the stated endpoint embedding dimension. The all-even-cap limit is a uniform comparison based on \(|K_j|\le\binom{n-1}{j}\). The supplied reproducibility checker passed all tests; it verifies finite identities only.

## Originality — PASS (bounded)

The closest previous scientific result is the three-capped Hamming negative-type threshold: its quadratic Walsh minimizer and \(n^{-1}\) scale do not determine the cubic parity minimizer for cap four, the one-dimensional endpoint kernel, or the \(n^{-(r-1)}\) even-cap hierarchy. Sánchez (2011) provides a general finite-metric method, Schoenberg (1938) provides the positive-definite-kernel equivalence, and Feinsilver–Schott (2018) supplies general Krawtchouk machinery. None of the materially inspected text states the present special thresholds. Deza–Maehara (1990) and Maehara (1986) are plausible antecedents in metric transforms, but complete primary text was not accessible; this leaves a historical priority risk. Failed discovery searches are not treated as proof of novelty.

## Mathematical value — PASS

Capped metrics model bounded or saturated dissimilarity. The result supplies a sharp scale for every fixed even truncation radius, not merely a fixed-size computation, and an exact formula and complete Hilbert-embedding rank transition for cap four. The parity obstruction is structurally different from the middle-band obstruction for cap three. This provides a new quantitative boundary for Gaussian distance kernels and a concrete family where a single Walsh direction disappears exactly at the critical exponent.

## Limits

The exact cap-four proof starts at dimension eight; higher even caps are asymptotic, not exact finite classifications. A relevant older metric-transform paper was available only through secondary descriptions, so stronger historical coverage cannot be categorically excluded. No independent review was performed.

Self-review: passed. Independent audit: not yet performed.
