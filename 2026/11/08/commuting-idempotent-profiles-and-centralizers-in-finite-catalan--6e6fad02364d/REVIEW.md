# Scientific review: commuting-idempotent profiles in Catalan monoids

## Correctness — PASS

A classical Catalan idempotent is the floor map to its fixed-point subset containing the least chain element. The proof derives the mixed-exclusive-point obstruction by evaluating the two composites at a fixed point of the second map, and proves sufficiency gap by gap. This establishes a bijection between commuting ordered pairs and concatenations of independently colored gaps. Each gap of length \(d\) contributes \((1+u)^{d-1}+(1+v)^{d-1}-1\), leading to the stated rational trivariate generating series. A separate endpoint-inclusion argument counts the idempotents commuting with every fixed \(e_S\). Standard partial fractions establish the exact total and probability asymptotic; differentiation in \(w\) gives the common-fixed-point statistic. There is no extrapolation from finite counts.

The standalone Python verifier independently enumerates all order-preserving decreasing maps through chain size seven, checks the idempotent normal form and directly composes all ordered idempotent pairs through chain size nine. Its independent gap enumeration matches **every** trivariate coefficient for each of these dimensions. It also verifies every centralizer count through size nine and the total recurrence, completing with `VERIFY_OK`.

Residual correctness risk: the verifier covers only stated finite dimensions. The infinite result rests on the textual bijective proof and standard rational-function manipulations, not computational extrapolation.

## Originality — PASS relative to inspected sources

Pantazi–Spircu determine and study the idempotents of individual Catalan monoids, while Ayık–Ayık–Koç (2011) count elements by their fixed-point sets (publisher abstract inspected; full text inaccessible). Sapir–Volkov compare classical Catalan monoids with their partial-injective variants, whose idempotents commute. Toker (2021) counts zero-divisors and graph edges with both products equal to the zero map, not all commuting pairs. Andrenšek's 2026 Corollary 3.9 supplies a general **decision criterion** for commutation of idempotents in Hecke–Kiselman monoids, so neither the idempotent normal form nor a general commuting criterion is asserted as novel. The present claim is the explicit **trivariate enumerator** separating the two exclusive fixed-point sets and their intersection, with a specialized closed sum for each idempotent's commuting-idempotent centralizer, plus quantitative asymptotics.

OEIS A007070 already contains the unrefined sequence \(1,4,14,48,164,\ldots\) (offset one) and the recurrence. The sequence by itself is not claimed new. The relevant implication test is whether any inspected source gives the *color-weighted Catalan-idempotent interpretation or an equivalent stronger parameterized theorem*, rather than merely identical coefficients or an abstract commutation test. No such coverage was identified. Targeted published-record and mathematical-literature searches were conducted, not treated as a mathematical proof of publication priority.

Residual originality risks: uninspected literature under compatible Catalan / Hecke–Kiselman / transformation-centralizer terminology may contain an equivalent refined enumeration; the 2026 general criterion might make it easy to rediscover, though it does not itself state the rational generating function. The 2011 full text could not be inspected, and some earlier relevant records were inaccessible; these absences are not treated as novelty proofs. Publication priority is provisional.

## Mathematical value — PASS

The motivating structural contrast is substantive: the partial-injective Catalan variant has pairwise commuting idempotents, whereas the classical total Catalan monoid does not. The new enumerator gives an exact **whole-family measurement** of this failure for every finite chain size, and refines it by all three natural fixed-point parameters. The centralizer formula answers the individual-idempotent version of the same question, rather than appending an arbitrary finite slice. The exponential commutation decay and the linear typical common-fixed-point scale for commuting pairs reveal information not supplied by the bare idempotent count or the existing OEIS recurrence. This is a natural semigroup invariant, not an arbitrary numerical coincidence.

The findings do not address non-idempotent commutation or higher tuples. The work is not represented as independently verified or as a certified priority claim.

Self-review: passed. Independent audit: not yet performed.
