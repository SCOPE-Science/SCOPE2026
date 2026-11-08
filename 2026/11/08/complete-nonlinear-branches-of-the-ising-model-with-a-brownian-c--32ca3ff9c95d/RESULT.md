# Complete nonlinear branches of the Ising model with a Brownian-covariance graphon

## Finding
Consider the zero-field ferromagnetic continuum Ising self-consistency equation
\[
m(x)=\tanh\!\left(\beta\int_0^1\min\{x,y\}m(y)\,dy\right),\qquad 0\le x\le1,\quad \beta>0.
\]
Set \(\beta_j=\pi^2(2j+1)^2/4\) for integers \(j\ge0\). For every finite positive \(\beta\), the complete set of continuous real solutions consists of \(m\equiv0\) and, for each \(j\) satisfying \(\beta>\beta_j\), exactly two nonzero solutions \(\pm m_{j,\beta}\). There are no further solutions, including at equality \(\beta=\beta_j\).

Normalize \(m_{j,\beta}\) by a positive initial derivative of its effective field. It has precisely \(j\) interior zeros, at the **temperature-independent** locations
\[
x_k=\frac{2k}{2j+1},\qquad k=1,\dots,j,
\]
and alternating signs between those zeros. Its effective-field amplitude \(a>0\) is the unique solution of
\[
\sqrt\beta=(2j+1)\,Q(a),\qquad
Q(a)=\int_0^a\frac{ds}{\sqrt{2[\log\cosh a-\log\cosh s]}}.
\]
The total magnetization of the chosen sign branch is strictly positive and satisfies
\[
M_j(\beta)=\int_0^1m_{j,\beta}(x)\,dx
=\sqrt{\frac{2\log\cosh a}{\beta}}.
\]
At the birth of branch \(j\), its amplitude obeys
\[
a=2\sqrt{\frac{\beta-\beta_j}{\beta_j}}+O((\beta-\beta_j)^{3/2}),
\quad \beta\downarrow\beta_j,
\]
with the implicit constant allowed to depend on \(j\). At fixed \(j\), as \(\beta\to\infty\),
\[
a\sim\frac{\beta}{2(2j+1)^2},\qquad M_j(\beta)\longrightarrow\frac{1}{2j+1}.
\]
For the standard zero-field continuum free-energy functional given below, \(m\equiv0\) is the **unique global minimizer** for \(\beta\le\pi^2/4\); for \(\beta>\pi^2/4\), the **only global minimizers** are \(\pm m_{0,\beta}\). The sign-changing solutions are stationary profiles, not additional global thermodynamic phases.

## Assumptions and scope
The graphon is exactly \(W(x,y)=\min\{x,y\}\) on the unit square, and the dimensionless attractive coupling is absorbed into \(\beta>0\). It is symmetric, takes values in \([0,1]\), and defines a compact, strictly positive self-adjoint integral operator \(K\) on \(L^2[0,1]\). The theorem classifies solutions of the displayed continuum equation; no claim is made that its excited stationary branches are stable under a particular finite-size stochastic dynamics.

Define the entropy density, continuously extended at \(\pm1\), by
\[
s(t)=\frac{1+t}{2}\log\frac{1+t}{2}+\frac{1-t}{2}\log\frac{1-t}{2},\qquad -1\le t\le1.
\]
The dimensionless free-energy functional on measurable \(|m|\le1\) is
\[
\mathcal F_\beta[m]=\int_0^1s(m(x))\,dx-\frac\beta2\int_0^1\!\int_0^1\min\{x,y\}m(x)m(y)\,dx\,dy.
\]
All global-minimizer assertions refer to this functional, with no external field.

## Proof
**1. Exact boundary reduction.** For any bounded \(m\), set \(h=\beta Km\). Direct differentiation of
\[
(Km)(x)=\int_0^x y m(y)\,dy+x\int_x^1m(y)\,dy
\]
gives \((Km)'(x)=\int_x^1m(y)\,dy\), \((Km)''(x)=-m(x)\), and \((Km)(0)=(Km)'(1)=0\). Thus every solution of the self-consistency equation is smooth and has \(m=\tanh h\), where
\[
h''=-\beta\tanh h,\qquad h(0)=0,\quad h'(1)=0.\tag{1}
\]
Conversely, the difference between \(h\) satisfying (1) and \(\beta K\tanh h\) has identically zero second derivative and the same mixed boundary data, so it vanishes. This proves a bijection between solutions of the integral equation and of (1).

