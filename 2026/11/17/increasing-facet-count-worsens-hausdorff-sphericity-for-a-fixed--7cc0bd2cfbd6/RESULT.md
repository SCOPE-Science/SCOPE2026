# Increasing facet count worsens Hausdorff sphericity for a fixed-strength design family

## Finding

For every integer \(n\ge4\), take the spherical \(3\)-design \(X_n\) of two aligned regular latitude rings described below and form its area-normalized Minkowski polytope \(P_n\). Even though the number of equal-area facets is \(2n\to\infty\), its Euclidean Hausdorff distance from the unit ball **increases strictly**. Precisely, put \(b_n^2=4\pi\cot(\pi/n)/(\sqrt3n)\). Then
\[
d_H(P_n,B_3)=b_n-1\quad\nearrow\quad \frac{2}{3^{1/4}}-1>0.
\]
By contrast, the volume increases strictly as \(\operatorname{Vol}(P_n)=4\pi b_n/(3\sqrt3)\), while the surface area is always \(4\pi\). The two competing monotonicities occur at **fixed spherical design strength three**, not at increasing design strength.

## Assumptions and scope

All metric quantities are in ordinary Euclidean \(\mathbb R^3\). For \(n\ge4\), write \(\theta_j=2\pi j/n\) and \(\alpha=\pi/n\), and define the \(2n\) distinct unit vectors
\[
X_n=\left\{\left(\sqrt{\frac23}\cos\theta_j,\sqrt{\frac23}\sin\theta_j,\frac{\sigma}{\sqrt3}\right):0\le j<n,\ \sigma\in\{-1,1\}\right\}.
\]
Set \(B_3=\{x\in\mathbb R^3:\|x\|_2\le1\}\). The Minkowski polytope \(P_n\) is the unique (up to translation) full-dimensional convex polytope with outward **unit** facet-normal list exactly \(X_n\), each corresponding facet of area \(2\pi/n\); choose its Steiner point to be the origin. This is the normalization of surface area \(4\pi\) used for spherical-design Minkowski polytopes in An [1]. The spherical design construction is a special case of Bajnok's Construction 3.3 [2], and is not claimed as new.

The node sets are exact spherical \(3\)-designs: the averages of coordinate monomials of degree at most three agree with normalized area measure on \(S^2\). Indeed, averaging over \(\sigma\) eliminates every odd vertical power; averaging over the regular \(n\)-gon eliminates horizontal Fourier modes of orders one through three; and the three quadratic diagonal moments all equal \(1/3\). They are not spherical \(4\)-designs, since the average fourth vertical moment is \(1/9\) rather than the sphere's \(1/5\).

## Proof

**1. Reconstruct the equal-area polytope.** Let
\[
a_n^2=\frac{4\pi}{\sqrt3n\sin(2\alpha)},\qquad b_n=\sqrt2\,a_n\cos\alpha.
\]
Take the convex hull of the equatorial vertices \(v_j=(a_n\cos(\theta_j-\alpha),a_n\sin(\theta_j-\alpha),0)\) and poles \(v_+=(0,0,b_n)\), \(v_-=(0,0,-b_n)\). For each \(j\), the equatorial edge joining \(v_j\) and \(v_{j+1}\) lies on the line with radial direction \(\theta_j\) after cyclic relabeling, and the upper/lower triangular facet has outward unit normal
\[
 x_{j,\sigma}=\left(\sqrt{\frac23}\cos\theta_j,\sqrt{\frac23}\sin\theta_j,\frac{\sigma}{\sqrt3}\right)
\]
with support value \(b_n/\sqrt3\): both the equatorial edge and the relevant pole give this value because \(\sqrt{2/3}\,a_n\cos\alpha=b_n/\sqrt3\). Each triangle has area
\[
 a_n\sin\alpha\sqrt{b_n^2+a_n^2\cos^2\alpha}
 =\sqrt3\,a_n^2\sin\alpha\cos\alpha=\frac{2\pi}{n}.
\]
The \(2n\) triangular facets bound the bipyramid. Consequently their surface-area measure is precisely the specified equal-atom measure. Minkowski uniqueness and rotational/reflection symmetry identify the Steiner-centered representative with this bipyramid; its center is the origin.

