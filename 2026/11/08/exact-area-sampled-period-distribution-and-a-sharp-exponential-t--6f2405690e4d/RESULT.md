# Exact area-sampled period distribution and a sharp exponential tail in a two-population replicator center

## Finding
Consider the continuous-time two-population zero-sum replicator center
\[
\dot X=(1-X^2)Y,\qquad \dot Y=-(1-Y^2)X,
\qquad (X,Y)\in(-1,1)^2.
\]
Choose \((X_0,Y_0)\) uniformly with respect to Euclidean area on the square and let \(\mathcal T\) be its minimal positive physical-time orbital period (defined almost surely, since the center is a zero-area exception). Write
\[
Q=(1-X_0^2)(1-Y_0^2),\quad k=\sqrt{1-Q},
\]
and use the standard complete elliptic integrals
\[
K(k)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}},\qquad
E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2\theta}\,d\theta.
\]
Then \(Q\) has the **exact density and cumulative distribution**
\[
 f_Q(q)=\frac12K(\sqrt{1-q}),\qquad
 \Pr(Q\le q)=1-E(\sqrt{1-q})+qK(\sqrt{1-q}),\qquad 0<q<1.
\]
The known exact period map is \(\mathcal T=4K(\sqrt{1-Q})\), strictly decreasing as a function of \(Q\). Consequently, for each \(t>2\pi\), let \(q_t\in(0,1)\) be the unique solution of \(4K(\sqrt{1-q_t})=t\). The **exact physical-time period tail** is
\[
\boxed{\Pr(\mathcal T>t)=1-E(\sqrt{1-q_t})+q_tK(\sqrt{1-q_t}).}
\]
For \(t\le2\pi\), this probability is one. Its two-term sharp large-time asymptotic is
\[
\boxed{\Pr(\mathcal T>t)=(2t+4)e^{-t/2}+O(t^2e^{-t})\quad(t\to\infty).}
\]
In particular, the exact exponential-moment threshold is
\[
\boxed{\mathbb E[e^{s\mathcal T}]<\infty\iff0\le s<\tfrac12,}
\]
where divergence holds also at \(s=\tfrac12\). Every finite ordinary positive moment exists.

## Assumptions and scope
The vector field is the normalized cubic subfamily of the invariant-square two-player evolutionary model from Gasull–Gouveia–Santana (2024). Specifically, put \(x=X/2\), \(y=Y/2\) in their square and select \(f(x,y)=-y\), \(g(x,y)=x\); their convention \(\dot x=(4x^2-1)f\), \(\dot y=(4y^2-1)g\) yields exactly the displayed normalized ODE **with no time rescaling**. Uniform original-square area and uniform normalized-square area define the same probability after this affine coordinate change. All probabilities are over the **initial condition**, not a stationary distribution of the flow. The parameter-free normalized case is considered; its classical center, first integral, and elliptic period are prior knowledge, not asserted as new.

## Proof
**First integral and nondegenerate periodic levels.** Set \(q(X,Y)=(1-X^2)(1-Y^2)\). Direct differentiation gives
\[
\frac{dq}{dt}=-2X(1-Y^2)(1-X^2)Y
 +2Y(1-X^2)(1-Y^2)X=0.
\]
The Hamiltonian \(H=(1-q)/2\) satisfies \(\dot X=\partial_YH\) and \(\dot Y=-\partial_XH\). In the open square, the only critical point is the origin, where \(q=1\). For every \(0<q<1\), the level is a smooth simple closed curve enclosing the origin, and the nonzero flow traverses it periodically. Its first-quadrant branch is
\[
Y=\sqrt{\frac{1-q-X^2}{1-X^2}},\qquad 0\le X\le\sqrt{1-q}.
\]
The quarter-orbit traversal (orientation reversed if necessary) lasts
\[
\int_0^{\sqrt{1-q}}\frac{dX}{\sqrt{1-X^2}\sqrt{1-q-X^2}}
=K(\sqrt{1-q}),
\]
after \(X=\sqrt{1-q}\sin\theta\). By reflection symmetry, the minimal original-time period is \(T(q)=4K(\sqrt{1-q})\). Its minimum limit as \(q\uparrow1\) is \(2\pi\), and it diverges as \(q\downarrow0\). The integrand shows strict decrease of \(T\) with \(q\).