**2. Every nonzero solution lies on one soft-oscillator orbit.** If \(h'(0)=0\), uniqueness of the smooth initial-value problem gives \(h\equiv0\). Otherwise flip the overall sign if necessary, so \(v=h'(0)>0\). Conservation of energy yields
\[
\tfrac12(h')^2+\beta\log\cosh h=\tfrac12v^2.
\]
There is a unique positive turning amplitude \(a\) with \(v^2=2\beta\log\cosh a\). The time from the zero crossing to the positive turning point is \(Q(a)/\sqrt\beta\). The orbit reaches turning points at all odd multiples of this quarter time, alternating between \(+a\) and \(-a\). Therefore its endpoint derivative vanishes if and only if
\[
1=(2j+1)Q(a)/\sqrt\beta,\qquad j=0,1,2,\ldots.\tag{2}
\]
Its intermediate zero crossings occur at the even multiples, proving the exact nodal locations once (2) is satisfied.

**3. Strict quarter-period monotonicity and exhaustive branch count.** Substitute \(s=au\) to obtain
\[
Q(a)=\int_0^1\left[2\int_u^1\frac{\tanh(av)}a\,dv\right]^{-1/2}du.
\]
For every \(v>0\), \(a\mapsto\tanh(av)/a\) is strictly decreasing: with \(z=av\), the sign of its derivative is the sign of \(z\operatorname{sech}^2z-\tanh z<0\), because \(g(z)=\tanh z-z\operatorname{sech}^2z\) has \(g(0)=0\) and \(g'(z)=2z\operatorname{sech}^2z\tanh z>0\). Consequently \(Q\) is strictly increasing and continuous. The limit \(a\downarrow0\) in the integral is \(\pi/2\), since \(\tanh(av)/a\to v\); the limit \(a\uparrow\infty\) is infinite (indeed \(Q(a)\sim\sqrt{2a}\)). Hence equation (2) has exactly one \(a>0\) if and only if \(\sqrt\beta>(2j+1)\pi/2\). No other initial slopes or turning-point counts exist. Negative initial slopes produce precisely the spin-flipped profiles.

**4. Exact magnetization and endpoint laws.** Integrate \(h''=-\beta m\) over \([0,1]\). Since \(h'(1)=0\),
\[
\int_0^1m(x)\,dx=\frac{h'(0)}\beta=\sqrt{\frac{2\log\cosh a}{\beta}}.
\]
The Taylor expansion \(\tanh z=z-z^3/3+O(z^5)\), inserted in the rescaled quarter-period integral, gives
\[
Q(a)=\frac\pi2\left(1+\frac{a^2}{8}+O(a^4)\right).
\]
Combining it with (2) gives the stated square-root amplitude law. For large \(a\), \(\log\cosh a-\log\cosh(au)\sim a(1-u)\) for each \(0\le u<1\). Splitting the integral into a fixed interior and a small endpoint region, with the inequality \(\tanh t\ge1/2\) for \(t\ge1\) to control the square-root singularity, proves by dominated convergence that \(Q(a)/\sqrt{2a}\to1\). Equation (2) then yields the large-\(\beta\) amplitude and magnetization limits.

**5. The global thermodynamic states.** The integral operator \(K\) is the inverse of \(-d^2/dx^2\) with Dirichlet data at \(0\) and Neumann data at \(1\). Its eigenfunctions are \(\sin((j+1/2)\pi x)\) and its eigenvalues are \(1/\beta_j\); the largest is \(4/\pi^2\). Since \(s(t)-s(0)\ge t^2/2\), strictly for every \(t\ne0\),
\[
\mathcal F_\beta[m]-\mathcal F_\beta[0]\ge\tfrac12(1-4\beta/\pi^2)\|m\|_2^2,
\]
strictly for every nonzero \(m\) even when the coefficient vanishes. Thus zero is the unique minimizer for \(\beta\le\beta_0\).

For \(\beta>\beta_0\), the trial profile \(m=\varepsilon\sin(\pi x/2)\) has lower free energy than zero for sufficiently small nonzero \(\varepsilon\). A minimizer exists: the bounded convex domain \(|m|\le1\) is weakly compact in \(L^2\); the convex entropy integral is weakly lower semicontinuous; and compactness of \(K\) makes the interaction quadratic weakly continuous. At a minimizer, the logarithmically divergent endpoint slopes of \(s\) exclude saturation on sets of positive measure. Its Euler--Lagrange equation is \(s'(m)=\operatorname{arctanh}m=\beta Km\), so it is one of the stationary profiles already classified.

Because \(W(x,y)>0\) almost everywhere on \((0,1]^2\), replacing any genuinely sign-changing \(m\) by \(|m|\) preserves entropy but strictly increases \(\langle m,Km\rangle\), and so strictly lowers free energy. Therefore no sign-changing profile is a global minimum. The only nonzero one-sign stationary profiles are the pair \(\pm m_{0,\beta}\), hence they are exactly the global minimizers. This also separates global equilibrium phase coexistence from the additional sign-changing stationary branches.

## Verification
The accompanying standard-library script `check.py` evaluates the regularized quarter-period integral by Simpson quadrature and independently solves the nonlinear boundary ODE by fourth-order Runge--Kutta. It checks quarter-period monotonicity on a parameter grid, the critical and large-amplitude laws, the endpoint Neumann condition, all predicted nodes, the exact total-magnetization identity, and the original integral equation at sample points. Execution returned `PASS 147 numerical consistency checks`. These tests independently check the formulas at finite samples; the universal statements are established by the proof above, not by finite testing.

## Relationship to prior work
Alexandrov and Medvedev (2026, arXiv:2608.20410) derived the general Ising graphon fixed-point equation, gave the eigenvalue criterion for local bifurcations, and studied Erdős–Rényi, small-world, and separable power-law graphons. Searle and Tindall (2023 preprint, arXiv:2303.00731; published 2024) had already developed the graphon spin limit, solved separable examples, **and in Appendix C obtained the second-order spin-field boundary equation for the growing-uniform-attachment graphon** \(W(x,y)=1-\max\{x,y\}\). Under the coordinate reflection \(x\mapsto1-x\), that graphon is exactly \(W(x,y)=\min\{x,y\}\). Therefore the reduction of this graphon to a semilinear mixed boundary-value problem, and the spectral critical-value principle, are **explicitly prior work and not claimed here as new**. The new contribution is the all-temperature **global** enumeration and uniqueness of every nonlinear nodal branch, the amplitude-dependent quarter-period argument, fixed nodal locations, sharp magnetization laws, and the complete distinction between the entire stationary set and the actual global free-energy minimizers. Neither the cited Appendix C's boundary-equation reduction nor the general local spectral criterion alone establishes these nonlinear global conclusions.

## Limitations
The theorem applies to the continuum ferromagnetic zero-field fixed-point equation, with the displayed normalization, and not to arbitrary graphons or nonzero magnetic fields. It does not prove metastable dynamical lifetimes, finite-size rates of convergence, or stochastic stability of nodal stationary states. General semilinear shooting theory underlies the proof, and an unindexed earlier application to this exact graphon could affect priority. The reflected form of this graphon and its associated second-order boundary equation already appear in Appendix C of Searle and Tindall (2023); this reduction is not novel. An unindexed earlier global classification of that boundary equation would cover the new claim and remains an originality risk.

## References
- Artem Alexandrov and Georgi S. Medvedev, *Graphon Spin Systems as Exactly Solvable Models*, arXiv:2608.20410, first posted 2026-08-13; *Physical Review E* **114**, 044102 (2026). https://arxiv.org/abs/2608.20410
- Amy Searle and Joseph Tindall, *The Thermodynamic Limit of Spin Systems on Random Graphs*, arXiv:2303.00731, first posted 2023-02-27; *Physical Review Research* **6**, 013011 (2024). https://arxiv.org/abs/2303.00731
