# Independent mathematical audit

## correctness

PASS

In the unabsorbed coupling the cycle pairs (Y,H) are iid: Y is the rightmost final displacement and H the maximum downward excursion of any walker during that cycle. The mean is −v/r+sqrt(2D) m_N sqrt(π)/(2 sqrt(r))=(v_c−v)/r. Finite nonzero variance makes the centered walk oscillate to arbitrarily negative reset positions, and a negative mean gives such positions by the strong law. A nonpositive reset position forces a prior continuous hit; positive reset positions alone would not imply survival. In the positive-mean case both cycle displacements and maximal absolute excursions have exponential moments near zero: for standard Brownian motion the one-sided supremum up to independent Exp(r) has tail exp(−u sqrt(2r)) by the hitting-time Laplace transform, and a union bound and Cauchy–Schwarz combine the two signs, N walkers and |v|T. Hence E exp(−θY)<1 for some θ>0; the sum of the Markov bounds for H_i−sum_{j<i}Y_j gives the record's exponential upper bound on capture for large x. This factors the current mark from past increments only. From every x>0, Brownian path support/positive killed transition probabilities and a reset in a finite time window give a positive probability of safely reaching that large reset level. There is also positive probability of capture before the first reset. The strong law, Poisson reset frequency, and exponential-tail Borel–Cantelli control of every within-cycle excursion give the stated almost-sure speed on survival, for all j. The coupled Gaussian maxima give strict increase and the stated N=1,2 checks and large-N leading term. Replay: RESULT.md lines 32–64; VERIFICATION.md and check.py were inspected, not executed. Numerical endpoint diagnostics cannot certify continuous or infinite-horizon survival.

## originality

PASS

Best-of-knowledge pass for the whole constant-drift sharp threshold and the almost-sure speed of survivors. There is substantial known overlap in the resetting protocol, Gaussian extreme-value kernel, and the zero-drift case. Neither priority over the driftless observation nor novelty of the renewal/random-walk methods is claimed.

## value

PASS

The question is whether cooperative resetting can offset actual inward drift when every walker is continuously exposed to absorption. The exact finite-N phase line, inclusion of critical capture, and linear speed on survival answer that question, with the contrast between reset-skeleton behavior and continuous survival made explicit. This is not an estimate extrapolated from finite-horizon observations, nor just the known zero-drift escape phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
