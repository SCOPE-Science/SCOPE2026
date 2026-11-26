# Independent mathematical audit

## correctness

PASS

Using the diagonal cross at index 1 gives residual spectral norm 1; using index 2 gives norm κ. The normalizing σ₂ is 1, yielding E[E^q]=1+(κ^q−1)p for the weak-column selection probability p. The first fixed-order partial-LU row pivot of (SA)ᵀ compares |κS₁₁| and |S₁₂| only. The angle of the two Gaussian coordinates is uniform, giving a two-sided wedge probability (2/π) arctan(1/κ). CPQR compares two independent squared Gaussian column norms scaled by κ² and 1. Dividing the first unscaled squared norm by their sum gives Beta(s/2,s/2), with miss threshold 1/(1+κ²). The beta integral at small z is z^(s/2)/[(s/2)B(s/2,s/2)] times 1+O(z), which gives exactly c_s and the error powers. Combining with the arctangent expansion proves all critical limits and convergence in probability. For s=1 the two rules coincide, as required by the distinct-cutoff assumption s≥2.

## originality

FAIL

The exact earlier CPQR first-pivot result covers both selection laws, not just the CPQR side. Its equation (4) becomes equality for two orthogonal columns and explicitly includes sketch height one. The first fixed-order LUPP step at any height is precisely a one-row CPQR first pivot by the definitions, since one-dimensional column norm is absolute value. Thus substituting heights s and 1 into the same published formula yields both pivot laws; for height 1 the beta-half CDF is the stated Cauchy tail. On the declared diagonal matrix, the conversion to normalized cross moments is a deterministic two-point readout. A first-term beta-integral expansion then gives both cutoffs and constants. No source need print the formulas side by side for this to be mechanical coverage. The same-day Cauchy record reinforces the mechanistic overlap but is not needed for the failure and does not itself assert the diagonal spectral comparison. The mathematics is correct; the failure is lack of a supported distinct scientific claim in this frozen scope.

## value

FAIL

The distinction between typical loss and mean loss is relevant to the motivating pivot choices, but on the frozen diagonal example the precise cutoffs and critical constants are mechanical readouts of the known two-column law at heights one and s. The cross error is just a relabeling of a known Bernoulli event, with no new loss control or structural step beyond the two-row pivot definition and elementary endpoint expansion. In this scope the result is an instructive example, not an independently needed unknown exact invariant. The separate same-day example already exhibits the qualitative oversampling blindness and rare-event loss for the same pivot mechanism; it is not used to equate the error metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
