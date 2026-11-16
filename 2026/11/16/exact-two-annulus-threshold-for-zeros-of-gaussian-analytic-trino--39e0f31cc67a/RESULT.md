# Exact two-annulus threshold for zeros of Gaussian analytic trinomials

## Finding
Let \(m\ge2\) be an integer and \(a>0\). If \(\xi_0,\xi_1,\xi_2\) are independent standard circular complex Gaussians, set
\[
P_{m,a}(z)=\xi_0+\sqrt a\,\xi_1 z^m+\xi_2 z^{2m}.
\]
The expected zero-counting measure has continuous, rotation-invariant planar density \(\rho_{m,a}(|z|)\) with respect to Lebesgue area. For \(r>0\), writing \(x=2m\log r\),
\[
\rho_{m,a}(r)=\frac{2m^2}{\pi r^2}\frac{a\cosh x+2}{(a+2\cosh x)^2}.
\]
For every \(m\ge2\), let \(u_m>1\) be the **unique** solution of
\[
4m^2(u_m-1)^3=4u_m^3-1,
\]
and put \(a_m=4u_m^{3/2}\). Then \(\rho_{m,a}\), as a function of radius \(r>0\), has exactly one strict local maximum if \(0<a\le a_m\), and exactly two strict local maxima if \(a>a_m\). For \(a>a_m\), they occur at one radius below one and one above one, separated by one strict local minimum. At \(a=a_m\), an additional stationary point above unit radius is a cubic shoulder, **not** an extremum. For \(0<a<a_m\) there is no such additional stationary point. The center has density zero and is not counted as a maximum.

The threshold is explicit algebraically for every degree, with
\[
a_m=4+6(3/4)^{1/3}m^{-2/3}+O(m^{-4/3})\qquad(m\to\infty).
\]
The two additional stationary radii split by an ordinary square-root fold at \(a_m\), as quantified in the proof.

## Assumptions and scope
The three Gaussian coefficients are independent, centered, circular, and normalized by \(\mathbb E|\xi_j|^2=1\). Parameters satisfy \(m\in\{2,3,\ldots\}\), \(a\in(0,\infty)\). The parameter \(a\) is the **variance** of the middle monomial, not its standard deviation. Density means expected zeros per unit **planar area**; it is not the density of the random radial coordinate, which includes a radial Jacobian. The classification is for the expectation, not the realized random number of zero rings.

## Proof
**1. Expected density and normalization.** The covariance on the diagonal is
\[
K(z,z)=\mathbb E|P_{m,a}(z)|^2=1+a|z|^{2m}+|z|^{4m}>0.
\]
At fixed \(z\), \(P_{m,a}(z)\) is circular Gaussian of variance \(K(z,z)\), so \(\mathbb E\log|P_{m,a}(z)|=\tfrac12\log K(z,z)+C\) with a universal finite constant \(C\). Since \(\Delta\log|P|=2\pi\sum_{P(\zeta)=0}\delta_\zeta\) in distributions, taking expectations yields the Edelman--Kostlan formula
\[
\rho_{m,a}(r)=\frac1{4\pi}\Delta\log(1+a r^{2m}+r^{4m}).
\]
There is no atom at the origin since \(\xi_0\ne0\) almost surely. Writing \(x=2m\log r\), \(r^{2m}=e^x\), and \(K=e^x(a+2\cosh x)\), radial differentiation gives
\[
\rho_{m,a}(r)=\frac{m^2}{\pi r^2}\frac{d^2}{dx^2}\log(a+2\cosh x)
=\frac{2m^2}{\pi r^2}\frac{a\cosh x+2}{(a+2\cosh x)^2}.
\]
It is strictly positive for \(r>0\), tends to zero as \(r\downarrow0\) for \(m\ge2\), and tends to zero as \(r\to\infty\). Independently, the expected number of zeros in the disk \(|z|<r\) is \(m(a r^{2m}+2r^{4m})/(1+a r^{2m}+r^{4m})\), tending to the correct total degree \(2m\).

**2. Derivative geometry.** Define the odd function
\[
h_a(x)=\sinh x\left(\frac{a}{a\cosh x+2}-\frac4{a+2\cosh x}\right).
\]
Because \(r^{-2}=e^{-x/m}\),
\[
\frac{d}{dx}\log \rho_{m,a}(e^{x/(2m)})=h_a(x)-\frac1m.
\]
Writing \(c=\cosh x\), its derivative simplifies exactly to
\[
h_a'(x)=\frac{a(a+2c)}{(ac+2)^2}-\frac{4(ac+2)}{(a+2c)^2}.
\]
Set \(t=(a/4)^{1/3}\). The sign of \(h_a'(x)\) is the sign of the affine function \(t(a+2c)-(ac+2)\), because the two terms in the derivative are positive multiples of cubes of that comparison. Thus \(h_a\) has at most one turning point for \(x>0\). Further, \(h_a'(0)=(a-4)/(a+2)\), \(h_a(0)=0\), and \(\lim_{x\to+\infty}h_a(x)=-1\) for every fixed \(a>0\). If \(a<\sqrt2\), its unique turning point is a minimum below \(-1\); for \(\sqrt2\le a\le4\), it is decreasing; for \(a>4\), its unique turning point is a strict maximum. In every case \(h_a(y)=-1/m\) has exactly one solution \(y>0\), because \(-1<-1/m<0\). By oddness, \(h_a(x)=1/m\) consequently has exactly one solution \(x<0\). This is always a strict local maximum of the density.

