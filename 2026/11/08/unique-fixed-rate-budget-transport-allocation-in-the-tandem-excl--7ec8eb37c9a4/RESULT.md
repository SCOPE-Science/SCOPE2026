# Unique fixed-rate-budget transport allocation in the tandem exclusion process

## Finding
Fix a bulk particle density \(0<\rho<1\) and a total kinetic-rate budget \(B>0\). In the thermodynamic stationary regime of the cooperative exclusion model with local transitions \(110\to101\) at rate \(\alpha>0\) and \(101\to011\) at rate \(\beta>0\), impose \(\alpha+\beta=B\). There exists **exactly one** positive ratio \(q_*(\rho)=\beta/\alpha\) maximizing the stationary particle current \(J_\infty(\rho;\alpha,\beta)\).

The unique maximizer is specified without optimization ambiguity by a real polynomial: set
\[
P_\rho(s)=(\rho-1)^3s^4-(\rho-1)(3\rho-1)(5\rho-3)s^3-\rho(5\rho^2-11\rho+4)s^2+\rho^2(5\rho-1)s+2\rho^3.
\]
Let \(s_*(\rho)\) be its unique zero in the physical interval \(s>0\) if \(\rho\ge1/2\), or \(0<s<\rho/(1-2\rho)\) if \(\rho<1/2\). Then
\[
q_*(\rho)=\frac{\rho-(1-2\rho)s_*(\rho)}{(1-\rho)s_*(\rho)^2},\quad
\alpha_* =\frac B{1+q_*},\quad \beta_*=\frac{Bq_*}{1+q_*}.
\]
In particular the optimum is never attained by assigning the entire kinetic budget to only one of the two transitions. Its extreme-density response is sharp:
\[
q_*(\rho)\sim\sqrt{\frac25}\,\rho^{-1/2},\quad
\frac{J_*(\rho)}B\sim2\rho^2\qquad(\rho\downarrow0),
\]
\[
q_*(\rho)\sim\frac{1-\rho}{4},\quad
\frac{J_*(\rho)}B\sim1-\rho\qquad(\rho\uparrow1).
\]
Thus the scarce-resource optimum changes from overwhelmingly favoring follower recovery at very low density to overwhelmingly favoring leader advancement near complete filling, but is uniquely interior at every fixed density strictly between zero and one.

## Assumptions and scope
The dynamics are the continuous-time tandem exclusion process on a periodic one-dimensional lattice, in the thermodynamic stationary sector with fixed density \(\rho\in(0,1)\). The rate budget \(B>0\) is an **externally imposed optimization constraint** on the two transition intensities, not a conserved particle pool. The proof optimizes the **stationary current per bond**, not the spectral gap, finite-size relaxation, or time-dependent transport. The stationary measure and transfer-matrix current law quoted below are the previously established results of Ngoc, Nhung and Thi (2026); only their constrained-rate optimization is claimed here.

## Proof
**Step 1: exact current parametrization.** For \(q=\beta/\alpha>0\), the established thermodynamic current law is
\[
J_\infty=\alpha\,\frac{q\rho s(s+2+qs)}{(1+s)(1+qs)^2},\qquad
q(1-\rho)s^2+(1-2\rho)s-\rho=0,
\]
with the unique positive solution \(s\). This law follows from the nearest-neighbor Gibbs stationary measure with bond transfer matrix \(\left(\begin{smallmatrix}1&z\\1&qz\end{smallmatrix}\right)\). The source's local pattern calculation gives \(J=\alpha\Pr(110)+\beta\Pr(101)\); no current formula is newly attributed to this result.

