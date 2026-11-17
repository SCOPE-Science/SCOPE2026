# Universal single-peak phase-security capacity in a three-oscillator cycle

## Finding

For an attractive Kuramoto triangle carrying injections \((P,-P,0)\), with edge couplings \(K_{12}=K_{23}=1\) and \(K_{13}=b>0\), impose the edge-specific phase-security limits \(|\theta_1-\theta_2|\le\gamma\), \(|\theta_3-\theta_2|\le\eta\), and \(|\theta_1-\theta_3|\le\gamma\), where \(0<\eta<\gamma<\pi/2\). The exact largest secure, exponentially stable injection is

\[
P_{\rm sec}(b)=\begin{cases}
\displaystyle\sin\gamma\left(1+\frac{b}{\sqrt{1+b^2+2b\cos\gamma}}\right),&0<b\le b_*,\\[5pt]
\displaystyle\sin\eta+\sin\left(\eta+\arcsin\frac{\sin\eta}{b}\right),&b\ge b_*,
\end{cases}
\quad b_*:=\frac{\sin\eta}{\sin(\gamma-\eta)}.
\]

More precisely, a secure equilibrium exists if and only if \(0\le P\le P_{\rm sec}(b)\); it is unique up to common phase and exponentially attracting modulo that common phase. The capacity is continuous and strictly increasing on \((0,b_*)\) and strictly decreasing on \((b_*,\infty)\), with unique peak \(P_{\rm sec}(b_*)=\sin\gamma+\sin\eta\), and limiting capacities \(\sin\gamma\) as \(b\downarrow0\) and \(2\sin\eta\) as \(b\to\infty\).

Therefore, for each
\[
\max\{\sin\gamma,2\sin\eta\}<P<\sin\gamma+\sin\eta,
\]
there are unique \(0<b_-(P)<b_*<b_+(P)<\infty\) such that a secure equilibrium exists **exactly** for \(b\in[b_-(P),b_+(P)]\). For any uncertain but fixed coupling \(b\in[b_L,b_U]\), where \(0<b_L\le b_U\), a secure equilibrium exists for **every** realization precisely when
\[
P\le\min\{P_{\rm sec}(b_L),P_{\rm sec}(b_U)\}.
\]
In the same reentrant-injection interval, for all sufficiently large \(b\) the network still possesses an exponentially stable zero-winding phase-locked equilibrium with all three principal differences strictly below \(\pi/2\), although its stricter security constraints fail.

For the explicit safety limits \(\gamma=\pi/3\) and \(\eta=\pi/6\), one has \(b_*=1\), \(P_{\rm sec}(1)=(1+\sqrt3)/2\), and
\[
P_{\rm sec}(b)=\begin{cases}
\frac{\sqrt3}{2}\left(1+\frac{b}{\sqrt{b^2+b+1}}\right),&0<b\le1,\\[4pt]
\frac12+\frac12\sqrt{1-\frac1{4b^2}}+\frac{\sqrt3}{4b},&b\ge1.
\end{cases}
\]

## Assumptions and scope

The first-order flow is \(\dot\theta_i=\omega_i-\sum_{j\ne i}K_{ij}\sin(\theta_i-\theta_j)\), with \(\omega_1=P\), \(\omega_2=-P\), \(\omega_3=0\), \(P\ge0\), and the symmetric positive edge weights stated above. All phase differences refer to a consistent lift of the three angles (zero winding), not arbitrary independent choices modulo \(2\pi\). The security caps \(\eta\) and \(\gamma\) are fixed, strict interior angles below \(\pi/2\); the inequalities themselves are non-strict and allow equality at the load boundary. The guarantee for uncertain \(b\) is pointwise in each frozen coupling, not a common solution or stability under switching or state-dependent changes. The claim is only about the specified network and caps, not a general Kuramoto graph.

## Proof

Write \(\delta=\theta_1-\theta_2\), \(\phi=\theta_1-\theta_3\), and \(\psi=\theta_3-\theta_2\), so \(\delta=\phi+\psi\). Node-3 balance and node-1 balance are, respectively,
\[
 b\sin\phi=\sin\psi,\qquad P=\sin\delta+b\sin\phi.
\]
Inside the security caps, \(\phi,\psi\in(-\pi/2,\pi/2)\). The first identity forces the signs of \(\phi\) and \(\psi\) to agree, hence to match the sign of \(\delta\); the second forces that sign to be nonnegative when \(P\ge0\). For \(P=0\) all differences vanish. For \(P>0\), \(0<\phi,\psi<\delta\le\gamma\).

For each \(b>0\) and \(0\le\delta\le\gamma\), node-3 balance and \(\phi+\psi=\delta\) have the unique principal solution
\[
\phi(\delta,b)=\arctan\left(\frac{\sin\delta}{b+\cos\delta}\right),\quad
\psi(\delta,b)=\delta-\phi(\delta,b).
\]
Equivalently,
\[
 b\sin\phi=\frac{b\sin\delta}{\sqrt{1+b^2+2b\cos\delta}},\quad
 P(\delta,b)=\sin\delta+\frac{b\sin\delta}{\sqrt{1+b^2+2b\cos\delta}}.
\]
Implicit differentiation of \(b\sin\phi=\sin\psi\), with \(\psi=\delta-\phi\), yields
\[
 \frac{\partial\phi}{\partial\delta}=\frac{\cos\psi}{b\cos\phi+\cos\psi}\in(0,1),\quad
\frac{\partial\psi}{\partial\delta}=\frac{b\cos\phi}{b\cos\phi+\cos\psi}>0.
\]
Hence \(P_{\delta}=\cos\delta+b\cos\phi\,\phi_{\delta}>0\) throughout \([0,\gamma]\). Secure solutions correspond exactly to \(0\le\delta\le\delta_{\max}(b)\), where \(\delta_{\max}\) is the first of the bounds \(\delta=\gamma\) or \(\psi=\eta\) to be reached. The third edge cap is automatically satisfied since \(0\le\phi\le\delta\le\gamma\).

