# Independent mathematical audit

## correctness

PASS

Normalization q_j(0)=1 fixes the constant of integration, so every admissible edge is q_j=Tq_{j+1}. Conversely, the drift ν{0} and Lévy measure ν(dx)/x on x>0 have Lévy integrability bounded by one, and the probability law they define has Tq_ν as Laplace transform. Its F-image is ν by differentiation and transform uniqueness. This permits arbitrary terminal probability, with no moment or ID requirement. The order reversal of T iterated N times sandwiches q_0 using 0≤q_N≤1. Terminal δ_0 realizes T^N1=h_{N+1}; δ_M approaches T^N0=h_N because the first integrated primitive is (1−exp(−Ms))/M≤1/M and T is continuous on each compact interval in the uniform norm. The unit-mean exponential q_* is fixed, so exact absolute deviation is the larger endpoint deviation. Iterating the Lipschitz integral bound for T gives N-fold integration of a function bounded by one, hence s^N/N!. At s=0 all h_n for n≥1 are one. For E_n=h_n−q_*, E_1=s+O(s²) and E_{n+1}=q_*(exp(−∫E_n)−1), so the leading monomial changes sign and is integrated once per step. The approachable endpoint therefore proves the claimed sharp limiting coefficient.

## originality

PASS

The map, inverse-law construction, and unit-mean exponential fixed point are prior. The exact finite-depth pointwise capacity with both endpoint constructions and the locally sharp factorial stability estimate are supported as distinct based on the inspected evidence.

## value

PASS

The natural finite-depth stability question has a complete sharp pointwise answer: an attainable bound, an escaping-terminal bound, and a quantitative distance to the normalized stationary law with best possible local constant. It distinguishes what is forced by a finite normalized chain from existence of inverse chains and exact periodic classification. This gives meaningful error control uniformly on bounded s-intervals without any terminal moment assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
