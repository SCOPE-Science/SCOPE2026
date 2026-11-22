# A logarithmic apex anomaly in short Euclidean surface chords of circular cones

## Finding

Let \(0<q<1\), \(L>0\), and let \(S_{q,L}\subset\mathbb R^3\) be the **lateral surface only** of the finite right circular cone parametrized by
\[
X(s,\theta)=(qs\cos\theta,qs\sin\theta,\sqrt{1-q^2}\,s),\qquad 0\le s\le L,\quad 0\le\theta<2\pi.
\]
The base radius is \(R=qL\), the height is \(H=L\sqrt{1-q^2}\), the lateral area is \(A=\pi qL^2\), and the rim perimeter is \(P=2\pi qL\). For two independent surface-area-uniform points \(U,V\in S_{q,L}\), let \(F_{q,L}(r)=\Pr(\|U-V\|_2\le r)\). Then, with the cone fixed and \(r\downarrow0\),
\[
\boxed{F_{q,L}(r)=\frac{\pi}{A}r^2-\frac{2P}{3A^2}r^3+\frac{\pi^2(1-q^2)}{16q A^2}\,r^4\log\frac{L}{r}+O_{q,L}(r^4).}
\]
The logarithmic coefficient is **strictly positive at every proper opening**, whereas it vanishes at the planar disk endpoint \(q=1\). It arises from the non-integrable square of the lateral principal curvature near the apex, rather than from the smooth circular rim.

In particular, if \(A\) is recovered from the leading probability coefficient and
\[
B:=A^2\lim_{r\downarrow0}\frac{F_{q,L}(r)-(\pi/A)r^2+(2P/3A^2)r^3}{r^4\log(L/r)},
\]
then \(B=\pi^2(1-q^2)/(16q)>0\). Put \(\beta=16B/\pi^2\). The cone is reconstructed without an external length scale by
\[
\boxed{q=\frac{2}{\sqrt{\beta^2+4}+\beta},\qquad L=\sqrt{\frac{A}{\pi q}},\qquad R=qL,\qquad H=L\sqrt{1-q^2}.}
\]
Here the displayed limit uses the rim coefficient already determined from the full distance law. The rim coefficient itself also encodes \(L\), so this reconstruction is an **alternative geometric signature**, not a minimal-statistic optimality claim.

## Assumptions and scope

The cone is nondegenerate with fixed \(0<q<1\) and \(L>0\). Surface-area uniform means normalized two-dimensional Hausdorff measure, so each point has independent azimuth \(\Theta\sim\mathrm{Unif}[0,2\pi)\) and slant coordinate with density \(2s/L^2\) on \([0,L]\). The base disk is **excluded**; adding it changes both area and lower-order coefficients. The apex itself has area zero. Distances are straight-line distances in the ambient Euclidean three-space, not intrinsic shortest paths along the cone. The error constant is allowed to depend on the fixed opening and slant length; no uniform estimate as \(q\to0\) or \(q\to1\) is asserted. \(\log(L/r)\) can be replaced by \(\log(1/r)\) only after a unit of length is specified, with a changed \(O(r^4)\) constant.

## Proof

**1. Exact two-dimensional representation.** Let the two slant coordinates be \(u,v\). Their squared Euclidean separation, conditional on azimuth difference \(\varphi\), is
\[
D^2=(u-v)^2+2q^2uv(1-\cos\varphi).
\]
Since \(u,v\) have density \(2u/L^2,2v/L^2\), and \(\varphi\) is uniform modulo \(2\pi\), conditioning yields, for \(|u-v|<r\), the exact angular probability
\[
\frac2\pi\arcsin\!\left(\min\!\left\{1,\frac{\sqrt{r^2-(u-v)^2}}{2q\sqrt{uv}}\right\}\right).
\]
The values at \(uv=0\) do not matter because they form a measure-zero set. Put \(h=u-v\), \(x=(u+v)/2\), and \(y=\sqrt{x^2-h^2/4}=\sqrt{uv}\). This linear change has absolute Jacobian one. For \(0<r<L\),
\[
F_{q,L}(r)=\frac8{\pi L^4}\int_{-r}^{r}\int_{|h|/2}^{L-|h|/2}y^2\arcsin\!\left(\min\left\{1,\frac{\sqrt{r^2-h^2}}{2qy}\right\}\right)\,dx\,dh.
\tag{1}
\]
Formula (1) is valid without a small-angle approximation. It also explicitly fixes the convention for the angular region in which every azimuth difference is admissible.

