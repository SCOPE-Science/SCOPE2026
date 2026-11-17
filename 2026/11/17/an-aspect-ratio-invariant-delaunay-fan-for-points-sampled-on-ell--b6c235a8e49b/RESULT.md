# An aspect-ratio-invariant Delaunay fan for points sampled on ellipses

## Finding
For any finite set of at least four distinct points with prescribed eccentric anomaly angles on \(E_{a,b}=\{(a\cos\theta,b\sin\theta):\theta\in\mathbb R\}\), the set of all Euclidean Delaunay triangulations is the same for every \(a>b>0\). In generic configurations the triangulation is unique. For four points taken in counterclockwise order, define
\[
\Delta=\det\begin{bmatrix}x_1&y_1&x_1^2+y_1^2&1\\x_2&y_2&x_2^2+y_2^2&1\\x_3&y_3&x_3^2+y_3^2&1\\x_4&y_4&x_4^2+y_4^2&1\end{bmatrix}.
\]
Then exactly
\[
\Delta=-16ab(a^2-b^2)\sin\!\left(\frac{\theta_1+\theta_2+\theta_3+\theta_4}{2}\right)\prod_{1\le i<j\le4}\sin\!\left(\frac{\theta_j-\theta_i}{2}\right).
\]
This identifies every possible four-point cocircular degeneracy by the angle-sum condition, independently of eccentricity.

For four independently sampled uniform eccentric anomalies, choose the first labelled point as the root of counterclockwise cyclic order and unwrap the three subsequent angles. The four positive cyclic gaps \(G_1,\ldots,G_4\), summing to \(2\pi\), have normalized joint Dirichlet \((1,1,1,1)\) law. Conditional on those gaps, the normalized signed incircle margin
\[
M=-\frac{\Delta}{16ab(a^2-b^2)\prod_{i<j}\sin((\theta_j-\theta_i)/2)}
\]
has precisely the standard arcsine distribution \(dt/(\pi\sqrt{1-t^2})\) on \((-1,1)\). Hence the two possible Delaunay diagonals are conditionally equiprobable, with \(\Pr(|M|\le t)=2\arcsin(t)/\pi\) on \([0,1]\).

## Assumptions and scope
Assume \(n\ge4\), pairwise distinct anomalies modulo \(2\pi\), and \(a>b>0\) with axes fixed; translations and common orthogonal coordinate rotations do not change the assertion. For the random four-point statement, the four points are independent and each has uniform eccentric anomaly. The cyclic ordering begins at the *originally labelled first point*, and each later angle is unwrapped by adding \(2\pi\) when necessary. This rooting is essential for the clean conditional statement and eliminates any sorting-at-an-arbitrary-origin ambiguity. The random point density is uniform in eccentric anomaly, not Euclidean arclength. General-position assertions hold almost surely under this distribution.

## Proof
**All-site rigidity.** Let \(c_j=\cos\theta_j\) and \(s_j=\sin\theta_j\). The standard paraboloid lift is \((x_j,y_j,x_j^2+y_j^2)\). On the ellipse,
\[
x_j^2+y_j^2=b^2+(a^2-b^2)c_j^2.
\]
The affine transformation of lifted space
\[
(x,y,z)\mapsto \left(x/a,y/b,\frac{z-b^2}{a^2-b^2}\right)
\]
is invertible and preserves vertical ordering since the third scaling is strictly positive. It maps every lifted point to \((c_j,s_j,c_j^2)\), a configuration independent of both semiaxes. Consequently its lower faces, including any nonsimplicial faces, have exactly the same incidences at all aspect ratios \(a>b>0\). Projecting lower faces gives the complete Euclidean Delaunay subdivision and its compatible triangulations, proving the all-\(n\) assertion.

