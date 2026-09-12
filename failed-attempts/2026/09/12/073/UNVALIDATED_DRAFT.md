# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of small-time local exact controllability for the circle dipole model — self-contained note

## 1. Setting

Let $S^1=\mathbb R/(2\pi\mathbb Z)$, $H=L^2(S^1,\mathbb C)$,
$H_0=-\partial_{\theta\theta}$ with domain $D(H_0)=H^2_{\rm per}(S^1)$,
self-adjoint, and $B$ multiplication by $\cos\theta$, bounded self-adjoint
with $\|B\|\le 1$, preserving every $H^k_{\rm per}$.
Control $u\in L^\infty((0,T),\mathbb R)\subset L^1$.
State equation (mild form)
\begin{equation}
\psi(t)=e^{-itH_0}\psi_0-i\int_0^t e^{-i(t-s)H_0}\,u(s)\,B\psi(s)\,ds,
\qquad \psi(0)=\psi_0.
\tag{1}
\end{equation}
For bounded $B$ and $u\in L^1$, (1) has a unique global solution
$\psi\in C([0,T];H)$ by contraction/Dyson series (bounded perturbation of a
unitary group; Kato/Pazy), norm-preserving ($\|\psi(t)\|=\|\psi_0\|$),
agreeing with classical/strong solutions for smooth data.
In particular the propagator $U(T;u)$ is unitary on $H$.
The constant $\phi_0=(2\pi)^{-1/2}$ satisfies $H_0\phi_0=0$,
$\|\phi_0\|_{L^2}=1$, and the reference orbit is stationary:
$\phi_0(T)=\phi_0$.

Define the reflection (parity) operator
\begin{equation}
(Rf)(\theta)=f(-\theta).
\end{equation}
$R$ is unitary on $H$, $R^2=I$, preserves $H^k_{\rm per}$ norms and the unit
sphere, and $R\phi_0=\phi_0$.

## 2. Lemma (parity commutation and preservation)

$R$ commutes with $H_0$ (on its domain), with $e^{-itH_0}$ for all $t$,
and with $B$. Consequently, for every $u$ and every even initial datum
$R\psi_0=\psi_0$, the unique mild solution of (1) satisfies
$R\psi(t)=\psi(t)$ for all $t$.

*Proof.* $R$ preserves $H^2_{\rm per}$ and
$R(-\partial_{\theta\theta}f)=-\partial_{\theta\theta}(Rf)$;
in Fourier basis $e_k=(2\pi)^{-1/2}e^{ik\theta}$,
$Re_k=e_{-k}$ while $H_0e_k=k^2e_k$ and
$e^{-itH_0}e_k=e^{-itk^2}e_k$ with $k^2$ symmetric under $k\mapsto-k$.
$B$ is multiplication by the even function $\cos\theta$:
$R(Bf)(\theta)=\cos(-\theta)f(-\theta)=\cos\theta(Rf)(\theta)=B(Rf)$.
Apply $R$ to (1): using commutation,
$R\psi(t)=e^{-itH_0}R\psi_0-i\int_0^t e^{-i(t-s)H_0}u(s)BR\psi(s)ds$,
i.e. $\tilde\psi:=R\psi$ solves the same equation with data $R\psi_0$.
If $R\psi_0=\psi_0$, uniqueness gives $\tilde\psi=\psi$. ∎

Concretely, in Fourier coefficients $c_k$, $B$ acts as
$(Bc)_j=(c_{j-1}+c_{j+1})/2$ and $R$ as $(Rc)_k=c_{-k}$; both visibly commute,
as does the diagonal free flow. The script
`output/artifacts/check_norms.py` verifies these commutators are exactly zero
on a truncated basis.

## 3. Even/odd orthogonal decomposition

