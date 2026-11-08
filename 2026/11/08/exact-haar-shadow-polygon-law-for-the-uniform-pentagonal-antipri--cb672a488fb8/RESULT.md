# Exact Haar shadow polygon law for the uniform pentagonal antiprism

## Finding

Let \(P\subset\mathbb R^3\) be the convex hull of the ten points
\[
(\cos(2\pi j/5),\sin(2\pi j/5),1/2),\quad
(\cos(2\pi j/5+\pi/5),\sin(2\pi j/5+\pi/5),-1/2),
\qquad j=0,1,2,3,4.
\]
This is the uniform pentagonal antiprism: two regular pentagonal bases and ten equilateral lateral triangles. Let \(U\) be uniform on the unit sphere and \(N(U)\) the number of vertices of the orthogonal projection of \(P\) to \(U^\perp\). Put
\[
\begin{gathered}
A=\arccos(-1/3),\quad B=\arccos(-\sqrt5/3),\quad
D=\arccos(1/3),\quad E=\arccos(\sqrt5/3),\\
\delta=(3-\sqrt5)/4,\qquad C=\arccos\!\left(\frac{\delta}{\sqrt{1+\delta^2}}\right).
\end{gathered}
\]
Then, except for a measure-zero family of viewing directions, \(N(U)\) is \(6\), \(8\), or \(10\), with the **complete exact law**
\[
\begin{aligned}
\Pr[N=6]&=\frac{5}{2\pi}(A+2B-2C-\pi)
&&\approx0.659378121806623,\\
\Pr[N=8]&=\frac5\pi(C+D+E-\pi)
&&\approx0.320188258269895,\\
\Pr[N=10]&=\frac{5A-3\pi}{2\pi}
&&\approx0.020433619923482.
\end{aligned}
\]
The exact orientation partition comprises ten pentagonal cells producing hexagons, twenty triangular cells producing octagons, and two pentagonal cells producing decagons. In particular, a decagonal shadow occurs with probability just over two percent. The expected silhouette size is \(6.722110996233718\ldots\); the new information is the entire distribution, not that expectation alone.

## Assumptions and scope

A generic direction has nonzero dot product with each of the antiprism's twelve facet normals. All generic projections are convex polygons and their sides are precisely the edges separating an outward-facing from an inward-facing facet. Non-generic directions lie on six great circles and have spherical area zero. Viewing directions \(U\) and \(-U\) give the same projected polygon. This is an orthogonal, not perspective, projection and the probability measure on directions is rotation invariant (Haar).

The base circumradius is one and the base half-separation is \(1/2\); this height makes the lateral triangles equilateral. The result is not asserted for other heights, nonuniform viewing distributions, or nonconvex meshes.

## Proof

**1. Normal fan and silhouette edge counting.** The outward unit directions, up to a common positive factor on lateral normals, consist of the top and bottom normals \(\pm e_3\), and ten lateral normals
\[
n_j=(\cos(j\pi/5),\sin(j\pi/5),(-1)^{j+1}\delta),\quad 0\le j<10.
\]
Indeed, the lateral facet through two successive vertices of one base and the intervening vertex of the opposite base has horizontal outward normal pointing at angle \(j\pi/5\), with alternating vertical slope \(\pm\delta\). Since \(n_{j+5}=-n_j\), there are six unoriented normal axes. For generic \(U\), record the six signs of the top-normal dot product and the first five lateral-normal dot products. The remaining six facet signs are their opposites.

There are twenty edges: ten between consecutive lateral triangular facets, five between an odd-indexed lateral facet and the top base, and five between an even-indexed lateral facet and the bottom base. Thus if \(t=\operatorname{sgn}\langle U,e_3\rangle\) and \(s_j=\operatorname{sgn}\langle U,n_j\rangle\) (indices modulo ten, with \(s_{j+5}=-s_j\)), the projected silhouette has exactly
\[
N(U)=\sum_{j=0}^9[s_j\ne s_{j+1}]
+\sum_{j\ \mathrm{odd}}[s_j\ne t]
+\sum_{j\ \mathrm{even}}[s_j\ne -t].
\]
The standard convex-polyhedron silhouette-edge criterion supplies the equality: every sign-changing edge is an exposed boundary edge in the orthogonal projection, and genericity prevents collinear projected adjacent edges. The included checker independently reconstructs the convex hull of the projected vertices to cross-check this incidence count.

