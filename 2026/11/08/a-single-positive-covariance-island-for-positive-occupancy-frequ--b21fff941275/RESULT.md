# A single positive covariance island for positive occupancy frequencies in uniform weak compositions

## Finding
For integers \(m\ge3\) and \(N\ge2\), choose \((Y_1,\ldots,Y_m)\) uniformly among the \(\binom{N+m-1}{m-1}\) weak compositions of \(N\). Let \(X_j=\#\{i:Y_i=j\}\). Fix a **positive** size \(1\le a\le N\). For the other positive size \(b\in\{1,\ldots,N\}\setminus\{a\}\), define
\[
 p_j=\frac{\binom{N-j+m-2}{m-2}}{\binom{N+m-1}{m-1}},\qquad
 q_a(L)=\begin{cases}\dfrac{\binom{L-a+m-3}{m-3}}{\binom{L+m-2}{m-2}},&L\ge a,\\0,&L<a.\end{cases}
\]
Then the exact covariance is
\[
 \operatorname{Cov}(X_a,X_b)=m(m-1)p_b\left[q_a(N-b)-\frac{m}{m-1}p_a\right]. \tag{1}
\]
In particular, the positive superlevel set of the bracket in (1), formally evaluated at all positive integers \(b\) including the otherwise excluded diagonal, is an integer interval (possibly empty). For actual cross-covariances, positive values occur at the intersection of that interval with \(\{1,\ldots,N\}\setminus\{a\}\). Thus the correlation sign has at most one positive island as the comparison part size increases, with zero values possible at its edges; the excluded diagonal is not a cross-covariance.

This is a genuinely non-monotone possibility. With \(m=4\), \(N=12\), and \(a=2\), the covariances are strictly negative for \(b\in\{1,3,4,5,6,7,10,11,12\}\), and strictly positive precisely at \(b=8,9\). Four adjacent values are
\[
 \operatorname{Cov}(X_2,X_7)=-\frac{48}{29575},\quad
 \operatorname{Cov}(X_2,X_8)=\frac{108}{41405},\quad
 \operatorname{Cov}(X_2,X_9)=\frac{72}{41405},\quad
 \operatorname{Cov}(X_2,X_{10})=-\frac{876}{207025}.
\]
The result concerns **positive versus positive** size counts. Vacancy-count comparisons are not asserted as a new result.

## Assumptions and scope
The sample is uniform across ordered nonnegative allocations, not uniform across allocations of distinguishable balls. It is also the symmetric Dirichlet–multinomial distribution with every concentration parameter equal to one. The theorem holds for all finite integer \(m\ge3\), \(N\ge2\), \(1\le a\le N\), and \(b\in\{1,\ldots,N\}\setminus\{a\}\). Binomial coefficients with impossible combinatorial parameters are defined as zero. Every marginal \(p_b\) in this domain is strictly positive, so (1) preserves the sign of the bracket. No claim is made for other concentration parameters, random composition lengths, or the diagonal \(b=a\).

## Proof
There are exactly \(D=\binom{N+m-1}{m-1}\) equally likely allocations. Fixing the first coordinate at \(j\) leaves \(\binom{N-j+m-2}{m-2}\) possibilities, so \(\Pr(Y_1=j)=p_j\). Fixing two distinct coordinates to \(a,b\) leaves \(\binom{N-a-b+m-3}{m-3}\) possibilities. Hence, for \(a\ne b\),
\[
 \mathbb E[X_aX_b]=m(m-1)\Pr(Y_1=a,Y_2=b)
 \quad\text{and}\quad
 \mathbb E[X_j]=mp_j.
\]
Given \(Y_2=b\), the other \(m-1\) coordinates form a uniform weak composition of \(N-b\); consequently \(\Pr(Y_1=a\mid Y_2=b)=q_a(N-b)\). Subtracting \(m^2p_ap_b\) gives (1), including \(a+b>N\), where the joint count is zero.

For every integer \(L\ge a\), direct cancellation gives
\[
 \frac{q_a(L+1)}{q_a(L)}=
 \frac{(L-a+m-2)(L+1)}{(L-a+1)(L+m-1)}.
\]
Both factors in the denominator are positive. The numerator minus the denominator is exactly
\[
 a(m-2)-L-1.
\]
Thus, over \(L\ge a\), the sequence \(q_a(L)\) first increases, possibly has a two-point plateau, then strictly decreases; if the turning point precedes \(a\), it decreases from its first defined value. The preceding \(L<a\) values are zero, so the entire \(L=0,\ldots,N\) sequence is unimodal. The positive superlevel set of any unimodal nonnegative finite sequence at a fixed threshold is an integer interval. Reversal \(L=N-b\) preserves interval structure. Taking the threshold \(\frac{m}{m-1}p_a>0\) from (1) proves the claimed positive-island law.

For the \(m=4,N=12,a=2\) example, substituting into the same exact binomial ratios produces the displayed four fractions, and the remaining distinct positive indices have negative brackets. The two positive values occur near the two-point mode \(L=3,4\) of \(q_2(L)\) (corresponding to \(b=9,8\)). This completes the finite and all-parameter claims.

## Verification
The standalone standard-library Python script `check.py` checks the conditional sign identity, every possible superlevel interval for \(3\le m\le11\) and \(0\le N\le31\), exhaustive uniform enumeration for seven finite sample spaces including \(m=4,N=12\), and the four rational boundary fractions. It also checks the familiar vacancy boundary as a regression check, **not as an originality claim**. In total, 114,429 exact assertions pass. Computations corroborate but do not replace the ratio proof, which handles every finite \(m,N\) in scope.

## Relationship to prior work
Bender and Canfield (2005) explicitly give a multivariate part-size marking generating function for unrestricted positive compositions. Their framework implies access to the unprocessed finite moments (after conditioning on fixed length and shifting every part by one), but the inspected treatment does not establish the positive-frequency covariance sign interval or its reentrant example. Thus **equation (1) is a standard consequence of stars and bars and is not claimed as intrinsically new**; the claimed contribution is the all-parameter qualitative sign theorem and a genuine negative–positive–negative frequency profile. Bender, Canfield and Gao (2012) study large-part asymptotics of variable-length locally restricted positive compositions, a different regime. Barbour and Gnedin (2008) study small occupancy frequencies in the classical independent-ball, infinite-box model, not uniform fixed-mass weak compositions. Exact vacancy-frequency comparisons and their consequences are outside the novelty claim.

## Limitations
The complete distribution and the marginal and joint factorial moments follow from classical occupancy generating functions; this theorem analyzes only a sharply specified sign structure. The positive interval may be empty, degenerate, or interrupted solely by the excluded diagonal. Its endpoints are determined by explicit rational binomial inequalities rather than a universal closed elementary formula. No independent priority validation has been performed; older unlocated joint-occupancy generating-function papers could contain the sign theorem implicitly. The finite verifier cannot establish historical originality or replace the analytic proof.

## References
- E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12(1), R57 (published 2005-11-07), https://doi.org/10.37236/1954 . Specifically Example 1 and Section 3.5 on marked part sizes.
- E. A. Bender, E. R. Canfield and Z. Gao, *Locally Restricted Compositions IV. Nearly Free Large Parts and Gap-Freeness* (first public arXiv 2012-08-03), https://arxiv.org/abs/1208.0870 .
- A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme* (first public arXiv 2008-09-25), https://arxiv.org/abs/0809.4387 .
