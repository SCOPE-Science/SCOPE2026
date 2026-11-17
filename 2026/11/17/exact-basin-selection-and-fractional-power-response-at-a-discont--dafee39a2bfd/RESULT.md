# Exact basin selection and fractional-power response at a discontinuous logistic border

## Finding

For the density-dependent dispersal map introduced by Morozov, Almutairi, Petrovskii and Lai, fixing the logistic growth parameter at the natural switching–maximum coincidence \(\mu=2\) makes the complete attraction basins exactly solvable. For every \(0<\varepsilon<1/2\) there are two attracting positive fixed states, and the upper-state basin has length \(\frac12\sqrt{\varepsilon/(1+\varepsilon)}\). Under a uniform initial-state distribution, this generates an exact fractional-power contribution of order \(\varepsilon^{3/2}\) to the mean selected equilibrium, and variance of order \(\varepsilon^{5/2}\).

**Complete classification.** Write
\[
L=\frac{1-2\varepsilon}{2(1-\varepsilon)},\qquad
U=\frac{1+2\varepsilon}{2(1+\varepsilon)},\qquad
c=\frac{1+\sqrt{\varepsilon/(1+\varepsilon)}}2.
\]
For all initial states \(x_0\in[0,1]\), the following mutually exclusive cases exhaust the possibilities:

| Initial state | Limit |
|---|---|
| \(0\) or \(1\) | \(0\) |
| \(\frac12\) or \(c\) | \(\frac12\) |
| \(\frac12<x_0<c\) | \(U\) |
| \(0<x_0<\frac12\) or \(c<x_0<1\) | \(L\) |

The two nonzero equilibria \(L,U\) are hyperbolically attracting with multipliers \(2\varepsilon\) and \(-2\varepsilon\), respectively. The switching point \(1/2\) is a fixed point by the stated sign convention but is not attracting. There are no nonfixed periodic orbits.

If \(X_0\) is uniform on \([0,1]\), the limit random variable \(X_\infty=\lim_{n\to\infty}H_\varepsilon^n(X_0)\) has distribution
\[
(1-p_\varepsilon)\delta_L+p_\varepsilon\delta_U,\quad
p_\varepsilon=\frac12\sqrt{\frac{\varepsilon}{1+\varepsilon}}.
\]
Its exact mean and variance are
\[
\begin{aligned}
\mathbb E[X_\infty]&=\frac{1-2\varepsilon}{2(1-\varepsilon)}+\frac{\varepsilon^{3/2}}{2(1-\varepsilon^2)\sqrt{1+\varepsilon}},\\
\operatorname{Var}(X_\infty)&=p_\varepsilon(1-p_\varepsilon)\frac{\varepsilon^2}{(1-\varepsilon^2)^2}.
\end{aligned}
\]
In particular, as \(\varepsilon\downarrow0\),
\[
\mathbb E[X_\infty]=\frac12-\frac\varepsilon2+\frac{\varepsilon^{3/2}}2+O(\varepsilon^2),\qquad
\operatorname{Var}(X_\infty)=\frac12\varepsilon^{5/2}+O(\varepsilon^3).
\]
The fractional terms express the opening of a basin of length proportional to \(\sqrt\varepsilon\) while the fixed-state separation is proportional to \(\varepsilon\).

## Assumptions and scope

Let \(F(x)=2x(1-x)\) and define
\[
H_\varepsilon(x)=\max\bigl\{0,F(x)[1+\varepsilon\operatorname{sgn}(x-F(x))]\bigr\},\quad x\in[0,1],\quad 0<\varepsilon<1/2.
\]
The sign convention is \(\operatorname{sgn}(0)=0\). On this state space, \(F(x)\ge0\) and the clipping operation is inactive. The assertions concern every deterministic initial state and, separately, the distribution selected from a uniform initial state; they do not concern transient duration, parameter noise, or arbitrary logistic growth \(\mu\). The parameter \(\varepsilon\) is the dispersal strength. The endpoints \(\varepsilon=0\) and \(\varepsilon=1/2\) are not part of the main theorem.

## Proof

**1. Exactly two smooth branches and the switching state.** For \(0<x<1\),
\[
x-F(x)=x(2x-1).
\]
Consequently \(H_\varepsilon(x)=a x(1-x)\) on \((0,1/2)\), \(H_\varepsilon(x)=b x(1-x)\) on \((1/2,1)\), with \(a=2(1-\varepsilon)\in(1,2)\) and \(b=2(1+\varepsilon)\in(2,3)\). At \(x=1/2\), the sign vanishes and \(H_\varepsilon(1/2)=1/2\). Both \(0\) and \(1\) map to zero.

**2. Lower half is invariant and globally attracted to \(L\).** The lower branch \(f(x)=ax(1-x)\) is strictly increasing on \((0,1/2)\) and \(0<f(x)<a/4<1/2\). Its only strictly positive fixed point is \(L=1-1/a\in(0,1/2)\). The exact identity is
\[
f(x)-x=a x(L-x).
\]
As \(f\) increases, initial states below \(L\) increase while staying below \(L\); those above decrease while staying above. Their limits must be fixed, hence equal \(L\).

**3. Exact upper half trapping cutoff.** The decreasing upper branch \(g(x)=bx(1-x)\) satisfies \(g(c)=1/2\) for the unique \(c\in(1/2,1)\) given above. Thus \((c,1)\) maps in one step into \((0,1/2)\). For \(1/2<x<c\),
\[
\frac12<g(x)<g(1/2)=\frac{1+\varepsilon}{2}<c.
\]
The last strict inequality follows from \(\sqrt{\varepsilon/(1+\varepsilon)}>\varepsilon\), equivalent to \(1>\varepsilon+\varepsilon^2\), valid for \(0<\varepsilon<1/2\). Therefore \((1/2,c)\) is invariant.

