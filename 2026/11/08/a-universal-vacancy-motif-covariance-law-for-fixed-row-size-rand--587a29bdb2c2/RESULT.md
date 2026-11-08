# A universal vacancy–motif covariance law for fixed-row-size random incidence graphs

## Finding

**Theorem (exact covariance and one-transition classification).** Let \(m\ge s\ge1\) and \(n>k\ge1\) be integers. For each \(i\in\{1,\ldots,m\}\), independently choose a uniformly random subset \(A_i\subseteq[n]\) of prescribed size \(0\le r_i<n\). Let \(Z\) count the right-side labels absent from every \(A_i\). Fix a simple bipartite graph \(H\) with labeled left vertices \(u_1,\ldots,u_s\) and labeled right vertices \(v_1,\ldots,v_k\), having no isolated vertex in either part. Let \(t_j=\deg_H(u_j)\ge1\). Let \(T_H\) count all ordered, injective bipartition-respecting **non-induced** embeddings of \(H\) in the incidence graph \(i\sim v\) iff \(v\in A_i\). Assume \(\mathbb ET_H>0\). Then \(\mathbb EZ>0\), and

\[
\boxed{\frac{\operatorname{Cov}(Z,T_H)}{\mathbb EZ\,\mathbb ET_H} = \frac{1-k/n}{\prod_{j=1}^s(1-t_j/n)}-1.}
\]

In particular the normalized covariance depends on \(H\) only through its number \(k\) of right vertices and its **left-degree multiset**, and is independent of the prescribed row sizes \((r_i)\) and the number of left vertices \(m\) whenever \(\mathbb ET_H>0\).

Write \(e=\sum_j t_j=|E(H)|\). Its sign is completely classified as follows. If \(s=1\), it is zero. If \(s\ge2\) and \(e\le k\), it is strictly negative. If \(s\ge2\), \(e>k\), and \(\max_j t_j=k\), it is strictly positive. In the remaining case, \(s\ge2\), \(e>k\), and \(\max_j t_j<k\), a unique real \(n_H>k\) solves

\[
1-\prod_{j=1}^s\left(1-\frac{t_j}{n_H}\right)=\frac{k}{n_H}.
\]

For admissible integer \(n>k\), the covariance is negative for \(n<n_H\), zero for \(n=n_H\), and positive for \(n>n_H\). The negative integer interval can be empty when \(n_H\le k+1\); the theorem asserts a unique **real** transition, not necessarily a crossing between consecutive admissible integers.

**Exact square threshold.** Let \(H_d\), for integer \(d\ge2\), consist of two \(d\)-stars with the same single right-side leaf and all remaining right-side leaves distinct. Then \(k=2d-1\), \((t_1,t_2)=(d,d)\), and for \(n\ge2d\),

\[
\boxed{\frac{\operatorname{Cov}(Z,T_{H_d})}{\mathbb EZ\,\mathbb ET_{H_d}}=\frac{n-d^2}{(n-d)^2}.}
\]

Thus the sign reverses exactly at the **integer** right-universe size \(n=d^2\) (at \(d=2\), the first admissible size is precisely the zero). For \(d=3\), it is negative at sizes \(6,7,8\), zero at \(9\), and positive for all sizes at least \(10\), provided the embedding count has positive expectation.

## Assumptions and scope

The left choices are independent, but incidence indicators within each left row are sampled **without replacement**. The right-side universe has size \(n\), no row exhausts it, and each side of the motif has no isolated motif vertex. Every embedding uses distinct left targets and distinct right targets; extra incidences are allowed. In particular, the statistic is *not* the count of induced motif copies in the projected random intersection graph. Labeled motif automorphisms are counted, as they are in any ordered injection count. The condition \(\mathbb ET_H>0\) is essential for division by the expectation; it holds exactly when some injection \(\alpha:[s]\hookrightarrow[m]\) satisfies \(r_{\alpha(j)}\ge t_j\) for all \(j\). The proof is finite and exact for all parameter values described.

## Proof

For integers \(a\ge b\ge0\), set \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\). For every ordered left-side injection \(\alpha:[s]\hookrightarrow[m]\) and ordered right-side injection \(\beta:[k]\hookrightarrow[n]\), row \(\alpha(j)\) must contain its \(t_j\) prescribed distinct right labels. The chance of this is \((r_{\alpha(j)})_{\underline{t_j}}/(n)_{\underline{t_j}}\), and independence across rows yields

\[
\mathbb ET_H=(n)_{\underline k}\sum_{\alpha:[s]\hookrightarrow[m]}\prod_{j=1}^s \frac{(r_{\alpha(j)})_{\underline{t_j}}}{(n)_{\underline{t_j}}}.
\]

The vacancy probability of each fixed right label is \(q=\prod_{i=1}^m(1-r_i/n)>0\), so \(\mathbb EZ=nq\). Condition on a fixed label, say \(1\), being vacant. Then the left subsets are still **independent**, but each is a uniform \(r_i\)-subset of the other \(n-1\) right labels. Because every right vertex of \(H\) has positive degree, no embedding can use the vacant label. Consequently

\[
\mathbb E(T_H\mid 1\text{ vacant})=(n-1)_{\underline k}\sum_{\alpha:[s]\hookrightarrow[m]}\prod_{j=1}^s \frac{(r_{\alpha(j)})_{\underline{t_j}}}{(n-1)_{\underline{t_j}}}.
\]

