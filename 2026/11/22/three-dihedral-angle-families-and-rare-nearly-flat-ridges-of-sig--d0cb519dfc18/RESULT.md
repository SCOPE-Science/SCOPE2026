# Three dihedral-angle families and rare nearly-flat ridges of signed Birkhoff polytopes

## Finding

Let \(n\ge 2\) and let \(\mathcal B_n^{\pm}\subset\mathbb R^{n\times n}\) be the convex hull of the signed permutation matrices, with the ambient Frobenius inner product. A *ridge* means a face of dimension \(n^2-2\), and its interior dihedral angle is the angle inside the polytope between its two supporting facets.

For every \(n\ge3\), the **complete ridge-angle multiset**, with multiplicities, is

\[
\begin{array}{c|c}
\text{interior angle}&\text{number of ridges}\\\hline
\pi/2 &n(n-1)\,2^{2n}\\
\pi-\arccos(1/n)&n^2\,2^{2n-1}\\
\pi-\arccos((n-2)/n)&n^2\,2^n.
\end{array}
\]

At \(n=3\), the last two numerical angles coincide and their multiplicities are added. For \(n=2\), there are exactly \(32\) ridges, all of angle \(2\pi/3\). In particular, **no ridge has an acute interior angle**. For \(n\ge4\) the three angle values are distinct. The total for \(n\ge3\) is \(n(n-1)2^{2n}+n^2 2^{2n-1}+n^2 2^n\).

If \(\Theta_n\) is the interior angle of a uniformly chosen ridge, then
\[
 n(\Theta_n-\pi/2)\ \Longrightarrow\ \frac23\delta_0+\frac13\delta_1,
 \qquad n\bigl(\mathbb E\Theta_n-\pi/2\bigr)\longrightarrow\frac13.
\]
The exceptional, nearly-flat ridge family has probability \(\sim(2/3)2^{-n}\), yet its angle approaches \(\pi\) with deficit \(\sim2/\sqrt n\). Thus the typical small angular excess and the rare almost-flat behavior have different scales.

## Assumptions and scope

Use the canonical, **unrescaled** signed-permutation realization and Frobenius metric \(\langle X,Y\rangle=\sum_{i,j}X_{ij}Y_{ij}\); arbitrary affine realizations are not asserted to preserve angles. An interior angle is \(\pi\) minus the angle between the two outward facet normals. The facets are indexed by a row or column \(i\in\{1,\dots,n\}\) and a sign vector \(s\in\{-1,1\}^n\), with inequalities \(\sum_j s_jX_{ij}\le1\) and \(\sum_i s_iX_{ij}\le1\), respectively. This is the established full irredundant facet description; there are \(2n2^n\) facets for \(n\ge2\).

## Proof

We first classify which unordered pairs of facets meet in a ridge. The signed doubly substochastic description is equivalent to every row and column having absolute-entry sum at most one. Saturation of a facet with sign vector \(s\) forces every nonzero entry on its supporting row or column to have sign \(s\).

1. **Same row or same column.** If the facet sign vectors differ in \(h\) positions, their common points have zeros in all \(h\) positions; besides the row/column supporting equality, this imposes \(h\) independent coordinate equalities. Thus for \(h\ge2\) there is no ridge. For \(h=1\) and \(n\ge3\), put magnitude \(1/(n-1)\) in every other position of that row/column, with the prescribed common signs, and zero elsewhere. Exactly the two candidate facets are tight, because the opposite coordinate sums are strictly smaller than one. Hence the intersection is a ridge. When \(n=2\), the remaining nonzero entry has magnitude one and forces a third, independent, perpendicular row/column facet equality; therefore no same-support pair is a ridge.

2. **Different rows or different columns.** For \(n\ge3\), fill both specified rows (or both columns) with entries of magnitudes \(1/n\) and their respective prescribed signs, leaving the other rows (columns) zero. The opposite-coordinate sums are \(2/n<1\). Exactly two facets are tight, proving a ridge for *every* choice of distinct supports and signs. For \(n=2\), two saturated rows force both columns to have absolute-entry sums equal to one, and vice versa. The chosen sign restrictions then make at least a third independent facet equality compulsory, so these pairs are not ridges.

