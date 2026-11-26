# The parity-dependent incenter locus of nonsquare two-row Monge polytopes

## Finding

For every integer \(m\ge3\), the normalized nonsymmetric two-row Monge polytope is
\[
\mathcal M_{2,m}=\left\{(a_1,\ldots,a_m;b_1,\ldots,b_m)\in\mathbb R_{\ge0}^{2m}:\ \sum_{j=1}^m(a_j+b_j)=1,\quad a_j+b_{j+1}\le a_{j+1}+b_j\ (1\le j<m)\right\}.
\]
Give its affine span the **intrinsic Frobenius (Euclidean) metric**, without any independent rescaling of the two rows. Put
\[
\alpha_m=\sqrt{1-\frac1{2m}},\qquad T_m=\left\lfloor\frac{m^2}{2}\right\rfloor,\qquad
\rho_m=\frac1{2m\alpha_m+T_m}.
\]
Then the exact Euclidean inradius is **\(\rho_m\)**. Every center of a largest contained ball has the following form, and every displayed matrix is such a center:
\[
\begin{split}
 w_j&=m+1-2j+\theta,\\
 a_j&=\rho_m\bigl(\alpha_m+\max\{-w_j,0\}\bigr),\\
 b_j&=\rho_m\bigl(\alpha_m+\max\{w_j,0\}\bigr),\qquad j=1,\ldots,m,\\
 \theta&=0\quad\text{if }m\text{ is odd},\qquad -1\le\theta\le1\quad\text{if }m\text{ is even}.
\end{split}
\]
In particular, **the optimal center is unique exactly for odd \(m\)**. For even \(m\), the complete optimal-center locus is an affine line segment of intrinsic Euclidean length \(2\rho_m\sqrt m\), whose endpoints are the choices \(\theta=\pm1\).

All \(m-1\) adjacent Monge facets touch every largest ball. At the unique odd-\(m\) center exactly \(m+1\) coordinate facets touch, giving \(2m\) tangent facets in all. At an even-\(m\) center with \(-1<\theta<1\), exactly \(m\) coordinate facets touch, giving \(2m-1\) tangent facets; at either endpoint \(\theta=\pm1\), exactly \(m+1\) coordinate facets touch, giving \(2m\) tangent facets. Finally \(m^2\rho_m\to2\) as \(m\to\infty\).

## Assumptions and scope

The orientation is the standard Monge convention \(a_j+b_k\le a_k+b_j\) for \(j<k\); the adjacent inequalities displayed above are equivalent to all these inequalities. All entries are nonnegative real numbers, their sum is one, and \(m\ge3\). The dimension of \(\mathcal M_{2,m}\) is \(2m-1\). This result concerns largest **Euclidean balls**, not maximum-volume ellipsoids, centroids, lattice volumes, or general rectangular \(p\times q\) Monge matrices. The excluded \(m=2\) case is already contained in a published theorem for square Monge polytopes and is deliberately not presented as new. Full facet descriptions of normalized Monge polytopes, including irredundancy of coordinate and adjacent Monge facets, were previously established by Erickson and Kretschmann (2023).

## Proof

**1. Exact ball-containment constraints.** Let \(H=\{X\in\mathbb R^{2m}:\sum X_{ij}=0\}\) be the translation space of the affine span. Each coordinate normal has orthogonal projection onto \(H\) of norm \(\alpha_m=\sqrt{1-(2m)^{-1}}\). An adjacent Monge normal has entries \(+1,-1,-1,+1\), sum zero, and norm \(2\). Consequently, a closed Euclidean \(H\)-ball of radius \(r\) centered at \((a;b)\) lies in \(\mathcal M_{2,m}\) **if and only if**
\[
 a_j,b_j\ge\alpha_m r\quad(1\le j\le m),\qquad
 (b_j-a_j)-(b_{j+1}-a_{j+1})\ge2r\quad(1\le j<m).
\tag{1}
\]
There are no additional inequalities to test, because all longer Monge inequalities telescope from the adjacent ones.

**2. Sharp discrete total-variation obstruction.** For a feasible positive radius \(r\), write
\[
 x_j=a_j-\alpha_m r\ge0,\quad y_j=b_j-\alpha_m r\ge0,\quad d_j=y_j-x_j=b_j-a_j.
\]
Then \(d_j-d_{j+1}\ge2r\), and \(x_j+y_j\ge|d_j|\). For each \(1\le j\le\lfloor m/2\rfloor\),
\[
 |d_j|+|d_{m+1-j}|\ge d_j-d_{m+1-j}\ge2r(m+1-2j).
\]
For odd \(m\), also \(|d_{(m+1)/2}|\ge0\). Adding yields
\[
 \sum_{j=1}^{m}|d_j|\ge rT_m,\qquad
 T_m=2\sum_{j=1}^{\lfloor m/2\rfloor}(m+1-2j)=\left\lfloor\frac{m^2}{2}\right\rfloor.
\tag{2}
\]
Thus \(1=\sum_j(a_j+b_j)\ge 2m\alpha_m r+rT_m\), proving \(r\le\rho_m\).

