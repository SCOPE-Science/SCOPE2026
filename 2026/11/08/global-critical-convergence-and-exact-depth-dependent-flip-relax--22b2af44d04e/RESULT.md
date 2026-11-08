# Global critical convergence and exact depth-dependent flip relaxation in a gradient-descent quotient map

## Finding
At the first multiplier-\(-1\) boundary of a depth-indexed scalar gradient-descent quotient, the critical relaxation rate is an explicit function of depth. For \(n\in\mathbb{N}\), define
\[
h_n(u)=u\left[1-\frac{1}{n}u^{1-1/n}(u-1)\right]^{2n},\qquad u>0,
\]
and define \(h_\infty(u)=u\exp(2u(1-u))\). Write \(\epsilon=1/n\) at finite depth and \(\epsilon=0\) in the limit. Every fixed map has a neighborhood of \(u=1\) on which all nonstationary forward orbits converge to \(1\), with their displacement changing sign at every sufficiently late step, and satisfy
\[
\lim_{k\to\infty}k\,(u_k-1)^2=\frac{3}{4(2-\epsilon)(5-2\epsilon)}.
\]
For the limiting map, the local assertion strengthens to **global convergence for every \(u_0>0\)**. Apart from the set of initial conditions whose orbit lands exactly at \(1\) after finitely many iterations, all such trajectories have
\[
\lim_{k\to\infty}\sqrt{k}\,|u_k-1|=\sqrt{\frac{3}{40}}.
\]

## Assumptions and scope
All iterations use the original discrete clock \(k=0,1,2,\ldots\). The parameter is exactly the first flip boundary \(c=1\); \(n\) is fixed before \(k\to\infty\), not allowed to grow with iteration count. Finite-depth conclusions are **local near \(1\)**; global convergence is proved **only** for the depth-limit map. For finite \(n\), any orbit with a finite hit at \(1\) is excluded from the nonzero asymptotic formula; sufficiently close nonfixed orbits cannot have such a finite hit. The limiting map's exceptional set is \(E=\bigcup_{j\ge0}h_\infty^{-j}(\{1\})\).

## Proof
**Local normal form.** Put \(z=u-1\). For finite depth introduce \(\epsilon=1/n\) and expand the analytic logarithm
\[
\log h_n(1+z)=\log(1+z)+\frac{2}{\epsilon}\log\left(1-\epsilon(1+z)^{1-\epsilon}z\right).
\]
The expression has a well-defined analytic limit at \(\epsilon=0\). Direct Taylor expansion, valid for fixed \(0\le\epsilon\le1\), gives
\[
h_n(1+z)-1=-z+az^2+bz^3+O(z^4),
\qquad a=\epsilon-2,\qquad b=\frac{\epsilon^2}{3}-2\epsilon+\frac83.
\]
Composing the map with itself cancels the quadratic term and yields
\[
h_n^2(1+z)-1=z-\kappa_n z^3+O(z^4),\quad
\kappa_n=2(a^2+b)=\frac43(2-\epsilon)(5-2\epsilon)>0.
\]
For sufficiently small nonzero \(|z|\), the two-step map preserves the sign of \(z\) and contracts its absolute value strictly. Its even subsequence tends to zero; its odd subsequence does as well, and the one-step derivative \(-1\) gives eventual sign alternation. If \(w_m=u_{2m}-1\), then
\[
\frac1{w_{m+1}^2}-\frac1{w_m^2}=2\kappa_n+O(|w_m|).
\]
Cesàro averaging gives \(m w_m^2\to(2\kappa_n)^{-1}\). Replacing \(2m\) by the actual step index \(k\), with odd terms asymptotically equal in magnitude, gives \(k(u_k-1)^2\to\kappa_n^{-1}\).

