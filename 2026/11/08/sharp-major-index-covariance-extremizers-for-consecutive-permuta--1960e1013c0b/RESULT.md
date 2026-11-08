# Sharp major-index covariance extremizers for consecutive permutation patterns

## Finding
Let \(\Pi\) be a uniform random permutation of \([n]\). For every pair of integers \(n\ge m\ge2\), and every pattern \(\sigma=(\sigma_1,\ldots,\sigma_m)\in S_m\), write
\[
M=\sum_{j=1}^{n-1}j\mathbf1\{\Pi_j>\Pi_{j+1}\},\qquad
T_\sigma=\sum_{i=1}^{n-m+1}\mathbf1\{\operatorname{std}(\Pi_i,\ldots,\Pi_{i+m-1})=\sigma\}.
\]
Then, setting \(N=n-m+1\),
\[
-\mathcal B_{n,m}\le\operatorname{Cov}(M,T_\sigma)\le\mathcal B_{n,m},
\qquad
\mathcal B_{n,m}=\frac{(m-1)n[N(m-1)+2]}{4(m+1)m!}.
\]
The upper equality holds **only** for the decreasing pattern \((m,m-1,\ldots,1)\), and the lower equality **only** for the increasing pattern \((1,2,\ldots,m)\). The result is an all-sample-size comparison across all \(m!\) patterns, not a large-sample or pattern-avoidance statement.

There is also an exact pattern-resolved formula. Put
\[
W_j=\frac{N(N+2j-1)}2\quad(1\le j<m),\qquad
A=\frac{N(N-1)}2,\qquad
B=(N-1)\left(\frac N2+m-1\right).
\]
For \(d_j=\mathbf1\{\sigma_j>\sigma_{j+1}\}\), one has
\[
\boxed{m!\operatorname{Cov}(M,T_\sigma)
=\sum_{j=1}^{m-1}W_j\left(d_j-\frac12\right)
+\frac{A(m+1-2\sigma_1)+B(2\sigma_m-m-1)}{2(m+1)}.}
\]
Thus the covariance depends only on the descent positions and the two endpoint ranks. For instance, with \(n=6,m=3\), the patterns \((1,3,2)\) and \((2,3,1)\) each have one descent, but their covariances are respectively \(7/12\) and \(-1/6\).

## Assumptions and scope
The random permutation is exactly uniform on \(S_n\), and every consecutive window is counted, including overlaps. The major index weights descent position \(j\) by \(j\), starting at 1. All statements hold for finite integers \(n\ge m\ge2\), with no asymptotic hypotheses. The symbols \(A,B,W_j\) in the statement are deterministic functions of \(n,m,j\) and are nonnegative.

## Proof
**Step 1: condition on a specified window.** Let \(E_i\) be the event that positions \(i,\ldots,i+m-1\) have relative order \(\sigma\). Its probability is \(1/m!\). Conditional on \(E_i\), the \(m-1\) internal descents are the fixed indicators \(d_j\); every descent strictly outside the window and not touching it retains probability \(1/2\), by permutation symmetry. If \(i>1\), the left boundary descent at \(i-1\) has probability \((m+1-\sigma_1)/(m+1)\), because the outside entry occupies an equiprobable rank among \(m+1\) entries. If \(i+m-1<n\), the right boundary descent at \(i+m-1\) has probability \(\sigma_m/(m+1)\). The unconditional descent probability at every position is \(1/2\). Consequently,
\[
\begin{split}
\mathbb E[M\mid E_i]-\mathbb EM
={}&\sum_{j=1}^{m-1}(i+j-1)\left(d_j-\frac12\right)\\
&+\mathbf1\{i>1\}(i-1)\frac{m+1-2\sigma_1}{2(m+1)}\\
&+\mathbf1\{i<N\}(i+m-1)\frac{2\sigma_m-m-1}{2(m+1)}.
\end{split}
\]
Because \(\operatorname{Cov}(M,\mathbf1_{E_i})=\Pr(E_i)(\mathbb E[M\mid E_i]-\mathbb EM)\), summing over \(i=1,\ldots,N\) and evaluating the three arithmetic sums gives exactly the boxed kernel in the finding.