**2. Exact chamber enumeration.** Each sign changes only on a great circle orthogonal to one of the six normal axes. Let \(\varphi=(1+\sqrt5)/2\), so \(2\delta=2-\varphi\). Applying the same positive diagonal change of coordinates \(\operatorname{diag}(2,2/\sin(\pi/5),2)\) to the lateral normals gives algebraic axis representatives
\[
\begin{array}{c|ccc}
 i&H_{i,x}&H_{i,y}&H_{i,z}\\ \hline
0&0&0&1\\
1&2&0&\varphi-2\\
2&\varphi&2&2-\varphi\\
3&\varphi-1&2\varphi&\varphi-2\\
4&1-\varphi&2\varphi&2-\varphi\\
5&-\varphi&2&\varphi-2
\end{array}
\]
where the top normal is merely rescaled by a positive number. This common invertible transformation preserves the sign-feasibility combinatorics, though not spherical angles; the latter are computed from the original physical normals.

For \(b=(b_0,\dots,b_5)\in\{-1,+1\}^6\), let the open chamber be \(b_i\langle U,H_i\rangle>0\) for all \(i\), using the corresponding dual transformed direction. The six bounding great circles have no triple intersections. A vertex of a chamber is therefore one of the 30 directed rays \(\pm(H_i\times H_j)\) for \(i<j\); such a ray is in the chamber closure precisely when all six weak sign inequalities hold. All signs can be decided exactly in \(\mathbb Z[\varphi]\) because \(\varphi^2=\varphi+1\).

The following table is the **exhaustive** result of testing all 64 masks against all 30 directed rays, counting silhouette edges by the preceding formula, and calculating the spherical interior angles of the resulting chambers from the *untransformed* normals. A mask has digit \(1\) for a positive sign, with digit \(0\) for a negative sign, ordered \(b_0\) through \(b_5\). In the angle patterns, \(P\) abbreviates \(\pi-C\).

| Shadow vertices | Number of cells | Chamber corners and angle multiset | All feasible bit masks |
| :--: | :--: | :-- | :-- |
| \(6\) | \(10\) | Pentagons: \(A,B,B,P,P\) | `000001 000111 010000 011100 011111 100000 100011 101111 111000 111110` |
| \(8\) | \(10\) | Triangles: \(C,C,E\) | `000000 000011 001111 011000 011110 100001 100111 110000 111100 111111` |
| \(8\) | \(10\) | Triangles: \(D,D,E\) | `000101 010001 010100 010111 011101 100010 101000 101011 101110 111010` |
| \(10\) | \(2\) | Pentagons: \(A,A,A,A,A\) | `010101 101010` |

For clarity, the angle at the intersection of active facet-normal great circles indexed by \(i,j\) has cosine \(-b_i b_j\langle \hat n_i,\hat n_j\rangle\), where \(\hat n_i\) are the original normalized outward axes (the first five lateral normals and top). Direct dot products yield only the angle types \(A,B,C,\pi-C,D,E\) above. A reproducible exact-integer implementation of the mask and angle tests is in `verify_pentagonal_antiprism.py` (part of this package). It tests every possible cell, not a random subset. The 32 positive-area chambers exhaust the sphere, also agreeing with the standard count \(m^2-m+2=32\) for six great circles in general position.

