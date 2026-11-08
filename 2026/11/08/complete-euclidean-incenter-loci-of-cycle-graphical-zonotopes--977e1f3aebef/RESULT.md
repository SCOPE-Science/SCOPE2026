# Complete Euclidean incenter loci of cycle graphical zonotopes

## Finding
For each integer \(n\ge3\), write \(e_1,\ldots,e_n\) for the standard basis of \(\mathbb R^n\), with cyclic indices, and define the centered cycle graphical zonotope
\[
K_n=\sum_{i=1}^{n}\left[-\frac12(e_i-e_{i+1}),\frac12(e_i-e_{i+1})\right]
\subset H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
All Euclidean balls below are intrinsic to the \((n-1)\)-dimensional affine span \(H_n\). Its Euclidean inradius is
\[
\boxed{\rho_n=\sqrt{\frac{n}{\lfloor n^2/4\rfloor}}.}
\]
The **complete set** \(\mathcal I_n\subset H_n\) of centers of intrinsic balls of radius \(\rho_n\) contained in \(K_n\) is classified as follows.

If \(n=2k+1\) is odd, \(\mathcal I_n=\{0\}\): the Euclidean incenter is unique.

If \(n=2k\) is even, \(k\ge2\), put \(\beta_k=1-\sqrt{1-k^{-2}}\). Then
\[
\boxed{\mathcal I_{2k}=\{(y_1,\ldots,y_k,y_1,\ldots,y_k):\ \sum_{i=1}^{k}y_i=0,\quad |y_i|\le\beta_k\ \forall i\}.}
\]
Thus the full incenter locus is a scaled, diagonally embedded central hyperplane section of a \(k\)-cube, with dimension \(k-1\). Its number of vertices is exactly
\[
\boxed{f_0(\mathcal I_{2k})=
\begin{cases}
\binom{k}{k/2},&k\text{ even},\\[2pt]
k\binom{k-1}{(k-1)/2},&k\text{ odd}.
\end{cases}}
\]
For even \(k\), these vertices have all coordinates \(y_i\in\{-\beta_k,\beta_k\}\), half of each sign; for odd \(k\), exactly one coordinate is zero and the remaining coordinates have equally many positive and negative endpoints. In particular, every even cycle has infinitely many distinct optimal Euclidean ball centers, whereas every odd cycle has one.

## Assumptions and scope
The cycle has \(n\ge3\) labeled vertices, each edge has unit weight, and the generators are the displayed half-difference segments. The usual graphical zonotope \(\sum_i[e_i,e_{i+1}]\) is \(K_n+(1,\ldots,1)\), so its incenter set is translated by that vector. The metric is the standard Euclidean metric induced on \(H_n\), not a coordinate \(\ell_\infty\) metric. No generic-position restrictions are imposed, and all endpoints in the incenter inequalities are included.

## Proof
**1. An exact interval description.** Each \(x\in K_n\) is of the form \(x_i=t_i-t_{i-1}\), with cyclic \(t_i\in[-1/2,1/2]\). In particular \(\sum_i x_i=0\). Conversely, when \(\sum_i x_i=0\), the cyclic difference equations have a solution whose \(t_i\) range has length equal to the range of the partial sums \(0,x_1,x_1+x_2,\ldots,x_1+\cdots+x_{n-1}\). They admit a common shift into \([-1/2,1/2]\) exactly when that range is at most one. Every difference of two such partial sums is the sum of a consecutive cyclic block, with the block complement giving the negative. Hence
\[
K_n=\left\{x\in H_n:\left|\sum_{j\in I}x_j\right|\le1
\quad\text{for each nonempty proper cyclic interval }I\right\}.
\tag{1}
\]
This establishes sufficiency as well as necessity of the inequalities, not merely a set of supporting candidates.

**2. The inradius and all permissible centers.** For an interval \(I\) of size \(s\), its normal within \(H_n\) is \(v_I=\mathbf1_I-(s/n)\mathbf1\), with
\[
\|v_I\|_2=\sqrt{\frac{s(n-s)}n}.
\]
The zonotope is centrally symmetric. If a ball of radius \(r\) is contained at a center \(c\), the reflected ball at \(-c\) is also contained, and convexity places the centered radius-\(r\) ball inside. From (1), the largest possible centered radius is therefore the reciprocal of the largest \(\|v_I\|\), which proves the displayed \(\rho_n\). Moreover, a vector \(c\in H_n\) is a center of a maximal ball **if and only if**
\[
\left|\sum_{i\in I}c_i\right|
\le1-\sqrt{\frac{s(n-s)}{\lfloor n^2/4\rfloor}}
\quad\text{for every cyclic interval }I\text{ of size }s.
\tag{2}
\]

**3. Odd cycles.** Let \(n=2k+1\). Both lengths \(s=k\) and \(s=k+1\) maximize \(s(n-s)\), so the right side of (2) is zero for every length-\(k\) block. Subtracting the zero sums for successive length-\(k\) blocks gives \(c_i=c_{i+k}\) for all \(i\). Because \(\gcd(k,2k+1)=1\), all coordinates agree. Their total is zero, hence \(c=0\). The origin is a center by step 2, proving uniqueness.

**4. Even cycles: necessary equations and bounds.** Let \(n=2k\). All length-\(k\) block sums in (2) vanish. Subtract consecutive such sums to obtain \(c_i=c_{i+k}\). Writing \(c=(y,y)\), its zero-sum condition becomes \(\sum_{i=1}^k y_i=0\). At the two near-balanced lengths \(s=k-1\) and \(s=k+1\), a block sums to the negative or positive of one \(y_i\), respectively. Its right-hand side is exactly \(\beta_k=1-\sqrt{1-k^{-2}}\). Hence every optimal center satisfies \(|y_i|\le\beta_k\).

**5. Even cycles: these conditions suffice.** Conversely, suppose \(c=(y,y)\), \(\sum_i y_i=0\), and all \(|y_i|\le\beta_k\). Any cyclic interval of length \(s=k\pm d\), with \(0\le d\le k-1\), has a sum equal, up to sign, to the sum of \(d\) consecutive entries of \(y\). Its absolute value is at most \(d\beta_k\). The right-hand side of (2) is
\[
f_k(d)=1-\sqrt{1-d^2/k^2}.
\]
The function \(f_k\) is convex on \([0,k)\) with \(f_k(0)=0\), so for each integer \(1\le d\le k-1\),
\[
f_k(d)\ge d f_k(1)=d\beta_k.
\]
For \(d=0\), both sides are zero. Thus every interval inequality (2) holds. This proves the complete even-cycle locus without an unverified restriction to particular facets.

**6. Dimension and vertex enumeration.** The map \(y\mapsto(y,y)\) is injective. Its domain is the \((k-1)\)-dimensional central section of \([-\beta_k,\beta_k]^k\). A vertex of that section must have at least \(k-1\) coordinate bounds active, since otherwise a nonzero zero-sum perturbation supported on two slack coordinates would preserve feasibility. Conversely, every point with \(k-1\) independent active coordinate bounds is a vertex. If \(k\) is even, the zero-sum condition forces the remaining coordinate to an endpoint as well, with exactly \(k/2\) positive and \(k/2\) negative coordinates. If \(k\) is odd, the \(k-1\) endpoint coordinates must balance, and the remaining coordinate is zero. This gives the two vertex counts.

## Verification
The six analytical steps prove the classification for every admissible \(n\). The accompanying standalone `verify.py` uses only Python's standard library and checks the normalized interval-support distances, the exact ranks of the active-constraint matrices, all predicted incenter vertices, and the convexity inequality at all integers \(3\le n\le21\). It evaluates boundary inequalities to 70-digit decimal precision and uses exact rational elimination for the active-constraint ranks. Replay command: `python3 verify.py`; expected final line: `CYCLE_GRAPHICAL_ZONOTOPE_INCENTER_CHECKS_PASSED`. These finite tests corroborate but are not prerequisites for the all-dimensional argument.

## Relationship to prior work
Padrol–Pilaud–Poullot introduce and study graphical zonotopes and their deformation cones, including the four-cycle example. Elia–Kim–Supina record standard halfspace descriptions while studying equivariant Ehrhart theory. Xu studies graphical zonotope face vectors. None of those results describes the full Euclidean incenter locus of cycle graphical zonotopes.

A published mathematical finding, *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, gives the general inradius as a graph-cut minimum. That earlier theorem already yields the **radius** displayed here and is not claimed as new. It explicitly leaves the set of all inball centers unclassified. The new contribution is the complete and unexpectedly simple **center locus**, its parity dichotomy, and its exact vertex census; these cannot be deduced from the radius value alone. Another available cycle-zonotope finding concerns the one-skeleton Laplacian spectrum and does not determine inball centers.

## Limitations
The result is confined to the unit-weight graphical zonotope of a simple cycle with its specified intrinsic Euclidean embedding. It does not classify all incenter loci for arbitrary graphs, positive edge weights, or different norms. It does not assert that the incenter locus is full-dimensional in \(H_n\); for even cycles it has dimension \(k-1\), strictly less than \(2k-1\). Searches and source comparisons support provisional originality, not an independent historical-priority guarantee. Independent mathematical review has not been carried out.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first public version 2021-11-24; *Discrete & Computational Geometry* 73 (2025), 447–465. https://arxiv.org/html/2111.12422v2
2. S. Elia, D. Kim, M. Supina, *Techniques in Equivariant Ehrhart Theory*, *Annals of Combinatorics* 28 (2024), 819–870; first journal publication 2023-11-21. https://link.springer.com/article/10.1007/s00026-023-00673-z
3. Z. Xu, *Graphical Zonotopes with the Same Face Vector*, arXiv:1809.08764, first public version 2018-09-24. https://arxiv.org/html/1809.08764v1
4. *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, previously published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab
5. *Laplacian spectrum and spanning-tree complexity of cycle graphical zonotopes*, previously published mathematical finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-laplacian-spectrum-and-spanning-tree-complexity-of-cycle-graphic--8dfabf4d984d
