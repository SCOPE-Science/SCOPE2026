# An exponentially weighted logarithmic critical-window law in an immigration host–parasitoid map

## Finding and scope

Fix \(0<\alpha<1\), \(\lambda\in\mathbb R\), and positive initial densities \(x_0,y_0\) independent of the integer \(N\). In each experiment keep \(\beta_N\) fixed for all iterates:
\[
x_{n+1}=\alpha x_ne^{-y_n}+\beta_N,\qquad
y_{n+1}=\alpha x_n(1-e^{-y_n}),\qquad
\beta_N=(1-\alpha)/\alpha+\lambda/N.
\]
Put
\[
c=\frac{\alpha}{1-\alpha},\qquad a=\frac{1+\alpha}{2(1-\alpha)},\qquad
B=\frac{1+3\alpha+9\alpha^2-\alpha^3}{6(1-\alpha)^2(1+\alpha)},\qquad
U_\lambda(t)=a\int_0^t e^{-c\lambda s}\,ds.
\]
Then for every fixed \(0<\varepsilon\le T<\infty\), uniformly for \(\varepsilon\le t\le T\),
\[
\frac{1}{y_{\lfloor Nt\rfloor}}=N U_\lambda(t)+B e^{-c\lambda t}\log N+O(1).
\]
In particular \(Ny_{\lfloor Nt\rfloor}\to U_\lambda(t)^{-1}\) and
\(N(x_{\lfloor Nt\rfloor}-1/\alpha)\to [\lambda-U_\lambda(t)^{-1}]/(1-\alpha)\) uniformly on these windows. The bounded remainder may depend on the fixed parameters, initial data and window. Initial data need not be on any invariant manifold. No bounded-residual limit or assertion for times much larger than \(N\) is made.

## Proof

**Entry and trapping.** Write \(\mu=\lambda/N\), \(R_\mu=1/\alpha+\mu/(1-\alpha)\), and \(h_n=x_n-R_\mu\). For sufficiently large \(N\), positive initial coordinates stay positive, and
\[
h_{n+1}=\alpha h_n-y_{n+1},\qquad y_{n+1}=(1+c\mu+\alpha h_n)(1-e^{-y_n}).
\]
At \(\mu=0\), the inequality \(x_{n+1}\le\alpha x_n+\beta_0\) gives \(\limsup x_n\le1/\alpha\). For any \(\xi>0\), eventually \(y_{n+1}\le(1+\alpha\xi)(1-e^{-y_n})\). This increasing, strictly concave scalar map has a unique positive fixed point and its iterates from any positive point converge to that fixed point by monotone comparison. Its fixed point tends to zero as \(\xi\downarrow0\): the fixed points are bounded by \(1+\alpha\xi\) and every limit point solves \(y=1-e^{-y}\). Thus \(y_n\to0\), and the stable equation for \(h_n\) gives \(h_n\to0\).

Set \(p=-1/(1-\alpha)\), \(z_n=h_n/y_n\), and \(r_n=y_{n+1}/y_n\). The equations imply
\[
r_n=(1+c\mu+\alpha y_nz_n)\frac{1-e^{-y_n}}{y_n},\qquad
z_{n+1}-p=\frac\alpha{r_n}(z_n-p)+\alpha p(1/r_n-1).
\]
Along the critical trajectory \(r_n\to1\); the last equation is eventually a uniform contraction with vanishing forcing, so \(z_n\to p\).

For detuned orbits take a rectangle \(|z-p|\le\delta_z\), \(0<y\le\eta\), with \(\delta_z>0\) small first and \(\eta>0\) chosen separately, sufficiently small relative to \(\delta_z\). The expansion \(r=1+c\mu+(\alpha z-1/2)y+O(y^2+|\mu|y)\), with \(\alpha p-1/2=-a<0\), gives constants \(D,c_1,c_2>0\) such that
\[
1-D/N-c_2y\le r\le1+D/N-c_1y.
\]
Take \(\eta\) smaller and \(N\) larger so that \(\alpha/r\le\theta_0=(1+\alpha)/2\) and \(|\alpha p(1/r-1)|\le(1-\theta_0)\delta_z\). This is possible since \(|r-1|\le D/N+C\eta\). The \(z\)-update stays in its interval. If \(y\le\eta/2\), \(r\le2\) suffices for \(ry\le\eta\); otherwise \(r\le1\) for large \(N\). The rectangle is therefore invariant. Choose a fixed \(n_0\ge1\) for which the critical orbit is in its interior. Continuity of finitely many iterates puts the detuned orbits there too for all sufficiently large \(N\).

With \(u_n=1/y_n\), shrink \(\eta\) so \(D/N+c_2\eta\le1/2\) for large \(N\). Taking reciprocals in the ratio inequalities yields
\[
(1-D/N)u_n+c_1\le u_{n+1}\le (1+2D/N)u_n+2c_2.
\]
Here the lower bound uses \(1/r\ge 2-r\); the upper uses \((1-v)^{-1}\le1+2v\) for \(0\le v\le1/2\). Iteration up to \(n\le NT\), with \(u_{n_0}\) bounded above and below away from zero by continuity, gives \(u_n\asymp_T n+1\).

