# Independent mathematical audit

## correctness

PASS

For the fixed original map, each of the two branches maps its half of the box onto the box up to its boundary, and has absolute Jacobian determinant 2. Backward iteration gives every length-n word mass 2^(-n), independently confirming STY (P4). The branch matrices are signed monomial; at each step exactly the column occupying output row 1 after the shift has its magnitude doubled. With input coordinate j=1+((-r) mod M) this gives the occupation count of post-step residue r. Multiplying by z_r on arrival gives the claimed row-vector PGF; at M=3,n=2 the four fair words give the four distinct monomials printed in the result. The Poisson relation (I−P)g_i=f_i gives increments (1−2S_j)f_i(R_(j−1)) and endpoint term Pg_i(R_0)−Pg_i(R_n), bounded by the oscillation 2(M−1)/M. Irreducibility and holding give ergodicity and uniform stationary occupation; the predictable covariance limit is I/M−11^T/M² and boundedness verifies martingale Lindeberg. Independently, every nonconstant Fourier eigenvalue λ=(1+ω)/2 has Re[λ/(1−λ)]=0, so the lag-covariance correction vanishes on the mean-zero subspace. The Euclidean range gives the condition-number law, and martingale orthogonality bounds the second moment of the normalized centered vector, so normalized ranges are uniformly integrable. For M=3, integration by parts gives E max Z_i=3∫φΦ²x dx=6∫φ²Φ dx=3/(2√π), hence the stated mean. Ergodicity also gives the common almost-sure growth rate. Read VERIFICATION.md and verify_twisted.py, not executed. The quoted 10,330 is a recorded count, not a fresh replay. The script actually loops over M=2 through 6 in the covariance check as well, not 2 through 8 as RESULT.md line 84 says. That does not affect the all-fixed-M proof.

## originality

FAIL

A distinct, directly inspected Resultary record, 11d620ed5ef6, gives the same multinomial covariance CLT, Gaussian condition-number range and mean for the larger domain M≥2, along with the exact same finite-time occupation reduction. The separately displayed PGF is a direct encoding of the full law already specified by that reduction; the M=3 mean is a specialization. This is demonstrable equivalent coverage; it is not a finding that the November 1 record preceded the October 19 frozen record or that the frozen author derived anything from it.

## value

FAIL

Multinomial covariance despite temporal dependence is mathematically substantive, as is the distinction between Lyapunov rates and square-root-scale anisotropy. But those contributions are already covered by the exact matching result. The remaining arrival-weight PGF and elementary Gaussian constant are routine expressions of laws already determined there, not a new motivated invariant or valuable boundary. No distinct valuable repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
