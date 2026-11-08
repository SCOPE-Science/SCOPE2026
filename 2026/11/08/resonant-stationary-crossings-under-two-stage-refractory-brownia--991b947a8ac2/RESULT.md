# Resonant stationary crossings under two-stage refractory Brownian resetting

## Finding

Consider Brownian motion interrupted by complete Poisson resets, each followed by two consecutive exponential resting stages. Its mean-square displacement can cross its stationary level infinitely often even when the resetting-rate spectrum contains a strictly slower real mode. In fact, if the active-to-rest transition rate is \(r>0\) and each resting-stage completion rate is \(q>0\), then the mean-square displacement has infinitely many strict stationary-level crossings if and only if
\[
 r=q\quad\text{or}\quad 2q\le r<4q.
\]
For \(r/q\ne1\) tending to one, the finite number \(N(r/q)\) of strict crossings grows as
\[
N(x)=\frac{2\sqrt3}{\pi}\log\frac{1}{|x-1|}+O(1),\qquad x=r/q\to1,\quad x\ne1.
\]
The isolated infinite-crossing point \(r=q\) is caused by exact cancellation of a non-oscillating slow pole, not by a collision of eigenvalues. This distinguishes it from the open oscillatory-dominance interval \(2q<r<4q\).

## Assumptions and scope

Take \(D,r,q>0\). At time zero the particle starts at the origin in the active state \(A\). While in \(A\), it obeys \(dX_t=\sqrt{2D}\,dB_t\) and switches after an independent exponential time of rate \(r\) to a first refractory state \(R_1\), resetting \(X_t\) to zero. It stays fixed at zero for an independent exponential time of rate \(q\), advances to \(R_2\), waits a second independent exponential time of rate \(q\), and returns to \(A\) at zero. Every clock and Brownian increment is independent across cycles. The observation includes the resting phases, where \(X_t=0\). Write \(M(t)=\mathbb E[X_t^2]\) and \(M_\infty=\lim_{t\to\infty}M(t)\). A *strict crossing* is a zero of \(M(t)-M_\infty\) at which its sign reverses; the count \(N(x)\) counts such points for \(t>0\). No first-passage or hitting-time claim is made.

## Proof

**1. Exact moment resolvent.** Let \(p_A,p_1,p_2\) be the probabilities of the three internal states. The initial data are \((p_A,p_1,p_2)=(1,0,0)\), and
\[
\dot p_A=-rp_A+qp_2,\qquad
\dot p_1=rp_A-qp_1,\qquad
\dot p_2=qp_1-qp_2.
\]
Since a reset removes all positional variance and the refractory states have zero position, Itô's formula and the Markov generator give the closed equation
\[\dot M(t)=2Dp_A(t)-rM(t),\qquad M(0)=0.\]
Solving the three-state resolvent yields, for \(s>0\),
\[
\widehat{p_A}(s)=\frac{(s+q)^2}{s[(s+q)^2+r(s+2q)]},\qquad
\widehat M(s)=\frac{2D(s+q)^2}{s(s+r)[(s+q)^2+r(s+2q)]}.
\]
The chain is finite irreducible, so the long-time active fraction is \(q/(q+2r)\), and therefore
\[
M_\infty=\frac{2Dq}{r(q+2r)}>0.
\]
In particular \(M(0)-M_\infty<0\), so the difference is not identically zero.

