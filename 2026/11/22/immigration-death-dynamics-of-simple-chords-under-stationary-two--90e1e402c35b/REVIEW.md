# Independent mathematical audit

## correctness

PASS

The forced switch has one-edge retention 1-2/n and creation 1/[n(n-1)]. Centering the sum gives the exact eigenmode 1-(2n-1)/[n(n-1)] of the full matching chain, without treating the count as Markov. Counting compatible ordered adjacency pairs gives E(S)_2=E(S)=2n/(2n-1), hence the claimed variance and all-lag covariance. The exact lag-one replay on 15, 105, and 945 matchings at n=3,4,5 gave 4/25, 20/49, and 44/81. Independently, disjoint k-tuples give the Poisson(1) initial law by factorial moments. For the path limit, the conditional expected birth and death counts are (2n-s)/[n(n-1)] and 2s/n. Stationarity bounds the probability of two deaths by E(S)_2/[n(n-1)] and reversibility gives the same bound for two births. A mixed event is bounded by four alternative reconnections per selected present short edge, so it is O(n^-2) in stationarity. Up to the time the count exceeds K, the next count can be maximally coupled to one grid step of the immigration–death chain: the conditional discrepancy is bounded by a constant times the conditional multiple-event probability plus O_K(n^-2) (the continuous-time chain has these single-jump probabilities to first order). Summing by stationarity for nT steps gives o(1) for fixed K; the expected initial count plus all births is O(1+T), so the probability of leaving the cutoff vanishes as K grows. The initial laws converge also in TV on the discrete state space. The limiting chain's finitely many jumps on a fixed horizon can be shifted to grid times in J1, since it has no fixed-time jumps. Thinning at survival probability exp(-2t) gives both limiting two-time formulas, including the void probability.

## originality

PASS

The pertinent older and indexed results already give the stationary law or its refinements, and the lazy matching process is the same forced process with holding inserted. The supported distinct claim is the stationary temporal eigen-covariance and J1 limit for the cyclic-adjacency count, with the associated two-time void law; no novelty is attributed to the chain or the static law.

## value

PASS

The familiar static count does not specify how nearby chords persist or reappear under rewiring. The exact all-lag covariance and full stationary path law resolve a natural local timescale in a globally studied Markov chain and determine joint temporal void probabilities. The path result is the substantive contribution, not a small finite calculation or a marginal Poisson approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
