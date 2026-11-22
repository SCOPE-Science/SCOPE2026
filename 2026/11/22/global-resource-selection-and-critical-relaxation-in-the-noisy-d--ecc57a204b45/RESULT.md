# Global resource selection and critical relaxation in the noisy donation feedback game

## Finding

Consider the noise-corrected donation-game dynamics defined below. Every solution initially in the open state square exhibits the following complete noise-driven trichotomy. At zero noise it is either the central equilibrium or periodic. For positive noise it converges globally to one explicitly selected state; that state lies in the interior until a sharp noise boundary is attained, and beyond that boundary it lies on the exhausted or fully restored environmental face. At the sharp boundary, environmental relaxation is algebraic with a universal inverse-time coefficient.

Put \(x_*=(1+\theta)^{-1}\), and for \(k\ge0\) define \(n_*=1/2+srk^2(\theta-1)/(1+\theta)\). For every \(k>0\), the limiting state \((X,N)\) is
\[
(X,N)=\begin{cases}
(x_*,n_*),&0\le n_*\le1,\\
(\frac12-\frac1{4srk^2},1),&n_*>1,\\
(\frac12+\frac1{4srk^2},0),&n_*<0.
\end{cases}
\]
If \(\theta\ne1\), the unique change from an interior to boundary limit occurs when
\[
k_c^2=\frac{1+\theta}{2sr|\theta-1|}.
\]
For \(\theta>1\), the limit has \(N=1\) at and above this threshold. For \(0<\theta<1\), it has \(N=0\). For \(\theta=1\), every positive noise intensity leads to \((X,N)=(1/2,1/2)\); there is no finite boundary transition.

At exactly \(k=k_c\), all strictly interior initial states obey
\[
\begin{array}{ll}
\theta>1:&\displaystyle \lim_{t\to\infty}t(1-n(t))=\frac1{\varepsilon(\theta-1)},\quad \lim_{t\to\infty}t(x(t)-x_*)=\frac1{\varepsilon(1+\theta)},\\
0<\theta<1:&\displaystyle \lim_{t\to\infty}t n(t)=\frac1{\varepsilon(1-\theta)},\quad \lim_{t\to\infty}t(x_*-x(t))=\frac1{\varepsilon(1+\theta)}.
\end{array}
\]
These statements classify deterministic limits of the published noise-corrected mean-field ODE, not individual stochastic trajectories.

## Assumptions and scope

Let \(0<r<5\), \(s>0\), \(\varepsilon>0\), \(\theta>0\), \(k\ge0\), and \(x(0),n(0)\in(0,1)\). Let \(x\) be cooperator frequency and \(n\) environmental resource quality. The donation payoffs are
\[
\Pi_1=\begin{pmatrix}5-r&-r\\5&0\end{pmatrix},\qquad
\Pi_0=\begin{pmatrix}5&0\\5-r&-r\end{pmatrix}.
\]
Equations (4), (9), and (14) of Chen, Wu, and Guan reduce exactly to
\[
\dot x=sx(1-x)\left[r(1-2n)+4sr^2k^2(\tfrac12-x)\right],\qquad
\dot n=\varepsilon n(1-n)((1+\theta)x-1).
\]
Both variables remain strictly between zero and one at each finite time. No additional restrictions on \(\varepsilon\) or initial conditions are imposed. The mathematical equation may be analyzed for arbitrary positive \(k\); its biological derivation assumes weak selection and cannot independently validate very strong noise.

## Proof

**1. Candidate fixed points.** Set \(x_*=1/(1+\theta)\). The interior environmental root from \(\dot x=0\) is \(n_*=1/2+srk^2(\theta-1)/(1+\theta)\). On \(n=1\), the unique interior frequency root is \(X_1=1/2-1/(4srk^2)\); on \(n=0\) it is \(X_0=1/2+1/(4srk^2)\), when these fall in \((0,1)\). If \(n_*>1\), then necessarily \(\theta>1\), \(X_1>x_*\), and \(0<X_1<1/2\). If \(n_*<0\), then necessarily \(\theta<1\), \(1/2<X_0<x_*\). At equality \(n_*=1\) or \(0\), the appropriate root merges with \(x_*\). Elementary rearrangement yields the stated unique critical intensity.

