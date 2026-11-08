# Distribution-free failure law and critical window for two-alternative stakeholder lotteries

## Finding
Let \(V_n\) be the least number of rejecting stakeholders over all lotteries on two alternatives under the random acceptance model in the next section. Put \(q=1-p\). For every integer \(k\geq1\), its exact upper tail is
\[
\Pr(V_n\geq k)=\sum_{u=k}^{n-k}\left[\binom{n}{u}-\binom{n}{k-1}\right]p^u q^{n-u},
\]
where an empty sum is zero. In particular,
\[
\Pr(V_n=0)=\sum_{u=0}^n p^u q^{n-u}=\begin{cases}(p^{n+1}-q^{n+1})/(p-q),&p\ne q,\\(n+1)2^{-n},&p=q=1/2.\end{cases}
\]
Both laws are independent of the common continuous threshold distribution. The optimal rejection count has a sharp three-regime limit. For fixed \(p\ne1/2\),
\[
\mathbb E[V_n]=n\min(p,q)-\frac{\min(p,q)}{|p-q|}+o(1),\qquad
\frac{V_n-n\min(p,q)}{\sqrt n}\Longrightarrow N(0,pq).
\]
At \(p=1/2\),
\[
\mathbb E[V_n]=\frac n2-\sqrt{\frac{2n}{\pi}}+\frac12+o(1),\quad
\frac{V_n-n/2}{\sqrt n}\Longrightarrow\frac{B(1)}2-\sup_{0\leq t\leq1}B(t),
\]
where \(B\) is standard Brownian motion. More generally, if \(p_n=1/2+\theta/\sqrt n\) for fixed real \(\theta\) (and sufficiently large \(n\)), then
\[
\frac{V_n-n/2}{\sqrt n}\Longrightarrow\frac{B(1)+2\theta}{2}-\sup_{0\leq t\leq1}\bigl(B(t)+2\theta t\bigr).
\]

## Assumptions and scope
There are \(n\geq1\) independent stakeholders and two alternatives. A lottery assigns probability \(\lambda\in[0,1]\) to the first alternative. Each stakeholder independently favors the first alternative with probability \(p\in(0,1)\), and otherwise favors the second. A first-favoring stakeholder accepts exactly \(\lambda\geq T_i\); a second-favoring stakeholder accepts exactly \(\lambda\leq T_i\). The random cutpoints \(T_i\) are independent and identically distributed with one common atomless distribution supported on \((0,1)\), independent of all preference directions. All acceptance inequalities are weak. This is a subclass of normalized binary-utility halfspace acceptance: the original utility threshold of a second-favoring stakeholder is \(1-T_i\). There is no claim for asymmetric orientation-conditioned threshold laws, atoms, dependent stakeholders, or more than two alternatives.

