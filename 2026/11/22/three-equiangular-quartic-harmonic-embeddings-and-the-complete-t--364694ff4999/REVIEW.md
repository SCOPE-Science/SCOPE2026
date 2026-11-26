# Independent mathematical audit

## correctness

PASS

In ambient dimension n−1, solving the axis-invariant degree-four harmonicity equations and normalizing at the axis gives P(t)=[(n+1)(n+3)t⁴−6(n+1)t²+3]/[n(n−2)]. The addition theorem with probability measure and h_n^−1/2 evaluation gives this polynomial as the Gram entry, with diagonal 1. Distinct roots give only 0 and ±1/2; evenness and the unsigned incidence identities CᵀC=2I+A and CCᵀ=(n−2)I+J give the constant, standard, and complementary sectors of dimensions 1,n−1,N−n and the three stated rational eigenvalues. They are all positive (including n=4), so the map onto the data is surjective, not necessarily injective on harmonic coefficients. I independently obtained all eigenvalue differences and verified the forward difference of the standard eigenvalue: its numerator is negative at 5 and 6, positive at 7, and after translating n=7+s all its coefficients are positive for s≥0. The constant eigenvalue increases, the two-row one decreases to 7/8, and the pairwise differences certify the minima and the two ties. There are both incident and disjoint pairs even at n=4, so equiangularity is exactly (a−b)(a+b)=0; the factors (n−21)(n+1) and (n−15)(n−5) give the only three dimensions. At n=21 the off-diagonal inner products are +1/133, giving the printed rank-one update and multiplicity 209. Independent symbolic replay: harmonic() in /workspace/calculations/algebra_checks.py. The supplied finite test code was inspected but not executed; in particular one checked four-cycle on each chosen four-set need not be an exhaustive basis (already at n=4), whereas the incidence proof gives the full multiplicity. No assertion of an optimal equiangular packing or unnormalized norm bound is needed.

## originality

PASS

The diagonalization mechanism is classical and the earlier indexed A₄ and A₅ results already give the exact n=5 and n=6 spectra, including the n=5 equiangular correlations. The PASS is for the combination of the all-rank quartic analysis, sharp least-sector/bound classification, and completeness of the quartic-kernel equiangular cases, including n=15 and 21. It is not for rediscovering either fixed-rank spectrum, for new Johnson graph spectral theory, or for generic constructions of equiangular lines.

## value

PASS

Unlike a new computation of generic Johnson eigenvalues, this gives the sharp normalized interpolation cost on a natural all-rank root configuration and explicitly identifies which symmetry sector limits conditioning and when. It also completely determines when the two root-pair types become equiangular in this specific harmonic embedding, including the all-positive 210-line case. The useful content is the joint exact behavior across ranks, not the two known low-rank examples or a generic Seidel sign pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
