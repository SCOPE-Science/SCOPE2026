# Rate-selected minority survival in weighted tripartite dimer jamming

## Finding

Let \(a,b,\rho>0\). For each positive integer \(N\), start irreversible edge-by-edge dimer adsorption on the complete tripartite graph with parts \(A,B,C\) of sizes \(\lfloor aN\rfloor,\lfloor bN\rfloor,\lfloor bN\rfloor\). Every available \(AB\)-edge or \(AC\)-edge has selection weight \(1\), and every available \(BC\)-edge has weight \(\rho\). At each step choose one edge with probability proportional to its weight, occupy both endpoints permanently, and stop when no edge remains. Write \(U_A,U_B,U_C\) for the final unmatched vertex counts.

Then, as \(N\to\infty\), jointly in probability and in mean,
\[
\frac{1}{N}(U_A,U_B,U_C)\longrightarrow (L_\rho(a,b),0,0),
\]
where the exact surviving \(A\)-density is
\[
\boxed{L_\rho(a,b)=\begin{cases}
 a\left(1-(2-\rho)b/a\right)^{2/(2-\rho)},&0<\rho<2\ \text{and}\ a>(2-\rho)b,\\
 0,&0<\rho<2\ \text{and}\ a\le(2-\rho)b,\\
 a\exp(-2b/a),&\rho=2,\\
 a\left(1+(\rho-2)b/a\right)^{-2/(\rho-2)},&\rho>2.
\end{cases}}
\]
For any \(0<a<2b\), the sharp rate threshold for a positive extensive \(A\)-remainder is \(\rho_c=2-a/b\). Approaching it from above,
\[
 L_\rho(a,b)\sim a(b/a)^{2b/a}(\rho-\rho_c)^{2b/a}.
\]
In particular, for equal initial part sizes \(a=b=1\), the transition occurs at \(\rho_c=1\), with \(L_\rho(1,1)\sim(\rho-1)^2\) as \(\rho\downarrow1\). At \(\rho=3\), \(L_3(1,1)=1/4\): asymptotically one-twelfth of all vertices remain uncovered even though these graphs admit perfect matchings along even total-size subsequences. More strikingly, at \(a=1/2,b=1,\rho=3\) the initially *smallest* part retains density \(1/18\), while the two larger parts have vanishing final densities.

At every finite part-size triple \((i,j,k)\), the exact joint terminal probability generating polynomial \(G_{i,j,k}(u,v,w)\) is specified recursively by
\[
G_{i,j,k}=\begin{cases}
u^iv^jw^k,&ij+ik+jk=0,\\
\dfrac{ijG_{i-1,j-1,k}+ikG_{i-1,j,k-1}+\rho jkG_{i,j-1,k-1}}{ij+ik+\rho jk},&\text{otherwise},
\end{cases}
\]
where \(u\) is the variable for the \(A\)-part. Thus all finite-size probabilities are exactly rational functions of \(\rho\).

## Assumptions and scope

All three graph parts are independent vertex sets, and every edge joining distinct parts is present. At each deposition step, probabilities are recomputed over currently admissible edges after the endpoints of earlier dimers have been removed. Occupied vertices never return. The pair weight \(\rho\) is fixed, finite and positive as \(N\to\infty\); the initial part-size densities \(a,b\) are strictly positive and fixed. The limiting result concerns the terminal state, not a finite-time fluctuation law or a spatial diffusion model.

## Proof

**1. Exact finite Markov chain.** With \((i,j,k)\) currently uncovered vertices, the total weight of available edges is \(W=ij+ik+\rho jk\). For \(W>0\), the next transition removes one vertex in each endpoint part, with probabilities \(ij/W,ik/W,\rho jk/W\), respectively. If \(W=0\), the state is terminal. Conditioning on the first edge proves the displayed recurrence and termination within \(\lfloor(i+j+k)/2\rfloor\) steps. It also shows that any terminal state has at most one nonempty part.

**2. A genuine stochastic fluid limit.** Give each currently available edge of weight \(w\) an independent exponential clock of rate \(w/N\), remove its endpoints when it rings, and restart the clocks. Memorylessness makes the ordered deposited-edge sequence exactly the stated weighted sampling process. If \((X_N,Y_N,Z_N)\) are uncovered counts at continuous time \(t\), its three total transition rates are \(X_NY_N/N, X_NZ_N/N,\rho Y_NZ_N/N\). Hence the rescaled counts have drift
\[
 f(x,y,z)=(-x(y+z),-y(x+\rho z),-z(x+\rho y)).
\]
Every jump has Euclidean norm at most \(\sqrt2/N\), and all intensities are bounded by a constant times \(N\) on the initial bounded state region. The compensated jump martingales consequently have quadratic variations \(O(T/N)\) for each fixed \(T\), so Doob's inequality and Gronwall's lemma show uniform convergence in probability on \([0,T]\) to the unique solution of \(\dot{\mathbf x}=f(\mathbf x)\), initialized at \((a,b,b)\). The vector field is Lipschitz on the relevant compact set. Symmetry and uniqueness keep the last two coordinates equal; writing them \(y(t)\) and the first coordinate \(x(t)\),
\[
\dot x=-2xy,\qquad \dot y=-xy-\rho y^2,\qquad (x(0),y(0))=(a,b).
\]

