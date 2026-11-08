# Sharp convex-order boundary slowdown in a two-by-three martingale Sinkhorn iteration

## Finding

Consider the smallest reflection-symmetric finite martingale bridge with two source atoms and three terminal atoms. Its exact alternating martingale/terminal marginal KL-projection algorithm has a **scalar nonlinear recursion**. Strict convex order gives a sharp geometric convergence rate, but at the feasible boundary of convex order the same algorithm slows to reciprocal-time convergence in relative entropy.

Let \(0<a<1\), \(a\le b<1\), and define
\[\mu=\tfrac12(\delta_{-a}+\delta_a),\qquad \nu=\tfrac b2(\delta_{-1}+\delta_1)+(1-b)\delta_0.\]
For the exact alternating projections specified below, the positive scalar \(t_k\) evolves by
\[t_0=\frac{2(1-b)}b,\qquad t_{k+1}=F_{a,b}(t_k):=\frac{1-b}{b(1-a^2)}\left(a^2t_k+\sqrt{a^2t_k^2+4(1-a^2)}\right).\]
For \(b>a\), the unique fixed point and exact local convergence factor are
\[t_* = \frac{2(1-b)}{\sqrt{b^2-a^2}},\qquad \rho=\frac{a^2(1-b)}{b(b-a^2)}.\]
The optimal **global** Lipschitz factor of this scalar map on positive inputs is \(L=a(1-b)/(b(1-a))<1\), and the relative entropy of the optimal joint coupling with respect to the martingale half-step iterates has exact asymptotic consecutive ratio \(\rho^2\). As \(b\downarrow a\), \(\rho\uparrow1\).

At the still feasible boundary \(b=a\), there is no finite fixed point; instead,
\[\frac{t_k}{\sqrt{k}}\longrightarrow\frac{2\sqrt{1-a}}a,\quad kq_-(t_k)\longrightarrow\frac{a(1-a)}4,\quad kH(\pi_*\mid\pi_k)\longrightarrow\frac{a(1-a)}4.\]

## Assumptions and scope

The source values are \(X\in\{-a,a\}\) with equal masses; target values are \(Y\in\{-1,0,1\}\) with masses \(b/2,1-b,b/2\). All arithmetic and KL projections are exact. The cost is zero and the reference probability measure is \(R=\mu\otimes\nu\). Starting with the untilted terminal factor \(\nu\) (zero dual potential), alternate these **full** KL projections: (i) for each source row, impose its source mass and conditional martingale mean, keeping current column factors; (ii) rescale columns to exactly restore \(\nu\). This is the finite-dimensional alternating-marginal/martingale Sinkhorn procedure, not an ordinary marginal-only Sinkhorn iteration and not a method using approximate martingale gradient updates.

Write \(\pi_k\) for the joint coupling **after the first projection in cycle** \(k\), before restoring terminal marginals. The marginal of \(X\) and the martingale constraint are then exact but the terminal marginal generally differs from \(\nu\). Write \(q_-(t),q_0(t),q_+(t)\) for the conditional probabilities of \(Y=-1,0,1\) given \(X=a\) at that half-step, with the other source row reflected. Set \(H(P\mid Q)=\sum_{x,y}P(x,y)\log(P(x,y)/Q(x,y))\), with the convention \(0\log(0/q)=0\).

The convex-order feasibility threshold is precisely \(b\ge a\). The optimizer \(\pi_*\) is unique by strict convexity of entropy and symmetry of the reference and constraints. For \(X=a\), its row law is \(((b-a)/2,1-b,(b+a)/2)\); for \(X=-a\), reflect the endpoints. It has full support for \(b>a\), but at \(b=a\) the opposite-sign endpoint cell has zero mass.

## Proof

