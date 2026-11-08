# Scientific review: finite-step Luce fixed points

## Correctness — PASS

The full claim fixes the draw-rank convention, finitely many positive class rates, consecutive label blocks and positive limiting proportions. Independent exponential clocks generate the Luce order. Conditional on the class word, labels in each class are uniformly and independently matched to their occupied draw slots; this yields the exact joint factorial identity (1). Empirical exponential-clock distribution functions and fixed-quantile convergence show the eligible-slot fractions converge to the stated exponential interval masses. The factorial moments are bounded uniformly and imply the independent Poisson generating function; discreteness upgrades convergence to total variation. Integration of the known permuton density verifies the diagonal formula. The two-class derivative was independently derived. The embedded `VERIFY.py` exact-rational finite enumeration passes, but does not substitute for the proof. Residual correctness risk: the argument depends on fixed positive rates/proportions, not arbitrary triangular arrays.

## Originality — PASS (provisional)

Borga–Chatterjee–Diaconis, arXiv:2509.07729v3, Section 5.2, explicitly leave the fixed-point limiting law open and conjecture the Poisson diagonal-density law. Their Theorem 2.1 and Proposition 2.2 determine only macroscopic permuton limits and density, which cannot by themselves imply this rare-point law. Chatterjee–Diaconis–Kim (arXiv:2306.16521v1, Sections 1 and 2.2) and Clay (arXiv:2603.09008v2, Section 8) also explicitly identify Luce fixed points as unresolved. Fulman (arXiv:2406.12139v2) proves Poisson laws for conjugation-invariant non-Luce mechanisms. The new finite-step class law and independent colored counts are not logical corollaries of those inspected results. Semantic research-record searches for the Luce/fixed-point Poisson law showed closest matches for uniform-permutation covariances and unrelated permutation problems rather than this theorem. Existing special-case priority remains a residual risk; no exhaustive uniqueness assertion is made.

## Mathematical value — PASS

The result resolves a precisely stated special case of a published open question about the Luce stationary distribution of the Tsetlin library. It converts a non-continuous microscopic statistic into explicit asymptotic Poisson parameters and establishes joint independence across classes, rather than only a formal diagonal-density heuristic. The two-block formula shows directional bias can make the expected number of fixed points either smaller or larger than the uniform-permutation value. The restrictions to finitely many macroscopic classes are natural because the conditional exchangeability decomposition is exact there. The work does not claim a general-profile theorem or a finite-sample error estimate.

## Sources and remaining risks

Primary accessible HTML inspected in the relevant sections: https://arxiv.org/html/2509.07729v3 (model, permuton density, Section 5.2), https://arxiv.org/html/2306.16521v1 (Luce background/open questions), https://arxiv.org/html/2603.09008v2 (Section 8), https://arxiv.org/html/2406.12139v2 (different conjugation-invariant mechanisms). Remaining risks are an unindexed finite-step fixed-point precedent and the absence of independent external proof review.

Self-review: passed. Independent audit: not yet performed.
