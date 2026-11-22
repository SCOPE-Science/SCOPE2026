# Review of the genus-pivot gap distribution

## Correctness — PASS

Shor's fully specified gap decomposition shows that the interval of missing integers containing the genus index is exactly \([qa+1,g]\), hence its length is \(r=g\bmod a\). Counting multiplicities by divisors of \(g-r\) gives the complete histogram, including the ordinary semigroup's exceptional \(r=g\). The mean is a double-counted summatory-divisor identity. The CDF proof explicitly controls the small-multiplicity region, counts at most \(O(\sqrt g)\) affine branch intervals on the remaining grid, and bounds excluded divisor indices, giving uniform error \(O(g^{-1/2})\). The transformed-uniform density and zeta moments are proved by convergent elementary integrals. The standard-library checker independently reconstructs all gap sets and exact histograms for every genus through 90.

## Originality — PASS on inspected evidence

Shor's 2022 preprint (full text, Proposition 3.4 and Section 5) already describes each gap set and the eligible multiplicities. In particular, the elementary identity \(R=g\bmod a\) is prior-implied and is not an original standalone claim. A published exact isolated-gap distribution for reflective semigroups (complete publicly accessible RESULT.md inspected) counts the number of **isolated** gaps, a discrete heavy-tail invariant, rather than the length of the contiguous block of gaps containing \(g\). Related Arf-closure findings concern the number of added individual gaps. Semantic searches for normalized remainders, genus-pivot gap blocks, aliases, and harmonic limits found no equivalent finite-genus divisor histogram together with a continuous harmonic-step law, quantitative convergence, and its zeta moments. The general parametrization is strong input, and an unindexed or implicit derivation could exist.

## Value — PASS

The gap run crossing the defining reflection pivot is intrinsic, well specified, and measures a different aspect of gap geometry from isolated-gap counts and global genus/Frobenius statistics. Its finite-genus histogram is a complete natural invariant distribution, and its scaled limit has a surprisingly piecewise-harmonic density with explicit zeta moments and a uniform finite-population error. The precise statistic is motivated before calculation by the reflection geometry; this is not a random or fixed arbitrary numerical slice. The main value lies in population-level structure, not the easy observation that a single run has length \(g\bmod a\).

## Closest literature and limitations

The primary parametrization and per-semigroup gap set are established in Shor's arXiv:2207.00051v1 (2022). The later isolated-gap population theorem is close in the underlying family but not covering the continuous length statistic. An earlier same-family asymptotic for a different numerical invariant was also checked for overlap. Attributing the established classification is essential; neither uniqueness of an unpublished theorem nor mathematical independence is claimed. This has only self-review and no independent audit.

Self-review: passed. Independent audit: not yet performed.
