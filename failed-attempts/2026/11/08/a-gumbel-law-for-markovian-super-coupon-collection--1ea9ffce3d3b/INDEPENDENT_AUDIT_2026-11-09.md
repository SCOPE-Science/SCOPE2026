# Independent mathematical audit

## correctness

PASS

The stated Johnson walk is the single-swap reversible chain on r-subsets; its inclusion-coordinate action has eigenvalues 1−j(n+1−j)/[r(n−r)] with a gap bounded away from zero for fixed r. For an s-target stationary entrance flux is (s/r)binom(r,s)/binom(n,s)=binom(r−1,s−1)/binom(n,s), not occupancy mass. Uniform fixed-k target union overlaps cost O(n^(−s−1)); the killed-chain spectral perturbation gives principal eigenvalue 1−kλ_n+O(n^(−s−1/2)), and spectral separation gives multiplicative joint avoidance at t≈(log binom(n,s)+x)/λ_n. Factorial moments lead to Poisson(e^(−x)) unseen shadows and a Gumbel cover time; union tail bounds yield the leading expectation. Independent exact finite enumeration of Johnson transitions gave stationary fluxes 1/7 for (n,r,s)=(7,3,1), 1/14 for (8,3,2), and 1/12 for (9,4,2). These checks supplement, rather than replace, the infinite proof.

## originality

FAIL

Decisively previously covered: full earlier Resultary RESULT.md from 2026-11-02, Gumbel shadow-cover times for fixed-size Johnson walks, proves for every fixed 1≤s<r the same one-element replacement walk, all-shadow cover-time Gumbel limit, Poisson missed-shadow limit and mean asymptotic at exactly a_n=binom(n,s)/binom(r−1,s−1). Current result adds no separate surviving claim beyond that previously published theorem. Its eigenvalue remainder O(n^(−s−1/2)) is actually weaker than earlier O(n^(−s−1)).

## value

PASS

A fixed-order shadow cover time in a temporally dependent Johnson walk is a motivated open coupon-collector question (Athreya–Mukherjee–Mukherjee Conjecture 2.4), requiring the correct entrance rather than occupation rate and nontrivial simultaneous avoidance. Its correctness/value remain meaningful despite exact priority loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
