# Sharp inverse-distance escape and Floquet-gap law at a three-dimensional Filippov cycle boundary

## Finding

In the symmetric zero-divergence three-dimensional Filippov family below, fix any \(\mu>0\), and let \(H\) increase to the upper boundary \(H_*=1/(2\cosh(\pi\mu)-1)\) through the interval of attracting crossing cycles. Put
\[
 k=e^{-\pi\mu},\qquad D=1-k+k^2,\qquad \delta=H_*-H>0,
\]
\[
 c=\frac{2k\mu(1-k)(1+k+k^2)}{(1+k)D^2},\quad
 A=\frac{2\mu(1-k)(1+k+k^2)}{(1+\mu^2)D^2},\quad
 K=\frac{2(1+k)D}{k(1-k)}.
\]
All three constants are strictly positive. Write \(p_0(H)=(x_0(H),y_0(H),0)\) for the positive upward crossing, \(T(H)\) for its minimal period, and \(M_+(H)\) for the transverse full-return multiplier that tends to \(1\) (the other tends to \(k^2\)). Then, for each fixed \(\mu>0\),
\[
 x_0(H)=\frac{A}{\delta}+O_\mu(1),\qquad
 y_0(H)=\frac{kA}{\delta}+O_\mu(1),
\]
\[
 T(H)=2\pi+\frac{2}{c}\delta+O_\mu(\delta^2),\qquad
 M_+(H)=1-K\delta+O_\mu(\delta^2).
\]
In particular,
\[
 \boxed{\lim_{H\uparrow H_*}x_0(H)[1-M_+(H)]
 =KA=\frac{4\mu(1+k)(1+k+k^2)}{k(1+\mu^2)D}>0.}
\]
Thus the cycle's crossing amplitude diverges precisely inversely with its vanishing contraction gap.

The *complete, rescaled periodic curve* also has a nonzero limit. Define
\[
 A_* =\begin{pmatrix}
 -2\mu&0&-H_*(9\mu^2+1)\\
 0&2\mu&-(1+\mu^2)\\
 0&1&0
 \end{pmatrix},\qquad P=(A,kA,0)^\mathsf T,
 \qquad S(x,y,z)=(-y,-x,-z).
\]
For the upper flight \(p_H^+(s)\), \(0\le s\le T(H)/2\),
\[
 \delta p_H^+\!\left(\frac{T(H)}2\theta\right)
 \longrightarrow q_+(\pi\theta):=e^{\pi\theta A_*}P,
 \qquad 0\le\theta\le1,
\]
with convergence in \(C^1([0,1];\mathbb R^3)\). The lower flight converges to \(S q_+(\pi\theta)\) in the same manner. Explicitly, for \(0\le s\le\pi\),
\[
 \begin{split}
 q_{+,z}(s)&=kA e^{\mu s}\sin s,\\
 q_{+,y}(s)&=kA e^{\mu s}(\cos s+\mu\sin s),\\
 q_{+,x}(s)&=A e^{-2\mu s}
 \bigl[1-H_*k\{e^{3\mu s}(3\mu\sin s-\cos s)+1\}\bigr].
 \end{split}
\]
This curve satisfies \(q_+(0)=P\) and \(q_+(\pi)=SP\) and has \(q_{+,z}(s)>0\) for \(0<s<\pi\). Its reflected lower flight closes a nonzero \(2\pi\)-periodic orbit of the *homogeneous limiting switched system*. Every positive scalar multiple is another such orbit. These limiting curves are not claimed to be finite-amplitude cycles of the original affine field at \(H=H_*\).

## Assumptions and scope

Use the canonical crossing-flight representative of Ferreira's symmetric, zero-divergence family, with switching plane \(\Sigma=\{z=0\}\), the upper field on \(z>0\), and its involutive partner on \(z<0\):
\[
 \begin{aligned}
 \dot x&=-2\mu x-H(9\mu^2+1)z+H,\\
 \dot y&=2\mu y-(1+\mu^2)z+1,\\
 \dot z&=y;\\
 X^-&=S_* X^+ S,
 \end{aligned}
\]
where \(S_*\) acts on vector fields by the derivative of the linear involution \(S\). The result concerns the unique transverse two-crossing periodic family already classified for \(\mu>0\) and \(H_{\mathrm g}(\mu)<H<H_*(\mu)\). It makes no claim at \(\mu=0\), no uniform-in-\(\mu\) error bound, and no assertion about sliding or all initial conditions.

