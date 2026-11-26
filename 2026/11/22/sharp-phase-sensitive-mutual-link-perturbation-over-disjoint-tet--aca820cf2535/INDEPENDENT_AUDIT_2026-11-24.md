# Independent mathematical audit

## correctness

PASS

The generic age and homogeneity identify each allowed labeled diagram with exactly one ordered pair type. Forbidden four-sets with one new point impose the all-one prohibition inside each old triple, and those with both new points forbid joint ones on the old pairs within S. The disjoint triples give independent blocks: 7^2, 7^2, 7^2-3^2 and 3^3-2 patterns, respectively. Factoring by the empty-base patterns gives the stated factors. For a uniform k-set, the linear block correction is 3(a-1)t(k)_2/(n)_2 plus O(t k^3/n^3). For r>=2 hit blocks, choose a pair in each block; a specified choice is contained with probability (k)_(2r)/(n)_(2r)<=(k/n)^(2r). Summing the binomial series yields O(t^2 k^4/n^4) on k<=ceil(20 log n). Outside this range both weights are bounded using binom(n,k)(40/49)^binom(k,2); the tail is smaller than every power of n even before dividing by the baseline partition function. The successive baseline ratios are strictly decreasing with a factor at most q per unit step and so give uniform Gaussian tails around m_n. For fixed integer j the weight ratio at m_n+j relative to m_n tends, uniformly in the changing phase, to q^(j(j-1)/2-j delta_n); uniform integrability gives both the baseline second falling-factorial moment and convergence of the centered absolute deviations. Centering the h(k)-tilt exactly gives half the mean absolute centered tilt divided by its mean. The L1 remainder divided by t log(n)/n^2 is O(log(n)^2/n + log(n)^3/n) over the entire t range. Expanding (m_n+J)_2 leaves 2m_n times the lattice mean absolute deviation, with only O(1) other terms. Its minimum over phases is positive by continuity and nondegeneracy. The phase coefficient is genuinely nonconstant: at delta=1/2 the mean crosses 1 with derivative b Var(J)>0, so the j=1 term in the mean absolute deviation produces a nonzero derivative jump. Independent replay: python3 /workspace/review_checks.py 3 counts sixteen fixed-link cases at n=6,t=2 by separate x-graph enumeration and inclusion-exclusion for y. This is finite corroboration; frozen code and its recorded output were inspected, not executed.

## originality

PASS

Credit the empty-base law and lattice phase as prior background, and the materially overlapping fixed-core total-count expansion as existing coverage without inferring chronology. The supported distinct parts are the explicit four weights for specified links over a matching, the sharp asymptotic uniform through t of order n, and especially the sharp scalar-TV amplitude for that regime (including fixed t).

## value

PASS

Disjoint old triples are a natural first nonempty extension model. Recording the rare-collision local weights and uniform TV coefficient explains how a linear number of old hyperedges can sharply suppress total realizable types while barely changing a natural observable, yet leave a lattice-phase signature in its first nonvanishing change. The result deliberately does not extend to overlapping triples or full-type TV.

The dated certificate retains the supplied scientific assessment, sources and limitations.
