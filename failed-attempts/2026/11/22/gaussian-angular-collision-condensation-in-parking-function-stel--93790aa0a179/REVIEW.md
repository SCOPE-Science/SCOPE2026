# Independent mathematical audit

## correctness

PASS

For distinct nonzero objective coordinates, rearrange any parking point in the order of the scores. The sorted vector with 1 on the negative coordinates and the bound s_j at every positive coordinate is feasible and attains the strict coordinatewise maximum. This yields the asserted layers and angle via independent signs and uniform positive-coordinate order. Squaring then counting by j=n-k gives 4^(-n)L_n(-1); when b_1=1, n! pairs of formerly distinct vertices merge, adding 2n/(4^n n!) to the squared mass. For the asymptotic put x=sqrt(n): n^j/(j!)^2, at j=x+u sqrt(x), is e^(2x)e^(-u^2)/(2 pi x) uniformly for bounded u; geometric summation from either endpoint using the decreasing ratios n/(j+1)^2 bounds the tails outside ±A sqrt(x) on the normalization scale by O(e^(-A^2)/A) in the limsup. The falling-factorial multiplier tends uniformly to e^(-1/2) there and is bounded by 1 globally, proving the constant and the stated CLT. For the star, a list of k leaves above the hub determines the simplex-sum maximizer: leaf i in that list wins 2^(n-i) hub-containing summands plus its singleton, and the hub wins 2^(n-k). Thus the lists are distinct, each with probability (n-k)!/(n+1)!, proving the star law and ratio. Independent integer-objective enumeration over all feasible parking points in six examples and explicit connected-subset maxima for star n=2 through 6 agree; replay with python3 /workspace/reproductions/4.py (captured 4.txt). The finite checks are not the limiting proof. The supplied checker uses the known candidate vertex formula and floating dot products; it is not an enumeration of all feasible parking points.

## originality

FAIL

The main parking-metric conclusions are already stated, including the r=2 special case and boundary correction. The remaining cross-realization ratio is a direct quotient of two published collision asymptotics for the exact two metrics. This is demonstrated coverage and mechanical implication, not a failure of access or an inference from shared keywords.

## value

FAIL

The collision-conditioned square-root rank is a meaningful geometric phenomenon, but the existing fixed-r theorem already supplies it and the boundary case. The only apparent addition is to divide that known asymptotic by the known star asymptotic. The metric contrast is useful exposition, not a surviving independent scientific result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
