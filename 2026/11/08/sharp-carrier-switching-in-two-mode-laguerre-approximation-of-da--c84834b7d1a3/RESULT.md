# Sharp carrier switching in two-mode Laguerre approximation of damped beats

## Finding
Consider an exponentially damped two-tone signal on the half-line and the family of two-dimensional modulated Laguerre subspaces with a *single* freely selected carrier. When the tone frequency is at least twice the damping exponent, the globally best carrier undergoes a sharp switch at a fixed, dimensionless frequency ratio.

For every \(a>0\) and \(\omega\ge 2a\), let
\[
f(x)=2e^{-ax}\cos(\omega x),\qquad x\ge0,
\]
and let \(\phi_0(x)=\sqrt{2a}e^{-ax}\), \(\phi_1(x)=\sqrt{2a}e^{-ax}(1-2ax)\). For every real carrier \(k\), let \(P_k\) be the orthogonal projector in \(L^2(0,\infty;\mathbb C)\) onto \(\operatorname{span}\{e^{ikx}\phi_0,e^{ikx}\phi_1\}\). Set \(s=2a\) and \(W=(\omega/s)^2\ge1\).

**Complete optimal-carrier classification:**

* For \(1\le W<3\), the maximizing carriers of \(\|P_k f\|_2^2\), equivalently the minimizing carriers of \(\|f-P_kf\|_2^2\), are precisely \(k=\pm s\sqrt{W-1}\). At \(W=1\), the two signs describe the same sole optimum \(k=0\).
* At \(W=3\), there are precisely four optimal carriers \(k=\pm s\sqrt2\) and \(k=\pm s\sqrt5\), all capturing squared energy \(4/(3s)\).
* For \(W>3\), there are precisely two optimal carriers \(k=\pm s\sqrt{t_*(W)}\), where \(t_*(W)\) is the unique zero in \((r_-(W),r_+(W))\) of
\[
Q_W(t)=t^3+(2-W)t^2+(1-W^2-12W)t+W^3+10W^2+W
\]
with
\[
r_\pm(W)=\frac{W^2+4W-1\pm2\sqrt{W(W-3)}}{W+1}.
\]
In particular, \(\lim_{W\downarrow3}t_*(W)=5\), while the optimizers from below satisfy \(\lim_{W\uparrow3}(W-1)=2\). This gives a genuine discontinuous global optimizer switch. As \(W\to\infty\), \(t_*(W)=W+2+\sqrt3+o(1)\).

The theorem concerns only the stated single-carrier, two-Laguerre-mode orthogonal approximation problem. The carrier need not equal either physical tone frequency.

## Assumptions and scope
The signal is the equal-amplitude, in-phase pair of damped complex exponentials, i.e. a real damped cosine. The half-line measure is Lebesgue measure. Scaling \(s=2a\) and orthonormal Laguerre functions are fixed as displayed; the optimization varies *only* the real modulation frequency \(k\). The theorem is for the resolved-frequency domain \(\omega\ge2a\), not for all smaller frequencies, nor for altered damping scales, unequal tone amplitudes, independently modulated modes, or more than two Laguerre orders.

## Proof
**1. Exact orthogonal projection.** The Laguerre identity \(\int_0^\infty e^{-u}L_j(u)L_m(u)\,du=\delta_{jm}\) proves that \(\phi_0,\phi_1\) are orthonormal and remain so after common modulation. For \(n=0,1\) and real \(\delta\), direct integration yields
\[
\int_0^\infty e^{-(s-i\delta)x}L_n(sx)\,dx
=\frac{(-i\delta)^n}{(s-i\delta)^{n+1}}.
\]
Therefore the two projection coefficients are known explicitly by adding the contributions with \(\delta=\omega-k\) and \(\delta=-\omega-k\). Setting \(t=(k/s)^2\ge0\), straightforward rational simplification gives
\[
s\|P_k f\|_2^2=J_W(t)=\frac{4N_W(t)}{P_W(t)^2},
\]
where
\[
\begin{aligned}
P_W(t)&=(1+W+t)^2-4Wt,\\
N_W(t)&=2t^3+(5-4W)t^2+(2W^2-6W+4)t+5W^2+2W+1.
\end{aligned}
\]
Here \(P_W(t)=(1+(\sqrt W-\sqrt t)^2)(1+(\sqrt W+\sqrt t)^2)>0\) for all \(W,t\ge0\). Consequently all inequalities below are valid on the complete continuous carrier domain. The signal norm is independent of the carrier, so maximizing \(J_W\) is exactly minimizing the orthogonal approximation error.

