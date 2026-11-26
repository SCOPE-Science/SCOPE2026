# Independent mathematical audit

## correctness

PASS

With the same independent masks in both paths, the KL chain rule gives the sum of conditional total correlations under the joint sampler. Given the old sites, unrevealed gaps are independent Markov bridges, and the conditional total correlation within a gap sums the mutual information between consecutive new sites conditioned on the two old endpoints. For two such sites d apart with endpoint offsets l,r, the Markov entropy identity H(X_v|X_u,X_w)=h(v-u)+h(w-v)-h(w-u), h(d)=log 2-I_f(d), gives precisely the four-term difference in (1). Weighting the old endpoints and absence of intervening old or new sites gives the stated p²q² and two geometric factors. With no old sites the selected process is a thinned Markov chain, giving the p=0 limit in (2); with all sites already revealed the cost is zero. At fixed f>0 the denominators in (2) are bounded below by 1-lambda² and the numerator factor q²(1-p)² equals the squared cumulative increment, ensuring continuity at saturated and empty rounds and hence existence of minimizers. Expanding I_f(d) in positive even powers and summing the geometric factors gives (2) term by term. Dominated convergence yields first-wave cost q log 2 for f/q→0 and q→0. For later waves use K=p/(4f); on k/K in a compact positive interval the kth term is asymptotic to q/(4K²)(1+k/K)^(-2) when p→0, f/p→0 and p/q→0. The full term is bounded by C q f²/(p+fk)² using 1-(1-p)(1-q)lambda^(2k)≥q, so the tails can be removed uniformly in the rescaled sum. The integral equals 1 and the cost is fq/p including q=1. Restriction to k of order (p+f)/f, with p≤1/2, gives the uniform lower bound cfq²/((p+f)(p+q+f)). The proposed trial supplies O(f^((m-1)/m)); the lower bound bounds each (p_i+f)/(p_(i-1)+f) by C f^(-1/m) up to and including the first crossing of one-half. Their product cannot cross one-half in fewer than m rounds. The full product then also bounds every ratio from below at the same scale, uniformly over minimizers. This puts every minimizer in the same compact rescaled region, and the m limiting positive cost terms multiply to log 2. Equality at the sharp AM–GM value fixes every rescaled fraction uniquely. This is convergence of all minimizers, not finite-f uniqueness or a terminal-output guarantee. The supplied finite checks were inspected, not run.

## originality

PASS

There is exact statement-level overlap at m=2 and m=3. Baule's exact screened functional and the more general Secchi–Zanella path-KL functional, Markov profile and stationarity recursion are prior inputs/frameworks. The supported distinct result is the sharp singular limit and all-minimizer localization for arbitrary fixed m, in particular beyond the already recorded two- and three-round cases. General representations and stationarity do not perform the uniform-in-schedule singular-limit proof or distinguish the global minimizers in this regime.

## value

PASS

A fixed number of Bernoulli reveals in an increasingly ordered chain is a practically and mathematically distinct limit from a smooth many-round decoder. The result identifies the sharp entropy penalty and forces the intermediate rates of every minimizing schedule, rather than supplying one plausible schedule or computing one more round count. The uniform localization/variational argument resolves the all-fixed-m hierarchy even after accounting for the prior small-round formulas and almost exact general optimization frameworks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
