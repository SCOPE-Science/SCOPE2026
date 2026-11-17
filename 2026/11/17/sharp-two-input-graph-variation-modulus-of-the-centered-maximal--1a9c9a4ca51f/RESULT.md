# Sharp two-input graph-variation modulus of the centered maximal operator on complete graphs

## Finding
For the finite complete graph \(K_n\), \(n\ge2\), and nonnegative real vertex signals, let
\[
 (Mf)_i=\max\left\{f_i,\overline f\right\},\qquad
 \overline f=\frac1n\sum_{j=1}^{n}f_j,
 \qquad \operatorname{TV}(h)=\sum_{1\le i<j\le n}|h_i-h_j|.
\]
Then the **exact sharp two-input perturbation constant** is
\[
 C_n:=\sup_{\substack{f,g\ge0\\\operatorname{TV}(f-g)>0}}
 \frac{\operatorname{TV}(Mf-Mg)}{\operatorname{TV}(f-g)}
 =\begin{cases}
 \frac12,&n=2,\\[1mm]
 1+\frac{\lfloor(n-2)^2/4\rfloor}{n(n-1)},&n\ge3.
 \end{cases}
\]
Every value is attained by a nonnegative pair with no ties between its coordinates and their respective means. The operator is pairwise variation nonexpansive precisely for \(n\le3\). For \(n\ge4\) it strictly amplifies some differences even though its **single-input** variation factor is strictly below one. Moreover \(\lim_{n\to\infty}C_n=5/4\).

## Assumptions and scope
The graph is simple, unweighted, undirected and complete; counting measure is used in each ball average. Functions are real and nonnegative, and \(\operatorname{TV}\) is the sum over unordered edges with no normalization. The maximal function takes the largest average over centered balls of integral graph radius; on \(K_n\) the only distinct balls are a singleton and the entire vertex set. The two-input ratio is restricted to positive denominator. The result holds for all integers \(n\ge2\), including the exceptional two-vertex case.

## Proof
**1. Local branches.** For \(S\subseteq\{1,\ldots,n\}\), define the linear constant-preserving map
\[
 (A_Sh)_i=\begin{cases}h_i,&i\in S,\\\overline h,&i\notin S.\end{cases}
\]
On an open region where exactly the indices in \(S\) lie strictly above the mean, \(M=A_S\). Such regions exist for every nonempty proper \(S\): the signal \(\mathbf1_S\) has mean strictly between zero and one. Along a segment of nonnegative signals, the maximal map is continuous and piecewise affine with these branches. Consequently its global two-input variation modulus is at most the maximum of the variation operator seminorms of the \(A_S\). Degenerate segments lying on a branch boundary are covered by continuity from nearby generic segments.

**2. Cut reduction.** For any constant-preserving linear map \(A\), its variation operator seminorm on a connected finite graph equals
\[
 \max_{\varnothing\ne U\subsetneq V}
 \frac{\operatorname{TV}(A\mathbf1_U)}{\operatorname{TV}(\mathbf1_U)}.
\]
Indeed, after arranging the finitely many coordinate levels of \(h\), write \(h=c\mathbf1+\sum_r\delta_r\mathbf1_{U_r}\) with \(\delta_r\ge0\) and nested strict upper-level sets. The graph coarea identity gives \(\operatorname{TV}(h)=\sum_r\delta_r\operatorname{TV}(\mathbf1_{U_r})\), while the triangle inequality and \(A\mathbf1=\mathbf1\) bound \(\operatorname{TV}(Ah)\) by the corresponding sum for its images. Each cut indicator attains its own ratio.

**3. Exact branch-cut value.** Fix a nontrivial cut \(U\), let \(l=|U|\), and put \(x=|S\cap U|\), \(z=|S\setminus U|\). Then \(0\le x\le l\) and \(0\le z\le n-l\). The vector \(A_S\mathbf1_U\) takes the values \(1\) on \(S\cap U\), \(0\) on \(S\setminus U\), and \(l/n\) on \(S^c\). Counting its pairwise absolute differences yields the identity
\[
 \frac{\operatorname{TV}(A_S\mathbf1_U)}{\operatorname{TV}(\mathbf1_U)}
 =\frac{x(n-x)}{nl}+\frac{z(n-z)}{n(n-l)}.
 \tag{1}
\]
This is an exact algebraic identity, not a relaxation.

