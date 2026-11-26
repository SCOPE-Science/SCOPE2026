# Independent mathematical audit

## correctness

PASS

Fontanari's drives on the edge satisfy U_A+U_B=1+gamma, U_A-U_B=(1-gamma)d. Below gamma=1 each drive t lies in [0,1] and t^(1/p)>=t, so all are eligible; above gamma=1 both drives are at least one. The surplus difference is strictly decreasing in u; because there is overlap, its root never assigns a voter to an ineligible choice. Its centered equation is exactly Phi_p(d_next)=(1-gamma)d. Phi_p is odd, has positive derivative, and its second derivative is strictly positive on (0,1) for every real p>2. Oddness gives the alternating-sign identity by induction. Convexity makes the secant Phi_p(r)/r strictly increasing from c_p to 1. For s=|1-gamma|>0 the amplitude map is strictly increasing: below/above each nonzero crossing it moves toward that crossing without overshoot, and at s<=c_p it decreases any nonzero amplitude to zero. Increasing amplitudes as a map exclude any other periodic behavior; signs then distinguish fixed points from the one two-cycle. At gamma=0,2 the nonzero limiting amplitude is 1, and its one-sided multiplier is 2/p. At gamma=1 the first iterate is identically zero (the origin needs no update). The critical inverse expansion has coefficient -beta=-(p-1)(p-2)/6; positivity of the iterates permits reciprocal squaring, giving an increment 2*beta+O(r_n^2), hence the stated limit by Cesaro summation at both thresholds. All-real proof is independent of finite tests. Replay: python replay/4_cutoff.py, exact generalized-series composition and reciprocal-square check for seven rational exponents plus 108 one-step reflected equation pairs from exact rational orbits at p=3,4,5,7, and exact p=3,4 amplitude checks. The uploaded verifier was read, not executed. No claim about abstention-positive start, p=2, or gamma>2 is needed.

## originality

PASS

The model, threshold locations, several attractor/basin descriptions, and implicitly the stationary/cycle amplitude equation are already in Fontanari. The accepted contribution is the global pointwise analytic derivation including the critical endpoints and their explicit common asymptotic coefficient, tied together by the exact reflected-orbit identity. No claim is made that generic monotone-map or parabolic-fixed-point arguments are new. Best of knowledge only; public search was unavailable, not evidence of absence.

## value

PASS

Neutral multipliers alone cannot quantify relaxation. The sharp coefficient for every nonzero edge start, exact pairing of opposite-sign regimes and rigorous elimination of additional periodic behavior provide usable information for the originating map's phase diagram. The motivation and new content are confined to the fully mobilized invariant edge; empirical claims and conclusions on the full simplex are not implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
