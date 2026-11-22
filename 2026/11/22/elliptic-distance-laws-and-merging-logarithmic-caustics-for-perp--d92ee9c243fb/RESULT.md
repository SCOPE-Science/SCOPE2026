# Elliptic distance laws and merging logarithmic caustics for perpendicular circular wires

## Finding
Let \(t\) and \(s\) be independent uniform angles in \([0,2\pi)\), and let
\[
P(t)=(\cos t,\sin t,0),\qquad Q_d(s)=(d,\cos s,\sin s),\qquad D_d=\|P-Q_d\|,\qquad d\ge0.
\]
These are two unit-speed circular wires in orthogonal planes. Their center distance is \(d\), and their circles meet exactly when \(d=0\). Define the centered squared-distance coordinate
\[
Z_d=\frac{2+d^2-D_d^2}{2},\qquad M_d=\sqrt{1+d^2},\qquad K(m)=\int_0^{\pi/2}\frac{du}{\sqrt{1-m\sin^2 u}}\quad(0\le m<1).
\]
Then \(Z_d\) has the symmetric density \(f_d\), whose two analytic branches are
\[
\boxed{f_d(z)=\begin{cases}
\displaystyle\frac{2}{\pi^2\sqrt{1+d^2-z^2}}K\!\left(\frac{1}{1+d^2-z^2}\right),& |z|<d,\\[6pt]
\displaystyle\frac{2}{\pi^2}K(1+d^2-z^2),&d<|z|<M_d,\\[6pt]
0,&|z|>M_d.
\end{cases}}
\]
For \(d=0\) only the second branch is used away from zero. The singular values \(z=\pm d\) have zero probability (the density diverges integrably there). As \(z\) approaches either support endpoint from within \([-M_d,M_d]\), the density tends to \(1/\pi\).

For each fixed \(d>0\), the two interior logarithmic singularities have sharp local forms
\[
\boxed{f_d(z)=\frac{1}{\pi^2}\log\frac{8}{d\,|z-d|}+o(1)\ (z\to d),\qquad
f_d(z)=\frac{1}{\pi^2}\log\frac{8}{d\,|z+d|}+o(1)\ (z\to-d).}
\]
At the intersecting-circle geometry \(d=0\), these two caustics merge and their logarithmic coefficient doubles:
\[
\boxed{f_0(z)=\frac{2}{\pi^2}\log\frac{4}{|z|}+o(1)\qquad(z\to0).}
\]
The **critical collision profile** is exact to leading two orders: uniformly for \(\lambda\) in compact subsets of \(\mathbb R\setminus\{-1,1\}\),
\[
\boxed{f_d(d\lambda)=\frac{2}{\pi^2}\log(1/d)+\frac{1}{\pi^2}\log\frac{16}{|1-\lambda^2|}+o(1)\qquad(d\downarrow0).}
\]
The original cross-wire distance has complete support and density
\[
\boxed{M_d-1\le D_d\le M_d+1,\qquad
 g_d(r)=r\,f_d\!\left(\frac{2+d^2-r^2}{2}\right)\quad(M_d-1<r<M_d+1).}
\]
The two density singularities in distance coordinates occur at \(r_\pm=\sqrt{2+d^2\mp 2d}\) for \(d>0\), and coincide at \(\sqrt2\) when \(d=0\). Its second and fourth moments are \(\mathbb E[D_d^2]=2+d^2\) and \(\mathbb E[D_d^4]=(2+d^2)^2+2d^2+1\). Thus \(d=\sqrt{\mathbb E[D_d^2]-2}\) is identifiable from the unlabelled cross-wire distance law. For \(d>0\), both endpoint one-sided densities exist and equal \((M_d-1)/\pi\) and \((M_d+1)/\pi\), respectively. At \(d=0\), \(\Pr(D_0\le r)\sim r^2/(2\pi)\) as \(r\downarrow0\).

## Assumptions and scope
Angles are independent and exactly uniform with respect to arclength; the circles have unit radii, occupy the specified perpendicular planes, and the center displacement is along the normal to the second circle. All statements concern Euclidean point-to-point distance, not random directional width, nearest-point distance, nor independent points sampled from filled disks. The density is understood in the Lebesgue sense, and every asymptotic explicitly specifies its fixed or jointly varying parameters.

## Proof
**1. Geometric reduction and support.** Direct expansion gives
\[
D_d^2=2+d^2-2(d\cos t+\sin t\cos s),\qquad Z_d=d\cos t+\sin t\cos s.
\]
Conditioned on \(s\), this is a phase-shifted cosine of uniform \(t\) with amplitude \(R(s)=\sqrt{d^2+\cos^2s}\). Its conditional density is exactly \(1/(\pi\sqrt{R(s)^2-z^2})\) on \(|z|<R(s)\). Since \(R(s)\) ranges from \(d\) to \(M_d\) and attains the upper bound, the claimed support of \(Z_d\) is exactly \([-M_d,M_d]\). Its monotone transformation to \(D_d\) yields the asserted distance support.

