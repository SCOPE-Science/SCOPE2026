# Multipartite stable-set polytopes: universal ridge curvature and exact five-partite cancellation

## Finding

Let \(k\ge3\), let \(n_1,\ldots,n_k\) be positive integers, and assume at least two of them exceed one. Set \(N=\sum_i n_i\), \(Q=\prod_i n_i\), and \(s=|\{i:n_i=1\}|\). Let \(G=K_{n_1,\ldots,n_k}\) be the complete multipartite graph. Its canonical stable-set polytope \(P\subset\mathbb R^N\) is the convex hull of indicator vectors of stable vertex sets, with the **standard coordinate Euclidean metric**. Write \(H\) for \((N-2)\)-dimensional Hausdorff measure on the ridges, and put

\[
 C=\frac{\prod_{i=1}^k n_i!}{(N-2)!}.
\]

Every ridge has one of three interior dihedral angles, with the following *total ridge measures*:

| Interior angle | Total \(H\)-measure of all ridges in this class |
|---|---|
| \(\pi/2\) | \(C\bigl((k^2-s)/2+(k-s)\sqrt{k}\bigr)\) |
| \(\alpha_k=\arccos(1/\sqrt{k})\) | \(Cs\sqrt{k-1}\) |
| \(\beta_k=\pi-\arccos((k-1)/k)\) | \(C(k-s)\sqrt{2k-1}/2\) |

A class has zero total measure precisely when its displayed coefficient vanishes. The corresponding **numbers of ridges** are respectively

\[
 \binom{N}{2}+Q(N-k),\qquad sQ,\qquad \frac{Q(N-k)}2.
\]

Thus all three area totals, divided by \(C\), depend only on the number of parts \(k\) and on their singleton count \(s\), independently of the sizes of the nonsingleton parts. Their area-weighted interior mean is

\[
 \frac\pi2+\frac{(k-s)\sqrt{2k-1}\,\arcsin((k-1)/k)/2-s\sqrt{k-1}\,\arcsin(1/\sqrt{k})}{(k^2-s)/2+(k-s)\sqrt{k}+s\sqrt{k-1}+(k-s)\sqrt{2k-1}/2}.
\]

In particular, take \(k=5\) and \((n_1,\ldots,n_5)=(1,1,1,p,q)\) with **arbitrary integers \(p,q\ge2\)**. Then the total measures of right, acute, and obtuse ridges are

\[
 (11+2\sqrt5)C,\qquad6C,\qquad3C,
 \quad C=\frac{p!q!}{(p+q+1)!}.
\]

The acute angle is \(\pi/2-\arctan(1/2)\), the obtuse angle is \(\pi/2+2\arctan(1/2)\), and therefore the area-weighted mean is **exactly \(\pi/2\)** for every \(p,q\ge2\), although positive area occurs in both non-right classes. With the Euclidean Steiner convention, the codimension-two intrinsic volume is

\[
 V_{N-2}(P)=\left(5+\frac{\sqrt5}{2}\right)\frac{p!q!}{(p+q+1)!}
 =N(N-1)\left(5+\frac{\sqrt5}{2}\right)V_N(P).
\]

## Assumptions and scope

Every part is nonempty, \(k\ge3\), and at least two parts have size at least two. The stronger formulas above also hold when fewer parts are nonsingleton; those boundary cases are included to make the structural formula complete, but are not treated as an independently new contribution. \(H\) denotes intrinsic Euclidean ridge measure in the standard \(0/1\) coordinate embedding, **not** a normalized lattice measure. All statements count ridges as distinct faces, without multiplicity from alternative inequality presentations. \(V_j\) are Euclidean intrinsic volumes normalized by

\[
 \operatorname{vol}_N(P+tB_N)=\sum_{j=0}^N\kappa_{N-j}V_j(P)t^{N-j}.
\]

## Proof

**1. Facets and volume.** Write the coordinates in block \(i\) as \(x_{i,a}\), \(1\le a\le n_i\). Since a complete multipartite graph is perfect, its stable-set polytope is exactly

\[
 x_{i,a}\ge0,\qquad \sum_{i=1}^k x_{i,a_i}\le1
 \quad (a_i\in\{1,\ldots,n_i\}).
\]

Each listed inequality supports a facet: for a coordinate lower bound, take that coordinate zero and all other coordinates small positive; for any upper inequality, choose positive selected coordinates whose sum equals one and put every unselected coordinate strictly between zero and the selected coordinate in its block. Hence there are \(N\) coordinate facets \(L_{i,a}\) and \(Q\) clique facets \(U_{a_1,\ldots,a_k}\).

For \(t_i=\max_a x_{i,a}\), the polytope is equivalently \(x\ge0\) with \(\sum_i t_i\le1\). Integrating the independent cube-block maxima gives