**4. All trapped upper states converge to \(U\).** The upper branch has unique positive fixed point \(U=1-1/b\in(1/2,c)\). Direct algebra yields
\[
g(g(x))-x=-x(bx-b+1)\bigl(b^2x^2-b(b+1)x+b+1\bigr).
\]
The discriminant of the quadratic factor is \(b^2(b+1)(b-3)<0\) for \(2<b<3\). Hence within the invariant interval the unique fixed point of \(g^2\) is \(U\). Since \(g^2\) is increasing on \((1/2,c)\), its iterates from any starting point are monotonic from the first step onward and bounded in the interval closure. The limit cannot equal an endpoint because \(g^2(1/2)\in(1/2,c)\) and \(g^2(c)=g(1/2)\in(1/2,c)\), and thus must equal \(U\). The odd subsequence also tends \(g(U)=U\). Equivalently the multiplier is \(g'(U)=2-b=-2\varepsilon\) with absolute value below one.

**5. Exhaustion and periodic exclusion.** The threshold state \(c\) maps to the fixed switch state \(1/2\). All other states either belong to an invariant basin immediately or enter the lower basin after one step. Thus all forward trajectories converge and no distinct prime-period orbit can exist. The lower fixed-state multiplier is \(f'(L)=2-a=2\varepsilon\), as claimed.

**6. Exact selection measure and asymptotics.** The upper basin is exactly the interval \((1/2,c)\) with Lebesgue measure \(c-1/2\); the four special states and endpoints have zero Lebesgue measure. The upper-state selection probability is consequently \(p_\varepsilon=c-1/2\) and its complement selects \(L\). Direct subtraction gives
\[
U-L=\frac{\varepsilon}{1-\varepsilon^2},
\]
so the two-atom expectation and variance follow from their elementary definitions. Expanding their exact formulas at \(\varepsilon=0^+\) gives the displayed \(\varepsilon^{3/2}\) and \(\varepsilon^{5/2}\) laws. No numerical extrapolation is used for those exponents.

## Verification

The standalone `verify_discontinuous_logistic.py` uses SymPy to check both fixed-point identities, the one-step threshold identity, exact second-iterate factorization and discriminant, multipliers and the square-root cutoff. It separately checks 995 selected initial states across five rational strengths by exact startup iteration followed by floating-point diagnostics (this numerical component does not establish the infinite theorem). The rational witness \(\varepsilon=1/8\) has \(c=2/3\), \(L=3/7\), \(U=5/9\), and upper basin length \(1/6\). Reproduce with `python verify_discontinuous_logistic.py` in an environment with SymPy installed. Only the analytic argument above proves the classification for all states and all strengths in the open parameter interval.

## Relationship to prior work

Morozov, Almutairi, Petrovskii and Lai (2023), Section 2.1, supply exactly this sign-of-density-change dispersal map, and Sections 3.1 and Appendix A discuss numerous transients and trapping mechanisms, especially for logistic growth near \(\mu=4\). Their Appendix A gives escape/trapping inequalities for a three-step itinerary near the switching set, but not an all-initial-state exact basin partition, its uniform-selection law, or the singular mean coefficient at \(\mu=2\). The present result is a specific solvable border-critical specialization of their model; the general model and transient mechanism are not new. Tan and Chia (1993) investigate sectional logistic discontinuities and report numerical basin/bifurcation conclusions; their accessible abstract does not establish that their branches coincide with the present density-triggered dispersal map. Jiang and collaborators (2024) investigate state-dependent impulsive logistic bifurcations with a different fixed impulse threshold. Neither inspected account supplies the present exact state-selection formula. The 2024 work and 1993 paper were not available in full for a definitive negative comparison; this remains a priority limitation.

## Limitations

The classification is special to \(\mu=2\) and \(0<\varepsilon<1/2\), and uses the precise zero-sign convention. It is not a statement about the original paper's chaotic and long-transient parameter ranges. It does not imply generic novelty for all discontinuous logistic maps. The scientific priority conclusion is conditional on inspected primary material and indexed searches; earlier equivalent formulas in unindexed studies cannot be excluded. All claims have received a single-model mathematical review, not independent validation.

## References

1. A. Yu. Morozov, D. Almutairi, S. V. Petrovskii, and Y.-C. Lai, “Long transients in discontinuous time-discrete models of population dynamics,” *Chaos, Solitons & Fractals* **174** (2023), 113707. First public publisher date: 2023-07-12. https://doi.org/10.1016/j.chaos.2023.113707. Author-uploaded full text: https://www.researchgate.net/publication/372410722_Long_transients_in_discontinuous_time-discrete_models_of_population_dynamics
2. B. L. Tan and T. T. Chia, “Properties of a logistic map with a sectional discontinuity,” *Physical Review E* **47** (1993), 3087–3098. https://doi.org/10.1103/PhysRevE.47.3087.
3. H. Jiang, Y. Liu, L. Zhang, and J. Yu, “Border-collision bifurcation in the Logistic map with state-dependent impulsive forces,” *Discrete and Continuous Dynamical Systems - S* **17** (2024), 2732–2745. https://doi.org/10.3934/dcdss.2024050.
