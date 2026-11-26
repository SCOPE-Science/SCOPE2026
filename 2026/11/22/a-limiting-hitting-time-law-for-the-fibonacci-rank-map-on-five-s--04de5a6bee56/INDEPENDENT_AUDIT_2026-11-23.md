# Independent mathematical audit

## correctness

PASS

The prime-power ranks and lcm rule give (a',b',c')=(max(u(a),2·1_{b>0}), max(1_{a>0},b−1,0),c), with u=(0,0,1,1,2,3,…) and u(a)=a−2 for a≥3. Lemmas 2.2–2.3 supply the nontrivial 2/3-ranks and the lcm; the 5-rank is also obtained from Lemma 2.9 using z(5)=5 and F_5=5, while z(1),z(2),z(4) follow from initial Fibonacci numbers. In the invariant a≥2,b≥1 quadrant the deficits from (2,1) decrease by (2,1) truncated at 0, so the time is the maximum of the two integer clocks. For a=1,b≥1 the first step goes to (2,max(b−1,1)); a=0,b≥2 goes to (2,b−1). For a≥4,b=0 the first step goes to (a−2,1). The exceptional chain (1,0)→(0,1)→(2,0)→(1,1)→(2,1) also handles these boundary times and (3,0) goes to (1,1). The origin is fixed. Hence the record's exact formula and a uniform absolute difference at most 4 from max(a/2,b) follow. With L=log X the unit cubes based at eligible integer exponents contain the budget-L simplex and fit in the budget-(L+log 30) simplex. Inclusion–exclusion shifts the first two coordinates by floor(2tL)+1 and floor(tL)+1; rounding costs O((L+1)^2) uniformly after positive-part truncation. Replacing the continuous clocks by H affects only fixed-width strips with O((L+1)^2) points. Division by the Θ(L³) denominator gives the stated uniform CDF error. The limit is the maximum of two scaled coordinates of a uniform simplex point. Since A>B, it has support [0,1/B] with mass in every interior open interval. Bounded support uniformly for large L allows integration of the error, and each cubic tail integrates to 1/(4q). Independent modular recurrence replay checked 216 triples (0≤a≤8, 0≤b≤5, 0≤c≤3), including arrival and first-hit times, and exponent iteration 63,001 pairs with a,b≤250. Exact-cutoff sampling at 10^6, 10^12, 10^24 and 10^36 corroborates the distribution; it cannot establish the stated error rate. Replay: /workspace/branches/0f4c8041-0546-4e2b-8ce5-ff57aaddd7e4/independent_check.py. Supplied code was inspected, not run.

## originality

PASS

The rank identities, fixed-point set, and the exact pure-two-power hitting times (also lifted to 2^a5^c by the prior iterated lcm result) are not novelty. The main addition is the smooth-height sampling theorem with an explicit uniform quantitative CDF and mean, using the complete mixed-exponent dynamics. No statement in the inspected work covers that law.

## value

PASS

Five-smooth inputs give an invariant domain containing all the fixed points, not a cutoff selected after computation. The theorem supplies typical first-passage behavior, an explicit compactly supported fluctuation law, and an O(1) error for the mean time on that domain. Those results go beyond confirming eventual convergence or giving sample trajectories. No assertion for uniform unrestricted integers is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