## Proof

**1. Source parametrization and the critical parameter.** Put \(\zeta=(1+\mu^2)^{-1}\), \(\beta=2\mu\zeta\), and let \(t\) be the positive half-period. The established analytic parametrization is
\[
 x_0(t)=\zeta\left[\mu-\frac{e^{\mu t}-\cos t}{\sin t}\right],\quad
 y_0(t)=\zeta\left[\frac{\cos t-e^{-\mu t}}{\sin t}-\mu\right],
\]
\[
 H=\eta(t)=\frac{x_0(t)y_0(t)+\zeta}
 {x_0(t)^2+y_0(t)^2-x_0(t)y_0(t)-\beta[x_0(t)-y_0(t)]+\zeta},
 \qquad \pi<t<t_{\mathrm g}(\mu).
\]
The source proves that \(\eta\) is strictly decreasing and that \(t\downarrow\pi\) corresponds to \(H\uparrow H_*\), with \(T=2t\).

**2. Desingularization at infinity.** Let \(u=t-\pi\downarrow0\), \(X=\zeta(1+k)/k\), and \(Y=kX\). Direct Taylor expansion of the displayed analytic expressions gives
\[
 x_0=X/u+\mu X+O_\mu(u),\qquad
 y_0=Y/u-\mu Y+O_\mu(u).
\]
Set \(B=X^2+Y^2-XY\) and \(C=2\mu(X^2-Y^2)-\beta(X-Y)\). Then
\[
 x_0y_0+\zeta=XY/u^2+O_\mu(1),\quad
 x_0^2+y_0^2-x_0y_0-\beta(x_0-y_0)+\zeta
 =B/u^2+C/u+O_\mu(1).
\]
Consequently,
\[
 \eta(t)=\frac{XY}{B}\left(1-\frac CB u+O_\mu(u^2)\right),
 \qquad \frac{XY}{B}=\frac{k}{D}=H_*.
\]
Since \(C=2\mu(X-Y)(X+Y-\zeta)>0\), the coefficient \(c=H_*C/B\) is positive. Reducing this elementary rational expression gives the stated closed form for \(c\). Therefore \(\delta=c u+O_\mu(u^2)\) and \(u=\delta/c+O_\mu(\delta^2)\). The first three claimed asymptotics follow, with \(A=Xc\).

**3. Sharp Floquet deficit.** The source proves that the derivative \(N\) of its symmetry-reduced half-return map has
\[
 \det N=\rho=\frac{y_0}{x_0},\quad
 \operatorname{tr}N=H\left(\frac\rho E+E\right)
 -\beta(1+\rho)\frac{x_0-Hy_0}{Q(-x_0)},
\]
where \(E=e^{-2\mu t}\), \(Q(v)=v^2+\beta v+\zeta\), and that its eigenvalues squared are the two nontrivial full-cycle Floquet multipliers. The expansions from Step 2 give
\[
 \rho=k-2\mu k u+O_\mu(u^2),\quad
 E=k^2(1-2\mu u)+O_\mu(u^2),\quad
 \operatorname{tr}N=1+k+\frac{2\mu(k^2-k-1)}D u+O_\mu(u^2).
\]
Because \(0<k<1\), the two eigenvalues at \(u=0\) are distinct. Expanding the characteristic polynomial at the eigenvalue \(1\) yields
\[
 \lambda_+(u)=1-\frac{2\mu(1+k+k^2)}D u+O_\mu(u^2).
\]
Hence \(M_+=\lambda_+^2=1-4\mu(1+k+k^2)u/D+O_\mu(u^2)\). Replacing \(u\) by \(\delta/c+O_\mu(\delta^2)\) yields exactly \(K=4\mu(1+k+k^2)/(Dc)\) and the stated rational formula for \(K\). The second full-return multiplier tends to \(k^2\).

