# Sharp mean-square A-stability for two-point randomized theta integration

## Finding

Apply the independently randomized theta rule to the scalar linear test equation \(y'=\lambda y\), with complex \(\lambda\), fixed \(h>0\), and \(z=h\lambda\):
\[
Y_{j+1}=Y_j+h\bigl((1-\Theta_j)\lambda Y_j+\Theta_j\lambda Y_{j+1}\bigr),\qquad
R(z,\theta)=\frac{1+(1-\theta)z}{1-\theta z}.
\]

**Theorem (two-point phase boundary and centered-law obstruction).** Suppose \(0<a<1/2<b\le1\), \(\Theta_j\) are independent identically distributed, and \(\Pr(\Theta_j=a)=p\), \(\Pr(\Theta_j=b)=1-p\), where \(0\le p\le1\). The method is mean-square A-stable, meaning \(\mathbb E|Y_N|^2\to0\) for every deterministic \(Y_0\) and every \(z\) with \(\operatorname{Re}z<0\), **if and only if**
\[
0\le p\le p_*(a,b):=\frac{(2b-1)a^2}{(1-2a)b^2+(2b-1)a^2}.
\]
The endpoint \(p=p_*(a,b)\) is included. In particular, for \(a=1/4\) and \(b=3/4\) the exact cutoff is \(p_*=1/10\). The cutoff is strictly below the probability \(p_{\rm mean}=(2b-1)/(2(b-a))\) that makes \(\mathbb E\Theta=1/2\).

More generally, **every nonconstant Borel probability distribution** for \(\Theta\) on \([0,1]\) with \(\mathbb E\Theta=1/2\) fails mean-square A-stability. For every real \(y\ne0\), its one-step mean-square factor at \(z=iy\) exceeds one. Letting
\[
\kappa=2\mathbb E\Theta^3-\mathbb E\Theta^2>0,
\]
its weak-damping stability boundary near the origin, expressed as \(z=-x+iy\), is
\[
x=\frac{\kappa}{2}y^4+O(y^6)\quad(y\to0).
\]
Locally the stable side is \(x\) greater than this boundary. For the symmetric two-point law \(a=1/2-d\), \(b=1/2+d\), \(p=1/2\), \(0<d<1/2\), the complete mean-square stability condition at \(x>0\), \(q=x^2+y^2\), is exactly
\[
4x(1+x)+(1-4d^2)xq>4d^2q^2,
\]
and its boundary coefficient is \(\kappa/2=d^2\).

## Assumptions and scope

The scalar test equation has no forcing and no stochastic differential-equation noise. The only randomness is the independently resampled implicitness parameter \(\Theta_j\), independent of the deterministic starting value. The method is well-defined for \(\operatorname{Re}z\le0\), since \(\theta\in[0,1]\) makes \(1-\theta z\ne0\) on that domain. Mean-square A-stability is pointwise in \(z\): it requires strict contraction for every fixed \(\operatorname{Re}z<0\), but not a uniform rate over the entire half-plane. The two-point characterization assumes strictly positive \(a\); the centered-law statement permits mass at zero.

## Proof

**1. Reduction to one-step amplification.** Iteration gives \(Y_N=Y_0\prod_{j=0}^{N-1}R(z,\Theta_j)\); independence implies
\[
\mathbb E|Y_N|^2=|Y_0|^2 F(z)^N,\qquad F(z)=\mathbb E|R(z,\Theta)|^2.
\]
For \(z=-x+iy\), \(x\ge0\), \(q=x^2+y^2\), direct expansion gives the exact identity
\[
|R(z,\theta)|^2-1=
\frac{-2x+(1-2\theta)q}{1+2\theta x+\theta^2q}.
\tag{1}
\]
Thus mean-square A-stability is equivalent to \(F(z)<1\) at every \(x>0\).

**2. Boundary test for the two-point law.** On the imaginary axis \(z=iy\), equation (1) gives
\[
F(iy)-1=
\frac{y^2(A+B y^2)}{(1+a^2y^2)(1+b^2y^2)},
\]
where
\[
A=p(1-2a)+(1-p)(1-2b),\qquad
B=p(1-2a)b^2+(1-p)(1-2b)a^2.
\]
The inequality \(B\le0\) is equivalent to \(p\le p_*(a,b)\). Because \(0<a<b\), direct comparison yields \(p_*<(2b-1)/(2(b-a))=:p_{\rm mean}\). Consequently, \(p\le p_*\) implies \(A<0\) and \(B\le0\), hence \(F(iy)\le1\) for all real \(y\), with strict inequality for \(y\ne0\).

**3. Extension from the boundary to the half-plane.** For fixed \(0<a,b\le1\), the two analytic functions \(R(z,a)\), \(R(z,b)\) have no poles on the closed left half-plane, and
\[
F(z)=p|R(z,a)|^2+(1-p)|R(z,b)|^2
\]
is subharmonic there. As \(|z|\to\infty\) with \(\operatorname{Re}z\le0\), it converges uniformly in direction to
\[
L=p\left(\frac{1-a}{a}\right)^2+(1-p)\left(\frac{1-b}{b}\right)^2,
\]
and elementary algebra shows \(L-1=B/(a^2b^2)\). For \(p\le p_*\), this limit is at most one. Apply the subharmonic maximum principle on a left half-disk of radius \(R\); its imaginary-axis boundary values are at most one and its semicircle boundary values at most \(1+o(1)\) as \(R\to\infty\). Therefore \(F(z)\le1\) throughout the open left half-plane. Equality at an interior point would force \(F\) to be constant by the strong maximum principle, contradicting \(F(-x)=1-2x+O(x^2)<1\) for small \(x>0\). Thus \(F(z)<1\) everywhere inside, including \(p=p_*\).

For \(p>p_*\), \(B>0\); the boundary formula gives \(F(iy)>1\) for all sufficiently large \(|y|\), and continuity yields \(F(-x+iy)>1\) for some arbitrarily small \(x>0\). This disproves mean-square A-stability and completes the necessary-and-sufficient classification.

**4. Universal centered-law obstruction.** Let \(\Theta\) be any nonconstant random variable on \([0,1]\) with mean \(1/2\), and let \(w_y(t)=(1+t^2y^2)^{-1}\). For \(y\ne0\), \(w_y\) is strictly decreasing on \([0,1]\). By equation (1),
\[
F(iy)-1=y^2\mathbb E[(1-2\Theta)w_y(\Theta)]
=-2y^2\operatorname{Cov}(\Theta,w_y(\Theta))>0.
\]
The strict sign follows from the independent-copy identity
\[
2\operatorname{Cov}(\Theta,w_y(\Theta))
=\mathbb E[(\Theta-\Theta')(w_y(\Theta)-w_y(\Theta'))]<0,
\]
since the law is nonconstant. Continuity again gives unstable points with negative real part.

