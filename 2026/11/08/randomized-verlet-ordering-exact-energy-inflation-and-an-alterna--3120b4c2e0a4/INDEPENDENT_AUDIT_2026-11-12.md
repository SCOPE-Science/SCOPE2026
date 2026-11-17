# Independent mathematical audit

## correctness

PASS

For unit harmonic oscillator, position/velocity Strang maps A=[[d,hc],[-h,d]], B=[[d,h],[-hc,d]], with d=1−h²/2,c=1−h²/4, have unit determinants and trace 2−h² in (−2,2) for 0<h<2, hence fixed powers bounded. Independent symbolic calculation gives (AᵀA+BᵀB)/2=(1+h⁶/32)I, proving exact all-n fair expected physical energy and time scale n h⁶. For arbitrary interior p, the 3D covariance determinant det(I−T_p)=−h⁸p(1−p)(8−h²)²/128<0; positivity gives a growing mean-square covariance mode (not every deterministic start or almost-sure growth). For deterministic alternating AB, the trace is 2−4h²+h⁴−h⁶/16; unimodularity and crossing tr=-2 at h=sqrt(5)−1 with AB≠−I establish bounded, Jordan, expanding regimes. SymPy verified polynomial identities independently; no extrapolation from finite h tests.

## originality

PASS

Earlier published paired symplectic Euler treats first-order drift–kick maps over TWO elementary steps and can not be substituted for the two palindromic second-order position/velocity Verlet maps here. General Strang-splitting and modified-Hamiltonian texts analyze fixed order stability, not independent switching mean physical energy or the exact AB boundary. The exact sixth-power rate and the sharp alternating threshold for these particular second-order maps survive implication comparisons; unknown older mixed-Verlet papers remain a priority risk.

## value

PASS

Symplectic time integrators are selected for bounded oscillatory long-time error, so independent random choice of two individually stable second-order variants is a natural failure mode. The exact scalar energy inflation coefficient 1/32, physical time h^(−5) onset, all-interior-p instability and contrasting deterministic alternation boundary furnish a precise, meaningful and reusable benchmark, not an arbitrary tiny numerical adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
