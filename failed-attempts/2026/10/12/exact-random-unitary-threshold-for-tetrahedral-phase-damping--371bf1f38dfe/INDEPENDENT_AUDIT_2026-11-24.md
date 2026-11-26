# Independent mathematical audit

## correctness

PASS

K is Hermitian with K²=3I and trace zero; the resulting C_t is a correlation matrix throughout the stated interval. Each basis projector is fixed, so its expectation in each perpendicular basis vector is zero termwise in any positive-weight unitary ensemble. Consequently all constituent unitaries are diagonal. For phases z=(1,e^(iθ),e^(i(φ+h)),e^(i(φ−h))), the six entry pairs give half the witness as cos θ+sin(2h)+2 Re[e^(iφ)(cos h−e^(−iθ)sin h)]. The last term is at most 2 sqrt(1−xy) for x=cos θ, y=sin(2h). Subtracting 4(1−xy) from (3−x−y)² gives (x+y−1)²+4(1−x)(1−y), with 3−x−y positive. Equality requires (x,y)=(1,0) or (0,1). In the first case θ=0 and h is a multiple of π/2; phase alignment gives the all-ones vector or (1,1,−i,i). In the second case h=π/4 mod π and θ=±π/2; alignment gives the other two listed vectors. Thus the continuum bound is 6 with exactly four projective maximizers. The trace of K against C_t is 4√3(1−t), giving necessity. The columns of Z=I+K are exactly the four vectors; ZZ†/4=I+K/2, giving sufficiency at the edge, and interpolation with the Fourier dephasing twirl covers the entire remaining interval. Z is invertible, so Z diag(w) Z†=ZZ†/4 forces w=(1/4,…,1/4). The full rank also forces a minimum of four terms. Uniqueness is of the ensemble after merging identical conjugations.

## originality

FAIL

The exact witness optimization is a specialization of the sharp finite-distribution Rényi norm bounds, under standard phase/norm duality for the tetrahedral SIC frame. The threshold and full minimal ensemble then follow from the phase columns of the same Gram matrix and K²=3I. The direct trigonometric proof is sound, but the submitted exact finding is mechanically implied by the prior bound and this linear algebra. No publication that states this exact Schur-channel parametrization was identified in the bounded comparison.

## value

FAIL

This is a motivated sharp boundary, and the elementary proof is useful exposition. However, the full numerical threshold and boundary ensemble are a direct lift of the known norm extremum for this tight frame. The record does not establish a further independent consequence or a new exact invariant beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
