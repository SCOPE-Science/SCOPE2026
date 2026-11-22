# Global convergence, nested diet activation, and inverse-time criticality for renewable floral rewards

## Finding

For a fixed positive pollinator population feeding adaptively on finitely many continuously renewing, depletable floral rewards, the coupled reward–preference dynamics below converge from **every** positive initial reward vector and every strictly interior initial preference vector to one explicitly computable equilibrium, independently of adaptation speed. The long-run diet includes progressively more floral sources, at sharp increasing pollinator-density thresholds. At the first two-source activation threshold, recruitment of the initially disfavored source has a universal inverse-time tail with an explicit coefficient, rather than exponential relaxation.

Let \(m\ge2\), and for every \(i=1,\dots,m\) take \(p_i,\delta_i,\kappa_i>0\). Fix population pressure \(A>0\) and adaptation speed \(G>0\). A floral reward \(F_i(t)>0\) and a foraging fraction \(x_i(t)>0\) evolve by
\[
\dot F_i=p_i-(\delta_i+A\kappa_i x_i)F_i,\qquad
\dot x_i=Gx_i\left(F_i-\sum_{j=1}^m x_jF_j\right),\qquad \sum_i x_i=1.
\]
Write \(r_i=p_i/\delta_i\) for the reward level without consumers and \((z)_+=\max\{z,0\}\). There is a unique \(L\in(0,\max_i r_i)\) satisfying
\[
\sum_{i=1}^m\frac{(p_i/L-\delta_i)_+}{\kappa_i}=A.
\]
Every interior solution converges to
\[
F_i^*=\min\{r_i,L\},\qquad
x_i^*=\frac{(p_i/L-\delta_i)_+}{A\kappa_i}.
\]
Thus the equilibrium and the active diet are independent of \(G\), and no nonconstant recurrent or periodic positive-interior trajectories exist.

If the unvisited reward levels are distinct, relabel them so \(r_1>r_2>\cdots>r_m\). Set \(A_1=0\) and, for \(2\le k\le m\),
\[
A_k=\sum_{i<k}\frac{p_i/r_k-\delta_i}{\kappa_i}.
\]
Then \(0=A_1<A_2<\cdots<A_m\), and \(x_k^*>0\) **exactly when** \(A>A_k\). In particular, every newly available floral source joins the asymptotic diet at its own threshold, with zero abundance precisely at equality. As \(A\to\infty\),
\[
L\sim\frac{\sum_i p_i/\kappa_i}{A},\qquad
x_i^*\longrightarrow\frac{p_i/\kappa_i}{\sum_j p_j/\kappa_j}.
\]

There is also an exact dynamical critical law. For \(m=2\), assume \(r_1>r_2\), and set
\[
A_c=\frac{p_1/r_2-\delta_1}{\kappa_1}>0,\qquad
K=GA_cr_2\left(\frac{\kappa_1}{\delta_1+A_c\kappa_1}+\frac{\kappa_2}{\delta_2}\right).
\]
At \(A=A_c\), every strictly interior initial condition obeys
\[
\lim_{t\to\infty}t\,x_2(t)=\frac1K.
\]
This critical inverse-time law is exact; it is not inferred from finite-time numerical experiments.

## Assumptions and scope

The model is a single, fixed-abundance pollinator guild; plant populations and the rates \(p_i\), \(\delta_i\), \(\kappa_i\), \(A\), and \(G\) remain constant. Each reward is replenished at constant rate and lost linearly by natural degradation and consumption. Foraging fitness is proportional to the same measured standing-reward level \(F_i\) across floral types; different conversion efficiencies, changing pollinator abundance, nonlinear resource functional responses, migration, and environmental noise are not covered. All \(x_i(0)\) are strictly positive, so no type is permanently ruled out by an initially zero preference. All \(F_i(0)>0\) and \(\sum_i x_i(0)=1\).

The phrase *active diet* refers to \(x_i^*>0\) in the asymptotic state, not an exact finite-time absence of visitation. The inverse-time assertion is restricted to a two-source threshold, with \(r_1>r_2\) and \(A=A_c\).

## Proof

**(1) Positive, bounded global dynamics.** The preference simplex is preserved because \(\sum_i\dot x_i=0\), and the explicit logarithmic equation for \(x_i\) prevents initially positive fractions from reaching zero in finite time. Positive reward production prevents \(F_i\) from reaching zero. The comparison inequalities
\[
p_i-(\delta_i+A\kappa_i)F_i\le\dot F_i\le p_i-\delta_i F_i
\]
provide positive lower bounds and finite upper bounds along every forward solution. Hence solutions are global and bounded, with each reward bounded away from zero.

