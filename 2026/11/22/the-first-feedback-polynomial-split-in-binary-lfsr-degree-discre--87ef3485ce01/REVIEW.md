# Scientific review

## Correctness — PASS

The finite claim has an exhaustive domain: the \(2^{k-1}\) monic odd coefficient masks at each \(2\le k\le5\). A full nonzero orbit of length \(2^k-1\) is equivalent to a primitive polynomial. Every valid full-cycle mask is examined, all starts and lengths through the complementary half-period are enumerated, and the complementary identity proves that no other length matters. The integer expression \(G=2M D\) removes every rounding issue. Separate recount-from-scratch and sliding-update routines agreed at 111 primitive-polynomial/horizon pairs. The fractions and reciprocal pair are explicitly asserted and reproducible using `verify_peak.py`. The theorem is finite and does not extrapolate to larger degrees.

## Originality — PASS, with residual risk

The closest publication, Pääkkönen's arXiv:2611.15635v1, defines this precise observable in Section 3 and states in Section 4 that it chooses one primitive polynomial per degree. Its degree-five table therefore cannot imply a six-polynomial spectrum or the first sensitivity threshold. Its grid sampling for degree five also differs from the exhaustive horizon maximum here. An earlier cited paper on fixed-horizon best-window optimization could not be inspected in full; it is a residual priority risk, though the cited description is not a complete polynomial-spectrum theorem. Search comparisons with published other discrepancy spectra concern de Bruijn-factor balance or autocorrelation rather than highest-bit degree frequencies. No general unpublished/poorly indexed equivalent is ruled out.

## Mathematical value — PASS

The source presents the normalized maximal discrepancy as a function of degree, yet degree alone does not determine its exhaustive peak. This complete classification identifies the **first** degree at which the feedback polynomial is a genuine parameter, rather than selecting an arbitrary numerical subcase. The reciprocal-pair obstruction distinguishes even closely related generators, relevant when interpreting one-polynomial-per-degree experimental envelopes. Its bounded finite scope is a limitation, not an asymptotic discovery.

## Scientific limits

Complete proof concerns only degrees two through five and a fixed power-basis convention. The earliest cited submitted companion study lacks accessible full text, so priority has an acknowledged residual risk.

Self-review: passed. Independent audit: not yet performed.