At \(\delta=\gamma\) the condition \(\psi\le\eta\) is equivalent, by the monotonicity of sine on the principal interval, to \(b\le\sin\eta/\sin(\gamma-\eta)=b_*\). Thus, if \(b\le b_*\), \(\delta_{\max}=\gamma\), giving the first capacity branch. If \(b\ge b_*\), the tighter edge reaches \(\psi=\eta\) first. There \(b\sin\phi=\sin\eta\) and \(\phi\in[0,\gamma-\eta]\), whence \(\phi=\arcsin(\sin\eta/b)\) and \(\delta_{\max}=\eta+\arcsin(\sin\eta/b)\), giving the second branch. Both expressions meet at \(P=\sin\gamma+\sin\eta\) for \(b=b_*\).

For the first branch, direct differentiation gives
\[
\frac{d}{db}\left(\frac{b}{\sqrt{1+b^2+2b\cos\gamma}}\right)
=\frac{1+b\cos\gamma}{(1+b^2+2b\cos\gamma)^{3/2}}>0.
\]
For the second branch \(\arcsin(\sin\eta/b)\) strictly decreases with \(b\), while its sum with \(\eta\) always lies in \((\eta,\gamma]\subset(0,\pi/2)\); hence the sine term strictly decreases. The endpoint limits follow directly. Since \(\sin\gamma+\sin\eta\) strictly exceeds both limiting capacities (because \(\gamma>\eta>0\)), the strict unimodality proves the two finite inverse roots and the complete reentrant window. The minimum of a unimodal function over a compact interval occurs at an endpoint, proving the robust condition.

At each secure equilibrium all three edge differences are strictly smaller than \(\pi/2\). The Jacobian is minus the weighted graph Laplacian with edge conductances \(K_{ij}\cos(\theta_i-\theta_j)>0\). Its kernel is precisely the common-phase direction, and both transverse eigenvalues are negative. The strictly increasing map \(\delta\mapsto P(\delta,b)\) gives uniqueness within the secure sector; the Hessian conclusion yields exponential orbital attraction there, including at a non-strict security boundary.

Finally, for any injection in the displayed reentrant interval, \(P<\sin\gamma+\sin\eta<2\). For sufficiently large \(b\), the strictly increasing same function on \(0\le\delta\le\pi/2\) satisfies
\[
 P(\pi/2,b)=1+\frac{b}{\sqrt{1+b^2}}\longrightarrow2>P.
\]
It therefore has a unique solution with \(0<\delta<\pi/2\) and \(0<\phi,\psi<\delta\). Its weighted Laplacian is positive on the transverse space, so this is still exponentially stable, but it violates the \(\psi\le\eta\) security cap because \(P>P_{\rm sec}(b)\) at large \(b\). This distinguishes loss of security from loss of phase locking.

## Verification

The companion `verify.py` checks the phase-balancing identity, analytic capacity formula, switch point, strict sampled monotonicity, and persistence of stable locking beyond the secure interval for five independent cap pairs. It produced `VERIFY_OK exact_boundaries=5 monotone_branch_tests=5 phase_balance_cases=3005 stable_beyond_security=5`. Those finite computations are checks, **not** a proof of the universal quantifiers; the arguments above establish them analytically.

## Relationship to prior work

Bačić et al. (arXiv:2611.06466v1, 2026) derive general sufficient certificates for robust phase locking with uncertain couplings and individual edge limits. Bačić et al. (arXiv:2610.24595v1, 2026) provide a convex network-flow equivalence and sufficient and necessary **bounds** using approximations, but not this exact sharp, all-parameter security capacity or its unique strengthening reversal. General zero-winding uniqueness and Laplacian stability are background rather than new results. Witthaut and Timme (2012) exhibit Braess-type loss of **phase locking** in larger power networks, a different property from the analytically isolated loss of **stricter edge security while stable locking survives** here. The exact formulas and the arbitrary-cap single-peak/reentrant classification are the proposed contribution; no claim is made to introduce generic cycle-flow theory or the Braess phenomenon.

## Limitations

This is a static three-node, symmetric-sine, first-order model with positive couplings and particular frequency balance. The two edge caps may differ, but both must be below \(\pi/2\). The robust statement does not imply one equilibrium common to multiple couplings, nor attraction under time-varying uncertain or adaptive weights. Stable equilibria outside the secure sector need not be globally unique. The full multistability or phase-slip portrait and dynamic security of arbitrary trajectories are not classified. Historical priority beyond the inspected sources awaits independent checking.

## References

1. I. Bačić et al., *Phase Locking in Oscillator Networks with Uncertain and State-Dependent Couplings*, arXiv:2611.06466v1 (first posted 2026-11-04), https://arxiv.org/html/2611.06466v1.
2. I. Bačić et al., *Linear Approximations Provide Rigorous Conditions for Phase Locking in Oscillator Networks and Power Grids*, arXiv:2610.24595v1 (posted 2026-10-17), https://arxiv.org/html/2610.24595v1.
3. D. Witthaut and M. Timme, *Braess's paradox in oscillator networks, desynchronization and power outage*, New Journal of Physics **14**, 083036 (2012), https://doi.org/10.1088/1367-2630/14/8/083036.