**(2) The water level is unique.** For \(0<L<\max_i r_i\), the function \(H(L)=\sum_i(p_i/L-\delta_i)_+/\kappa_i\) is continuous and strictly decreasing wherever positive; it tends to infinity as \(L\downarrow0\) and to zero as \(L\uparrow\max_i r_i\). Thus \(H(L)=A\) has exactly one solution. The displayed \(x^*\) sums to one by this equation, and direct substitution gives \(p_i=(\delta_i+A\kappa_i x_i^*)F_i^*\). For \(x_i^*>0\) its reward is \(F_i^*=L\); for \(x_i^*=0\), its unvisited reward is \(F_i^*=r_i\le L\). This is an equilibrium, including at threshold ties.

**(3) Global attraction.** For \(F>0\), define \(\Phi(F;f)=F-f-f\log(F/f)\). With the convention that zero-weight entropy terms are omitted, consider
\[
\mathcal V(F,x)=\sum_i\frac{\Phi(F_i;F_i^*)}{A\kappa_i}+
\frac1G\sum_{i:x_i^*>0}x_i^*\log\frac{x_i^*}{x_i}.
\]
Each summand is nonnegative after summation (the second is relative entropy on the simplex), and the total vanishes precisely at \((F^*,x^*)\). Using \(p_i=(\delta_i+A\kappa_i x_i^*)F_i^*\), direct differentiation gives the *exact* identity
\[
\dot{\mathcal V}=-\sum_i\frac{\delta_i+A\kappa_i x_i^*}{A\kappa_i}\frac{(F_i-F_i^*)^2}{F_i}+
\sum_i(x_i-x_i^*)(F_i^*-L)\le0.
\]
The last sum is nonpositive: its nonzero terms arise only where \(x_i^*=0\) and \(F_i^*\le L\). Boundedness and the entropy bound ensure precompact positive-reward trajectories; positive-equilibrium preference coordinates also stay bounded away from zero. Whenever \(\dot{\mathcal V}=0\), every \(F_i=F_i^*\). A trajectory remaining in this set must satisfy \(\dot F_i=-A\kappa_iF_i^*(x_i-x_i^*)=0\), hence \(x=x^*\). The invariance principle therefore proves convergence of **every** permitted initial condition to that equilibrium. It also rules out nonconstant interior recurrent trajectories.

**(4) Exact support thresholds.** From the explicit equilibrium, \(x_k^*>0\) if and only if \(L<r_k\). At \(L=r_k\), the water-level equation reads \(A=A_k\); strict decrease of \(H\) gives \(L<r_k\) exactly for \(A>A_k\). Since \(r_k\) strictly decreases, these thresholds strictly increase. Once all floral types are active, the water-level equation simplifies to \(L=(\sum_i p_i/\kappa_i)/(A+\sum_i\delta_i/\kappa_i)\); this also proves the high-pressure limits.

**(5) Exact inverse-time critical recruitment.** For two sources at \(A=A_c\), set \(u=x_2\), \(q=r_2\), \(a_1=\delta_1+A_c\kappa_1\), and \(e_i=F_i-q\). Global attraction already gives \(u,e_1,e_2\to0\). Their exact equations are
\[
\dot e_1=-a_1e_1+A_c\kappa_1u(q+e_1),\qquad
\dot e_2=-\delta_2e_2-A_c\kappa_2u(q+e_2),\qquad
\dot u=Gu(1-u)(e_2-e_1).
\]
Since \(\dot u/u=G(1-u)(e_2-e_1)\to0\), for every fixed \(s\ge0\) we have \(u(t-s)/u(t)\to1\). Moreover, after an arbitrary late time, \(|\dot u/u|\) is smaller than any chosen positive exponential rate. Applying the variation-of-constants formula and dominated convergence to the two stable linear reward equations therefore yields
\[
\frac{e_1(t)}{u(t)}\longrightarrow\frac{A_c\kappa_1 q}{a_1},\qquad
\frac{e_2(t)}{u(t)}\longrightarrow-\frac{A_c\kappa_2q}{\delta_2}.
\]
(The exponentially decaying initial-condition terms divided by \(u(t)\) vanish because \(\dot u/u\to0\).) Consequently \(\dot u/u^2\to-K\), so \(\frac{d}{dt}(1/u)\to K\). Integrating and dividing by \(t\) gives \(t u(t)\to1/K\), as asserted.

## Verification

