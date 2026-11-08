# Makai–flag equality rigidity and sharp polygon-factor gaps in Cartesian products

## Finding

Let \(k\ge1\) and let \(Q_1,\ldots,Q_k\) be arbitrary nondegenerate convex polygons, with \(n_j\ge3\) vertices. Put \(P=Q_1\times\cdots\times Q_k\subset\mathbb R^{2k}\). Let \(\mathcal F(P)\) count complete face-flags, and let \(\mathcal M(P)=\operatorname{vol}(P)\operatorname{vol}((P-P)^\circ)\). Define the dimensionless flag-normalized Makai ratio
\[
\mathcal R(P)=\frac{((2k)!)^2}{\mathcal F(P)}\,\mathcal M(P).
\]
**Exact tensorization and equality classification:**
\[
\boxed{\mathcal R(P)=\prod_{j=1}^{k}\frac{2\,\operatorname{area}(Q_j)\operatorname{area}((Q_j-Q_j)^\circ)}{n_j}.}
\]
In particular, \(\mathcal R(P)\le1\), with equality **if and only if every factor is a triangle or parallelogram**. This settles equality in the Makai–flag inequality on the entire Cartesian-product class of planar polygons (without imposing central symmetry).

If at least \(r\ge1\) factors have \(n_j\ge5\), then the uniform strictly separated bound is
\[
\mathcal R(P)<\left(\frac{\pi^2}{10}\right)^r.
\]
For the subclass in which every factor is centrally symmetric (hence \(n_j\) is even), a **sharp fixed-combinatorial-type envelope** holds:
\[
\boxed{\mathcal R(P)\le\prod_{j=1}^{k}\left[\frac{n_j}{2}\sin^2\left(\frac{\pi}{n_j}\right)\right],}
\]
with equality precisely when all factors are affine images of regular \(n_j\)-gons. Consequently, if exactly \(r\) centrally symmetric factors have at least six vertices and the remaining factors have four, \(\mathcal R(P)\le(3/4)^r\), sharply attained by products of affine-regular hexagons and parallelograms.

## Assumptions and scope

All polygons are compact, full-dimensional in their own Euclidean planes, and have distinct genuine vertices (no redundant collinear subdivisions). Products use the orthogonal direct-sum coordinate identification; all formulas are affine-invariant and therefore apply to arbitrary affine product embeddings. The polar of \(P-P\) is taken at its origin, which lies in its interior. A complete flag means one vertex, one edge, and exactly one face of every successive dimension up to the polytope. The classification concerns **only products of polygons**, not arbitrary polytopes of dimension \(2k\). The first displayed strict estimate assumes \(r\ge1\); if \(r=0\), the equality classification is the appropriate statement.

## Proof

**1. Product polar volume.** More generally, for convex bodies \(A_j\subset\mathbb R^{d_j}\) containing the origin in their interiors, let \(D=\sum_jd_j\). Since
\[
\left(\prod_j A_j\right)^\circ=\left\{(y_j):\sum_j h_{A_j}(y_j)\le1\right\},
\]
and \(\operatorname{vol}_{d_j}\{y_j:h_{A_j}(y_j)\le t\}=t^{d_j}\operatorname{vol}_{d_j}(A_j^\circ)\), repeated layer-cake integration (equivalently the Dirichlet simplex integral) gives
\[
\operatorname{vol}_D\left(\left(\prod_j A_j\right)^\circ\right)
=\frac{\prod_jd_j!}{D!}\prod_j\operatorname{vol}_{d_j}(A_j^\circ).
\]
Take \(A_j=Q_j-Q_j\), for which \(P-P=\prod_jA_j\); multiplying by \(\operatorname{vol}_{D}(P)=\prod_j\operatorname{area}(Q_j)\) yields \(\mathcal M(P)=(2!)^k\prod_j\mathcal M(Q_j)/(2k)!\).

**2. Flag count.** A complete product flag is uniquely a collection of factor flags plus an interleaving of their dimension-raising steps. The number of interleavings is \(D!/\prod_jd_j!\). Every \(n_j\)-gon has exactly \(2n_j\) complete flags. Consequently
\[
\mathcal F(P)=\frac{(2k)!}{(2!)^k}\prod_j(2n_j)=(2k)!\prod_jn_j.
\]
Combining the two identities proves the exact tensorization formula.

**3. Triangle and quadrilateral factors.** Affine invariance reduces a triangle to \(\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), for which direct polarity gives \(\mathcal M(Q)=3/2\), and hence \(\mathcal R(Q)=1\).

For an arbitrary convex quadrilateral, move the diagonal intersection to the origin and use an invertible affine transformation to set the cyclic vertices to
\[
(1,0),\quad(0,1),\quad(-p,0),\quad(0,-q),\qquad p\ge q\ge1.
\]
The inequalities \(p\ge q\ge1\) are achieved by choosing the shorter arm of each diagonal as the positive unit and then swapping the two coordinate axes. Put \(H=(p+1,0)\), \(V=(0,q+1)\), \(C=(p,1)\), \(D=(p,-q)\). The six positive representatives of vertex differences are \(H,V,C,D,(1,q),(1,-1)\). The last two are redundant: \((1,q)=C/p+(pq-1)V/[p(q+1)]\) and \((1,-1)=D/p+(p-q)(-V)/[p(q+1)]\), with nonnegative coefficients summing to at most one. Thus
\[
Q-Q=\operatorname{conv}\{\pm H,\pm V,\pm C,\pm D\}.
\]
Writing \(X=(p+1)x\), \(Y=(q+1)y\), the polar is the square \(|X|,|Y|\le1\) clipped by
\[
\left|\frac{pX}{p+1}+\frac{Y}{q+1}\right|\le1,\qquad
\left|\frac{pX}{p+1}-\frac{qY}{q+1}\right|\le1.
\]
The former pair removes two disjoint triangles, each of area \((p-q)^2/[2p(p+1)(q+1)]\); the latter removes two further triangles, each of area \((pq-1)^2/[2pq(p+1)(q+1)]\). Since \(\operatorname{area}(Q)=(p+1)(q+1)/2\), this gives
\[
\boxed{\mathcal M(Q)=2-\frac{q(p-q)^2+(pq-1)^2}{2pq(p+1)(q+1)}.}
\]
Both squared terms vanish exactly when \(p=q=1\), i.e. precisely for parallelograms. Hence \(\mathcal R(Q)=\mathcal M(Q)/2\le1\), with equality only for parallelograms. This planar quadrilateral profile is *not* claimed as a new standalone result.

