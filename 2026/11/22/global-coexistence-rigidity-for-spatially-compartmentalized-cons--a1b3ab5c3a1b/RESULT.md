# Global coexistence rigidity for spatially compartmentalized consumer-resource systems

## Finding

For every pair of positive integers \(s,m\), consider the fixed-isolation deterministic local/global nutrient system in the following section. **If it possesses a strictly positive stationary state, that state is unique and attracts every strictly positive initial state.** It is a hyperbolic exponentially attracting equilibrium. In particular, there is no other positive stationary state, no positive periodic orbit, and no nonstationary compact recurrent dynamics entirely within the strictly positive orthant. There is no small-coupling, equal-isolation, equal-uptake, or single-nutrient hypothesis.

## Assumptions and scope

There are \(s\geq1\) consumer species with biomasses \(N_i\), \(m\geq1\) abiotic nutrients with shared concentrations \(R_j\), and one local nutrient compartment \(T_{ij}\) for each consumer-nutrient pair. The fixed numbers \(R_{j0},k_i,\alpha_{ij},\beta,\gamma\) are strictly positive; fixed species-specific isolation fractions satisfy \(0<\theta_i\leq1\). The positive state obeys

\[
\begin{aligned}
\dot N_i &=N_i\left[\sum_{j=1}^{m}\alpha_{ij}\big((1-\theta_i)R_j+\theta_i T_{ij}\big)-k_i\right],\\
\dot R_j &=R_{j0}-R_j-\gamma R_j\sum_{i=1}^{s}(1-\theta_i)\alpha_{ij}N_i-\beta\sum_{i=1}^{s}(R_j-T_{ij}),\\
\dot T_{ij}&=\beta(R_j-T_{ij})-\gamma\theta_i\alpha_{ij}T_{ij}N_i.
\end{aligned}
\]

A **strictly positive stationary state** \((N^*,R^*,T^*)\) means that every component is positive and all displayed derivatives vanish. Its existence is an explicit hypothesis, **not** claimed for every input or mortality vector. The source's adaptive-isolation and stochastic-supply variants are not included.

## Proof

Put \(h_a(z)=z-a-a\log(z/a)\) for \(z,a>0\), and define the nonnegative coercive entropy

\[
\mathcal V(N,R,T)=\gamma\sum_{i=1}^s h_{N_i^*}(N_i)+\sum_{j=1}^m h_{R_j^*}(R_j)+\sum_{i=1}^s\sum_{j=1}^m h_{T_{ij}^*}(T_{ij}).
\]

At the stationary state, the local-nutrient balances give

\[
\beta(R_j^*-T_{ij}^*)=\gamma\theta_i\alpha_{ij}T_{ij}^*N_i^*>0,
\qquad t_{ij}=\frac{T_{ij}^*}{R_j^*}\in(0,1).
\]

Set \(u_j=R_j/R_j^*\), \(v_{ij}=T_{ij}/T_{ij}^*\), and

\[
P(u,v)=u^2+uv^2-3uv+v
=(u-\sqrt v)^2+u\sqrt v\,(\sqrt v-1)^2(\sqrt v+2)\geq0.
\]

Every term on the right is nonnegative for \(u,v>0\); equality in \(P\) occurs only for \(u=v=1\). Direct differentiation of the entropy, substituting the three equilibrium balance equations and collecting the consumption and exchange terms, yields the exact identity

\[
\begin{aligned}
\dot{\mathcal V}={}&-\sum_{j=1}^m\left(1+\gamma\sum_{i=1}^s(1-\theta_i)\alpha_{ij}N_i^*\right)\frac{(R_j-R_j^*)^2}{R_j}\\
&-\beta\sum_{i=1}^{s}\sum_{j=1}^{m}\frac{R_j^*}{u_jv_{ij}}\left[t_{ij}(u_j-v_{ij})^2+(1-t_{ij})P(u_j,v_{ij})\right].
\end{aligned}
\]

Here \(t_{ij}\in(0,1)\) and the prefactor of each shared-resource square is at least one. Therefore \(\dot{\mathcal V}\leq0\), and \(\dot{\mathcal V}=0\) implies \(R_j=R_j^*\) and \(T_{ij}=T_{ij}^*\) for all indices. If a solution remained in this zero-dissipation set, its local-resource equation would give

