# A single covariance reversal for paired vacancies in a three-shore hard-core gas

## Finding
Let \(G_{n,k}\) be obtained from \(K_{n,n,n}\), with three named shores of size \(n\), by deleting all three cross-shore edges inside each of \(k\) pairwise disjoint aligned triples, where \(n\ge3\) and \(1\le k\le n\). Let a hard-core configuration \(I\) have probability proportional to \(z^{|I|}\), with \(z>0\), and let \(X_a,X_b\) be the occupation indicators of two vertices in the same deleted triple but different shores.

Write \(t=1+z\) and
\[
Z_{n,k}=3t^n-2+kz^2(3+z),\quad A_{n}=zt^{n-1}+z^2(2+z),\quad B=z^2t.
\]
Then
\[
\operatorname{Cov}(X_a,X_b)=\frac{B Z_{n,k}-A_n^2}{Z_{n,k}^2}=\frac{z^2 F_{n,k}(z)}{Z_{n,k}^2},
\]
where
\[
F_{n,k}(z)=-t^{2n-2}+t^{n+1}+2t^{n-1}-2t-(t^2-1)^2+ktz^2(z+3).
\]
For \(n=3\), the covariance is strictly positive for every \(z>0\). For every \(n\ge4\), there is exactly one finite activity \(z_{n,k}>0\) at which it vanishes: the covariance is strictly positive for \(0<z<z_{n,k}\), zero at \(z_{n,k}\), and strictly negative for \(z>z_{n,k}\). The zero is simple.

With \(L=\log 2\), uniformly over all integer \(1\le k\le n\),
\[
z_{n,k}=\frac{L}{n}+\frac{2L+\frac12(1+3k/n)L^2}{n^2}+O(n^{-3}).
\]
For every fixed \(x>0\), again uniformly over \(1\le k\le n\),
\[
\lim_{n\to\infty}n^2\operatorname{Cov}_{z=x/n}(X_a,X_b)
=\frac{-x^2(e^x-1)(e^x-2)}{(3e^x-2)^2}.
\]
Thus the positive-to-negative crossover has universal leading scale \((\log2)/n\), while its next correction detects the density of deleted triples.

## Assumptions and scope
The graph is simple, labeled, and has exactly three independent shores. Deletion affects only the three cross-shore edges joining the corresponding vertices of each of \(k\) disjoint triples; other cross-shore edges remain present. Activities are common and strictly positive. The graph size \(n\) is an integer at least three, and \(k\) is an integer between one and \(n\). The assertion concerns one pair of distinct vertices from a single deleted triple, on different shores; no sign classification is asserted for other vertex-pair types or inhomogeneous fugacities. The crossover is a finite-size correlation zero, not a claimed thermodynamic phase transition.

## Proof
**Exact weighted enumeration.** An independent set either uses vertices from at most one shore, giving \(3(1+z)^n-2\), or uses vertices of at least two shores, in which case all its vertices lie in one deleted triple. Each deleted triple contributes three two-vertex choices and one three-vertex choice, giving the stated \(Z_{n,k}\). The weighted count containing \(a\) is \(A_n\): a single-shore contribution \(zt^{n-1}\), two cross-shore pairs, and the full triple. The weighted count containing both \(a,b\) is \(B=z^2+z^3\). The covariance identity and the stated formula for \(F_{n,k}\) follow by direct expansion.

**The exceptional size.** For \(n=3\), expansion gives
\[
F_{3,k}(z)=2z+(3k-2)z^2+4(k-1)z^3+(k-1)z^4,
\]
strictly positive for all \(z>0\) and \(1\le k\le3\).

**One zero for every larger size.** Write \(F_{n,k}(z)=\sum_{j\ge0}a_j z^j\), with missing binomial coefficients interpreted as zero. For \(n\ge4\), \(a_0=0\), \(a_1=n-1>0\), and
\[
\begin{aligned}
a_2&=\frac{6k-n^2+5n-10}{2},\\
a_3&=\frac{24k-5n^3+24n^2-31n-12}{6},\\
a_4&=\frac{24k-13n^4+90n^3-215n^2+210n-96}{24}.
\end{aligned}
\]
For \(n=4\), the ordered nonzero coefficient sequence is obtained from
\[
F_{4,k}(z)=3z+3(k-1)z^2+4(k-3)z^3+(k-11)z^4-5z^5-z^6.
\]
As \(1\le k\le4\), this sequence changes sign exactly once.

