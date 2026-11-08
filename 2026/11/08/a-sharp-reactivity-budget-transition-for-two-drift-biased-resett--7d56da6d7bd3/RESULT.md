# A sharp reactivity-budget transition for two drift-biased resetting traps

## Finding

Consider one-dimensional Brownian search with positive drift, exponentially timed resetting to its launch point, and two imperfect point traps at equal distances upstream and downstream. With a fixed total local killing strength, the strategy that minimizes the mean absorption time undergoes a **unique, explicit allocation transition**. At sufficiently low total strength, put *all* reactivity at the downstream target; above one computable threshold, allocate positive strengths to both targets, with the downstream target remaining strictly favored.

More precisely, fix \(D,a,r,\mu,K>0\). Between resets the particle solves \(dX_t=\mu\,dt+\sqrt{2D}\,dW_t\), starts at \(X_0=0\), and resets to zero at independent exponential rate \(r\). Local killing has potential
\[
V(x)=k\delta(x-a)+(K-k)\delta(x+a),\qquad 0\le k\le K.
\]
Put
\[
q=\sqrt{\mu^2+4Dr},\quad c=e^{-qa/D},\quad z=e^{\mu a/D},\quad t=K/q,
\]
\[
A=(1-c)(1-cz)>0,\quad b=c(z+1)-2<0,\qquad
K_c=q\,\frac{b+\sqrt{b^2+4A(z-1)}}{2A}.
\]
Then the mean time to killing has a **unique** minimizer \(k_*\). Its precise phase classification is
\[
\boxed{\begin{cases}
k_*=K,&0<K\le K_c,\\
K/2<k_*<K,&K>K_c.
\end{cases}}
\]
For zero drift, \(\mu=0\), the unique minimizer is instead \(k_*=K/2\) for every \(K>0\). Negative drift is obtained by reflection, interchanging the two target labels.

The optimum is characterized without a search over resetting rates: \(D,a,r,\mu\) are fixed and **only the total reactivity \(K\) is redistributed**. In the nonzero-drift interior phase, \(k_*\) is the unique solution of \(\partial_k B(k)=0\) on \((K/2,K)\), where the explicit absorption-before-reset probability \(B\) is below.

For example, \(D=\mu=a=r=1\) gives \(K_c=1.8149905664\ldots\). At \(K=4K_c\), the downstream optimum is \(k_*/K\simeq0.7428517\), while below the threshold all reactivity is downstream.

## Assumptions and scope

The state space is the full real line; there are no reflecting or absorbing spatial boundaries. Killing is exponential in the occupation-density local time, with the delta-function convention that the Feynman--Kac weight over a reset-free trajectory is
\[
\exp\!\left[-k\int_0^t\delta(X_s-a)\,ds-(K-k)\int_0^t\delta(X_s+a)\,ds\right].
\]
The point-sink strengths thus have units of length per time, matching the one-point convention in Mazzolo (2026). Resetting is instantaneous, independent of diffusion and killing, and reinitializes the particle at the origin with no accumulated reaction clock. The theorem concerns the unconditional expected eventual absorption time for fixed \(r>0\), not an optimal choice of \(r\) or of trap positions. For \(K>0\), absorption is eventual and the mean is finite.

## Proof

**1. Two-sink resolvent and renewal law.** The reset-free drift-diffusion resolvent is
\[
G_r(y\mid x)=\frac{1}{q}\exp\!\left[\frac{\mu(y-x)-q|y-x|}{2D}\right].
\]
Write \(E=e^{\mu a/(2D)}=\sqrt z\), \(h=e^{-qa/(2D)}=\sqrt c\), \(g=1/q\), and \(k_+=k\), \(k_-=K-k\). For the Laplace-time integrated killed densities at \(\pm a\), the rank-two resolvent equation has coefficient matrix and right-hand side
\[
\begin{pmatrix}1+gk_+&gc z\,k_-\\gc z^{-1}k_+&1+gk_-\end{pmatrix}
\begin{pmatrix}u_+\\u_-\end{pmatrix}
=gh\begin{pmatrix}E\\E^{-1}\end{pmatrix}.
\]
Its determinant is \(1+gK+g^2(1-c^2)k(K-k)>0\). The probability of being killed before an independently drawn reset is the total discounted killing flux \(B(k)=ku_++(K-k)u_-\), hence exactly
\[
\boxed{B(k)=\frac{h}{q}\,
\frac{Ek+E^{-1}(K-k)+\frac{1-c}{q}(E+E^{-1})k(K-k)}
{1+K/q+\frac{1-c^2}{q^2}k(K-k)}.}
\]
Indeed, if \(S_k(t)\) is reset-free target survival, integration by parts gives \(B(k)=1-r\int_0^\infty e^{-rt}S_k(t)\,dt\). Renewal over independent cycles therefore gives the resetting mean absorption time
\[
\boxed{T(k)=\frac{1-B(k)}{rB(k)}.}
\]
The mean is minimized precisely when \(B\) is maximized.

