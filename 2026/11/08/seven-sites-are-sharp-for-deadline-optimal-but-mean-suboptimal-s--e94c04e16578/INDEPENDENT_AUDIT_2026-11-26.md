# Independent mathematical audit

## correctness

PASS

On a tree each seed-to-sentinel infection time is the sum of one independent unit exponential per unique path edge (zero at the seed). Uniform averaging gives total distance divided by n for the mean, and the miss tail e^(-t)/n times the polynomial with coefficients c_j(v)=#{u:d(u,v)>j} in the t^j/j! basis. One can check the small-order proof structurally: moving across an edge from w to m with component sizes a on w's side and b on m's side changes the total distance by a-b. A nonmedian has a neighbor on a side b>n/2; otherwise every path from it has nondecreasing total distance because forward components are nested. If n<=6 and b>a then a<=2. The difference c_j(w)-c_j(m) is the number at distance j from m on m's side minus the number at distance j from w on w's side. The side of size at most two has shell counts (1) or (1,1); the larger connected side has at least as many vertices in each such shell, with a strict inequality somewhere since b>a. Thus a nonmedian can strictly improve at every t>0. The separate finite replay also confirms median dominance for all 6212 nonmedians on 1442 labeled trees, Cayley counts (1,1,3,16,125,1296). On the given broom the distance sums are (12,11,12,15,20,17,17). Site 1 dominates each site 2–6 in every coefficient and strictly in at least one. For 0 minus 1, the replay and direct distance counts give -t+t^2/2+t^3/6, negative before its only positive root (sqrt(33)-3)/2 and positive after. Exactly 0 and 1 tie there, and their mean times are 12/7 and 11/7. The result neither covers t=0 nor asserts that this broom is the only seven-site witness.

## originality

PASS

The closest same-model indexed record changes the number of sentinels from one to two, and a nearby single-sentinel record changes the random process and score. Inspected literature gives the general outbreak detection problem, known first-passage ingredients, different SIR exact tables, and static centrality separations, not the sharp all-positive-deadline theorem and phase comparison stated here. The decision credits familiar ingredients and is bounded to the inspected corpus.

## value

PASS

For defensive monitoring, minimizing the expected wait and minimizing the probability of missing a fixed deadline are different natural choices. The result identifies exactly when the two can first diverge in a transparent tree model and exhibits an exact crossover with unique optima on both sides. The finite cutoff is therefore meaningful independently of the census and without asserting empirical application to a particular outbreak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