**2. One dissipation identity proves all positive-noise global claims.** For an admissible target \(a\in[0,1]\) define the nonnegative Bernoulli divergence
\[
D_a(z)=a\log\frac a z+(1-a)\log\frac{1-a}{1-z},\qquad 0<z<1,
\]
with the continuous conventions \(D_0(z)=-\log(1-z)\), \(D_1(z)=-\log z\). For the corresponding selected \((X,N)\) above, use
\[
V(x,n)=D_X(x)+\frac{2sr}{\varepsilon(1+\theta)}D_N(n).
\]
Since \(r(1-2N)+4sr^2k^2(1/2-X)=0\), direct differentiation gives the **exact** identity
\[
\dot V=-4s^2r^2k^2(x-X)^2+2sr(n-N)(X-x_*).
\]
For an interior target or its critical boundary limit, \(X=x_*\), so the second term vanishes. The largest invariant subset of \(x=X\) consists solely of \((X,N)\): otherwise \(\dot x=-2srX(1-X)(n-N)\ne0\). For a strict environmental boundary target, \((n-N)(X-x_*)<0\) at every interior point, making \(\dot V<0\) away from the target. Sublevel sets of \(V\) keep \(x\) away from \(0,1\), and keep \(n\) away from the environmental endpoint opposite \(N\); for \(0<N<1\) they are compact in the open square. For \(N=0\) or \(1\), the same sublevels are compact in the closed square with only the selected environmental endpoint permitted. Standard compact-set invariance and LaSalle's principle thus give convergence from every interior state. No positive-noise interior periodic orbit can exist.

**3. The zero-noise alternative.** At \(k=0\), the same function with \(X=x_*\) and \(N=1/2\) is exactly conserved. It is strictly convex and proper on the open square, has only one critical point, and each positive level is a regular simple closed curve. The flow has no zero on such a level and hence every noncentral interior orbit is periodic.

**4. Critical inverse-time clock.** For \(\theta>1\) at \(k=k_c\), put \(u=x-x_*\), \(v=1-n\). Linearization at the limiting boundary state has one strictly negative eigenvalue, with an attracting one-dimensional center manifold whose tangent satisfies \(u=(\theta-1)v/(1+\theta)+O(v^2)\). Restricted to it,
\[
\dot v=-\varepsilon(\theta-1)v^2+O(v^3).
\]
Its positive branch is attracting, and interior trajectories cannot lie in the boundary strong-stable manifold \(v=0\), by invariance and uniqueness. Hence \(tv\to1/(\varepsilon(\theta-1))\), and the tangent relation gives the cooperator coefficient. For \(0<\theta<1\), put \(v=n\). The center manifold instead satisfies \(x-x_*=-(1-\theta)v/(1+\theta)+O(v^2)\), with \(\dot v=-\varepsilon(1-\theta)v^2+O(v^3)\), yielding the second pair. Global convergence from Step 2 places every interior solution in the local regime to which this calculation applies.

## Verification

The bundled `check.py` verifies symbolic payoff reductions, the environmental and boundary equilibrium identities, the exact Lyapunov derivative and critical thresholds, then integrates 18 contrasting initial-value cases. It corroborates, rather than substitutes for, the global argument. In the exact example \(\theta=2\), \(r=4\), \(s=1/2\), \(\varepsilon=2\), the threshold is \(k_c=\sqrt3/2\); at \(k=1/2\) every interior state converges to \((1/3,2/3)\), and at \(k=1\) it converges to \((3/8,1)\). Reflection of the feedback asymmetry to \(\theta=1/2\), \(k=1\), gives the environment-depletion limit \((5/8,0)\).

## Relationship to prior work

Chen, Wu, and Guan (2026), Secs. II–III and Appendices, derive the exact noise-corrected payoff model, the interior fixed point and its *local* noise-dependent stability; in particular they report stable internal coexistence for weak positive noise in their donation example. This finding does not claim discovery of that model, its equilibrium, or local damping. It establishes global selection for all interior initial states, explicit finite noise-driven loss of interior coexistence when feedback is asymmetric, and the universal algebraic rate at the boundary. Weitz et al. (2016) establish zero-noise environmental-game oscillations. Wang et al. (2026) study noise-corrected replicator dynamics without this coupled resource variable. Other resource-feedback models can have Lyapunov functions, but their payoff and feedback structures do not supply this theorem by implication.

## Limitations

The theorem concerns a two-dimensional, well-mixed, deterministic mean-field reduction. The source model uses a weak-selection approximation, so the arbitrarily large formal noise regime need not be quantitatively realistic in finite populations. There is no claim of almost-sure stochastic convergence, finite-population fixation, universal results for other payoff matrices, or global attraction from the invariant state-space boundary. The claimed originality is bounded by the accessible literature; the full 2026 foundational *Physical Review Letters* article could not be inspected through available institutional access, although its abstract describes a game without environmental feedback. Independent scientific verification has not been performed.

## References

1. Y.-D. Chen, Z.-X. Wu, J.-Y. Guan, *Fluctuations in Environmental Resource Availability Alter the Oscillatory Tragedy of the Commons*, arXiv:2611.06156v1, first public November 4, 2026, https://arxiv.org/abs/2611.06156 .
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113 (2016), E7518–E7525, https://doi.org/10.1073/pnas.1604096113 .
3. G. Wang, Q. Su, L. Wang, J. B. Plotkin, *Noise-Induced Replicator Dynamics in Evolutionary Games*, Phys. Rev. Lett. 137 (2026), 097401, https://doi.org/10.1103/3yby-qq2n .
