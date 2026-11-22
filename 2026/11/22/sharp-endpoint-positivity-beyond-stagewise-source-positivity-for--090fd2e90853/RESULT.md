# Sharp endpoint positivity beyond stagewise source positivity for the cubic two-stage integrator

## Finding
For every integer \(n\ge1\), let \(X\) be any real symmetric \(n\)-by-\(n\) matrix with \(0\preceq X\preceq I\). Consider the cubic reaction \(Q(X)=X-X^3\), using ordinary matrix powers, and its two-stage explicit second-order update
\[
Y=X+hQ(X),\qquad Z=\tfrac12\bigl(X+Y+hQ(Y)\bigr),\qquad h\ge0.
\]
The sharp *completed-step* positive-semidefinite-preservation boundary is
\[
\boxed{Z\succeq0\text{ for all }0\preceq X\preceq I\quad\Longleftrightarrow\quad 0\le h\le H:=2\sqrt2-1.}
\]
At \(h=H\), precisely one scalar initial value \(x_*\in(0,1)\) has zero output, given by
\[
a_*:=\sqrt{2+\sqrt3},\qquad x_*:=\left(\frac{1+a_*^2}{1+a_*+a_*^4-a_*^3}\right)^{1/2} \approx0.7002523889.
\]
For every \(h>H\), choosing a scalar input \(x_*\), or a symmetric matrix containing \(x_*\) as an eigenvalue, makes the completed update have a negative eigenvalue.

The intermediate source \(Q(Y)\) is positive semidefinite **for all** initial matrices in the stated domain if and only if \(0\le h\le1/2\). Consequently, the nonempty interval \(1/2<h\le H\) preserves endpoint positive semidefiniteness universally even though some intermediate sources are not positive semidefinite. This is a distinction between two conditions, not a counterexample to a theorem assuming stagewise source positivity.

## Assumptions and scope
This theorem concerns one application of the unmodified two-stage explicit Heun/SSPRK2 formula for the *zero-linear-part* matrix equation \(\dot X=X-X^3\). Its initial domain is the symmetric spectral unit interval \(0\preceq X\preceq I\). The output guarantee is only \(Z\succeq0\), not \(Z\preceq I\). No assertion is made for nonlinear terms defined using entrywise cubic powers, general nonzero linear parts, nonsymmetric matrices, arbitrary real positive-semidefinite input spectra above one, or repeated timesteps.

## Proof
**1. Reduction to eigenvalues.** Every polynomial in a real symmetric \(X\) has the same orthonormal eigenbasis. It is therefore necessary and sufficient to establish nonnegativity of the scalar output \(z_h(x)\) for every \(x\in[0,1]\), where \(y=x+h(x-x^3)\) and \(z_h(x)=[x+y+h(y-y^3)]/2\). At \(x=0\), the update is zero; at \(x=1\), it is one. Hence consider \(0<x<1\).

**2. All possible zero crossings.** Set \(u=x^2\in(0,1)\) and \(a=y/x=1+h(1-u)\), so \(a>1\) whenever \(h>0\). Direct substitution yields
\[
\frac{2z_h(x)(1-u)}x=1+a^2-u(1+a+a^4-a^3).
\]
Thus a completed-step zero requires
\[
u=\frac{1+a^2}{1+a+a^4-a^3}\in(0,1),\qquad
h=G(a):=\frac{a^4-a^3+a+1}{a(a^2-1)}.
\]
Conversely, every \(a>1\) produces a valid \(u\in(0,1)\): the denominator-minus-numerator equals \(a(a-1)^2(a+1)>0\). The formula for \(h\) follows from \(h=(a-1)/(1-u)\). Therefore all strictly positive timestep zero crossings are parametrized, without omissions, by \(a>1\).

**3. Sharp minimal crossing.** The derivative factorizes exactly as
\[
G'(a)=\frac{(a^2+1)(a^4-4a^2+1)}{a^2(a-1)^2(a+1)^2}.
\]
The only critical point for \(a>1\) is \(a_*=\sqrt{2+\sqrt3}\). Since \(G(a)\to\infty\) as \(a\downarrow1\) and as \(a\to\infty\), it is the unique global minimizer, with exact value \(G(a_*)=2\sqrt2-1\). At \(h=H\), the only interior scalar root is \(x_*\) as stated. Continuity, together with \(z_0(x)=x>0\), proves that \(z_h(x)>0\) for all \(0<x<1\) and \(0\le h<H\), and \(z_H(x)\ge0\) throughout the interval.

