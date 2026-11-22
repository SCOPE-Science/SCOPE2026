# Sharp obliquity law for isotropic width variance of circular cylinders

## Finding
Fix a disk radius \(r>0\), generator length \(\ell>0\), and inclination \(0\le\theta<\pi/2\). Let
\[
K_{r,\ell,\theta}=\{(x,y,0):x^2+y^2\le r^2\}+[0,\ell(0,\sin\theta,\cos\theta)]\subset\mathbb R^3.
\]
This is a solid oblique circular cylinder, with the right circular cylinder at \(\theta=0\). For a Haar-uniform unoriented line direction \(U\in S^2/\{\pm1\}\), let \(W_\theta\) be the length of the orthogonal projection of \(K_{r,\ell,\theta}\) onto that line. Define the complete elliptic integrals, using the **parameter** rather than the modulus,
\[
\mathbf K(m)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-m\sin^2\phi}},\qquad
\mathbf E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\phi}\,d\phi.
\]
With \(m=\sin^2\theta\in[0,1)\), the exact first and second moments are
\[
\boxed{\mathbb EW_\theta=\frac{\pi r+\ell}{2}},\qquad
\boxed{\mathbb EW_\theta^2=\frac{8r^2+\ell^2}{3}+\frac{8r\ell}{3\pi}\bigl[2\mathbf E(m)-(1-m)\mathbf K(m)\bigr]}.
\]
In particular, the mean is independent of inclination, but the variance \(V(m)=\operatorname{Var}(W_\theta)\) is **strictly increasing in \(m\)**. More sharply, for all \(0\le m_1<m_2<1\),
\[
\boxed{\frac{r\ell}{3}(m_2-m_1)\le V(m_2)-V(m_1)
\le\frac{4r\ell}{3\pi}(m_2-m_1)}.
\]
Both slope constants are globally best possible, in the limits \(m\downarrow0\) and \(m\uparrow1\), respectively. The smallest variance occurs uniquely at the right cylinder. The supremum, approached as the cylinder flattens to a planar stadium, exceeds that minimum by the exact positive amount
\[
\boxed{\sup_{0\le m<1}V(m)-V(0)=\frac{4r\ell}{3}\left(\frac4\pi-1\right)}.
\]
For known \(r,\ell\), the single population observable \(\operatorname{Var}(W_\theta)\) therefore determines the absolute inclination \(\theta\) uniquely and with the stated sharp inverse-stability bounds in \(\sin^2\theta\).

## Assumptions and scope
Widths are Euclidean one-dimensional projection lengths, not intrinsic distances, planar shadow areas or random material-chord lengths. Directions are sampled from normalized spherical area; replacing a unit direction by its negative does not change width. The disk and interval form a Minkowski sum, and the generator has positive normal component \(\ell\cos\theta\), so the body is full-dimensional for \(\theta<\pi/2\). The limiting \(\theta=\pi/2\) body is the planar stadium, used only to state a sharp unattained supremum within the full-dimensional family. The radius and generator length are held fixed when varying inclination. The inverse claim presumes these two lengths known; it is not an assertion that variance alone determines all three geometric parameters.

## Proof
**1. Exact support width and normalization.** Additivity of support functions under Minkowski addition gives, for a unit vector \(u=(u_1,u_2,u_3)\),
\[
w_{K_{r,\ell,\theta}}(u)=2r\sqrt{1-u_3^2}+\ell\lvert\sin\theta\,u_2+\cos\theta\,u_3\rvert.
\tag{1}
\]
For \(U\) uniform on \(S^2\), each fixed unit-vector projection has second moment \(1/3\) and absolute first moment \(1/2\); moreover \(U_3\) is uniform on \([-1,1]\), so
\[
\mathbb E\sqrt{1-U_3^2}=\pi/4,\qquad
\mathbb E(1-U_3^2)=2/3.
\]
This yields the asserted mean. Squaring (1) reduces the second moment to
\[
\mathbb EW_\theta^2=\frac{8r^2+\ell^2}{3}+4r\ell\,F(\theta),
\quad F(\theta)=\mathbb E\left[\sqrt{1-U_3^2}\,\lvert\sin\theta\,U_2+\cos\theta\,U_3\rvert\right].
\tag{2}
\]

**2. Angular integration.** Put \(s=\sin\theta\), \(c=\cos\theta\), \(m=s^2\). Conditional on \(t=\lvert U_3\rvert\), which is uniform on \([0,1]\), the remaining azimuth is uniform. The standard integral of \(\lvert A+B\cos\phi\rvert\) gives
\[
\frac1{2\pi}\int_0^{2\pi}\lvert ct+s\sqrt{1-t^2}\cos\phi\rvert\,d\phi
=\begin{cases}
\dfrac2\pi\left(\sqrt{s^2-t^2}+ct\arcsin\dfrac{ct}{s\sqrt{1-t^2}}\right),&0\le t<s,\\
ct,&s\le t\le1.
\end{cases}
\tag{3}
\]
For \(s=0\), equation (2) directly gives \(F(0)=1/3\). For \(0<s<1\), multiply (3) by \(\sqrt{1-t^2}\) and integrate in \(t\). Integrating the arcsine term by parts, using
\[
\frac{d}{dt}\arcsin\frac{ct}{s\sqrt{1-t^2}}
=\frac{c}{(1-t^2)\sqrt{s^2-t^2}},
\]
cancels the \(ct\) contribution from \(t\ge s\). The result is
\[
F(\theta)=\frac2\pi\left[
\int_0^s\sqrt{(1-t^2)(s^2-t^2)}\,dt
+\frac{c^2}{3}\int_0^s\frac{\sqrt{1-t^2}}{\sqrt{s^2-t^2}}\,dt\right].
\tag{4}
\]
With \(t=s\sin\phi\), the second integral is \(\mathbf E(m)\). The first is \(m\int_0^{\pi/2}\cos^2\phi\sqrt{1-m\sin^2\phi}\,d\phi\). The classical integration-by-parts identity
\[
\int_0^{\pi/2}(1-m\sin^2\phi)^{3/2}\,d\phi
=\frac{2(2-m)\mathbf E(m)-(1-m)\mathbf K(m)}3
\]
then gives
\[
m\int_0^{\pi/2}\cos^2\phi\sqrt{1-m\sin^2\phi}\,d\phi
=\frac{(1+m)\mathbf E(m)-(1-m)\mathbf K(m)}3.
\]
Thus
\[
\boxed{F(\theta)=\frac2{3\pi}\bigl[2\mathbf E(m)-(1-m)\mathbf K(m)\bigr]}.
\tag{5}
\]
Substitution in (2) establishes the exact second moment. The endpoint limits are continuous: \(F(0)=1/3\), and \(\lim_{m\uparrow1}F(m)=4/(3\pi)\) because \((1-m)\mathbf K(m)\to0\) and \(\mathbf E(1)=1\).

