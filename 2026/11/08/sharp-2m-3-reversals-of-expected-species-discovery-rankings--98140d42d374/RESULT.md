# Sharp \(2m-3\) reversals of expected species-discovery rankings

## Finding

For every integer \(m\ge2\), two finite communities with the same \(m\) strictly positive species probabilities can reverse their ranking by expected next-draw discovery probability **at most \(2m-3\) times** as sample size increases. The bound is attained by two rational-probability communities for every \(m\ge2\). More precisely, writing
\[
U_{\boldsymbol p}(t)=\sum_{i=1}^{m}p_i(1-p_i)^t,\qquad H(t)=U_{\boldsymbol p}(t)-U_{\boldsymbol q}(t),
\]
either \(H\equiv0\), or \(H\) has at most \(2m-3\) zeros, with multiplicities, on \(t>0\). For each \(m\), rational profiles and increasing *positive integers* \(n_1<\cdots<n_{2m-2}\) exist such that the signs of \(H(n_j)\) alternate, realizing exactly \(2m-3\) strict ranking reversals. These claims concern discovery rates, **not** crossings of cumulative expected species-richness curves.

For three species an exact witness is
\[
\boldsymbol p=(1,7,22)/30,\qquad \boldsymbol q=(2,10,18)/30.
\]
The sign of \(H(n)\) is that of
\[
29^n+7\cdot23^n+22\cdot8^n-2\cdot28^n-10\cdot20^n-18\cdot12^n.
\]
The signs at \(n=6,7,12,13,15,16\) are respectively \(-,+,+,-,-,+\), hence three strict reversals. There are exactly three sign-changing gaps in these observations, \((6,7),(12,13),(15,16)\). The general upper bound certifies that there are no further crossings for this witness.

## Assumptions and scope

Each community has exactly \(m\) species with probabilities \(p_i>0\), \(\sum_i p_i=1\); respectively \(q_i>0\), \(\sum_i q_i=1\). Draws are independent with replacement, and a species is observed if and only if sampled. If \(D_{n+1}\) is the indicator that draw \(n+1\) belongs to a species unseen in the first \(n\) draws, then \(\Pr(D_{n+1}=1)=U_{\boldsymbol p}(n)\). The real extension \(t\ge0\) is only a mathematical interpolation. A strict reversal is a change of strict sign between increasing integer sample sizes; a tie is not a strict reversal. The bound counts *all* positive real zeros with multiplicities, so it also bounds strict ranking reversals.

## Proof

**1. Expected discovery rate.** By disjointness of the species that might appear at draw \(n+1\), the event that species \(i\) is drawn then but was absent on the first \(n\) draws has probability \(p_i(1-p_i)^n\). Summing gives the displayed expression.

**2. Exponential-polynomial zero bound.** We use the following generalized Descartes rule: if \(0<b_1<\cdots<b_s\) and all real coefficients \(c_j\ne0\), the number of real zeros, with multiplicity, of \(f(t)=\sum_{j=1}^s c_jb_j^t\), counted over the entire real axis, is at most the number of sign changes in \((c_1,\ldots,c_s)\). To see this, put \(x=e^t>0\), write \(f=\sum_jc_jx^{\lambda_j}\) with strictly increasing \(\lambda_j=\log b_j\), divide by \(x^{\lambda_1}\), and differentiate. The derivative is a generalized polynomial with the coefficients \(c_j(\lambda_j-\lambda_1)\) for \(j\ge2\). If \(c_1,c_2\) have opposite signs, Rolle's theorem gives at most one more zero than the derivative; if they have the same sign, \(f/x^{\lambda_1}\) begins with the sign of \(c_1\) at \(x\downarrow0\), whereas its derivative begins with the same sign, forcing an additional derivative zero before the first zero of the function. The derivative bound therefore subtracts precisely the initial sign variation in either case; repeated roots are handled with their multiplicities. Induction proves the rule. (Equivalently one may invoke the standard generalized Descartes rule for real powers.)

In the present application, collect identical bases in the difference \(H\) and discard zero coefficients. There are at most \(2m\) distinct bases, each coefficient having the sign of the profile from which it came. If fewer than \(2m\) remain, the coefficient sequence has at most \(2m-2\) sign changes. If all \(2m\) bases are distinct, having \(2m-1\) sign changes would force perfect alternation between the \(m\) probabilities of \(\boldsymbol p\) and the \(m\) probabilities of \(\boldsymbol q\) in decreasing probability order. Such alternation would give either \(p_{(j)}>q_{(j)}\) for every ordered coordinate \(j\), or the opposite inequality for every \(j\). Both contradict \(\sum p_i=\sum q_i=1\). Therefore \(H\) has at most \(2m-2\) real zeros (with multiplicities). Because \(H(0)=1-1=0\), at most \(2m-3\) zeros occur in \(t>0\). If all coefficients cancel, \(H\equiv0\) and no strict reversal is possible.

