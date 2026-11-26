# Independent mathematical audit

## correctness

PASS

The complete repaired RESULT.md corrects only the decimal expansion of C; its exact expression and fixation claims are unchanged. A vertex with a discordant neighbors picks one with probability a/deg, and, conditional on that pick, the closed-neighborhood expression is a/(deg+1) for either current label. Thus the hub jumps with rate equal to discordant count squared divided by d=m(m+1); each discordant leaf jumps at rate 1/2. From each nonabsorbing state a positive-probability sequence of leaf flips with no hub flip reaches consensus in the current hub label, so there is no nonsingleton recurrent class and absorption is almost sure. The harmonic equations give increments u[k+1]-u[k]=2(m-k)w[k]/d and v[k+1]-v[k]=2(k+1)w[k+1]/d. Their difference gives (d+2(k+1))w[k+1]=(d+2(m-k))w[k], including the boundaries; reversing factors gives R_m=1, so u_m=1 and v_0=0 give the stated normalization. At m=1 both seed probabilities are 1/2. The log expansion has uniform O(1/m) aggregate error, and the limiting Riemann integral is reduced by symmetry to the Gaussian integral in the claim. R_1→1 and m²/d→1 give the scaled leaf constant. The node-update voter comparison follows from the degree-weighted martingale with bounded terminal values 0 and 2m. Independent enumeration tested 1020 labeled states with m=1..8 against the original per-neighbor update rule, not the lumped generator; it checked exact harmonic residuals, boundary values and label symmetry. For the decimal, the integral is the convergent sum of a_k=2^k k!/(2k+1)! (integrate the exponential Taylor series); a_{k+1}/a_k=1/(2k+3) bounds the omitted tail. It gives C=0.4148196588637697539269..., so the original trailing ...976 is not the exact expansion. Replay: python3 /workspace/independent_checks.py 1. The frozen check was inspected but not run.

## originality

PASS

Credit the closed-neighborhood conformity rule, nonlinear voter models, and prior star analyses. The distinct finding is eventual fixation from all initial states for this specified degree-dependent quadratic update, including the exact single-leaf m^{-2} law with a positive limiting hub probability. Neither the strongest eventual-fixation comparison nor the first-reversal comparison covers that combination. This is a bounded statement-level finding, not an absolute priority claim.

## value

PASS

For a motivated conformity dynamic, the all-initial-state formula resolves a natural consensus invariant and identifies an order-of-magnitude difference between hub and leaf placement: the hub retains a constant chance, while leaf survival into eventual consensus is quadratically instead of linearly suppressed. Neither a first-reversal probability nor a voter-model normalization comparison would answer this eventual-fixation question. The finding is confined to the explicitly specified endpoint, not a conclusion about heterogeneous economic incentives or simultaneous updates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
