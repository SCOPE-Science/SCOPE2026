# Scientific review: A sharp mobility boundary for hotspot spacing in cyclic epidemic networks

## Correctness — PASS

The mathematical assertion has been checked for the full stated domain \(n\ge5\), \(0<h<2/5\), positive rates, and for the complete five-cycle range \(0<h\le1/2\). The matrix \(K=P\operatorname{diag}(\boldsymbol\beta)P\) follows from the equal-population symmetric SIR-network model [1, Eq. (4)]. A rank-two secular identity reduces the top eigenvalue to a unique positive resolvent root. A proved cyclic convolution lemma gives strict Green-kernel radial monotonicity. Exact five-cycle Fourier multipliers yield a difference with the sign of \(2-5h\), and an independent factorization yields full arbitrary-rate permutation invariance at equality. The rational inverse calculations and all-rate matrix identity were replayed by `verify.py` using exact fractions (597 checks). These finite checks are supporting tests, not an infinite proof. The local invasion criterion and all endpoint restrictions are explicit.

## Originality — PASS, with residual risks

The initiating source [1] studies the SIR-network next-generation matrix and one exceptional transmission patch, including cycle geometry. Its inspected full-text model, cyclic section, results and appendices do **not** give a two-hotspot distance comparison, a uniform \(2/5\) mobility boundary or arbitrary-rate permutation erasure on the five-cycle. Altenberg [2] proves spectral comparisons when changing mixing matrices or strength, rather than permuting fixed heterogeneous rates at fixed mobility. Hajaiej, Han and Hua [3] study discrete rearrangements on integer lattices; such machinery could subsume aspects of the low-mobility ordering, but its inspected theorem does not imply the high-mobility five-cycle reversal. Separate source/alias/equivalence and database searches found no directly covering theorem. Full publication-priority certainty is not claimed; unindexed cyclic spectral comparison results and a recent periodic-lattice rearrangement article are residual risks. The convolution closure lemma is standard in spirit and is **not** claimed as independently original.

## Value — PASS

The geometric question is not an arbitrary parameter slice: with two heterogeneous patches, their relative separation is the first new spatial variable absent with one hotspot. The five-cycle is the smallest simple ring with two distinct two-step destinations; on a four-cycle the two length-two directions meet at the same antipodal vertex. The exact transition at a mobility fraction \(2/5\) is surprising: initially dispersing two hotspots suppresses invasion, whereas sufficiently strong movement on the same graph can make separation **increase** invasion potential. The exact rational witness actually switches which of two spatial arrangements crosses the disease-free instability threshold, with all local infection and recovery rates unchanged. At the transition, all arrangements of **arbitrary** rate heterogeneity share the same reproduction number. Together the uniform low-mobility theorem, exact reversal and all-rate invariance are a meaningful structural contribution beyond verifying a few five-node eigenvalues.

## Closest literature and limitations

[1] H. K. Das and L. M. Stolerman, arXiv:2308.01998 (2023), https://arxiv.org/abs/2308.01998, especially Eq. (4), Section 4.2 and the related appendices. Journal version DOI:10.1137/23M1579522.

[2] L. Altenberg, arXiv:1301.4969 (2013), https://arxiv.org/abs/1301.4969, especially Theorems 9–10 on variation of commuting mixing operators.

[3] H. Hajaiej, F. Han and B. Hua, arXiv:2209.01003 (2022), https://arxiv.org/abs/2209.01003, especially the generalized lattice Riesz inequality and rearrangement applications.

A later nearest-neighbor periodic-lattice rearrangement study (X. Liang, arXiv:2608.11986, August 2026) was identified at abstract level only; its operator is a first-order nearest-neighbor difference operator, not the squared movement operator treated here. It is a residual literature-access risk, not asserted to be excluded by full-text inspection.

The theorem is for symmetric cycles and an idealized next-generation invasion threshold. It does not predict the ultimate infection burden or peak of a closed SIR epidemic and makes no claim for arbitrary networks, unequal patch sizes, or arbitrary hotspot amplitudes across all cycle sizes.

Self-review: passed. Independent audit: not yet performed.
