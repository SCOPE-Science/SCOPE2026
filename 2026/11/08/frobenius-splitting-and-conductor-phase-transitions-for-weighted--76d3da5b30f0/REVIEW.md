# Self-review

## Correctness

**PASS.** The monomial degree-\(a\) exponent interval follows from exact enumeration by the number of weight-\(e\) generators and a checked adjacent-interval inequality. This gives the full semigroup, not merely its Hilbert function. The normalization and conductor follow by adjoining \(t^d\) and checking arbitrary multiplication by normalized monomials. The monoid seminormalization and Frobenius splitting/failure follow from explicit lattice witnesses and the monomial projection; these are infinite proofs. Exact diagnostics from `check_weighted_curve.py` cover 56 small parameter pairs, five primes, and conductor residue tests; they do not replace the proofs.

## Originality

**PASS, subject to historical priority.** The closest primary studies are Banks--Ramkumar, arXiv:2604.17735 (weighted minimal-degree geometry) and Davis--Sobieska, arXiv:2410.04586 (weighted rational embeddings, determinantal equations, Hilbert series and nonnormality). The inspected sections do not provide the exact conductor, its degree-\(e\) map on the nonnormal divisor, or the splitting/seminormality phase diagram. General affine-monoid results of Bruns--Li--Römer, Nguyen, and De Stefani--Montaño--Núñez-Betancourt provide broad criteria; deriving these family-specific statements still requires the precise semigroup and boundary calculation. Overlap searches of accessible prior records and published-finding corpus found no equivalent. An unlocated explicit treatment, or a general monoid theorem whose worked example exactly coincides, remains a risk.

## Value

**PASS.** These two-parameter weighted rational cones are geometrically natural despite their smooth weighted-projective curve and excellent homological properties. The conductor and degree-\(e\) nonnormal divisor map identify the concrete failure of normality, while the sharp characteristic-dependent Frobenius-splitting threshold separates mild nonnormal singularities from more severe cases in a natural infinite family. A complete parameter classification and explicit geometric conductor have use independent of the source Hilbert series.

## Limitations

Classification is not for arbitrary weighted scrolls, and potential independent historical priority remains unresolved. The checker only tests finite truncations. The source introducing the original rational curve family predates the two-year recent boundary, but the later 2026 motivating source treats a new weighted minimal-degree framework and is the first-public source for this direction. General methods may imply parts of the theorem without an exact published family specialization.

Self-review: passed. Independent audit: not yet performed.
