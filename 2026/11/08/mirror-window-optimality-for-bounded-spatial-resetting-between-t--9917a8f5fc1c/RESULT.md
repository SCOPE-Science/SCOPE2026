# Mirror-window optimality for bounded spatial resetting between two absorbing endpoints

## Finding
For a driftless Brownian searcher on an interval with two absorbing endpoints, suppose the local rate of Poisson resetting to a fixed interior site is controlled between zero and a fixed ceiling. The globally optimal rate is maximal precisely between the resetting site and its mirror image about the interval midpoint, and zero elsewhere. The switching positions do not depend on diffusivity or on the rate ceiling. This policy minimizes the mean time to hit **either** endpoint simultaneously for every starting position and even against nonstationary adapted rate controls.

Specifically, let \(D,L,R>0\), \(a\in(0,L)\), and \(b=\min(a,L-a)\). The optimal spatial rate, away from the immaterial switching positions, is
\[
u_*(x)=R\mathbf 1_{(b,L-b)}(x).
\]
For a particle initially at the reset site, the exact optimal mean exit time is
\[
\inf_u \mathbb E_a\tau_u
 =\frac{b^2}{2D}+\frac{b}{\sqrt{DR}}
 \tanh\!\left(\sqrt{\frac{R}{D}}\left(\frac L2-b\right)\right).
\]
When \(a=L/2\), resetting is never strictly beneficial; the optimum is attained by the zero rate and equals \(L^2/(8D)\). For \(a\ne L/2\), the controlled value at the reset site is strictly smaller than its no-reset value \(a(L-a)/(2D)\), decreases strictly with \(R\), and tends to \(b^2/(2D)\) as \(R\to\infty\).

## Assumptions and scope
The uncontrolled particle is one-dimensional Brownian motion with generator \(D\partial_{xx}\) on \((0,L)\). Absorption occurs immediately on first hitting either \(0\) or \(L\). Until absorption, a controller may choose a predictable, history-dependent stochastic resetting intensity \(u_t\in[0,R]\); each reset jumps the position instantaneously to the fixed site \(a\), without a delay or a charge. The controller observes the present position; spatial rates are included, but the optimization is not restricted to spatial rates. The objective is the undiscounted mean of the first absorption time \(\tau_u\), with \(\inf_u\mathbb E_x\tau_u\) taken separately from every \(x\in[0,L]\). All constants are finite and positive, with \(a\) strictly interior. The two endpoints are interchangeable target outcomes, not two targets that must *both* be visited.

By reflection it suffices to prove the formulas for \(0<a\le L/2\). For \(0<a<L/2\), set
\[
\kappa=\sqrt{R/D},\qquad \delta=L/2-a,\qquad
s=\frac{\tanh(\kappa\delta)}{\sqrt{DR}},\qquad
A=\frac{a^2}{2D}+as.
\]
Define a function \(V:[0,L]\to\mathbb R\) by
\[
V(x)=\begin{cases}
\dfrac{x(2a-x)}{2D}+sx,&0\le x\le a,\\[4pt]
A+\dfrac1R\left(1-\dfrac{\cosh(\kappa(x-L/2))}{\cosh(\kappa\delta)}\right),&a\le x\le L-a,\\[4pt]
V(L-x),&L-a\le x\le L.
\end{cases}
\]
For \(a=L/2\) take \(V(x)=x(L-x)/(2D)\). For \(a>L/2\), use \(V(x;a)=V(L-x;L-a)\) in the displayed formula. These specifications completely define the optimum for every initial state.

