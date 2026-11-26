# Independent mathematical audit

## correctness

PASS

For fixed S=sL and diffusion −aL, both stages involve the same commuting operator and complete to (I+E_h²)/2. With ρ=a/s, t=sh and λ∈{0,1,3}, the filter amplification is 4(1+λt)/(2+λt)², so the completed amplification is G(ρq(λt)), G(w)=1−w+w²/2. The constant mode stays one; differentiating q gives max q=2C₂, so 1/2≤G≤1 throughout 0<ρ≤1/C₂. Projection onto the constant, antisymmetric and remaining symmetric modes shows only T_13=T_31 can be negative; 6T_13=ρ(3q(t)−q(3t))−ρ²(3q(t)²−q(3t)²)/2. The first bracket is positive because q(t)/t strictly decreases, so sign can fail only in the positive-denominator domain of R. I regenerated the denominator polynomial M and derivative polynomial P from q, recovering both displayed coefficients and signs: each has exactly one sign change, M(0)=−256<M(1)=605576, and P(3)<0<P(4). Thus the denominator becomes positive at one t_0∈(0,1); on (t_0,∞), R decreases to exactly one minimum t_*∈(3,4) and increases after. The positive numerator stays nonzero at t_0, and the large-t orders t⁻¹ over t⁻² give divergence at infinity. This proves the all-step cutoff, isolated contact and one bounded open negativity interval for ρ between the positivity and energy limits. Direct exact resolvent composition at (s,a,h)=(1,3/2,4) gives T_13=−37010590/4202539929, with 2/3>C₂, also proving the gap is strict. For a connected two-vertex graph the constant mode plus one contracted mode yields off-diagonal entries (1−g)/2≥0; hence no smaller graph supplies this defect. The conclusions concern the completed matrix in the specified energy-stable scalar-split class, not every stage or noncommuting and nonlinear cases.

## originality

PASS

Wu–Shu already provide the second-order filter, completed SSP-EIN2 method, and energy constant C₂. Distinct same-date Resultary records cover closely related first-order cone-positivity problems. The supported distinct result is the all-step entrywise threshold strictly above C₂ for the completed second-order map on the unweighted three-site path, with exact contact and a single bounded violation window. It is not a claim of priority for either the method or the general distinction between stability and positivity.

## value

PASS

The minimal path is a natural diffusion test, and the published energy bound is a meaningful baseline. The exact cone test shows that a completed second-order step can create a negative remote-node value even while stable in Euclidean norm, and gives the precise additional splitting required to avoid it and where it can fail. The small dimension is structural, not merely computational convenience: one nonzero mode cannot cause the defect. A lone sampled negative entry or recomputation of the energy constant would not establish this classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
