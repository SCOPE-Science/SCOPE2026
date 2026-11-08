# Global equilibrium convergence and a four-sink window in symmetric May–Leonard mutation dynamics

## Finding
Consider the three-population May–Leonard model with equal cross-competition coefficients and balanced global linear mutation:
\[
\dot x_i=x_i\bigl(1-x_i-a(x_j+x_k)\bigr)+\mu(x_j+x_k-2x_i),\qquad \{i,j,k\}=\{1,2,3\}.
\]
For **every** \(a>0\), \(\mu>0\), and \(x(0)\in[0,\infty)^3\setminus\{0\}\), the solution converges to a *single positive equilibrium*. In particular, there is no nonconstant periodic orbit, heteroclinic cycle, or non-equilibrium compact omega-limit set in the positive cone.

The equilibrium and attraction classification is sharp. If \(0<a\le1\), the only nonzero equilibrium is \(e=(1,1,1)/(1+2a)\), and it attracts every nonzero nonnegative initial point. For \(a>1\), define
\[
\mu_c=\frac{a-1}{3(2a+1)},\qquad
\mu_f=\frac{a-1}{4a+2\sqrt{2(a+1)}}.
\]
Then \(0<\mu_c<\mu_f\). If \(0<\mu<\mu_f\), all nonuniform equilibria consist of the three coordinate permutations of \((u_-,u_-,t_-u_-)\) and the three permutations of \((u_+,u_+,t_+u_+)\), except that at \(\mu=\mu_c\) the former coincide with \(e\). Here \(t_-<\sqrt{2(a+1)}<t_+\) are the two positive roots of
\[
\mu t^2+[4a\mu-(a-1)]t+2(a+1)\mu=0,
\qquad u_\pm=\frac{t_\pm+2}{t_\pm^2+4at_\pm+2(a+1)}.
\]
Every \(t_+\) equilibrium is a hyperbolic sink, and every nonuniform \(t_-\) equilibrium is a hyperbolic saddle with one unstable direction. The equal-population equilibrium \(e\) is a hyperbolic sink for \(\mu>\mu_c\), and has two positive eigenvalues for \(\mu<\mu_c\). In particular, for
\[
\boxed{\quad a>1,\qquad \mu_c<\mu<\mu_f\quad}
\]
there are **exactly four hyperbolic attracting equilibria**: \(e\) and three symmetry-related nonuniform sinks. At \(\mu=\mu_c\) and \(\mu=\mu_f\) some equilibria are nonhyperbolic, but the global convergence conclusion remains valid. For \(\mu>\mu_f\), the equal-population equilibrium attracts all nonzero nonnegative states.

## Assumptions and scope
The evolution is autonomous in physical time, the coefficients satisfy \(a,\mu>0\), and initial populations are finite and nonnegative, with strictly positive total \(S(0)=x_1(0)+x_2(0)+x_3(0)\). The origin is an equilibrium but is not part of the convergence statement; its linearization has positive eigenvalue \(1\). Convergence means existence of a single vector limit as \(t\to\infty\), not merely convergence of time averages or distance to the stationary set. No exponential rate is asserted at nonhyperbolic thresholds or on saddle stable manifolds.

## Proof
**1. Positivity and compactness away from the boundary.** Write \(S=x_1+x_2+x_3\). At a vanishing coordinate, \(\dot x_i=\mu S>0\) as soon as \(S>0\); the nonnegative cone is forward invariant and its nonzero trajectories are strictly positive after any positive time. Summing yields
\[
\dot S=S-aS^2+(a-1)\sum_i x_i^2.
\]
Using \(S^2/3\le\sum_i x_i^2\le S^2\) gives logistic upper and lower comparisons \(\dot S\le S-c_1S^2\) and \(\dot S\ge S-c_2S^2\), with positive constants \(c_1,c_2\) depending only on \(a\). Thus after finite time \(S\) stays between two positive constants and the solution is bounded. With bounded \(S\), each coordinate satisfies \(\dot x_i\ge\mu S-Cx_i\) for some fixed \(C>0\). Hence each coordinate is bounded below by a positive constant eventually; the omega-limit set is a nonempty compact invariant subset of the *interior* positive cone.

