# Exact demand symmetrization of selfish and fleet-optimal traffic on affine parallel roads

## Finding

Fix a finite collection of at least two parallel roads and a common origin and destination. Each road has a strictly increasing affine travel-time law. Let a fraction of the fixed total demand be nonatomic self-routing traffic and the remaining fraction one centrally optimized fleet, minimizing **its own** total travel time, not the system-wide total. The unique mixed equilibrium is determined by two *ordinary* all-selfish Wardrop equilibria at symmetrically shifted demands.

Write \(W_i(q)\) for the unique all-selfish flow on road \(i\) at demand \(q\geq0\). For total demand \(D>0\) and coordinated share \(0\leq\alpha\leq1\), the equilibrium has

\[
S_i=W_i((1-\alpha)D),\qquad
C_i=\frac{W_i((1+\alpha)D)-W_i((1-\alpha)D)}{2},
\]
\[
F_i=S_i+C_i=\frac{W_i((1+\alpha)D)+W_i((1-\alpha)D)}{2}.
\]

Here \(S_i\), \(C_i\) and \(F_i\) denote selfish, coordinated, and total road flows. In particular, no coupled equilibrium solver is needed: two scalar Wardrop water-filling solves suffice for any finite number of roads. The same identity proves that selfish-flow support is contained in fleet-flow support whenever both classes have positive demand.

## Assumptions and scope

There are \(n\geq2\) roads, with fixed coefficients \(a_i\geq0\) and \(b_i>0\), and travel times

\[
d_i(f)=a_i+b_if\quad(f\geq0).
\]

The fixed total demand is \(D>0\). The selfish class has volume \((1-\alpha)D\); the fleet has volume \(\alpha D\). Selfish traffic follows Wardrop's minimum-current-travel-time condition. The fleet, holding selfish flow fixed, minimizes \(\sum_i C_id_i(S_i+C_i)\), subject to its own nonnegative link-flow and demand constraints. There are no capacities, path-interaction effects, external fleet objectives, heterogeneous origin–destination pairs, or stochastic fluctuations.

Define \((u)_+=\max\{u,0\}\) and

\[
G(\lambda)=\sum_{i=1}^n\frac{(\lambda-a_i)_+}{b_i}.
\]

For every \(q>0\), there is exactly one \(\lambda(q)>\min_i a_i\) satisfying \(G(\lambda(q))=q\). Set

\[
W_i(q)=\frac{(\lambda(q)-a_i)_+}{b_i}\quad(q>0),\qquad W_i(0)=0.
\]

These are the ordinary all-selfish Wardrop flows, including ties at activation thresholds. The convention at zero demand avoids assigning a meaningless unique zero-volume multiplier.

## Proof

**1. A strict potential for the two-class game.** Let \(S_i,C_i\geq0\) have the prescribed class totals. The selfish and fleet first-order road costs, respectively, are

\[
P_i^S=a_i+b_i(S_i+C_i),\qquad
P_i^C=a_i+b_i(S_i+2C_i).
\]

These are the partial derivatives of the exact potential

\[
\Phi(S,C)=\sum_i\left[a_i(S_i+C_i)+\frac{b_i}{2}S_i^2+b_iS_iC_i+b_iC_i^2\right].
\]

The Hessian of its \(i\)-th summand is \(b_i\begin{pmatrix}1&1\\1&2\end{pmatrix}\), whose eigenvalues are \(b_i(3\pm\sqrt5)/2>0\). Thus \(\Phi\) is strictly convex. Coordinatewise convex first-order conditions for each class are exactly the minimization first-order conditions of \(\Phi\) on the product of the two demand simplices. Hence the two-class equilibrium exists and is unique and coincides with the unique potential minimizer. This also proves global, not merely local, equilibrium uniqueness at boundary supports.

**2. Decouple the potential.** Introduce transformed road flows

\[
L_i=S_i,\qquad H_i=S_i+2C_i.
\]

The complete feasible region becomes \(0\leq L_i\leq H_i\) with

\[
\sum_i L_i=(1-\alpha)D,\qquad
\sum_i H_i=(1+\alpha)D.
\]

A direct exact expansion gives

\[
\Phi=\frac12\sum_i\left(a_iL_i+\frac{b_i}{2}L_i^2\right)
+\frac12\sum_i\left(a_iH_i+\frac{b_i}{2}H_i^2\right).
\]

If the cross-constraints \(L_i\leq H_i\) are temporarily dropped, the independent strictly convex minimizers are \(L_i=W_i((1-\alpha)D)\) and \(H_i=W_i((1+\alpha)D)\): their KKT conditions are precisely Wardrop water filling.

