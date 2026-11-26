# Arithmetic lower floors for the spherical Fourier energy of disjoint balls

## Finding

Let \(d\ge2\) and \(\Omega=\bigcup_{j=1}^m B(c_j,r_j)\subset\mathbb R^d\) be a union of \(m\ge2\) open balls with pairwise disjoint closures and positive radii. For probability surface measure \(d\sigma\) and the Fourier transform with phase \(e^{-2\pi i x\cdot\xi}\), put
\[
E_\Omega(R)=\int_{\mathbb S^{d-1}}|\widehat{\mathbf1_\Omega}(R\omega)|^2\,d\sigma(\omega),\qquad \phi_d=\frac{\pi(d+1)}4,\qquad \alpha_d=\frac{d+3}{8}.
\]
For fixed geometry and all real \(R\to+\infty\),
\[
R^{d+1}E_\Omega(R)=\frac1{\pi^2}\sum_j r_j^{d-1}\cos^2(2\pi r_jR-\phi_d)+O_\Omega(R^{-\min\{1,(d-1)/2\}}).\tag{1}
\]
Define the integer relation lattice \(\Lambda_r=\{h\in\mathbb Z^m:h\cdot r=0\}\) and the subtorus
\[
T_r=\{\theta\in(\mathbb R/\mathbb Z)^m:h\cdot\theta\in\mathbb Z\ \text{for all }h\in\Lambda_r\}.
\]
Then
\[
L:=\liminf_{R\to\infty}R^{d+1}E_\Omega(R)=\frac1{\pi^2}\min_{\theta\in T_r}\sum_j r_j^{d-1}\cos^2(2\pi\theta_j-\phi_d).\tag{2}
\]
There exists \(c>0\) such that \(E_\Omega(R)\ge cR^{-d-1}\) for all sufficiently large \(R\) if and only if \(L>0\). In terms of \(\Lambda_r\) this is equivalent to either of the following tests:

* For each \(\varepsilon\in\{0,1\}^m\), some \(h\in\Lambda_r\) has \(\alpha_d\sum_j h_j+\tfrac12\sum_j h_j\varepsilon_j\notin\mathbb Z\).
* Some \(h\in\Lambda_r\) has \(4\nmid (d+3)\sum_j h_j\).

In particular, the test depends only on the radii. For two radii \(q\rho,p\rho\) with \(p,q\) positive coprime integers, it becomes \(4\nmid(p-q)(d+3)\). An irrational pair has \(L=0\). Pairwise irrationality does not suffice when there are three or more balls: for \(r=(1,\sqrt2,1+\sqrt2)\) each pair has zero lower envelope, while the triple has a strictly positive floor in every \(d\not\equiv1\pmod4\), by the relation \((1,1,-1)\).

In the plane with radii \(\rho,2\rho\),
\[
\boxed{L=\frac{\rho}{\pi^2}\left(\frac32-\sqrt{\frac{2367+129\sqrt{129}}{2048}}\right)>0.}\tag{3}
\]
This equals approximately \(0.13209245\,\rho/\pi^2\). It is the **supremum** of eventual lower coefficients: each \(c<L\) is an eventual lower coefficient, and none with \(c>L\) is. The endpoint \(c=L\) need not be an eventual lower bound, even in this planar example.

## Assumptions and scope

The closures of the balls are disjoint, so \(|c_i-c_j|>r_i+r_j\). The bounded open union need not be connected. For unnormalized surface area every coefficient is multiplied by \(|\mathbb S^{d-1}|\). The statements concern all large positive **real** \(R\), not integer samples; all geometry is fixed before taking the limit. A uniform cutoff over varying geometry is not asserted.

## Proof

**Bessel reduction.** The radial Fourier amplitude of a centered ball of radius \(r\) is
\[
A_r(R)=r^{d/2}R^{-d/2}J_{d/2}(2\pi rR),\qquad R>0.
\]
Disjointness makes the indicator additive, and translation multiplies the amplitude by \(e^{-2\pi iR c_j\cdot\omega}\). Hence the spherical energy is exactly
\[
\sum_j A_{r_j}(R)^2+2\sum_{i<j}A_{r_i}(R)A_{r_j}(R)\,\mathcal J_d(2\pi R|c_i-c_j|),
\quad
\mathcal J_d(s)=\int_{\mathbb S^{d-1}}e^{is\omega_1}d\sigma(\omega)=\Gamma(d/2)(2/s)^{d/2-1}J_{d/2-1}(s).
\]
The fixed-order asymptotic \(J_\nu(s)=\sqrt{2/(\pi s)}[\cos(s-\pi\nu/2-\pi/4)+O_\nu(s^{-1})]\) yields
\[
A_r(R)=\frac{r^{(d-1)/2}}{\pi R^{(d+1)/2}}\cos(2\pi rR-\phi_d)+O_{r,d}(R^{-(d+3)/2}),\qquad \mathcal J_d(s)=O_d(s^{-(d-1)/2}).
\]
Thus the normalized self-energy errors are \(O_\Omega(R^{-1})\), and all finitely many normalized cross terms together are \(O_\Omega(R^{-(d-1)/2})\), proving (1).

**Relation torus and zeros.** The closure of \(Rr\pmod{\mathbb Z^m}\) is the subtorus \(T_r\), since its annihilator consists exactly of the integer characters with \(h\cdot r=0\). By compact-torus recurrence every point of \(T_r\) is approached along positive times tending to infinity. Applying (1) to a minimizing sequence, and bounding the leading sum below by its minimum, gives (2). The sum has positive minimum precisely when no point of \(T_r\) lies in the finite set \(\alpha_d\mathbf1+\{0,1/2\}^m\). Membership in that torus is exactly the condition that every \(h\in\Lambda_r\) pairs integrally with the point in question. Negating existence gives the bit-vector test.

