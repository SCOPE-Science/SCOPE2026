# A unimodular overlap simplex and invariant Euclidean damage under two hypersimplex vertex erasures

## Finding
For every integer pair \(n\ge4\), \(2\le k\le n-2\), let the standard hypersimplex be
\[
P_{n,k}=\operatorname{conv}\{\mathbf1_H:H\subseteq[n],\ |H|=k\}=\{x\in[0,1]^n:\sum_i x_i=k\}.
\]
Choose any **distinct** \(k\)-element subsets \(H,J\subset[n]\), and let \(Q_{H,J}\) be the convex hull of all hypersimplex vertices **except** \(\mathbf1_H\) and \(\mathbf1_J\). Write \(A(n-1,k-1)\) for the Eulerian number counting permutations of \(n-1\) elements with \(k-1\) descents, and use the lattice-normalized \((n-1)\)-volume
\[
\mathcal V(K)=\frac{(n-1)!}{\sqrt n}\,\operatorname{vol}_{n-1}(K)
\]
inside the affine hyperplane \(\sum_i x_i=k\), with zero assigned when the dimension drops. Then
\[
\boxed{\mathcal V(Q_{H,J})=A(n-1,k-1)-2\binom{n-2}{k-1}+\mathbf1_{\{|H\cap J|=k-1\}}.}\tag{1}
\]
This **one-unit interaction** is structural. Let \(C_H=\{x\in P_{n,k}:x(H)>k-1\}\), where \(x(H)=\sum_{i\in H}x_i\). Two such open vertex caps meet if and only if their apex vertices are adjacent in the Johnson graph, equivalently \(|H\cap J|=k-1\). In that case the closure of \(C_H\cap C_J\) is **one unimodular \((n-1)\)-simplex**, not merely a region with normalized volume one. For nonadjacent vertices the caps have disjoint interiors.

In contrast, every such pair of erasures has **exactly the same Euclidean Hausdorff damage**, independent of whether its two vertices are adjacent:
\[
\boxed{d_H(P_{n,k},Q_{H,J})=\sqrt{\frac{n}{k(n-k)}}.}\tag{2}
\]
The only farthest points of \(P_{n,k}\) from \(Q_{H,J}\) are the two deleted vertices, and each has an explicit unique closest point. Thus adjacent deletion loses one **less** lattice volume unit than nonadjacent deletion, yet both have identical worst Euclidean distance.

## Assumptions and scope
All geometry uses the canonical zero-one embedding, with its inherited Euclidean metric; no affine distortion or rescaling is tacitly allowed. A pair of erased vertices is adjacent precisely when their supports differ in one element. The coordinate-sum affine lattice has covolume \(\sqrt n\) in its Euclidean hyperplane. The definition of normalized volume in equation (1) uses this lattice, not ordinary ambient volume. Boundary intersections of closed caps may occur even when their strict interiors are disjoint; the assertion of disjointness refers to open caps.

Both ranks and coranks are at least two. This includes the boundary case \((n,k)=(4,2)\), where two nonadjacent erasures produce a lower-dimensional polytope and the normalized volume formula correctly yields zero. The full-volume value \(\mathcal V(P_{n,k})=A(n-1,k-1)\) and the one-cap volume \(\binom{n-2}{k-1}\) are classical background; they are **not** presented as new discoveries.

## Proof
**1. Two exact cutting inequalities.** Put \(D_H=\{x\in P_{n,k}:x(H)\le k-1\}\). The only hypersimplex vertex violating the displayed inequality is \(\mathbf1_H\). Every edge of the hypersimplex exchanges one selected coordinate for an unselected one, so any edge leaving \(\mathbf1_H\) ends exactly on the cutting hyperplane; cutting creates no additional fractional vertices. Consequently \(D_H=\operatorname{conv}(\operatorname{vert}P_{n,k}\setminus\{\mathbf1_H\})\), and its new face
\[
F_H=\{x\in P_{n,k}:x(H)=k-1\}\cong\Delta(k,k-1)\times\Delta(n-k,1)
\]
is the Cartesian product of two simplices, with vertices exactly the single-exchange neighbors of \(\mathbf1_H\).

