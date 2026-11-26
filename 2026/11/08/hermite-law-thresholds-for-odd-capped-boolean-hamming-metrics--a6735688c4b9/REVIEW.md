# Independent mathematical audit

## correctness

PASS

The capped distance is a metric by subadditivity of the cap. Subtracting the constant r^p leaves -r^p at the origin and corrections j^p-r^p for 1≤j<r; a nonzero Walsh character annihilates the constant. Its eigenvalue is therefore exactly (1), and the nontrivial characters span the mean-zero subspace. For fixed degree j the generating function with z=u/√n and t=(n-2k)/√n converges uniformly on compact sets to exp(tu-u²/2); coefficient comparison gives H_j(t)/j!, and only degree 2m survives the n^m normalization on bounded t. For |s|≥R√n, dividing the Krawtchouk recurrence by s^{j+1} gives K_j/s^j=1/j!+O_m(n/s²) for each fixed j. Thus K_{2m} is positive and ≥c_m s^{2m} there for large R; its coefficient stays strictly negative as p→0 and dominates the lower powers uniformly. The compact mesh then yields the positive maximum constant because the nonzero even Hermite polynomial has Gaussian mean zero and positive leading coefficient. Bernstein subordination makes the CND range an initial interval, so the signs at (C_m^{-1}±δ)n^{-m} trap the supremum. Continuity and finiteness yield an attained zero of a nontrivial mode; the same uniform estimates apply with p=β as β→0, forcing its rescaled frequency to approach the minimizer set. Extrema of H4 and H6 confirm both explicit constants. Symbolic replay: python /workspace/audit_evidence/reconstruct.py (hermite_constants); this tests only the low-degree arithmetic, not the limit.

## originality

PASS

The bounded comparison distinguishes general negative-type criteria and central polynomial asymptotics from the leading constant and global obstruction localization for fixed odd caps at least five. The separate cap-three and even-cap records have different hypotheses; the exact catalogue hit is the audited record itself.

## value

PASS

This identifies the sharp embedding-related exponent and the location of the Fourier obstruction for an infinite natural family. For an odd cap, the leading shell has even degree and forces a central-limit-scale extremizer rather than an outer parity mode; the exact cap-five and cap-seven constants make the distinction quantitative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