**2. Local and macroscopic ranges.** Fix a constant \(C>\max\{4,4/q\}\). For sufficiently small \(r\), split the \(x\)-integration at \(Cr\). The subregion \(x\le Cr\) contributes \(O_{q,L}(r^4)\): the integrand before normalization is at most \(\pi x^2/2\), and the \(x\)- and \(h\)-ranges are each of length \(O(r)\). On \(x\ge Cr\), the arcsine argument is uniformly at most \(1/2\); with \(k=\sqrt{r^2-h^2}/(2q)\), uniformly in \(|h|\le r\),
\[
\begin{split}
y^2\arcsin(k/y)&=ky+\frac{k^3}{6y}+O_q(r^5/x^3)\\
&=kx+\frac{-kh^2/8+k^3/6}{x}+O_q(r^5/x^3).
\end{split}
\tag{2}
\]
Indeed \(y=x-h^2/(8x)+O(h^4/x^3)\), \(y^{-1}=x^{-1}+O(h^2/x^3)\), and \(\arcsin z=z+z^3/6+O(z^5)\). After integration over \(x\ge Cr\) and \(|h|\le r\), the error in (2) is \(O_{q,L}(r^4)\), since \(\int_{Cr}^L x^{-3}\,dx=O_q(r^{-2})\). The difference between \(\log((L-|h|/2)/(Cr))\) and \(\log(L/r)\) is uniformly bounded, producing only \(O(r^4)\) after integration against the logarithmic coefficient.

**3. Quadratic and cubic coefficients.** Integrating \(kx\) in (2) from \(Cr\) to \(L-|h|/2\) gives
\[
\frac{k}{2}\left(L-\frac{|h|}{2}\right)^2+O_q(r^3).
\]
The \(O_q(r^3)\) is pointwise in \(h\), hence \(O_q(r^4)\) after the remaining integral. Use the elementary identities
\[
\int_{-r}^r\sqrt{r^2-h^2}\,dh=\frac\pi2r^2,\qquad
\int_{-r}^r|h|\sqrt{r^2-h^2}\,dh=\frac23r^3.
\]
Multiplication by \(8/(\pi L^4)\) gives respectively \(r^2/(qL^2)=\pi r^2/A\) and \(-4r^3/(3\pi qL^3)=-2Pr^3/(3A^2)\).

**4. The logarithmic coefficient and the remainder.** The \(x^{-1}\) term in (2) gives, modulo \(O_{q,L}(r^4)\),
\[
\frac8{\pi L^4}\log\frac Lr\int_{-r}^r\left(-\frac{kh^2}{8}+\frac{k^3}{6}\right)dh.
\]
The required two further definite integrals are
\[
\int_{-r}^rh^2\sqrt{r^2-h^2}\,dh=\frac\pi8r^4,\qquad
\int_{-r}^r(r^2-h^2)^{3/2}\,dh=\frac{3\pi}{8}r^4.
\]
Substituting \(k=\sqrt{r^2-h^2}/(2q)\) yields
\[
\frac{1-q^2}{16q^3L^4}r^4\log\frac Lr
=\frac{\pi^2(1-q^2)}{16qA^2}r^4\log\frac Lr.
\]
All omitted integrations have total error \(O_{q,L}(r^4)\), establishing the stated expansion with the full correct remainder order.

**5. Sign, disk boundary and reconstruction.** Since \(0<q<1\), the logarithmic coefficient is strictly positive. At \(q=1\), the parametrized cone becomes a planar disk; its standard circular-disk pair-distance expansion is analytic at this order and has zero logarithmic term. For the positive cone coefficient, \(\beta=(1-q^2)/q\) is strictly decreasing in \(q\in(0,1)\); solving the quadratic \(q^2+\beta q-1=0\) gives the displayed unique inverse. The leading \(r^2\) coefficient gives \(A\), hence \(L\), \(R\) and \(H\).

As an independent geometric check on the logarithmic constant, the two principal curvatures away from the apex are \(0\) and \(\sqrt{1-q^2}/(qs)\). The local Euclidean-ball surface area correction is \(\pi r^4(\kappa_1-\kappa_2)^2/32\); its area integral contributes a \(\log(L/r)\) factor because the surface measure is \(qs\,ds\,d\theta\). This yields precisely the same coefficient, but the full proof above does not require assuming a uniform curvature expansion near the singular apex.