**Exact area distribution.** If \(X\) is uniform on \((-1,1)\), then \(U=1-X^2\) has density \(f_U(u)=1/(2\sqrt{1-u})\) on \((0,1)\). The independent variable \(V=1-Y^2\) has the same law and \(Q=UV\). Hence
\[
f_Q(q)=\frac14\int_q^1\frac{du}{\sqrt{u(1-u)(u-q)}}
=\frac12K(\sqrt{1-q}),
\]
by \(u=1-(1-q)\sin^2\theta\). For \(k=\sqrt{1-q}\), standard derivatives of the elliptic integrals yield
\[
\frac{d}{dq}\left[1-E(k)+qK(k)\right]=\tfrac12 K(k).
\]
The bracket vanishes at \(q=0\) by continuity, proving the CDF. The tail formula follows from strict monotonicity of \(T\) and the event \(\{\mathcal T>t\}=\{Q<q_t\}\).

**Sharp two-term limit.** Put \(L(q)=\log(4/\sqrt q)\). The complementary-modulus expansions as \(q\downarrow0\) are
\[
K(\sqrt{1-q})=L(q)+O(qL(q)),\qquad
E(\sqrt{1-q})=1+\tfrac q2\left(L(q)-\tfrac12\right)+O(q^2L(q)).
\]
Thus the exactly normalized area CDF satisfies
\[
\Pr(Q\le q)=\tfrac q2 L(q)+\tfrac q4+O(q^2L(q)).
\]
Inverting \(t=4K(\sqrt{1-q_t})\) gives
\[
q_t=16e^{-t/2}\left(1+O(te^{-t/2})\right),\quad
L(q_t)=t/4+O(te^{-t/2}).
\]
Combining these identities gives \((2t+4)e^{-t/2}+O(t^2e^{-t})\) with **both the leading and constant coefficients fixed**. Finally, for \(s>0\), the layer-cake identity
\[
\mathbb E[e^{s\mathcal T}]=1+s\int_0^\infty e^{st}\Pr(\mathcal T>t)\,dt
\]
(with nonnegative extended integrals) gives convergence exactly when \(s<1/2\), and divergence at and above the boundary because the tail is asymptotic to \(2te^{-t/2}\). The case \(s=0\) is trivial. The same bound yields all ordinary moments.

## Verification
The accompanying standalone program `scripts/check_period_law.py` symbolically checks Hamiltonian and first-integral identities, numerically checks the elliptic period and the exact probability formula against independent quadrature, and tests convergence of the two-term tail for several small \(q\). These finite checks supplement the analytic proof and are not claimed to prove asymptotic statements. Reproduce with `python scripts/check_period_law.py` in an environment with the versions stated in `requirements.txt`.

## Relationship to prior work
The 2024 model paper identifies the invariant-square family and discusses qualitative periodic dynamics of its cubic subfamily; its theorems chiefly concern limit cycles, centers and bifurcations in the broader quartic family. The zero-sum two-population Hamiltonian structure is classical (Hofbauer, 1996). An earlier published analysis of an **invariant-square quartic center**, whose degree-four vector field includes factors \(1+pX\) and \(1+qY\), already gives \(T(E)=4K(\sqrt{1-e^{-2E}})\) in its symmetric specialization. With \(E=-\tfrac12\log Q\), this is exactly the period formula used above, so it is explicitly **not** part of the claimed novelty. The present assertion concerns the **uniform-area pushforward**, exact full-period cumulative law, and the two-term tail including its moment boundary; these do not occur in the inspected earlier statements. Related 2026 research contrasts nonisochronous expected-utility matching-pennies dynamics with isochronous log-payoff dynamics; only the former is treated here. A search without a match is not proof of worldwide novelty.

## Limitations
The probability measure is uniform Euclidean area, not an invariant measure, and the dynamical system is deterministic. Results apply only to the displayed normalization of the two-strategy zero-sum center and do not extend automatically to perturbed asymmetric games, noisy replicator equations or different fitness rules. The closed-orbit period formula and qualitative Hamiltonian nature are known. Unindexed earlier calculations of this distribution remain a priority risk, and no independent mathematical audit is claimed.

## References
1. A. Gasull, L. F. S. Gouveia, and P. Santana, *On the limit cycles of a quartic model for evolutionary stable strategies*, arXiv:2410.15354v1 (posted October 20, 2024), https://arxiv.org/html/2410.15354v1.
2. J. Hofbauer, *Evolutionary dynamics for bimatrix games: A Hamiltonian system?*, J. Math. Biol. 34 (1996), 675–688, https://doi.org/10.1007/BF02409754.
3. *Universal two-term period growth in an invariant-square quartic center*, published mathematical result, October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-two-term-period-growth-in-an-invariant-square-quartic--73607523fe89.
4. J. Ruiz-Serra, N. Ay, and M. Harré, *Bayesian Replicator Dynamics and the Inversion of Strict Dominance in Bimatrix Games*, arXiv:2610.36345v1 (posted October 26, 2026), https://arxiv.org/abs/2610.36345.
