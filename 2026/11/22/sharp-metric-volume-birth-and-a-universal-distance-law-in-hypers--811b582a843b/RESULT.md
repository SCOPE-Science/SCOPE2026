# Sharp metric–volume birth and a universal distance law in hypersimplex vertex covers

## Finding
Let \(n\ge4\) and \(2\le k\le n-2\). In its ordinary intrinsic Euclidean metric consider the hypersimplex
\[
P_{n,k}=\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i=k\},\qquad
V_{n,k}=\{\mathbf1_I: I\subset[n],\ |I|=k\}.
\]
For \(0<\lambda\le1/2\), let \(C_\lambda=\bigcup_{v\in V_{n,k}}[\lambda v+(1-\lambda)P_{n,k}]\), the vertex-copy cover, and \(U_\lambda=P_{n,k}\setminus C_\lambda\). Put \(s=\min(k,n-k)\), \(R=\max(k,n-k)\), \(m=R+1\), and \(\lambda_0=1/m\), \(\lambda_1=1/R\). Let
\[
M_{n,k}=\begin{cases}\binom{n}{s-1},& k\ne n/2,\\2\binom{n}{s-1},&k=n/2,\end{cases}
\qquad t=m\lambda-1,
\]
and let \(A(n-1,k-1)\) be the Eulerian number counting permutations of \(n-1\) with \(k-1\) descents.

**Theorem (the entire first noncoverage phase).** The cover is exact for \(\lambda\le\lambda_0\). For every \(\lambda_0<\lambda<\lambda_1\), the closure of \(U_\lambda\) is the disjoint union of precisely \(M_{n,k}\) congruent regular \((n-1)\)-simplices of edge length \(\sqrt2\,t\). Their distinguished centers at first emergence are the barycenters of the maximal-dimensional simplex coordinate faces of \(P_{n,k}\), and they remain the **unique farthest points** from \(C_\lambda\) throughout this interval. The exact missing-volume fraction and maximum Euclidean error are
\[
\boxed{\frac{\operatorname{Vol}_{n-1}(U_\lambda)}{\operatorname{Vol}_{n-1}(P_{n,k})}
=\frac{M_{n,k}}{A(n-1,k-1)}(m\lambda-1)^{n-1}},\qquad
\boxed{d_H(P_{n,k},C_\lambda)=\sqrt{\frac{n}{n-1}}(\lambda-\lambda_0)}.
\]
If \(X\) is uniform in \(P_{n,k}\) with respect to intrinsic \((n-1)\)-volume and \(D=d(X,C_\lambda)\), then conditional on \(X\in U_\lambda\) the entire distance distribution is universal:
\[
\boxed{\mathbb P\!\left\{\frac{D}{d_H(P_{n,k},C_\lambda)}>u\ \middle|\ X\in U_\lambda\right\}=(1-u)^{n-1}\quad(0\le u\le1).}
\]
Thus the normalized conditional error is \(\operatorname{Beta}(1,n-1)\). The exposed interior interface between covered and uncovered regions has exact \((n-2)\)-area
\[
\boxed{M_{n,k}(R+1)\frac{\sqrt{n-1}}{(n-2)!}(m\lambda-1)^{n-2}}.
\]
In particular, the volume deficit is \(C^{n-2}\) but not \(C^{n-1}\) as a function of \(\lambda\) across the sharp onset \(\lambda_0\), whereas the Hausdorff error grows linearly. The volume and metric identities extend continuously to the endpoints \(\lambda_0\) and \(\lambda_1\), but the disjoint-closure assertion is made only in the open interval.

## Assumptions and scope
All dimensions and ranks are integer, \(n\ge4\), \(2\le k\le n-2\). Intrinsic volume means Hausdorff \((n-1)\)-measure on the affine hyperplane \(\sum x_i=k\), with the Euclidean norm inherited from \(\mathbb R^n\). The cover is a union of finitely many closed convex pieces, but is generally nonconvex. Boundary ties in the coverage predicate do not change volume, but are respected in the distance theorem. The full theorem concerns precisely the first parameter interval \(1/(R+1)<\lambda<1/R\), not all \(0<\lambda<1/2\).

