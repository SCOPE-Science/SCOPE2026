# Sharp nine-equilibrium and four-sink bounds in a heterogeneous neuron chain

## Finding
For the six-dimensional Chialvo–Rulkov–Chialvo map defined below, every parameter choice in the stated positive-feedback class has at most **nine distinct real fixed points and four hyperbolic attracting fixed points**. Both bounds are attained simultaneously, with all nine fixed points in the strictly positive orthant and all four couplings strictly positive, at the explicit rational parameters in the Verification section. In fact, that example has exactly four hyperbolic sinks and five unstable hyperbolic fixed points. The bounds persist as achieved values on a nonempty open neighborhood of that parameter vector.

## Assumptions and scope
Let the state, in order, be \((x_1,y_1,x_2,y_2,x_3,y_3)\in\mathbb R^6\). Consider the map
\[
\begin{aligned}
x_1'&=x_1^2 e^{y_1-x_1}+k_0+s_1(x_2-x_1),&y_1'&=ay_1-bx_1+c,\\
x_2'&=\frac{\alpha}{1+x_2^2}+y_2+t_1(x_1-x_2)+t_3(x_3-x_2),&y_2'&=y_2-\mu(x_2-\gamma),\\
x_3'&=x_3^2 e^{y_3-x_3}+k_0+s_3(x_2-x_3),&y_3'&=ay_3-bx_3+c.
\end{aligned}
\]
Assume \(0<a<1\), \(b\geq0\), \(\mu>0\), \(\gamma>0\), \(k_0>0\), \(\alpha>0\), \(s_1,s_3>0\) and \(t_1,t_3>0\); \(c\) is real. A *sink* means every eigenvalue of the full six-dimensional Jacobian has modulus strictly below one. The upper bounds count all real fixed points, regardless of the signs of recovery coordinates; the attaining witness has all six coordinates strictly positive. No global attraction claim is made.