**2. Modes and cancellation.** Set \(x=r/q\), \(u=qt\), \(V(u)=qM(u/q)/(2D)\), and \(V_\infty=1/[x(1+2x)]\). The nonstationary poles are \(-r\) and the roots of
\[
H(s)=s^2+(r+2q)s+q(q+2r),\qquad
\operatorname{disc}H=r(r-4q).
\]
The pole at \(-r\) has exact residue
\[
\mathop{\rm Res}_{s=-r}\widehat M(s)=-\frac{2D(q-r)^2}{rq^2}.
\]
For \(0<x<4\), set
\[
 a=\frac{x+2}{2},\quad \omega=\frac{\sqrt{x(4-x)}}2,\quad
 c=-\frac{(1-x)^2}{x},\quad b=-V_\infty-c,\quad
 d=\frac{1+xc+ab}{\omega}.
\]
Inverse Laplace transformation, with the initial value and derivative \(V(0)=0\), \(V'(0)=1\), gives the exact identity
\[
V(u)-V_\infty=c e^{-xu}+e^{-au}[b\cos(\omega u)+d\sin(\omega u)].\tag{1}
\]
At the isolated cancellation point \(x=1\), \(c=0\) and \((b,d)=(-1/3,1/\sqrt3)\). Hence
\[
V(u)-\frac13=e^{-3u/2}\left[-\frac13\cos\left(\frac{\sqrt3 u}{2}\right)+\frac1{\sqrt3}\sin\left(\frac{\sqrt3 u}{2}\right)\right],
\]
which changes sign infinitely often. For \(0<x<2\), \(x\ne1\), the negative term \(ce^{-xu}\) is slower than the oscillatory pair \(e^{-au}\) and consequently the difference is eventually strictly negative, permitting only finitely many zeros.

For \(2<x<4\), the oscillatory pair is slower than \(e^{-xu}\), and its nonzero amplitude guarantees infinitely many strict crossings. At \(x=2\), the decay rates coincide, but exact coefficients give
\[
V(u)-\frac1{10}=e^{-2u}\left[-\frac12+\frac25\cos u+\frac45\sin u\right].
\]
The sinusoidal amplitude \(2/\sqrt5\) exceeds the magnitude \(1/2\) of the offset, and there are infinitely many strict crossings. At \(x=4\), the quadratic has a repeated real root, giving a finite exponential polynomial with at most finitely many zeros. At \(x>4\), all nonstationary roots are real; the inverse transform is a nonzero sum of three real exponentials, which has finitely many zeros (real exponentials with distinct rates form a Chebyshev system). This proves the if-and-only-if statement, including all boundaries.

**3. Near-resonant zero-count law.** Fix \(x\ne1\) sufficiently near one, so \(0<x<2\), \(c<0\), and \(\delta=a-x=(2-x)/2>0\). Write \(b\cos(\omega u)+d\sin(\omega u)=A\cos(\omega u-\theta)\), where \(A=\sqrt{b^2+d^2}>0\). Multiplying (1) by \(e^{au}\) gives the zero equation
\[
A\cos(\omega u-\theta)=\eta e^{\delta u},\qquad
\eta=-c=\frac{(x-1)^2}{x}.
\]
The positive right side is strictly increasing. No solutions can occur after
\[
U_x=\frac1\delta\log\frac A\eta.
\]
Within each positive cosine lobe the left-minus-right difference is strictly concave, since its second derivative is \(-A\omega^2\cos(\omega u-\theta)-\eta\delta^2 e^{\delta u}<0\). Its endpoints are negative. For every lobe whose center is at least a sufficiently large *fixed* distance before \(U_x\), its center value is positive, and it therefore has exactly two simple zeros. No lobe entirely beyond \(U_x\) can contain a zero. Only a bounded number of lobes lie in a fixed-width transition region near \(U_x\), or touch the origin. Since lobe centers are separated by \(2\pi/\omega\),
\[
N(x)=\frac{\omega}{\pi}U_x+O(1).
\]
As \(x\to1\), \(\omega\to\sqrt3/2\), \(\delta\to1/2\), \(A\to2/3\), and \(\eta=(x-1)^2/x\); smooth dependence gives \(U_x=4\log(1/|x-1|)+O(1)\). The stated logarithmic law follows, with the bounded remainder uniform from either side near one.

## Verification

The accompanying standalone `checker.py` derives the transform independently from the three-stage resolvent using exact symbolic arithmetic; checks the stationary residue, discriminant and equal-rate/equal-decay coefficients; compares the closed-form moment with 48 independent high-accuracy integrations of the generator ODE; and carries out 10 finite near-resonance crossing-count consistency checks. The analytic arguments above, rather than the finite numerical checks, establish the infinite-crossing and logarithmic theorems. Reproduce with `python checker.py` using Python, NumPy, SciPy and SymPy.

## Relationship to prior work

Evans and Majumdar (2018) derive a renewal description of Brownian resetting with general refractory waiting times, which encompasses the present Erlang-2 waiting law and therefore already supplies the general mechanism for computing the Laplace-domain position distribution. García-Valladares, Gupta, Prados and Plata (2023) provide a full pathway formulation and exact relaxation results for *single-exponential* refractory periods. Olsen and Löwen (2024) derive exact general time-dependent moments for partial resets and arbitrary refractory durations, and document nonmonotonic moments for *deterministic* refractory waiting. The present claim is **not** novelty of the renewal resolvent, the existence of refractory states, or qualitative oscillations. Its narrower claim is the complete three-regime strict-crossing classification for *two-stage exponential* refractory periods and the unbounded logarithmic crossing count near an isolated exact spectral cancellation. No cited source was found to explicitly state this pair of results; their formulas can be specialized to the present setting, so implicit coverage and undiscovered equivalent presentations remain risks.

## Limitations

All resetting is complete and instantaneous and each of the two refractory phases has the *same* exponential completion rate. Initial conditions are fixed at the origin and active; the stationary-level crossing count may differ for other initial phase distributions or position observables. The claims concern the ensemble mean-square displacement, not individual trajectories or generic refractory distributions. The \(O(1)\) crossing-count remainder is bounded, not evaluated exactly. The work has only the stated self-review; independent validation and publication-priority verification have not been performed.

## References

1. M. R. Evans and S. N. Majumdar, *Effects of refractory period on stochastic resetting*, arXiv:1809.01551, originally public 2018-09-05, https://arxiv.org/abs/1809.01551.
2. G. García-Valladares, D. Gupta, A. Prados, and C. A. Plata, *Stochastic resetting with refractory periods: pathway formulation and exact results*, arXiv:2310.19913, originally public 2023-10-30, https://arxiv.org/abs/2310.19913.
3. K. S. Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039, originally public 2024-06-14, https://arxiv.org/abs/2406.10039.