\[
0=\dot T_{ij}=-\gamma\theta_i\alpha_{ij}T_{ij}^*(N_i-N_i^*),
\]

and hence \(N_i=N_i^*\). Thus the largest forward-invariant subset of the zero-dissipation set is the singleton stationary state.

Strict positivity is forward invariant: each biomass equation is linear in the corresponding biomass along a solution, and the nutrient equations have positive inputs at zero concentration. Because \(h_a(z)\) tends to infinity at both \(z\to0^+\) and \(z\to\infty\), every initial entropy sublevel set is a compact subset of the strictly positive orthant. The local solution consequently extends for all positive time. LaSalle's invariance argument now proves convergence of every positive trajectory to \((N^*,R^*,T^*)\).

A second strictly positive stationary state would have zero entropy derivative in the preceding identity, forcing its shared and local nutrient coordinates to equal the reference values; the local equations then force all its biomasses to coincide as well. Hence uniqueness.

Finally, the quadratic leading form of \(\mathcal V\) at equilibrium is positive definite, and the quadratic dissipation annihilates only perturbations supported in the biomass coordinates. Such a nonzero perturbation cannot be an invariant mode of the Jacobian, because any changed biomass immediately changes at least one local nutrient derivative through the strictly positive factor \(\gamma\theta_i\alpha_{ij}T_{ij}^*\). If a linearized eigenvector had real part of its eigenvalue nonnegative, the quadratic entropy inequality would force its nutrient coordinates to vanish and then its biomass coordinates to vanish, a contradiction. Hence all Jacobian eigenvalues have strictly negative real parts, giving local exponential attraction.

## Verification

The standalone script `verify_global.py` constructs a fully rational, three-consumer/two-nutrient positive equilibrium; it checks all stationary equations and independently compares the entropy derivative with the displayed identity at 700 randomly chosen strictly positive rational states, with exact rational arithmetic. A separate symbolic one-consumer/one-nutrient reduction was also expanded and found to vanish identically. These checks are supporting evidence, **not** substitutes for the all-size proof above; no numerical convergence experiment certifies asymptotic stability.

## Relationship to prior work

ElGamel and Mugler (2026) introduce precisely this local/global nutrient uptake mechanism and study coexistence, resilience, multinutrient benefits and adaptive isolation, mostly by numerical and equilibrium analyses. Their fixed-isolation formulas do not establish the conditional all-size, arbitrary-isolation **global** positive-attractor theorem above. Earlier chemostat literature proves global convergence under other nutrient-growth or intraspecific-competition assumptions; those results are not presented as new. Results for a single common nutrient and equal isolation, including an existing local stability and entry-threshold classification, do not imply global convergence for different \(\theta_i\) across multiple nutrients. The precise new object is the entire fixed-isolation, exchange-coupled model with the explicit entropy dissipation identity. Priority beyond the compared literature remains unverified independently.

## Limitations

No assertion of existence of a positive equilibrium without further conditions. No conclusions about which boundary species persist if a positive equilibrium is absent, adaptive or time-dependent isolation, fluctuating supplies, demographic stochasticity, or parameter perturbations leaving the stated hypotheses. Convergence need not be uniform over parameter families approaching \(\theta_i=0\). The numerical checks are finite, and neither source priority nor independent scientific validation has been established.

## References

1. Motasem ElGamel and Andrew Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, arXiv:2611.00222v1 (first public 2026-10-30). https://arxiv.org/abs/2611.00222
2. N. Abdellatif, R. Fekih-Salem and T. Sari, *Competition for a single resource and coexistence of several species in the chemostat*, Mathematical Biosciences and Engineering **13** (2016), 631–652. https://doi.org/10.3934/mbe.2016012
3. F. Yu, W. Song and Y. Wang, *Effect of diffusion on a consumer-resource system with source-sink patches*, Discrete and Continuous Dynamical Systems B **28** (2023), 1905–1937. https://doi.org/10.3934/dcdsb.2022152
4. X. Zhang, Q. An and H. Wang, *Global solvability and stability of cognitive consumer-resource model with nonlocal usage of memory*, Journal of Mathematical Analysis and Applications (2026). https://doi.org/10.1016/j.jmaa.2025.130076
5. C. Alvarez-Latuz, T. Bayen and J. Coville, *Global stability of perturbed chemostat systems*, arXiv:2501.08011 (2025). https://arxiv.org/abs/2501.08011