**Four-site factorization.** In the determinant substitute \(x_j=a\cos\theta_j\), \(y_j=b\sin\theta_j\), and subtract the constant \((a^2+b^2)/2\) times the last column from the third. Then the third column becomes \((a^2-b^2)\cos2\theta_j/2\), so
\[
\Delta=\frac{ab(a^2-b^2)}2\det[\cos\theta_j,\sin\theta_j,\cos2\theta_j,1]_{j=1}^4.
\]
Writing \(z_j=e^{i\theta_j}\), multiplying each row by \(z_j^2\), and expanding the four Laurent-polynomial columns gives a Vandermonde product times \((1-\prod_jz_j)\). The elementary identities \(z_j-z_i=2ie^{i(\theta_i+\theta_j)/2}\sin((\theta_j-\theta_i)/2)\) and \(1-e^{iS}=-2ie^{iS/2}\sin(S/2)\) simplify this determinant to \(-32\sin(S/2)\prod_{i<j}\sin((\theta_j-\theta_i)/2)\), where \(S=\sum_j\theta_j\). Multiplying prefactors yields the displayed exact identity. Since every pairwise sine is strictly positive for a counterclockwise unwrapping spanning less than \(2\pi\), zero determinant is equivalent to \(S\in2\pi\mathbb Z\). The sign is the ordinary incircle predicate and chooses one of the two diagonals.

**Marked sampling law.** Root at the original first labelled point of the iid sample. Its anomaly \(U\) is uniform on \([0,2\pi)\) and independent of the other three relative uniform angles. Their sorted differences partition the circumference into a Dirichlet \((1,1,1,1)\) gap vector. With \(\theta_1=U\), \(\theta_2=U+G_1\), \(\theta_3=U+G_1+G_2\), and \(\theta_4=U+G_1+G_2+G_3\), the phase equals
\[
\frac S2=2U+\frac{3G_1+2G_2+G_3}{2}.
\]
For every fixed gap vector, \(2U\) is uniform modulo \(2\pi\). Hence \(\sin(S/2)\) is exactly arcsine, independent of the gaps. The determinant factorization identifies this sine as \(M\). Its sign is balanced; direct integration of the arcsine density gives the stated near-zero mass.

## Verification
The included `verify.py` numerically checks the signed determinant identity on nondegenerate quadruples over multiple semiaxes and independently checks the invariant interior edge sets of planar Delaunay triangulations for generic \(n=4,7,12\). The exact proof is algebraic; numerical agreement does not certify all real parameters. The script also evaluates the exact arcsine cumulative formula against numerical quadrature.

## Relationship to prior work
The classical incircle predicate and lower convex-hull paraboloid lifting are well established. Khanimov and Sharir (arXiv:1510.04608, first public 2015-10-15) study how independent Gaussian perturbations of grids and regular cyclic polygons choose Delaunay triangulations; the deterministic ellipse-axis deformation here is a different perturbation with a rigid, globally invariant triangulation fan. Agarwal, Kaplan, Rubin and Sharir (arXiv:1404.4851, 2014-04-18) analyze kinetic Delaunay diagrams under polygonal *distance functions*, whereas this theorem concerns the ordinary Euclidean distance, with all moving sites constrained to a common noncircular ellipse. No novelty is claimed for the incircle or lifting primitives. The precise all-site aspect-ratio rigidity, explicit four-point degeneracy hyperplanes, and marked arcsine law are the compared contributions.

## Limitations
The invariant fan assertion requires all points to share the *same* ellipse and to retain their eccentric anomaly angles while the ellipse's axes change. It does not assert affine invariance of Euclidean Delaunay triangulations for arbitrary point sets. The circular case \(a=b\) is completely cocircular and is not covered by unique-triangulation claims. The fair random diagonal conclusion is specific to uniform eccentric anomalies and a distinguished cyclic root. Historical uniqueness is provisional; independent validation has not been performed.

## References
1. M. Khanimov and M. Sharir, *Delaunay Triangulations of Degenerate Point Sets*, initial arXiv release 2015-10-15, https://arxiv.org/abs/1510.04608 .
2. P. K. Agarwal, H. Kaplan, N. Rubin, and M. Sharir, *Kinetic Voronoi Diagrams and Delaunay Triangulations under Polygonal Distance Functions*, initial arXiv release 2014-04-18, https://arxiv.org/abs/1404.4851 .
3. L. J. Guibas and J. Stolfi, *Primitives for the manipulation of general subdivisions and the computation of Voronoi diagrams*, ACM Transactions on Graphics 4 (1985), 74–123; cited for the classical incircle predicate.
