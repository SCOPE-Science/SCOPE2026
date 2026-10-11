# Exact defect decomposition for the Lemoine pedal-triangle minimum
## Finding
Let \(ABC\) be a nondegenerate Euclidean triangle, with side lengths \(a=BC\), \(b=CA\), \(c=AB\), area \(\Delta\), and \(S=a^2+b^2+c^2\). Let \(K\) be the symmedian (Lemoine) point. Choose \(X\in BC\), \(Y\in CA\), \(Z\in AB\), and let \(M\) be the centroid of \(XYZ\). Let \(D_a,D_b,D_c\) be the perpendicular feet from \(M\) to the lines \(BC,CA,AB\). For consistently oriented unit normals \(n_a,n_b,n_c\) to these sidelines,
\[
XY^2+YZ^2+ZX^2
=\frac{12\Delta^2}{S}
+3\sum_{i\in\{a,b,c\}}\bigl(n_i\cdot(M-K)\bigr)^2
+3\bigl(D_aX^2+D_bY^2+D_cZ^2\bigr).
\]
Thus the classical Lemoine-pedal minimum has the exact value
\[
\min\bigl(XY^2+YZ^2+ZX^2\bigr)=\frac{12\Delta^2}{a^2+b^2+c^2},
\]
and equality holds exactly for the pedal triangle of \(K\).

## Assumptions and scope
The triangle \(ABC\) is nondegenerate. The points \(X,Y,Z\) lie on the three closed sides for the minimization statement. The displayed identity itself remains valid if the points are allowed on the corresponding extended sidelines. The normals are chosen consistently, for example inward-pointing; changing all three signs leaves the squared defect unchanged.

## Proof
For any triangle \(XYZ\) with centroid \(M\), the centroid identity gives
\[
XY^2+YZ^2+ZX^2=3\bigl(MX^2+MY^2+MZ^2\bigr).
\]
Orthogonal projection onto the three sidelines gives
\[
MX^2=MD_a^2+D_aX^2,
\]
with the analogous identities for \(Y,Z\). Therefore
\[
XY^2+YZ^2+ZX^2
=3F(M)+3\bigl(D_aX^2+D_bY^2+D_cZ^2\bigr),
\]
where \(F(P)\) is the sum of the squared signed distances from \(P\) to the three sidelines.

The symmedian point has barycentric coordinates \(a^2:b^2:c^2\). Hence its signed distances to \(BC,CA,AB\), with consistent inward normals, are
\[
\delta_a(K)=\frac{2\Delta a}{S},\qquad
\delta_b(K)=\frac{2\Delta b}{S},\qquad
\delta_c(K)=\frac{2\Delta c}{S}.
\]
Rotating the directed side-vector closure of \(ABC\) by a right angle yields the normal equilibrium
\[
a n_a+b n_b+c n_c=0.
\]
For \(h=M-K\), signed distance is affine, so
\[
\delta_i(M)=\delta_i(K)+n_i\cdot h.
\]
Expanding the squares and using the normal equilibrium gives
\[
F(M)=F(K)+\sum_{i\in\{a,b,c\}}\bigl(n_i\cdot(M-K)\bigr)^2.
\]
Moreover,
\[
F(K)=\frac{4\Delta^2(a^2+b^2+c^2)}{S^2}=\frac{4\Delta^2}{S}.
\]
Substitution proves the claimed decomposition.

Every term after \(12\Delta^2/S\) is nonnegative. If equality holds, the normal-square term vanishes; since two nonparallel side normals already span the plane, this forces \(M=K\). The three offset terms then force \(X=D_a\), \(Y=D_b\), \(Z=D_c\), so \(XYZ\) is the pedal triangle of \(K\). Conversely, for the perpendicular feet \(P_a,P_b,P_c\) from \(K\),
\[
P_a+P_b+P_c=3K-\sum_i\delta_i(K)n_i=3K,
\]
again by normal equilibrium, so their centroid is \(K\); all defect terms vanish. This proves both sharpness and uniqueness.

## Verification
The supplied verifier recomputes the decomposition from Cartesian coordinates for several scalene, right, and obtuse nondegenerate triangles and a deterministic grid of points on their three sides. It also checks the normal equilibrium, the barycentric formula for \(K\), the equality case at the pedal triangle, and the equilateral normalization. Numerical calculations are supplementary to the symbolic proof and are not used to infer the universal statement.

## Relationship to prior work
The Lemoine/symmedian point and the optimizer itself are classical. Finbarr Holland's 2007 enrichment notes state that the pedal triangle of the Lemoine point minimizes the sum of squared side lengths of an inscribed triangle. Those notes display the lower bound as \(4\Delta^2/S\), while the proof immediately below identifies the pedal-triangle side-square sum as three times the sum of squared distances from the Lemoine point to the sides. The equilateral triangle already shows the displayed constant is too small by a factor of three: for unit side length the medial/pedal triangle has squared-side sum \(3/4\), whereas \(4\Delta^2/S=1/4\). The corrected sharp value is \(12\Delta^2/S\).

The exact identity above is stronger than the minimum statement: it splits the entire excess into two geometrically distinct nonnegative quantities, one measuring displacement of the inscribed triangle's centroid from \(K\), and one measuring failure of the vertices to be the perpendicular projections of that centroid. Bani-Yaghoub, Rhee, and Sadek (2016) give a least-squares characterization of the symmedian point, an adjacent viewpoint; the accessible abstract does not state this inscribed-triangle defect identity. Arnold and Arreche (2024) develop hyperbolic-barycenter analogues of symmedian optimality, but do not supply this Euclidean two-term decomposition in the inspected material.

## Limitations
The exact decomposition concerns Euclidean triangles and this particular quadratic objective. The classical minimizer is not claimed as new. The literature search supports novelty of the explicit two-term defect decomposition and the factor-three correction to the displayed constant in the inspected 2007 notes, but it cannot exclude an equivalent identity in every older geometry text. The 2016 Mathematics Magazine article was compared through bibliographic metadata and its abstract because full text was not available from the inspected lawful sources; this is the principal residual historical-access risk.

## References
1. F. Holland, *Enrichment Lectures 2007*, University College Cork, March 26, 2007, Theorem 25, pp. 24--25. https://www.irmo.ie/notes07.pdf
2. M. Bani-Yaghoub, N. H. Rhee, and J. Sadek, "An Algebraic Method to Find the Symmedian Point of a Triangle," *Mathematics Magazine* 89(3) (2016), 197--200. DOI: 10.4169/math.mag.89.3.197.
3. M. Arnold and C. E. Arreche, "Symmedians as Hyperbolic Barycenters," *Comptes Rendus Mathématique* 362 (2024), 1743--1762. DOI: 10.5802/crmath.677.
