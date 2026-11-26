# Independent mathematical audit

## correctness

PASS

The local inverse of the consistent P1 mass is (2/ℓ_i) times the 2-by-2 matrix with diagonal 2 and off-diagonal −1; its true multiplicity averaging inserts 1/k independently on each hub row and column. With S=Σℓ_i, T=Σ1/ℓ_i, h=(ℓ_i), a=(1/ℓ_i), this gives the displayed assembled matrices. Substitution into BM fixes (0,a) and (1,−2e+(2S/k)a); off the equal-length case the joint kernel of eᵀ,hᵀ on leaf coordinates has dimension k−2 and eigenvalue 4/3. The trace gives the last root μ=4ST/(3k²); equal lengths give the same characteristic polynomial by continuity and μ=4/3. Both mass and BRAS matrices are positive definite by assembly with full-column-rank injection. Hence BM is similar to the symmetric-preconditioned matrix, and μ≥4/3 by Cauchy–Schwarz gives the condition number, not a singular-value claim on BM. The Jacobi scaling is identity plus the rank-two off-diagonal unit-vector update with eigenvalues ±1/2. The inequalities ℓ_i+mM/ℓ_i≤m+M and AM–GM give μ≤(R+1)²/(3R), attained by two arms at each endpoint for k=4. Solving against the Jacobi value 3 gives the stated sharp all-star threshold and strict comparison on either side in the claimed senses. Positive lengths, free hub and leaves, and k≥3 are all respected. Checker inspected, not run.

## originality

PASS

Credit the original BRAS definition, general projector spectrum/rank mechanism and the classical Kantorovich inequality. The distinct claim is the star-specific evaluation of the full spectrum and the sharp Jacobi comparison over all branched one-element-per-arm stars. General rank and norm results require an additional star calculation to reveal the repeated 4/3 modes and the arithmetic–harmonic outlier. Known adjacent threshold records change the geometry or the weighting and do not specialize to this claim.

## value

PASS

The exact evaluation isolates the one mode sensitive to arm-length imbalance and quantifies when the original approximate inverse reverses the comparison with diagonal scaling. A genuinely branched balanced endpoint construction proves sharpness, making this a useful stress test for graph mass preconditioners beyond a numerical example. No solver-time claim or extension to subdivided stars is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
