# Self-review

## Correctness (C) — PASS

The statement fixes the algebraic closure of characteristic five, the two-parameter normalized equation, the smooth locus \(b\Delta\ne0\), and the precise definitions of \(5\)-rank and Cartier \(a\)-number. Smoothness follows by the separable cubic substitution \(t=x^3\). The coefficient calculation produces the full \(4\)-dimensional Cartier matrix, and the stable rank is proved using the **inverse-Frobenius semilinearity**, not an untwisted matrix square. In particular, the relevant invariant is \(\lambda=(2a+1)^5b^2+2(2a+2b)^5\), not an expression obtained by swapping the twisted matrix factors. Both elimination identities on \(w=0\) are exact over \(\mathbb F_5\) and establish a single reduced rank-zero point after excluding singular parameters. Independently implemented point counts through degree four over \(\mathbb F_5\) establish all four witness ranks by Newton identities. Both packaged programs were run and completed. These finite checks do not prove the universal algebraic-closure theorem; the symbolic proof does.

## Originality (O) — PASS, subject to residual historical-priority risk

Kudo--Nakagawa--Takagi, arXiv:2210.14822v1, introduce exactly this family and prove the already known \(p\equiv2\pmod3\) Cartier rank bound, which would imply nonordinarity if applied in characteristic five. Their stated main classification/algorithm assumes \(p\ge7\) and concerns superspecial curves; it does not state the present characteristic-five coefficient-wise stable-rank strata or the single reduced rank-zero parameter. The general no-\(a\)-number-three conclusion is already proved by Frei (arXiv:1703.03516, §4.2) and is not presented as a new contribution. A general 2022 cyclic-cover moduli stratification supplies global existence and boundary results, not this exact normalized arithmetic locus. Targeted prior-literature comparisons did not yield a dominating result. An unindexed computation or a general cyclic-cover formula specialized to these coefficients could contain an equivalent statement; database absence does not prove priority.

## Mathematical value (V) — PASS

The motivating 2022 work specifically studies this order-six automorphism family to find unusually small Cartier ranks, but excludes characteristic five from its main calculation. The specialization is *not* a random low-dimensional polynomial slice: it comes with a natural genus-one quotient and a separate three-dimensional complementary Cartier block. The theorem determines their stable ranks simultaneously and gives the **entire** arithmetic stratification of the smooth characteristic-five parameter surface, including a unique transverse rank-zero intersection. The exact isolated lowest-rank parameter is a natural extremal locus relevant to arithmetic moduli, and the distinction between Cartier rank and stable rank is essential. No arbitrary bounded enumeration is promoted to a universal theorem, and neither the published family nor the published nonordinarity mechanism is claimed as new.

## Closest literature and limitations

The principal exact-object source is Kudo--Nakagawa--Takagi (arXiv:2210.14822v1, §§2–3). The closest relevant general obstruction is Frei (arXiv:1703.03516, §4.2). Generic cyclic-cover rank-stratum results provide background but do not settle this coefficient-normalized locus. The count is of parameter pairs, not isomorphism classes; no Newton polygon or supersingularity classification is asserted. Independent audit and outside priority determination are not performed.

Self-review: passed. Independent audit: not yet performed.
