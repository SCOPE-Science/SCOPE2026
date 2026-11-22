# Exact convex hulls of integral epicycloids and a persistent perimeter deficit

## Finding
For every positive integer \(n\) and rolling radius \(r>0\), let
\[
z(t)=r\big((n+1)e^{it}-e^{i(n+1)t}\big),\qquad 0\le t\le2\pi.
\]
Write \(\alpha=\pi/(n+2)\). The convex hull of the complete epicycloid has exactly \(n\) flat bitangent sides, each spanning the deleted cusp interval \([2\pi j/n-\alpha,2\pi j/n+\alpha]\), and exactly \(n\) exposed, strictly convex pieces of the original curve between those intervals. Each straight side has length \(2nr\sin\alpha\). The complete convex hull has
\[
P_n=2r(n+2)^2\sin\alpha,
\]
and
\[
A_n=r^2\left[2\pi(n+1)+\frac{(n+2)(n^2+2n+2)}2\sin(2\alpha)\right].
\]
In particular, the area ratio of convex hull to enclosed epicycloid tends to \(1\) as \(n\to\infty\), while the convex-hull perimeter divided by the original curve length tends to \(\pi/4\). Hence an asymptotically negligible *relative area* modification removes a nonvanishing fraction \(1-\pi/4\) of the boundary length.

## Assumptions and scope
All statements concern the plane with its ordinary Euclidean convex hull, positive integer winding ratio \(n\ge1\), complete parameter period \([0,2\pi]\), and a positive rolling-circle radius \(r\). The convex hull is of the traced curve or, equivalently, of the compact region it encloses. Distinct cusp intervals are disjoint since \(\alpha<\pi/n\). The case \(n=1\) is the cardioid, and \(n=2\) is the nephroid. The formulas are dimensionally homogeneous under \(z\mapsto rz\).