**Step 1: Reduce the row projection.** After any symmetric column projection, the two endpoint base weights agree, so modulo a common scale the current target weights are \((1,t,1)\), with \(t>0\). The entropy projection under a conditional mean constraint \(\mathbb E[Y\mid X=a]=a\) exponentially tilts these to \((z^{-1},t,z)\), uniquely for some \(z>0\). Put \(s=z+z^{-1}\), \(d=z-z^{-1}\). The mean constraint gives \(d=a(s+t)\), while \(s^2-d^2=4\). The unique positive solution is
\[s(t)=\frac{a^2t+\sqrt{a^2t^2+4(1-a^2)}}{1-a^2}.\]
Therefore
\[q_0(t)=\frac{t}{s(t)+t},\qquad q_\pm(t)=\frac{1-q_0(t)\pm a}{2}.\]
The reflected row for \(X=-a\) ensures that after the martingale projection the target column masses are \(((1-q_0)/2,q_0,(1-q_0)/2)\).

**Step 2: Reduce the column projection.** Restoring target masses \((b/2,1-b,b/2)\) multiplies endpoint column weights by \(b/(1-q_0)\), and the central column by \((1-b)/q_0\). The new center-to-endpoint weight ratio consequently is
\[t^+=t\frac{(1-b)/q_0}{b/(1-q_0)}=\frac{1-b}{b}s(t)=F_{a,b}(t).\]
At the initial untilted reference weights the ratio is \(t_0=(1-b)/(b/2)=2(1-b)/b\). This proves the claimed exact recurrence for **all cycles**.