**2. Exact insphere and circumsphere.** All facet support planes have outward unit normals \(x\in X_n\) and the same origin-distance \(r_n=b_n/\sqrt3\). Hence the origin-centered ball of that radius lies in the polytope and contacts every facet. If a radius-\(r\) ball has center \(c\), then \(x\cdot c+r\le b_n/\sqrt3\) for every \(x\in X_n\); summing all \(2n\) inequalities and using \(\sum_{x\in X_n}x=0\) gives \(r\le b_n/\sqrt3\). At equality every \(x\cdot c=0\), and since \(X_n\) spans \(\mathbb R^3\), \(c=0\). Thus the inball is unique. For \(n\ge4\), \(\sqrt2\cos(\pi/n)\ge1\), with equality only at \(n=4\); therefore the largest vertex norm equals \(b_n\). The poles are diametrically opposite at distance \(2b_n\), so the origin-centered sphere of radius \(b_n\) is the unique smallest enclosing sphere. At \(n=4\) all six vertices contact it, whereas at \(n>4\) only the two poles do.

**3. Hausdorff distance.** For compact convex bodies, \(d_H(K,L)=\sup_{\|u\|_2=1}|h_K(u)-h_L(u)|\), and \(h_{B_3}\equiv1\). Since the maximum and minimum of \(h_{P_n}\) are respectively \(b_n\) and \(b_n/\sqrt3\),
\[
d_H(P_n,B_3)=\max\{b_n-1,\ 1-b_n/\sqrt3\}.
\]
We have \(b_4^2=\pi/\sqrt3\), \(b_n\ge b_4>3-\sqrt3\), and \(b_n<2/3^{1/4}<\sqrt3\). The threshold \(b_n>3-\sqrt3\) is exactly equivalent to \(b_n-1>1-b_n/\sqrt3\). Consequently \(d_H(P_n,B_3)=b_n-1\).

**4. Strict monotonicity and volume.** The equivalent form
\[
b_n^2=\frac{4}{\sqrt3}\left(\frac\pi n\cot\frac\pi n\right)
\]
shows that \(b_n\) increases strictly with integer \(n\ge4\), because \(x\cot x\) decreases strictly on \((0,\pi/4]\): its derivative is \((\sin x\cos x-x)/\sin^2x<0\). Its limit as \(n\to\infty\) is \(b_\infty=2/3^{1/4}\). The area of the equatorial polygon is \(\frac n2a_n^2\sin(2\alpha)=2\pi/\sqrt3\); taking two pyramids of height \(b_n\) gives
\[
\operatorname{Vol}(P_n)=\frac{4\pi}{3\sqrt3}b_n,
\]
which also strictly increases, to \(8\pi/3^{7/4}\). The bodies converge in Hausdorff distance to a nonround double right circular cone with equatorial radius \(\sqrt{2/\sqrt3}\) and poles at heights \(\pm 2/3^{1/4}\).

## Verification

The accompanying `verify.py` independently constructs both the facet-normal design and the polytope's vertices for each integer \(4\le n\le40\). Using a convex-hull algorithm, it checks all \(2n\) actual triangular facet normals, unit offsets, face areas, whole surface area, volume, and sphere radii. It also compares all polynomial moments through total degree three against sphere moments, and samples additional support directions. A separate numerical sweep checks strict Hausdorff monotonicity for \(4\le n\le300\). Executing `python verify.py` passed 16,023 counted assertions; these finite checks corroborate but do not establish the infinite theorem. The complete analytic proof above supplies the unrestricted quantifiers.

## Relationship to prior work

Bajnok [2], Construction 3.3, already constructs these two-ring spherical \(3\)-designs; that combinatorial fact is not original here. An [1] associates equal-facet-area Minkowski polyhedra to spherical designs and proves a general sphericity estimate when **design strength tends to infinity**, independently of cardinality. That general result does not assert a fixed-strength facet-number monotonicity or the present explicit bipyramid metric and volume formulas. The point is to distinguish increasing the number of nodes at fixed strength from increasing design strength. Published geometry records about six-node \(2\)-design Minkowski volumes and about planar equal-area Minkowski polygon Hausdorff errors address different geometries and parameter regimes. Literature/record searches revealed no exact statement of this opposing monotonicity for the present family; historical priority is provisional, not proved by the searches.

## Limitations

The result is specific to the aligned two-ring construction, surface-area normalization \(4\pi\), and ordinary Euclidean distance to the centered unit ball. It does not assert that all fixed-strength spherical designs worsen with cardinality, that this family is extremal among all designs of the same strength or size, or that higher-strength sphericity theorems fail. The spherical \(3\)-design construction predates the result. External mathematical priority remains provisional and there has been no independent audit.

## References

1. Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570, first posted 2026-08-12. https://arxiv.org/abs/2608.11570 .
2. Béla Bajnok, *Constructions of Spherical 3-Designs*, *Graphs and Combinatorics* **14** (1998), 97–107, Construction 3.3, openly available as arXiv:2404.15544. https://arxiv.org/abs/2404.15544 .
