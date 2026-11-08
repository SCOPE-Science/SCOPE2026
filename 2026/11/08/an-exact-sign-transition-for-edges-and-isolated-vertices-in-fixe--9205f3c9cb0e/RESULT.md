# An exact sign transition for edges and isolated vertices in fixed-size induced cluster graphs

## Finding

Let \(r\ge2\) and \(m\ge2\) be integers. Let \(G=rK_m\) be the disjoint union of \(r\) labeled complete graphs, each on \(m\) vertices. Uniformly choose a \(k\)-vertex subset \(S\subseteq V(G)\), where \(0\le k\le rm\). Write \(E\) for the number of edges in \(G[S]\) and \(I\) for the number of isolated vertices in \(G[S]\) (the number of clique blocks represented exactly once).

For \(k\ge1\), define
\[
Q_{r,m,k}=k\frac{\binom{(r-1)m}{k-1}}{\binom{rm-1}{k-1}},
\]
with an out-of-range binomial coefficient equal to zero. Then \(\mathbb EI=Q_{r,m,k}\) and
\[
\boxed{\operatorname{Cov}(E,I)=Q_{r,m,k}\frac{(m-1)(k-1)[m(k-2r)+2]}{2((r-1)m-1)(rm-1)}.}
\tag{1}
\]
For \(k=0\), the covariance is zero.

For \(m\ge3\) the complete sign classification is
\[
\operatorname{Cov}(E,I)
\begin{cases}
<0,& 2\le k\le 2r-1,\\
>0,& 2r\le k\le(r-1)m+1,\\
=0,& k=0,1\ \text{or}\ (r-1)m+2\le k\le rm.
\end{cases}
\tag{2}
\]
For \(m=2\), the covariance is negative exactly when \(2\le k\le2r-2\) and otherwise zero. The cases \(k=2r-1\) and \(k=2r\) show why \(m=2\) is exceptional.

For comparison, if each vertex of the *same* graph \(G\) is retained independently with probability \(p\in(0,1)\), and \(E_p,I_p\) count induced edges and isolated retained vertices, then
\[
\boxed{\operatorname{Cov}(E_p,I_p)=-r\binom m2\,mp^3(1-p)^{m-1}<0.}
\tag{3}
\]
In particular, conditioning the sample size can change the covariance sign, although the host graph is unchanged.

At fixed \(r\ge2\) and \(k\ge1\), as \(m\to\infty\),
\[
\operatorname{Cov}(E,I)\longrightarrow
\frac{k(k-1)(k-2r)}{2r(r-1)}\left(1-\frac1r\right)^{k-1}.
\tag{4}
\]
At the critical sample size \(k=2r\), the positive finite-capacity correction has the exact first-order limit
\[
\boxed{\lim_{m\to\infty}m\operatorname{Cov}(E,I)
=\frac{2(2r-1)}{r-1}\left(\frac{r-1}{r}\right)^{2r-1}>0.}
\tag{5}
\]

## Assumptions and scope

The host has exactly \(r\) mutually disconnected complete blocks of equal size \(m\). The main ensemble is simple random sampling *without replacement* of exactly \(k\) vertices. Isolated vertices means degree zero **within the induced graph**; unselected host vertices are not counted. All equalities and signs in (1)--(3) hold at finite integer parameters. The limit (4) fixes \(r,k\) and lets the block capacity \(m\) increase.

This is a covariance statement, not a claim of monotone regression, negative association, or a stochastic-order comparison. The independent-retention ensemble in (3) is a separate model, not a conditioning identity for every sample size.

## Proof

Put \(N=rm\) and \(B=(r-1)m\). For any fixed host edge, the probability both endpoints lie in \(S\) is \(k(k-1)/(N(N-1))\). There are \(r\binom m2\) host edges, so
\[
\mathbb EE=\frac{(m-1)k(k-1)}{2(N-1)}.
\tag{6}
\]

Fix a host vertex \(v\). The event \(A_v\) that \(v\) is selected and isolated in the induced subgraph requires selecting \(v\) and choosing all other \(k-1\) vertices from the \(B\) vertices outside its clique. Consequently
\[
\Pr(A_v)=\frac{k}{N}\frac{\binom B{k-1}}{\binom{N-1}{k-1}},\qquad
\mathbb EI=N\Pr(A_v)=Q_{r,m,k}.
\tag{7}
\]

If \(\Pr(A_v)>0\), conditioning on \(A_v\) leaves a uniform \((k-1)\)-element subset of the \(r-1\) other cliques. Using the same edge-count calculation gives
\[
\mathbb E[E\mid A_v]
=\frac{(m-1)(k-1)(k-2)}{2(B-1)}.
\tag{8}
\]
As \(I=\sum_{v\in V(G)}\mathbf1_{A_v}\), and the conditional mean in (8) is the same for every vertex,
\[
\begin{aligned}
\operatorname{Cov}(E,I)
&=\sum_v\Pr(A_v)(\mathbb E[E\mid A_v]-\mathbb EE)\\
&=Q_{r,m,k}\frac{(m-1)(k-1)}2
\left(\frac{k-2}{B-1}-\frac{k}{N-1}\right).
\end{aligned}
\tag{9}
\]
The numerator when combining the two fractions is
\[
(k-2)(rm-1)-k((r-1)m-1)=m(k-2r)+2.
\tag{10}
\]
Equations (9)--(10) prove (1) when \(Q_{r,m,k}>0\). If \(Q_{r,m,k}=0\), no isolated selected vertex is possible, hence \(I=0\) identically and both sides of (1) vanish. The trivial cases \(k=0,1\) also have constant \(E=0\).