The included `check.py` numerically stress-tests the closed formulas, the Lyapunov derivative, and trajectories; it does not replace the analytic proof. It passed 1,500 random parameter tests of the exact derivative identity and equilibrium equations, nine long-horizon dynamics tests at three population pressures and three adaptation speeds, and a critical-threshold convergence test.

In the reproducible example \(p=(6,4,2)\), \(\delta_i=\kappa_i=1\), the activation pressures are \(A_2=1/2\) and \(A_3=3\). At \(A=1/4\) only the first source has positive limiting preference; at \(A=2\) the two positive preferences are \((7/10,3/10)\); and at \(A=5\) they are \((3/5,1/3,1/15)\). For the two-source submodel with \(G=1\), \(A_c=1/2\), the inverse-time coefficient is \(1/K=3/10\). A numerical trajectory gives \(t x_2(t)\approx0.299860\) at \(t=10^4\), consistent with—not a proof of—the exact limit.

To reproduce, run `python check.py` with Python, NumPy and SciPy installed. Numerical tolerances and pseudorandom seed are visible in the source. The main proof itself is symbolic and uses only elementary differential-equation comparison, an invariant-set argument, and asymptotic convolution estimates.

## Relationship to prior work

Yahaya, Rodger, Landi and Hui (2024) model floral resource renewal and adaptive foraging in large plant–pollinator networks and report a negative relationship between pollinator density and specialization; their main paper supplies the ecological motivation and examines local stability in a two-plant/one-pollinator toy model. Valdovinos, Moisset de Espanés, Flores and Ramos-Jiliberto (2013) already couple explicitly renewing floral reward stocks with adaptive-foraging replicator dynamics in a plant–pollinator model, and evaluate three empirical networks by simulation; the model mechanism itself is therefore prior. Valdovinos and Marsland (2021) already give equilibrium equal-profit conditions and a graphical niche analysis for related consumer–resource systems. Garay, Cressman and Varga (2003) prove *local* evolutionary stability for a two-bee/two-plant game with a static, algebraic nectar-stock response. These source-level statements are prior results, not novel claims here.

The proposed new contribution is the combined, quantified statement for an explicitly specified dynamic-reward/fixed-guild system: global convergence at every positive adaptation speed in arbitrary finite dimension, the complete nested activation staircase, and the exact inverse-time critical transition. Neither equal-profit stationarity nor local stability by itself implies global convergence or the critical relaxation law. The 2024 paper's supplementary toy-model appendix could not be retrieved; its coverage of the two-source boundary remains a priority uncertainty. More generally, classical replicator relative entropy and consumer–resource stability methods are acknowledged as closely related, and an unlocated stronger theorem could subsume portions of the analysis.

## Limitations

No claim is made for dynamic plant or pollinator abundances, heterogeneous profitability per reward unit, habitat movement, nonlinear handling times, random seasonal inputs, or more than one pollinator guild. Foraging fractions are deterministic population-level allocations, not individual-level diet decisions; exactly zero initial preferences remain zero and violate the full-support result. The supported reward-density thresholds are theoretical predictions under fixed rates, not measured ecological values. The first-activation inverse-time coefficient is proved for two sources only. Novelty is assessed against inspected accessible primary literature and mathematical search records; independent historical priority and external audit remain unperformed.

## References

1. Yahaya, M. M., Rodger, J. G., Landi, P., and Hui, C. (2024), *Emergence of structure in plant–pollinator networks: low floral resource constrains network specialisation*, Oikos e10533, first published 2024-05-03, https://doi.org/10.1111/oik.10533 .
2. Valdovinos, F. S., Moisset de Espanés, P., Flores, J. D. and Ramos-Jiliberto, R. (2013), *Adaptive foraging allows the maintenance of biodiversity of pollination networks*, Oikos 122, 907–917, first online 2012-10-30, https://doi.org/10.1111/j.1600-0706.2012.20830.x .
3. Valdovinos, F. S. and Marsland, R. III (2021), *Niche Theory for Mutualism: A Graphical Approach to Plant-Pollinator Network Dynamics*, The American Naturalist 197, https://doi.org/10.1086/712831 .
4. Garay, J., Cressman, R. and Varga, Z. (2003), *Optimal behaviour of honey bees based on imitation at fixed densities*, Community Ecology 4(2), 219–224, https://plantsys.elte.hu/pdf/garay/Com-Ecol-2003.pdf .
5. Wang, Y. (2018), *Dynamics of a plant-nectar-pollinator model and its approximate equations*, Mathematical Biosciences 307, 42–52, https://doi.org/10.1016/j.mbs.2018.12.001 .