**2. Elliptic evaluation.** Averaging over the uniform \(s\) and using its fourfold symmetry gives
\[
f_d(z)=\frac{2}{\pi^2}\int_0^{\pi/2}
\frac{\mathbf1_{\{d^2+\cos^2s>z^2\}}}{\sqrt{d^2+\cos^2s-z^2}}\,ds.
\]
Write \(A=1+d^2-z^2\). If \(|z|<d\), then \(A>1\) and the integral is \(A^{-1/2}K(1/A)\). If \(d<|z|<M_d\), then \(0<A<1\); the admissible interval is \(0\le s<\arcsin\sqrt A\), and substituting \(\sin s=\sqrt A\sin u\) turns it into \(K(A)\). This proves both branches, their normalization (they were derived from an averaged conditional probability density), and their endpoint limit because \(K(0)=\pi/2\).

**3. Local singularities and collision scaling.** The standard elliptic integral expansion
\[
K(1-\eta)=\log\frac4{\sqrt\eta}+O\!\bigl(\eta\log(1/\eta)\bigr),\qquad\eta\downarrow0,
\]
comes directly by isolating a neighborhood of \(u=\pi/2\) in its defining integral (or via the arithmetic-geometric-mean representation). At \(z\to\pm d\) with \(d>0\), the relevant gap \(\eta\) on either side equals \(|d^2-z^2|+O((d^2-z^2)^2)\); the first branch has an extra factor \(A^{-1/2}=1+O(|d^2-z^2|)\). Thus \(f_d(z)=\pi^{-2}\log(16/|d^2-z^2|)+o(1)\), which gives the two stated constants by \(|d^2-z^2|=2d|z\mp d|(1+o(1))\). At \(d=0\) the gap is \(z^2\), doubling the logarithmic coefficient. For \(z=d\lambda\) on a compact set avoiding \(\pm1\), the gap is \(d^2|1-\lambda^2|\) times a factor \(1+O(d^2)\), uniformly; the claimed crossover follows from the same expansion.

**4. Density, moments, and singular endpoint.** The change of variables \(z=(2+d^2-r^2)/2\), with \(|dz/dr|=r\), yields the distance density. The cross terms of \(Z_d=d\cos t+\sin t\cos s\) average to zero, so \(\mathbb EZ_d=0\) and \(\mathbb EZ_d^2=d^2/2+1/4\). Squaring \(D_d^2=2+d^2-2Z_d\) gives the exact second/fourth moments. The inversion formula follows since \(d\ge0\). At positive \(d\) the endpoint distances are positive and \(f_d(\pm M_d)=1/\pi\), giving the two finite endpoint densities. At \(d=0\), \(r\downarrow0\) implies \(z=1-r^2/2\) and \(g_0(r)\sim r/\pi\), which integrates to \(r^2/(2\pi)\).

## Verification
A standalone standard-library Python checker `checker.py` and its actual replay output `CHECKER_OUTPUT.txt` are included. They compare the elliptic expression to an independent direct conditional angular quadrature, test both sides of the logarithmic caustics, the fixed-scale collision profile, the zero-offset singularity, and moments from seeded independent angle samples. The checker passed 61 diagnostics. These finite diagnostics are supplementary only; the exact integral reductions and asymptotic bounds above supply the infinite-domain proof.

## Relationship to prior work
Finch's *Convex Hull of Two Orthogonal Disks* (arXiv:1211.4514, first public 2012-11-19) studies related perpendicular disk configurations, their convex-hull volume, surface area, and mean width. The full article's abstract and sections on convex-hull support show a different random object: direction-uniform supporting-plane widths, not the distribution of cross-wire distances for two independent arclength-uniform boundary points. Bäsel and Dirnböck's *The Extended Oloid and Its Inscribed Quadrics* (arXiv:1503.07399, first public 2015) treats the classical perpendicular-circle hull and its developable geometry; it does not state an independent pairwise random-distance law. Classical same-circle line picking has a different one-dimensional chord density. The exact elliptic cross-wire law, parameter-dependent split caustics and their collision profile were not located in the checked primary works or in the indexed comparisons described in `AUDIT.json`. This is an evidence-limited priority assessment, not a uniqueness or historical-priority certificate.

## Limitations
The result treats equal unit radii, this one-parameter relative position, independent arclength-uniform endpoints, and Euclidean distance. It does not cover arbitrary offsets/tilts, random points on disk interiors, or random supporting-plane widths. The logarithmic expansion is not uniform through \(\lambda=\pm1\), where the limiting density is infinite. Known general elliptic-integral identities could imply special cases; independent literature checking remains warranted.

## References
1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first submitted 2012-11-19), https://arxiv.org/abs/1211.4514 .
2. U. Bäsel and H. Dirnböck, *The Extended Oloid and Its Inscribed Quadrics*, arXiv:1503.07399 (2015), https://arxiv.org/abs/1503.07399 .
3. E. W. Weisstein, *Circle Line Picking*, MathWorld, https://mathworld.wolfram.com/CircleLinePicking.html (same-circle comparator, not cross-wire distribution).
