# Two-mode reset-count statistics and a slow-gate exponential law for a blinking Brownian target

## Finding

For a one-dimensional Brownian searcher undergoing Poisson resetting while a two-state absorbing target retains its state, the *number of resets before detection* has an exact rational probability-generating function of degree two. In contrast with the geometric reset-count law for a permanently active target, both conditional laws have two distinct, noncancelling modes. When the target switches very slowly, an initially inactive target yields a universal exponentially rescaled reset count.

With the notation established below, set
\[
\begin{aligned}
F_A(z)&=\frac{h(T-rz)+\eta qTk(1-z)}{L(z)},\\
F_I(z)&=\frac{h(T-rz)-qTk(1-z)}{L(z)},\\
L(z)&=hz(T-rz)+(1-z)\big[(T-rz)+\eta q(T-rz+rzk)\big].
\end{aligned}
\]
These formulas hold for every \(0\le z\le1\) and extend as rational functions. The coefficients of \(L(z)=c_0-c_1z+c_2z^2\) are
\[
\begin{aligned}
c_0&=T(1+\eta q),\\
c_1&=T(1+\eta q-h)+r(1+\eta q(1-k)),\\
c_2&=r(1+\eta q(1-k)-h).
\end{aligned}
\]
In particular, with \(p_{j,n}=\Pr(K=n\mid J_0=j)\),
\[
c_0p_{j,n}-c_1p_{j,n-1}+c_2p_{j,n-2}=0\qquad(n\ge2;\ j=A,I).
\]
Both distinct characteristic roots \(0<\mu_-<\mu_+<1\) contribute nontrivially for strictly positive parameters; the reset-count law is therefore not geometric. The first probabilities are
\[
\Pr(K=0\mid A)=\frac{h+\eta qk}{1+\eta q},\qquad
\Pr(K=0\mid I)=\frac{h-qk}{1+\eta q}.
\]
When \(\alpha=\eta\beta\) and \(\beta\downarrow0\) for fixed \(\eta,r,D,x_0>0\),
\[
\frac{\beta K}{r}\ \Big|\ J_0=I\ \Longrightarrow\ \operatorname{Exp}(1),
\]
whereas \(K\mid J_0=A\) converges to the geometric distribution with success probability \(h\). When \(\alpha+\beta\to\infty\) at a fixed positive ratio \(\alpha/\beta\), both conditional reset-count laws converge to that geometric distribution.

## Assumptions and scope

Fix diffusion constant \(D>0\), reset rate \(r>0\), initial/reset position \(x_0>0\), and gate-switching rates \(\alpha,\beta>0\). The particle follows Brownian motion on the whole line with generator \(D\partial_{xx}\), is returned to \(x_0\) at each independent rate-\(r\) Poisson reset, and is absorbed at the first time it visits the origin while an independent two-state gate is active. An inactive target is transparent. The gate follows the transition rates \(A\to I\) at \(\alpha\), \(I\to A\) at \(\beta\), and **is not reset with the particle**. The random variable \(K\) counts only particle resets strictly before absorption.

Write
\[
\lambda=\alpha+\beta,\quad T=r+\lambda,\quad
q=\sqrt{r/T},\quad
h=e^{-x_0\sqrt{r/D}},\quad
k=e^{-x_0\sqrt{T/D}},\quad
\eta=\alpha/\beta.
\]
Thus \(0<k<h<1\), \(0<q<1\), and \(\eta>0\). Conditional PGFs are \(F_j(z)=\mathbb E[z^K\mid X_0=x_0,J_0=j]\). The formulas are exact for this model, not for a target whose gate state is refreshed at each reset.

## Proof

**1. Boundary-value characterization.** At starting position \(x\), let \(f_j(x,z)=\mathbb E_{x,j}[z^K]\). Conditioning on the next infinitesimal jump and using the strong Markov property gives, away from the origin,
\[
\begin{aligned}
D\partial_{xx}f_A-(r+\alpha)f_A+\alpha f_I+rz f_A(x_0,z)&=0,\\
D\partial_{xx}f_I-(r+\beta)f_I+\beta f_A+rz f_I(x_0,z)&=0.
\end{aligned}
\]
Absorption imposes \(f_A(0,z)=1\). Reflection symmetry of the full-line process about the origin, conditional on gate state and for the fixed reset destination, gives the Neumann condition \(\partial_x f_I(0,z)=0\) in the folded-coordinate representation. Bounded solutions are unique for \(0\le z<1\), for instance by contraction at the next reset or absorption; continuity extends the formulas to \(z=1\), where almost-sure detection gives \(F_j(1)=1\).