\[
 V_N(P)=\int_{\sum t_i\le1}\prod_i n_i t_i^{n_i-1}\,dt
 =\frac{\prod_i n_i!}{N!}.
\]

**2. Exactly which pairs are ridges.** Every pair of coordinate facets meets in codimension two: make their coordinates zero and all remaining coordinates small positive. For a lower facet \(L_{i,a}\) and an upper facet \(U_{b_1,\ldots,b_k}\), if \(a\ne b_i\), one may take the chosen upper coordinates to be strict block maxima while setting the unchosen coordinate to zero; this is a ridge. If \(a=b_i\) and \(n_i=1\), set that singleton coordinate to zero, choose strict positive maxima in all other blocks summing to one, and again obtain a ridge. Conversely, if \(a=b_i\) and \(n_i>1\), saturation of the upper inequality with \(x_{i,a}=0\) forces **every** coordinate in block \(i\) to vanish (replace the selected index in that inequality). Thus there are at least three linearly independent active supporting equalities, so no ridge.

For two distinct upper facets \(U_{\bf a},U_{\bf b}\), let \(r\) be the number of blocks in which their chosen coordinates differ. Since both maximal clique sums are saturated, in every differing block the two chosen coordinates are equal block maxima. Together with the common maximal-sum equality, this imposes \(r+1\) independent equations. If \(r\ge2\), the intersection is of codimension at least three. If \(r=1\), give the two chosen coordinates in that block the same positive maximum, the other selected coordinates strict positive maxima, and make all unselected coordinates strictly smaller; exactly two upper inequalities are tight, hence there is a ridge.

It follows that the four ridge types and their counts are

\[
 \begin{array}{c|c}
 LL&\binom N2\\
 LU\text{ with unselected lower coordinate}&Q(N-k)\\
 LU\text{ with selected singleton lower coordinate}&sQ\\
 UU\text{ differing in one block}&Q(N-k)/2.
 \end{array}
\]

**3. Dihedral angles.** The outward normals are \(-e_{i,a}\) for \(L_{i,a}\), and \(u_{\bf a}=\sum_i e_{i,a_i}\) for \(U_{\bf a}\). Each \(u_{\bf a}\) has squared norm \(k\). The outward-normal dot product is zero for \(LL\) and the admissible unselected \(LU\); it is \(-1\) for singleton-selected \(LU\); and it is \(k-1\) for \(UU\) differing in one block. The interior angle is \(\pi\) minus the angle between outward normals. This yields, in order, \(\pi/2\), \(\alpha_k\), and \(\beta_k\) as stated.

**4. Exact intrinsic ridge measures.** Set \(C=(\prod_i n_i!)/(N-2)!\). In a ridge with two zero coordinates, integrate the same block-maxima Dirichlet density with the corresponding part sizes reduced by one or two. When both zero coordinates lie in a nonsingleton block \(i\), each ridge has measure \(C/[n_i(n_i-1)]\), and summing its \(\binom{n_i}{2}\) choices gives \(C/2\). When the two zeros lie in distinct blocks \(i,j\), each ridge has measure \(C/(n_i n_j)\), and its \(n_i n_j\) choices total \(C\). Thus all \(LL\) ridges total \(C[(k-s)/2+\binom{k}{2}]=C(k^2-s)/2\).

Parameterize an upper facet by positive block maxima \(t_i\), \(\sum_i t_i=1\), and the unselected coordinates in \([0,t_i]\). For an \(LU\) ridge with an unselected zero coordinate in nonsingleton block \(i\), the induced Euclidean Jacobian on the maximal-sum hyperplane is \(\sqrt{k}\). The corresponding Dirichlet integral gives each such ridge area

\[
 \frac{\sqrt{k}(n_i-2)!\prod_{j\ne i}(n_j-1)!}{(N-2)!}
 =\frac{\sqrt{k}C}{Q(n_i-1)}.
\]

There are \(Q(n_i-1)\) such ridges for block \(i\), so each nonsingleton block contributes \(\sqrt{k}C\).

For an \(LU\) ridge with a selected singleton coordinate fixed to zero, the maximal-sum hyperplane involves only the other \(k-1\) blocks and has Euclidean Jacobian \(\sqrt{k-1}\). Each ridge has area \(\sqrt{k-1}C/Q\); each singleton block contributes \(Q\) ridges, totaling \(\sqrt{k-1}C\).

For a \(UU\) ridge differing in block \(i\), two coordinates in that block tie at the maximum. Its free-maxima parametrization has Jacobian \(\sqrt{2k-1}\): the determinant of the Gram matrix of the \(k-1\) free maximal-coordinate directions is \(2k-1\). Its Dirichlet integral gives area

\[
 \frac{\sqrt{2k-1}(n_i-2)!\prod_{j\ne i}(n_j-1)!}{(N-2)!}
 =\frac{\sqrt{2k-1}C}{Q(n_i-1)}.
\]

