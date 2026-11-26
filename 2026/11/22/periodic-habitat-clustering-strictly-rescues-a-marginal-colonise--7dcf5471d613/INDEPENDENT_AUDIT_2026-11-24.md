# Independent mathematical audit

## correctness

PASS

The source landing factor and replacement equations agree with the frozen model: d_L=1 makes λ_L=K and ℓ=c_LK independent of A. For continuous positive periodic b the resident substitution Z=K/M−1 gives Z′=μ−(Kb−μ)Z. The affine period map has a positive offset and multiplier exp[−T(K mean(b)−μ)]<1, hence a unique positive periodic Z and exponential convergence. Averaging (log(M*/Y))′ and (log M*)′ gives μ〈1/Y〉=mean(b) and 〈bM*〉=K mean(b)−μ, where Y=K−M*. The invasion exponent is ℓ〈Y〉−K mean(b); the constant-rate vacancy is μ/mean(b), the harmonic mean of Y. Strictness follows by AM–HM, since constant M* would force constant b. This proves an invasion gain, not necessarily positive invasion away from the constant-environment threshold. If invasion is positive, V=1/L obeys V′=−a(t)V+ℓ with positive forcing and contracting periodic monodromy on M*. For other positive resident trajectories the coefficient approaches a(t) exponentially; the evolution kernel retains exponential decay and the difference V−V* is forced by an exponentially decaying term. Thus V→V* and L→L*. The physical simplex is invariant (total derivative −μK on the sloping edge); the periodic state lies there by the limit along periods of interior trajectories, and cannot touch that edge since the derivative there is strictly inward. I checked the admissible Aη range and the perturbation calculation: γ=3/50, first cosine response u_c=9/34, ε=η/5, and averaging bM* gives the second-order mean resident change −u_c ε²/(2b₀), yielding 3/340 for the coefficient of η² in invasion. This verifies the decisive formulas analytically (RESULT.md lines 9–31 and 35–88). The package's numerical checker was inspected, not executed; its finite tests are not used for waveform-uniform claims.

## originality

PASS

The supported distinct claim is the exact invasion comparison and static-threshold periodic coexistence in the hierarchical replacement model with fixed inferior colonisation, not the single-species occupancy penalty, Jensen's inequality, or seasonally induced coexistence as a general phenomenon. Known resident occupancy comparisons are closely related: the gain is exactly ℓ(M₀−〈M*〉). One needs the two-species replacement term's exact period-average cancellation and the positive periodic attractor implication to identify the phase change in this system.

## value

PASS

At fixed habitat area and mean effective superior colonisation, the exact sign is tied to a genuine persistence boundary, not a comparison of arbitrary simulated waveforms. The inferior invader's gain balances resident-free capacity and replacement exactly, and produces an attracting positive coexistence orbit for every nonconstant admissible modulation from a marginal constant comparator. The explicit admissible habitat family and amplitude coefficient connect the all-waveform theorem to the motivating model. This is not a comparison at fixed mean autocorrelation, an empirical prediction, or a claim when both colonisation rates vary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