Put \(K=1+b/(1-a)\), \(C=c/(1-a)\) and, for \(i=1,3\),
\[
 A_i=\frac{e^C}{1+s_i},\quad d_i=\frac{k_0+s_i\gamma}{1+s_i},\quad
 G_i(x)=x-A_ix^2e^{-Kx}.
\]
Each \(d_i>0\). The number of fixed points is exactly the product of the numbers of positive roots of \(G_1(x)=d_1\) and \(G_3(x)=d_3\). In particular, it is at most nine. More explicitly, set
\[
 A_{*,i}=\frac{K e^{2-\sqrt2}}{2(\sqrt2-1)}.
\]
If \(A_i\le A_{*,i}\), there is one distinct positive root. Otherwise, let \(r_i^-<r_i^+\) be the two positive roots of \(G_i'(x)=0\), with \(r_i^-\) the local maximum and \(r_i^+\) the local minimum, and set \(U_i=G_i(r_i^-)\), \(L_i=G_i(r_i^+)\). There are three distinct roots exactly when \(L_i<d_i<U_i\); there are two at either fold equality \(d_i=U_i\) or \(d_i=L_i>0\); otherwise there is one. A fold root is counted once. Only roots on strictly increasing branches of \(G_i\) can belong to hyperbolic sinks, yielding the four-sink bound.

## Proof
**1. Exact reduction and root census.** The fixed recovery equation for the middle neuron gives \(x_2=\gamma\). The outer recovery equations give \(y_i=C-bx_i/(1-a)\). Substitution into each outer voltage equation yields \(G_i(x_i)=d_i\). Because \(x_i^2e^{y_i-x_i}\ge0\), every fixed point has \(x_i>0\), and conversely each positive root pair uniquely determines a full fixed point via
\[
 y_2=\gamma-\frac\alpha{1+\gamma^2}-t_1(x_1-\gamma)-t_3(x_3-\gamma).
\]
For \(x>0\), \(G_i'(x)=1-A_i x(2-Kx)e^{-Kx}\). The positive function \(h(x)=x(2-Kx)e^{-Kx}\) is positive only on \((0,2/K)\), where it has a unique maximum \(2(\sqrt2-1)e^{\sqrt2-2}/K\) at \((2-\sqrt2)/K\). Thus \(G_i'\) has at most two positive zeros. Since \(G_i(0)=0<d_i\) and \(G_i(x)\to\infty\), the stated one-/two-/three-root classification follows by monotonicity and tangency.

**2. Spectral obstruction for a decreasing scalar branch.** At a fixed point let \(Y_i=x_i^2e^{y_i-x_i}\), \(J_i=Y_i(2/x_i-1)-s_i\), and define
\[
 Q_i(\lambda)=(\lambda-J_i)(\lambda-a)+bY_i,\qquad
 Q_2(\lambda)=(\lambda-r)(\lambda-1)+\mu,
\]
where \(r=-2\alpha\gamma/(1+\gamma^2)^2-t_1-t_3\). Direct block elimination gives the exact characteristic identity
\[
 \det(\lambda I-D F)=Q_1Q_2Q_3
 -(\lambda-a)(\lambda-1)[s_1t_1Q_3+s_3t_3Q_1].\tag{1}
\]
The identity holds for all complex \(\lambda\), without division by any polynomial. At \(\lambda=1\),
\[
 Q_i(1)=(1-a)(1+s_i)G_i'(x_i),\qquad Q_2(1)=\mu.\tag{2}
\]
A fold has a unit eigenvalue by (1)–(2). If exactly one outer root lies on a decreasing branch, (1)–(2) give \(\det(I-DF)<0\). The characteristic polynomial is monic of degree six, so it has a real root greater than one.

If *both* outer roots lie on decreasing branches, each quadratic \(Q_i\) has exactly one real root \(\lambda_i>1\), since \(Q_i(1)<0\) and \(Q_i(\lambda)\to\infty\). At the larger of \(\lambda_1,\lambda_3\), either both quadratics vanish, giving an eigenvalue greater than one in (1), or precisely one vanishes while the other is positive; then (1) is negative because the corresponding couplings are positive. Again a real eigenvalue greater than one exists. Hence no hyperbolic sink includes a decreasing-branch root. Each \(G_i\) has at most two roots on increasing branches, so there are at most four sinks, independent of the inward coupling strengths.

**3. Sharp simultaneously attaining example.** Take
\[
 a=\frac45,\ b=\frac1{10},\ c=\frac12,\ k_0=\frac1{1000},\quad
 \gamma=1,\ \alpha=\frac12,\ \mu=\frac1{10},\quad
 s_1=s_3=\frac1{1000},\quad t_1=t_3=\frac1{10^6}.
\]
Here \(K=3/2\), \(C=5/2\), and both outer root equations coincide:
\[
 x-\frac{1000}{1001}x^2e^{5/2-3x/2}=\frac2{1001}.
\]
An exact rational certificate (see Verification and `check.py`) encloses its three simple positive roots in the disjoint intervals
\[
(0.002048938,0.002048940),\qquad
(0.092330362,0.092330364),\qquad
(2.188864390,2.188864392).
\]
Their crossing signs alternate, and step 1 excludes any further roots. The three pairings yield nine distinct fixed points, all with positive recovery coordinates (the outer recovery value is \(5/2-x/2>1.4\), and the middle recovery lies between \(0.749997\) and \(0.750003\)).

To certify the full six-dimensional spectra, first set only \(t_1=t_3=0\), leaving the outer couplings \(s_i=1/1000\) intact. The Jacobian becomes block triangular. Using exact rational interval arithmetic from the root enclosures, the two eigenvalues of each low-branch outer block lie in \((0,0.1)\) and \((0.7,0.8)\); those of the middle-branch block lie in \((0.8,0.82)\) and \((1.8,1.9)\); and both high-branch eigenvalues lie in \((0,0.7)\). The middle Rulkov block has eigenvalues in \((-0.2,-0.15)\) and \((0.9,0.92)\). Thus four root pairings are sinks and five are not.

Let \(Q_2^0(\lambda)=\lambda^2-3\lambda/4-3/20\). For any of the nine equilibria, adding \(t_1=t_3=\tau\) leaves \(Q_1,Q_3\) unchanged and transforms (1) *exactly* into
\[
 P_\tau(\lambda)=Q_1Q_3Q_2^0+2\tau(\lambda-1)Q_1Q_3
 -\frac\tau{1000}(\lambda-a)(\lambda-1)(Q_1+Q_3).
\]
On \(|\lambda|=1\), the preceding rigorous eigenvalue intervals give \(|Q_1|,|Q_3|\ge0.09\), \(|Q_1|,|Q_3|\le5.3\), and \(|Q_2^0|\ge0.064\). Therefore
\[
 |P_0|\ge0.0005184,\qquad
 |P_\tau-P_0|\le112.39816\tau.
\]
At \(\tau=10^{-6}\) the second bound is \(0.00011239816\), strictly smaller. Rouché's theorem preserves the exact count of eigenvalues inside the unit disk for **each of the nine** full coupled Jacobians. Consequently exactly four of the nine full fixed points are hyperbolic sinks and the other five are unstable. All inequalities are strict, so the same nine/four configuration persists on an open set of nearby positive parameters.

## Verification
Run `python check.py` using Python 3. The checker uses exact rational arithmetic, no numerical root solver, and Taylor intervals for the exponential with a conservative remainder bound \(21\cdot3^{61}/61!\) whenever the exponent has absolute value at most three (using \(e^3<21\)). It checks alternating endpoint signs, disjoint root intervals, the low/middle/high quadratic eigenvalue bounds, and the explicit Rouché inequality \(0.00011239816<0.0005184\). The proof of the spectral identity and root-count bound is in the previous section; the checker independently verifies the exact rational inequalities needed at the displayed witness.

## Relationship to prior work
Ghosh, Nair, Fatoyinbo and Muni (2024) introduce this precise six-dimensional chain and display the fixed-point equations and numerical eigenvalue continuation. Their formulas already imply the scalar decoupling after fixing the middle activation, so that reduction alone is **not claimed as novel**. The contribution here is the complete positive-parameter nine-root bound with fold criteria, the nontrivial **global four-sink ceiling**, and an exact rational parameter certificate attaining both bounds in a fully bidirectionally coupled, positive-state chain. Their reported numerical scan encountered no stable equilibria in its chosen parameter region; that scan does not cover the present region. A same-author study of a Chialvo-only higher-order ring-star network uses different node dynamics and topology, and does not imply this chain's bounds. Related standalone Chialvo and Rulkov fixed-point calculations do not establish the coupled-network ceiling.

## Limitations
The theorem is about the **number and local hyperbolic stability** of equilibria, not all nonlinear attractors, basins, or biological realism of the example. The return couplings in the certified witness are small but strictly positive, and open parameter robustness is proved rather than asserted from floating-point continuation. The four-sink bound is a necessary obstruction and does not give a complete stability phase diagram for arbitrary parameters. Novelty remains subject to comparison with any unindexed equivalent equilibrium-census theorem.

## References
1. I. Ghosh, A. S. Nair, H. O. Fatoyinbo and S. S. Muni, *Dynamical properties of a small heterogeneous chain network of neurons in discrete time*, first posted 2024-05-09, arXiv:2405.05675, https://arxiv.org/abs/2405.05675; open-access full text, *European Physical Journal Plus* 139, 545 (2024), https://doi.org/10.1140/epjp/s13360-024-05363-0, particularly Sections 3–5.
2. A. S. Nair, I. Ghosh, H. O. Fatoyinbo and S. S. Muni, *On the higher-order smallest ring-star network of Chialvo neurons under diffusive couplings*, first posted 2024-05-09, arXiv:2405.06000, https://arxiv.org/abs/2405.06000. Distinct Chialvo-only network.