**3. Areas and probabilities.** Girard's formula gives the areas of the four types of spherical cells, respectively,
\[
\begin{aligned}
a_6&=A+2B+2(\pi-C)-3\pi=A+2B-2C-\pi,\\
a_{8,1}&=2C+E-\pi,\qquad a_{8,2}=2D+E-\pi,\\
a_{10}&=5A-3\pi.
\end{aligned}
\]
All are positive. The ten plus twenty plus two cells form a partition of the unit sphere outside boundaries, so the probabilities are \(10a_6/(4\pi)\), \(10(a_{8,1}+a_{8,2})/(4\pi)\), and \(2a_{10}/(4\pi)\). Simplification yields the stated exact law. Their sum equals one, as also follows directly from the chamber partition. This proves the result for almost every orientation.

## Verification

Run `python3 verify_pentagonal_antiprism.py` using a Python 3 interpreter; the script requires **only the standard library**. The exact \(\mathbb Z[\varphi]\) implementation checks pairwise great-circle intersections, absence of triple concurrence, every one of the 64 possible six-bit sign patterns and all 30 directed intersection rays, the complete 32-cell mask table, all 20 edge-incidence counts, and the four spherical-angle signatures. It then confirms the exact-formula probabilities numerically sum to one and are positive. Independently, it projects the actual ten antiprism vertices along 10,000 seeded isotropic viewing directions, constructs their planar convex hull by a monotone-chain algorithm, and verifies the resulting number of vertices agrees with the face-sign formula for every tested direction. On execution, success lines include `EXACT_PENTAGONAL_ANTIPRISM_CHAMBERS_OK` and `PENTAGONAL_ANTIPRISM_SILHOUETTE_OK` and `INDEPENDENT_PROJECTED_HULL_CROSSCHECK_OK`.

Exhaustivity of the finite mask checking follows from the proof that the six great circles have no triple intersection and the chamber-vertex test is sufficient; simulation by itself would not prove an all-orientation statement. The analytical dot-product and Girard identities, together with the exhaustive algebraic chamber test, establish the continuous probability law.

## Relationship to prior work

Glisse and Lazard (2007) give upper bounds on average silhouette complexity for broad classes of polyhedra, including a careful definition using front/back facet signs, but not the fixed antiprism's exact polygon-type probabilities. Glisse, Lazard, Michel, and Pouget (2016) study silhouettes of random spherical-sample polytopes and their maximum complexity, not this deterministic uniform antiprism under random orientation. Kettner and Welzl (1997) analyze polyhedral contour-edge expectations and experiments for general models; the complete original manuscript was not accessible in this comparison, which leaves a specific historical-priority risk.

An existing exact formula for the **expected** number of random shadow edges of every regular antiprism specializes to the mean \(6.722110996233718\ldots\) here. It is consistent with the present result, but one mean cannot determine three positive probabilities. Also, a published exact central-section law for the *regular icosahedron* treats a different solid and statistic; it does not supply this pentagonal-antiprism projection law. The distinctive contribution is the 32-chamber incidence classification and all three exact probabilities, including the rare decagonal probability.

## Limitations

All probabilities are conditional on the exact specified uniform antiprism geometry and uniform orientation; the theorem does not classify silhouettes at the measure-zero great-circle boundaries, offset perspective views, arbitrary antiprism heights, or mesh perturbations. The proof uses a finite exhaustive algebraic certificate with source included; it does not rely on random simulation to claim exhaustiveness. The literature search cannot rule out an unindexed earlier calculation, and the complete Kettner–Welzl 1997 article was not inspected. The mean silhouette identity is previously known and is not asserted as new. No independent scholarly review has yet been performed.

## References

1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, first posted February 14, 2007, https://arxiv.org/abs/cs/0702087.
2. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a Random Polytope*, Journal of Computational Geometry **7** (2016), 86–99, DOI:10.20382/jocg.v7i1a5, https://jocg.org/index.php/jocg/article/view/3009.
3. L. Kettner and E. Welzl, *Contour Edge Analysis for Polyhedron Projections*, in *Geometric Modeling: Theory and Practice* (1997), 379–394, DOI:10.1007/978-3-642-60607-6_25.