**3. Sharp monotonicity and quantitative inverse.** Differentiating (5), with the standard derivative identities of complete elliptic integrals, yields
\[
\frac{dF}{dm}=
\frac{\mathbf E(m)-(1-m)\mathbf K(m)}{3\pi m}
=\frac1{3\pi}\int_0^{\pi/2}\frac{\cos^2\phi}{\sqrt{1-m\sin^2\phi}}\,d\phi.
\tag{6}
\]
The integral is strictly positive. Since for \(m\in[0,1)\),
\[
\cos\phi\le\sqrt{1-m\sin^2\phi}\le1
\quad(0\le\phi\le\pi/2),
\]
(6) gives \(1/12\le dF/dm\le1/(3\pi)\). Its lower limit is \(1/12\) at \(m=0\), and its upper limit is \(1/(3\pi)\) as \(m\uparrow1\). Multiplication by \(4r\ell\), integration over \([m_1,m_2]\), and subtraction of the constant squared mean prove the two-sided sharp variance bounds. Strict monotonicity gives the inverse assertion; evaluating (5) at the endpoints gives the exact supremum gap. There is no claim that the planar limiting body is a three-dimensional cylinder.

## Verification
Run `python verify_oblique_width.py` in an ordinary Python 3 environment. The standalone diagnostic uses only the standard library. It compares (5) with a separately derived azimuthally averaged sphere integral at eight inclinations, checks the endpoint constants, tests the sharp finite-difference bounds on three independently scaled families, and compares mean and second moment with direct fixed-seed Cartesian spherical samples. It reports `OBLIQUE_CYLINDER_WIDTH_CHECKS_OK 79`. These numerical tests are finite diagnostics, not substitutes for the analytic proof for all real parameters.

## Relationship to prior work
Finch, *Oblique Circular Cones and Cylinders* (arXiv:1212.5946, initially posted December 24, 2012), derives the inclination-independent **mean width** of these oblique cylinders, as well as their surface area, but does not derive the orientation-dependent **second moment**, its elliptic-integral formula, or the sharp monotonicity and inverse-stability law. The mean formula here is a confirmation of that known result, not asserted as a novelty.

The previously published note *Exact random-width law and sharp inverse ambiguity for right circular cylinders* gives the full law for **orthogonal** generators; it covers the endpoint \(m=0\), not any nonzero tilt. The published *A sharp width-fluctuation gap and rigidity law for Euclidean right prisms* explicitly requires orthogonal products, hence does not imply the oblique moment formula. Gesmundo and Meroni, *The Geometry of Discotopes* (arXiv:2111.01241), establish Minkowski-sum support identities and algebraic face geometry but not the claimed spherical mixed-width expectation. Vickers' paper on random projected **areas** of ellipsoids and cylinders studies a different observable, not the one-dimensional projection-width variance. A relevant general zonoid correlation identity might imply part of (5), and comprehensive historical priority is not established.

## Limitations
The conclusion applies to solid circular cylinders formed from a planar disk and one fixed-length generator, with isotropic viewing directions and known disk radius and generator length for inverse recovery. It does not establish the complete directional-width CDF for general oblique cylinders, nor variance extremality at fixed height, surface area, or volume. The upper equality occurs only in the degenerate planar limit. Independent mathematical audit and comprehensive historical-priority validation have not been performed.

## References
1. Steven R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1, first public December 24, 2012; relevant §1 and §1.1. https://arxiv.org/abs/1212.5946 and https://arxiv.org/html/1212.5946.
2. *Exact random-width law and sharp inverse ambiguity for right circular cylinders*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-random-width-law-and-sharp-inverse-ambiguity-for-right-cir--385986078a70.
3. *A sharp width-fluctuation gap and rigidity law for Euclidean right prisms*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-width-fluctuation-gap-and-rigidity-law-for-euclidean-rig--0823a9ee8045.
4. Fulvio Gesmundo and Chiara Meroni, *The Geometry of Discotopes*, arXiv:2111.01241v1, first public November 1, 2021; §§1–3. https://arxiv.org/abs/2111.01241.
5. Glenn Vickers, *The projected areas of ellipsoids and cylinders*, Powder Technology 86 (1996), 197–204, https://doi.org/10.1016/0032-5910(95)03049-2 (abstract accessible; full text not inspected).