**3. A rational two-species start.** At \(m=2\) take \(\boldsymbol p=(1,9)/10\) and \(\boldsymbol q=(2,8)/10\). Direct integer powers give \(H(5)<0\) and \(H(6)>0\); this attains the bound \(1=2m-3\).

**4. Induction constructing two additional reversals.** Suppose rational positive profiles \(\boldsymbol p,\boldsymbol q\) of length \(m\) have strictly alternating nonzero signs at \(2m-2\) increasing positive integer arguments, the last being positive (the base case has this property). For a sufficiently small positive **rational** \(b\), set \(a=b^2\) and form
\[
\boldsymbol p'=((1-a)p_1,\ldots,(1-a)p_m,a),\quad
\boldsymbol q'=((1-b)q_1,\ldots,(1-b)q_m,b).
\]
All probabilities remain positive and each profile sums to one. At each of the finitely many old integer arguments, the new difference tends to the old difference as \(b\downarrow0\), preserving all strict signs. Let \(N_b=\lceil1/b\rceil\), chosen beyond the last old argument. Since all old probabilities are bounded below by a fixed positive constant, their total contribution to \(H'(N_b)\) is \(O(e^{-c/b})\) for some \(c>0\). The new positive-species term is at most \(a=b^2\), while the negative term is \(-b(1-b)^{N_b}\), whose magnitude is asymptotic to \(b/e\). Thus \(H'(N_b)<0\) for all sufficiently small rational \(b>0\). Finally, for this fixed \(b\), the new probability \(a=b^2\) is strictly smaller than \(b\) and every old (slightly rescaled) probability; hence \(a(1-a)^L\) is the unique slowest-decaying term and makes \(H'(L)>0\) for some integer \(L>N_b\). Two further strict sign changes have been appended, producing \(2(m+1)-3\) reversals. The upper bound proves there can be no additional zeros. In fact every positive zero for these witnesses is simple, because the \(2m-3\) witnessed sign-changing intervals each require an odd-multiplicity zero and the upper bound counts multiplicity.

## Verification

Run `python3 artifacts/check_coverage_crossings.py` from the package root using Python 3 (standard library only). Exact integer calculations confirm the two-, three-, and four-species witnesses have respectively one, three, and five alternating reversals at specified integer sample sizes. Independent state enumeration checks the next-draw discovery formula at sample sizes 0 through 4 for two profiles. The checker also verifies a rational instance of the induction with \(b=1/200\). These finite checks supplement, but do not replace, the arbitrary-\(m\) analytic zero bound and induction. For the four-species witness the profiles are \((484,426,81,9)/1000\) and \((272,58,665,5)/1000\), with alternating transitions between sample sizes \((4,5),(14,15),(19,20),(47,48),(144,145)\).

## Relationship to prior work

The expected discovery probability/coverage deficit \(\sum_i p_i(1-p_i)^n\) is standard in species sampling (Good and Toulmin 1956). Chao and Jost (2012, including Appendix H) compare coverage-based and richness-based rarefaction, while Chao, Wang and Jost (2013) describe the derivative of the species-accumulation curve using discovery rates. Lande, DeVries and Walla (2000) analyze crossings of *cumulative richness* curves. The previously studied relationship between the stochastic indicators of two **successive** discoveries concerns covariance within a single profile; it does not compare two distinct profiles' expected discovery rates. None of these inspected claims implies the present sharp \(2m-3\) bound and rational construction. An already known sharp threshold for **cumulative richness** ranking reversals is a different invariant: differentiating a difference of cumulative curves does not preserve its number of crossings. The present result does not claim that discovery rates, coverage deficits, or the underlying generalized-Descartes lemma were previously unknown.

## Limitations

The result assumes finite equal-size species supports, iid draws, constant species probabilities, and perfect detection. It counts comparisons at common sample size, not comparisons standardized by sample coverage. Ties are excluded from strict reversals. The analytic bound is independent of samples but does not quantify the smallest sample sizes needed to realize the construction; the inductive profiles may be extremely uneven. Historical priority of the exact sharp bound remains provisional; older literature under terms such as occupancy, exponential sums, and discovery-probability crossings may contain related theorems. Independent external assessment has not been performed.

## References

1. Lande, R., DeVries, P. J., and Walla, T. R. (2000). *When species accumulation curves intersect: implications for ranking diversity using small samples*. Oikos. https://doi.org/10.1034/j.1600-0706.2000.890320.x
2. Chao, A., and Jost, L. (2012). *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*. Ecology. https://doi.org/10.1890/11-1952.1 ; supplementary Appendix H: https://esapubs.org/archive/ecol/E093/238/appendix-H.pdf
3. Chao, A., Wang, Y. T., and Jost, L. (2013). *Entropy and the species accumulation curve: a novel entropy estimator via discovery rates of new species*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.12108
4. Good, I. J., and Toulmin, G. H. (1956). *The number of new species, and the increase in population coverage, when a sample is increased*. Biometrika. https://doi.org/10.1093/biomet/43.1-2.45