**2. Sharp baseline comparison and the transition.** For every \(W>0\), direct polynomial expansion gives the identities
\[
J_W(W-1)=\frac{W+1}{W},
\]
\[
J_W(t)-\frac{W+1}{W}
=-\frac{(t-W+1)^2H_W(t)}{WP_W(t)^2},
\]
where
\[
H_W(t)=(W+1)t^2-2(W^2+4W-1)t+W^3+7W^2+3W+1.
\]
The discriminant of \(H_W\) is exactly \(16W(W-3)\). For \(1\le W<3\), it is negative, so the quadratic is strictly positive. The only global maximizer \(t\ge0\) is \(t=W-1\); this is feasible because \(W\ge1\). At \(W=3\), \(H_3(t)=4(t-5)^2\), and precisely \(t=2,5\) give equality, with shared value \(4/3\). This already proves both pre-switch optimality and the exact coexistence threshold.

**3. The unique post-transition winner.** For \(W>3\), the positive-leading-coefficient quadratic \(H_W\) is negative precisely on \((r_-,r_+)\), where the roots are as in the Finding. Both roots exceed \(W\), in particular \(r_->W-1\). It follows from the preceding identity that \(J_W\) exceeds its baseline \((W+1)/W\) precisely inside this interval, whereas every point outside has gain at most the baseline. The derivative factors exactly as
\[
\frac{dJ_W}{dt}=-\frac{8(t-W+1)Q_W(t)}{P_W(t)^3}.
\]
At \(r_-\), the derivative of \(J_W\) is positive; at \(r_+\), it is negative. Therefore \(Q_W(r_-)<0<Q_W(r_+)\). Moreover \(Q_W''(t)=6t+4-2W>0\) for \(t>W\). Hence the sublevel set of \(Q_W\) in \([r_-,r_+]\) is an interval containing its left endpoint but not its right endpoint; there is exactly one zero \(t_*\) in the open interval, and the derivative changes from positive to negative there. This is the unique global maximizer of \(J_W\) on \(t\ge0\). Its two lifts to the real carrier variable are \(k=\pm s\sqrt{t_*}\).

**4. Boundary and high-frequency behavior.** The shrinking interval \([r_-(W),r_+(W)]\) tends to the singleton \(\{5\}\) as \(W\downarrow3\), so \(t_*(W)\to5\). Substitution of \(t=W+u\) gives the exact identity
\[
Q_W(W+u)=W(2u^2-8u+2)+u^3+2u^2+u.
\]
The two positive-\(t\) roots near the high-frequency region have \(u\to2\pm\sqrt3\); since \(t_*\) is the larger such root inside \((r_-,r_+)\), it obeys \(t_*(W)=W+2+\sqrt3+o(1)\). These arguments establish all claimed limits.

## Verification
The standalone `CHECK.py` verifies the exact projection rational form through independent numerical half-line quadrature, the exact polynomial baseline/difference/derivative/discriminant identities through symbolic algebra, and global optimizer candidates at representative normalized frequencies on both sides of and at the transition. Run `python CHECK.py` with Python 3, SymPy, and SciPy. The script prints `TWO_MODE_LAGUERRE_CARRIER_EXACT_AND_INTEGRAL_CHECKS_PASSED` on success. The proof above, rather than the finite numerical grid, establishes uniqueness and continuous-parameter optimality.

## Relationship to prior work
Wang, Zhao, and Zhao (2026, arXiv:2609.27910) introduce adaptive frequency detection and multi-carrier Laguerre tail approximations. Their Sections 3--6 discuss close frequencies, residual mismatches, error bounds, and a numerical parameter strategy, but do not give the exact best **single** common carrier for a two-frequency damped beat, nor a discontinuous switch between globally optimal carrier branches. Hu and Yu (2026, arXiv:2602.03083) establish general scaled Laguerre/Hermite approximation and projection-error analysis, but their scale-optimization statements do not imply this fixed-scale common-modulation optimizer classification. This proof gives an explicit simplest nontrivial carrier-selection instance with global sharpness.

## Limitations
The result is for ideal infinite-half-line \(L^2\) projection, not discrete or regularized least squares. Frequencies below \(\omega=2a\), unequal amplitudes, relative phases, more Laguerre modes, and freely optimized damping/scaling are not classified. The theorem does not assert performance improvements for an unconstrained multi-carrier representation. A previously published equivalent rational optimization under another terminology cannot be ruled out solely by the cited database and text comparisons.

## References
1. C. Wang, Z. Zhao, and T. Zhao, *A Localized Core-Tail Fourier-Laguerre Frame Method with Adaptive Frequency Detection for Unbounded-Domain Problems*, arXiv:2609.27910 (source page dated 2026-09-13), Sections 3--6. https://arxiv.org/abs/2609.27910
2. H. Hu and H. Yu, *Scaling Optimized Spectral Approximations on Unbounded Domains: The Generalized Hermite and Laguerre Methods*, arXiv:2602.03083v1 (2026-02-03), Sections 2, 4--6. https://arxiv.org/html/2602.03083v1
3. J. Shen, *Stable and Efficient Spectral Methods in Unbounded Domains Using Laguerre Functions*, SIAM Journal on Numerical Analysis 38 (2000), 1113--1133. (Background on Laguerre-function spectral approximation.)