**2. Diagonalization and exact solution.** Define \(S=(\beta f_A+\alpha f_I)/\lambda\) and \(d=f_I-f_A\). Then
\[
D S''-rS+rzS(x_0)=0,\qquad Dd''-Td+rz d(x_0)=0.
\]
On \(x\ge0\) the bounded general solutions are
\[
\begin{aligned}
S(x)&=zS_0+(1-z)S_0e^{-\sqrt{r/D}(x-x_0)},\\
d(x)&=\frac{rz}{T}d_0+\frac{T-rz}{T}d_0e^{-\sqrt{T/D}(x-x_0)},
\end{aligned}
\]
where \(S_0=S(x_0)\), \(d_0=d(x_0)\). From \(f_A(0)=1\) and \(f_I'(0)=0\), algebra gives
\[
S_0=\frac{h(T-rz)}{L(z)},\qquad
 d_0=-\frac{(1+\eta)qTk(1-z)}{L(z)}.
\]
Now \(F_A=S_0-\alpha d_0/\lambda\) and \(F_I=S_0+\beta d_0/\lambda\), yielding the two boxed generating functions. As a check, \(L(1)=h\lambda\) and both numerators equal \(h\lambda\).

**3. Two noncancelling modes.** Expanding the common denominator gives the coefficients stated in the finding. They obey \(c_0,c_1,c_2>0\), \(L(1)=h\lambda>0\), and \(c_1<2c_0\). Its discriminant is
\[
\Delta=T^2\left[\left(1+\eta q-h-q^2(1+\eta q(1-k))\right)^2+4\eta q^3hk\right]>0.
\]
Consequently the characteristic roots
\[
\mu_{\pm}=\frac{c_1\pm\sqrt\Delta}{2c_0}
\]
are positive, distinct, and both less than one (their product is positive; \(L(1)>0\) places both roots on the same side of one, while their arithmetic mean is less than one). Extracting coefficients of the rational PGFs proves the recurrence.

The numerator of \(F_A\) cannot share a factor with \(L\): after dividing \(L\) by \(T\) and writing \(r/T=q^2\), their resultant is, apart from an overall nonzero power of \(T\),
\[
\eta h kq(1-q^2)^2\big[h-1-\eta q(1-k)\big]\ne0.
\]
The corresponding inactive-state resultant has a nonzero factor proportional to
\[
R=[1-q^2-(h-qk)]+\eta q[1-q^2-q(h-qk)]>0.
\]
Indeed, \(h-qk\le1-q\) follows by differentiation with respect to \(x_0\), since \(\sqrt{r/D}=q\sqrt{T/D}\) and \(h\ge k\). Both terms defining \(R\) are therefore positive. This proves neither mode cancels for either gate state; it also excludes an unacknowledged geometric simplification.

**4. Singular gate limits.** For fixed \(\eta\) and \(\beta\downarrow0\), evaluate \(F_I\) at \(z=e^{-s\beta/r}\) for \(s\ge0\). With \(\lambda=(1+\eta)\beta\), \(q\to1\), \(k\to h\), both its numerator and denominator are first-order in \(\beta\), and their ratio tends to \((1+s)^{-1}\). The Laplace-continuity theorem gives \(\beta K/r\Rightarrow\operatorname{Exp}(1)\). At any fixed \(z\in[0,1)\), the active-state PGF tends to \(h/[1-(1-h)z]\), implying geometric weak convergence. The same geometric limit holds for both initial states as \(\lambda\to\infty\) with \(\eta\) fixed because \(q,k\to0\).

## Verification

A standalone Python/SciPy script, `verify.py`, evaluates the closed PGFs and independently solves a finite-difference approximation of the *coupled killed Markov generator* on a large spatial interval. It checks three parameter configurations and four PGF arguments each, independently verifies the discriminant and characteristic-root inequalities, and prints numerical slow/fast-gate convergence. This numerical test is corroboration, not a substitute for the analytic proof. The finite interval, spatial grid and asymptotic truncation give finite numerical error.

## Relationship to prior work

Mercado-Vásquez and Boyer (2021, arXiv:2107.02148) established the stochastically gated Brownian first-passage and its time moments for a reflecting closed gate on a half-line. Their original backward equations are the folded absolute-position counterpart of the present full-line model. Żbik et al. (2025, arXiv:2512.09739) independently formulate the transparent full-line target with particle-only resets and give Laplace first-passage transforms and mean times. Both papers establish the stochastic transport model and time-to-detection statistics. Neither inspected paper states the reset-count PGFs, their two-mode factorization, or the initial-inactive slow-gate exponential scaling. These are distinct observables; however, the count PGF can be computed from the previously known underlying Markov generator, and implicit broader coverage is a residual originality risk.

Bressloff (2026, arXiv:2601.01588) studies gated-boundary renewal constructions with desorption-induced, near-boundary restarts; its restart mechanism differs from independent bulk Poisson resets. This paper was assessed at abstract level, not as a full-text exclusion certificate. The discovery claim is limited to the explicit count laws and the singular scaling, not the backward-equation technique.

## Limitations

This is one-dimensional Brownian motion with a two-state Markov gate and Poisson **particle-only** resetting. A reset that also refreshes the gate, finite reactive target, drift, multiple targets, or non-Poisson resetting requires a different analysis. The two-mode conclusion requires all four positive rates and positive initial distance; the singular limits use specifically indicated parameter scaling. First-passage time transforms and mean results in the cited literature are prior work. Previously unlocated, potentially covering general Markov-renewal work remains a scientific originality risk.

## References

- G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, J. Phys. A 54 (2021), 444002, arXiv:2107.02148 (first posted 2021-07-05).
- B. Żbik, B. Dybiec, K. Capała, Z. Palmowski and I. M. Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739 (first posted 2025-12-10).
- P. C. Bressloff, *Renewal theory for Brownian motion with stochastically gated targets*, arXiv:2601.01588 (first posted 2026-01-04).