**3. Sharpness and all equality cases.** Set \(r=\rho_m\), choose \(\theta\) as in the Finding, and set \(d_j=r(m+1-2j+\theta)\), \(x_j=\max\{-d_j,0\}\), \(y_j=\max\{d_j,0\}\). The adjacent differences equal \(2r\). For odd \(m\), the middle \(d_j\) is zero and opposing terms in each pair have opposite signs; for even \(m\), the same sign condition holds for all pairs precisely when \(-1\le\theta\le1\). Hence equality holds throughout (2), and
\[
 \sum_j(a_j+b_j)=2m\alpha_mr+\sum_j|d_j|=\rho_m(2m\alpha_m+T_m)=1.
\]
The matrix is therefore a valid largest-ball center.

Conversely, every center attaining \(r=\rho_m\) must attain equality in every inequality above. From \(x_j+y_j=|d_j|\) and nonnegativity, necessarily \(x_j=(-d_j)_+\) and \(y_j=(d_j)_+\). The outermost-pair inequality in (2) must be equality; thus
\(d_1-d_m=2r(m-1)\). Since each of the \(m-1\) adjacent differences is at least \(2r\), **each adjacent difference equals \(2r\)**. Therefore \(d_j=r(m+1-2j+\theta)\) for some \(\theta\). When \(m\) is odd, equality also forces the middle entry \(d_{(m+1)/2}=0\), hence \(\theta=0\). When \(m\) is even, equality of the absolute-value triangle inequalities for the innermost pair forces \(d_{m/2}\ge0\ge d_{m/2+1}\), equivalent to \(-1\le\theta\le1\). This proves the entire center classification.

**4. Locus geometry, tangent facets and asymptotics.** For even \(m\), the signs of \(d_j\) remain fixed for \(-1<\theta<1\); each of the \(m\) columns has exactly one of its two coordinates varying at speed \(\rho_m\) in absolute value. The resulting center segment has length \(2\rho_m\sqrt m\). All adjacent Monge inequalities are active with exactly \(2r\) slack and thus tangent to the radius-\(r\) ball. A coordinate facet is tangent exactly when its entry equals \(\alpha_mr\). If \(d_j\ne0\), exactly one entry in column \(j\) does so; if \(d_j=0\), both do. Odd \(m\) has one zero-difference central column; even \(m\) has none for \(|\theta|<1\) and one at each endpoint. The tangent counts follow, using the established irredundant facet system. Since \(T_m/m^2\to1/2\) and \(2m\alpha_m/m^2\to0\), the stated asymptotic follows.

## Verification

The included standalone `verify_monge_two_row.py` checks the exact extremizer construction with `fractions.Fraction` for \(2\le m\le50\), samples all permitted parameter endpoints and interior values, verifies predicted tangency counts, and tests the lower bound by exhaustive integer enumeration over explicitly **finite** domains for \(2\le m\le5\). It separately formulates and solves the complete intrinsic inball linear program with SciPy/HiGHS for \(2\le m\le18\), comparing optimum radii and the extrema of one center coordinate on the optimal face. On the recorded execution it passed **12,661 assertions**. These computations check for algebraic or normalization errors; the preceding proof, not finite experiments, establishes the claim for every \(m\ge3\).

## Relationship to prior work

Erickson and Kretschmann (arXiv:2311.07522, 2023) describe the facets of normalized Monge polytopes and compute their two-row volumes; the present argument uses their facet system but considers a distinct Euclidean metric invariant. Erickson and Jones (arXiv:2609.09508, first posted 2026-09-08) obtain a lattice-path/Stanley model for the volume and Ehrhart series of Monge polytopes; their accessible abstract and introduction do not assert a Chebyshev-center result. A publicly available 2026 theorem on **square** \(n\times n\) Monge polytopes already computes all of their Euclidean incenters. It includes the \(2\times2\) case, which is therefore excluded here; it does not imply the full \(2\times m\) family for \(m\ge3\) in its stated metric, nor its odd/even center-locus dichotomy. An earlier calculation of the **centroid** of the two-row Monge polytope also concerns a different center notion and does not determine its inradius. These are comparisons of statements, not assertions of comprehensive historical priority.

## Limitations

The theorem does not cover arbitrary rectangular aspect ratios beyond two rows, weighted coordinate metrics, John ellipsoids, or spherical enclosing radii. It uses the sum-one normalization; other normalizations rescale distances. Although the 2026 motivating source's abstract and introduction were materially inspected, its entire manuscript could not be reinspected in this run; a hidden equivalent Euclidean statement there or in unindexed earlier work cannot be ruled out. This is not an independent historical-priority certification.

## References

- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first posted 2023-11-13; especially the published facet and two-row volume descriptions.
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508v1, first posted 2026-09-08, primary MSC2020 52B12.
- *An affine \(n-1\)-cube of Euclidean incenters for square Monge polytopes*, mathematical research record, first made public 2026-10-11; comparison pertains to square matrices only.
- *Exact centroids and logarithmic edge profiles of two-row Monge polytopes*, mathematical research record (2026); comparison pertains to centroids only.