**2. Ordering and collapse onto an equality plane.** Subtraction of the equations gives the exact identity
\[
\frac{d}{dt}(x_i-x_j)=\bigl[1-aS+(a-1)(x_i+x_j)-3\mu\bigr](x_i-x_j).
\]
Consequently coordinate ordering and each equality plane are invariant. If any two coordinates initially coincide, the trajectory lies in an equality plane. Otherwise relabel the coordinates so \(x_1>x_2>x_3\), and set \(R=(x_1-x_2)/(x_2-x_3)>0\). Direct subtraction of logarithmic derivatives gives
\[
\frac{d}{dt}\log R=(a-1)(x_1-x_3).
\]
For \(a\ne1\), the positive ratio \(R\) is monotone. If its limit belongs to \((0,\infty)\), the nonnegative integral \(\int_0^\infty(x_1-x_3)\,dt\) is finite. Since all solutions and their derivatives are bounded, \(x_1-x_3\) is uniformly continuous; hence it tends to zero. The omega-limit set lies on the diagonal and must equal the unique diagonal equilibrium \(e\). If instead \(R\to\infty\), boundedness forces \(x_2-x_3\to0\); if \(R\to0\), it forces \(x_1-x_2\to0\). Thus in all cases the omega-limit set is contained in a coordinate-equality plane, or already is \(\{e\}\).

When \(a=1\), the exact identities \(\dot S=S(1-S)\) and \(\dot p_i=\mu(1-3p_i)\), where \(p_i=x_i/S\), yield \(S\to1\), \(p_i\to1/3\). Hence convergence holds also at \(a=1\).

