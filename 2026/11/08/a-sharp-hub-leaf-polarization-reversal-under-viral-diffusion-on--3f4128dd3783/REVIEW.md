# Independent mathematical audit

## correctness

PASS

Orthogonal star Laplacian eigenspaces have attenuation (1+w)^{-1} on leaf differences and [1+(m+1)w]^{-1} on hub-versus-leaf mean. For activation state (h,k), exact polarization/ε²=A(k−k²/m)+B(h−k/m)² with A=(1+w)^−2 and B=m/[(m+1)(1+(m+1)w)²]. Hub cascade yields h=1,K~Bin(m,p); leaf cascade yields (0,1) with 1−p, or (1,1+Bin(m−1,p)) with p. Taking binomial first two moments and subtracting gives the affine-in-p bracket and prefactor (m−1)(1−p)²/m². For m≥3 its intercept is negative and value at p=1 positive, yielding one p*∈(0,1); for m=1 both seeds symmetric, m=2 leaf strictly wins. Expected reach gap is (m−1)p(1−p). Independent sign checks used 15 weighted-star settings, not as all-size proof.

## originality

PASS

Tu–Neumann 2022 introduces the IC-plus-Friedkin–Johnsen model and generic expected polarization/seed heuristics. Its model is credited rather than claimed new. The current spectral star decomposition and explicit seed-order reversal threshold across every m,w,p is not entailed by the original general optimization descriptions without this model-specific computation. Related opinion-control work with stubborn agents or changing edges has different mechanisms. Resultary searches found no earlier stronger star-specific exact crossover.

## value

PASS

This is a motivated exact structural witness of a robust disagreement between maximizing viral reach and maximizing equilibrium polarization on the simplest nontrivial social-network topology. An all-star-size sharp transition is an interpretable parameter design boundary and a usable test case for generic seed-selection algorithms, not an arbitrary single-instance check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