**3. Exact limiting density.** Both coordinates are nonnegative and nonincreasing. Since \(\dot y\le-\rho y^2\), we have \(y(t)\to0\). Along every positive-time trajectory,
\[
\frac{dy}{dx}=\frac12+\frac{\rho y}{2x}.
\]
For \(\rho\ne2\), multiplication by \(x^{-\rho/2}\) gives the first integral
\[
 y=\frac{x}{2-\rho}+\left(b-\frac{a}{2-\rho}\right)(x/a)^{\rho/2}.
\]
For \(\rho=2\), the first integral is \(y/x=b/a+\tfrac12\log(x/a)\). Following the positive trajectory until \(y\downarrow0\) gives the unique positive endpoint when the corresponding first integral has a positive root, and gives \(x\downarrow0\) otherwise. Solving these root conditions yields exactly \(L_\rho(a,b)\) as displayed, including equality at the threshold. In particular \(x(t)\to L_\rho(a,b)\).

**4. Pass from every fixed time to the random terminal state.** On each realization and for each \(T>0\), every adsorption after time \(T\) which consumes an \(A\)-vertex also consumes a \(B\)- or \(C\)-vertex. Thus
\[
 X_N(T)-Y_N(T)-Z_N(T)\le U_A\le X_N(T),
 \qquad 0\le U_B\le Y_N(T),\quad0\le U_C\le Z_N(T).
\]
Divide by \(N\), first let \(N\to\infty\) at fixed \(T\) using Step 2, and then let \(T\to\infty\) using Step 3. This squeezes the terminal vector to \((L_\rho(a,b),0,0)\) in probability. Since every rescaled count is uniformly bounded, the same convergence holds for expectations. No exchange of stochastic and infinite-time limits is assumed; the displayed pathwise inequalities justify it.

**5. Threshold and examples.** For \(a<2b\), \(\rho_c=2-a/b\) lies in \((0,2)\). Just above it, \(1-(2-\rho)b/a=(b/a)(\rho-\rho_c)\), while \(2/(2-\rho)\to2b/a\). The product of the varying-exponent correction and \(\log(\rho-\rho_c)\) tends to zero, giving the stated sharp critical asymptotic. The two examples follow by substitution. A complete tripartite graph admits a perfect matching when its vertex count is even and no part exceeds half the vertices; both specified population ratios meet the latter condition.

## Verification

The standalone `verify_exact.py` computes the finite rational recurrence with exact `Fraction` arithmetic, and independently enumerates labeled available-edge choices. It checks every positive three-part triple with coordinates at most three and total size at most seven at the five rational weights \(1/2,1,3/2,2,3\). `verify_limit.py` symbolically differentiates both first integrals to zero, numerically integrates the deterministic equations across subcritical, critical and supercritical parameter cases, and compares seeded finite stochastic simulations with the formula. Both scripts executed successfully with Python 3.13.5, SymPy 1.14.0 and SciPy 1.17.0. Their checks confirm the algebra and test representative finite systems; the rigorous all-size assertion rests on the proof above, not on the simulations.

## Relationship to prior work

Ben-Avraham and Redner (1986) derived conservation relations and an explicit mean-field three-species solution **for the equal-reaction-rate annihilation model**. In particular the \(\rho=1\) specialization belongs to that prior rate-symmetric framework and is not claimed as a new special case. Pippenger (1989) established foundational results for random sequential adsorption on graph families, including edge adsorption; its stated local-regularity setting does not evaluate this growing-degree weighted tripartite family. Hilhorst, Washenberger and Täuber (2004) formulated broad multispecies annihilation rate and master equations and studied segregation/decay with symmetry assumptions; in Section 3.1 they explicitly set aside unequal-density terminal survivors. The present evaluated terminal law, rate-driven minority persistence, explicit noninteger critical exponent and finite-graph terminal convergence are the claimed distinction, rather than the generic master equation or the mass-action ansatz themselves.

## Limitations

This is an all-fixed-parameter thermodynamic limit for a finite graph sequence, not a theorem about the critical-window distribution, fluctuation exponents at the threshold, finite-time decay rates, or diffusion-limited spatial annihilation. Equal-rate three-species deterministic kinetics have substantial prior coverage. The 1986 primary article was available in abstract and bibliographic form but not inspectable in full during comparison, so historical priority remains provisional despite the difference in edge rates. No independent audit of the result has been performed.

## References

1. D. ben-Avraham and S. Redner, “Kinetics of n-species annihilation: Mean-field and diffusion-controlled limits,” *Physical Review A* **34** (1986), 501–509, https://doi.org/10.1103/PhysRevA.34.501 (publisher's verified public date: 1986-07-01).
2. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401, https://doi.org/10.1137/0402034.
3. H. J. Hilhorst, M. J. Washenberger, and U. C. Täuber, “Symmetry and species segregation in diffusion-limited pair annihilation,” arXiv:cond-mat/0409079 (first posted 2004-09-03), https://arxiv.org/abs/cond-mat/0409079.
