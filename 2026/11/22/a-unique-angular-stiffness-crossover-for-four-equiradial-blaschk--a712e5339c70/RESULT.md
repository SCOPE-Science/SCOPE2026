# A unique angular-stiffness crossover for four equiradial Blaschke zeros

## Finding

A degree-four finite Blaschke product with zeros on a prescribed circle has a natural boundary-speed variance. At its regular-square zero configuration the full angular Hessian has precisely two transverse spectral bands. Their order reverses **exactly once** as the zero radius increases: the alternating angular displacement is the softest mode for small radii, whereas the two-dimensional first-Fourier displacement is softest for large radii. At one explicit algebraic radius all three transverse Hessian directions have equal curvature.

Precisely, put \(u=r^2\), where \(0<r<1\), and define
\[
\begin{aligned}
L_1(u)&=\frac{4u(1-u)(1+4u+19u^2+24u^3+19u^4+4u^5+u^6)}{(1+u)^3(1+u^2)^3},\\
L_2(u)&=\frac{32u^2(1-u)(1+u)}{(1+u^2)^3}.
\end{aligned}
\]
These are exactly the coefficients of the squared Euclidean projections of angular perturbations onto the first-Fourier and alternating subspaces, respectively. Both are strictly positive for every \(0<u<1\). The unique crossing \(u_*\in(0,1)\) is the unique positive root below one of
\[
p(u)=u^6-4u^5-13u^4-24u^3-13u^2-4u+1,
\]
with \(u_*=0.152011526727727\ldots\) and zero radius \(r_*=\sqrt{u_*}=0.389886556228510\ldots\). For \(0<u<u_*\), \(L_2(u)<L_1(u)\); for \(u_*<u<1\), \(L_1(u)<L_2(u)\). At \(u=u_*\) the Hessian is isotropic after quotienting by common rotation.

