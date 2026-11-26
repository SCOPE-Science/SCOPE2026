# Independent mathematical audit

## correctness

PASS

Reconstructed the stationary path observable independently. The aligned orbit A and minority orbit B form a two-state chain A→B at 3h and B→A at d. Symmetry makes the stationary law constant within each orbit; the full per-state ratio pi_B/pi_A=h/d. Thus each A↔B jump's medium entropy is cancelled exactly by its contribution to stationary system entropy. Within B the two possible jumps occur at rates a=(1+gamma_o)/2 and b=(1-gamma_o)/2 and have increments +2eta and -2eta respectively, because their reverse rates exchange a and b. Conditional on the orbit trajectory these marks have independent Poisson counts with those rates times the B-occupation time: all rates and the orbit exit hazard are independent of the microstate within B. Feynman–Kac on the orbit process adds g_s-1 to the B diagonal, since a exp(-2s eta)+b exp(2s eta)=g_s. The resulting irreducible Metzler matrix has diagonals -3h and -d-1+g_s and off-diagonal product 3hd. Its larger eigenvalue gives the displayed SCGF for all real s, and g_s=g_(1-s) gives symmetry and both zeros. Stationary occupation has mean p and covariance p(1-p) exp(-(3h+d)|t|). Conditional expectation and variance of the two Poisson counts give the displayed mean and variance rates, including the extra occupation term. For gamma_o=0 all path increments are zero; otherwise the mean is positive. The all-real-s function is not a constant-rate Poisson difference: its two large-|s| slopes and leading exponential coefficients would fix the step magnitude and rates to the unmixed B process, which has the wrong mean by the factor p<1. Inspected verification.py: its numerical eight-state spectral and derivative grids corroborate but do not prove these conclusions. The exact proof uses the strict parameter interior, the triangle, and stationary path entropy.

## originality

PASS

The supported distinct claim is the explicit three-spin stationary entropy SCGF and the resulting fluctuation rates, not the kinetic model, Gibbs stationarity, the fluctuation theorem, or the general tilted-generator method. No inspected source contains or directly implies that model-specific SCGF.

## value

PASS

The triangle is a natural minimal periodic model with distinct left and right neighbours and with dissipation despite Gibbs-type stationarity. The observable-specific all-field result is a precise benchmark for nonequilibrium entropy statistics. The positive occupation-time correction quantifies why the jump fluxes alone cannot predict the variance, rather than merely checking a generic fluctuation symmetry or a numerical small matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