There are \(Q(n_i-1)/2\) such ridges in block \(i\), totaling \(\sqrt{2k-1}C/2\) per nonsingleton block. Summing these four mutually exclusive classes yields the stated three angle-class measure totals. In every Dirichlet integral, the elementary identity used is

\[
 \int_{\substack{t_i\ge0\\\sum_{i=1}^k t_i=1}}\prod_i t_i^{a_i-1}\,dt_1\cdots dt_{k-1}
 =\frac{\prod_i\Gamma(a_i)}{\Gamma(\sum_i a_i)}.
\]

**5. Five-partite cancellation and Steiner coefficient.** If \((n_1,\ldots,n_5)=(1,1,1,p,q)\) with \(p,q\ge2\), then \(s=3\) and \(k-s=2\), giving \(A_{\rm right}=C(11+2\sqrt5)\), \(A_{\rm acute}=6C\), and \(A_{\rm obtuse}=3C\). Let \(z=\arctan(1/2)\). Since \(\sin z=1/\sqrt5\) and \(\sin(2z)=4/5\), the acute interior angle is \(\pi/2-z\), while the obtuse one is \(\pi/2+2z\). The area-weighted signed deviations from \(\pi/2\) are \(-6Cz\) and \(+3C(2z)\), exactly cancelling.

For each ridge the exterior angle is \(\pi-\theta\). The Euclidean second Steiner coefficient gives

\[
 V_{N-2}(P)=\frac1{2\pi}\sum_{\text{ridges }F}(\pi-\theta_F)H(F).
\]

The same cancellation implies the area-weighted exterior angle is also \(\pi/2\). Hence \(V_{N-2}=\frac14 C(20+2\sqrt5)=(5+\sqrt5/2)C\). Dividing by the already established \(V_N=\prod_i n_i!/N!\) proves the final normalized formula.

## Verification

The standalone checker `check_multipartite_ridges.py` enumerates all stable-set vertices and all coordinate/clique facet pairs, computes affine ranks by exact rational elimination, and verifies the ridge criterion, class counts, and outward-normal Gram products for ten profiles, including \((1,1,1,2,2)\), \((1,1,1,2,3)\), and \((1,1,1,3,3)\). It returned `MULTIPARTITE_RIDGE_CLASSIFICATION_PASS profiles=10`.

An independent numerical cross-check `numeric_area_check.py` projects the common-face vertices to their affine spans and computes their intrinsic Euclidean volumes with NumPy/SciPy. It checked **every ridge** in each of the profiles \((1,1,2)\), \((1,2,2)\), \((1,1,1,2,2)\), and \((1,1,1,2,3)\), agreeing with the individual Dirichlet/Jacobian formulas within \(2\times10^{-7}\). It returned `NUMERIC_RIDGE_MEASURES_PASS`. These finite checks corroborate the proof but do not establish the theorem for arbitrary part sizes.

Run with `python check_multipartite_ridges.py` and `python numeric_area_check.py` (the latter additionally requires `numpy` and `scipy`). The exact identity \(\sin(2\arctan(1/2))=4/5\) supplies the cancellation without numerical approximation.

## Relationship to prior work

The standard definition and geometric study of stable-set polytopes, their one-skeleta, and their facet descriptions are given by Aliniaeifard et al. (arXiv:1804.00360, first public version 2018-04-02), including the classical facet description for perfect graphs. Those known facts are premises, not claimed as new. Previously derived angle spectra for general bipartite stable-set polytopes cover the two-part case; previously derived metric ridge measures for clique–independent split graphs cover the case of a **single** nonsingleton part. Neither restricted case alone implies the asserted full ridge-measure classification for **two or more** nonsingleton parts, nor its five-partite two-large-block cancellation. Existing exact-volume and covariance results for complete multipartite stable-set polytopes are not claimed anew. In particular the full-dimensional volume formula here serves solely to normalize the new codimension-two metric invariant.

## Limitations

The novelty claim is restricted to multipartite profiles with at least two nonsingleton parts, and especially the exact five-partite balance. The metric is the canonical coordinate Euclidean metric; arbitrary affine transformations do not preserve the reported angles or ridge measures. The result is an analytic theorem for finite positive integer block sizes, not an assertion about random graphs. Independent mathematical review has not occurred. Historical priority against unindexed or inaccessible equivalent metric calculations remains uncertain; no universal uniqueness of the five-partite cancellation among all possible part counts is claimed.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first posted 2018-04-02; https://arxiv.org/abs/1804.00360 ; accessible full text: https://ar5iv.labs.arxiv.org/html/1804.00360 .
2. Classical Chvátal perfect-graph stable-set facet characterization, as recorded with references in Section 7.3.1 of Aliniaeifard et al. (above).
3. Previous results on bipartite stable-set ridge-angle spectra and clique–independent stable-set ridge-curvature measures are acknowledged in the relationship section; their pre-established special cases are excluded from the novelty scope.