**5. Universal fourth-order boundary.** Taylor expansion, uniform for \(\Theta\in[0,1]\), yields
\[
F(iy)-1=\kappa y^4+O(y^6),\qquad
\kappa=2\mathbb E\Theta^3-\mathbb E\Theta^2
=2\operatorname{Cov}(\Theta,\Theta^2)>0.
\]
The map \((x,y)\mapsto F(-x+iy)-1\) is real analytic near the origin with \(\partial_xF(-x+iy)|_{(0,0)}=-2\). The implicit-function theorem therefore gives a unique local even analytic stability-boundary graph \(x=x(y)\). Substitution of \(x(y)=O(y^4)\) yields \(x(y)=\kappa y^4/2+O(y^6)\), with \(F<1\) on its larger-\(x\) side. For the symmetric two-atom law, multiplying the two denominators in (1) gives the stated polynomial inequality exactly and \(\kappa=2d^2\).

## Verification

Run `python3 verify.py` (Python standard library only) in the directory containing the bundled verifier. It checks equation (1), the rational two-atom imaginary-axis identity, the sharp threshold and infinity equality, the symmetric-law polynomial, and representative centered laws using exact rational arithmetic. The recorded run passed 396 exact-rational assertions. These finite checks do not prove the full statements: the argument in Proof sections 3–5 establishes the half-plane and arbitrary-law conclusions.

## Relationship to prior work

Bochacik, Przybyłowicz and Stępień study the **uniform** random-parameter implicit RK2 method \(R(z,U)=1+z/(1-Uz)\), with \(U\) uniform on \([0,1]\); their 2024 preprint establishes that its mean-square stability region is not A-stable. A previously established exact uniform-law boundary also has \(x\sim y^4/12\), recovered here by inserting \(\mathbb E U^2=1/3\) and \(\mathbb E U^3=1/4\). Neither uniform-only conclusion yields the sharp variable-probability two-point A-stability criterion or the obstruction for **every** centered nonconstant law. The older 2020 randomized explicit RK study analyzes a different amplification polynomial \(1+z+Uz^2\). The 2021 operator-equation work randomizes additive step perturbations, not the theta coefficient. A 2026 randomized SDIRK construction has realizations that are themselves algebraically stable and therefore does not imply this two-point rule's phase boundary.

## Limitations

The theorem is for independent random coefficients and linear scalar test equations. It gives no general nonlinear convergence theorem, no statement about almost-sure stability at the mean-square instability threshold, and no optimality over all possible integrators. The weak-damping fourth-order coefficient concerns the local stability boundary, not an all-frequency asymptotic. Publication precedence remains subject to specialist work on random-coefficient theta methods not located in the examined literature. No independent scientific audit has been performed.

## References

1. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, first public preprint 2024-04-29, https://arxiv.org/abs/2404.19059 (later journal version with Ł. Stępień).
2. T. Bochacik, M. Goćwin, P. M. Morkisz, P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, first public preprint 2020-06-22, https://arxiv.org/abs/2006.12131.
3. H. C. Lie, M. Stahn, T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, first public preprint 2021-03-30, https://arxiv.org/abs/2103.16506.
4. M. Eisenmann, M. Jans, R. Kruse, H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge–Kutta Method*, first public preprint 2026-07-21, https://arxiv.org/abs/2607.18928.
5. D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM J. Numer. Anal. 38 (2000), 753–769, DOI:10.1137/S003614299834736X. This concerns numerical SDEs with multiplicative noise and a fixed method parameter, a different model.