Equivalently, multiplication by two maps \(T_r\) onto itself: its image is compact and contains the dense orbit \(2Rr\). The points with all cosine squares zero are exactly the torus preimages of \(2\alpha_d\mathbf1\) under doubling. A simultaneous zero therefore exists precisely if \(2\alpha_d\mathbf1\in T_r\), that is, if \(4\mid (d+3)\sum_j h_j\) for **every** relation \(h\). Taking the negation gives the second test. For two commensurate radii the generator of \(\Lambda_r\) is \((p,-q)\); for an irrational pair it is the zero lattice. In the three-ball example all three ratios of distinct radii are irrational and \((1,1,-1)\) is a relation with coordinate sum one. Equation (2) also shows that any \(c<L\) is eventually a lower coefficient and every \(c>L\) fails on a sequence tending to infinity; this in particular proves the equivalence between \(L>0\) and existence of some eventual positive coefficient.

**Planar constant.** For \(d=2\) and radii \(\rho,2\rho\), set \(t=2\pi\rho R\). The leading sum after multiplication by \(\pi^2/\rho\) is
\[
F(t)=\cos^2(t-3\pi/4)+2\cos^2(2t-3\pi/4)=\tfrac32-\tfrac12\sin(2t)-\sin(4t).
\]
For \(g(u)=\tfrac12\sin u+\sin(2u)\) the critical cosines solve \(8\cos^2u+\cos u-4=0\); they are \(c_\pm=(-1\pm\sqrt{129})/16\). At each the squared value of \(g\) is \((1-c_\pm^2)(1/2+2c_\pm)^2=(2367\pm129\sqrt{129})/2048\). The larger square corresponds to \(c_+\), and the positive maximum is attained there with \(\sin u>0\). The minimum of \(F\) is therefore the bracket in (3). Strict positivity also follows from the radius congruence.

**Endpoint nonattainment for a separated configuration.** Take center separation \(4\rho\). Write \(t_*=\tfrac12\arccos c_+\) and \(R_n=(t_*+2\pi n)/(2\pi\rho)\). Since \(1/2<c_+<1/\sqrt2\), one has \(\pi/8<t_*<\pi/6\). At these frequencies the normalized self-energy sum is \(L+O(R_n^{-1})\). The cross term has leading order \(R_n^{-1/2}\) because the planar angular factor is \(J_0\). Its leading sign is that of
\[
\cos(t_*-3\pi/4)\,\cos(2t_*-3\pi/4)\,\cos(4t_*-\pi/4),
\]
which is strictly negative: on the indicated interval the first factor is negative and the other two are positive. Thus along this sequence \(R_n^3 E_\Omega(R_n)=L-C R_n^{-1/2}+O(R_n^{-1})\) for some \(C>0\). The distance \(4\rho\) obeys the strict separation assumption. Consequently \(c=L\) is not an eventual lower coefficient for this geometry.

## Verification

The proof derives the exact Bessel decomposition, relation-torus test, planar stationary values and endpoint example analytically. The unchanged companion `verify.py` checks the two-ball congruence against the two-bit condition over a finite range, compares (3) to periodic grid minimization, and checks examples of the three-dimensional asymptotic with exact closed forms for half-integer Bessel functions. The finite diagnostics do not certify the general theorem or the endpoint behavior.

## Relationship to prior work

Iosevich, Merlo and Mourgoglou establish sharp upper spherical decay for regularity classes, note that a single ball can have individual zero radii, and discuss lower bounds for a limsup. Their statements do not characterize a positive bound at every sufficiently large radius for fixed disconnected ball unions. Brandolini, Hofmann and Iosevich establish upper decay; Iosevich and Rudnev study lower bounds for classes of measures under energy and Fourier-positivity hypotheses, not the arithmetic envelope of this fixed indicator. The closely related catalogue finding *Arithmetic lower envelopes of the spherical Fourier energy of two separated balls* explicitly gives the same asymptotic and congruence for two balls, as well as an upper-envelope criterion, a Cesàro distribution, and a three-dimensional radius-1:2 example. Its two-ball conclusions do not supply the many-ball classification, including relations invisible in all pairwise tests, nor the explicit planar evaluation. The shared catalogue date establishes no priority order. The novelty assessed here concerns the general arithmetic floor and the explicit planar evaluation, not the standard Bessel or torus facts or the shared two-ball criterion.

## Limitations

This does not address overlapping balls, connected perturbations, arbitrary smooth components, nonuniform weights, or cutoffs uniform in radii and center separations. The torus minimum is an exact characterization, not a closed algebraic formula for general radii. Priority comparisons are limited to inspected sources; earlier equivalent formulations are not ruled out.

## References

1. A. Iosevich, A. Merlo, M. Mourgoglou, *Sharp decay of the spherical averages of the Fourier transform of open sets*, arXiv:2611.04426v1, https://arxiv.org/abs/2611.04426.
2. L. Brandolini, S. Hofmann, A. Iosevich, *Sharp rate of average decay of the Fourier transform of a bounded set*, Geom. Funct. Anal. 13 (2003), 671–680, arXiv:math/0303188.
3. A. Iosevich, M. Rudnev, *On lower bounds for spherical averages of Fourier transforms*, manuscript dated 2005-06-21, https://people.maths.bris.ac.uk/~maxmr/lowerbound3.pdf.
4. NIST Digital Library of Mathematical Functions, §10.17, https://dlmf.nist.gov/10.17/.
5. *Arithmetic lower envelopes of the spherical Fourier energy of two separated balls*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-arithmetic-lower-envelopes-of-the-spherical-fourier-energy-of-tw--eb0dce2c6ca4.