**Slow jet and stable error.** Put \(H(y)=py+qy^2\), where \(q=-\alpha(1+\alpha)/[2(1-\alpha)^3]\). Its image in the slow coordinate is
\[
Y(y,\mu)=(1+c\mu+\alpha H(y))(1-e^{-y})
=y+c\mu y-a y^2+b y^3+O(y^4+|\mu|y^2),\quad
b=\frac{1-6\alpha^2-\alpha^3}{6(1-\alpha)^3}.
\]
Indeed the quadratic and cubic coefficients of \(Y(y,0)\) are \(\alpha p-1/2\) and \(1/6-\alpha p/2+\alpha q\). The choices \((1-\alpha)p=-1\), \((1-\alpha)q=a(p+1)\) cancel the linear and quadratic coefficients of \(H(Y(y,0))+Y(y,0)-\alpha H(y)\). Detuning changes this defect by \(O(|\mu|y)\), so it is \(O(y^3+|\mu|y)\). With \(e_n=h_n-H(y_n)\) we have \(y_{n+1}-Y(y_n,\mu)=\alpha(1-e^{-y_n})e_n\). The stable equation and bounded derivative of \(H(y)+y\) give
\[
|e_{n+1}|\le(\alpha+C y_n)|e_n|+C(y_n^3+|\mu|y_n).
\]
In the preceding rectangle choose \(\eta\) sufficiently small and \(N\) large so \(\alpha+C\eta\le\theta<1\), \(r_n\ge1-\rho>0\), and \(\theta(1-\rho)^{-3}<1\); choose \(\theta\) strictly between \(\alpha\) and one before shrinking. Then \(y_j\le y_n(1-\rho)^{-(n-j)}\) for \(j\le n\), and the geometric convolution gives
\[
|e_n|\le C\bigl(y_n^3+|\mu|y_n+\theta^{n-n_0}\bigr)\qquad(n_0\le n\le NT).
\]

**Reciprocal recurrence.** The actual ratio and the graph ratio \(Y(y_n,\mu)/y_n\) differ by \(O(|e_n|)\), with both bounded away from zero. Replacing the actual ratio by the graph ratio in \(u_{n+1}\) thus costs at most \(C u_n|e_n|\). In the graph reciprocal, retaining terms of orders \(1,\mu,y_n,y_n^2\) gives
\[
u_{n+1}=(1-c\lambda/N)u_n+a+\frac{d}{u_n}+E_{n,N},\qquad d=a^2-b,
\]
\[
|E_{n,N}|\le C\left(u_n^{-2}+N^{-1}+u_n/N^2+\theta^{n-n_0}u_n\right).
\]
The bound includes the discarded products \(O(y_n^3+|\mu|y_n+\mu^2)\) in the graph reciprocal, multiplied by \(u_n\), and the stable error. By \(u_n\asymp_T n+1\), the sum of \(|E_{n,N}|\) through \(\lfloor NT\rfloor\) is bounded. Direct summation of \(u_{n+1}-u_n-a\) gives \(u_n=an+O_T(1+n^2/N+\log(n+1))\); dividing the difference by \(anu_n\) and summing gives
\[
\sum_{j=n_0}^{\lfloor NT\rfloor}\left|u_j^{-1}-(aj)^{-1}\right|=O_T(1).
\]

**Weighted summation.** Write \(r_N=1-c\lambda/N>0\). Variation of constants, the bounded error sum, and uniformly bounded powers of \(r_N\) give
\[
u_n=a\sum_{j=n_0}^{n-1}r_N^{n-1-j}+\frac{d}{a}\sum_{j=n_0}^{n-1}\frac{r_N^{n-1-j}}j+O_T(1).
\]
For \(n=\lfloor Nt\rfloor\), \(\varepsilon\le t\le T\), the first sum with its coefficient is \(NU_\lambda(t)+O_T(1)\), by the uniform Riemann sum estimate (also valid for \(\lambda=0\)). Since \(r_N^{n-1-j}=e^{-c\lambda t}+O_T((j+1)/N)\), the harmonic sum is \(e^{-c\lambda t}\log N+O_{\varepsilon,T}(1)\). Simplification gives \(d/a=B>0\). The host limit follows from \(h_n=H(y_n)+e_n=py_n+O_T(y_n^2+|\mu|y_n+\theta^{n-n_0})\) and the definition of \(R_\mu\).

## Verification and prior context

The companion `checker.py` uses exact symbolic arithmetic for the critical jet, the invariance cancellations and \(d/a\). Its floating-point trajectories are finite illustrations at \(t=1\), not a proof of trapping, uniformity or bounded remainder. The two-width invariant rectangle above is needed for the trapping argument; the ratio variable need not stay within an arbitrary equal-width box.

Hu, Shen and Jia [1] establish the threshold and critical global attraction, not this two-term clock. Known leading finite-time scaling for transcritical normal forms [2] accounts for the leading profile once the slow equation is identified, not the logarithmic coefficient. A related finite-window weighted logarithm in a neutral-flip sigmoid map [3] uses inverse-square amplitude; it does not give the present map's cubic coefficient, positive-data trapping or host response. The result is model-specific; neither transcritical scaling nor the weighted summation method is claimed as new. No claim of exhaustive historical priority is made.

[1] L. Hu, Y. Shen and X. Jia, *Global behavior of a discrete population model*, AIMS Mathematics **9** (2024), 12128–12143, https://doi.org/10.3934/math.2024592, Sections 4–5.

[2] D. A. Martin, Q.-Y. Tang and D. R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, https://arxiv.org/abs/2505.24673, Sections II–III.

[3] *An exponentially weighted logarithmic crossover at the neutral flip of a sigmoid interval map*, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-an-exponentially-weighted-logarithmic-crossover-at-the-neutral-f--ec7e4796f3ca/RESULT.md.
