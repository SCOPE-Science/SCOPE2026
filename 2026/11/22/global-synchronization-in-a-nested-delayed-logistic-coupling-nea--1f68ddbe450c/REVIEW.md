# Independent mathematical audit

## correctness

PASS

For strictly interior histories every new value is in (0,3/4]. Once both current values are in that range, g(t)/t is uniformly large for t<=1/4 and all cross-inputs in [1/4,3/4] give outputs greater than 3/5, so m_{n+1}>=min((12/5)m_n,3/5) gives finite entry into the persistent [1/4,3/4] current-value interval. The next values are in [15561/25600,3/4]. Using that g decreases for t>1/2, the five rational interval images land strictly inside [13/20,71/100]; the next iterate has all four components in that invariant box. For t there, |g'|=(2t-1)(1+(2t-1)^2)/2 increases, and the min gain is (4-a)-Lipschitz in its two arguments. The difference of each updated coordinate is at most 0.990051 times the old four-coordinate distance. The shift itself is only nonexpansive, but after two updates both time layers have the smaller bound; hence the full square contracts by at most 0.991. Uniqueness for the square and commutation with the map and coordinate swap give a synchronized fixed point, strictly between the endpoints by the strict box inequalities. The original map also converges on odd iterates, and invariant probabilities collapse to the fixed-point mass by bounded convergence. Independent replay `python /workspace/review_replay.py 4` checks the exact five intervals, invariant bounds and quantitative Lipschitz coefficient. This is an exact-real dynamical theorem for the explicitly composed recurrence, not for the different literal rendering of Eq. (8).

## originality

PASS

The composition, logistic seed and controls are prior, but the verified all-history attraction and quantitative trapping result on the interval with positive delayed gain were not covered by the strongest compared statements. This is a best-of-knowledge assessment, not a priority certification.

## value

PASS

The theorem establishes a nonzero-width interval with a genuinely active delayed term, proves attraction from arbitrarily small positive histories rather than only near the equilibrium, and supplies a concrete quantitative stability window for the published composition at its emphasized a=3.99. It is not a scalar endpoint computation, an optimal threshold, or a claim about an implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
