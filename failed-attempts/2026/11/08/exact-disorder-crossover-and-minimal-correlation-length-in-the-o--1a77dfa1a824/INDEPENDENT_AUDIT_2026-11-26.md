# Independent mathematical audit

## correctness

PASS

The cyclic constraints are exactly avoidance of 11 and 000, including N=3. The stated pair-state matrix appends the new symbol with its occupation weight and its closed walks count indexed words once. It is primitive by strongly connected returns of lengths 2 and 3. In the limiting Perron-transformed Markov chain, state 01 records an occupied site; its first returns have raw path weight z and lengths 2 and 3. Perron-vector factors telescope on a return, giving probabilities z/λ² and z/λ³ independently on successive returns. Put p=z/λ³=1/(1+λ). Then ρ=1/(2+p), and the conditioned occupation series is U(s)=1/[1−(1−p)s²−ps³]=1/[(1−s)(1+s+ps²)]. The connected series ρ[U(s)−ρ/(1−s)] removes the Perron pole and no other pole. Cauchy–Hadamard yields the stated limsup decay even with zero coefficients on subsequences. The two nontrivial normalized transfer roots solve t²+t+p=0. The dominant modulus is √p for p>1/4 and (1+√(1−4p))/2 for p<1/4, yielding the unique minimum at λ=3 and z=27/4, as well as the stated phase angle. At p=1/4 partial fractions have coefficients 4/9 at (1−s)^−1, 2/9 at (1+s/2)^−1 and 1/3 at (1+s/2)^−2. Thus C(r)=4(3r+5)(−1/2)^r/81, including r=0 and 1. The repeated eigenvalue −3/2 has one eigenvector direction by the first two equations of (T+3I/2)v=0; the double pole confirms a Jordan contribution to this observable. The primitive eigenvalue stays simple and analytic; λ∼z^(1/3) at zero and λ∼√z at infinity give the two endpoint scales. Independent finite cyclic enumeration for N=3,…,12 agreed with (N/k)binom(k,N−2k) at occupancy k, obtained by marking an occupied starting site and ordering the gaps, then dividing by k. The critical renewal recurrence was independently checked through r=30.

## originality

FAIL

The known blockade-one jammed-atom model is the identical constrained lattice gas, not just a related higher-dimensional model. Published work already gives its exact occupation-weighted independent block polynomial z(y²+y³), and the earlier renewal correlation calculation for the same jammed configurations gives the pole/modulus criterion and repeated-pole behavior (worked at unit activity). Normalizing the published block weights to probabilities and applying the renewal formula leaves precisely one quadratic. The critical fugacity and length minimum are the coalescence and minimum modulus of that quadratic; the all-r covariance is the direct coefficient evaluation at the double pole. This is prior-ingredient coverage by explicit routine implication, not an assertion that a source was found printing the value 27/4 or the same covariance in this notation.

## value

FAIL

The leading oscillation mode and the activity minimizing the correlation length are meaningful observables; the exact numbers can be useful as reference values. But for this frozen claim the prior same-model free-block kernel and established renewal pole analysis mechanically supply them by evaluating a quadratic and extracting a double-pole coefficient. No independently useful non-routine spectral or Gibbs result remains beyond that specialization. This is a value decision on the submitted result, not on the motivation of disorder crossovers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