Apply the second cut \(x(J)\le k-1\) to \(D_H\). It is violated by precisely the remaining vertex \(\mathbf1_J\). Original edges incident to \(\mathbf1_J\) terminate at \(x(J)=k-1\). An edge created by the first cut is contained in \(F_H\); if \(J\) is nonadjacent to \(H\), \(\mathbf1_J\notin F_H\). If it is adjacent, then \(\mathbf1_J\) is a vertex of the product \(F_H\), and each of its product-neighbors is another one-exchange neighbor of \(\mathbf1_J\), so again has \(x(J)=k-1\). Thus the second cut also introduces no fractional vertices. Therefore
\[
\boxed{Q_{H,J}=P_{n,k}\cap\{x(H)\le k-1\}\cap\{x(J)\le k-1\}.}\tag{3}
\]

**2. One cap and its volume.** For any \(H\), the cap \(C_H\) is a pyramid with apex \(\mathbf1_H\) and base \(F_H\). The base has intrinsic \((n-2)\)-volume \(\sqrt{k(n-k)}/[(k-1)!(n-k-1)!]\), and the perpendicular apex-to-base height is \(\sqrt{n/[k(n-k)]}\). Its normalized volume is therefore
\[
\mathcal V(C_H)=\binom{n-2}{k-1}.\tag{4}
\]
The full hypersimplex has lattice-normalized volume \(A(n-1,k-1)\), by its standard unit-cube slicing / Eulerian triangulation.

**3. Cap intersections and the unimodular simplex.** Let \(h=|H\cap J|\). For every \(x\in P_{n,k}\),
\[
x(H)+x(J)=x(H\cup J)+x(H\cap J)\le k+h.
\]
If \(h\le k-2\), this is at most \(2k-2\), so \(C_H\cap C_J=\varnothing\). Suppose instead \(h=k-1\). Write \(H=A\cup\{i\}\), \(J=A\cup\{j\}\), with \(|A|=k-1\), and put \(B=[n]\setminus(A\cup\{i,j\})\), of size \(n-k-1\).

For any point in the common cap closure, put \(y_a=1-x_a\) for \(a\in A\), \(d=\sum_{a\in A}y_a\), \(u=x_i-d\), \(v=x_j-d\), and \(z_b=x_b\) for \(b\in B\). The two cap inequalities say \(u,v\ge0\); the cube and sum constraints give exactly
\[
 y_a,u,v,z_b\ge0,\qquad \sum_{a\in A}y_a+u+v+\sum_{b\in B}z_b=1.\tag{5}
\]
Conversely every such standard-simplex coordinate tuple yields a point of the common cap closure via \(x_a=1-y_a\), \(x_i=d+u\), \(x_j=d+v\), and \(x_b=z_b\), satisfying all cube constraints automatically. The transformation and its inverse use integer-affine coordinates on the coordinate-sum lattice, so it is **unimodular**. Equivalently, the common-cap closure is the simplex with the following \(n\) vertices:
\[
\mathbf1_H,\ \mathbf1_J,\quad
\{\mathbf1_{(A\setminus\{a\})\cup\{i,j\}}:a\in A\},\quad
\{\mathbf1_{A\cup\{b\}}:b\in B\}.
\]
These vertices are affinely independent, and the simplex has normalized volume exactly \(1\).

**4. Two-cap volume.** By equation (3), the region removed from \(P_{n,k}\) is exactly \(C_H\cup C_J\), modulo boundary sets of zero volume. Inclusion-exclusion using equation (4), the absence of overlap for nonadjacent vertices, and the unit-simplex overlap for adjacent vertices proves equation (1).

**5. Euclidean damage and all maximizers.** For a deleted vertex \(v_H=\mathbf1_H\), the orthogonal foot onto \(x(H)=k-1\) inside \(\sum_i x_i=k\) is
\[
(y_H)_a=\begin{cases}1-1/k,&a\in H,\\1/(n-k),&a\notin H.\end{cases}\tag{6}
\]
Its squared distance from \(v_H\) is \(1/k+1/(n-k)=n/[k(n-k)]\), and it lies in the cube. To check the other cut, write \(t=|H\setminus J|\ge1\). Directly,
\[
 y_H(J)=k-1-t\left(1-\frac1k-\frac1{n-k}\right)\le k-1,
\]
since \(1/k+1/(n-k)\le1\) in the specified rank/corank range. Thus \(y_H\in Q_{H,J}\) by equation (3). As \(Q_{H,J}\) lies in the supporting halfspace \(x(H)\le k-1\), the orthogonal lower bound is attained: \(y_H\) is the **unique nearest point** of \(v_H\) in \(Q_{H,J}\). The same argument holds for the deleted vertex \(v_J\).