## Verification

The standalone program `checks/verify_cone_short_chords.py`, with dependency stated in `requirements.txt`, evaluates the **exact** conditional-angle double integral using Gauss–Legendre quadrature with an analytic full-azimuth sector and a square-root-regularized residual sector. It checks the predicted logarithmic slopes at three distinct cone openings, compares them with the independent local-curvature coefficient, tests the explicit inverse reconstruction, and independently draws 200,000 Euclidean pairs to compare a finite-radius CDF. It returned `CONE_EXTRINSIC_SMALL_CHORD_LOG_CHECKS_OK numerical=9 inversion=3 sampling=200000`. These finite tests support arithmetic and normalization; the uniform error argument in the proof, not numerical extrapolation, establishes the asymptotic theorem.

## Relationship to prior work

Guigues (arXiv:1406.0005, first posted 30 May 2014) studies Euclidean distance **from a fixed point** to a variable sampled in disks, balls, line segments or polyhedral boundaries, including an exact algorithm in the last case. Its object is not the pair-distance law of a curved cone surface; its material on surface-distance computation is a motivation, not the claimed log coefficient.

Gille (2000) analyzed short random-line **chord-length distributions for solid circular cones** and explicitly noted a logarithmic singularity associated with edges and the tip. That historical logarithm is **not** claimed as new. However, the full paper could not be obtained during the comparison; an unnoticed relation to the present surface-point statistic is a significant residual priority risk. A line-invariant chord measure and a pair of independently surface-uniform points are distinct measures, so the abstract alone does not imply the displayed coefficient.

Ma and Torquato (arXiv:1808.01326, Sections III.A and Appendix A) analyze leading surface–surface correlation functions. Their text explicitly confines the surface–surface expansion to leading order and excludes conical singularities from the smooth local argument; it does not establish the present finite-cone fourth-order logarithm. Their work supports the distinction between leading smooth-interface behavior and subleading singularity-sensitive terms.

The publicly accessible claims *The exact short Euclidean surface-pair law and its dihedral bending coefficient* concern **polyhedral** surfaces and a polynomial short-range law. *Exact small-distance law on flat cone surfaces and Euclidean orbifold signature recovery* concerns **intrinsic geodesic** distance on compact boundaryless flat cone surfaces. The former has faceted hinge geometry; the latter uses an incompatible metric and no rim. Neither statement subsumes the curved lateral cone's extrinsic \(r^4\log(1/r)\) correction. Older specialized scattering literature could still affect priority.

## Limitations

This is a fixed-cone small-radius asymptotic, not an exact all-distance distribution and not a uniform estimate over openings. The base disk is excluded, and adding it alters the local geometry at the rim. The \(O(r^4)\) term is not resolved to a finite constant. The logarithmic coefficient is another identification route, not proof that fewer leading coefficients cannot identify the cone. The comparison with Gille's paper is incomplete because its full text was inaccessible. Independently validated mathematical priority and proof certification have not been performed.

## References

1. V. Guigues, *Exact computation of the CDF of the Euclidean distance between a point and a random variable uniformly distributed in disks, balls, or polyhedrons and application to PSHA*, arXiv:1406.0005, first public version 2014-05-30, https://arxiv.org/abs/1406.0005 . Primary full text, especially introduction and Section 5, inspected.
2. W. Gille, *Analysis of the chord length distribution of the right circular cone for small chord lengths*, Computers & Mathematics with Applications **40** (2000), 1027–1035, DOI: 10.1016/S0898-1221(00)85013-0 . Accessible abstract/catalogue only; full article unavailable in this comparison.
3. Z. Ma and S. Torquato, *Precise algorithms to compute surface correlation functions of two-phase heterogeneous media and their applications*, arXiv:1808.01326, first public version 2018-07-31, https://arxiv.org/abs/1808.01326 . Primary full text inspected, Section III.A and Appendix A.
4. *The exact short Euclidean surface-pair law and its dihedral bending coefficient*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-exact-short-euclidean-surface-pair-law-and-its-dihedral-bend--61a02a61804e ; RESULT.md inspected.
5. *Exact small-distance law on flat cone surfaces and Euclidean orbifold signature recovery*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-small-distance-law-on-flat-cone-surfaces-and-euclidean-orb--81c24c6429e8 ; RESULT.md inspected.