**2. Strict global concavity.** Set \(L_\pm(t)=\int_0^t\delta(X_s\mp a)\,ds\) for the *unreset* drift diffusion. They are nonnegative and have all finite-time polynomial moments. Thus
\[
S_k(t)=\mathbb E\exp[-kL_+(t)-(K-k)L_-(t)]
\]
and differentiation under the exponentially weighted time integral yields
\[
B''(k)=-r\int_0^\infty e^{-rt}\,
\mathbb E\big[(L_+(t)-L_-(t))^2e^{-kL_+(t)-(K-k)L_-(t)}\big]\,dt<0.
\]
Strictness holds because there is positive probability that a continuous Brownian path visits one target but not the other in a finite interval. Therefore \(B\) is strictly concave on the entire closed budget interval; its maximizer is unique, with no unexamined interior extrema.

**3. Directional symmetry and the threshold.** The quadratic terms in the numerator and denominator of \(B(k)\) are invariant under \(k\mapsto K-k\), so for \(\mu>0\),
\[
B(k)-B(K-k)=\frac{h}{q}\,
\frac{(E-E^{-1})(2k-K)}{1+K/q+\frac{1-c^2}{q^2}k(K-k)}.
\]
Consequently a maximizer cannot lie to the left of \(K/2\). Moreover \(B'(K/2)>0\) when \(\mu>0\), so it lies strictly to the right. Differentiating the exact rational expression at the downstream endpoint yields
\[
\frac{q(1+K/q)^2}{hE^{-1}}B'(K)
=\Phi(t),\qquad
\Phi(t)=(z-1)+[c(z+1)-2]t-(1-c)(1-cz)t^2.
\]
Because \(q>\mu>0\), \(0<c<1\), \(cz=e^{-(q-\mu)a/D}<1\), and \(c(z+1)<2\). Thus \(\Phi(0)=z-1>0\) and \(\Phi'(t)<0\) for every \(t\ge0\); it has exactly one positive zero \(t_c=K_c/q\), given in the finding. For \(K\le K_c\), strict concavity and \(B'(K)\ge0\) force the unique optimum \(k_*=K\). For \(K>K_c\), \(B'(K)<0<B'(K/2)\), so the unique optimum is interior to \((K/2,K)\). At \(\mu=0\), symmetry and strict concavity force the unique optimum \(K/2\). This proves the complete classification.

## Verification

The included standard-library script `verify.py` checks 4,760 deterministic conditions. Its separately constructed two-by-two Green-function linear solve reproduces the rational expression for \(B\) across a parameter grid; it checks the sign transition and strict concavity at selected budgets; and a distinct nearest-neighbor drift-diffusion chain, with reaction rates approximating point sinks, reproduces several absorption-before-reset probabilities as the lattice spacing decreases. The script is supplementary finite testing, **not** a substitute for the global strict-concavity and threshold arguments above. Run with `python3 verify.py` from the extracted package directory.

## Relationship to prior work

The motivating 2026 single-point model of Mazzolo provides the drifted Green-function and renewal framework, with a single local killing strength and optimality questions about resetting rate. Whitehouse, Evans, and Majumdar (2013) analyze a single partially absorbing target with resetting. Bressloff and Schumm (2021/2022) handle many finite-size partially absorbing traps under resetting in bounded two- or three-dimensional domains using narrow-capture asymptotics; their target reactivity is a common parameter rather than an optimally divided fixed total budget. Evans and Majumdar (2011) optimize resetting strategy for a *distribution of a single absorbing target*, not the simultaneous two-target killing-strength allocation considered here. All these foundational resolvent and renewal principles are prior mathematics; the new statement is the sharp resource-split transition with uniqueness and its explicit dimensionless threshold.

## Limitations

No claim is made about correlated resetting, traps of finite width, interacting particles, nonconstant drift, time-varying reactivities, or the joint optimization of reset rate, positions, and budget. This is a two-target, one-dimensional exact-solvability result, not a general multi-target allocation theorem. The strict-comparison proof is specific to independent exponential killing in accumulated local time and independent instantaneous Poisson resetting. A more general existing rank-two resolvent or optimal experimental design result could imply some or all of the classification, even without identical wording; the originality assessment is therefore provisional pending independent specialist review.

## References

1. A. Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes*, arXiv:2609.22527v1 (first public 2026-09-18), https://arxiv.org/abs/2609.22527.
2. J. Whitehouse, M. R. Evans, S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, Phys. Rev. E **87**, 022118 (2013), arXiv:1301.2489, https://arxiv.org/abs/1301.2489.
3. P. C. Bressloff, R. D. Schumm, *The narrow capture problem with partially absorbing targets and stochastic resetting*, Multiscale Model. Simul. **20**, 857--881 (2022), arXiv:2110.06895, https://arxiv.org/abs/2110.06895.
4. M. R. Evans, S. N. Majumdar, *Diffusion with Optimal Resetting*, J. Phys. A **44**, 435001 (2011), arXiv:1107.4225, https://arxiv.org/abs/1107.4225.