## Proof
**Step 1: regularity and boundary values.** For \(0<a<L/2\), the left branch gives \(V(0)=0\), \(V(a)=A\), and \(V'(a-)=s\). The middle branch also gives \(V(a)=A\) and
\[
V'(a+)=\frac\kappa R\tanh(\kappa\delta)=s.
\]
Both one-sided second derivatives equal \(-1/D\) at \(x=a\), because \(\kappa^2=R/D\). Reflection gives the same matching at \(x=L-a\). Thus \(V\in C^2([0,L])\) with \(V(0)=V(L)=0\). In the open central region, \(V(x)>V(a)=A\), since \(\cosh(\kappa(x-L/2))<\cosh(\kappa\delta)\); on both exterior regions, \(V(x)<A\), since the left parabola has strictly positive derivative \((a-x)/D+s\) for \(0\le x<a\), and the right branch is its reflection.

**Step 2: exact Hamilton–Jacobi–Bellman identity.** On the two exterior regions \(DV''=-1\). On the central region direct differentiation gives
\[
DV''+R\bigl(V(a)-V(x)\bigr)=-1.
\]
Consequently, pointwise (including switching points by continuity),
\[
DV''(x)+\min_{0\le u\le R}u\bigl(V(a)-V(x)\bigr)=-1.
\]
The minimizing feedback is \(u=R\) exactly where \(V(x)>V(a)\), namely \((a,L-a)\), and \(u=0\) elsewhere. The rate at the interfaces may be arbitrary. Reflection handles \(a>L/2\). At \(a=L/2\), the no-reset parabola satisfies the same identity because it is maximized at \(a\), so \(V(a)-V(x)\ge0\) for all \(x\).

**Step 3: verification against every admissible controller.** For any predictable control \(u_t\in[0,R]\), the controlled extended generator acting on \(V\) is \(D V''(x)+u_t(V(a)-V(x))\), which is at least \(-1\) by Step 2. The stopped jump-Itô/Dynkin formula thus gives
\[
\mathbb E_x V(X_{t\wedge\tau_u})\ge V(x)-\mathbb E_x(t\wedge\tau_u).
\]
This can be passed to the limit \(t\to\infty\). Indeed, realize any admissible intensity by thinning independent rate-\(R\) proposals. Over each interval of a fixed length \(t_0>0\), the event of no proposals has probability \(e^{-Rt_0}>0\); conditional on that event, from every interior starting point the Brownian motion has a uniformly positive probability of hitting a boundary within \(t_0\) (e.g. by a signed displacement of at least \(L\)). The strong Markov property therefore yields a geometric bound on survival in successive \(t_0\) blocks and a uniform finite expected exit time. As \(V\) is bounded and \(V(X_{\tau_u})=0\), dominated convergence applies to the stopped value. Hence \(\mathbb E_x\tau_u\ge V(x)\). For the feedback in Step 2, its generator applied to \(V\) equals \(-1\), so equality holds. This proves the global value and policy for all initial positions and history-dependent bounded intensities.

**Step 4: benefit, monotonicity and limiting regimes.** At the reset position the formula simplifies to \(V(a)=a^2/(2D)+as\). Without resetting, solving \(DT''=-1\) with Dirichlet boundaries yields \(T_0(a)=a(L-a)/(2D)\). Writing \(z=\sqrt{R/D}(L/2-a)>0\) gives
\[
T_0(a)-V(a)=\frac{a(L/2-a)}D\left(1-\frac{\tanh z}{z}\right)>0.
\]
The ratio \(\tanh z/z\) strictly decreases on \(z>0\), as its derivative has sign of \(z\operatorname{sech}^2z-\tanh z<0\), whose negative derivative is strictly positive. Thus \(V(a)\) strictly decreases with \(R\). The limits \(z\downarrow0\) and \(z\to\infty\) give respectively the no-reset mean and \(a^2/(2D)\). Reflection substitutes \(b\) for \(a\). If \(a=L/2\), the optimal value is the no-reset parabola. This proves all statements.

## Verification
The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`; it independently solves discrete continuous-time random-walk control problems by policy iteration, evaluating each policy via a tridiagonal system and a rank-one reset correction. It checks 60 lattice problems (three mesh sizes, five reset sites, four rate ceilings), comparing all optimal reset regions and 11,260 lattice values with the continuum formula; it also checks smooth fit and local HJB identities across additional parameters. Numerical checks are consistency evidence only. The infinite-dimensional, all-controls conclusion follows from the analytical argument above.

## Relationship to prior work
Evans and Majumdar (2011) introduced position-dependent resetting, a nonresetting window around the starting point, and a one-sided optimal immediate-reset rule when the target position is known (their Section 3.2). The present two-absorbing-endpoint problem has different boundary data and a distinct *central resetting* window whose endpoints are fixed at the reset site and its reflection, even under finite rate ceilings. Their one-sided rule and nonresetting-window formulas do not imply the two-exit solution.

De Bruyne and Mori (2021 preprint; 2023 journal) established a general resetting-control Bellman paradigm. Their explicit finite-interval Appendix B concerns discounted rewards and boundary reinjection rather than absorption upon first exit. Their discussion identifies first-passage payoffs as a further problem; the HJB principle is not claimed as new here. Our contribution is an explicit solved globally optimal two-exit control and value for all ceiling strengths.

Aspman, Mastropietro, and Mareček (first publicly available September 15, 2025; revised 2026) investigated spatially dependent reset rates in one-target potential landscapes, with piecewise-constant rates tied to a potential gradient. Their full open HTML examines one target, drift potentials, and preset spatial cutoffs rather than the unconstrained spatial-policy optimization with two absorbing endpoints.

Pal et al. (2025) analyzed constant-rate resetting and conditional/unconditional passage times between two absorbing endpoints. Their exact constant-rate formula is for a different, noncontrolled policy; it does not optimize over measurable spatially variable rates.

## Limitations
The result assumes driftless one-dimensional diffusion, exact position observation, zero-cost instantaneous resetting, a fixed reset destination, two fully absorbing endpoints, and a uniform finite intensity ceiling. It does not settle optimal reset-site choice, target-specific splitting objectives, costs, imperfect sensing, partial absorption, or multi-dimensional geometry. Existing general HJB and spatial-resetting equations are prior results, and separate earlier treatments of the exact same special boundary-value problem could affect publication priority. The finding has self-review only, not independent validation.

## References
1. J. Aspman, D. Mastropietro, J. Mareček, *Stochastic restarting with multiple restart conditions* (first public arXiv:2509.11809v1, 2025-09-15); revised as *First passage time in space-dependent stochastic resetting*, Phys. Rev. E 114, 024110 (2026). https://arxiv.org/abs/2509.11809 ; https://doi.org/10.1103/w2yj-91m8
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), J. Phys. A 44, 435001 (2011). https://arxiv.org/abs/1107.4225 ; https://doi.org/10.1088/1751-8113/44/43/435001
3. B. De Bruyne and F. Mori, *Resetting in Stochastic Optimal Control*, arXiv:2112.11416 (2021), Phys. Rev. Research 5, 013122 (2023). https://arxiv.org/abs/2112.11416 ; https://doi.org/10.1103/PhysRevResearch.5.013122
4. S. Pal, L. Dagdug, D. Ghosh, D. Boyer, A. Pal, *Universal criterion for selective outcomes under stochastic resetting*, arXiv:2502.09127 (2025), Phys. Rev. E 112, 034116 (2025). https://arxiv.org/abs/2502.09127
