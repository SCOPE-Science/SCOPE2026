# Subexponential collision probability for Pyranim game isomorphism

## Finding

Let \(\mathcal T_n\) be the stable positions (order ideals of the interval-containment poset) of an \(n\)-tier Pyranim game, and let \(X_n,Y_n\) be independent uniform samples from \(\mathcal T_n\). Write \(X_n\cong Y_n\) if they are game-isomorphic, equivalently if the associated unlabeled unit interval graphs are isomorphic. Then

\[
\boxed{\lim_{n\to\infty}\Pr(X_n\cong Y_n)^{1/n}=1.}
\]

More quantitatively, there exist absolute constants \(K>0\) and \(n_0\) such that for all integers \(n\ge n_0\),

\[
\exp\!\left(-K\frac{n\log\log n}{\log n}\right)
\leq\Pr(X_n\cong Y_n)\leq 1.
\]

This settles the exponential-scale question explicitly posed in Section 5.3, question 4 of Binyamin and Kniffen [1]. The lower estimate is not claimed to be the precise decay rate.

## Assumptions and scope

Fix an integer \(n\ge1\) and let \(\mathcal P_n=\{[i,j]:1\le i\le j\le n\}\), ordered by interval containment: \([a,b]\le[i,j]\) when \(i\le a\le b\le j\). A stable position \(X\subseteq\mathcal P_n\) is downward closed. The associated graph \(\Gamma(X)\) has vertices \(i\) for which \([i,i]\in X\), and edges \(\{i,j\}\) for which \([i,j]\in X\), for \(i<j\). Its components are unlabeled unit interval graphs [1]. Corollary 5.1 of [1] proves that two positions are game-isomorphic if and only if their associated graphs are isomorphic.

Let \(C_j=\binom{2j}{j}/(j+1)\) denote the Catalan numbers. The number of stable positions is exactly \(|\mathcal T_n|=C_{n+1}\) [1]. Let \(c_m\) denote the number of unlabeled connected unit interval graphs on \(m\) vertices. By the enumeration of Saitoh, Yamanaka, Kiyomi and Uehara [2], for every \(m\ge1\),

\[
c_m=\frac12\left(C_{m-1}+\binom{m-1}{\lfloor(m-1)/2\rfloor}\right)
\ge\frac12 C_{m-1}.
\]

No random-graph distribution or uniformity over isomorphism classes is assumed. The sampling is uniform over individual stable positions, independently with replacement.

## Proof

**1. Sufficiently many distinct connected component types.** For every integer \(j\ge0\), the central binomial coefficient is the largest term of \(\sum_{i=0}^{2j}\binom{2j}{i}=4^j\), hence

\[
\binom{2j}{j}\ge\frac{4^j}{2j+1}.
\]

Consequently, for \(m\ge1\),

\[
c_m\ge\frac{C_{m-1}}2\ge\frac{4^{m-1}}{2m(2m-1)}.
\]

For all sufficiently large integers \(n\), choose

\[
m=m_n=\left\lceil\log_4 n+4\log_4(\log n)\right\rceil,
\qquad r=r_n=\left\lfloor\frac nm\right\rfloor.
\]

Here \(\log\) is the natural logarithm. Then \(m=(\log n+4\log\log n)/\log4+O(1)\), so \(m=O(\log n)\), \(1\le m\le n\), and \(4^m\ge n(\log n)^4\). Thus

\[
c_m\ge\frac{n(\log n)^4}{8m(2m-1)}
\ge \frac nm\ge r
\]

for sufficiently large \(n\), because \((\log n)^4\ge 8(2m-1)\) eventually. We may select \(r\) pairwise nonisomorphic connected unit interval graphs, each with exactly \(m\) vertices.

**2. A factorial-sized isomorphism class.** Every connected unit interval graph has a proper interval ordering of its vertices (an umbrella ordering), in which an edge between positions \(i<j\) forces all edges between positions \(a<b\) with \(i\le a<b\le j\) [1,2]. For each of the chosen \(r\) graph types, fix one such ordering on an \(m\)-vertex consecutive block. Retain the bottom chips and those upper chips corresponding to its edges, without chips crossing block boundaries; this produces a downward-closed set of intervals, hence a stable position.