**3. Planar exclusion of recurrent sets.** On, for example, \(x_2=x_3=u\), \(x_1=v\), the restricted positive planar system is
\[
\dot u=u[1-(a+1)u-av]+\mu(v-u),\qquad
\dot v=v[1-2au-v]+2\mu(u-v).
\]
For the Dulac multiplier \(B(u,v)=1/(uv)\),
\[
\partial_u(B\dot u)+\partial_v(B\dot v)
=-\frac{a+1}{v}-\frac1u-\frac\mu{u^2}-\frac{2\mu}{v^2}<0
\]
throughout the simply connected positive quadrant. Bendixson–Dulac therefore excludes every periodic orbit, homoclinic loop, and closed polycycle contained in that quadrant (the latter also follows by applying Green's theorem across the finitely many equilibrium vertices). The restricted planar polynomial system has finitely many equilibria, as shown in step 4. Standard planar chain-recurrence/Poincaré–Bendixson theory implies that every compact *internally chain transitive* subset of this quadrant is a single equilibrium when periodic orbits and closed connection cycles are absent; see Benaïm–Hirsch (1995, 1996). The omega-limit set of the original bounded autonomous trajectory is internally chain transitive. Since it is contained in an invariant equality plane, it is an internally chain transitive set for this planar flow. It must therefore be a singleton equilibrium. This proves convergence globally for every nonzero nonnegative initial state, including all degenerate parameter boundaries.

**4. Complete equilibrium list.** For \(a\ne1\), three pairwise distinct positive equilibrium coordinates are impossible: otherwise the difference identity in step 2 would require \(1-aS+(a-1)(x_i+x_j)-3\mu=0\) for all three pairs, and subtraction would force equality. Thus a positive equilibrium is either \(e\), or after a permutation it is \((u,u,tu)\) with \(t>0\), \(t\ne1\). Substitution into the equations and cancellation give
\[
H(t)=t^2+4at+2(a+1),\qquad
u=\frac{t+2}{H(t)},\qquad
\mu=\frac{(a-1)t}{H(t)}.
\]
This is impossible for \(0<a<1\). For \(a>1\), the function \(t\mapsto(a-1)t/H(t)\) increases until \(t_*=\sqrt{2(a+1)}\) and then decreases. Its maximum is \(\mu_f\), and its value at \(t=1\) is \(\mu_c\). Hence the asserted enumeration and strict ordering of thresholds. The origin and \(e\) are the only equilibria if \(a=1\), by the explicit normalized system above.

**5. Stability and exact four-sink window.** At \(e\), the eigenvalues are \(-1\) and \((a-1)/(1+2a)-3\mu\) with multiplicity two. For a nonuniform equilibrium \((u,u,tu)\) as in step 4, the Jacobian splits into the antisymmetric mode and the two-dimensional symmetric mode. The antisymmetric eigenvalue, planar block trace, and determinant simplify respectively to
\[
\lambda_{\rm anti}=-\frac{(a-1)(t-1)(t+2)}{H(t)},\qquad
\operatorname{tr}=-\frac{at^2+(a+3)t+4a}{H(t)}<0,
\]
\[
\det=\frac{(a-1)(t-1)(t+2)[t^2-2(a+1)]}{H(t)^2}.
\]
Since \(t_+>t_*>1\), all three eigenvalues at the \(t_+\) equilibrium have negative real part. For \(t_-<1\) the antisymmetric eigenvalue is positive and the planar block is stable; for \(1<t_-<t_*\) the planar block has one positive and one negative eigenvalue while the antisymmetric mode is stable. Thus each nonuniform \(t_-\) equilibrium is an index-one saddle. At \(\mu_c<\mu<\mu_f\), \(e\) is also a hyperbolic sink, proving exactly four and completing the classification.

## Verification
An accompanying executable performs rational-arithmetic checks of the equilibrium parametrization, the three factored Jacobian invariants, and the positivity of the planar Dulac divergence for a finite rational parameter grid. Independent numerical integration of representative initial conditions at \(a=2\), with \(\mu\) below, inside, and above the interval \((\mu_c,\mu_f)\), agreed with the predicted sinks. These finite checks support, but do not substitute for, the universal analytical proof. The key infinite-step argument is ordering-collapse plus planar exclusion of internally chain transitive sets.

## Relationship to prior work
Jaramillo, Mrad and Stepien (arXiv:2210.04342, DOI:10.1063/5.0138150) introduced this mutated May–Leonard vector field, proved the local homogeneous linear stability boundary, computed symmetry-broken equilibrium branches (including their fold), and numerically assessed nonuniform stability and long-run dynamics. Those features are credited, not claimed as first discoveries here. Their paper does not establish universal convergence of every nonzero orbit for the equal-competition slice, nor an analytical global no-recurrence theorem at the degenerate boundary. The new contribution is a complete global convergence result and its sharp dynamical consequence that the four locally attracting states exhaust the possible generic asymptotic destinations in the interval \((\mu_c,\mu_f)\). The explicit branch reparameterization and Jacobian factorizations furnish a reproducible exact description of that consequence.

Classical unmutated May–Leonard dynamics and earlier carrying-/balance-simplex theory do not imply the conclusion for positive all-to-all mutation, which destroys invariance of the coordinate faces. The argument uses standard planar chain-recurrence tools of Benaïm and Hirsch, rather than claiming those tools as new.

## Limitations
The statement requires equal cross-competition coefficients. For unequal coefficients the paper exhibits periodic orbits, so no global-convergence claim is made there. No smooth carrying-simplex construction, characterization of individual basin boundaries, uniform convergence rate at the folds, stochastic-population analogue, or independent mathematical audit is provided. There is residual publication-priority risk from potential unindexed reversible-mutation or symmetric population-system literature with an equivalent all-orbit convergence theorem.

## References
1. G. Jaramillo, L. Mrad and T. L. Stepien, *Dynamics of a linearly-perturbed May–Leonard competition model*, arXiv:2210.04342 (first public 2022-10-09), *Chaos* **33**, 063121 (2023), DOI:10.1063/5.0138150. https://arxiv.org/abs/2210.04342
2. M. Benaïm and M. W. Hirsch, *Chain recurrence in surface flows*, *Discrete and Continuous Dynamical Systems* **1** (1995), 1–16, DOI:10.3934/dcds.1995.1.1.
3. M. Benaïm and M. W. Hirsch, *Asymptotic pseudotrajectories and chain recurrent flows, with applications*, *Journal of Dynamics and Differential Equations* **8** (1996), 141–176, DOI:10.1007/BF02218617.
4. S. Baigent and collaborators, *Balance simplices of 3-species May–Leonard systems*, *Journal of Biological Dynamics* (2020), DOI:10.1080/17513758.2020.1736656 (unmutated related geometry).
