# Review of the dyadic adjacent-quadratic valuation law

## Correctness: PASS

The underlying quadratic is a product of two linear factors in the dyadic integers because both simple roots modulo two lift uniquely. On each parity class the two observed valuations equal distances to two same-parity centres. The two collision depths are exactly \(1\) and \(d=\nu_2(|a^2-b^2+4ac|)-1\), by the discriminant product identity. The two-centre lemma enumerates every pair and yields one residue class modulo the specified power of two; no numerical extrapolation is used. A geometric tail bound justifies the covariance limit. The accompanying executable independently checks 128 coefficient triples, including the zero-resultant boundary, against 81 exact cell probabilities and 49 modular one-class assertions per triple.

## Originality: PASS, with residual risk

The 2020-12-18 Boultinghouse–Long–Kozhushkina–Trulen preprint and the 2021 journal full text classify one-point valuation trees, rather than neighbouring-index pairs. Medina–Moll–Rowland classify valuation boundedness and periodicity, not this law. The closest known research finding derives a joint-root correlation law for **odd primes**; its statement does not include \(p=2\), and the present coefficient-level dyadic phase diagram and sharp sign threshold are not directly asserted there. The Hensel/nested-ball technique itself is standard and is **not** claimed as novel. Equivalent unindexed dyadic-correlation research is still possible.

## Value: PASS

A complete bivariate sequence statistic is determined for an infinite natural coefficient family previously treated only one coordinate at a time, including all impossible transitions, exact one-residue frequencies, and the full attainable covariance spectrum. Unlike a routine reparametrization, the answer identifies a sharp, observable change from negative to positive neighbouring dependence at the arithmetic boundary \(16\mid(a^2-b^2+4ac)\), with examples achieving every phase and covariance value. This supplies an interpretable local-dynamical invariant for the quadratic valuation tree family.

## Closest literature and limitations

- W. Boultinghouse, J. Long, O. Kozhushkina and J. Trulen, *2-Adic Valuations of Quadratic Sequences*, arXiv:2012.10332, first posted 2020-12-18; *Journal of Integer Sequences* 24 (2021), article 21.6.1: single-index trees.
- L. Medina, V. Moll and E. Rowland, *Periodicity in the p-adic valuation of a polynomial*, arXiv:1505.02302: boundedness and periodicity.
- Closely related odd-prime joint-root collision results: methodology overlaps, but dyadic adjacent-quadratic phase classification is outside their quantified prime domain.
- Limitations: only positive odd \(a,b\) and positive even \(c\); finite arithmetic verification is not an infinite proof; possible unindexed prior literature.

Self-review: passed. Independent audit: not yet performed.
