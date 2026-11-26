# Independent mathematical audit

## correctness

PASS

For adsorption from the empty graph, first run the internal dimer processes with all spokes suppressed. Conditional on these paths, survival of the hub is the event that no spoke to a then-vacant blade vertex rings; the first such ring would also be accepted in the actual process. For a blade with 2j vacancies the internal holding time is exponential of rate alpha*j*(2j-1); the holding times along the even-size descent are independent by the Poisson restart property and the fact that the total rate depends only on j. The conditional no-spoke factor during that hold is exp(-2j*beta*T_j). Its expectation produces (2j-1)/(2j-1+2b), and independent blade paths give the rth power. An odd blade leaves a vacant vertex forever in the suppressed process, precluding survival for positive beta even when other sizes differ. The gamma ratio has the stated constant and exponent. Writing -log P as r times the sum of log(1+b/(j-1/2)) gives rb(log k+O(1))+O(rb^2) uniformly for small b. If rb log k stays bounded, b tends to zero and the errors vanish. For the divergent case, monotonicity in b bounds P above by the probability at b=L/(r log k) for each fixed L>0 eventually; letting L tend to infinity gives zero. This checks both limits without needing a uniform fixed-b gamma expansion.

## originality

FAIL

The exact finite two-impurity law in the distinct same-date record 8fcef0aa0356 already evaluates the one-blade avoidance probability at every size and positive rate by identifying the two impurity clocks at each native vertex with one clock of summed rate. Windmill survival then factorizes over the disjoint blade clock families on the event of no hub adsorption. Thus the full weighted product follows by a direct reduction, and both joint limits follow from elementary uniform bounds on its logarithm. This is affirmative coverage by implication, not a priority inference from the date or an assertion that the other record literally studies windmills.

## value

FAIL

Hub survival is a natural statistic, but the stated exact law is the already evaluated clique avoidance factor multiplied across independent tests. The crossover is a direct uniform logarithmic estimate of the known factor, not a different asymptotic regime requiring a new analysis of coupled dynamics. No distinct valuable exact fact remains in the frozen claim beyond this reduction and estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
