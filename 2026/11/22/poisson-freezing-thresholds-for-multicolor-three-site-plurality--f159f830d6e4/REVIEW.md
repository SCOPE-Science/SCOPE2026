# Independent mathematical audit

## correctness

PASS

The center c flips only if both neighbors have the same different color b. Given that flip, each neighbor either stays b or copies the old center color c, with a copy exactly when its outer neighbor is c; the center can flip twice only if both copies occur. If the center stays c, a neighbor can only stay put or copy c, so updated agreement of both neighbors away from c would already have forced the center to flip. These exhaust the local possibilities, even when sites in the five-site notation coincide modulo n. Thus triple-AND erosion iterates to an alternating two-color word of length 2t+3. An infinite alternating cyclic word requires even n and produces a true two-cycle; counting ordered first colors gives q(q-1) states. A noncheckerboard odd ring allows at most n alternating letters, and a noncheckerboard even ring at most n-1. A full alternating linear word on an odd ring and a length n-1 alternating run with a third last color on an even ring attain the claimed bounds. For fixed L=2t+3, p=(q-1)/q^(L-1) and the joint event at offsets s=1,...,L-2 costs p q^(-s), because overlap of at least two letters fixes both colors; one-letter overlap gives independent indicators. Hence variance is at most lambda_n(1+O_L(1/q)). For bounded positive means the block argument loses o(1) expected hits at boundaries (including any last partial block), has probability o(1) of any multiple-hit block, and gives independent block-hit indicators of maximal probability o(1). This proves Poisson convergence, with the zero and diverging regimes following by Markov and the variance bound. At adjacent deadlines the expected counts differ by factors q^2, giving concentration on t and t+1, also at t=0 since T>=0. Frozen finite checks and output were inspected, not rerun; the stochastic and infinite-size assertions follow from the proof.

## originality

PASS

Binary majority ring erosion, clocks and Poisson extremes already occur in the accessible indexed work. The supported distinct claim is the exact criterion for categorical incumbent-preserving plurality with three-way ties and its fixed-deadline, growing-palette Poisson transition. Neither the binary law nor the inspected ternary median and one-sided plurality statements contain this result. Unresolved access to adjacent literature limits priority claims but is not a scientific verdict.

## value

PASS

The update is a canonical plurality extension in which true three-way ties prevent simply reusing binary disagreement runs. An exact erosion description for the actual multicolor flippers yields sharp deterministic clocks, and the hierarchy of palette scales n^(1/(2t+1)) answers whether any defects persist through a specified deadline. The quantitative two-point fixation distribution gives information beyond a recurrence classification or the known binary growing-time laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
