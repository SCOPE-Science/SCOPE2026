# Topology-dependent benefit of hub resetting in equilateral Brownian stars

## Finding

Let \(m\ge1\) be an integer. On the metric star with \(m\) arms of common length \(L>0\), run Brownian diffusion with generator \(D\,d^2/dx^2\), \(D>0\), Kirchhoff conditions at the central junction, a perfectly absorbing endpoint on one designated arm, and reflecting endpoints on all the remaining arms. Start at the junction. Independently reset the walker instantaneously to the junction at Poisson rate \(r\ge0\); stop on first absorption.

Writing \(z=L\sqrt{r/D}\), its exact mean absorption time for \(r>0\) is
\[
T_m(r)=\frac{L^2}{D}\frac{m\cosh z-1-(m-1)\operatorname{sech}z}{z^2},
\quad T_m(0)=\frac{L^2}{D}\left(m-\frac12\right).
\]
Define the optimal fractional time saving
\[
R_m=1-\frac{\min_{r\ge0}T_m(r)}{T_m(0)}.
\]
Then \(R_1=0\), whereas \(0<R_2<R_3<\cdots\). In addition, the sharp degree-independent upper bound within this equilateral-star family is
\[
\sup_{m\ge1}R_m
=1-\min_{z>0}\frac{\cosh z-\operatorname{sech}z}{z^2}
=0.1447363448\ldots.
\]
The minimum on the right is attained at the **unique positive** root \(z_\infty\) of
\[
2\sinh(2z)-z\cosh(2z)-3z=0,
\qquad z_\infty\approx1.606115299.
\]
For every choice of positive minimizing rates \(r_m^*\) with \(m\ge2\), one has \(L\sqrt{r_m^*/D}\to z_\infty\) as \(m\to\infty\). Thus the gain increases strictly with branching but cannot exceed approximately \(14.474\%\) of the no-reset mean time. No uniqueness of the finite-\(m\) optimal rate is asserted.

The no-reset first-passage coefficient of variation is exactly
\[
\operatorname{CV}_m^2
=1+\frac{4m-5}{12(m-1/2)^2}.
\]
It is below one for the single arm and above one for every \(m\ge2\), locating the first beneficial-reset topology at two arms.

## Assumptions and scope

The central junction is a zero-storage Kirchhoff vertex: the exit probabilities to the \(m\) equal arms are equal, and the backward equation has continuous vertex values with zero sum of outward derivatives. The diffusion constant is spatially uniform. All arms have the same positive length. Exactly one tip is absorbing; the other \(m-1\) tips are Neumann reflecting. All resetting is instantaneous, exponential and specifically to the junction. The conclusions hold for each finite integer \(m\ge1\), all \(L,D>0\), and all \(r\ge0\). The bound is only asserted for these boundary conditions; it is not a universal constraint for unequal arms, different targets, or non-Poisson resetting.

## Proof

**1. Laplace transform without resetting.** Let \(\tau\) be the absorption time with \(r=0\), and put \(\phi_m(s)=\mathbb E[e^{-s\tau}]\), \(s>0\). On each arm, with coordinate \(0\le x\le L\) increasing away from the hub, the backward equation is \(D f''=sf\). Put \(k=\sqrt{s/D}\), \(z=kL\), and write the common junction value as \(a\). On each reflecting arm the unique solution is
\[
f_j(x)=a\frac{\cosh(k(L-x))}{\cosh z},
\]
whose derivative at the hub is \(-ka\tanh z\). On the target arm write \(f_t(x)=a\cosh(kx)+b\sinh(kx)\). Kirchhoff balance gives \(b=(m-1)a\tanh z\). The target boundary condition \(f_t(L)=1\) therefore yields
\[
\phi_m(s)=a=\frac{\cosh z}{1+m\sinh^2 z}.
\]
Continuity and elliptic uniqueness guarantee this is the desired transform.

**2. Renewal and small-rate expansion.** Repeated independent attempts separated by Poisson resetting give the exact restart identity
\[
T_m(r)=\frac{1-\phi_m(r)}{r\phi_m(r)}.
\]
Substitution gives the formula in the Finding. Taylor expansion at zero yields
\[
\frac{D}{L^2}T_m(r)
=m-\frac12+\frac{5-4m}{24}z^2+O(z^4).
\]
In particular, every \(m\ge2\) has \(T_m(r)<T_m(0)\) at sufficiently small positive \(r\). For \(m=1\), the normalized mean is \(2(\cosh z-1)/z^2>1\) for every \(z>0\), by the strictly positive higher coefficients of the exponential series. For \(m\ge2\), the mean tends to infinity as \(z\to\infty\); continuity then yields a positive minimizing rate.

Differentiating the identity at \(r=0\), or using the first two coefficients of \(\phi_m\), gives \(\mathbb E\tau=(m-1/2)L^2/D\) and
\[
\mathbb E\tau^2
=\left[2(m-1/2)^2+\frac{4m-5}{12}\right]\frac{L^4}{D^2}.
\]
The stated coefficient-of-variation formula follows by subtracting the square of the mean and dividing by it.