For \(k<n/2\), each component is indexed by a subset \(H\subset[n]\) of cardinality \(k-1\), and its closure has the exact parametrization
\[
\overline{U_H}=\left\{x_i=b_i-z_i:\ z_i\ge0,\ \sum_i z_i=t\right\},\quad
b_i=\begin{cases}1&i\in H,\\ \lambda&i\notin H.\end{cases}
\]
The corresponding uncovered points satisfy \(z_i>0\) for \(i\notin H\); the other \(z_i\) can be zero. For \(k>n/2\), apply the isometry \(x\mapsto\mathbf1-x\) to the same description with rank \(n-k\). In the balanced case \(k=n/2\), both orientations occur. This specifies every component, including its boundary behavior.

## Proof
**1. Exact vertex-copy membership and the onset.** A point \(x\in P_{n,k}\) belongs to \(\lambda\mathbf1_I+(1-\lambda)P_{n,k}\) precisely when \(x_i\ge\lambda\) for \(i\in I\) and \(x_i\le1-\lambda\) for \(i\notin I\): the coordinate sum of the residual point is automatically \(k\). Since \(\lambda\le1/2\), a suitable \(k\)-subset exists if and only if at least \(k\) coordinates are at least \(\lambda\) and at most \(k\) coordinates exceed \(1-\lambda\). For \(\lambda\le1/(R+1)\), both inequalities always hold: \(k+1\) entries greater than \(1-\lambda\) would sum to more than \(k\), and at most \(k-1\) entries at least \(\lambda\) would sum to less than \(k\), using \(\lambda\le1/(k+1),1/(n-k+1)\). This exact threshold and full order-statistic criterion already appear in the cited rank–corank convexification work; they are premises, not claimed as novel here.

**2. First-phase components.** By complement symmetry it is enough to treat \(k\le n/2\). If \(k<n/2\), then \(\lambda<1/R\le1/(k+1)\), so the excess-large-coordinate obstruction is absent. The small-coordinate obstruction means at most \(k-1\) coordinates reach \(\lambda\). It cannot mean at most \(k-2\): otherwise \(\sum x_i<(k-2)+(n-k+2)\lambda\le k\), contradiction. Thus exactly the indices in a set \(H\) of size \(k-1\) reach \(\lambda\). Write their coordinates as \(1-z_i\), and all remaining coordinates as \(\lambda-z_i\), with \(z_i\ge0\). The sum constraint is exactly \(\sum z_i=(n-k+1)\lambda-1=t\). Since \(0<t<\lambda\), the low coordinates lie strictly between zero and \(\lambda\) except where \(z_i=0\), and the high ones remain above \(\lambda\). Conversely every such point with all low \(z_i>0\) is uncovered. The closures are regular simplices with vertices \(b-te_i\), whose pairwise distances are \(\sqrt2\,t\). The high/low index set is unique, so distinct closures do not meet. When \(k=n/2\), the large-coordinate obstruction gives an additional disjoint family obtained by complementing, with the same number and shape of components.

**3. Exact volume and interface.** The Gram matrix of the \(n-1\) edge vectors \(t(e_i-e_n)\) is \(t^2(I_{n-1}+\mathbf1\mathbf1^\top)\), of determinant \(nt^{2(n-1)}\). Hence each component has volume \(\sqrt n\,t^{n-1}/(n-1)!\), and each of its \(n\) facets has area \(\sqrt{n-1}\,t^{n-2}/(n-2)!\). Exactly \(m=R+1\) facets, those with a low coordinate equal to \(\lambda\), separate uncovered from covered points in the relative interior of \(P_{n,k}\); the other \(s-1\) facets are on the original cube boundary. There are \(M_{n,k}\) congruent components. The intrinsic volume of \(P_{n,k}\) is \(\sqrt n\,A(n-1,k-1)/(n-1)!\), by the Irwin–Hall density at integer level \(k\) (equivalently, slice-volume integration for a unit cube). Dividing proves the volume and interface formulas.

