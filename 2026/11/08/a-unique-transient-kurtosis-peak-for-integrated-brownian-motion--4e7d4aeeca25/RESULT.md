# A unique transient kurtosis peak for integrated Brownian motion with velocity resetting

## Finding
Consider an unconfined particle with position \(X_t\), velocity \(V_t\), initially \(X_0=V_0=0\), and dynamics \(dX_t=V_t\,dt\), \(dV_t=\sqrt{2D}\,dW_t\) between independent Poisson events of rate \(r>0\). Each event changes \(V_t\) to zero but leaves \(X_t\) unchanged; the Brownian innovations after each event are independent. For every \(D,r>0\) and \(t>0\), define the excess position kurtosis
\[
\mathcal K_r(t)=\frac{\mathbb E[X_t^4]}{(\mathbb E[X_t^2])^2}-3.
\]
Write \(z=rt\) and
\[
 f(z)=z-2+(z+2)e^{-z},\qquad
 g(z)=12z^2+120z-840+(9z^4+68z^3+288z^2+720z+840)e^{-z}.
\]
Then \(\mathcal K_r(t)=\mathcal K(z)=g(z)/(4f(z)^2)-3>0\). **The new conclusion is that \(\mathcal K\) is strictly increasing up to exactly one positive point \(z_*\), and strictly decreasing thereafter.** Thus the transient excess kurtosis has one and only one global maximum, at \(t_*=z_*/r\), independent of the acceleration-noise amplitude. The maximum is itself universal:
\[
 z_*=6.6595993253935155\ldots,\qquad \mathcal K(z_*)=3.4561814355534937\ldots.
\]
The exact specification of \(z_*\) is the unique positive zero of the explicitly defined exponential polynomial \(H\) in the proof. The endpoint laws are \(\mathcal K(z)=\frac9{10}z+O(z^2)\) as \(z\downarrow0\) and \(\mathcal K(z)=42/z+O(z^{-2})\) as \(z\to\infty\). The second/fourth moment formulas and the large-time fourth cumulant coefficient were previously published; they are not claimed here as new.

## Assumptions and scope
The process is on the full real line, with no mechanical friction and no refractory interval. Reset times form a homogeneous Poisson process independent of the Brownian driver. At each reset the velocity is set exactly to zero, and position is not reset. The initial velocity is zero, and \(\mathbb E[X_t]=0\). The theorem concerns the population excess kurtosis at a single deterministic time; it makes no claim about finite-sample estimates or about changing the reset law.

## Proof
Let \(L_1,\ldots,L_{N_t+1}\) be the positive inter-reset lengths making up \([0,t]\), including the unfinished final length, and set \(S_t=\sum_{j=1}^{N_t+1}L_j^3\). An integrated Brownian segment of length \(u\), started at velocity zero, is centered Gaussian with variance \(2Du^3/3\). Independence of the segments therefore gives
\[
 X_t\mid(L_1,\ldots,L_{N_t+1})\sim N\!\left(0,\frac{2D}{3}S_t\right),\quad
 \mathbb E[X_t^2]=\frac{2D}{3}\mathbb E[S_t],\quad
 \mathbb E[X_t^4]=\frac{4D^2}{3}\mathbb E[S_t^2].
\]
In particular, \(\mathcal K_r(t)=3\operatorname{Var}(S_t)/(\mathbb E[S_t])^2\). This is strictly positive: the event of no reset has positive probability and gives \(S_t=t^3\), while the event of precisely one reset, also of positive probability, gives \(S_t=u^3+(t-u)^3<t^3\) almost surely.

For completeness, first-renewal conditioning and a Laplace transform in \(t\) give, with \(m(t)=\mathbb E[S_t]\) and \(q(t)=\mathbb E[S_t^2]\),
\[
 \widetilde m(s)=\frac{6}{s^2(s+r)^2},\qquad
 \widetilde q(s)=\frac{720}{s^2(s+r)^5}+\frac{72r}{s^3(s+r)^5}.
\]
For example, the renewal recursion for \(q\) has the no-reset contribution \(e^{-rt}t^6\), a first-reset contribution \(r e^{-ru}[u^6+2u^3m(t-u)+q(t-u)]\) integrated over \(0<u<t\), and the analogous recursion for \(m\) has \(u^3+m(t-u)\). Exact inversion yields \(m(t)=6r^{-3}f(z)\) and \(q(t)=3r^{-6}g(z)\), giving the asserted formula for \(\mathcal K\). These moment expressions agree with the prior formulas in den Hollander et al. and Smith--Majumdar.