**3. Strict monotonicity with branch number.** For \(z>0\), define the normalized mean \(H_m(z)=T_m(Dz^2/L^2)/T_m(0)\). A direct algebraic decomposition gives
\[
H_m(z)=F(z)+\frac{G(z)}{m-1/2},
\quad F(z)=\frac{\cosh z-\operatorname{sech}z}{z^2},
\quad G(z)=\frac{\cosh z+\operatorname{sech}z-2}{2z^2}.
\]
Here \(G(z)=(\cosh z-1)^2/(2z^2\cosh z)>0\). Consequently \(H_{m+1}(z)<H_m(z)\) for every positive \(z\). Evaluating the strict inequality at any positive minimizer for \(m\ge2\) proves \(R_{m+1}>R_m\); the \(m=1\) case was handled above.

**4. Limiting optimum, uniqueness, and sharpness.** The positive function \(F\) extends continuously to \(F(0)=1\), has \(F(z)=1-z^2/6+O(z^4)\) near zero, and diverges as \(z\to\infty\). Differentiation shows that \(F'(z)\) has the opposite sign of
\[
Q(z)=2\sinh(2z)-z\cosh(2z)-3z.
\]
Its power-series identity is
\[
Q(z)=\frac23z^3-
\sum_{j=2}^{\infty}\frac{2^{2j}}{(2j)!}
\left(1-\frac4{2j+1}\right)z^{2j+1}.
\]
The function \(Q(z)/z^3\) is strictly decreasing from \(2/3\) to \(-\infty\) on positive \(z\); hence it has one zero. This proves that \(F\) has exactly one positive global minimizer \(z_\infty\). Since \(H_m(z)>F(z)\) for \(z>0\) and \(H_m(z)\to F(z)\) pointwise, their minima converge to \(\min F\), using evaluation at \(z_\infty\) for the upper bound. For large \(m\), every minimizer of \(H_m\) stays in a compact subset of \((0,\infty)\) because \(F(0)=1>\min F\) and \(F\to\infty\); local uniform convergence and uniqueness of the limit minimizer imply that every sequence of optimal dimensionless rates tends to \(z_\infty\). This also proves sharpness of the limiting fractional-gain bound.

## Verification

The included `verify.py` uses only the Python standard library. It independently discretizes the backward boundary-value problem on each arm, checks its hub solution against the closed-form Laplace transform, verifies the renewal formula and small-branch optimum, and checks strict pointwise degree monotonicity and the numerical limiting constant. Its 52 diagnostics pass with a maximum finite-difference transform tolerance of \(10^{-4}\) at 3,200 segments per arm. These numerical checks support but are not substitutes for the all-dimension analytic proof above. Reproduce with `python3 verify.py`.

## Relationship to prior work

Evans and Majumdar's 2011 model introduced Poisson resetting for Brownian target search and supplies the general renewal mechanism. Their solved geometry is the half-line, not an equilateral star with one absorbing and many reflecting tips. Their 2011 follow-up treats variable reset laws and target distributions, again without the stated topological monotonicity. Riascos, Boyer, Herringer and Mateos (2019 preprint, 2020 journal) derive spectral formulas for reset random walks on discrete networks and analyze finite Cayley trees, but do not state the Kirchhoff metric-star degree threshold or the sharp large-degree gain. Dassios and Zhang (first published 2021) derive Brownian hitting-time transforms on multiple rays with **all** outer tips as stopping boundaries and **no** restarting. The boundary/target observable and the claimed optimization result are different. These general theories motivate the model and could assist its derivation; the claimed contribution is the particular sharp topology-dependent optimization and limiting fractional gain, not a new renewal identity.

## Limitations

The conclusion is specific to equilateral metric stars, a single fully absorbing tip, uniformly reflecting other tips, Kirchhoff junction transport, and immediate Poisson resetting. The result does not assert a thermodynamic phase transition, a generalized benefit for all graphs, or uniqueness of each finite-degree optimum. Literature comparison was made against accessible full text and searchable indexed records; obscure earlier network-resetting work might contain equivalent special cases. Numerical constants are approximations, while the defining minimization and transcendental equation are exact. Independent validation has not been carried out.

## References

1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first posted 2011-02-14), https://arxiv.org/abs/1102.2704.
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (first posted 2011-07-21), https://arxiv.org/abs/1107.4225.
3. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random Walks on Networks with Stochastic Resetting*, arXiv:1910.13568 (first posted 2019-10-29), https://arxiv.org/abs/1910.13568.
4. A. Dassios and J. Zhang, *First Hitting Time of Brownian Motion on Simple Graph with Skew Semiaxes*, first published 2021-09-15, https://doi.org/10.1007/s11009-021-09884-4.