## Proof
First take \(r=1\). Direct differentiation gives
\[
z'(t)=2(n+1)e^{i(n+2)t/2}\sin(nt/2).
\]
The signed radial sweep satisfies
\[
\operatorname{Im}(\overline{z(t)}z'(t))=(n+1)(n+2)(1-\cos nt)\ge0,
\]
so the curve is simple and star-shaped, apart from its \(n\) cusps at \(t=2\pi j/n\). Each smooth cusp-to-cusp arc has strictly increasing tangent direction and hence strictly positive signed curvature.

At the cusp at parameter zero, reflection is complex conjugation. The two symmetric parameters \(t=\pm\alpha\) give the contact points
\[
z(\pm\alpha)=(n+2)\cos\alpha\ \pm\ i n\sin\alpha.
\]
The vertical line \(x=(n+2)\cos\alpha\) is a supporting line for the *whole* epicycloid. Indeed, for
\[
x(t)=(n+1)\cos t-\cos((n+1)t),
\]
all extrema on a complete period occur either at cusps \(t=2\pi j/n\) (where \(x=n\cos t\le n\)), or at \(t=(2j+1)\pi/(n+2)\) (where \(x=(n+2)\cos t\le(n+2)\cos\alpha\)); the latter maximum is attained only at \(t=\pm\alpha\) modulo the period. The strict inequality \((n+2)\cos\alpha>n\) follows from \(\cos u\ge1-u^2/2\) and \(n+2\ge3\). Rotation by \(2\pi j/n\) gives the \(n\) bitangents, with each contact pair joined by a supporting segment of length \(2n\sin\alpha\).

Remove each of the \(n\) parameter arcs around a cusp and replace it by that chord. On a deleted cusp interval, the ordinate strictly increases from \(-n\sin\alpha\) to \(+n\sin\alpha\), and the curve lies strictly on the interior side of its bitangent. The patched Jordan curve encloses the original curve. Its tangent direction is continuous across the chord–arc contacts. Along every remaining smooth arc the tangent direction increases through exactly \(2\pi/n\):
\[
\frac{n+2}{2}\left(\frac{2\pi}{n}-2\alpha\right)=\frac{2\pi}{n}.
\]
Across each chord it is constant. Thus the patched Jordan curve has nondecreasing total turning through exactly \(2\pi\), so it bounds a convex region. All its boundary arcs and segments belong to the original curve or to exposed bitangents of that curve; consequently it is precisely the convex hull. This proves uniqueness of the listed boundary decomposition.

The unmodified full-curve length is \(L_n=8(n+1)\). On each deleted cusp interval its length is
\[
\frac{8(n+1)}n(1-\sin\alpha),
\]
while the replacement chord length is \(2n\sin\alpha\). Therefore
\[
P_n=8(n+1)\sin\alpha+2n^2\sin\alpha
=2(n+2)^2\sin\alpha.
\]
Green's theorem or direct integration of the signed radial sweep gives original enclosed area \(A_n^{\mathrm{old}}=\pi(n+1)(n+2)\). The area gained from each removed cusp interval is the region between its supporting line and the old arc:
\[
D_n=2n(n+2)\sin\alpha\cos\alpha
-\int_{-\alpha}^{\alpha}x(t)y'(t)\,dt.
\]
Here \(y'(t)=(n+1)(\cos t-\cos((n+1)t))\). Expanding this elementary trigonometric integral and using \((n+2)\alpha=\pi\) yields
\[
D_n=(n+2)\left[\frac{n^2+2n+2}{2n}\sin(2\alpha)-(n+1)\alpha\right].
\]
Adding \(nD_n\) to \(A_n^{\mathrm{old}}\), the terms proportional to \(n(n+1)\pi\) cancel, leaving precisely the asserted formula for \(A_n\). Scaling multiplies perimeter by \(r\) and area by \(r^2\).

Finally, \(\sin(\pi/(n+2))\sim\pi/(n+2)\) implies
\[
\frac{P_n}{L_n}\to\frac\pi4,
\qquad \frac{A_n}{A_n^{\mathrm{old}}}\to1.
\]
Both limits hold along positive integers, with no assumption of a continuous cusp count.

## Verification
The included `verify_epicycloid_hulls.py` independently constructs polygonal samples of complete epicycloids, computes their convex hulls with a monotone-chain algorithm, and compares convex-hull area and perimeter with the exact formulas for several small and larger cusp counts. It also checks the global supporting-line inequality on sampled parameters. These are numerical reproducibility checks, not substitutes for the analytic proof above. The script needs only the Python 3 standard library. Run `python3 verify_epicycloid_hulls.py` after extracting the package.

## Relationship to prior work
MacTutor and the Encyclopedia of Mathematics state the classical parametrization, full curve length and enclosed area. Apostol and Mnatsakanian (2009) study cycloidal and epicycloidal sector/cap area identities; the accessible institutional record has only abstract and metadata, and does not establish whether its full text contains an equivalent convex-hull quadrature. Gibert (2014) gives explicit nephroid bitangent constructions and discusses inscribed nephroids, a relevant special-case contact mechanism, but the inspected material does not state the complete all-\(n\) convex-hull boundary, its area/perimeter pair, or the different limiting area/perimeter effects. The proposed distinction is specifically about *convexification* of the complete epicycloid, not its classical original area or length. Earlier derivations of any or all of these convex-hull formulas may exist; historical priority has not been independently certified.

## Limitations
No claim is made for noninteger winding ratios, incompletely traced arcs, offset epitrochoids, or other cycloidal curves. The exact formulas do not describe curvature of the resulting straight-line segments. Numerical polygonal approximation is finite and cannot establish a global convex-hull identity on its own. A highly relevant 2009 cycloidal-area article was available only as abstract/metadata; the full-text priority comparison remains unresolved.

## References
1. T. M. Apostol and M. A. Mnatsakanian, *New Insight into Cycloidal Areas*, American Mathematical Monthly 116 (2009), 598–611. DOI: https://doi.org/10.4169/193009709X458573 ; institutional record: https://authors.library.caltech.edu/records/7wxkh-b1h64 (record dated 2009-12-04).
2. Bernard Gibert, *Inscribed Nephroids and Related Curves*, created 2014-10-23, https://bernard-gibert.fr/files/Resources/nephr.pdf.
3. MacTutor History of Mathematics, *Epicycloid*, https://mathshistory.st-andrews.ac.uk/Curves/Epicycloid/.
4. Encyclopedia of Mathematics, *Epicycloid*, https://encyclopediaofmath.org/wiki/Epicycloid.