For \(x>0\), elementary simplification gives
\[
h_a(x)=\frac{\sinh x\,[a^2-8-2a\cosh x]}{(a\cosh x+2)(a+2\cosh x)}.
\]
It is nonpositive on \(x>0\) if \(a\le4\). For \(a>4\), it is positive exactly on
\(0<x<\operatorname{arcosh}((a^2-8)/(2a))\), where its unique strict maximum occurs at
\[
c_*(a)=\cosh x_*(a)=\frac{2t^4-1}{t(2t^2-1)},\qquad t=(a/4)^{1/3}>1.
\]
Substitution gives the exact peak height
\[
H(a)=h_a(x_*(a))=\frac{2(t^2-1)^{3/2}}{\sqrt{4t^6-1}}.
\]
It increases strictly from \(0\) to \(1\) as \(t\) runs from \(1\) to infinity: differentiation of \(\log H\) in \(u=t^2>1\) has positive sign \(4u^2-1\). Since \(1/m\in(0,1)\), the equation \(H(a)=1/m\) has precisely one solution. Squaring (both sides are positive) and setting \(u=t^2\) yields \(4m^2(u-1)^3=4u^3-1\). For \(a<a_m\), \(h_a(x)<1/m\) on \(x>0\); at equality it touches the level once without changing sign; for \(a>a_m\), it crosses this level twice. As \(h_a-1/m\) is the logarithmic derivative of the positive density, its sign changes give respectively zero, one degenerate, or two additional positive-\(x\) stationary radii: first a strict minimum, then a strict maximum in the supercritical case. Together with the unique negative-\(x\) maximum, this proves the classification and all boundary cases.

**3. Critical contact and asymptotics.** At \(a=a_m\), the maximum of \(h_a\) is nondegenerate because the affine comparison for \(h_a'\) crosses zero transversely in \(c=\cosh x\) with \(x>0\). Moreover
\[
\partial_a h_a(x)=\sinh x\left[\frac2{(a\cosh x+2)^2}+\frac4{(a+2\cosh x)^2}\right]>0\quad(x>0).
\]
Writing \(x_m=x_*(a_m)\), Taylor expansion at the critical pair gives the two new stationary logarithmic radii as
\[
x_\pm(a)=x_m\pm C_m\sqrt{a-a_m}+O(a-a_m),\qquad C_m=\sqrt{\frac{-2\partial_a h_{a_m}(x_m)}{h_{a_m}''(x_m)}}>0.
\]
At criticality the logarithmic density derivative vanishes quadratically, so the stationary point has cubic contact, not an extra peak. Finally put \(u_m=1+v_m\). The defining cubic reads \(4m^2v_m^3=3+12v_m+12v_m^2+4v_m^3\), whence \(v_m=(3/4)^{1/3}m^{-2/3}+O(m^{-4/3})\); expansion of \(4(1+v_m)^{3/2}\) proves the displayed \(a_m\) asymptotic.

## Verification
The included `CHECK.py` uses the Python standard library only. Running `python CHECK.py` checks two independent density expressions, the exact derivative identity, the algebraic critical equation and its tangent condition, representative root counts on either side of the threshold, and the large-degree scaling. A finite grid of assertions is supportive numerical evidence, not a proof of global root counts; the proof above uses exact sign analysis. In a direct replay, 149 assertions passed.

## Relationship to prior work
The expected-zero identity \(\rho=(4\pi)^{-1}\Delta\log K\) is classical (Edelman--Kostlan); it is not claimed as new. Kiro and Nishry (2021) give general covariance-kernel formulas and variance estimates for Gaussian Taylor-series zeros. Those formulas supply the starting point but do not identify the sharp one- to two-annulus transition for the variance-tuned three-monomial ensemble, the all-degree cubic threshold, or its \(m^{-2/3}\) displacement. Kawada (2026) studies universal radial laws for dense iid-coefficient random polynomials; those asymptotic laws do not cover this sparse, nonidentically weighted finite-degree model. Related deterministic Fock-intensity and Fock concentration mode transitions concern different mathematical quantities; none of their checked statements implies this expected-zero density phase diagram.

## Limitations
The result classifies **expected planar intensity**, not a typical realization, conditional zero distributions, higher correlations, or the radial zero-count density. The ensemble has exactly three independent circular Gaussian coefficients in degrees \(0,m,2m\), with real positive middle variance. No general claim for arbitrary degree triples or non-Gaussian laws is made. General covariance formulas exist; the contribution is the sharp global modality analysis. An equivalent special case in older sparse-polynomial or exponential-family literature remains possible, and no independent review has been performed.

## References
1. S. Kawada, *Universal Radial Laws for Random Polynomials: Erdős Problem #522 and Non-Universal Fluctuations*, arXiv:2610.11324 (first posted 2026-10-08), https://arxiv.org/abs/2610.11324.
2. A. Kiro and A. Nishry, *Fluctuations for zeros of Gaussian Taylor series*, J. London Math. Soc. 104 (2021), 1172–1203, https://doi.org/10.1112/jlms.12457.
3. A. Edelman and E. Kostlan, *How many zeros of a random polynomial are real?*, Bull. Amer. Math. Soc. 32 (1995), 1–37. The expectation identity is also derived directly above for the present complex-Gaussian model.
