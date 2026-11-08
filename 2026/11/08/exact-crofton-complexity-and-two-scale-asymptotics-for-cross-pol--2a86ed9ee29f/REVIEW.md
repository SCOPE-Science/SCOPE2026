# Scientific review: Crofton complexity of regular cross-polytopes

## Correctness — PASS

The claim uses invariant measure on intersecting **affine** hyperplanes, not Haar measure on central hyperplanes or uniform orientation without directional-width bias. With \(k\) signed vertices above the offset, exactly \(k(2d-k-1)\) non-antipodal edges cross the section. The Gaussian-radius cancellation reduces the conditioned Crofton measure to expected half-normal spacing lengths; the resulting masses telescope and sum to one. A separate edge-by-edge integration gives \(2d(d-1)/(\sqrt\pi\,\mathbb E H_{(d)})\) for the expected section vertex count. The beta exponent follows from upper order statistics at rank \(d^{y+o(1)}\); quadratic-scale rarity comes from the interior sample quantile; the positive-moment law follows by a Gaussian-tail dominated-convergence bound. The octahedral specialization is checked analytically by integration by parts.

The standalone program independently simulates weighted affine hyperplanes and enumerates all crossed graph edges. In dimensions three, four, six it agrees with the complete order-statistic law; the numerical integral reproduces the mean from the independent edge formula and the exact octahedral constant. The program is corroborative only: it does not certify asymptotic statements.

## Originality — PASS, with priority risk

The closest overlapping work addresses different geometric operations or observables: Donoho–Tanner (2006 and 2008) count surviving faces under **random projections**; Kabluchko–Litvak–Zaporozhets (2015) study **mean width** and random projection lengths, supplying already-known Gaussian maximum asymptotics but not a translated-section complexity law. De Loera–Lopez-Campos–Torres (2024/2025) study deterministic maximal and attainable hyperplane-section vertex counts and recall the edge-crossing principle, but not an affine Crofton probability distribution for cross-polytopes. Another published record gives an exact **diameter** distribution for **central** cross-polytope sections; diameter is not vertex count, and central planes do not carry the Crofton translation distribution. An already recorded affine-simplex section theorem gives the same beta limiting exponent for a different polytope; this coincidence is acknowledged. No implication from these results supplies the claimed finite cross-polytope law, sharp quadratic-scale rarity or positive-moment constants. A targeted search for equivalences and tables did not locate dominating coverage, but a negative search is not a proof of global novelty.

## Mathematical value — PASS

This is a natural full-dimensional sequence of sections of the regular \(\ell_1\) ball, rather than a parameter-only variant of an isolated finite problem. The exact distribution classifies all possible section-vertex counts for **every dimension**, including the top-count degeneracy. It distinguishes two incompatible complexity regimes: a nondegenerate beta-distributed logarithmic exponent for typical sections and an exact logarithmically rare quadratic upper tail dominating all fixed positive moments. The sharp tail coefficient is an intrinsic quantile of the half-normal law; the result offers a reproducible benchmark for high-dimensional Crofton section complexity.

## Scope and remaining uncertainty

All conclusions are restricted to codimension-one translated affine sections of unit-radius regular cross-polytopes, and the limiting statements require fixed threshold or fixed positive moment order. Numerical checks are finite. The inspected sources do not exclude unindexed results or every historical special case, and independent audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
