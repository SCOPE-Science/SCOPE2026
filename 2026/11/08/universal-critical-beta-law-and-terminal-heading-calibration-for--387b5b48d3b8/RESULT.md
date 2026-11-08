# Universal critical beta law and terminal-heading calibration for ageing persistent walks

## Finding
Consider a one-dimensional persistent walk whose independent velocity-reversal probabilities satisfy \(k p_k\to c\in(0,\infty)\). Although the particle makes infinitely many reversals, its displacement remains of ballistic order, and the *entire* normalized displacement and terminal-velocity pair converges jointly:
\[
\left(\frac{X_n}{n},V_n\right)\ \Rightarrow\ (Y,S),\qquad
\Pr\{Y\in dy,S=s\}=\frac{1+sy}{2}\,\frac{\Gamma(c+\frac12)}{\sqrt{\pi}\Gamma(c)}(1-y^2)^{c-1}\,dy,
\quad -1<y<1,\quad s\in\{-1,1\}.
\]
Equivalently, \((1+Y)/2\) is \(\operatorname{Beta}(c,c)\), while the terminal heading has the exact limiting calibration \(\mathbb E[S\mid Y=y]=y\). In particular,
\[
\mathbb E[Y^2]=\frac1{2c+1},\qquad
\mathbb E[Y^4]=\frac3{(2c+1)(2c+3)},\qquad
\lim_{n\to\infty}\left(1-\frac{\mathbb E[X_n^4]}{3(\mathbb E[X_n^2])^2}\right)=\frac2{2c+3}.
\]
Thus the critical Binder cumulant is exactly determined, independently of lower-order changes to the reversal schedule. The limit undergoes an explicit **critical-amplitude shape transition**: its density is endpoint-divergent and U-shaped for \(0<c<1\), exactly uniform for \(c=1\), and centered/unimodal with vanishing endpoint density for \(c>1\).

For the admissible exact schedule \(p_k=c/(k+a)\), with \(c>0\) and \(a\ge c\), the finite-time probability of an entirely one-directional trajectory, including both possible headings, is
\[
\Pr\{|X_n|=n\}=\prod_{k=2}^n\left(1-\frac{c}{k+a}\right)
=\frac{\Gamma(a+2)}{\Gamma(a+2-c)}\,
\frac{\Gamma(n+a+1-c)}{\Gamma(n+a+1)}
\sim \frac{\Gamma(a+2)}{\Gamma(a+2-c)}n^{-c}.
\]
Consequently the finite-time ballistic endpoint atoms disappear at a known power, even as the limiting bulk density may have integrable endpoint singularities for \(0<c<1\).

## Assumptions and scope
Fix \(c>0\). Let \(V_0\) be a fair random sign, and let \(B_k\), for integers \(k\ge1\), be independent Bernoulli variables independent of \(V_0\) with \(\Pr(B_k=1)=p_k\in[0,1]\). Assume \(k p_k\to c\). Set \(V_k=(-1)^{B_k}V_{k-1}\) and \(X_n=\sum_{k=1}^n V_k\) for each integer \(n\ge1\). All weak convergence is of Borel probability measures on \([-1,1]\times\{-1,1\}\); convergence of the displayed even moments follows from boundedness. The exact endpoint-atom formula is only asserted when \(p_k=c/(k+a)\), \(a\ge c\), not for arbitrary asymptotically harmonic schedules.

## Proof
**1. A universal logarithmic-time Poisson limit.** For any fixed \(\varepsilon\in(0,1)\), the independent point measure \(\sum_{k=1}^n B_k\delta_{k/n}\) on \([\varepsilon,1]\) converges to a Poisson point process with intensity \(c\,du/u\). Indeed, uniformly in \(k\ge\varepsilon n\), \(p_k=(c+o(1))/k\). For every continuous nonnegative test function supported in this interval, the logarithm of its Laplace functional is the sum of \(\log[1-p_k(1-e^{-f(k/n)})]\). The linear terms converge to \(-c\int_\varepsilon^1(1-e^{-f(u)})du/u\) by a Riemann sum, while the total absolute quadratic remainder is bounded by a constant times \(\sum_{k\ge\varepsilon n}p_k^2=O(n^{-1})\). This proves the point-process convergence and joint convergence of the finitely many sign changes in any compact subinterval avoiding the origin.

**2. Joint convergence, without relying on a central-limit approximation.** Because \(V_0\) is a fair sign, conditional on *all* flip flags the terminal sign \(S_n:=V_n\) is fair. Hence it is independent of those flags. For \(k<n\), \(V_k=S_n(-1)^{\sum_{j=k+1}^n B_j}\). The point-process limit and continuous mapping imply joint convergence of \(S_n\) and the truncated Riemann sum \(n^{-1}\sum_{k=\lceil\varepsilon n\rceil}^n V_k\) to \(S\int_\varepsilon^1(-1)^{N((u,1])}\,du\), where \(S\) is an independent fair sign and \(N\) is the limiting Poisson measure. Both the discarded discrete part and its limiting integral have absolute value at most \(\varepsilon+1/n\). Letting \(\varepsilon\downarrow0\) yields
\[
(Y,S)\ \overset d=\ \left(S\int_0^\infty e^{-t}(-1)^{N_t}\,dt,S\right),
\]
where \(N_t\) is a rate-\(c\) Poisson counting process (the change of variable \(t=-\log u\)). This also proves universality for every sequence with \(k p_k\to c\); early exceptional flips contribute no limiting mass.

