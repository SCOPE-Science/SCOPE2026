# Universal quartic environmental-mean bias in nonlinear imitation feedback cycles

## Finding

Fix \(a,\epsilon,\theta>0\), \(0<t<1\), and a \(C^5\) imitation probability \(g:\mathbb R\to(0,1)\) with \(g'(z)>0\) for all \(z\). Put \(F(z)=g(z)-g(-z)\). For the two-variable feedback dynamics
\[
\dot x=x(1-x)F(a(t-n)),\qquad
\dot n=\epsilon n(1-n)((1+\theta)x-1),
\]
every non-equilibrium trajectory starting in \((0,1)^2\) is periodic, with a unique interior equilibrium \((x_*,t)\), \(x_*=(1+\theta)^{-1}\). Every such orbit has the exact cooperation average \(\overline x=x_*\).

Let \(A=(\max n-\min n)/2\) denote the environmental half-range on a periodic orbit. As the orbit shrinks to the equilibrium (equivalently \(A\downarrow0\)), its physical-time environmental mean satisfies the universal asymptotic law
\[
\boxed{\displaystyle
\overline n-t=-\frac{a^2F'''(0)(1-2t)}{24F'(0)t(1-t)}A^4+o(A^4).}
\]
Thus, whenever \(F'''(0)(1-2t)\ne0\), sufficiently small nonconstant cycles have a strict mean-environment displacement with the stated sign, even though their cooperation mean equals equilibrium exactly. Whenever its coefficient is nonzero, the quartic term is the **first nonzero term** of the environmental-mean expansion.

For the standard Fermi imitation probability \(g(z)=(1+e^{-z})^{-1}\), so \(F(z)=\tanh(z/2)\), this reads
\[
\boxed{\displaystyle \overline n-t=\frac{a^2(1-2t)}{48t(1-t)}A^4+o(A^4).}
\]
When \(t=1/2\), symmetry forces the stronger exact identity \(\overline n=1/2\) on **every** periodic orbit, for every admissible \(g\), not just small orbits.

## Assumptions and scope

The state variables \(x,n\in(0,1)\) represent cooperation frequency and environmental quality. The payoff advantage of cooperation over defection is \(a(t-n)\) after absorbing imitation intensity into \(a\). This is realized by the strictly admissible payoff interpolation
\[
A(n)=(1-n)\begin{pmatrix}at&at\\0&0\end{pmatrix}
+n\begin{pmatrix}0&0\\a(1-t)&a(1-t)\end{pmatrix}.
\]
In particular cooperation is strictly favored in the depleted environment, and defection is strictly favored in the replete environment. The strategy payoff *difference* is independent of opponent strategy; the individual payoffs themselves are specified explicitly above. The response \(F\) is odd, strictly increasing, \(C^5\), and \(F'(0)=2g'(0)>0\). The theorem concerns the deterministic, autonomous, strictly interior system. The indicated bars are averages over one full orbit with respect to original physical time, not uniformly sampled phase or energy.

At fixed parameters, every energy above the equilibrium energy gives one periodic oval. The expansion is taken along any such ovals with environmental half-range tending to zero. No attracting limit cycle, stochastic statement, or claim about initial conditions on the boundary is made.

## Proof

**1. Global periodic foliation.** Set \(\sigma(s)=(1+e^{-s})^{-1}\), \(u=\log(x/(1-x))\), and \(v=\log(n/(1-n))\). Then
\[
\dot u=f(v):=F(a(t-\sigma(v))),\qquad
\dot v=h(u):=\epsilon((1+\theta)\sigma(u)-1).
\]
Writing \(u_*=\log(x_*/(1-x_*))\) and \(v_*=\log(t/(1-t))\), define
\[
H(u,v)=\int_{u_*}^u h(s)\,ds-\int_{v_*}^v f(s)\,ds.
\]
Its gradient is \((h(u),-f(v))\), and \((\dot u,\dot v)=(-H_v,H_u)\); hence \(\dot H=0\). Moreover \(h\) is strictly increasing with its unique zero at \(u_*\), whereas \(f\) is strictly decreasing with its unique zero at \(v_*\). Thus \(H\) is a sum of two strictly convex nonnegative single-well functions. It tends to infinity when either \(u\) or \(v\) tends to either infinity: the two limits of \(h\) are \(-\epsilon\) and \(\epsilon\theta\), and those of \(f\) are \(F(at)>0\) and \(F(-a(1-t))<0\). Consequently every positive level of \(H\) is one compact smooth closed curve, with no equilibrium on it, and is traversed periodically. Its zero level is only \((u_*,v_*)\).

**2. Exact average.** Periodicity of \(v\) gives
\[
0=\overline{\dot v}=\epsilon((1+\theta)\overline x-1),
\qquad \overline x=x_*.
\]
Periodicity of \(u\) also yields the exact nonlinear balance
\[
\overline{F(a(t-n))}=0.
\]
This last identity is not generally the same as \(\overline n=t\), because \(F\) is nonlinear.

**3. Universal cubic-moment lemma.** Put \(p=t(1-t)\), \(p_2=p(1-2t)\), \(q=x_*(1-x_*)\), and write \(U=u-u_*\), \(V=v-v_*\). Taylor expansion gives
\[
\dot U=-\alpha V-\alpha_2 V^2+O(V^3),\qquad
\dot V=\beta U+\beta_2 U^2+O(U^3),
\]
where \(\alpha=aF'(0)p\), \(\alpha_2=aF'(0)p_2/2\), \(\beta=\epsilon(1+\theta)q\), and \(\beta_2=\epsilon(1+\theta)q(1-2x_*)/2\). Write \(\omega^2=\alpha\beta>0\). Parameterize a small oval by its upper environmental turning point \(U(0)=0\), \(V(0)=\rho>0\). With a rescaled \(2\pi\)-periodic phase \(s\), the first harmonics are \(V=\rho\cos s+O(\rho^2)\) and \(U=-\omega\rho\sin s/\beta+O(\rho^2)\). At quadratic order, \(\ddot V+\omega^2V=-\beta\alpha_2V^2-2\alpha\beta_2UV+O(\rho^3)\). Consequently the constant and cosine-second-harmonic terms in \(V/\rho^2\) are respectively
\[
C_0=-\frac{\alpha_2}{2\alpha},\qquad C_2=\frac{\alpha_2}{6\alpha}.
\]
A sine-second-harmonic term, and homogeneous first harmonics fixed by the initial conditions, make no contribution to the fourth-order cubic moment. As \(n-t=pV+(p_2/2)V^2+O(\rho^3)\), averaging the cube and using \(\langle\cos^2s\rangle=1/2\), \(\langle\cos^2s\cos2s\rangle=1/4\), \(\langle\cos^4s\rangle=3/8\) gives
\[
\overline{(n-t)^3}
=3p^2\rho^4\left[p(C_0/2+C_2/4)+\frac{3p_2}{16}\right]+O(\rho^5)
=\frac{p^2p_2}{4}\rho^4+O(\rho^5).
\]
The environmental half-range is \(A=p\rho+O(\rho^2)\), so
\[
\overline{(n-t)^3}=\frac{1-2t}{4t(1-t)}A^4+o(A^4).
\]
Smooth small-oval parameterization and time rescaling justify the uniform remainder; the quadratic forcing contains no resonant fundamental, so no first-order frequency correction affects this coefficient. In particular the moment coefficient is independent of \(\epsilon\), \(\theta\), and the higher derivatives of \(F\).

**4. Environmental bias and exact symmetric exception.** Oddness and \(C^5\) regularity yield \(F(z)=F'(0)z+F'''(0)z^3/6+O(z^5)\). Applying the exact balance from step 2 to \(z=-a(n-t)\), and using \(\max|n-t|=O(A)\) for shrinking ovals, gives
\[
\overline n-t=-\frac{a^2F'''(0)}{6F'(0)}\overline{(n-t)^3}+O(A^5),
\]
which, with step 3, is the asserted coefficient. For the Fermi response, \(F'(0)=1/2\) and \(F'''(0)=-1/4\), yielding its stated positive or negative formula.

If \(t=1/2\), then \(v_*=0\) and \(f(-v)=-f(v)\), since both \(F\) and \(\sigma(v)-1/2\) are odd. The Hamiltonian \(H(u,v)\) is even in \(v\), and reflection \((u,v)\mapsto(u,-v)\) reverses time on each invariant oval. Equal-time pairing gives \(\overline{\sigma(v)}=\overline{\sigma(-v)}=1-\overline{\sigma(v)}\), so \(\overline n=1/2\) exactly.

## Verification

The standalone \(\texttt{verify.py}\) checks the Taylor and second-harmonic algebra with SymPy, then numerically integrates complete periods with high-tolerance adaptive integration for six parameter/response families and three small amplitudes each. It tests Fermi and modified bounded monotone response functions
\[
F_\lambda(z)=\frac{\tanh(z/2)+\lambda\tanh^3(z/2)}{1+\lambda},\quad \lambda\in\{0,1\},
\]
which arise from valid imitation probabilities \(g_\lambda=(1+F_\lambda)/2\). Their derivative ratios satisfy \(F_\lambda'''(0)/F_\lambda'(0)=(3\lambda-1)/2\), making the predicted bias reverse sign when \(\lambda\) goes from zero to one. For example, with \(t=1/4\), \(a=4\), and Fermi imitation, the predicted coefficient is \(8/9\); the observed ratio \((\overline n-t)/A^4\) is approximately \(0.8887\) at environmental half-range \(0.02844\). Numerical integration is a consistency check, not a proof for all cycles or a substitute for the analytic expansion. Run \(\texttt{python verify.py}\) with the listed packages installed.

## Relationship to prior work

Liu, Cao and Wu (2022), Section 2 and Section 3.4/Appendix F, introduce general nonlinear imitation in precisely this strategy-environment feedback setting. They derive the exact cooperation mean and describe the environment mean as approximately equal to equilibrium; their Appendix F converts a zero mean nonlinear payoff response into a zero mean raw payoff difference. That implication does not hold for general nonlinear \(F\). The contribution here is the precise nonzero fourth-order difference and its response-curvature sign law for a natural payoff-independent-composition subclass, plus a complete neutral periodic foliation for that subclass. Their existence of attracting/repelling isolated cycles under strict inequalities addresses different parameter regimes and does not imply this coefficient.

Weitz and collaborators (2016), especially their Eq. (17) and discussion of a first integral, already establish closed neutral cycles for a symmetrically balanced **linear-replicator** game with equilibrium environment \(1/2\); that classical periodic-foliation phenomenon is not claimed here as new. Their system has a linear payoff response and the symmetric environmental mean, neither of which supplies the asymmetric fourth-order mean bias for nonlinear imitation. A later global classification for a two-community environmental game likewise concerns a different number of environmental coordinates and linear replicator response, not this curvature-dependent single-environment statistic.

## Limitations

This is a theorem about deterministic autonomous two-dimensional feedback dynamics with strategy-independent payoff *differences*. The general model with payoff differences depending on strategy frequency need not be integrable, and no global cycle-mean law for that wider model is asserted. The coefficient vanishes when \(t=1/2\) or \(F'''(0)=0\); in the latter case a higher-order law would require further analysis and is not claimed. For \(t\ne1/2\) and nonzero \(F'''(0)\), strict bias is proved only for sufficiently small nontrivial ovals. No physical calibration, stochastic finite-population inference, or global sign of bias for arbitrary large cycles is established. The literature comparison cannot exclude unindexed equivalent formulations or later independent derivations; external mathematical validation is not performed.

## References

1. Y. Liu, L. Cao and B. Wu, *General non-linear imitation leads to limit cycles in eco-evolutionary dynamics*, arXiv:2210.10552, first public version October 19, 2022; *Chaos, Solitons & Fractals* 165 (2022), 112817, https://arxiv.org/abs/2210.10552 . Specifically Section 2, Sections 3.1–3.4 and Appendix F.
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown and W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, *PNAS* 113 (2016), E7518–E7525, https://doi.org/10.1073/pnas.1604096113 . Especially Eq. (17) and the neutral-periodic discussion.
3. A. R. Tilman, J. B. Plotkin and E. Akçay, *Evolutionary games with environmental feedbacks*, *Nature Communications* 11 (2020), 915, https://doi.org/10.1038/s41467-020-14531-6 . Background on wider payoff-environment coupling.