**3. Prove the dropped inequalities are automatically satisfied.** The function \(G\) is continuous and strictly increasing above \(\min_i a_i\). Therefore \(q\mapsto\lambda(q)\) is strictly increasing for positive \(q\), and each \(W_i(q)\) is nondecreasing on \([0,\infty)\). Because \((1-\alpha)D\leq(1+\alpha)D\), the independent minimizers satisfy \(L_i\leq H_i\) for every road. They are therefore feasible in the original coupled region and, being the global minimizers of the relaxed strictly convex problem, uniquely minimize the constrained one. The inverse transformation \(S_i=L_i\), \(C_i=(H_i-L_i)/2\) proves the exact identities, including \(\alpha=0\), \(\alpha=1\), coincident free-flow times and all support-transition boundaries.

**4. Sharp two-road efficiency illustration.** Consider \(D=1\), delays \(d_1(f)=f\) and \(d_2(f)=\tau+\beta f\), where \(0<\tau<1\) and \(\beta>0\). From the identity,

\[
F_1(\alpha)=\begin{cases}
(\beta+\tau)/(1+\beta),&0\leq\alpha\leq1-\tau,\\
(1+2\beta+\tau-\alpha)/(2(1+\beta)),&1-\tau<\alpha\leq1,
\end{cases}
\qquad F_2(\alpha)=1-F_1(\alpha).
\]

For total travel time \(T=F_1^2+\tau F_2+\beta F_2^2\), the unique system optimum has \(F_1^{\mathrm{opt}}=(\tau+2\beta)/(2(1+\beta))\). Completing the square yields the **exact inefficiency gap**

\[
T(\alpha)-T_{\mathrm{opt}}=
\frac{\min\{\tau,1-\alpha\}^2}{4(1+\beta)}.
\]

The fleet's effect therefore has a nonzero *sharp plateau* through \(\alpha=1-\tau\), followed by an explicit quadratic reduction to zero at full coordination. This is one example, not a claim that every parallel-road network has the same two-segment formula.

## Verification

The accompanying `fleet_symmetrization_checker.py` uses exact rational arithmetic. It constructs both Wardrop flows, verifies class totals and nonnegativity, and checks both classes' minimum-cost/KKT conditions on 2,100 deterministic pseudo-random parameter instances with two to nine roads, including endpoint class shares. It also checks the explicit two-road flow and inefficiency identities on 1,344 rational parameter instances. These are supplementary finite tests; universal correctness follows from the analytical strict-potential and decoupling proof, not enumeration.

## Relationship to prior work

Toso, Parise, Frasca and Kibangou (first public preprint 2024-08-28) define the same selfish-versus-coordinated traffic game, prove uniqueness under strong monotonicity, and establish fleet-share monotonicity of efficiency for parallel networks. Their published statements do not present the exact *two shifted-demand Wardrop equilibria* representation or this explicit two-road inefficiency formula. Battifarano and Qian (2023) derive critical fleet-size conditions and restricted analytic formulas for parallel networks, including formulas conditional on preserving the original user-equilibrium assignment; those differ from an unconditional formula for every fleet share and arbitrary positive affine slopes. Nilsson, Grover and Kalabić (2018) give the same two-objective traffic equilibrium and convergence algorithms but not the independent water-filling decomposition. The present claim is the affine parallel-road decoupling, not the existence of the underlying traffic game, its general potential theory, or generic Wardrop equilibrium.

## Limitations

This is an exact static affine parallel-road result. For nonlinear latencies the transformed Hessian need not separate, and for shared links or multiple origin–destination pairs transformed Wardrop solutions need not satisfy the same feasibility condition. Without capacities the result is not a traffic-flow or ride-hailing deployment prediction. The model's fleet minimizes its *own* travel time; replacing it with an altruistic system optimum or a Stackelberg leader changes the game. Historical priority remains subject to earlier equivalent formulations in broader traffic-equilibrium literature; no independent external review has been conducted.

## References

- Toso, T., Parise, F., Frasca, P., and Kibangou, A. Y., *On the impact of coordinated fleets size on traffic efficiency*, arXiv:2408.15742, original preprint posted 2024-08-28, https://arxiv.org/abs/2408.15742.
- Battifarano, M. and Qian, Z. S., *The Impact of Optimized Fleets in Transportation Networks*, *Transportation Science* (2023), https://doi.org/10.1287/trsc.2022.1189; accessible full text https://par.nsf.gov/servlets/purl/10482295.
- Nilsson, G., Grover, P., and Kalabić, U., *Assignment and Control of Two-Tiered Vehicle Traffic*, IEEE Conference on Decision and Control (2018), https://doi.org/10.1109/CDC.2018.8619411; full text https://www.merl.com/publications/docs/TR2018-171.pdf.
