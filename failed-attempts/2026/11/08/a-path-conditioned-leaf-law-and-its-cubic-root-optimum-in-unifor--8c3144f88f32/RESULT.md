# A path-conditioned leaf law and its cubic-root optimum in uniform labeled trees

## Finding

Let \(T_n\), for integer \(n\ge3\), be uniform among the \(n^{n-2}\) labeled trees on \([n]\). Fix distinct labels \(u,v\); let \(D=d_{T_n}(u,v)\) and let \(L\) be the total number of degree-one vertices. Given \(D=d\), write \(k=d+1\), \(m=n-d-1\). Let \(X\) count leaves outside the unique \(u\)-to-\(v\) path, and let \(Y\) count its two endpoints that are leaves. For \(1\le d\le n-2\), \(0\le r\le m\), and \(0\le s\le2\), the complete mixed binomial moments are
\[
\boxed{\mathbb E\!\left[\binom Xr\binom Ys\mid D=d\right]
=\binom mr\binom2s\frac{k-s}{k}\left(\frac{n-r-s}{n}\right)^{m-1}.}\tag{1}
\]
When \(k=s\) the right side is interpreted as zero. Equivalently, the exact probability-generating polynomial of \(L=X+Y\), conditional on this distance, is
\[
\boxed{\mathbb E[t^L\mid D=d]
=\sum_{r=0}^{m}\sum_{s=0}^{2}
\binom mr\binom2s\frac{k-s}{k}\left(\frac{n-r-s}{n}\right)^{m-1}(t-1)^{r+s}.}\tag{2}
\]
At \(d=n-1\), \(L=2\) almost surely, so the generating polynomial is \(t^2\).

In particular, the conditional expected number of leaves equals
\[
\boxed{M_n(d)=\mathbb E[L\mid D=d]
=\left(n-d+1-\frac2{d+1}\right)
\left(1-\frac1n\right)^{n-d-2},\qquad 1\le d\le n-2,}\tag{3}
\]
with \(M_n(n-1)=2\). Its maximum over integer distances \(1\le d\le n-1\) is attained at \(d=\lceil a_n\rceil\), where the unique positive \(a_n\) solves
\[
\boxed{a_n(a_n+1)^2=2(n-1).}\tag{4}
\]
If \(a_n\) is an integer, the maximizing distances are instead the two consecutive values \(a_n\) and \(a_n+1\). Consequently, every maximizing distance is asymptotic to \((2n)^{1/3}\). In particular, the conditional mean is **not** monotone in the distance when \(n\ge4\).

For any integers \(d_n\) with \(d_n\to\infty\) and \(d_n/\sqrt n\to z\in[0,\infty)\),
\[
\boxed{M_n(d_n)-\frac ne\longrightarrow\frac{5-z^2}{2e}.}\tag{5}
\]
The familiar Rayleigh distance limit then yields
\[
\boxed{\frac{\operatorname{Cov}(D,L)}{\sqrt n}\longrightarrow
-\frac1{2e}\sqrt{\frac\pi2}.}\tag{6}
\]
The cubic-root optimizing distance is much smaller than the typical distance, which has order \(\sqrt n\).

## Assumptions and scope

Vertices are labeled, the tree is uniform, and \(u\ne v\) are fixed. A leaf has graph degree exactly one, so the interior vertices of the marked path are never leaves. The mixed moments in (1) determine the full finite law of \(L\mid D=d\), not just its expectation. In (2), \(t\) may be an indeterminate or any complex number; the identity is polynomial. The case \(d=n-1\) is treated separately. The limit (5) assumes that the conditioning distance tends to infinity; it does not assert the same constant correction for fixed \(d\). The limiting covariance refers to ordinary finite covariance without conditioning.

## Proof

**Rooted-forest enumeration.** Fix the ordered labeled path \(P\) between \(u\) and \(v\), with \(k=d+1\) path vertices. Removing the \(d\) path edges from any tree containing \(P\) produces a forest rooted at the \(k\) path vertices. Conversely, restoring \(P\) turns any such forest into a tree with the stipulated path. The classical Cayley rooted-forest formula counts exactly \(k n^{n-k-1}=k n^{m-1}\) such forests. Because a tree has a unique path between two marked vertices, conditioning on \(D=d\) and then on the ordered labels of \(P\) yields a uniform rooted forest of this kind.

