# Independent mathematical audit

## correctness

PASS

For the specified separated planar equations with a common decay γ and cross-slopes −a,+a, perturbing the hidden coordinate at fixed x(0)=x_* gives (u,w)=e^(−γt)(−sin(at),cos(at)). Thus ∂_T∂_vP at T_k=kπ/a is −a r_k. Variation of constants for the second variation, forced by (F''w²,G''u²), gives at T_k the integral r_k∫₀^{T_k} e^(−γs)(F''cos³(as)+G''sin³(as))ds. The m=1,3 harmonics both acquire the same truncation factor 1−r_k; combining their elementary Laplace transforms gives the stated D and K and hence r_k(1−r_k)K/D. For K≠0 this has alternating sign and the implicit function theorem for ∂_vP=0 yields a nondegenerate extremum at a time-dependent v_k(T) on both sides, with derivative aD/[K(1−r_k)]. Each such extremum supplies exact paired outputs locally, not a fixed pair for all times. For the logistic illustration the equilibrium jets give D=20 and K=−16; monotone F also makes x and its instantaneous derivative determine y. Global attraction can be checked independently: let S(x)=G(x)−G(1) and R(y)=F(y)−F(1). The function ∫₁ˣS(u)du−∫₁ʸR(v)dv is positive definite and proper for these strictly monotone bounded sigmoids, and its derivative is −(x−1)S(x)+(y−1)R(y), strictly negative off equilibrium. Thus sublevel compactness and the invariance principle give attraction; the positive quadrant is forward invariant. Replay: frozen RESULT.md, Assumptions and Proof, lines 23–92, and the Lyapunov check above. Time and state neighborhoods need not have a uniform width in k. The bundled checker was inspected without execution; numerical equality is not the proof of exact aliasing.

## originality

PASS

Credit is for the explicit second-order curvature and location drift at every half-turn and the resulting detuned fold branches for K≠0, not for half-turn aliasing in itself, a general fold theorem, or derivative-based reconstruction. The strongest indexed overlap has half-turn aliasing on an affine strip (K=0) plus a separate sharp separation bound. The closest checked sampled nonlinear singularity paper uses a vanishing quadratic jet in its pendulum example. Neither gives the nonzero model-specific jet and its persistent branch. Same-day indexing establishes overlap, not priority.

## value

PASS

A nonzero resonant quadratic jet is a quantitatively different and stable local failure mode from exact linear resonance aliasing: it proves true two-snapshot ambiguity on open detuning intervals and gives the extremum's initial-state drift. An explicit globally attracting bounded feedback flow realizes that mechanism, showing why instantaneous reconstructibility does not give injectivity even slightly away from resonance. The contribution is this quantified witness and all-resonance condition, not a new general theory of folds or an observer design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
