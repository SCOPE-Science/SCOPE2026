# Scientific review

## Correctness

PASS. The random-location approximation ratio reduces exactly to the reciprocal-gap identity (1); the finite optimum is the minimum consecutive spacing. Exponential spacings remove the common normalization, while a heavy-tailed reciprocal law yields the factor \(2n\log n\). The adjacent-maximum correction to the squared reciprocal sum is negligible at scale \(n^2\). Joint Poisson convergence of the rescaled minimum and inverse-square point sum then proves the stated distribution by Slutsky's theorem. The finite exact-rational checker passes \(3,223\) location profiles and \(125\) seeded scale tests. The checker is diagnostic only; it does not prove convergence.

## Originality

PASS, with residual literature risk. The defining mechanism and worst-case \(\Theta(\sqrt n)\) guarantee are established by Chan–Lin–Wang, arXiv:2608.22484, Section 4. The original full primary text was examined, including its incentive and approximation proofs, and no uniform-random-sample, logarithmic or Poisson limit was found. Fotakis–Tzamos, arXiv:1305.3333, Section 6, gives an alternative mechanism and a worst-case factor \(2\), not the asserted law for Inverse-Square. Published mathematical-record searches using mechanism names, inverse-square weighting, random uniform gaps and Poisson extreme sums found no claim entailing this exact limit; absence from indexing cannot prove absolute priority. Historical research claims of gap-product facility selection concern a different sampling rule and a fixed number of facilities.

## Mathematical value

PASS. The theorem exposes a concrete logarithmic typical-performance penalty for a natural recently proposed strategyproof rule, quantitatively distinguishing typical behavior from its substantially weaker square-root worst-case envelope. The random Poisson limit is sharper than a mere order bound and reveals how the smallest neighboring gap interacts with many reciprocal spacings; it offers a benchmark for comparing robust metric mechanisms and line-specific alternatives.

## Remaining limits

Uniform independent samples, one fewer facility than agents, and linear social cost only. The result is in distribution, not in expectation. General metrics are used only to contextualize the mechanism's existing worst-case theorem. Published work outside inspected materials may contain an equivalent result.

Self-review: passed. Independent audit: not yet performed.
