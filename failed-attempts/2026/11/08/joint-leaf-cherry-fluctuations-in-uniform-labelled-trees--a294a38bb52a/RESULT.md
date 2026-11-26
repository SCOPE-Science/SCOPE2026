# Joint leaf–cherry fluctuations in uniform labelled trees

## Finding

Let \(T_n\) be uniformly distributed over the \(n^{n-2}\) simple trees with labelled vertex set \(\{1,\ldots,n\}\). Write \(L_n\) for its number of degree-one vertices. A *degree-three cherry* consists of an unordered pair of degree-one vertices with a common neighbor of degree exactly three; let \(C_n\) be the number of these pairs. For \(n\ge7\), put
\[
A_n=\frac{n(n-1)(n-2)(n-3)^{n-4}}{2n^{n-2}},\qquad
B_n=\frac{(n)_6(n-6)^{n-6}}{4n^{n-2}},
\]
where \((n)_6=n(n-1)\cdots(n-5)\), and
\[
a_n=\left(1-\frac1n\right)^{n-2},\qquad
b_n=\left(1-\frac2n\right)^{n-2},\qquad
q_n=\left(1-\frac1{n-3}\right)^{n-4}.
\]
The exact moment identities are
\[
\begin{aligned}
\mathbb E L_n&=na_n,&\mathbb E L_n^2&=na_n+n(n-1)b_n,\\
\mathbb E C_n&=A_n,&\mathbb E C_n^2&=A_n+B_n,\\
\mathbb E[L_n C_n]&=A_n[2+(n-3)q_n].
\end{aligned}
\]
In particular,
\[
\boxed{\operatorname{Cov}(L_n,C_n)=A_n\bigl(2+(n-3)q_n-na_n\bigr)>0.}
\]
The same mixed-moment formula and strict positivity hold for \(n=5,6\) when \(A_n\) is defined by the formula above. Thus the positive-covariance assertion holds for every \(n\ge5\).

Moreover, as \(n\to\infty\),
\[
\frac1{\sqrt n}\begin{pmatrix}L_n-\mathbb E L_n\\C_n-\mathbb E C_n\end{pmatrix}
\ \xrightarrow{\mathrm d}\ N_2\!\left(0,
\begin{pmatrix}
(e-2)e^{-2}&(e-2)e^{-4}\\
(e-2)e^{-4}&(e^3-3)/(2e^6)
\end{pmatrix}\right).
\]
The limiting Pearson correlation is strictly between zero and one and equals
\[
\boxed{\rho=\sqrt{\frac{2(e-2)}{e^3-3}}\;\approx0.289966697254.}
\]

## Assumptions and scope

The probability space is the uniform *unrooted Cayley labelled tree* model, not a binary phylogenetic tree, an increasing/recursive tree, or a conditioned fixed-degree model. All degrees are ordinary undirected degrees. The vertex pair in each cherry is unordered; a degree-three center with precisely two leaf neighbors contributes one cherry. For \(n\ge5\) a degree-three center cannot have three leaf neighbors, since that would be a four-vertex connected component equal to the whole tree. Hence different cherries in these sizes have disjoint triples of vertices.

The Gaussian statement concerns two jointly observed statistics of the *same* random tree, centered by their exact means. It makes no assertion about independent sampling, conditional Gaussianity at fixed degree sequence, or stronger modes of convergence. The exact second-moment identity is asserted for \(n\ge7\), with the \(n=6\) interpretation \(0^0=1\) in \(B_n\) also correct; the checker verifies the small orders explicitly.

## Proof