**Step 3: Strict convex order and exact rate.** If \(b>a\), the fixed point must have \(q_0(t_*)=1-b\), so the conditional endpoint weights are \((b-a)/2\) and \((b+a)/2\). The constraint \(s^2-[a(s+t)]^2=4\) then gives
\[t_*=\frac{2(1-b)}{\sqrt{b^2-a^2}},\quad s_* =\frac{2b}{\sqrt{b^2-a^2}}.\]
The scalar map is differentiable, strictly increasing and strictly convex. Its derivative rises toward
\[\sup_{t>0}F'_{a,b}(t)=\frac{a(1-b)}{b(1-a)}=:L<1\quad(b>a).\]
Thus the recurrence is globally contracting, and this sup derivative is the **sharp** global Lipschitz constant. At the fixed point,
\[F'_{a,b}(t_*)=\frac{a^2(1-b)}{b(b-a^2)}=:\rho\in(0,1).\]
As \(t_0<t_*\), the trajectory is nonstationary and increases strictly to \(t_*\); differentiability implies its exact consecutive error ratio tends to \(\rho\).

For KL relative entropy, each row of \(\pi_k\) has the same divergence from its reflected optimal row, so
\[H(\pi_*\mid\pi_k)=\frac{b-a}{2}\log\frac{b-a}{1-q_0(t_k)-a}+(1-b)\log\frac{1-b}{q_0(t_k)}+\frac{b+a}{2}\log\frac{b+a}{1-q_0(t_k)+a}.\]
Writing \(\delta=q_0(t)-(1-b)\), Taylor expansion gives
\[H(\pi_*\mid\pi(t))=\frac{\delta^2}{2}\left(\frac1{1-b}+\frac b{b^2-a^2}\right)+O(\delta^3),\]
with positive coefficient. Moreover \(q'_0(t_*)>0\). Consequently the exact consecutive KL ratio tends to \(\rho^2\), and \(\rho\to1\) as \(b\downarrow a\).

**Step 4: Boundary convex order.** At \(b=a\), positive \(t\) satisfies \(F_{a,a}(t)>t\). No finite fixed point exists, because \(q_0(t)<1-a\) at every finite \(t\). Hence \(t_k\uparrow\infty\). Expansion of the exact positive square root shows
\[F_{a,a}(t)=t+\frac{2(1-a)}{a^2t}+O(t^{-3}),\qquad t_{k+1}^2-t_k^2\longrightarrow\frac{4(1-a)}{a^2}.\]
Cesàro averaging yields \(t_k/\sqrt{k}\to 2\sqrt{1-a}/a\). Furthermore,
\[q_-(t)=\frac{1-q_0(t)-a}{2}\sim\frac{(1-a)^2}{at^2}.\]
The optimal boundary conditional law is \((0,1-a,a)\). Since \(q_0=1-a-2q_-\) and \(q_+=a+q_-\), its KL divergence satisfies
\[H(\pi_*\mid\pi(t))=(1-a)\log\frac{1-a}{1-a-2q_-}+a\log\frac{a}{a+q_-}=q_-+O(q_-^2).\]
Thus both \(kq_-(t_k)\) and \(kH(\pi_*\mid\pi_k)\) tend to \(a(1-a)/4\).

## Verification

`verify_martingale.py` independently checks the fixed-point identities symbolically, the two projection steps for 350 reproducible rational-parameter samples (covering nontrivial cost-free rows), derivative and contraction inequalities, and representative strict and boundary instances, as well as 60 full two-by-three alternating KL-projection cycles computed independently by numerical tilt root solves. Boundary tests use 100,000 exact-map iterations for three values of \(a\), checking the claimed constants with relative tolerance \(0.5\%\). The symbolic arguments above, not finite experiments, establish the infinite limits and all-parameter statements. Run `python verify_martingale.py` with Python 3 and SymPy.

## Relationship to prior work

Kazeykina, Ren and Wang (2026, arXiv:2609.18850) prove exponential convergence for entropy martingale Sinkhorn under a strict convex-order condition and **convex support of the terminal marginal**; this three-atom example does **not** meet the convex-support assumption, and its boundary case violates strict convex order. Chen, Conforti, Ren and Wang (2024, arXiv:2407.14186) establish exponential convergence under their conditions and examine dependence on the terminal marginal numerically. Here the exact two-by-three recursion, its optimal global Lipschitz bound, exact local KL ratio, and boundary reciprocal-time constants are supplied directly, independent of applying those general results.

Bifronte, Ley and Sylvestre (2026, arXiv:2610.26504) prove linear convergence of **SISTA**, which performs a martingale-potential gradient step rather than the exact martingale KL projection treated here. Tang and collaborators (2025, arXiv:2508.17641) formulate discrete martingale Sinkhorn-type and sparse-Newton methods for approximate constraint satisfaction; their algorithmic comparison does not yield the stated exact scalar recurrence or convex-order boundary law. Generic iterative KL/Bregman projection theory supplies context but not these sharp instance-specific formulas. The finite model is a diagnostic example, not an extension of assumptions asserted in any of these sources.

## Limitations

The theorem is restricted to the reflection-symmetric two-source, three-target zero-cost KL bridge initialized at the unmodified reference weights; the target support has three isolated points. It does not give sharp rates for larger discrete supports, nonsymmetric costs, accelerated martingale algorithms, or finite-precision arithmetic. At the boundary the dual ratio diverges although the primal couplings converge; this is not nonexistence of an entropic optimizer. The literature comparison cannot exclude unpublished or unindexed equivalent small-state calculations. Independent mathematical validation has not been performed.

## References

1. Anna Kazeykina, Zhenjie Ren and Hecheng Wang, *Exponential convergence of Sinkhorn algorithm for entropy martingale optimal transport*, arXiv:2609.18850, first public 2026-09-16. https://arxiv.org/abs/2609.18850
2. Fan Chen, Giovanni Conforti, Zhenjie Ren and Xiaozhen Wang, *Convergence of Sinkhorn’s Algorithm for Entropic Martingale Optimal Transport Problem*, arXiv:2407.14186, first public 2024-07-19. https://arxiv.org/abs/2407.14186
3. Giorgia Bifronte, Armand Ley and Maxime Sylvestre, *On the Linear Convergence of SISTA for Entropic Martingale Optimal Transport*, arXiv:2610.26504, first public 2026-10-19. https://arxiv.org/abs/2610.26504
4. Xun Tang, Michael Shavlovsky, Holakou Rahmanian, Tesi Xiao and Lexing Ying, *An efficient algorithm for entropic optimal transport under martingale-type constraints*, arXiv:2508.17641, first public 2025-08-25. https://arxiv.org/abs/2508.17641