For \(k\ge2\), the factor \(Q_{r,m,k}\) is positive precisely when \(k-1\le B\), i.e. \(k\le (r-1)m+1\). All denominator factors in (1) are strictly positive for \(r,m\ge2\). If \(m\ge3\), the factor in (10) is strictly negative for \(k\le2r-1\) and strictly positive for \(k\ge2r\). The positive range exists because \((r-1)m+1\ge2r\) for \(r\ge2,m\ge3\). This proves (2). For \(m=2\), (10) equals \(2(k-2r+1)\), and the largest \(k\) allowing an isolate is \(2r-1\). This proves the exceptional classification.

For independent vertex retention, write \(E_p=\sum_{j=1}^r E_{p,j}\), \(I_p=\sum_{j=1}^r I_{p,j}\) for block contributions. Distinct blocks are independent. Inside one block, \(I_{p,j}=1\) means exactly one selected vertex and forces \(E_{p,j}=0\). Therefore
\[
\operatorname{Cov}(E_{p,j},I_{p,j})
=-\mathbb EE_{p,j}\mathbb EI_{p,j}
=-\binom m2p^2\,mp(1-p)^{m-1}.
\]
Summation over the independent blocks proves (3).

Finally, for fixed \(r,k\), the product form of (7) implies
\[
Q_{r,m,k}\longrightarrow k\left(\frac{r-1}{r}\right)^{k-1}.
\]
Substitution into (1) gives (4). In the boundary case \(k=2r\), the bracket \(m(k-2r)+2\) equals \(2\), and multiplying (1) by \(m\) before taking the limit gives (5). These limits are algebraic and do not rely on finite verification.

## Verification

Run `python3 verify.py`. The checker uses `fractions.Fraction` and independently obtains covariance by weighting every finite occupancy profile \((n_1,\ldots,n_r)\) with \(\prod_j\binom m{n_j}\). For small host graphs it additionally enumerates literal selected vertex subsets. It checks every admissible sample size in a bounded parameter grid, both covariance formulas, and the sign regimes. It reports `PASS: 903 exact assertions` on the packaged code. Finite enumeration corroborates but does not replace the exact argument above; the convergence tests in the code are also supplementary to the algebraic proof.

## Relationship to prior work

Janson's 2008 percolation study treats independently retained vertices of random graphs with prescribed degree distributions and emphasizes giant components and cores. The present fixed host and its fixed-cardinality sample, and the edge--isolate covariance sign classification, are not among those stated results.

Penrose's 2009 paper studies normal approximation for singleton counts in independently allocated urns, a with-replacement model, whereas the present occupancy vector is multivariate hypergeometric. The published exact richness--frequency and richness--pair-collision covariance results for independent categorical sampling likewise concern different sampling and response statistics.

Holst's 1979 finite-urn work and Charalambides' 1981 restricted-occupancy paper are especially relevant to the underlying bounded-capacity occupancy model; Charalambides' 2005 joint occupancy distribution could supply all moments in principle. Such general moment machinery is not itself an explicit derivation of the sharp \(k=2r\) sign transition, the exceptional \(m=2\) classification, or the contrast (3). Full text of the latter historical papers was not available for detailed theorem-by-theorem comparison; implicit coverage remains an important priority risk.

## Limitations

This finding is restricted to equal-size clique components. Unequal component sizes need not have a threshold depending only on the number of components. General covariance identities for finite-population occupancy might imply (1) upon specialization; the result claimed as distinctive is the complete sign classification and its ensemble contrast, not the multivariate-hypergeometric distribution itself. The historical-priority comparison remains qualified because some plausible older sources were inaccessible in full text. No claim of statistical association stronger than covariance is made.

## References

1. S. Janson, “On percolation in random graphs with given vertex degrees,” arXiv:0804.1656, first public 2008-04-10, https://arxiv.org/abs/0804.1656.
2. M. D. Penrose, “Normal approximation for isolated balls in an urn allocation model,” arXiv:0901.3493, first public 2009-01-22, https://arxiv.org/abs/0901.3493.
3. L. Holst, “A unified approach to limit theorems for urn models,” *Journal of Applied Probability* 16 (1979), 154–162, DOI:10.2307/3213383.
4. C. A. Charalambides, “On a restricted occupancy model and its applications,” *Biometrical Journal* 23 (1981), 601–610, DOI:10.1002/bimj.4710230609.
5. C. A. Charalambides, “Derivation of a joint occupancy distribution via a bivariate inclusion and exclusion formula,” *Metrika* 62 (2005), 149–160, DOI:10.1007/s00184-005-0413-0.
6. “A one-switch covariance law for occupancy richness and frequency counts,” published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
7. “Universal positive covariance of sample richness and unbiased Gini–Simpson diversity,” published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-universal-positive-covariance-of-sample-richness-and-unbiased-gi--e84114bd4ba0.