**4. Exact distance to the cover.** In one low-coordinate component, set \(L=[n]\setminus H\), \(|L|=m\), and \(a=\min_{i\in L}z_i\). Every covered point must raise at least one coordinate from \(L\) to at least \(\lambda\). In the sum-zero tangent hyperplane, a single coordinate displacement of at least \(a\) costs Euclidean distance at least \(\sqrt{n/(n-1)}a\), by Cauchy–Schwarz. Choose \(i\in L\) with \(z_i=a\); increase \(x_i\) by \(a\) and decrease every other coordinate by \(a/(n-1)\). The resulting point has sum \(k\), makes the selected low coordinate exactly \(\lambda\), and remains in \([0,1]^n\). Indeed, each other low coordinate satisfies \(z_j\le t-(m-1)a\), so its new value is at least \(\lambda-t+(m-1-1/(n-1))a\ge0\); for each high coordinate, \(z_j\le t-ma\), so its new value is at least \(1-t+(m-1/(n-1))a\ge\lambda\) because \(t<\lambda\le1/2\). Thus \(k\) coordinates now reach \(\lambda\) and no more than \(k\) exceed \(1-\lambda\), proving the adjusted point is covered. Its distance equals the lower bound. Consequently
\[
d(x,C_\lambda)=\sqrt{\frac n{n-1}}\min_{i\in L}z_i.
\]
Since \(\sum_i z_i=t\), this is at most \(\sqrt{n/(n-1)}t/m\), with equality if and only if all high \(z_i=0\) and all low \(z_i=t/m\). The unique maximizing point in this component has high coordinates \(1\) and low coordinates \(\lambda-t/m=1/m\), hence is independent of \(\lambda\) and is exactly the barycenter of the \(R\)-simplex face obtained by fixing the high coordinates to \(1\). Taking complements and both families when balanced proves the sharp Hausdorff formula and all maximizers.

**5. The universal conditional law.** Uniform intrinsic volume on a regular simplex corresponds to \(z/t\sim\operatorname{Dirichlet}(1,\dots,1)\). As all components have equal volume, the component label is uniform. For \(0\le u\le1\), the condition \(d(X,C_\lambda)>u\,d_H(P,C_\lambda)\) means all \(m\) selected low coordinates satisfy \(z_i>ut/m\). Subtracting \(ut/m\) from each leaves a simplex of total mass \(t(1-u)\), with volume ratio \((1-u)^{n-1}\). This proves the exact Beta law. The endpoint continuity is immediate from the formulas. The one-sided \((n-1)\)st derivative of the volume deficit is nonzero, while all lower-order derivatives vanish, establishing the stated regularity.

## Verification
`verification/check.py` is a standalone Python program (standard library only). It independently tests exact rational membership against all vertex-anchored copies on 95,682 hypersimplex lattice-grid points, reconstructs closest distances by numerical water-filling projection onto **each** homothetic vertex copy on 225 points, verifies seven exact edge-Gram determinants, checks the uniform-Dirichlet minimum law, and independently verifies the Eulerian slice-volume identity through dimension 12. It prints `HYPERSIMPLEX_FIRST_VOID_PASS` after all tests. Finite tests do not establish the general proof; Steps 1–5 do. To reproduce: `python verification/check.py` from the package root.

## Relationship to prior work
Artstein-Avidan, Falah, and Slomka's vertex-generation work introduces the covering parameter and proves general results about vertex copies. A previous exact hypersimplex rank–corank convexification calculation establishes the sharp threshold and order-statistic membership criterion, but explicitly leaves the uncovered-volume and Hausdorff-deficit problems untreated. This work uses that criterion, then derives the full first-phase Euclidean void shape, its metric depth and localization, the exact volume–metric scaling and the conditional Beta distance law. The published exact projection/Beta law for **sparse-paving base polytopes** concerns projection onto a different single convex body and does not cover the vertex-copy union here. Earlier regular-simplex deep-hole results concern simplices rather than the nonsimplicial hypersimplices \(2\le k\le n-2\). The elementary simplex-slice Eulerian volume identity is established background, not claimed novel.

## Limitations
The structural and distributional conclusions are confined to the first noncoverage interval; later regions can overlap or change combinatorial type. The exact nearest-point **distance** is established, not a unique nearest-point projection in all configurations. The source of the sharp global threshold is prior work. No independence or external validation is claimed. The possibility of unindexed equivalent results remains a priority risk.

## References
1. S. Artstein-Avidan, T. Falah, B. A. Slomka, *Boundary sums and vertex generated polytopes*, first publicly posted as arXiv:2306.15293v1 on 2023-06-27; later split into successor papers. https://arxiv.org/abs/2306.15293
2. S. Artstein-Avidan, T. Falah, B. A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1, first posted 2024-07-30. https://arxiv.org/abs/2407.20604
3. *Sharp rank–corank convexification of hypersimplex vertex sets*, published-finding corpus record c74758654390, published 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-corank-convexification-of-hypersimplex-vertex-sets--c74758654390
4. *Exact Euclidean projection and a universal Beta distance law for sparse-paving matroid polytopes*, published-finding corpus record 8d39b121255f, published 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-euclidean-projection-and-a-universal-beta-distance-law-for--8d39b121255f
5. L. Euler and classical Irwin–Hall sum-of-uniform density, used only for the standard hypersimplex volume normalization; no publication-priority claim is made for this identity.
