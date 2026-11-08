# Scientific review

## Correctness

PASS. The state space, tie rule, fixed states, probability normalization and integer thresholds are explicitly defined. Strict majority flips reduce bichromatic edge count; the only traps are two equal-bit consensus states and doubly tied mixed states. First loss of a strict opposing majority selects which consensus is subsequently unavoidable. The order of first activation times of all initially eligible vertices is a uniform random permutation, yielding the exact finite sum. The order-statistic beta laws establish odd-odd fairness and parity effects. Two independently implemented exact-rational checkers cover 1,936 aggregate states and 7,684 labelled states respectively. These are checks, not substitutes for proof.

## Originality

PASS, qualified. Auletta et al. (arXiv:1402.4050) use the same deterministic local flip rule but ask existential and adversarial reachability questions, not probabilities under uniform random update order. Feldman et al. (arXiv:1408.5192) and Mohan–Prałat (arXiv:2309.04691) study asynchronous majority with initially unannounced opinions and private-signal tie resolution, and do not evaluate this bipartite absorption kernel. Accessible full-text arXiv versions were consulted for all three, including model statements and relevant results, and no relevant complete-bipartite closed winner-selection formula was observed. Searches of related nomenclature and stored prior claims disclosed no equivalent or stronger theorem. The beta-order-statistic tools themselves are classical. Residual historical-priority uncertainty remains because not all mathematical literature is indexed or searchable.

## Value

PASS. Conditional consensus selection from antagonistic community majorities is a natural quantitative question in sequential opinion dynamics. The finite-sum all-start kernel yields exact probabilities for every bipartite size, including update-order sensitivity; the size-independent fairness of *unequal odd* unanimously opposing camps and the even-size bias/large-camp limit are structural, not just isolated arithmetic examples. Neither graph shape alone nor the deterministic set of reachable states answers these probabilities. Expected absorption times and extension to other tie conventions remain open here.

Self-review: passed. Independent audit: not yet performed.
