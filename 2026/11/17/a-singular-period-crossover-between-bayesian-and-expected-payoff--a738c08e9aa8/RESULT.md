# A singular period crossover between Bayesian and expected-payoff cycles

## Finding

Consider the normalized interpolation between the logarithmic-evidence and expected-utility replicator dynamics of unbiased Matching Pennies. For every mixing weight \(0\leq\theta\leq1\), set
\[
f_\theta(z)=(1-\theta)z+2\theta\tanh(z/2),\qquad
F_\theta(z)=\frac{1-\theta}{2}z^2+4\theta\log\cosh(z/2).
\]
The planar dynamics in log-odds coordinates is
\[
\dot v=f_\theta(w),\qquad \dot w=-f_\theta(v),
\quad H_\theta(v,w)=F_\theta(v)+F_\theta(w).
\]
For each \(E>0\), the level \(H_\theta=E\) is one periodic orbit. Let \(T_\theta(E)\) denote its least positive physical-time period. The following statements hold.

1. For \(\theta=0\), \(T_0(E)=2\pi\) for all \(E>0\). For every \(0<\theta\leq1\), \(T_\theta(E)\) is **strictly increasing** on \((0,\infty)\), with the local expansion
\[
T_\theta(E)=2\pi\left(1+\frac{\theta}{8}E+O_\theta(E^2)\right)
\quad(E\downarrow0).
\]
2. For every fixed \(0\leq\theta<1\),
\[
\lim_{E\to\infty}T_\theta(E)=\frac{2\pi}{1-\theta};
\]
whereas at the expected-utility endpoint,
\[
\lim_{E\to\infty}\frac{T_1(E)}{E}=1.
\]
3. More sharply, write \(\varepsilon=1-\theta\). For **every fixed \(e>0\)**,
\[
\boxed{\lim_{\varepsilon\downarrow0}
\varepsilon T_{1-\varepsilon}\left(\frac e\varepsilon\right)
=\mathcal P(e):=8\arctan\sqrt{1+\frac e2}-2\pi.}
\]
The crossover is nonconstant: \(\mathcal P(e)=e+O(e^2)\) as \(e\downarrow0\) and \(\mathcal P(e)\to2\pi\) as \(e\to\infty\). Thus an arbitrarily small logarithmic-evidence component bounds the high-energy period, but the bound is reached only beyond an energy scale of order \((1-\theta)^{-1}\). The formula gives the complete leading crossover profile at that scale.

## Assumptions and scope

Use the zero-sum Matching Pennies matrices \(A=\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)\) and \(B=-A^{\mathsf T}\). For a player facing a mixed-strategy vector \(y\), form its fitness vector from \(\theta Ay+(1-\theta)A\log y/2\), with the logarithm applied coordinatewise; for the opponent use the analogous formula with \(B\) and \(x\). This normalization makes both endpoint flows have unit linear frequency at the mixed equilibrium. For strictly interior strategy probabilities, the log odds \(v=\log(x_1/x_2)\), \(w=\log(y_1/y_2)\) satisfy the displayed system exactly. No claims are made for boundary probabilities at which a logarithm is undefined. The family is a defined interpolation, not an empirically fitted Bayesian learning mechanism. Time is the autonomous differential-equation time, and energy is the explicit \(H_\theta\), with no arbitrary additive shift.

The conclusions cover every \(\theta\in[0,1]\) and \(E>0\), with the order of limits exactly as stated. Uniformity of the joint crossover is asserted only along sequences \(\varepsilon\downarrow0\) with \(\varepsilon E\to e\in(0,\infty)\), not at \(e=0\) or \(e=\infty\).

## Proof

