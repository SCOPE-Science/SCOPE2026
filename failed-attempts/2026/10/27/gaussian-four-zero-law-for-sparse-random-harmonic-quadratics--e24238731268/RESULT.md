# Gaussian four-zero law for sparse random harmonic quadratics

## Finding
Let \(A\) and \(C_s\) be independent circular complex Gaussian variables with densities \(\pi^{-1}e^{-|a|^2}\) and \((\pi s^2)^{-1}e^{-|c|^2/s^2}\), respectively, where \(s>0\). The harmonic polynomial
\[
H_s(z)=z^2-\overline{Az}-C_s
\]
has, almost surely, either two or four distinct complex zeros. Its exact four-zero probability \(p(s)\) is
\[
\boxed{p(s)=\frac1\pi\int_0^{2\pi}\frac{1+\cos(3t)}{q(t)}\left[1-\frac{2\sqrt\pi\,s}{\sqrt{q(t)}}e^{4s^2/q(t)}\operatorname{erfc}\!\left(\frac{2s}{\sqrt{q(t)}}\right)\right]dt,\quad q(t)=5-4\cos(3t).}
\]
In particular, \(\mathbb E N_s=2+2p(s)\), where \(N_s\) is the number of distinct zeros. The function \(p\) is strictly completely monotone: \((-1)^k p^{(k)}(s)>0\) for every integer \(k\geq0\) and every \(s>0\). It has the sharp two-term limits
\[
\boxed{p(s)=1-\frac{2(9E(k_0)-K(k_0))}{3\sqrt\pi}\,s+\frac{16}{3}s^2+O(s^3)\quad(s\downarrow0),\qquad k_0=\frac{2\sqrt2}{3},}
\]
\[
\boxed{p(s)=\frac1{4s^2}-\frac9{32s^4}+O(s^{-6})\quad(s\to\infty).}
\]
Here \(K\) and \(E\) are complete elliptic integrals of the first and second kind, using their modulus (not parameter) convention. The coefficient of \(s\) above is \(2.81908397948545026798\ldots\). At unit noise, \(p(1)=0.14635487513720280773\ldots\), giving \(\mathbb EN_1=2.29270975027440561547\ldots\).

## Assumptions and scope
A circular complex normal variable of variance \(v\) has density \((\pi v)^{-1}\exp(-|z|^2/v)\) on \(\mathbb C\). Coefficients \(A\) and \(C_s\) are independent; the analytic quadratic coefficient is deterministic and exactly one. Zeros are counted without multiplicity. The critical-value set and hence singular zeros have probability zero for every \(s>0\). The result is a sparse Gaussian harmonic polynomial model, not the fully random, all-coefficient Kac model.

Define the deltoid domain \(D\) as the bounded component of the complement of the Jordan curve \(w(t)=e^{2it}-2e^{-it}\), \(0\leq t\leq2\pi\). Since the curve is star-shaped about zero, denote its radial boundary by \(R(\varphi)>0\) for polar angle \(\varphi\). Its radii lie between \(1\) and \(3\).

## Proof
**1. Critical values and root-count dichotomy.** If \(A\neq0\), rotation of the input and output changes the equation into \(z^2-u\overline z=c\) with \(u=|A|>0\) and a rotated circular Gaussian target \(c\). The Jacobian of \(z\mapsto z^2-u\overline z\) is \(4|z|^2-u^2\). The critical circle \(|z|=u/2\) is mapped to the deltoid curve \((u^2/4)w(t)\).

Writing \(q(t)=|w(t)|^2=5-4\cos(3t)\), direct differentiation gives
\[
-\frac{d}{dt}\arg w(t)=\frac{2(1+\cos(3t))}{q(t)}\geq0.
\]
Moreover, \(w(t)=e^{-it}(e^{3it}-2)\) winds once clockwise about zero: the factor in parentheses never winds about zero. Consequently each ray meets the critical-value curve exactly once and the curve is a star-shaped Jordan curve, with only three cusp points. On the component containing \(c=0\), the equation has the four simple solutions \(0\) and \(u e^{2\pi i j/3}\) for \(j=0,1,2\). For sufficiently large \(|c|\), no solution lies in \(|z|\leq u/2\); the topological degree at infinity is two and every remaining solution has positive Jacobian, so there are exactly two. On varying \(c\) without crossing the critical-value curve the number of simple zeros is constant, by properness and the inverse function theorem. The two connected complementary regions therefore have respectively four and two zeros. The Gaussian target misses the curve almost surely.

**2. Random deltoid dilation.** The square \(X=|A|^2\) has density \(e^{-x}\) on \(x>0\). Independently, write \(C_s=sVe^{i\Phi}\), where \(\Phi\) is uniform on \([0,2\pi)\), and \(V\) has density \(2v e^{-v^2}\) on \(v>0\). Conditional on \(V,\Phi\), the four-zero condition \(C_s\in(X/4)D\) is exactly
\[
X>\frac{4sV}{R(\Phi)}.
\]
Therefore
\[
p(s)=\mathbb E\exp\left(-\frac{4sV}{R(\Phi)}\right).
\]
This Laplace-transform representation proves \((-1)^k p^{(k)}(s)=\mathbb E[(4V/R(\Phi))^k e^{-4sV/R(\Phi)}]>0\) for all \(k\ge0\), since \(R\ge1\) and the Rayleigh variable has every moment.

