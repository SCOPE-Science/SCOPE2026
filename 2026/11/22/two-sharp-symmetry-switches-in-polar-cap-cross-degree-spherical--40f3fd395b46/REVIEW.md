# Independent mathematical audit

## correctness

PASS

With probability surface measure, the one-dimensional density is c_d(1−u²)^((d−3)/2); after factoring J₁ the truncated even powers of u are moments of 1−(1−s)Y with Y beta((d−1)/2,1). Recomputed these and all six full-sphere norms symbolically by Gaussian monomial moments, and recovered the three stated squared normalized overlaps. The O(d−1) transverse sectors are orthogonal, also for d=3 where reflections pair the two azimuthal signs. All three normalized overlaps are positive: P has negative discriminant, Q>0 and s<1. The leftover cubic transverse space has the stated dimension. For the top envelope, the reduced C/B ratio decreases through one at s₂₁; P−h_d Q is an upward quadratic negative at 1/(d+2) and positive at both endpoints. The exact crossing-defect factorization was independently verified and is strictly positive. To justify the whole interval before s₂₁, not just the defect at the endpoint, A/C is proportional to P/(1−s)², whose derivative is 2(d−1)(d+3)s/(1−s)³. Hence A<C there as well. The two roots of A−B straddle s₂₁ and the upper one lies above 1/(d+2), giving the exact tie spaces and no other top switch. Scaling by ds gives the two quoted limits (the upper root of z²−√6 z+3−√6 for the second), and at the thin cap the A/C ratio has the stated coefficient because P(1)=(d−1)(d+3). Read, but did not run, verify.py; verification_output.txt reports 308 finite assertions, corroboration rather than an all-d proof. The positive condition number excludes the genuine kernel and a=1.

## originality

PASS

The fixed-order cap overlap in dimension three is explicitly available in classical Slepian work, and the exact hemisphere singular values there are covered by an earlier adjacent-degree finding. The surviving distinct claim is the globally proved variable-aperture envelope and transition laws in every ambient dimension, supported by the all-d cross-block calculation. Neither prior general Slepian machinery nor the numerically similar switches for a same-degree antipodal concentration problem supplies this strict sector separation.

## value

PASS

The isolated cross block measures leakage between two particular harmonic degrees without conflating that leakage with within-degree cap energy. The first adjacent pair with three matching sectors is a motivated test, not an arbitrary truncation. Knowing the optimal sector and both tie dimensions at every cap size adds information missing from the general Slepian construction; the dimension-scaled boundary and thin-cap loss of conditioning quantify when that distinction matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