For each permutation \(\sigma\) of the \(r\) distinct component types, concatenate the corresponding blocks in the first \(rm\) positions of \(\{1,\ldots,n\}\), leaving the final \(n-rm\) bottom positions unoccupied and all chips crossing block boundaries absent. Each construction is a stable position \(X_\sigma\). Its associated graph is the disjoint union of the same \(r\) connected graphs, independently of their order. Thus all \(X_\sigma\) are game-isomorphic by [1]. They are pairwise different as positions: at the first block where \(\sigma\) and \(\tau\) differ, the resulting connected subgraphs have different isomorphism types. Therefore **one isomorphism class contains at least \(r!\) distinct stable positions**.

**3. Collision probability and the limit.** Partition \(\mathcal T_n\) into game-isomorphism classes \(\mathcal Q\). Independence and uniform sampling give the exact identity

\[
p_n:=\Pr(X_n\cong Y_n)
=\sum_{Q\in\mathcal Q}\left(\frac{|Q|}{C_{n+1}}\right)^2.
\]

By step 2 and the Catalan bound \(C_{n+1}\le4^{n+1}\),

\[
p_n\ge\left(\frac{r!}{C_{n+1}}\right)^2
\ge\left(\frac{r!}{4^{n+1}}\right)^2.
\]

Since \(m=(\log n+4\log\log n)/\log4+O(1)\) and \(r=n/m+O(1)\), Stirling's formula gives

\[
\log(r!)=r\log r-r+O(\log r)
=n\log4-O\!\left(\frac{n\log\log n}{\log n}\right).
\]

Substitution in the preceding lower bound yields

\[
\log p_n\ge-O\!\left(\frac{n\log\log n}{\log n}\right).
\]

The reverse bound \(p_n\le1\) is automatic. Dividing logarithms by \(n\) and exponentiating proves the claimed limit, as well as the stated quantitative lower estimate. All estimates hold for every sufficiently large integer \(n\); no numerical extrapolation is used. \(\square\)

## Verification

A standalone Python 3 script `verify.py` independently enumerates all interval-order ideals for \(1\le n\le6\). It checks their Catalan counts, counts connected graph types up to vertex-permutation isomorphism, and compares them with the formula for \(c_n\). At \(n=6\) it explicitly constructs two distinct but game-isomorphic states by swapping a three-vertex path and a triangle; both are checked to satisfy the ideal property. Numerical supply checks at selected larger \(n\) confirm \(c_m\ge r\). The script prints `VERIFY_OK` when all tests pass. These finite tests are supplementary and do not certify the infinite asymptotic theorem, which follows from the preceding inequalities.

## Relationship to prior work

Binyamin and Kniffen [1] provide the stable-position/Dyck-path correspondence, show that game isomorphism coincides with the unlabeled unit interval graph isomorphism, and explicitly pose the \(n\)-th-root collision-probability limit as an open question. Saitoh and coauthors [2], following earlier enumeration, give the exact connected-type count used in step 1. The present argument combines that count with a distinct-component permutation construction to obtain the previously unstated factorial-class bound and the collision exponent. The earlier enumerations of isomorphism classes, including OEIS A005217 [3], count different objects and by themselves neither determine the uniform-position collision probability nor entail the displayed limit without the new class-size analysis.

## Limitations

The lower estimate does not identify the true subexponential decay scale or a sharp leading constant, and it does not independently establish whether the collision probability tends to zero. Independent validation and a comprehensive historical priority audit have not been performed. The theorem concerns uniform sampling from all stable \(n\)-tier positions, not uniformly sampled isomorphism types or positions conditioned to have a full bottom row.

## References

[1] Y. Binyamin and E. Kniffen, *Enumerating Pyranim Isomorphisms*, arXiv:2611.16153v1, first posted 2026-11-12. https://arxiv.org/abs/2611.16153 ; accessible full text https://borowiecki.dev/pdf/2611.16153 . Relevant sections: 2.4, 3, 4.1–4.2, 5.1, and question 4 of 5.3.

[2] T. Saitoh, K. Yamanaka, M. Kiyomi and R. Uehara, *Random Generation and Enumeration of Proper Interval Graphs*, IEICE Transactions on Information and Systems E93.D(7), 1816–1823 (2010), Theorem 1. https://doi.org/10.1587/transinf.E93.D.1816 . Open full text https://www.jstage.jst.go.jp/article/transinf/E93.D/7/E93.D_7_1816/_pdf/-char/en .

[3] OEIS A005217, *Number of unlabeled unit interval graphs with n nodes*. https://oeis.org/A005217 .