**4. Five or more vertices.** Set \(C=Q-Q\). The planar Brunn–Minkowski inequality gives \(\operatorname{area}(C)\ge4\operatorname{area}(Q)\). Because \(C\) is centrally symmetric, the planar Blaschke–Santaló inequality gives \(\operatorname{area}(C)\operatorname{area}(C^\circ)\le\pi^2\). Thus \(\mathcal M(Q)\le\pi^2/4\) and, for \(n\ge5\),
\[
\mathcal R(Q)=\frac{2\mathcal M(Q)}n\le\frac{\pi^2}{2n}\le\frac{\pi^2}{10}<1.
\]
The strict product separation and full equality classification now follow from factorization and steps 3–4.

**5. Sharp centrally symmetric envelope.** For a centrally symmetric \(n\)-gon, \(Q-Q=2(Q-c)\) after centering at \(c\), so \(\mathcal R(Q)=\operatorname{area}(Q)\operatorname{area}((Q-c)^\circ)/(2n)\). The sharp planar volume-product theorem of Meyer and Reisner, also proved in Alexander–Fradelizi–Zvavitch, says
\[
\operatorname{area}(Q)\operatorname{area}((Q-c)^\circ)\le n^2\sin^2(\pi/n),
\]
with equality exactly for affine-regular \(n\)-gons. Multiplication proves the fixed-side-count envelope and its equality characterization. The factor \(f(x)=\tfrac{x}{2}\sin^2(\pi/x)\) decreases strictly for \(x\ge4\), since, putting \(t=\pi/x\in(0,\pi/4]\), its derivative has the sign of \(\tan t-2t<0\). Indeed \(\tan t/t\) increases on this interval and never reaches \(2\) (its endpoint value is \(4/\pi<2\)). Finally \(f(4)=1\) and \(f(6)=3/4\), proving the final sharp power bound.

## Verification

The self-contained standard-library program `verify.py` independently performs exact rational half-plane clipping of planar difference-body polars. It compares all tested quadrilateral ratios to the displayed closed formula, checks the triangle/parallelogram/affine-regular-hexagon witnesses, tests exact four-dimensional product flag–beta identities, and checks monotonicity numerically over a broad finite range of even side counts. Run `python verify.py`; its expected output for this package is `MAKAI_POLYGON_PRODUCT_OK 142`. These finite checks are supplementary; the universal identities and inequalities are analytic.

In dimension four, two affine-regular hexagonal factors yield \(\mathcal R=9/16\), while one parallelogram and one affine-regular hexagon yield \(\mathcal R=3/4\). Two parallelograms or two triangles yield \(\mathcal R=1\), in agreement with the classification.

## Relationship to prior work

Winter (arXiv:2610.09990; first public 2026-10-07) proves \(\mathcal R(P)\le1\) for arbitrary polytopes and explicitly leaves the equality classification open. The present claim gives an exact product factorization, an equality classification on all polygon products, and a sharp fixed-even-side-count upper envelope. It does not assert a general solution to Winter's equality conjecture.

The planar regular-polygon volume-product maximum with unique affine equality is the theorem of Meyer–Reisner (2011), with a complete proof in Alexander–Fradelizi–Zvavitch (arXiv:1708.07914, Theorem 4.1). This planar theorem, standard Brunn–Minkowski and Blaschke–Santaló inequalities, and the known planar quadrilateral computation are prior ingredients rather than new conclusions. The new structural content is their exact joint consequence for all Cartesian products and the dimension-independent gap depending on the number of nontrivial factors. A publicly indexed quadrilateral Makai-profile record independently covers the single-factor quadrilateral case; nothing is claimed new about that one case.

## Limitations

The equality characterization covers Cartesian products of full-dimensional **polygons** only, not polytopes with irreducible higher-dimensional factors. The factor \(\pi^2/10\) is a convenient universal separation for arbitrary factors with at least five vertices, not claimed optimal. The fixed-combinatorial-type envelope is sharp only under the stated central-symmetry hypothesis. No independent external audit has been performed, and an exhaustive historical-priority determination is not asserted. The full text of one relevant publicly indexed quadrilateral-profile record could not be accessed; its announced single-factor result is fully acknowledged, and the quadrilateral step is independently reconstructed here.

## References

1. M. Winter, *A relation between Mahler volume and flag number for convex polytopes*, arXiv:2610.09990 (first publicly posted 2026-10-07), https://arxiv.org/abs/2610.09990.
2. M. Alexander, M. Fradelizi, A. Zvavitch, *Polytopes of Maximal Volume Product*, arXiv:1708.07914 (2017), Section 4 and Theorem 4.1, https://arxiv.org/abs/1708.07914.
3. M. Meyer and S. Reisner, *On the volume product of polygons*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 81 (2011), 93–100, DOI:10.1007/s12188-011-0054-3.
4. Classical Brunn–Minkowski inequality; planar Blaschke–Santaló inequality. See the convex-geometry references in [2].
