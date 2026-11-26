# Independent mathematical audit

## correctness

PASS

Cycle removal gives a uniform fixed-root forest. Deleting r prescribed nonroot leaves and independently restoring their parents gives the ratio (1−r/n)^(n−k−1) of compatible forests, which determines the joint indicators and the occupancy law; the all-cycle case has no leaves. Cycle counts give the conditioned Poisson law, and consecutive conditional means have strictly negative differences in k. On the √n cycle scale a Taylor expansion yields (1−x²)/(2e); the consecutive differences also give the global bound |mₙ,ₖ−n/e|≤C(1+k²/n). Poisson moment bounds then justify the mixed moment and covariance limit using E|Z|³=2E|Z|. For the conditional CLT, Fourier inversion in total Poisson count at its mean conditions the joint Gaussian limit: the marked-box outcomes (1,0) and (2,0) bound the integrand modulus by exp(−cn u²) uniformly in the other Fourier parameter near zero, allowing the scaled Gaussian integral. The Schur complement is e⁻¹−2e⁻². Uniformity for bounded k/√n and tightness give the independent joint limit. Vacancy indicators have nonpositive pair covariance, bounding the exact conditional variance by n/4 for the variance limit. Independent replay, python3 /workspace/frozen_math_replay.py 1, enumerates fixed-root parent maps for n=3,…,7 and checks the joint counts, including 68,295 graphs at n=7. The finite check does not establish the limit.

## originality

FAIL

A distinct published indexed record, 9f53c3cb582f, covers the same ensemble, cycle law, exact occupancy law, strict conditional regression, independent Gaussian/half-normal limit, quadratic conditional mean shift and sharp raw covariance coefficient. Allowing nonconstant nondecreasing tests instead of strictly increasing ones follows immediately from the same strict regression and positive support. The generating function and unconditional mean and variance limits follow from the shared occupancy law and moment analysis; they do not supply a distinct substantial remainder. In addition, 007c2a04bfe9 already contains the actual fixed-root conditional occupancy calculation in mapping language, which transfers exactly to one directed cycle of length at least three and then by forgetting the cycle orientation. This is a finding of demonstrated coverage, not a finding about which version was first public: index dates alone do not establish chronology or derivation.

## value

PASS

The substantive probability phenomenon is useful: two natural graph statistics are asymptotically independent at their first fluctuation scale while the conditional mean encodes a nontrivial residual response and a sharp smaller covariance. This evaluates scientific content, not distinctness; the covered formulas do not offer a separate viable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