**3. Exact one-dimensional integral.** The change from the boundary parameter \(t\) to polar angle \(\varphi\) has positive measure \(d\varphi=2(1+\cos(3t))q(t)^{-1}dt\) after reversing orientation. The elementary Rayleigh Laplace integral is
\[
\int_0^\infty 2v\exp(-v^2-hv)\,dv=1-\frac{\sqrt\pi h}{2}\exp(h^2/4)\operatorname{erfc}(h/2).
\]
Substitute \(h=4s/\sqrt{q(t)}\) and the angle-change formula into the expectation to obtain the boxed formula for \(p(s)\).

**4. Small-noise expansion.** Put \(I_j=(2\pi)^{-1}\int_0^{2\pi}R(\varphi)^{-j}\,d\varphi\). The deltoid parameter gives
\[
I_j=\frac1\pi\int_0^{2\pi}\frac{1+\cos(3t)}{[5-4\cos(3t)]^{1+j/2}}\,dt.
\]
Using \(1+\cos(3t)=(9-q(t))/4\), the standard elliptic integral evaluations at modulus \(k_0=2\sqrt2/3\) give \(I_1=(9E(k_0)-K(k_0))/(3\pi)\); differentiation of the elementary integral \(\int_0^{2\pi}(5-4\cos t)^{-1}dt=2\pi/3\) yields \(I_2=2/3\). As \(\mathbb EV=\sqrt\pi/2\) and \(\mathbb EV^2=1\), Taylor's theorem with an integrable third-order remainder in the Laplace representation yields
\[
p(s)=1-2\sqrt\pi I_1s+8I_2s^2+O(s^3),
\]
which is the claimed expansion.

**5. Large-noise expansion.** Conditional on \(X=x\), changing variables in the circular Gaussian density gives the identity
\[
p(s)=\int_0^\infty e^{-x}\frac{x^2}{16\pi s^2}\int_D\exp\!\left(-\frac{x^2|w|^2}{16s^2}\right)dA(w)\,dx.
\]
The clockwise boundary satisfies \(-\operatorname{Im}(\overline w w'(t))=2(1+\cos(3t))\). The divergence theorem, first for \(1\) and then for \(|w|^2\), gives the exact deltoid area moments
\[
\int_DdA=2\pi,\qquad \int_D|w|^2dA=3\pi.
\]
Indeed these equal \(\frac12\int 2(1+\cos3t)dt\) and \(\frac14\int q(t)2(1+\cos3t)dt\). Expand the Gaussian factor to first order. The exponential moments \(\mathbb EX^2=2\) and \(\mathbb EX^4=24\) yield the coefficients \(1/4\) and \(-9/32\). The next-order error is \(O(s^{-6})\) by boundedness of \(D\), the estimate \(|e^{-y}-1+y|\le y^2/2\) for \(y\ge0\), and \(\mathbb EX^6<\infty\). This completes the proof.

## Verification
Running `python checker.py` in a Python environment with `numpy` and `mpmath` verifies the one-dimensional quadrature, the elliptic coefficient, monotonicity at sample points, and both asymptotic coefficient limits. It also compares physical roots of an independently constructed algebraic quartic against the deltoid inclusion test for 350 seeded random samples. The quartic is obtained by eliminating the conjugate variable and has coefficients \((1,0,-2c,-u^3,c^2-u^2\overline c)\). Potential spurious algebraic roots are removed by evaluating the original harmonic equation. All checks passed during preparation. They corroborate but do not establish the global theorem; the proof above supplies the infinite and all-parameter assertions.

## Relationship to prior work
Lundberg's 2022 study uses probability to establish existence of harmonic polynomials with large valence; its focus is not the complete zero-count distribution of the sparse quadratic model. Lundberg and Thomack's 2023 study gives general Kac-model Kac–Rice integrals and large-degree asymptotics; the present law concerns a fixed monic quadratic with just two independent Gaussian perturbations, and supplies a full two-/four-zero probability law and sharp noise endpoints. Work on deterministic harmonic trinomial zero counts and caustic topology supplies background for the deltoid classification but not this Gaussian mixture and its two-sided asymptotics. An and Evans's 2006 treatment concerns a different rational gravitational lens with deltoid-like caustics and magnification distributions, not this polynomial random-parameter law.

## Limitations
The proof requires circular, independent complex Gaussians and a deterministic monic quadratic analytic part. It does not determine the zero-count law for a fully random harmonic quadratic, non-Gaussian or correlated coefficients, or degrees above two. The caustic is not a physical Chang–Refsdal lens: the latter has a different rational mapping. Numerical approximations to \(p(1)\) are noncertified decimal evaluations of the exact integral. Historical priority remains provisional, particularly for work treating stochastic polynomial caustics under different terminology; independent scientific validation has not been performed.

## References
- Erik Lundberg, *The valence of harmonic polynomials viewed through the probabilistic lens*, arXiv:2201.00788, first posted 2022-01-03; Proceedings of the American Mathematical Society 151 (2023), 2963–2973.
- Erik Lundberg and Andrew Thomack, *On the average number of zeros of random harmonic polynomials with i.i.d. coefficients: precise asymptotics*, arXiv:2308.10333, first posted 2023-08-20.
- Oluma Ararso Alemu and Hunduma Legesse Geleta, *Zeros of a Two-parameter Family of Harmonic Quadrinomials*, arXiv:2106.15824, first posted 2021-06-30.
- Michael Brilleslyper, Jennifer Brooks, Michael Dorff, Russell Howell, and Lisbeth Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proc. Amer. Math. Soc. Ser. B 7 (2020), 82–90, DOI:10.1090/bproc/51.
- Jin H. An and N. Wyn Evans, *The Chang–Refsdal Lens Revisited*, arXiv:astro-ph/0601457, first posted 2006-01-20; Monthly Notices of the Royal Astronomical Society 369 (2006), 317–334.
