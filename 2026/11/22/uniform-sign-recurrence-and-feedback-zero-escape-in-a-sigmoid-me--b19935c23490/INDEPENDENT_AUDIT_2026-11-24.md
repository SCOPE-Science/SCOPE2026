# Independent mathematical audit

## correctness

PASS

For the displayed map and σ₁σ₂η ≠ 0, let H(y)=ηy|y|/2−y and Q=z−σ₂H(y). On a transition with both endpoints in a single closed half-line, H restricts to one quadratic and ΔQ is ∓σ₂η x²/2, including zero endpoints. Thus a one-sided string of N transitions wholly in the box has Σx² ≤ 4B_R/|σ₂η|. The derivative bound for the sigmoid gives |x_{j+1}−σ₁/2| ≤ L_R|x_j|, hence x_j²+x_{j+1}² ≥ σ₁²/[4(1+L_R²)]. Summing N−1 adjacent pairs gives N≤1+C_R; a floor(C_R)+3 time block has floor(C_R)+2 transitions, strictly more than this. This excludes each closed half-line and thus forces both strict signs. Continuity gives forward invariance of the support of a stationary law (preimages of neighborhoods of an image point have positive mass), and integration of the block indicator inequalities gives the two 1/M_R bounds. At σ₃=0, the x-iterates from time 1 have the sign of σ₁ and magnitude at most |σ₁|, and from time 2 magnitude at least δ. Summation gives the stated y bound; thereafter the z increments have eventual sign sgn(σ₂σ₁η) and magnitude bounded below by a positive linear function of time, yielding quadratic escape. Eq. (9) has θ=s−1+Υ, so at Υ=1 the current-state −x₁ cancels exactly in the first forward-difference step.

## originality

PASS

The source equation and its absence-of-equilibria observation are prior. The supported distinct contribution is the within-box strict-sign block bound and stationary masses, together with global zero-feedback escape rates for this map; the closest model and sign-crossing comparisons do not supply them.

## value

PASS

The exact signed coboundary links the absence of one-sided recurrence to a uniform quantitative constraint on any compact invariant law of the named model. This supplies an analytic diagnostic beyond numerical chaos evidence and absence of equilibria. The zero-feedback estimates identify a necessary coupling condition for boundedness and distinguish drift of the two memory coordinates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
