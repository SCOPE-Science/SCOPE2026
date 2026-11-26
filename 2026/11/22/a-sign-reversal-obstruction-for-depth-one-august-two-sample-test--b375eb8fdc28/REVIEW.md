# Independent mathematical audit

## correctness

PASS

At depth one the first cell is the event of rank at most one among three references, or being below their median. The contrast 2 times this indicator minus one therefore gives h(u)=1−6u²+4u³. Under X∼G and Y∼F, U=F(X) has CDF Q and F(Y) is uniform, so the expectations are ∫h dQ and ∫h(Q) du. Integration by parts plus the exact cubic expansion gives the two perturbation identities. Q(0)=0, Q(1)=1; the degree-three Bernstein coefficients on the three stated subintervals are positive (replay by expressing Q'(a+(b−a)t)=∑c_i t^i; coefficient j is ∑_{i≤j} c_i binom(j,i)/binom(3,i)). Thus Q' is strictly positive and the Gaussian-composed densities are positive real analytic and distinct. Independent exact coefficient integration reproduces a=1/250, b=45549381047/5150145000000 and −ab=−45549381047/1287536250000000. Replay: set T=700Q; expand 700³−6·700·T²+4T³, integrate coefficient of u^j by dividing by j+1 (common multiplier 360360), and divide by 700³. For a use h T'/700 and the same monomial integration. Strong laws give the negative alternative limit; equivalently use uniform empirical CDF convergence and the O(1/n) replacement error for three references. In the null, E h=0, E h²=17/35, and fixing a reference uniform u gives 2E median(u,V,W)−1=−h(u)/3. The first projections are therefore exactly opposite, with higher-order degenerate terms of variance O((m+n)^−2) in the stated balanced regime. The CLT gives the scaled chi-square law, so the exact continuous-rank null's fixed-level upper-tail quantile tends to zero, giving zero limiting power against the fixed negative alternative. For the finite mean, neither overlap has mean product zero; exactly one gives −17/105, and if both distinguished draws are shared, conditioning on x<y gives the two factors 1−2x² and 1−4y+2y². Integrating their product over that triangle and doubling gives −17/45. Weighting the cases by the independent inclusion probabilities 3/m and 3/n and negating gives 17(m+n+1)/(35mn). The frozen checker and notes were inspected, not executed. No general statement at higher depth or at fixed finite sample size follows.

## originality

PASS

The original statistic, its population formula and its U-statistic asymptotics are clearly prior. The two strictly nonzero same-sign population signals, their explicit positive-analytic witness, the resulting wrong-tail failure, and the separate finite-null mean were not covered by the compared primary statements.

## value

PASS

A continuous positive-analytic counterexample to the intuitive sign of an established two-sample test identifies zero asymptotic power, not merely reduced sensitivity or two vanishing coordinates. The wrong-side signal gives a concrete reason the one-sided combination can fail. The exact rank-null mean is a useful calibration check alongside, not the main reason to accept the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