**4. Limiting loop.** Let \(A_H\) be the matrix of the upper affine field and \(b_H=(H,1,0)^\mathsf T\). The upper orbit has the exact variation-of-constants expression
\[
 p_H^+(s)=e^{sA_H}p_0(H)+\int_0^s e^{(s-v)A_H}b_H\,dv.
\]
By Steps 1–2, \(\delta p_0(H)\to P\), \(A_H\to A_*\), and \(t(H)\to\pi\). Multiplying by \(\delta\), changing to normalized time \(s=t(H)\theta\), and differentiating the matrix-exponential formula proves the claimed \(C^1\) convergence. Solving the last two homogeneous equations yields \(q_{+,z}\) and \(q_{+,y}\) above; integrating the first equation with an integrating factor yields \(q_{+,x}\). Substitution of \(H_*=k/D\) gives \(q_+(\pi)=SP\), and \(q_{+,z}>0\) on the open flight. The lower flow is the image under \(S\), hence gives a negative-\(z\) return from \(SP\) to \(P\). Homogeneity makes every positive multiple of this limiting periodic orbit another one. This finishes the single boundary theorem.

## Verification

Run `python CHECK.py` with SymPy and mpmath installed. The standalone script verifies rational-symbolic identities for \(c\), \(A\), the first derivative of \(\lambda_+\), and \(K\); tests the limit coefficients at three distinct positive values of \(\mu\) using 85-digit arithmetic; and compares the rescaled affine flights with the homogeneous limiting curve. These computations support but do not replace the analytic expansions and matrix-flow proof above.

## Relationship to prior work

Ferreira (2026, arXiv:2609.33034v1) proves the existence interval, explicit crossing parametrization, global uniqueness and attraction, and the qualitative endpoint facts \(x_0,y_0\to\infty\), \(T\to2\pi\), and transverse multipliers \(\to1,k^2\). The present theorem takes those established facts as inputs and supplies the *first-order parameter-normalized amplitude, period, and spectral-gap coefficients together with the entire nonzero rescaled critical loop*. It does not claim to originate the model or the large-amplitude boundary.

Ferreira, Freitas and Medrado (2026, arXiv:2604.25773v1) establish analytic half-return-time expansions and limiting stability criteria near infinity in a broader symmetric framework, but do not provide these four fixed-\(\mu\), inclination-normalized limits for the classified canonical branch. Freire and collaborators (2020, DOI:10.1016/j.nonrwa.2020.103112) analyze a different *continuous three-zone* oscillator with an infinity bifurcation and analytic amplitude/period estimates. Its hypotheses and return map are not those of the present *two-zone discontinuous visible-two-fold* system, so its expansion does not furnish the coefficients above.

## Limitations

The estimates hold for each fixed \(\mu>0\) only as \(H\uparrow H_*\) within the admissible cycle wedge. They are not uniform as \(\mu\downarrow0\) or \(\mu\to\infty\). The nontrivial limiting homogeneous cycle is a rescaled object, not a finite periodic orbit of the original affine field at the boundary. No global basin classification at that boundary, no classification of sliding continuations, and no independent audit are asserted. More general historical infinity-bifurcation theorems could share the qualitative rates but have not been shown to imply these precise model-specific constants and profile.

## References

- S. C. S. Ferreira, *Global classification of oscillatory dynamics in symmetric zero-divergence 3D piecewise-linear Filippov systems with a visible–visible two-fold*, arXiv:2609.33034v1, first posted September 27, 2026. https://arxiv.org/abs/2609.33034
- S. C. S. Ferreira, B. R. Freitas, J. C. R. Medrado, *Symmetric Limit Cycles in 3D Piecewise Linear Systems with Visible-visible Two-Fold Singularity*, arXiv:2604.25773v1, first posted April 28, 2026. https://arxiv.org/pdf/2604.25773
- E. Freire, E. Ponce, J. Ros, E. Vela, A. Amador, *Hopf bifurcation at infinity in 3D symmetric piecewise linear systems. Application to a Bonhoeffer–van der Pol oscillator*, Nonlinear Analysis: Real World Applications **54** (2020), 103112. https://doi.org/10.1016/j.nonrwa.2020.103112
