# Eight exact arcs of primitive three-periodic points at a toral-shear resonance

## Finding
Consider the area-preserving piecewise-linear torus map \(H_\eta\) defined below. Its set of non-isolated points fixed by the third iterate is empty for every \(0<\eta<1/2\) with \(\eta\ne1/3\). At the resonance \(\eta=1/3\), that set is exactly the union, modulo the edge identifications of the unit square, of the **eight closed straight segments** in the following table. Every point on these segments has *primitive* period three. Their total one-dimensional Hausdorff length in the standard flat torus metric is
\[
\mathcal H^1\bigl(\operatorname{Acc}(\operatorname{Fix}(H_{1/3}^3))\bigr)
=\frac49(1+\sqrt2+\sqrt5).
\]
Here \(\operatorname{Acc}\) denotes the set of accumulation points. In particular, \(\eta=1/3\) is the **unique** parameter in \((0,1/2)\) admitting a nonconstant continuum of third-iterate fixed points.

| Segment | First endpoint \((x,y)\) | Second endpoint \((x,y)\) | Branch order on its interior |
|---|---|---|---|
| 1 | \((0,7/9)\) | \((2/9,8/9)\) | RLR |
| 2 | \((0,8/9)\) | \((2/9,1)\) | RLR |
| 3 | \((7/9,2/3)\) | \((1,7/9)\) | RLR |
| 4 | \((7/9,7/9)\) | \((1,8/9)\) | RLR |
| 5 | \((2/9,2/9)\) | \((4/9,2/9)\) | LRR |
| 6 | \((5/9,4/9)\) | \((7/9,4/9)\) | LRR |
| 7 | \((2/9,2/3)\) | \((4/9,8/9)\) | RRL |
| 8 | \((5/9,7/9)\) | \((7/9,1)\) | RRL |

The coordinates \(1\) in this table denote the same torus coordinate as \(0\); the tabulated segments are understood using the quotient projection of the closed unit square. Some adjoining segments meet at torus edges; the stated Hausdorff length counts each open arc once.

## Assumptions and scope
For \(0<\eta<1/2\), take the standard two-torus \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), represented by \([0,1)^2\). Let
\[
f_\eta(y)=\begin{cases}y/(1-\eta),&0\le y\le1-\eta,\\(1-y)/\eta,&1-\eta\le y\le1.\end{cases}
\]
Define \(H_\eta(x,y)=(x+f_\eta(y),\,y+x+f_\eta(y))\pmod1\). The two affine pieces are denoted L and R, with the common switching line counted in both closures. We classify the **non-isolated** points of \(\operatorname{Fix}(H_\eta^3)\), not all isolated periodic points or the dynamics at higher periods.

