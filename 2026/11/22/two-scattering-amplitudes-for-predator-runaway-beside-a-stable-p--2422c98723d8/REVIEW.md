# Independent mathematical audit

## correctness

PASS

The OA primary PDF confirms Eq. (2) at β=1 gives the frozen recurrence. Strict inequalities force k>0 and P to decrease through x_* before γ. The prey-only multipliers are 0 and exp(P(γ))<1; the interior characteristic polynomial is positive at zero (A>B), negative at one (−B), and positive for large t, giving the claimed saddle. Exact arithmetic verifies the chamber witness. Within the wedge the predator multiplier is bounded below by exp(P(ε))>1, so summing geometric predation yields ∑ exp(rn)x_n<∞ for every finite r>0. The exact predator telescope gives positive L; the remaining log-predator error is a nonnegative tail of O(x_j). Its weighted sum at exp(sn) is finite by interchanging nonnegative sums, hence ∑|y_n−L exp(sn)|<∞ and ∑x_n y_n<∞. Consequently replacing y_n/(H+x_n) by L exp(sn)/H changes the accumulated prey forcing by an absolutely summable error, leaving a finite log K. The estimates are uniform on wedge compacts; the geometric prey bound gives L≥const·y_0 at fixed x_0, establishing nonconstancy. The numerical example at y_0=Y is on the wedge boundary but enters it strictly after one step, so it does not invalidate the diagnostic or extend the theorem's stated quantifiers.

## originality

PASS

The recurrence, boundary sink criterion and fixed-point setting are prior. The checked same-map paper treats local equilibria and bifurcations; the closest verified escape results use different continuous-time equations or a different discrete update. None supplies the positive-orbit escape wedge coexisting with the sink and both discrete amplitudes. This is a bounded comparison, not a priority certification.

## value

PASS

An explicit open escape set in a published recurrence demonstrates why a stable extinction equilibrium does not guarantee bounded positive orbits. The summable forcing estimate adds a finite prey prefactor and a finer timescale than the usual qualitative runaway or leading log-growth result. The slice is stated openly and supports a nonempty chamber of full dimension within that slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