## Proof
1. Almost surely the cutpoints are distinct. Arrange them increasingly and write \(X_j=1\) for a first-favoring stakeholder at position \(j\) and \(X_j=-1\) otherwise. The ordered signs are independent, with \(\Pr(X_j=1)=p\). Let \(U_n\) be the number of positive signs, \(S_j=\sum_{r=1}^jX_r\), \(S_0=0\), and \(M_n=\max_{0\leq j\leq n}S_j\). In a cell immediately after the first \(j\) thresholds, precisely the negative signs among these \(j\) and the positive signs among the remaining thresholds reject. This is \(U_n-S_j\). At an equality cutpoint one of these adjacent cell counts applies, because exactly one stakeholder is satisfied on both sides; no smaller count can arise there. Hence \(V_n=U_n-M_n\) almost surely. The threshold law has disappeared.
2. Condition on \(U_n=u\). All \(\binom nu\) sign words are equiprobable. The event \(V_n\geq k\) is \(M_n\leq u-k\). It is possible only for \(k\leq u\leq n-k\). Reflect a path at its first visit to the forbidden level \(u-k+1\), exchanging its subsequent up and down steps. The resulting unrestricted path ends at \(2(u-k+1)-(2u-n)=n-2k+2\), so the reflected word has exactly \(n-k+1\) positive signs, or equivalently \(k-1\) negative signs. This is a bijection, giving exactly \(\binom nu-\binom n{k-1}\) admissible sign words. Weighting by \(p^u q^{n-u}\) proves the upper-tail formula.
3. For zero violations, the word must be some initial block of positive signs followed by a block of negative signs. Indeed \(V_n=0\) forces \(M_n=U_n\), so every positive step precedes every negative step. For each \(u\), exactly one word has this form, of probability \(p^u q^{n-u}\); summing proves the feasibility formula. It also follows by subtracting the reflection tail for \(k=1\).
4. If \(p<1/2\), the positive-drift excursion maximum \(M_n\) is nondecreasing and converges almost surely and in mean to the finite supremum of a negative-drift random walk. The standard first-passage recurrence or optional stopping applied to the geometric harmonic function gives \(\Pr(M_\infty\geq a)=(p/q)^a\) for integers \(a\geq1\). Thus \(\mathbb E M_\infty=p/(q-p)\), and \(V_n=U_n-M_n\) gives the first fixed-bias expectation. If \(p>1/2\), reverse and negate the increments. Then \(M_n-S_n\) has the law of the maximum of a negative-drift walk with upward probability \(q\). Since \(V_n=(n-U_n)-(M_n-S_n)\), its expectation is \(nq-q/(p-q)+o(1)\). In both cases the correction is tight, so the ordinary binomial central limit theorem and Slutsky's lemma give the stated centered Gaussian limit.
5. At \(p=1/2\), the standard reflection principle implies \(\mathbb E M_n=\mathbb E|S_n|-\Pr(S_n>0)\), valid for all \(n\geq1\). The symmetric binomial identity \(\mathbb E|S_n|=n\binom{n-1}{\lfloor(n-1)/2\rfloor}2^{-(n-1)}\), together with Stirling's formula and \(\Pr(S_n>0)\to1/2\), establishes the displayed expectation. Donsker's invariance principle and the continuity of the supremum under uniform convergence give the Brownian limit because \(U_n=(n+S_n)/2\). The same triangular-array invariance principle for \(p_n=1/2+\theta/\sqrt n\), with drift \(2\theta t\) and asymptotic unit variance, proves the critical-window limit.

## Verification
The standalone standard-library script `verify.py` exhaustively traverses all \(131070\) sign words of lengths \(1\) through \(16\), independently minimizes the number of rejections over all cells, and compares all conditional binomial reflection counts (\(932\) parameter checks). It additionally tests the exact rational feasibility law and the biased upper-tail probabilities with \(p\in\{1/4,2/5,1/2,3/4\}\), including \(140\) separate rational tail checks. All tests passed. Reproduce with `python3 verify.py`. These finite checks support the algebra but do not establish the asymptotic claims, which are proved above.

## Relationship to prior work
Teh and Goldberg (2026), Appendix E.1 Proposition E.1, identify the interval-overlap representation for two alternatives and give a deterministic \(O(n\log n)\) optimizer for an arbitrary fixed profile. Choo, Goldberg and Teh (2026) develop query procedures for unanimously feasible lotteries. Neither inspected source gives the exact random-threshold rejection distribution, the distribution-free feasibility law, or the fixed-bias/critical-window stochastic transitions under the assumptions above. The reflection principle, binomial limit theorem and Donsker invariance principle are classical and are not claimed as new; the contribution is their exact application to the motivated social-choice invariant and its random-threshold phase structure.

## Limitations
The claim relies essentially on independent orientations and common continuous effective cutpoints. Atoms can produce simultaneous boundary events, invalidating the simple one-at-a-time walk count; unequal conditional threshold laws remove exchangeability of the sorted orientations. No statement of universal novelty or independent verification is made. Published work not indexed in the targeted searches may contain an equivalent stochastic formulation.

## References
1. N. Teh and P. W. Goldberg, *Learning Lotteries with Minimal Stakeholder Violations from Membership Queries*, arXiv:2610.37828v1, first public 2026-10-27. https://arxiv.org/abs/2610.37828 (Section 4.3; Appendix E.1, Proposition E.1).
2. D. Choo, P. W. Goldberg and N. Teh, *Learning Unanimously Acceptable Lotteries via Queries*, arXiv:2604.17505v1, first public 2026-04-19. https://arxiv.org/abs/2604.17505.
3. Classical results used: random-walk reflection principle, biased gambler's-ruin hitting probabilities, the binomial central limit theorem, Stirling's approximation, and Donsker's invariance principle.