**1. Hamiltonian and orbit geometry.** Subtracting the two fitness components of each player gives \(\dot v=(1-\theta)w+2\theta\tanh(w/2)\) and \(\dot w=-(1-\theta)v-2\theta\tanh(v/2)\). Since \(F_\theta'=f_\theta\), \(H_\theta\) is conserved. Moreover
\[
F_\theta''(z)=1-\theta+\theta\operatorname{sech}^2(z/2)>0,
\]
and \(F_\theta\) is even, strictly increasing on the positive half-line, and tends to infinity. Each positive energy level is therefore a smooth strictly convex oval enclosing the sole equilibrium. Its vector field is nonzero and tangent to the oval, so it is a periodic orbit with a well-defined least period.

**2. Exact angular representation and strict increase.** Write \((v,w)=r(\cos\phi,\sin\phi)\). At energy \(E>0\), the unique radial intersection \(r=r_\theta(E,\phi)>0\) is strictly increasing with \(E\) at every angle. The clockwise angular speed is
\[
\Omega_\theta(r,\phi)=
\frac{\cos\phi\,f_\theta(r\cos\phi)+\sin\phi\,f_\theta(r\sin\phi)}{r}
=(1-\theta)+\theta\sum_{u\in\{\cos\phi,\sin\phi\}}
 u^2 Q(ru),
\]
where \(Q(z)=2\tanh(z/2)/z\) for \(z\ne0\), \(Q(0)=1\). The function \(Q\) is strictly decreasing in \(|z|>0\): for \(t>0\), \(\tanh t-t\operatorname{sech}^2t>0\), as its derivative is \(2t\operatorname{sech}^2t\tanh t>0\) and it vanishes at zero. Hence for every \(\theta>0\) the angular speed decreases strictly when \(r\) increases. The period identity
\[
T_\theta(E)=\int_0^{2\pi}
\frac{d\phi}{\Omega_\theta(r_\theta(E,\phi),\phi)}
\]
proves strict period increase, while \(\theta=0\) gives \(\Omega_0\equiv1\). Taylor expansion \(f_\theta(z)=z-\theta z^3/12+O_\theta(z^5)\), together with \(r_\theta(E,\phi)^2=2E+O_\theta(E^2)\) and \(\int_0^{2\pi}(\cos^4\phi+\sin^4\phi)\,d\phi=3\pi/2\), yields the stated local coefficient \(\theta/8\).

**3. Fixed-parameter large-energy laws.** For \(0\leq\theta<1\), \(f_\theta(z)/z\to1-\theta\) as \(|z|\to\infty\). Every radial level radius tends to infinity as \(E\to\infty\), uniformly in angle. Since \(1-\theta\leq\Omega_\theta\leq1\), dominated convergence in the angular formula gives \(T_\theta(E)\to2\pi/(1-\theta)\). At \(\theta=1\), rescale \(V=v/E\), \(W=w/E\), and \(s=t/E\). The rescaled energy \(H_1(EV,EW)/E\) converges uniformly on compact sets to \(2(|V|+|W|)\); the rescaled vector field converges away from the coordinate axes to \((2\operatorname{sgn}W,-2\operatorname{sgn}V)\). The limiting level is the diamond \(|V|+|W|=1/2\). Each of its four side arcs is traversed in \(1/4\) unit of \(s\)-time. The crossings of the axes are transverse, and the period convergence follows also by dominated convergence in polar angle: the level radius remains uniformly bounded above and below, and the angular speed is bounded away from zero for sufficiently large \(E\). Thus \(T_1(E)/E\to1\).

**4. The singular crossover.** Put \(\theta=1-\varepsilon\), \(V=\varepsilon v\), \(W=\varepsilon w\), and \(s=\varepsilon t\). The scaled energy at \(E=e/\varepsilon\) is exactly
\[
\mathscr H_\varepsilon(V,W)=G_\varepsilon(V)+G_\varepsilon(W)=e,
\quad G_\varepsilon(z)=\frac{z^2}{2}+4\varepsilon(1-\varepsilon)
\log\cosh\!\left(\frac{z}{2\varepsilon}\right).
\]
The evolution in \(s\)-time is
\[
V'=g_\varepsilon(W),\qquad W'=-g_\varepsilon(V),
\quad g_\varepsilon(z)=z+2(1-\varepsilon)\tanh\!\left(\frac z{2\varepsilon}\right).
\]
For fixed \(e>0\), \(G_\varepsilon\to G_0(z)=z^2/2+2|z|\) locally uniformly, because \(|\log\cosh u-|u||\leq\log2\). Thus the strictly star-shaped energy level has a radial parametrization converging uniformly to that of \(G_0(V)+G_0(W)=e\). The scaled angular speed is \([Vg_\varepsilon(V)+Wg_\varepsilon(W)]/(V^2+W^2)\geq1\); at every fixed angle it converges to the corresponding speed for \(g_0(z)=z+2\operatorname{sgn}z\) away from zero (the products \(zg_0(z)\) extend continuously at zero). The angular period formula and dominated convergence imply \(\varepsilon T_{1-\varepsilon}(e/\varepsilon)\to T_{\mathrm{lim}}(e)\).

In the first quadrant, the limiting equations are \(V'=W+2\), \(W'=-(V+2)\): a circular arc about \((-2,-2)\) of angular velocity one. Each positive axis intercept is \(a_e=\sqrt{4+2e}-2\). The transit from \((0,a_e)\) to \((a_e,0)\) has angular duration
\[
\Delta(e)=\arctan\frac{a_e+2}{2}-\arctan\frac{2}{a_e+2}
=2\arctan\sqrt{1+e/2}-\frac\pi2.
\]
There are four congruent arcs, so \(T_{\mathrm{lim}}(e)=4\Delta(e)=8\arctan\sqrt{1+e/2}-2\pi\). Elementary expansions at zero and infinity give the asserted crossover endpoints. If \(\varepsilon E\to e>0\) rather than being identically \(e\), the same convergence follows from uniform convergence of energy levels in a compact neighborhood of \(e\). This proves the theorem.

## Verification

A standalone standard-library checker, `verify_period.py`, numerically integrates the *exact* angular-period formula on Hamiltonian levels. It compares monotonicity across 5 parameters, the small-energy coefficients at 3 parameters, the singular crossover at 4 scaled energies for two small mixing weights, and the large-energy laws at 3 cases. Run `python3 verify_period.py`. The expected final line is `VERIFY_OK strict_period_cases=5 small_energy_checks=3 crossover_parameters=4 high_energy_cases=3`. These are corroborative finite tests, not a proof of the continuum claims. All infinite statements are established analytically above.

## Relationship to prior work

Ruiz-Serra, Ay and Harré (first posted 2026-10-26) derive the linear- versus logarithmic-fitness Matching Pennies centers, including the constant logarithmic-fitness period and the qualitative growth of the expected-utility period near the strategy boundary. Their results supply the two natural endpoints and the interpretation of the payoff interpolation. The present result concerns a *normalized mixture of those fitness functions* and derives its global strict monotonicity, high-energy plateau and exact singular crossover profile. General criteria for monotonic periods of separable planar Hamiltonians are well established (Chicone; Villadelprat and Zhang; Nascimento); no originality is claimed for such general monotonicity criteria. The parameter-dependent closed crossover formula is a distinct calculation for the above mixed-payoff family. A historical priority check is not a proof of uniqueness; uninspected older separable-Hamiltonian literature remains a limitation.

## Limitations

The interpolation is defined for this symmetric zero-sum two-action game, with a specific normalization of the log-fitness contribution. It does not imply the same crossover for biased games, higher-dimensional games, or stochastic learning. The joint limit requires \(\varepsilon E\) to remain in a compact positive range; it is not a uniform relative-error approximation down to zero scaled energy. The statistical meaning of mixed fitness is a modeling choice, not an experimentally validated claim. The numerical checker samples finitely many parameters and cannot certify the infinite-domain proof or historical novelty. No independent scientific audit has been performed.

## References

- J. Ruiz-Serra, N. Ay and M. Harré, *Bayesian Replicator Dynamics and the Inversion of Strict Dominance in Bimatrix Games*, arXiv:2610.36345v1, first public posting 2026-10-26, https://arxiv.org/abs/2610.36345 . Relevant sections II.1–II.2 and III.4, especially Corollary III.2 and Remark III.3.
- F. J. S. Nascimento, *Monotonicity of the Period Function in Planar Separable Hamiltonian Systems: An Extension of Chicone’s Criterion*, *Qualitative Theory of Dynamical Systems* 25 (2026), article 166, https://doi.org/10.1007/s12346-026-01595-w . Particularly Theorem 1.1, examples and comparison section.
- J. Villadelprat and X. Zhang, *The Period Function of Hamiltonian Systems with Separable Variables*, *Journal of Dynamics and Differential Equations* 32 (2020), 741–767, https://doi.org/10.1007/s10884-019-09759-w . The accessible abstract and introductory preview were consulted; full text was not available for detailed comparison.
- C. Chicone, *The monotonicity of the period function for planar Hamiltonian vector fields*, *Journal of Differential Equations* 69 (1987), 310–321.