**Step 2: invert the density constraint and impose the budget.** Solving the quadratic for \(q\),
\[
q(s)=\frac{\rho-(1-2\rho)s}{(1-\rho)s^2}.
\]
For \(\rho<1/2\), the physical range is \(0<s<\rho/(1-2\rho)\); for \(\rho\ge1/2\), it is \(s>0\). On either range, \(q(s)>0\) and \(q'(s)<0\), and this parameter maps bijectively onto \((0,\infty)\). With \(\alpha=B/(1+q)\), direct substitution and cancellation produce
\[
\mathcal J_\rho(s):=\frac{J_\infty}B=
\frac{(1-\rho)s^2[\rho-(1-2\rho)s][\rho+(1-\rho)s]}{\rho(1+s)^2[\rho-(1-2\rho)s+(1-\rho)s^2]}.
\]
All denominator factors are positive on the physical range. Direct differentiation yields the exact sign identity
\[
\frac{d\mathcal J_\rho}{ds}=
\frac{(1-\rho)sP_\rho(s)}{\rho(1+s)^3[\rho-(1-2\rho)s+(1-\rho)s^2]^2}.
\]
Hence stationary points of the constrained current are precisely physical positive roots of \(P_\rho\).

**Step 3: uniqueness for \(\rho\ge1/2\).** The coefficients of \(P_\rho\), in descending powers, have signs \((-,-,+,+,+)\) for \(1/2\le\rho<3/5\) and \((-,+,+,+,+)\) for \(3/5<\rho<1\), with a zero cubic coefficient at \(\rho=3/5\). Indeed the quadratic coefficient is \(-\rho(5\rho^2-11\rho+4)>0\) throughout \(\rho\ge1/2\). Descartes' rule of signs therefore permits at most one positive zero. Since \(P_\rho(0)=2\rho^3>0\) and its leading coefficient is \((\rho-1)^3<0\), that zero exists, is unique, and changes the derivative from positive to negative.

**Step 4: uniqueness for \(0<\rho<1/2\).** Introduce the physical half-line coordinate \(t>0\) via
\[
s=\frac{\rho t}{(1-2\rho)(1+t)}.
\]
Multiplication by the positive quantity \((1-2\rho)^4(1+t)^4/\rho^3\) converts the critical polynomial into \(Q_\rho(t)\), whose coefficients in descending degrees are
\[
\begin{aligned}
[t^4]Q_\rho&=\rho(\rho-1)^2(3\rho-2)<0,\\
[t^3]Q_\rho&=-\rho^2(\rho-1)(2\rho-1)<0,\\
[t^2]Q_\rho&=(2\rho-1)^2(13\rho^2-16\rho+5)>0,\\
[t]Q_\rho&=(2\rho-1)^3(11\rho-7)>0,\\
[t^0]Q_\rho&=2(2\rho-1)^4>0.
\end{aligned}
\]
The quadratic in the third coefficient is strictly positive because its discriminant is \(-4\). Again there is exactly one sign change and opposite endpoint signs, so exactly one physical root exists. It is a strict global maximum because the derivative changes from positive to negative and no further stationary points occur. This proves existence, uniqueness and strict positivity of both optimized rates at **every** \(\rho\in(0,1)\), including \(\rho=1/2\).

**Step 5: sharp endpoint regimes.** As \(\rho\downarrow0\), the positive zero \(t_*\) of \(Q_\rho\) diverges and balancing its quartic and quadratic contributions, whose leading coefficients are \(-2\rho\) and \(5\), gives \(t_*\sim\sqrt{5/(2\rho)}\). The remaining terms are lower order under this scaling; Descartes uniqueness excludes any competing branch. Consequently \(q_*\sim\sqrt{2/5}\,\rho^{-1/2}\). Substitution into the exact current gives \(J_*/B\sim2\rho^2\).

As \(\rho\uparrow1\), the sole positive root \(s_*\) diverges. In the defining quartic the dominant terms are \(-(1-\rho)^3s^4+4(1-\rho)s^3\), implying \(s_*\sim4/(1-\rho)^2\). The two neglected lower powers have strictly smaller order at this scale, and uniqueness identifies this branch. It follows that \(q_*\sim(1-\rho)/4\) and \(J_*/B\sim1-\rho\). This completes the proof.

## Verification
The standalone `check.py` uses symbolic elimination to verify the rational current, derivative polynomial, transformed coefficients, and half-density cubic factorization. It then tests the asserted unique optimum against off-optimal rate ratios at fourteen representative densities, compares singular scaling coefficients against small- and large-density samples, and independently enumerates finite-ring canonical binary words at the \(q=1\) normalization point. Run `python check.py` with SymPy and SciPy installed. These finite and symbolic checks corroborate, but do not replace, the all-density sign proof above.

At \(\rho=1/2\), \(P_{1/2}(s)=-(s+1)(s^3-s-2)/8\). The positive root \(s\approx1.5213797068\) yields \(q_*\approx0.4320408003\) and \(J_*/B\approx0.1384765897\). At \(\rho=2/3\), \(q_*\approx0.1946252627\) and \(J_*/B\approx0.1782263550\).

## Relationship to prior work
Ngoc, Nhung and Thi derive the local transition model, Gibbs stationary measure and unconstrained stationary current \(J(\rho;\alpha,\beta)\), and establish strict current increase with \(q\) when **\(\alpha\) is fixed**. That monotonicity does not settle how to allocate a fixed sum \(\alpha+\beta\): increasing \(q\) then reduces \(\alpha\). This result supplies the unique interior solution and the two extreme-density allocation exponents under that distinct constraint. Optimizing **particle density** at fixed transition rates is also a different question from optimizing the **rate ratio** at fixed density.

Lakatos–Chou–Kolomeisky (2005) treat site-periodic hop rates in a different exclusion model; Haldar–Roy–Basu (2021) treat a **finite particle reservoir** with coupled entry and exit, not the two-stage tandem kinetic-rate budget. The classical descriptions are neither asserted to imply this theorem nor treated as exhaustive novelty evidence. Search comparisons are necessarily limited by indexing and available text, and a broader unpublished rate-allocation result cannot be excluded.

## Limitations
The result assumes the established infinite-volume Gibbs stationary current and may not describe regimes with frozen initial configurations outside the associated stationary sector, finite-ring current maxima, or time-dependent switching between allocations. The finite-rate sum is a modeling design constraint, not a microscopic conservation law. The numerical checks are finite. Originality is assessed only against inspected accessible sources and relevant indexed claims, not proved by absence of search hits; no independent audit is claimed.

## References
- N. P. N. Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1, first public 2026-06-01. https://arxiv.org/abs/2606.01568
- G. Lakatos, T. Chou and A. Kolomeisky, *Steady-state properties of a totally asymmetric exclusion process with periodic structure*, Physical Review E **71**, 011103 (2005). https://doi.org/10.1103/PhysRevE.71.011103
- A. Haldar, P. Roy and A. Basu, *Asymmetric exclusion processes with fixed resources: Reservoir crowding and steady states*, Physical Review E **104**, 034106 (2021). https://doi.org/10.1103/PhysRevE.104.034106