**Specified leaves.** Fix a set \(R\) of \(r\) off-path vertices and a set \(S\) of \(s\) marked endpoints. Require all vertices in \(R\cup S\) to be leaves. Delete \(R\cup S\), retaining the path edges between surviving path vertices and the corresponding rooted-forest structure. The remaining \(N=n-r-s\) vertices form a forest with \(k-s\) specified roots. There are \((k-s)N^{N-(k-s)-1}=(k-s)N^{m-r-1}\) such forests. Each deleted off-path leaf is reattached independently to one of the \(N\) surviving vertices, giving \(N^r\) possibilities; a selected endpoint is reattached only by its already stipulated path edge. Thus the number of compatible original trees is \((k-s)(n-r-s)^{m-1}\), compared with \(k n^{m-1}\) trees conditional on the fixed path. When both path vertices are deleted, there is no possible rooted forest; this is precisely the zero factor for \(k=s\). Taking sums over all \(\binom mr\binom2s\) choices proves (1). Expanding \(t^{X+Y}=(1+(t-1))^X(1+(t-1))^Y\) proves (2).

**Conditional mean and optimizer.** The terms \((r,s)=(1,0)\) and \((0,1)\) of (1) yield
\[
M_n(d)=\left(m+\frac{2(k-1)}k\right)
\left(1-\frac1n\right)^{m-1},
\]
which is (3). For every \(1\le d\le n-3\), direct exact subtraction gives
\[
\boxed{M_n(d+1)-M_n(d)
=\left(1-\frac1n\right)^{n-d-3}
\frac{2(n-1)-d(d+1)^2}{n(d+1)(d+2)}.}\tag{7}
\]
The numerator changes sign only once as \(d\) increases. The remaining step, \(d=n-2\) to \(d=n-1\), has difference \(-1+2/(n-1)\), negative for \(n\ge4\) and zero for \(n=3\). Consequently (4) describes the exact maximizing distances, including integer-threshold ties. Since \(a_n(a_n+1)^2=2(n-1)\), one has \(a_n\sim(2n)^{1/3}\).

**Large-tree expansion.** Put \(q_n=1-1/n\). Uniformly for \(1\le d\le n^{3/5}\), elementary Taylor expansions of \(\log q_n\) and \(\exp\) in (3) give
\[
M_n(d)-\frac ne
=\frac1{2e}\left(5-\frac4{d+1}-\frac{d^2}{n}\right)
+O\!\left(\frac{d+1}{n}+\frac{(d+1)^3}{n^2}\right).\tag{8}
\]
This proves (5) whenever \(d_n/\sqrt n\) remains bounded and \(d_n\to\infty\).

The exact marked-distance mass, obtained by counting paths via the classical forest-extension formula, is
\[
\Pr(D=d)=\frac{(d+1)(n-2)_{d-1}}{n^d},
\qquad 1\le d\le n-1,\tag{9}
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\). Its product form yields \(D/\sqrt n\Rightarrow R\), where \(R\) has density \(x e^{-x^2/2}\) for \(x>0\), and provides Gaussian upper tails for \(D/\sqrt n\). Specifically, the factor \(\prod_{j=2}^{d}(1-j/n)\) is bounded by \(\exp(-(d(d+1)-2)/(2n))\); hence the contribution of \(D>n^{3/5}\) to any polynomially bounded moment is exponentially small. On \(D\le n^{3/5}\), the remainder in (8) is uniformly \(o(1)\), and the bounded term \(4/(D+1)\) tends to zero in probability and in mean because \(D/\sqrt n\Rightarrow R\) with \(\Pr(R=0)=0\). Therefore the pair \((D/\sqrt n,M_n(D)-n/e)\) converges in distribution and in the mixed moments needed for covariance to \((R,(5-R^2)/(2e))\). Finally, \(\mathbb ER=\sqrt{\pi/2}\), \(\mathbb ER^2=2\), and \(\mathbb ER^3=3\sqrt{\pi/2}\), so
\[
\frac{\operatorname{Cov}(D,L)}{\sqrt n}
=\operatorname{Cov}\!\left(\frac D{\sqrt n},M_n(D)-\frac ne\right)
\longrightarrow-\frac{\mathbb ER^3-\mathbb ER\,\mathbb ER^2}{2e}
=-\frac1{2e}\sqrt{\frac\pi2}.
\]
This establishes (6).

