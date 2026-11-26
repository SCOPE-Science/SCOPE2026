# Independent mathematical audit

## correctness

PASS

The stationary convolution is well-defined by positive occupation of the on mode. On/off transport of U=kV/D−1 has velocities −2kU and 2k, so zero flux gives the joint-density ratio f_off/f_on=u and the stationary shapes B and B+1 at the common rate A. At a stationary off observation, the joint measure of the entry excess u₀ and age t is proportional to b f_on(u₀)exp(−at) du₀dt: the transition hazard is constant, and survival after entry depends only on t. Thus U₀ and 2kT are independent Gammas with shapes B and 1, and J=2kT/U is Beta(1,B), independent of U and therefore of X in the off mode. For either mode, at u=Rv the exponential rate is Av+1/(2v) with unique minimizer √(k/a). At u≤δR the likelihood is bounded by exp(−R/(4δ)) for large R; at u≥MR the Gamma exponential controls the tails even after adding a moment weight. This yields both posterior concentration and the first-moment asymptotic in the on mode. Rescaling 2kT=JU gives the stated Beta limit, and the exact on/off density odds give the coefficient √(aD)/(k||x||).

## originality

FAIL

The result is mathematically correct but covered by a direct specialization of Frydel's earlier age-structured and variance-space formulas, arXiv:2607.05173v1. This is not a conclusion drawn from static laws alone. The earlier paper supplies the stationary age/birth propagator, its deterministic variance version, and the explicit memoryless Gamma law, all for the same complete-release model with finite on stiffness. Substitution gives the very joint kernel whose Beta fraction and far-position limit the frozen record claims. The earlier paper need not state the Beta limit verbatim for the coverage to hold.

## value

FAIL

Inferring excursion age from a distant observation is a motivated path question, and the beta fraction is an informative interpretation. But for this exact exponential-switching case the earlier age-resolved variance kernel and Gamma solution already yield the split, and the scalar saddle gives the two limits without a new invariant or estimate. The fixed-dimensional formulation changes only the Gaussian likelihood prefactor and does not add a new mechanism or nontrivial extension. The claimed narrow exact result therefore does not supply an independently needed new fact beyond a direct deduction from the earlier framework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
