# Scientific assessment

## Correctness — PASS

The literal AWVC blocking definition for a three-alternative top-choice-approval election is equivalent to four integer inequalities: total disapprovers, last-place disapprovers, and the two groups preferring each rival to the candidate. The proof reduces all possible coalitional preference intersections to these cases and establishes that two simultaneous survivors are impossible. Uniform rankings yield a four-class multinomial law with weights \((1/3,1/3,1/6,1/6)\). A normalized likelihood-ratio bound and an explicit attainable type prove the exact large-deviation rate for all voter counts. The exact subsequence prefactor follows from a multinomial change of measure, a summable lattice cone, a verified geometric-series evaluation \(14904/121\), and Stirling's formula. No numerical experiment is used as an infinite proof. The standalone checker exhaustively compared 5,004 anonymous strict-ranking histograms through nine voters and checked finite probabilities and the rational constant.

## Originality — PASS, with residual risks

The directly relevant source is Dong et al., *Where Should Society Draw the Line?* (arXiv:2609.10759v1), specifically Definition 8 (AWVC), Theorem 4 (its majority-approval and veto guarantees), and the synthetic-data study. Those results introduce the general solution concept and experiment with it, whereas the current claim establishes the exact three-alternative nonemptiness law and a sharp lattice large-deviation prefactor under uniform top-one preferences. Their general majority condition is only a necessary condition here: the exact rate \(\log(27/16)/6\) is stronger than the majority-only binomial rate \(\log(9/8)/2\). Ianovski and Kondratev, *Computing the Proportional Veto Core* (arXiv:2003.09153), study the expected size of a different, approval-free veto core. No directly covering statement was identified in the accessible literature or claim searches. The primary document was materially inspected at its relevant definition, theorem, algorithm and empirical discussion; not every appendix was read end-to-end. The older source's complete text and potentially unindexed equivalent results remain material originality risks; an independent audit has not been conducted.

## Mathematical value — PASS

A consent procedure is useful only insofar as it can produce defensible options, making its probability of returning an empty set a natural operational question. The exact three-alternative impartial-culture model is the smallest nontrivial ordinal culture with both last-place and two distinct middle-place coalitional veto patterns. The theorem proves structural uniqueness of consent under top-choice approval, delivers exact finite probabilities, and separates the full core's exponentially small survival probability from the weaker majority-only benchmark. The explicit rational \(n^{-3/2}\) prefactor captures a genuine three-constraint lattice boundary rather than an arbitrary finite census. It does not claim broader preference models or strategic truthfulness.

## Closest literature and limitations

Primary: C. Dong et al., arXiv:2609.10759v1 (September 9, 2026), https://arxiv.org/abs/2609.10759. Secondary: E. Ianovski and A. Y. Kondratev, arXiv:2003.09153, https://arxiv.org/abs/2003.09153. Other residue classes share the logarithmic rate but are not claimed to share one leading constant. The older proportional-veto paper's expected-size result is not a result about the AWVC rule defined in 2026; nonetheless a stronger reduction from that paper remains a residual check for subsequent independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