**Step 2: compare with the decreasing pattern.** Let \(\rho=(m,m-1,\ldots,1)\) and let \(\mathcal A=\{j: \sigma_j<\sigma_{j+1}\}\) be the set of ascent positions of \(\sigma\). Subtracting the two kernels gives
\[
m!\bigl[\operatorname{Cov}(M,T_\rho)-\operatorname{Cov}(M,T_\sigma)\bigr]
=\sum_{j\in\mathcal A}W_j-
\frac{A(m-\sigma_1)+B(\sigma_m-1)}{m+1}.
\]
If \(\mathcal A\) is empty then \(\sigma=\rho\). Otherwise let \(a\) and \(b\) be the earliest and latest ascent positions. The values up to position \(a\) strictly decrease from \(\sigma_1\), so all \(m-\sigma_1\) values larger than \(\sigma_1\) lie among the final \(m-a\) positions. Similarly, the values from position \(b+1\) to the end strictly decrease to \(\sigma_m\), so all \(\sigma_m-1\) values smaller than \(\sigma_m\) lie among the first \(b\) positions. Therefore
\[
m-\sigma_1\le m-a\le\sum_{j\in\mathcal A}(m-j),\qquad
\sigma_m-1\le b\le\sum_{j\in\mathcal A}j.
\]
Using \(A,B\ge0\) we obtain
\[
\begin{split}
m!\bigl[\operatorname{Cov}(M,T_\rho)-\operatorname{Cov}(M,T_\sigma)\bigr]
&\ge\frac1{m+1}\sum_{j\in\mathcal A}\bigl[(m+1)W_j-A(m-j)-Bj\bigr]\\
&=\frac1{m+1}\sum_{j\in\mathcal A}\left[\frac{N(N-1)}2+j(2N+m-1)\right]>0.
\end{split}
\]
The final inequality follows from \(N\ge1\), \(m\ge2\), \(j\ge1\). Hence \(\rho\) is the unique maximizer.

**Step 3: evaluate the maximum.** Substitute \(d_j=1\), \(\sigma_1=m\), \(\sigma_m=1\) in the exact kernel and simplify:
\[
m!\operatorname{Cov}(M,T_\rho)=\frac{(m-1)n[N(m-1)+2]}{4(m+1)}.
\]
This is the stated bound. Complementing every entry, \(\Pi_j\mapsto n+1-\Pi_j\), maps \(M\) to \(n(n-1)/2-M\) and maps pattern occurrences \(T_\sigma\) to \(T_{\sigma^c}\), where \(\sigma^c_j=m+1-\sigma_j\). Thus \(\operatorname{Cov}(M,T_{\sigma^c})=-\operatorname{Cov}(M,T_\sigma)\). Since complementation exchanges decreasing and increasing patterns, the unique minimum is the increasing pattern with the negative of the maximal covariance. This completes the proof.

## Verification
Run `python3 check.py` in the directory containing this document. The self-contained Python 3 checker computes rational covariances independently by enumerating all permutations for \(2\le n\le7\) and compares them with the derived formula for every \(2\le m\le n\) and each \(\sigma\in S_m\). It checks the unique upper and lower equality cases, the earliest/latest ascent inequalities for all patterns of length at most eight, and the positive-coefficient identity over a larger parameter grid. The package's run returned **PASS 128362 exact assertions**. These finite tests are corroboration; the proof above establishes all integer parameters.

## Relationship to prior work
Elizalde's survey (arXiv:1504.07265, especially Sections 4.3 and 5.2) reviews consecutive-pattern enumeration, statistic-refined avoidance generating functions, and extremal *avoidance probabilities*. Its most-avoided-pattern comparison is distinct from an extremum of covariance with major index. Janson, Nakamura and Zeilberger (arXiv:1312.3955) study joint moments and normal approximations for classical subsequence-pattern counts, not the claimed all-length consecutive-pattern/major-index ordering. Opler (arXiv:1505.07135) studies major-index distributions within classical pattern-avoiding classes. Zhuang (arXiv:2108.10309, Section 4.2) develops inverse-major-index refinements for specific consecutive patterns; inverse major index is not the ordinary major index of the displayed claim, and the cited section concerns selected patterns rather than an all-pattern sharp covariance comparison. These broad methods may make some first moments computable, but no directly equivalent finite-parameter extremizer theorem was identified in the inspected material.

## Limitations
The result concerns only the first mixed moment (covariance) under the *uniform* permutation law; it does not assert a stochastic ordering, a comparison of avoidance probabilities, joint distribution, or applicability to Mallows permutations. The theorem is mathematically proved here, but historical priority and implicit coverage by an unlocated generating-function specialization remain possible. It has not undergone an independent external audit.

## References
- S. Janson, B. Nakamura and D. Zeilberger, *On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns*, arXiv:1312.3955, first posted 2013-12-13, https://arxiv.org/abs/1312.3955.
- S. Elizalde, *A Survey of Consecutive Patterns in Permutations*, arXiv:1504.07265, first posted 2015-04-27, https://arxiv.org/abs/1504.07265.
- M. Opler, *Major Index Distribution over Permutation Classes*, arXiv:1505.07135, first posted 2015-05-26, https://arxiv.org/abs/1505.07135.
- Y. Zhuang, *A Lifting of the Goulden–Jackson Cluster Method to the Malvenuto–Reutenauer Algebra*, arXiv:2108.10309, first posted 2021-08-23, https://arxiv.org/abs/2108.10309.