Every other vertex of \(P_{n,k}\) belongs to \(Q_{H,J}\) and has distance zero. Distance to a convex set is convex, so no point of \(P_{n,k}\) can exceed the common deleted-vertex distance; this proves equation (2). In fact the farthest points are precisely \(v_H,v_J\): any convex combination with a retained vertex has strictly lower distance by the triangle inequality, and on the open segment between \(v_H,v_J\) the distinct equal-length outward residual vectors \(v_H-y_H\) and \(v_J-y_J\) have a strict convex-combination norm deficit. This establishes the equality classification. \(\square\)

## Verification
The standalone script `verify_two_erasure.py` (Python 3 with NumPy, SciPy and SymPy) constructs the genuine retained-vertex convex hull, evaluates its intrinsic normalized volume independently by SciPy's convex-hull algorithm, and compares it with equation (1) for **all feasible ranks and all possible vertex-intersection types** at \(4\le n\le8\). It checks the proposed orthogonal-foot vectors and their distances, then forms the stated common-cap simplices and checks 28 unimodular determinants **exactly** with integer arithmetic for \(4\le n\le10\). The completed run printed `PASS` for **37** rank/intersection profiles and **28** exact determinant tests. These finite checks do not establish unrestricted \(n,k\); Steps 1–5 prove those quantifiers.

To reproduce, run `python verify_two_erasure.py` in a Python environment with the named dependencies. The entire argument is self-contained except for the classical Eulerian hypersimplex-volume identity, explicitly cited below.

## Relationship to prior work
Yi's 2026 study of maximal isosceles sets singles out the regular-simplex edge-midpoint configurations (the rank-two Johnson configurations) as the unique extremal examples in a range of dimensions; it does not compute their erasure volume/Euclidean damage. The theorem above investigates this natural robustness question for **all** hypersimplex ranks, not just those extremal examples.

For nonadjacent forbidden bases, their pair forms the missing-base set of a sparse-paving matroid. Earlier matroid valuations, particularly Ferroni–Schröter's sparse-paving volume formula, **already give the additive volume term** in equation (1). A prior exact projection theorem for sparse-paving matroid polytopes likewise gives the nonadjacent Hausdorff value. These are acknowledged as **known cases**, not claimed as new. In contrast, adjacent forbidden bases cannot be the only nonbases of a matroid because circuit elimination forces more; the two cap interiors now overlap, and the explicit **single unimodular overlap simplex** accounts for the sharp unit correction. The same metric plateau in this nonmatroid case is proved in Step 5.

Lam and Postnikov's general alcoved-polytope triangulation and volume enumeration is broader algorithmic background and can be applied after suitable coordinate reordering to both two-cut polytopes. The present claim is not a new general ability to calculate alcoved volumes: it is the **direct local geometric identification of the incident-cap overlap as exactly one unimodular simplex**, together with the complete adjacent-versus-nonadjacent comparison and the equality cases of the Euclidean Hausdorff metric. No inspected source states that combined structural result. Historical priority remains provisional.

## Limitations
The theorem concerns exactly **two** erased vertices and the canonical standard Euclidean/lattice normalization. It makes no claim for three or more erasures, weighted or affine-distorted hypersimplices, other convex bodies, or continuous-point deletion. The nonadjacent/matroid volume and metric special cases, and the general alcoved enumeration, are existing mathematical knowledge; the structural two-cap interaction is the claimed new element. Finite tests cannot prove the universal formula and no independent mathematical audit or exhaustive historical priority certification has been performed.

## References
1. H. Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421, first publicly submitted 2026-11-02, especially Theorem 1.1 and the Johnson configuration in the introduction. https://arxiv.org/abs/2611.05421
2. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, arXiv:2208.04893 (2022), Section 6, especially Corollary 6.7 and the classical Eulerian hypersimplex volume. https://arxiv.org/abs/2208.04893
3. T. Lam and A. Postnikov, *Alcoved Polytopes I*, arXiv:math/0501246 (2005), Section 3 and Theorem 3.2. https://arxiv.org/abs/math/0501246
4. *Exact Euclidean projection and a universal beta distance law for sparse-paving matroid polytopes*, public mathematical research result, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-euclidean-projection-and-a-universal-beta-distance-law-for--8d39b121255f
5. *Exact facial-distance spectrum and a quarter-density transition for hypersimplices*, public mathematical research result, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-facial-distance-spectrum-and-a-quarter-density-transition--6a44089f2869