Every summand in the conditioned sum differs from its original counterpart by the **same factor**, so the ratio of these two positive expectations equals

\[
\frac{(n-1)_{\underline k}}{(n)_{\underline k}}\prod_{j=1}^s\frac{(n)_{\underline{t_j}}}{(n-1)_{\underline{t_j}}}
=\frac{n-k}{n}\prod_{j=1}^s\frac{n}{n-t_j}.
\]

Write \(Z=\sum_{v=1}^n\mathbf 1_{\{v\text{ vacant}\}}\). By symmetry in the right labels and the conditional-expectation identity,

\[
\operatorname{Cov}(Z,T_H)=nq\left(\mathbb E(T_H\mid1\text{ vacant})-\mathbb ET_H\right).
\]

Substituting proves the covariance formula without any approximation.

For the signs put \(x=1/n\) and \(f(x)=1-\prod_j(1-t_jx)\), defined on \([0,1/k]\). The normalized covariance has the sign of \(f(x)-kx\). If \(s=1\), the requirement that no right motif vertex is isolated gives \(t_1=k\), and the expression is identically zero. For \(s\ge2\),

\[
f''(x)=-2\sum_{i<j}t_it_j\prod_{\ell\ne i,j}(1-t_\ell x)<0\quad(0<x<1/k),
\]

where the sum is positive because all \(t_i>0\) and all factors are positive on this interval. Thus \(f(x)/x\) is strictly decreasing on \((0,1/k)\), with limit \(f'(0)=e\) as \(x\downarrow0\). If \(e\le k\), strict decrease gives \(f(x)/x<k\). If \(e>k\) and some \(t_j=k\), then \(f(1/k)=1\) and strict decrease forces \(f(x)/x>k\) for every \(0<x<1/k\). If \(e>k\) but all \(t_j<k\), then \(f(1/k)=1-\prod_j(1-t_j/k)<1\), so \(f(1/k)/(1/k)<k\); the intermediate-value theorem and strict decrease yield exactly one solution \(x_H\in(0,1/k)\) of \(f(x_H)/x_H=k\). Setting \(n_H=1/x_H\) proves the direction of the signs and uniqueness.

For \(H_d\), substitute \(k=2d-1\) and \(t_1=t_2=d\) into the covariance ratio. One line of rational simplification gives \((n-d^2)/(n-d)^2\), as claimed.

## Verification

The standalone Python 3 checker `verify_incidence.py` uses integer counting, the standard-library `fractions.Fraction` and exhaustive enumeration of all row subsets for seven finite examples, including a non-homogeneous triple-row example. It computes the motif embedding count independently by traversing ordered injections and comparing the exact mixed moment to the formula; it also checks the conditional-expectation identity directly. Tested examples cover negative, zero and positive covariance and the one-left-vertex zero case. A second independent rational loop checks 638 instances of the double-star formula and its sign classification for sizes \(2\le d\le12\). The checker reports `PASS`. These finite computations are diagnostic, not the justification for the all-size theorem; the above proof covers every admissible finite model.

## Relationship to prior work

Blackburn and Gerke introduced and analyzed the standard uniform-subset random intersection-graph model, proving a connectivity threshold rather than a vacancy-versus-bipartite-motif covariance law [1]. Bloznelis, Jaworski and Kurauskas developed projected-graph assortativity and clustering, not this finite incidence-motif sign classification [2]. Karoński, Scheinerman and Singer-Cohen studied thresholds for induced subgraphs in **projected** random intersection graphs [3]; only the abstract and bibliographic material were accessible, and implicit coverage in the inaccessible body is an outstanding priority risk. The present statement concerns **non-induced embeddings in the underlying incidence bipartite graph**, with row sizes fixed independently rather than the total number of incidences fixed. Those differences are material: a global fixed-edge random graph does not satisfy the independent fixed-row conditional law used in the proof.

## Limitations

The normalization is undefined if the motif has zero expected embeddings; the theorem excludes that case. The assumption \(r_i<n\) ensures vacancy has positive expectation; when a left row exhausts the universe, \(Z\) is identically zero and the asserted normalized comparison is inapplicable. The motif must have no isolated right vertices to ensure an embedding cannot use a vacant right label. For motifs with isolated right vertices, this conditional multiplier is different. The theorem concerns **non-induced incidence embeddings**, not projected-graph induced subgraph counts, and its uniqueness is a **real-parameter** claim; an integer-size sign change is not guaranteed in every motif family. Novelty is assessed only against the accessible literature and searchable records described above, not established by an independent comprehensive historical audit.

## References

[1] S. R. Blackburn and S. Gerke, *Connectivity of the Uniform Random Intersection Graph*, arXiv:0805.2814v1, first submitted 19 May 2008. https://arxiv.org/abs/0805.2814

[2] M. Bloznelis, J. Jaworski and V. Kurauskas, *Assortativity and clustering of sparse random intersection graphs*, arXiv:1209.4675v1, 20 September 2012. https://arxiv.org/abs/1209.4675

[3] M. Karoński, E. R. Scheinerman and K. B. Singer-Cohen, *On Random Intersection Graphs: The Subgraph Problem*, *Combinatorics, Probability and Computing* **8** (1999), 131–159. https://doi.org/10.1017/S0963548398003459