**Global convergence for the limiting map.** Put \(f(u)=u\exp(2u(1-u))\). For \(u>0\), \(f(u)>u\) when \(u<1\), and \(f(u)<u\) when \(u>1\); the only fixed points of \(f\) on \([0,\infty)\) are \(0,1\). The derivative of \(\log f\) vanishes only at \(u_*=(1+\sqrt5)/4\), so \(0\le f(u)\le M=f(u_*)\) and the compact interval \([0,M]\) maps into itself.

We prove there is **no prime two-cycle**. Suppose \(0<u<v\) with \(f(u)=v\) and \(f(v)=u\). The comparison with the identity above forces \(u<1<v\). Multiplying the two cycle equations gives
\[
u(1-u)+v(1-v)=0.
\]
Set \(s=u+v\) and \(\delta=v-u\). As \(u,v>0\) are distinct, this identity forces \(1<s<2\), \(\delta^2=s(2-s)\), and \(2u(1-u)=(s-1)\delta\). But the strict logarithmic-mean inequality gives
\[
\log(v/u)>\frac{2(v-u)}{v+u}=\frac{2\delta}{s}>(s-1)\delta=2u(1-u),
\]
contradicting \(\log(v/u)=2u(1-u)\) from \(f(u)=v\). Here \(2/s>s-1\) for \(1<s<2\).

Apply the classical interval-iteration convergence theorem of Coppel: a continuous self-map of a compact interval without points of least period two has convergent iterates from every initial point. Every strictly positive orbit enters \((0,M]\) and hence converges to a fixed point of \(f\) in \([0,M]\). It cannot converge to \(0\), because eventually being in \((0,1)\) would make every subsequent term increase strictly. Thus every positive orbit converges to \(1\). Once it enters the local neighborhood proved above, its non-finite-hitting orbit obeys the same sharp limit at \(\epsilon=0\), namely \(\kappa_\infty=40/3\) and \(k(u_k-1)^2\to3/40\).

## Verification
The companion \(checks/verify.py\) computes the exact cubic coefficient symbolically for general \(\epsilon\), takes its analytic infinite-depth limit, and tests five finite iteration scenarios, including the depth-limit map. It prints `VERIFY_OK exact_coefficients=3 cubic_return=1 finite_orbits=5` on success. This is supporting reproducibility; the universal and global claims are established by the analytic proof and Coppel's theorem, not by finite iteration experiments.

## Relationship to prior work
Hofmann (2026) derives the finite-depth quotient and limiting Ricker-type map, locates the first flip boundary, and describes the post-edge dynamics. These objects and the first bifurcation are **prior results**. The contribution here is the sharp *physical-iteration-time* relaxation constant for each depth at the neutral boundary, together with a global threshold convergence proof for the limit map. Coppel's original theorem provides the general interval-dynamical implication, and prior Ricker work treats related but different exponential-growth maps. A period-two exclusion argument specialized to the quadratic-exponent limit is essential; one must not identify \(u\exp(2u(1-u))\) with the classical \(u\exp(r(1-u))\) without an explicit conjugacy.

## Limitations
No global finite-depth convergence is proved; the finite maps may have other fixed points or other attractors far from \(u=1\). The rate is for fixed depth before the long-time limit and may not be uniform as depth grows. A positive orbit that hits \(1\) in finite time converges exactly and does not have the nonzero square-root constant. The global theorem is for positive initial data; the boundary fixed point \(0\) does not converge to \(1\). General deep-learning systems and stochastic iterations are outside scope. The historical-priority assessment is based on the inspected sources and targeted searches and is not independent certification.

## References
- Thomas Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, arXiv:2607.04993v1 (first public 2026-07-06), https://arxiv.org/abs/2607.04993.
- W. A. Coppel, *The solution of equations by iteration*, Proceedings of the Cambridge Philosophical Society 51 (1955), 41–43.
- S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira, and R. Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications 29 (2023), 575–591, https://doi.org/10.1080/10236198.2023.2222855 (related Ricker literature on a different map).
