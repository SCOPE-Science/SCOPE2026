# Mathematical review

## Correctness

**PASS.** The conclusion concerns independent sampling with replacement, strictly positive probabilities, and the first instant of full coverage for any integer number of types \(N\ge2\). Poisson thinning preserves the discrete label sequence exactly. Conditioning on the unique last first arrival gives exact, mutually exclusive events for one versus two singleton types. Since \(F_i'(t)=p_i^2t e^{-p_it}\), integration by parts converts each one-singleton term into an ordered sum of two-singleton terms; symmetrization gives a kernel multiplied by \((p_i-p_j)^2\). All boundary terms vanish and every kernel is integrable and strictly positive, including the empty-product two-type case. This proves both inequality and equality case without a finite-size extrapolation. Separately, 522 exact-rational checker assertions compare independent finite-state and integral-expansion computations on sizes two through six.

## Originality

**PASS against inspected sources, with historical-priority limitations.** The 2003 uniform-singleton formula of Myers–Wilf includes the special case where the two probabilities are equal; that equality is expressly not claimed to be new. Adler–Oren–Ross and Doumas–Papanicolaou primarily derive expectations and bounds for the nonuniform siblings model; Doumas–Spektor establish extremality of **expected** missing types. Long's 2026 full generating-function identity determines the probabilities in principle, but the accompanying radial transform and binomial-moment inequalities do not imply the asserted order of two **consecutive atoms for each fixed nonuniform sampling vector**. The positivity and exact pairwise-square expression require the separate comparison proved here. Two published finite-type results establish comparison with uniform sampling for three or four types, not an all-size inequality internal to a single distribution. A published conditional likelihood-ratio result orders singleton counts across completion times, not their unconditional first two masses. These result texts and the closest primary papers were inspected. An older unindexed equivalent identity remains a priority risk.

## Value

**PASS.** The sign of the difference between the first two singleton-count probabilities is a natural question about the first sibling's residual missing types, rather than a selected arbitrary coefficient. It gives an exact if-and-only-if characterization of uniform coupon weights for *every* finite alphabet size, a positive pairwise quadratic heterogeneity decomposition, and thus a direct finite-sample structural fact not supplied by expectation or probability-generating-function extremality. The specific fact is meaningful independently of a broader stochastic-order classification: no such classification or universal mode theorem is claimed. The higher-sibling two-type example demonstrates a genuine boundary of applicability.

## Closest literature and limitations

Myers and Wilf (2003), Section 4, https://arxiv.org/abs/math/0304229; Adler, Oren and Ross (2003), Section 3, https://oren.ieor.berkeley.edu/pubs/coupon.pdf; Doumas and Spektor (2026), https://arxiv.org/abs/2606.21591; Long (2026), Proposition 2.1 and Remark 1.2, https://arxiv.org/abs/2606.31391. Full accessible published comparisons include all-type conditional likelihood-ratio ordering and three- and four-type stochastic-order claims. The new result does not cover higher siblings or prove stronger stochastic orders; independent historical-priority and mathematical assessments have not been performed. The checker tests finite rational examples, not the continuum.

Self-review: passed. Independent audit: not yet performed.