**3. Identification with a confined telegraph stationary law.** Take a two-sided stationary symmetric telegraph signal \(H_t\in\{-1,1\}\) flipping at rate \(c\) and define the stable linear filter \(Z_t=\int_{-\infty}^t e^{-(t-r)}H_r\,dr\). Then \(\dot Z_t=H_t-Z_t\), \(|Z_t|\le1\). Reversibility of the symmetric telegraph process gives \((Z_0,H_0)\overset d=(Y,S)\). This stationary law is unique: two filters driven by the same signal differ by an exponentially decaying factor, while copies of the finite-state signal can be coupled in finite time. The signal switches infinitely often in both time directions almost surely, so \(|Z_0|<1\) almost surely. Its stationary densities \(p_s(y)\) obey (in the distributional sense on the interior)
\[
0=-\frac{d}{dy}[(s-y)p_s(y)]-c p_s(y)+c p_{-s}(y).
\]
The total stationary probability flux is constant and must vanish at the ends, so \((1-y)p_+(y)=(1+y)p_-(y)\). Writing \(\rho=p_++p_-\) gives \(p_s(y)=(1+sy)\rho(y)/2\), and the plus equation becomes \(\frac{d}{dy}[(1-y^2)\rho(y)]=-2cy\rho(y)\). Its integrable normalized solution is
\[
\rho(y)=\frac{\Gamma(c+1/2)}{\sqrt\pi\Gamma(c)}(1-y^2)^{c-1}\mathbf1_{(-1,1)}(y).
\]
It is indeed invariant: substituting these functions into both stationary transport equations gives zero and the boundary flux vanishes as \((1-y^2)^c\to0\). Uniqueness of the invariant filter proves this is the limiting law, including its sign-dependence, with no endpoint masses.

**4. Moments and endpoint atoms.** Substitution \(t=(1+y)/2\) yields \(t\sim\operatorname{Beta}(c,c)\). Beta integration gives the stated second and fourth moments; bounded weak convergence transfers them to \(X_n/n\), and the fourth-to-second-moment ratio is legitimate because \(\mathbb E[Y^2]>0\). The joint density directly gives \(\Pr(S=s\mid Y=y)=(1+sy)/2\) and \(\mathbb E[S\mid Y=y]=y\). The event \(|X_n|=n\) occurs if and only if \(B_2=\cdots=B_n=0\), regardless of \(B_1\). Multiplication of these independent probabilities gives the exact product, the gamma-function identity, and the asymptotic from \(\Gamma(n+u)/\Gamma(n+v)\sim n^{u-v}\). No finite simulation is used as an infinite-time proof.

## Verification
The accompanying standard-library `check.py` tests exact finite-step joint laws against two independent moment constructions for four rational choices of \((c,a)\), including the exact endpoint-atom probability at each tested horizon. It additionally checks large finite-time moments and the Binder ratio against the analytic limits. It reports **952 deterministic assertions passed**. These finite checks validate implementation and normalization, while the proof of universal weak convergence and its limiting density is the analytical argument above.

## Relationship to prior work
Pradhan, Roy, and Ray (2026) established the transition for time-dependent reversal probabilities, its critical second-moment prefactor \(1/(2c+1)\), and numerical critical displacement/Binder behavior. Those contributions are not claimed here. Dhar et al. (2018) established the stationary beta-type density for a *continuously confined* one-dimensional run-and-tumble particle; Guéneau, Majumdar, and Schehr (2026) further developed trapped run-and-tumble stationary and Dirichlet representations. The stationary beta formula itself is therefore **prior mathematics**. The finding here is the distributional ageing-walk-to-confined-telegraph correspondence for every \(k p_k\to c\), its *joint* displacement/terminal-sign critical limit, the exact critical Binder value, and the separately quantified, finite-step endpoint-atom decay. The correspondence is a time-change/Poisson-limit argument, not an assertion that the two microscopic dynamics are identical.

## Limitations
This is a one-dimensional two-heading independent-flip result with an initially fair orientation. The statement makes no multidimensional universality assertion, no diffusion-scale rate of convergence in the bulk, and no finite-size approximation bound for arbitrary \(p_k\). The special gamma-product endpoint formula requires the rational schedule exactly. Stationary trapped-telegraph laws are known, so the originality is in the ageing-walk scaling correspondence and resulting critical observables, not in discovering a new beta stationary distribution. Priority against broader generalized ageing-telegraph limit theorems requires independent literature assessment.

## References
- A. Pradhan, R. Roy, and P. Ray, *Diffusive-to-Ballistic transition in a Persistent Random Walk* (first posted 2026-05-19), arXiv:2605.20116, https://arxiv.org/abs/2605.20116. See the original full-text discussion of the \(\alpha=1\) case, displacement variance, and numerical Binder cumulant.
- A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, and G. Schehr, *Run-and-tumble particle in one-dimensional confining potential: Steady state, relaxation and first passage properties* (2018), arXiv:1811.03808, https://arxiv.org/abs/1811.03808. See the harmonic-trap stationary density and coupled transport equations.
- A. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential* (2026), arXiv:2602.08436, https://arxiv.org/abs/2602.08436. See the generalized one-dimensional stationary and stick-breaking formulations.