3. **One row and one column.** Suppose their shared cell is \((i,j)\). If the prescribed signs at this cell disagree, the shared entry must vanish on the intersection. The row facet with that entry's sign flipped is also tight, introducing an independent additional supporting equality, so there is no ridge. If the signs agree, choose the shared entry of magnitude \(\varepsilon\in(0,1)\), distribute the remaining magnitude \(1-\varepsilon\) strictly positively over the other \(n-1\) entries of the selected row and selected column, respecting their signs, and put zeros elsewhere. All other row/column absolute sums are strictly below one. Exactly the designated two facets are tight, so their intersection is a ridge for every \(n\ge2\).

A point at which precisely two linearly independent irredundant facet inequalities are active lies in the relative interior of a codimension-two face. Conversely, the extra independent equalities in the excluded cases force codimension at least three. This proves the classification without assuming the polytope is simple.

Every outward normal has Frobenius length \(\sqrt n\). For different parallel supports (different rows or columns) the normals are orthogonal. For a compatible row-column pair their inner product is \(1\). For same-support signs at Hamming distance one it is \(n-2\). Therefore their interior angles are exactly the three displayed values.

There are \(2n\) row/column support groups, each containing \(2^n\) sign vectors. Each group's sign cube has \(n2^{n-1}\) Hamming-one edges, giving \(n^2 2^n\) same-support ridges for \(n\ge3\). Different-row or different-column supports contribute \(2\binom n2 2^{2n}=n(n-1)2^{2n}\) ridges. There are \(n^2\) row-column support pairs, each with exactly \(2^{2n-1}\) compatible sign pairs, giving \(n^2 2^{2n-1}\). At \(n=2\), only the last class survives, with \(32\) ridges and common angle \(\pi-\arccos(1/2)\).

As \(n\to\infty\), the three class probabilities tend to \(2/3,1/3,0\). The right-angle class has zero scaled excess, the mixed-support class has \(n\arcsin(1/n)\to1\), and the last class has probability \(\sim (2/3)2^{-n}\), with angle \(\pi-\arccos(1-2/n)=\pi-2n^{-1/2}+o(n^{-1/2})\). The vanishing rare mass proves weak convergence of the scaled law. Its contribution to the scaled expectation tends to zero, proving the asserted mean limit.

## Verification

The accompanying `verify_ridges.py` constructs all signed-permutation vertices and all facet normals, computes face dimensions from the affine ranks of vertices saturating each facet pair, and compares those *calculated* dimensions with the claimed ridge classes. Exhaustive computations pass at \(n=2,3,4\), respectively examining \(120\), \(1128\), and \(8128\) facet pairs. These computations test the small-order behavior, especially the four-dimensional exception; the complete statement for arbitrary \(n\) follows from the independent geometric argument above, not from extrapolation. Run `python verify_ridges.py` with Python 3 and NumPy.

## Relationship to prior work

Kohl, Olsen and Sanyal's study of unconditional reflexive polytopes (2019 preprint, 2020 journal version) provides the signed Birkhoff polytope's exact facet inequalities. An earlier superseded type-B Birkhoff preprint was publicly posted 29 March 2019. Chen and Zhu (2024) develop a general facial-matrix description and classify low-dimensional faces. Their theorem supplies a general route to determine ridge incidence, but their inspected statements do not give this metric ridge-angle histogram or its two-scale limiting law. The present result uses their known combinatorial objects and established facet coordinates, and gives a closed metric classification rather than a new general face theorem.

## Limitations

The theorem concerns Euclidean dihedral angles, **not** solid angles, ridge areas, or the second intrinsic volume. The rare-class asymptotic gives frequency among ridges, not any area-weighted curvature contribution. It does not assert priority over unknown or unindexed equivalent computations. No independent mathematical audit has been performed.

## References

- F. Kohl and M. Olsen, *Birkhoff polytopes of different type and the orthant-lattice property*, arXiv:1903.12634v1, first posted 2019-03-29; withdrawn in favor of the expanded study below: https://arxiv.org/abs/1903.12634.
- F. Kohl, M. Olsen and R. Sanyal, *Unconditional reflexive polytopes*, arXiv:1906.01469, first posted 2019-06-03, particularly §5 and Corollary 5.7: https://arxiv.org/abs/1906.01469; *Discrete & Computational Geometry* 64 (2020), 427–452, https://doi.org/10.1007/s00454-020-00199-8.
- Z. Chen and K. Zhu, *Faces of the signed Birkhoff polytopes*, *Electronic Journal of Linear Algebra* 40 (2024), 747–765, particularly §§2–3: https://doi.org/10.13001/ela.2024.8153; https://journals.uwyo.edu/index.php/ela/article/download/8153/6817/22441.
