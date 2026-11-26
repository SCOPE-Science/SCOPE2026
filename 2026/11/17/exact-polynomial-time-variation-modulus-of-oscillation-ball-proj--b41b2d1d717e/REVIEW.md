# Independent mathematical audit

## correctness

PASS

Clipping onto [c,c+R] and minimizing in c gives a piecewise-affine projector. In a strict exterior chamber, differentiation of stationarity gives dc equal to the average of the perturbations on the clipped set S. Every S of size at least two occurs: split it into nonempty lower and upper sets L,U, take inputs strictly below 0 by |U| and above 1 by |L| respectively, and put remaining coordinates at 1/2; the strict chamber has c=0 for R=1. Scaling handles other radii. On the quotient by constants, path differences are an isometry to l1 and the inverse basis is the single-jump family. Continuous affine formulas on the closures of finitely many chambers give the global upper bound by segment subdivision; a small in-chamber step in a maximizing jump direction attains it. At a straddling cut the selected value is b/(a+b); the two internal transitions have weights b/(a+b) and a/(a+b), and the four cut edges give exactly the stated B. With final bit zero, if k<m-k, surround each one by zeros for 2k switches; otherwise alternate 1,0 for each of the m-k zeros and prepend extra ones for 2(m-k)-1. Complement and reversal handle the other endpoint conditions. The two independent word maxima prove the formula and its O(n^3) count. Charging internal switches to selected or unselected sites gives min{s,2(n-s)} as an upper bound, plus one for the cut. Equal alternating halves ending and beginning with zeros at the cut give n/2 for even n>=4, and appending an endpoint gives the odd lower bound (the identity suffices for n=2,3). Independent exact enumeration over all subsets and jumps reproduced the full table through n=16 and independently checked the switch maxima through length 16. In particular the first expansive dimension is four.

## originality

PASS

The supported distinct claim is the exact two-input modulus for the range-constrained Euclidean projector in nonperiodic path variation, including its cubic evaluation and growth. The strongest indexed match with the same path variation and first expansive dimension concerns a different constraint and has bounded, rather than growing, modulus. The same record indexed under its own ID is not independent coverage. No inspected distinct statement implies the formula; this is a best-of-current-knowledge assessment, not a priority guarantee.

## value

PASS

The invariant quantifies the sharp sensitivity of a simple range constraint used to clip signals, in a metric that measures changes along the path instead of squared error. The contrast with both Euclidean nonexpansivity and the uniformly bounded TV-ball coefficient is substantive: this modulus grows linearly and its maximum is attained by finite perturbations. The binary-switch compression removes exponential subsets from an exact calculation and helps explain the growth rather than merely producing a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