**4. Global maximization.** Because \(A_S(\mathbf1-\mathbf1_U)=\mathbf1-A_S\mathbf1_U\), cut complements have identical ratios. Thus assume \(l\le n/2\). Set \(F=\lfloor n^2/4\rfloor\). Since \(x\le l\le n/2\), one has \(x(n-x)\le l(n-l)\); also \(z(n-z)\le F\) for every integer \(z\). Equation (1) therefore implies
\[
 R\le\frac{n-l}{n}+\frac{F}{n(n-l)}=\frac1n\left(m+\frac Fm\right),\qquad
 m=n-l\in[\lceil n/2\rceil,n-1].
\]
The function \(m\mapsto m+F/m\) is strictly convex for \(m>0\), so its maximum on this interval lies at an endpoint. Its value at \(\lceil n/2\rceil\) is exactly \(n\). Its value at \(n-1\) is \(n+[F-(n-1)]/(n-1)\), which is at least \(n\) for \(n\ge3\). Since \(F-(n-1)=\lfloor(n-2)^2/4\rfloor\), every branch satisfies the claimed upper bound when \(n\ge3\).

**5. Attainment and the boundary cases.** For \(n\ge3\), take \(U=\{1\}\) and choose \(S\) to contain vertex \(1\) and exactly \(\lfloor n/2\rfloor\) of the remaining vertices. Then in (1) \(l=x=1\) and \(z=\lfloor n/2\rfloor\), so both inequalities in Step 4 attain equality. Put \(f=\mathbf1_S\) and \(g=f+\varepsilon\mathbf1_U\), where \(\varepsilon>0\) is sufficiently small. Both data vectors are nonnegative and have the same strict active set \(S\); hence \(Mg-Mf=\varepsilon A_S\mathbf1_U\), giving the exact global ratio. For \(n=2\), a direct check gives \((Mf)_1-(Mf)_2=(f_1-f_2)/2\) for every nonnegative input. Therefore all two-input variation differences are exactly halved. This completes the proof.

## Verification
Run `python3 verify_complete_graph_maximal.py` using Python's standard library. The exact-rational checker exhausts the cardinality parameters \(n,k,l,x\) in the range \(2\le n\le31\), directly enumerates all active sets and cut subsets for \(2\le n\le8\), tests the explicit sharp pairs through \(n=300\), and samples deterministic rational pairs. It also checks the obstruction to removing the nonnegative-input hypothesis. The code is supplementary evidence: the theorem for all finite orders rests on Steps 1–5, not on finite enumeration.

## Relationship to prior work
Soria and Tradacete introduced sharp finite-graph Hardy–Littlewood maximal-operator \(\ell_p\) estimates and the complete-graph formula for individual outputs (arXiv:1410.6204). González-Riquelme and Madrid proved sharp **single-input** graph-variation estimates for complete graphs and qualitative continuity statements in graph BV norms (arXiv:2005.03146, Theorems 1 and 3). González-Riquelme, Kovač and Madrid completed the sharp single-input variation theorem for all exponents (arXiv:2603.12462, Theorem 1). None of those inspected statements supplies the present exact constant for \(\operatorname{TV}(Mf-Mg)\) relative to \(\operatorname{TV}(f-g)\); single-input inequalities cannot be applied to nonlinear output differences. An earlier two-input exact result is not ruled out by a finite literature search.

## Limitations
The result applies only to nonnegative real signals on complete graphs with counting-measure centered averages. For the conventional signed-input maximal operator \(M|f|\), graph variation of differences cannot be bounded solely by graph variation of input differences: a constant shift can change the output variation nontrivially, even when the input-difference variation vanishes. This is a domain obstruction rather than a contradiction. Weighted graphs, other topologies, other variation exponents, and a classification of *all* maximizing pairs are not treated. Historical priority remains subject to independent bibliographic review.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (public preprint 2014-10-22), particularly Sections 1–3. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (public preprint 2020-05-06), Theorems 1 and 3. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (public preprint 2026-03-12), Theorem 1. https://arxiv.org/abs/2603.12462