The sharp local variance-stability coefficient is \(\min\{L_1(u),L_2(u)\}\), with asymptotic behavior \(32u^2+O(u^3)\) at \(u\downarrow0\) and \(\frac92(1-u)+O((1-u)^2)\) at \(u\uparrow1\).

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Fix \(r\in(0,1)\). For an ordered four-tuple of real angles \(\theta=(\theta_0,\theta_1,\theta_2,\theta_3)\), let
\[
B_{r,\theta}(z)=\prod_{j=0}^{3}\frac{z-r e^{i\theta_j}}{1-r e^{-i\theta_j}z},
\qquad
V_r(\theta)=\frac1{2\pi}\int_0^{2\pi}\bigl(|B_{r,\theta}'(e^{it})|-4\bigr)^2\,dt.
\]
The angles may coincide; the analytic formulas remain valid. Let \(\theta^*=(0,\pi/2,\pi,3\pi/2)\) be the square. For a real perturbation \(h\in\mathbb R^4\), let \(\Pi_1\) denote Euclidean orthogonal projection onto
\[
E_1=\operatorname{span}\{(1,0,-1,0),(0,1,0,-1)\},
\]
and let \(\Pi_2\) project onto \(E_2=\operatorname{span}\{(1,-1,1,-1)\}\). The remaining one-dimensional subspace consists of common rotations.

The precise local statement, with the Euclidean norm on \(\mathbb R^4\), is
\[
V_r(\theta^*+h)=\frac{32u^4}{1-u^4}
+L_1(u)\|\Pi_1h\|^2+L_2(u)\|\Pi_2h\|^2+O_r(\|h\|^3)
\quad (h\to0).
\]
The cubic remainder is for a fixed radius and locally labeled nodes. No assertion is made about unrestricted radial motions, global minimization among all angle tuples, or products of other degrees.

## Proof

**1. Boundary speed and Parseval.** On the unit circle, the finite-Blaschke logarithmic derivative identity yields
\[
|B_{r,\theta}'(e^{it})|=\sum_{j=0}^3 P_r(t-\theta_j),\qquad
P_r(x)=\frac{1-r^2}{1-2r\cos x+r^2}
=\sum_{k\in\mathbb Z}r^{|k|}e^{ikx}.
\]
Set \(S_k(\theta)=\sum_{j=0}^3 e^{ik\theta_j}\). By absolute convergence and Parseval,
\[
V_r(\theta)=2\sum_{k=1}^{\infty}u^k|S_k(\theta)|^2.
\]
At the square, \(S_k(\theta^*)=4\) if \(4\mid k\) and zero otherwise. Consequently \(V_r(\theta^*)=32u^4/(1-u^4)\).

**2. Exact transverse quadratic form.** Define the unitary discrete Fourier coordinates
\[
d_\ell=\frac12\sum_{j=0}^3h_j e^{i\pi\ell j/2},\qquad \ell=0,1,2,3.
\]
Since \(h\) is real, \(d_3=\overline{d_1}\) and \(d_2\) is real. Moreover
\[
\|\Pi_1h\|^2=2|d_1|^2,\qquad \|\Pi_2h\|^2=|d_2|^2.
\]
For \(4\nmid k\), expansion of \(S_k\) around \(\theta^*\) gives \(|S_k|^2=4k^2|d_{k\bmod4}|^2+O_k(\|h\|^3)\). For \(4\mid k\), its quadratic variation is \(-4k^2(2|d_1|^2+|d_2|^2)\). The series of third derivatives converges locally because \(\sum_{k\ge1}k^3u^k<\infty\); hence termwise expansion has the asserted \(O_r(\|h\|^3)\) remainder.

For \(0\le\ell\le3\), put
\[
A_\ell(u)=\sum_{q=0}^{\infty}(4q+\ell)^2u^{4q+\ell},
\]
where the zero term in \(A_0\) is harmless. The quadratic coefficients of the two real Fourier subspaces are
\[
L_1=4(A_1+A_3-2A_0),\qquad L_2=8(A_2-A_0).
\]
Let \(v=u^4\). Differentiating the geometric series twice gives the exact identity
\[
A_\ell=u^\ell\left(
\frac{\ell^2}{1-v}+\frac{8\ell v}{(1-v)^2}+\frac{16v(1+v)}{(1-v)^3}
\right).
\]
Substitution and rational simplification yield the displayed formulas for \(L_1,L_2\). Their explicit positive factors prove strict transverse positivity and hence strict local minimality modulo rotation.

**3. Unique change of softest mode.** Exact subtraction gives
\[
L_1(u)-L_2(u)=\frac{4u(1-u)p(u)}{(1+u)^3(1+u^2)^3}.
\]
The polynomial \(p\) is reciprocal. On \(0<u<1\), set \(v=u+u^{-1}\in(2,\infty)\). Then
\[
\frac{p(u)}{u^3}=f(v)=v^3-4v^2-16v-16,
\qquad f'(v)=(3v+4)(v-4).
\]
The factorization of \(f'\) shows that \(f\) is decreasing on \((2,4)\), then strictly increasing on \((4,\infty)\). Since \(f(2)=-56\), \(f(4)=-80\), and \(f(v)\to+\infty\), there is exactly one \(v_*>4\) with \(f(v_*)=0\). The inverse map \(u=(v-\sqrt{v^2-4})/2\) gives one and only one \(u_*\in(0,1)\). The signs at \(u\downarrow0\) and \(u\uparrow1\) give the claimed ordering. At the crossing the two coefficients coincide, yielding isotropy in all three nonrotational directions.

**4. Sharp endpoint scales.** Direct expansion of the positive rational expressions gives \(L_1(u)=4u+O(u^2)\), \(L_2(u)=32u^2+O(u^3)\) as \(u\downarrow0\); and \(L_1(u)=\tfrac92(1-u)+O((1-u)^2)\), \(L_2(u)=8(1-u)+O((1-u)^2)\) as \(u\uparrow1\). This establishes the sharp least-eigenvalue asymptotics.

## Verification

Run `python3 check.py` with Python 3.10 or later, using only the standard library. The checker independently evaluates the geometric-series residue formulas with exact rational arithmetic; compares the rational stiffness expressions and factor identity; brackets the single algebraic transition; and compares second symmetric finite differences of the pairwise Poisson-energy formula against the analytic quadratic coefficients for several radii and both angular deformation types. Those finite tests are diagnostics, not a substitute for the general proof above.

## Relationship to prior work

Kovalev and Yang (first public preprint 19 July 2020) derive the boundary Poisson-kernel identity and classify extreme **pointwise** values of the angular derivative of finite Blaschke products; their optimization is over the minimum and maximum boundary speeds, not the local Hessian of the **squared integrated speed variance** with fixed equal-modulus zeros. Gluchoff and Hartmann (2013) investigate Hardy means and configurations of zeros, notably interior circle means of the Blaschke function itself; their angular comparison for degrees two and three is for a different functional and does not imply this degree-four variance-Hessian crossover. Related published analyses of angular Hessians for Bergman boundary-pole energies use other kernels and parameters, and do not transfer their numerical thresholds to the present Poisson-convolution energy. The present claim is deliberately local and degree four; it does not claim a new general theory of circular energy minimizers.

## Limitations

A coincident older formulation under discrete Poisson-energy or four-particle interaction terminology cannot be excluded solely by search, and priority remains provisional pending wider expert review. Numerical checks do not establish the infinite Fourier identities or unique crossing; those follow analytically in the proof. Only fixed, common zero radius and perturbations of the regular square are treated. There is no claim about global angular optimality, varying radii, higher degree, or an independent proof audit.

## References

1. L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760v1 (19 July 2020), https://arxiv.org/abs/2007.09760 .
2. A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative*, in *Blaschke Products and Their Applications*, Fields Institute Communications 65 (2013), DOI:10.1007/978-1-4614-5341-3_9 .