Since \(f(0)=0\) and \(f'(z)=1-(1+z)e^{-z}>0\) for \(z>0\), the derivative of \(\mathcal K\) has the sign of
\[
 H(z)=e^{2z}\bigl(g'(z)f(z)-2g(z)f'(z)\bigr).
\]
Direct differentiation and collection of exponentials give the exact identity
\[
\begin{split}
H(z)={}&(1440-168z)e^{2z}\\
&-(9z^5+32z^4+132z^3+264z^2+2544z+2880)e^z\\
&+9z^5+104z^4+564z^3+1704z^2+2712z+1440.
\end{split}
\]
Write \(H(z)=\sum_{n=0}^\infty a_nz^n\). Exact coefficient comparison shows \(a_0=\cdots=a_8=0\). For every integer \(n\ge6\), letting \((n)_{j}=n(n-1)\cdots(n-j+1)\),
\[
 n!a_n=2^n(1440-84n)-\bigl[9(n)_5+32(n)_4+132(n)_3+264(n)_2+2544n+2880\bigr].
\]
For \(n=9,10,11,12,13,14,15\), the values of \(n!a_n\) are respectively \(6048,33840,113784,291456,608088,1019616,1149840\), all positive. At \(n=16,17\), they are \(-374208,-7594512\). For every \(n\ge18\), the first term \(2^n(1440-84n)\) is negative and the subtracted bracket is strictly positive, so \(a_n<0\). Consequently all nonzero Taylor coefficients have exactly one sign transition: \(a_n>0\) for \(9\le n\le15\) and \(a_n<0\) for \(n\ge16\).

For \(z>0\), divide the entire series by \(z^{15}\). Its positive-coefficient terms are nonincreasing functions of \(z\), with at least one strictly decreasing, whereas its negative-coefficient terms are strictly decreasing. The power series and its derivative converge locally uniformly, so \(H(z)/z^{15}\) is **strictly decreasing**. As \(z\downarrow0\) it tends to \(+\infty\) by the \(a_9z^{-6}\) term, while as \(z\to\infty\) it tends to \(-\infty\) since \(H(z)\sim-168ze^{2z}\). It therefore has exactly one positive zero, with positive sign before and negative sign afterward. Because
\[
\mathcal K'(z)=\frac{e^{-2z}H(z)}{4f(z)^3},
\]
the same sign classification proves the strict increase and decrease and the unique global maximum.

Finally, Taylor expansion of the exact renewal moments gives \(\operatorname{Var}(S_t)=3rt^7/10+O(r^2t^8)\) and \(\mathbb E[S_t]=t^3+O(rt^4)\), yielding the small-\(z\) law. The leading terms of the exact moments are \(\mathbb E[S_t]=6t/r^2+O(1)\) and \(\operatorname{Var}(S_t)=504t/r^5+O(1)\), yielding \(42/z+O(z^{-2})\) at infinity. Numerical solving of the unique-zero equation gives the displayed approximations; uniqueness itself requires no numerical search.

## Verification
The accompanying standalone \(check.py\) reconstructs the exponential polynomial from \(f,g\), checks every finite sign needed in the coefficient argument and the all-order sign condition, verifies both Laplace-transform identities by symbolic inversion, checks the two endpoint expansions, and computes high-precision values of the unique zero and its kurtosis. All checks are finite or symbolic confirmation of the algebra. The analytic coefficient-sign argument, not any sampled grid, establishes uniqueness over the whole positive half-line.

## Relationship to prior work
Den Hollander, Majumdar, Meylahn and Touchette (arXiv:1801.09909, Section V, Theorem V.1) give the exact finite-time second and fourth moments of the area under Poisson-reset Brownian motion. Smith and Majumdar (arXiv:2202.03546, Section III, Eqs. (85)--(89)) repeat those exact moments and obtain the asymptotic cumulants, including the coefficient giving \(42/(rt)\). Olsen and Löwen (arXiv:2401.12685, Sections 2 and 3) frame exactly the velocity-only resetting interpretation and give a general recursion for displacement moments. Thus neither the model, the moment formulas, nor the leading long-time cumulants are novel. The additional global statement here is a **complete critical-point classification** of their dimensionless excess-kurtosis function, proved by the one-sign-change property of a nonpolynomial entire function. Searches described in the self-review did not find a published proof or statement of this strict global unimodality, but literature coverage cannot guarantee priority.

## Limitations
This is a theorem for the specified zero-initial-velocity Brownian acceleration model only. It does not assert unimodality for nonzero initial velocity, friction, random reset velocities, other renewal clocks, or other Gaussian self-similarity exponents. The exact moments and long-time cumulant coefficient are prior results and are included solely as premises. The root and peak figures are numerical approximations to an exact implicit characterization. No independent audit or experimental inference test has been carried out.

## References
- F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (first public version 2018-01-30), Section V, https://arxiv.org/abs/1801.09909.
- N. R. Smith, S. N. Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting*, arXiv:2202.03546 (first public version 2022-02-07), Section III, https://arxiv.org/abs/2202.03546.
- K. S. Olsen, H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (first public version 2024-01-23), Sections 2--3, https://arxiv.org/abs/2401.12685.