For \(n\ge5\) and \(k\le n\),
\[
a_3\le-\frac{(n-1)(5n^2-19n-12)}6<0,\qquad
a_4\le-\frac{(n-1)(13n^3-77n^2+138n-96)}{24}<0.
\]
For every \(j\ge5\), the fixed-degree terms in \(F_{n,k}\) vanish, hence
\[
a_j=-\binom{2n-2}{j}+\binom{n+1}{j}+2\binom{n-1}{j}.
\]
The ratios \(\binom{n+1}{j}/\binom{2n-2}{j}\) and \(\binom{n-1}{j}/\binom{2n-2}{j}\) are nonincreasing in \(j\), wherever their denominator is nonzero. At \(j=5\),
\[
a_5=-\frac{(n-3)(n-2)(n-1)(29n^2-111n+80)}{120}<0.
\]
Consequently all \(a_j<0\) for \(5\le j\le2n-2\). Thus, regardless of the sign of \(a_2\), coefficients of \(F_{n,k}/z\) have exactly one sign change for every \(n\ge5\). Descartes' rule of signs gives at most one positive root counted with multiplicity. Because \(F_{n,k}(z)=(n-1)z+O(z^2)>0\) near zero and its leading coefficient is \(-1\), it tends to negative infinity as \(z\to\infty\). Hence it has exactly one positive root, with multiplicity one, and the asserted signs follow.

**Universal scaling and its correction.** Uniformly for \(k/n\in[0,1]\) and \(x\) in a fixed compact set,
\[
F_{n,k}(x/n)=f_0(x)+n^{-1}f_1(x;k/n)+O(n^{-2}),
\]
where
\[
f_0(x)=-e^{2x}+3e^x-2=-(e^x-1)(e^x-2),
\]
\[
f_1(x;\rho)=e^{2x}(2x+x^2)-e^x(x+3x^2/2)-2x+3\rho x^2.
\]
The unique positive zero of \(f_0\) is \(L=\log2\) and \(f_0'(L)=-2\). The previous sign classification places \(nz_{n,k}\) near \(L\), uniformly in \(k\), and Taylor expansion at this simple zero yields the claimed activity expansion because \(f_1(L;\rho)=4L+(1+3\rho)L^2\). Finally \(Z_{n,k}(x/n)\to3e^x-2\) uniformly in \(k\), proving the rescaled covariance limit.

## Verification
The companion standalone `check_three_shore.py` uses exact rational full-independent-set enumeration on graphs of up to fifteen vertices, and independently checks the partition, one-site and two-site weighted counts. It also verifies the exact coefficient expression and sign-variation count for every integer parameter pair with \(3\le n\le70\) and \(1\le k\le n\). Its recorded output is `THREE_SHORE_DEFECT_CHECKS_PASSED 12464`. These finite calculations are supplementary to the all-size combinatorial and Descartes arguments, not a substitute for them.

## Relationship to prior work
The hard-core measure and occupation statistics are standard; Kahn (2001) established entropy and occupation bounds for regular bipartite models. Later spatial-mixing results such as Sinclair, Srivastava and Yin (2013), and graph-container results such as Jenssen, Malekshahian and Park (2026), concern general correlation structure or phase selection on different graph families; their examined statements do not provide this exact three-shore defect-pair covariance sign law. Standard polynomial tables already give \(3(1+z)^n-2\) for undeleted \(K_{n,n,n}\), a baseline used here rather than claimed as new. The present contribution is the all-size *uniqueness* of the sign reversal, its exceptional size, and a uniform two-term finite-size crossover expansion for locally compatible vertices. General weighted-independent-set identities alone do not settle this sign-variation problem.

## Limitations
The result applies only to equal fugacity and disjoint complete triangular edge deletions. No claim is made about arbitrary defect locations, nonidentical activities, other pairs, zero-free regions, infinite-volume phase coexistence, or uniqueness of any other observable's zero. Although available searches and inspected sources did not identify an equivalent statement, complete historical-priority confirmation and independent validation have not been performed.

## References
1. J. Kahn, *An Entropy Approach to the Hard-Core Model on Bipartite Graphs*, Combinatorics, Probability and Computing 10 (2001), 219–237. https://doi.org/10.1017/S0963548301004631 (online publication dated 25 June 2001).
2. A. Sinclair, P. Srivastava, Y. Yin, *Spatial mixing and approximation algorithms for graphs with bounded connective constant*, arXiv:1308.1762 (8 August 2013). https://arxiv.org/abs/1308.1762.
3. M. Jenssen, A. Malekshahian, J. Park, *A Refined Graph Container Lemma and Applications to the Hard-Core Model on Bipartite Expanders*, Random Structures & Algorithms (2026). https://doi.org/10.1002/rsa.70041.
4. E. W. Weisstein, *Independence Polynomial*, MathWorld, tabulated complete tripartite and crown graph cases. https://mathworld.wolfram.com/IndependencePolynomial.html.
