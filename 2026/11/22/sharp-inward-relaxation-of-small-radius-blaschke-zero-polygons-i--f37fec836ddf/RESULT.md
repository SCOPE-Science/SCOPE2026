# Sharp inward relaxation of small-radius Blaschke zero polygons in every degree

## Finding
Fix an integer \(d\ge3\). For a degree-\(d\) finite Blaschke product \(B\) with zeros \(a_0,\ldots,a_{d-1}\) counted with multiplicity, define its boundary-speed variance by
\[
\mathcal V(B)=\frac1{2\pi}\int_0^{2\pi}\bigl(|B'(e^{it})|-d\bigr)^2\,dt.
\]
For \(0<r<1\), restrict to the natural outermost-zero constraint \(\max_j|a_j|=r\), and write \(\mathcal V_d^*(r)\) for the attained minimum.

**Theorem.** There exists \(\varepsilon_d>0\) such that, for every \(0<r<\varepsilon_d\), the minimizing zero multiset is unique up to common rotation. Exactly one zero has modulus \(r\); after rotating it to \(a_0=r\), all remaining zeros are simple, lie strictly inside the radius-\(r\) disk, and admit the labelled expansions
\[
 a_j=r\zeta_j\left[1+\frac{d}{(d-1)^2}(\zeta_j-1)r^2+O_d(r^4)\right],\qquad
 \zeta_j=e^{2\pi i j/d},\quad 1\le j\le d-1.
\]
The sharp minimum has the universal two-term expansion
\[
\boxed{\mathcal V_d^*(r)=2d^2r^{2d}-\frac{2d^4}{(d-1)^2}r^{2d+2}+O_d(r^{2d+4}).}
\]
The minimizer is an analytic perturbation (in \(r^2\)) of the regular root-of-unity polygon. The first shape coefficient is forced and nonzero: at fixed outermost radius, the regular polygon is **not** optimal for all sufficiently small positive radii. More precisely, the minimizing normalized zero polynomial satisfies
\[
\prod_{j=0}^{d-1}(z-a_j/r)
=z^d-1-\frac{d^2}{(d-1)^2}r^2(z-1)+O_d(r^4)
\]
coefficientwise. In particular, after the distinguished zero is fixed, the minimizing multiset is invariant under complex conjugation.

## Assumptions and scope
The degree \(d\) is a fixed integer at least three; the radius tends to zero with \(d\) fixed. No uniformity in growing \(d\) and no explicit value of \(\varepsilon_d\) is claimed. Blaschke products differing only by an unimodular scalar have the same variance and zero multiset; this scalar freedom is implicit in the uniqueness statement. Repeated zeros are permitted in the feasible class but do not occur in the small-radius minimizer. The variance is that of the **boundary angular speed** \(|B'|\), not the Hardy mean of \(|B|\) on interior circles, nor the pointwise maximum or minimum of \(|B'|\).

Write \(u_j=a_j/r\), select a maximal-modulus zero and rotate so that \(u_0=1\), and put \(p_m(u)=\sum_{j=0}^{d-1}u_j^m\) for \(m\ge1\). For a polynomial \(P_u(z)=\prod_j(z-u_j)\), all power sums are determined algebraically by its coefficients through Newton's identities.

## Proof
### 1. Positive Fourier energy and existence
On the unit circle, the logarithmic derivative identity for Blaschke products gives
\[
|B'(e^{it})|=\sum_{j=0}^{d-1}\frac{1-|a_j|^2}{|e^{it}-a_j|^2}
=d+2\operatorname{Re}\sum_{m\ge1}\overline{\sum_j a_j^m}\,e^{imt}.
\]
Parseval therefore yields the exact, absolutely convergent identity
\[
\frac12\mathcal V(B)=E_r(u):=\sum_{m\ge1}r^{2m}|p_m(u)|^2.
\]
The normalized feasible set \(u_0=1\), \(|u_j|\le1\) for \(j\ge1\), is compact. Since \(r<1\), the series converges uniformly on this set, so a minimum exists. For the regular polygon \(u_j=\zeta_j\), the only nonzero power sums occur at multiples of \(d\), whence
\[
E_r(\zeta_0,\ldots,\zeta_{d-1})=\frac{d^2r^{2d}}{1-r^{2d}}.
\]
Every normalized minimizer consequently satisfies, for \(1\le m\le d-1\),
\[
|p_m(u)|\le\frac{d\,r^{d-m}}{\sqrt{1-r^{2d}}}.
\]
As \(r\downarrow0\), all these power sums tend to zero. Newton's identities make the first \(d-1\) elementary symmetric functions tend to zero. Because \(u_0=1\), the monic polynomial \(P_u\) must therefore tend coefficientwise to \(z^d-1\): indeed, its limiting polynomial has form \(z^d+c\), and vanishing at one forces \(c=-1\). Thus *every* family of global minimizers, after rotation and relabelling, converges to this same regular polygon.

### 2. Coordinates, convexity, and uniqueness
Near the regular polygon use the complex coordinates \(q=(p_1,\ldots,p_{d-1})\). Newton's identities give an analytic, locally invertible triangular map from \(q\) to the coefficients of the monic zero polynomial with the distinguished root \(1\). All other roots are simple and depend holomorphically on \(q\) near \(0\). Thus for all \(m\ge d\) the power sums \(p_m=p_m(q)\) are holomorphic, \(p_d(0)=d\), and \(p_m(0)=0\) unless \(d\) divides \(m\).

On a fixed sufficiently small convex ball \(\|q\|\le\delta\), all these holomorphic functions and their first two derivatives grow at most geometrically in \(m\). This follows either from the simple-root representation with roots in a fixed bounded disk or from Cauchy estimates on a slightly larger coefficient neighborhood. Therefore, for all sufficiently small \(r\), the real Hessian of the tail
\[
T_r(q)=\sum_{m\ge d}r^{2m}|p_m(q)|^2
\]
has operator norm at most \(C_d r^{2d}\), uniformly on the ball. The core \(\sum_{m=1}^{d-1}r^{2m}|q_m|^2\) has real Hessian at least \(2r^{2d-2}I\). Hence
\[
D^2E_r(q)\succeq(2r^{2d-2}-C_dr^{2d})I\succ0
\]
for sufficiently small \(r\). Thus the energy is strictly convex on this ball.

At \(q=0\), its value is \(d^2r^{2d}/(1-r^{2d})\); on the boundary \(\|q\|=\delta\), its nonnegative core is at least \(\delta^2r^{2d-2}\). Hence it has a unique **interior** stationary minimum \(q_*(r)\) in the ball. The preceding compactness argument places every global minimizer in this ball for all sufficiently small \(r\); a feasible global minimizer, if interior to the coordinate ball, must be compared with this unconstrained minimum. Feasibility of \(q_*(r)\) is established in Step 4 below. At that point its energy is no larger than any feasible energy, proving global uniqueness up to rotation and relabelling. Complex conjugation preserves the objective and the fixed root \(1\), so uniqueness implies that \(q_*(r)\) is real.

### 3. First stationary jet and sharp energy coefficient
The degree-\(d\) power sum has derivatives at the regular configuration
\[
\frac{\partial p_d}{\partial q_m}(0)=-\frac{d}{m},\qquad 1\le m\le d-1.
\]
For completeness, write the nearby zero polynomial in the form
\[
P_u(z)=z^d-1+\sum_{j=1}^{d-1}b_j(z^j-1).
\]
The simple-root formula, or differentiated Newton identities, gives \(\partial p_m/\partial b_{d-m}(0)=-m\) for \(m<d\), with all other first derivatives of these power sums zero, while \(\partial p_d/\partial b_j(0)=d\) for all \(j\). The displayed identity follows by the chain rule.

Stationarity in the Wirtinger variables \(\overline q_m\), together with the uniform tail-derivative bound, yields
\[
q_m=O_d(r^{2(d-m)}),\qquad 1\le m\le d-1.
\]
Refining the equation for \(m=d-1\), using \(p_d(q_*)=d+O_d(r^2)\) and the preceding derivative, gives
\[
q_{d-1}=\frac{d^2}{d-1}r^2+O_d(r^4).
\]
All earlier coordinates satisfy \(q_m=O_d(r^4)\) for \(m\le d-2\). The inverse Newton map consequently gives
\[
b_1=-\frac{d^2}{(d-1)^2}r^2+O_d(r^4),\qquad
b_j=O_d(r^4)\quad (j\ge2).
\]
The normalized zero polynomial expansion follows. Furthermore,
\[
p_d(q_*)=d-\frac{d^3}{(d-1)^2}r^2+O_d(r^4).
\]
The contribution of \(m=d-1\) to \(E_r\) is \(d^4r^{2d+2}/(d-1)^2+O_d(r^{2d+4})\), that of \(m=d\) is \(d^2r^{2d}-2d^4r^{2d+2}/(d-1)^2+O_d(r^{2d+4})\), and all remaining terms together contribute \(O_d(r^{2d+4})\). This last bound follows from the coordinate estimates for \(m<d-1\), the fact that \(p_m(0)=0\) for \(d<m<2d\), and geometric convergence of the higher tail. Summing and multiplying by the Parseval factor \(2\) establishes the stated minimum expansion.

### 4. Strict radial feasibility and geometry
The roots of \(z^d-1\) are simple. Inserting the coefficient expansion into the implicit root equation gives, uniformly in the finitely many labels,
\[
u_j=\zeta_j\left[1+\frac{d}{(d-1)^2}(\zeta_j-1)r^2+O_d(r^4)\right].
\]
The distinguished root remains exactly \(u_0=1\) by construction. For every \(j\ge1\),
\[
|u_j|=1-\frac{d}{(d-1)^2}\bigl(1-\cos(2\pi j/d)\bigr)r^2+O_d(r^4)<1
\]
when \(r>0\) is sufficiently small. Hence the unconstrained stationary minimum is feasible with exactly one outermost zero, and Steps 1–3 prove the global statement. The stationarity system becomes a nonsingular real-analytic system after rescaling each coordinate by \(r^{2(d-m)}\); the implicit-function theorem yields real analyticity of the minimizing coefficients in \(r^2\) near zero. This justifies the stated Taylor remainders. Finally, the strict negative second energy coefficient implies that the regular equal-radius polygon is strictly suboptimal for all sufficiently small \(r>0\).

## Verification
The accompanying `CHECK.py` is standalone Python-standard-library diagnostic code. It checks exact rational Newton-identity Taylor coefficients for degrees \(3\) through \(13\), reconstructs perturbed zero polygons by Newton iteration for degrees \(3\) through \(9\), and independently evaluates the finite Parseval sums for three small positive radii. The checked upper-bound expansion agrees with the proved coefficient. Finite checks are not used as a proof of global uniqueness, the infinite Fourier identity, or uniform small-radius existence; those rely on the preceding analytic argument.

Run `python CHECK.py` in the folder containing the extracted file. This requires Python 3.9 or newer and no third-party packages.

## Relationship to prior work
Kovalev and Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760v1 (19 July 2020), study attainable pairs of the **pointwise** boundary derivative extrema and describe their hypergeometric equality cases. Their Poisson-kernel representation underlies Step 1, but the inspected theorems concern \(\min |B'|\) and \(\max |B'|\), rather than the squared mean variance at fixed outermost zero radius.

Gluchoff and Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative* (2013), analyze interior-circle Hardy means, their relation to derivative sampling means, and selected equal-radius zero patterns. The zero-location section's objective \(1-M_2(r,B)^2\) is not \(\mathcal V(B)\). Classical equal-circle energy and polarization comparisons also do not imply the present theorem: the optimizing zeros here have **unequal radii**, with precisely one at the outermost permitted radius. A previously available degree-two fixed-radius calculation does not establish the all-degree \(d\ge3\) uniqueness and expansion here.

## Limitations
The theorem is a sufficiently-small-radius statement at each fixed degree. It does not determine an effective threshold, the optimizer for arbitrary radii, or uniform behavior as the degree grows. The upper-error term has a degree-dependent constant. The source comparisons support originality only to the best currently checked knowledge; older equivalent Poisson-energy and point-configuration formulations remain a historical-priority risk. No independent mathematical audit is asserted.

## References
1. L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760v1, posted 19 July 2020; https://arxiv.org/abs/2007.09760 ; open paper https://math.illinois.edu/system/files/2020-09/X.%20Yang-3.pdf .
2. A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative*, in *Blaschke Products and Their Applications*, 2013, DOI:10.1007/978-1-4614-5341-3_9 .