**One cherry and its leaf count.** Fix distinct labels \(u,v,w\), with \(u,v\) required to be leaves adjacent to degree-three center \(w\). Delete \(u,v\) and their edges. This gives a uniform labelled tree on the remaining \(n-2\) vertices in which \(w\) is a leaf; conversely any such tree uniquely extends by reattaching \(u,v\) to \(w\). Its Prüfer word has length \(n-4\) and uses any of the other \(n-3\) remaining labels with equal probability. Consequently a fixed cherry occurs with probability \((n-3)^{n-4}/n^{n-2}\). Summing over \(n\binom{n-1}{2}\) choices gives \(\mathbb E C_n=A_n\). Conditionally on the fixed cherry, vertices \(u,v\) are leaves, \(w\) is not, and every other remaining vertex is a leaf exactly when absent from that shorter Prüfer word. Thus
\[
\mathbb E[L_n\mid u,v,w\text{ form a cherry}]=2+(n-3)q_n.
\]
Multiplying by the cherry indicators and summing proves \(\mathbb E[L_n C_n]=A_n[2+(n-3)q_n]\).

**One leaf and two leaves.** The ordinary Prüfer word has length \(n-2\) over \(n\) equally likely symbols. A vertex is a leaf exactly when its symbol is absent. Hence the one- and two-vertex leaf probabilities are respectively \(a_n\) and \(b_n\), giving both stated leaf moments.

**Two cherries.** For \(n\ge7\), distinct degree-three cherry triples are vertex-disjoint. For a specified *ordered* pair of distinct cherries with six distinct labels, there are \((n-6)^{n-6}\) extension trees: start with a tree on the other \(n-6\) labels, then attach each designated degree-three center by its third edge to any of those \(n-6\) vertices. There are \((n)_6/4\) ordered choices of the two triples, each leaf pair being unordered. Thus the contribution of *unequal* indicator pairs to \(\mathbb E[C_n^2]\) is \(B_n\). The diagonal contribution is exactly \(\mathbb E C_n=A_n\), not twice that quantity. This proves \(\mathbb E C_n^2=A_n+B_n\). The \(n=6\) boundary corresponds to the unique joining edge between the two cherry centers and yields the same formula with \(0^0=1\).

**Strict sign.** Write \(\Delta_n=2+(n-3)q_n-na_n\). Directly, \(\Delta_5=11/25>0\). For \(n\ge6\), using \(\log(1-t)\ge-t/(1-t)\) for \(0<t<1\) gives \(q_n\ge e^{-1}\). Also \(\log(1-t)\le-t-t^2/2\) yields \(a_n\le e^{-1+x_n}\), where \(x_n=3/(2n)+1/n^2\le5/(3n)\). Since \(e^x\le(1-x)^{-1}\) for \(0\le x<1\), we obtain
\[
\Delta_n\ge2-\frac3e-\frac{n}{e}\frac{x_n}{1-x_n}
\ge 2-\frac{69}{13e}>0,
\]
where the last inequality uses \(e>8/3\). Therefore the covariance is positive at every stated size.

**Asymptotic matrix.** Expansion of the exact expressions gives
\[
\begin{aligned}
A_n&=\frac{n}{2e^3}+\frac9{4e^3}+O(n^{-1}),\\
B_n&=\frac{n^2}{4e^6}+\frac{3n}{4e^6}+O(1),\\
2+(n-3)q_n-na_n&=2-\frac4e+O(n^{-1}).
\end{aligned}
\]
Therefore
\[
\begin{aligned}
\frac1n\operatorname{Var}(L_n)&\longrightarrow(e-2)e^{-2},\\
\frac1n\operatorname{Var}(C_n)&\longrightarrow\frac{e^3-3}{2e^6},\\
\frac1n\operatorname{Cov}(L_n,C_n)&\longrightarrow(e-2)e^{-4}.
\end{aligned}
\]
The limiting covariance matrix is strictly positive definite since its determinant equals \((e-2)(e^3-2e+1)/(2e^8)>0\).