**4. Every larger timestep fails at the same input.** For fixed \(u=x^2\in(0,1)\), the scalar ratio expands as
\[
\frac{z_h(x)}x=1+(1-u)h+\tfrac12(1-u)(1-3u)h^2-\tfrac32u(1-u)^2h^3-\tfrac12u(1-u)^3h^4.
\]
Read in descending powers of \(h\), its nonzero coefficient signs are \((-,-,\pm,+,+)\). Thus Descartes' rule gives *exactly one positive root*, counting multiplicity, because the expression is positive at zero and tends to minus infinity for \(h\to\infty\). At \(x=x_*\), that root is \(H\), so \(z_h(x_*)<0\) for every \(h>H\). The scalar example already proves necessity in all matrix dimensions, since a diagonal matrix may include this eigenvalue.

**5. Intermediate-source frontier.** For \(x\in[0,1]\), the first stage obeys \(y\ge0\), and
\[
y-1=(1-x)\bigl(hx(1+x)-1\bigr).
\]
For every input, \(y\le1\) if \(h\le1/2\), giving \(Q(y)=y-y^3\ge0\). Conversely, if \(h>1/2\), choose \(x<1\) sufficiently near one so that \(hx(1+x)>1\). Then \(y>1\) and \(Q(y)<0\). Applying this argument eigenvaluewise proves the claimed source threshold.

## Verification
The self-contained accompanying `verify.py` uses exact SymPy identities to check the scalar update, zero-crossing parametrization, derivative factorization, radical simplification and exact rational sign-reversal example. It additionally performs 500 rational interior diagnostic checks at five subthreshold timesteps. These finite checks are *diagnostic*, not a substitute for the analytic all-dimensions proof above. Running `python verify.py` requires Python 3 and SymPy. For a fully rational negative example, at \(h=2\), \(x=7/10\) gives
\[
z_2(7/10)=-44518243/125000000<0.
\]

## Relationship to prior work
Zhang, Lan and Jing (2026) study positivity-preserving integrating-factor SSP Runge–Kutta methods for differential Lyapunov equations. Their equation (5) reduces, when \(A=0\) and the nonlinear source is evaluated at each stage, to the two-stage update studied here; their experiment (10) uses \(Q(X)=X-X^3\). Their published positivity proof assumes the evaluated source \(Q\) is positive semidefinite. Our result quantifies the completed-step scalar/matrix positivity boundary *after* that stagewise hypothesis can fail. It is not a contradiction of their result or a new general SSP theory.

The earlier literature develops sufficient stagewise maximum-bound-principle restrictions or uses *stabilized, rescaled, extended, or otherwise modified* integrating-factor/Runge–Kutta methods for Allen–Cahn equations. Those algorithms and their maximum-bound principle requirements are logically different from the sharp nonnegative **completed output** of this unmodified zero-linear-part cubic method. In particular, the historical forward-Euler/SSP stagewise step bound \(1/2\) does not imply sharpness for endpoint semidefiniteness. No claim is made that exhaustive prior-art exclusion has been proved; the 2021 Applied Numerical Mathematics paper was only accessible through its abstract/metadata, leaving a historical-priority risk.

## Limitations
The theorem is one-step and proves a lower eigenvalue bound only. The scalar continuous flow is positive, but the discrete method might exceed one; therefore the theorem cannot be applied recursively without additional invariant-domain arguments. The proof relies on scalar functional calculus and does not extend automatically to entrywise cubics, noncommuting linear terms, or nonlinear matrix functions not sharing eigenvectors. Numerical diagnostics do not establish global results by themselves. Independent mathematical review has not been performed.

## References
- W. Zhang, R. Lan, X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation* (first publicly released 14 June 2026), arXiv:2606.15703v1, https://arxiv.org/abs/2606.15703 .
- L. Ju, X. Li, Z. Qiao, J. Yang, *Maximum bound principle preserving integrating factor Runge-Kutta methods for semilinear parabolic equations* (2020), arXiv:2010.12165, https://arxiv.org/abs/2010.12165 .
- J. Li, X. Li, L. Ju, X. Feng, *Stabilized integrating factor Runge–Kutta method and unconditional preservation of maximum bound principle* (2021), arXiv:2104.09977, https://arxiv.org/abs/2104.09977 .
- H. Zhang, J. Yan, X. Qian, S. Song, *Numerical analysis and applications of explicit high order maximum principle preserving integrating factor Runge-Kutta schemes for Allen-Cahn equation*, Applied Numerical Mathematics 161 (2021), 372–390, https://doi.org/10.1016/j.apnum.2020.11.022 .
- Z. Jiang, C. Quan, X. Zhao, *A Class of High Order Unconditional Maximum Principle Preserving Extended IFRK Schemes for Allen-Cahn Equation*, SIAM Journal on Scientific Computing 48 (2026), A474–A493, https://doi.org/10.1137/25M1730582 .