## Proof
Write one step in coordinates as \((x',y')=(x+f_\eta(y)-m,\,y+x+f_\eta(y)-m-n)\), where the integer wrap bits \(m,n\in\{0,1\}\) are determined by reducing each coordinate modulo one. Each of the three consecutive branch choices and wrap-bit pairs gives a planar affine map on a polygonal itinerary cell. Its derivative is a product of three matrices from
\[
L=\begin{pmatrix}1&(1-\eta)^{-1}\\1&1+(1-\eta)^{-1}\end{pmatrix},\quad
R=\begin{pmatrix}1&-\eta^{-1}\\1&1-\eta^{-1}\end{pmatrix}.
\]
For branch words containing respectively zero, one, two, or three R's, direct multiplication gives the following determinants of \(I\) minus the three-step derivative:
\[
\begin{array}{c|c}
\text{number of R's}&\det(I-DH_\eta^3)\\\hline
0&(3\eta-4)^2/(\eta-1)^3\\
1&(3\eta-4)(3\eta-2)/(\eta(\eta-1)^2)\\
2&3(3\eta-1)/\eta^2\\
3&(3\eta-1)^2/\eta^3.
\end{array}
\]
Cyclic and other rearrangements have the same determinant by cyclic trace, and each derivative has determinant one. Consequently, outside \(\eta=1/3\), each of finitely many cells contains **at most one** solution of \(H_\eta^3(z)=z\), since \(I-DH_\eta^3\) is nonsingular. The fixed-point set is finite there; it has no accumulation points.

At \(\eta=1/3\), the matrices are \(L=\bigl(\begin{smallmatrix}1&3/2\\1&5/2\end{smallmatrix}\bigr)\) and \(R=\bigl(\begin{smallmatrix}1&-3\\1&-2\end{smallmatrix}\bigr)\). In particular \(R^3=I\). For any LRR itinerary, the fixed-point equation has rank one (and likewise for its cyclic permutations). To obtain the *entire* positive-dimensional solution locus, one must impose all intermediate branch and integer-wrap inequalities: there are exactly \(2^3\cdot4^3=512\) formal three-step branch/wrap combinations. For each one, solve the two affine equations, intersect the solution line with the six intermediate coordinate bounds and three branch bounds, and retain positive-length intersections. Exact rational elimination yields **twelve positive-length itinerary cells**: four RLR cells, four LRR cells, and four RRL cells. The two adjacent collinear cells in each of the two LRR pairs and each of the two RRL pairs unite, giving precisely the eight straight segments tabulated above. All remaining two-R cells are empty, points, or inconsistent. Reproducible exact rational enumeration is provided in `CHECK.py`.

The remaining three-R word requires special attention because its affine third derivative is the identity. For its third-iterate affine translation to vanish, all three wrap-bit pairs must be identical; this follows by substituting the four wrap vectors into \(I+R+R^2=0\). With a constant wrap pair \((m,n)\), the corresponding one-step affine map has fixed center \((n,1-m/3)\). Since the derivative has exact order three, that center is the average of its three iterates. Every canonical first coordinate belongs to \([0,1)\), so an average equal to \(n\in\{0,1\}\) forces a boundary orbit; there is **no** positive-dimensional three-R periodic cell. Thus the eight listed segments exhaust the non-isolated third-iterate fixed-point set.

For a direct, non-enumerative existence check, consider segment 2, parametrized by \((x,y)=(2t-16/9,t)\), \(8/9\le t\le1\). Its successive canonical points (for interior \(t\)) are
\[
(2t-16/9,t)\longmapsto(11/9-t,2/9)
\longmapsto(14/9-t,16/9-t)
\longmapsto(2t-16/9,t).
\]
The branch itinerary is RLR; the wrapping is well defined throughout the open segment. Continuity extends the equality to endpoints. The checker verifies the other seven arcs by exact rational substitution. No point of the eight arcs is fixed by \(H_{1/3}\): the fixed points of this shear map are \((0,0)\) and \((0,2/3)\), neither of which lies on the tabled segments. Since every point is fixed by the third iterate, its least period is exactly three.

The eight segments have lengths \(\sqrt5/9\) (four RLR arcs), \(2/9\) (two LRR arcs), and \(2\sqrt2/9\) (two RRL arcs). Distinct interiors do not overlap. Their sum proves the stated Hausdorff-length formula.

## Verification
Run `python CHECK.py` with Python 3 and SymPy. The self-contained script enumerates all three-step branch/wrap combinations using exact rational linear algebra, checks the twelve positive-length itinerary cells against the eight listed geometric arcs, and checks \(59\) rational interior points on each arc by three exact forward iterations. Its expected final line is `PERIOD_THREE_RESONANT_EIGHT_ARCS_OK; cells=12; arcs=8; exact_points=472`. A separate symbolic calculation of the four displayed determinant factors was performed using exact matrices. The finite checker is a reproducibility aid for the finite partition; the proof of impossibility at other parameter values is the displayed symbolic determinant identity.

## Relationship to prior work
Myers Hill, Sturman, and Wilson introduce precisely this family, establish nonuniform hyperbolicity for a parameter interval below \(1/3\), and identify the loss of hyperbolicity of a three-step branch matrix at \(1/3\) and elliptic islands around period-three orbits above it. Those results do not themselves imply that at the transition the entire non-isolated third-iterate fixed locus consists of eight exact line segments with an exact total length. An earlier related exact calculation gives invariant ellipses and their areas **strictly above** \(1/3\); the present boundary classification is disjoint in parameter and conclusion. The endpoint and global finite-branch comparisons distinguish the present assertion from local derivative degeneracy alone.

## Limitations
The result classifies only positive-dimensional/non-isolated third-iterate fixed loci. It does not enumerate isolated period-three cycles, classify periods above three, or establish global mixing at the resonant parameter. Enumeration assumes exact arithmetic and the standard continuous torus quotient; it is not a floating-point assertion. Priority relative to potentially unindexed work cannot be ruled out. Independent external validation has not been performed.

## References
- J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346, first posted 2021-12-14; peer-reviewed version *A Family of Non-Monotonic Toral Mixing Maps*, *Journal of Nonlinear Science* 32, article 31 (2022), DOI:10.1007/s00332-022-09790-0.