**Joint Gaussian convergence.** The local-pattern central limit criterion of Isaev, Southwell and Zhukovskii (arXiv:1912.09838, Theorem 1.1) applies to every fixed real linear combination \(\alpha L_n+\beta C_n\). Indeed, a single legal edge reattachment changes the leaf count at at most two vertices, and can change cherry counts only in bounded-size neighborhoods of the changed endpoints: a vertex qualifying as a cherry center has degree three, and an endpoint changing leaf status has degree at most two. Thus the linear combination is bounded-Lipschitz under reattachments, and two reattachments separated by more than a fixed distance have additive effects (bounded superposability radius). The variance of every nonzero linear combination is asymptotically \(n\) times a strictly positive quadratic form, by the matrix above. Thus the criterion gives a univariate normal limit for every combination; the Cramér–Wold device yields the displayed bivariate limit. This does not assert that the published criterion itself is new.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The checker independently enumerates every Prüfer word for sizes five through eight, decodes its tree, counts leaves and degree-three cherries, and compares all five rational moments with the formulas. It also checks the strict finite-size covariance sign through size 500 and the algebraic/numerical limiting-matrix identities. It prints `VERIFY_OK 282379 exact and asymptotic-sign checks`. The finite enumeration does not certify an infinite theorem; that follows from the preceding proof.

## Relationship to prior work

Junk, Schmidt and Weber (2020) study the same degree-three cherry convention in uniform labelled trees and derive cherry-indicator enumerations, the mean and asymptotic prevalence of cherries. Our new assertion is the **mixed leaf–cherry moment/covariance and its explicitly parameterized joint Gaussian law**, including the limiting correlation. The diagonal-versus-distinct-pair decomposition above is independently established; it is necessary to obtain the correct leading cherry variance. The source's displayed second-moment expression should not be substituted for this decomposition without independently checking conventions and diagonal multiplicities.

Isaev, Southwell and Zhukovskii (first publicly available in 2019) prove a general normal approximation criterion and random-tree pattern-count central limit results; those general limit tools are used, not rediscovered, here. The explicit mixed covariance matrix is not one of their reported results. Ekhad and Zeilberger (2022) analyze joint *degree counts*, including asymptotic decorrelation between degree-one and degree-three counts. The cherry statistic is strictly finer than the degree-three count because it records the degrees of neighbors. Choi, Kaur and Wu (2021) prove joint limit laws for cherries and pitchforks in binary phylogenetic tree models, a different sample space with different statistics. Literature searches found no exact leaf–degree-three-cherry mixed law for Cayley trees; absence from search is not a proof of historical priority.

## Limitations

The result does not establish independence (the limiting correlation is positive) or a conditional central limit theorem at fixed leaf count. The asymptotic law uses an existing general pattern-count Gaussian criterion. Some broader enumeration frameworks could yield the finite moments after specialization, and unindexed historical sources may contain an equivalent result. No independent audit or exhaustive historical-priority certification has been performed.

## References

1. M. Isaev, A. Southwell and M. Zhukovskii, *Distribution of tree parameters by martingale approach*, arXiv:1912.09838 (initial version 2019-12-20); Combinatorics, Probability and Computing 31 (2022), 737–764. https://arxiv.org/abs/1912.09838 ; https://doi.org/10.1017/S0963548321000523
2. L. Junk, S. Schmidt and M. Weber, *Almost all trees have quantum symmetry*, arXiv:1911.02952 (first public version 2019-11-07); Archiv der Mathematik 115 (2020), 367–378. https://arxiv.org/abs/1911.02952 ; https://doi.org/10.1007/s00013-020-01476-x
3. S. B. Ekhad and D. Zeilberger, *Automated Counting and Statistical Analysis of Labeled Trees with Degree Restrictions*, arXiv:2201.07326 (2022-01-18). https://arxiv.org/abs/2201.07326
4. K. P. Choi, G. Kaur and T. Wu, *On asymptotic joint distributions of cherries and pitchforks for random phylogenetic trees*, Journal of Mathematical Biology 83 (2021), article 40. https://doi.org/10.1007/s00285-021-01667-2
