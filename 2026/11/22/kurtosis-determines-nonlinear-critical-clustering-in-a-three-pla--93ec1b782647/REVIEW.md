# Scientific review

## Correctness — PASS
The payoff gradient is obtained by direct differentiation of the positive Gaussian allocation fractions. The transverse Jacobian at the unique symmetric strategy and the stable common-direction eigenvalue match the full source model. Reflection symmetry makes the strategy line \((a,-a,0)\) exactly invariant; its third-order coefficient is reconstructed from an explicit algebraic fraction. Permutation symmetry and oddness lift the coefficient to the full two-dimensional center manifold. A negative cubic coefficient yields local asymptotic stability and the exact square-root rate; a positive one yields a genuine unstable invariant trajectory. The symbolic checker and numerical examples passed. Boundary \(\kappa=13/12\) is expressly unproved.

## Originality — PASS, bounded by available literature
The closest primary source is Lovett–Fu (arXiv:2611.17148), which derives the first linear instability threshold, describes pitchfork and later bifurcation behavior for a Gaussian-mixture landscape, and states results using the Jacobian. The new result concerns *the exactly nonhyperbolic equality case*, which is not decided by that linear test: the critical cubic has the exact fourth-moment threshold \(13/12\), and two laws of identical variance give opposite nonlinear outcomes. Full main-article definitions, results and formal statements were compared, as were the distinct Lotka–Volterra resource-competition results of Pigolotti et al. Published mathematical-result searches by exact source, cubic normal form, fourth moment, and resource competition returned no demonstrably covering claim. The main paper points to a separately hosted supplemental bifurcation calculation that was not accessible, so historical priority is literature-bounded, not certified.

## Value — PASS
The original linear instability threshold depends only on resource variance and leaves its critical surface undecided. The exact fourth-moment criterion determines whether the symmetric profile is attracting or repelling at that surface, supplies a sharp slow-convergence rate when attracting, and separates two natural finite resource laws with indistinguishable linearizations. This is a structural nonlinear distinction in a three-player resource competition model, not a numerical recomputation or a change of notation.

## Scientific limits and risks
The result is local, deterministic and exactly three-player; the degenerate threshold \(\kappa=13/12\) and off-critical global dynamics remain open. The supplemental bifurcation analysis attached to the originating paper could contain closer prior coverage than the inspected main text. All claims are self-reviewed, with independent audit outstanding.

Self-review: passed. Independent audit: not yet performed.