## Verification

A self-contained Python verifier, `verify.py`, constructs every Prüfer-coded tree for \(3\le n\le8\), a total of \(280391\) labeled trees. It independently computes the marked path, separates off-path from endpoint leaves, and matches all conditional mixed binomial moments in (1) with exact rational arithmetic. It also checks the conditional means, every interior finite-difference identity through \(n=74\), the maximizing-distance pattern, and controlled large-size numerical instances of (5). Execution reports **3013 passed exact or controlled checks**. These finite tests are supporting checks only: the rooted-forest count, exact difference identity, and asymptotic bounds prove the statements for all stated orders.

## Relationship to prior work

Cayley's rooted-forest enumeration and Moon's forest-extension formula are classical; they provide the counting engine rather than the new conditional leaf law. Pitman's 1996 technical report collects these enumerations in Sections 2.1 and 2.2 but does not state (1)–(8). Aldous's 1990 study examines leaves, degrees and tree distances as classical properties of uniform labeled trees; the inspected discussion does not identify the total leaf-count regression on a marked-pair distance. Remmel and Williamson (2002) study spanning-tree function classes and various multivariate enumeration mechanisms, but their inspected material does not determine (1) or the cubic-root optimum. Berzunza Ojeda and Janson (2022, initially public in 2020) study global distance profiles and leaf-biased tree distributions, not the finite distance-conditioned complete leaf law.

Joyal's classical correspondence between functions and doubly marked labeled trees identifies the path vertices with cyclic points of a mapping and the **off-path leaves** with zero-indegree mapping vertices. Consequently the \(s=0\) part of (1), and the leading covariance contributed by those off-path leaves, are also obtainable from existing conditional mapping indegree-zero moment formulas: **these parts are acknowledged as prior coverage**, not claimed as novel. The contribution that is not supplied by that mapping marginal is the **joint law with the two marked endpoint leaf indicators** (the \(s=1,2\) terms), which produces the nonmonotone full-leaf regression and its sharp cubic-root maximizing distance. A separately indexed Cayley-tree result supplies an exact decreasing conditional law for the degree of one marked endpoint; it does not determine the joint endpoint/off-path leaf law or the conditional full-leaf optimum. Targeted searches for that joint law, equivalent generating polynomials, and the cubic-root maximum found no identified prior statement, but a negative search cannot prove uniqueness.

## Limitations

The classical off-path-only law is covered by the Joyal mapping correspondence and is not separately claimed. The model is the uniform complete-graph spanning tree; other random-tree models may behave differently. Formula (5) excludes fixed conditioning distances. The cubic-root maximizing distance is a conditional-mean phenomenon, not a description of typical marked-pair distance. The finite verifier does not prove any infinite limit. Older literature on multivariate Cayley-tree generating functions may implicitly contain a stronger identity; this historical-coverage uncertainty remains. No independent examination of the new proof is claimed.

## References

1. J. Pitman, “Coalescent Random Forests,” University of California, Berkeley, Statistics Technical Report 457, publicly dated September 1, 1996. https://statistics.berkeley.edu/tech-reports/457 . Relevant enumeration formulas in Sections 2.1–2.2 (the accessible PDF is a revised version).
2. D. J. Aldous, “The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees,” *SIAM Journal on Discrete Mathematics* 3 (1990), 450–465. DOI 10.1137/0403039.
3. J. B. Remmel and S. G. Williamson, “Spanning Trees and Function Classes,” *Electronic Journal of Combinatorics* 9 (2002), Research Paper 34. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r34/pdf/ .
4. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” *Combinatorics, Probability and Computing* 31 (2022), 368–410. arXiv:2009.00572, first posted September 2020.
5. A. Joyal, “Une théorie combinatoire des séries formelles,” *Advances in Mathematics* 42 (1981), 1–82. DOI 10.1016/0001-8708(81)90052-9 (mapping–tree species correspondence).
6. M. Soria, “Distribution of Image Points in Random Mappings,” INRIA Algorithms Seminar, November 10, 1996. https://algo.inria.fr/seminars/sem96-97/soria.html .