$H=E\oplus O$ orthogonally, where $E=\{f:Rf=f\}$, $O=\{f:Rf=-f\}$.
Indeed if $f\in E$, $g\in O$,
$\langle f,g\rangle=\int_0^{2\pi}\overline{f(\theta)}g(\theta)d\theta
=\int_0^{2\pi}\overline{f(-\theta)}g(-\theta)d\theta=-\langle f,g\rangle$
by $\theta\mapsto-\theta$, so $\langle f,g\rangle=0$.
Every $f$ splits as $f_e=(f+Rf)/2\in E$, $f_o=(f-Rf)/2\in O$,
and for any $g\in E$,
$\|f-g\|_{L^2}^2=\|f_e-g\|^2+\|f_o\|^2\ge\|f_o\|^2$.
Hence $\mathrm{dist}_{L^2}(f,E)=\|f_o\|_{L^2}$.

By the Lemma, from $\psi(0)=\phi_0\in E$, every reachable state satisfies
$\psi(T)=U(T;u)\phi_0\in E$ for every $T>0$ and every $u\in L^\infty$.

## 4. Counterexample family inside every $H^3$-ball

Let $\eta(\theta)=\pi^{-1/2}\sin\theta$, smooth, odd ($R\eta=-\eta$),
$\|\eta\|_{L^2}=1$, $\langle\phi_0,\eta\rangle=0$,
$\|\eta\|_{H^3}=2^{3/2}=2\sqrt2$ (Fourier modes $k=\pm1$ only, weight
$(1+k^2)^3=8$). For $\varepsilon>0$ set
\begin{equation}
\psi_{f,\varepsilon}=\frac{\phi_0+\varepsilon\eta}{\sqrt{1+\varepsilon^2}}.
\end{equation}
Then $\psi_{f,\varepsilon}\in H^3(S^1)\cap S$ (unit sphere), and with
$N=\sqrt{1+\varepsilon^2}$,
\begin{equation}
\|\psi_{f,\varepsilon}-\phi_0\|_{H^3}
\le \frac{N-1}{N}\|\phi_0\|_{H^3}+\frac{\varepsilon}{N}\|\eta\|_{H^3}
\le \frac{\varepsilon^2}{2N}+\frac{2\sqrt2\,\varepsilon}{N}\le 4\varepsilon
\quad(\varepsilon\le1),
\end{equation}
since $\|\phi_0\|_{H^3}=1$ and $N-1=\varepsilon^2/(N+1)$.
So $\psi_{f,\varepsilon}\to\phi_0$ in $H^3$ as $\varepsilon\to0$:
every $H^3$-ball of radius $\delta>0$ around $\phi_0$ contains such states
(e.g. $\varepsilon<\min(1,\delta/4)$).
But the odd part of $\psi_{f,\varepsilon}$ is $(\varepsilon/N)\eta$, so
\begin{equation}
\mathrm{dist}_{L^2}(\psi_{f,\varepsilon},E)=\frac{\varepsilon}{\sqrt{1+\varepsilon^2}}>0,
\end{equation}
and in particular $\psi_{f,\varepsilon}\notin E$.
Since all reachable states lie in $E$, $\psi_{f,\varepsilon}$ is
unreachable from $\phi_0$ by any $L^\infty$ control at any time $T>0$.

## 5. Theorem (target is false)

There do not exist constants $T^*>0$, $C>0$, $q\ge0$, $\delta>0$ as in the
target claim. In fact exact reachability from $\phi_0$ fails at every $T>0$:
for every $T$ and every $\delta>0$ there is
$\psi_f\in H^3\cap S$ with $\|\psi_f-\phi_0(T)\|_{H^3}<\delta$ unreachable by
any $u\in L^\infty(0,T)$. The control-cost bound $\|u\|_\infty\le CT^{-q}$
plays no role; the obstruction is a conserved parity valid for all bounded
(indeed all $L^1$) controls and all times, stronger than a small-time
quadratic/cubic drift. A fortiori small-time local exact controllability
around the ground-state orbit fails, and so does $L^2$-approximate
controllability toward non-even targets.

*Remark.* This says nothing about controllability within the even subspace;
that restricted question is left open and would require the degenerate
Fourier/Lie-bracket analysis of the original program.
