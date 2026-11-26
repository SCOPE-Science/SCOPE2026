# Independent mathematical audit

## correctness

PASS

Every path from depth i+1 to the root must reach depth i. Conditional on the first visit and observed history, future independent offers admit at most the optimal depth-i success probability with the remaining time, bounded by the full-horizon value. Thus value is nonincreasing in depth for every horizon. Bellman maximization always admits parent-first as an optimizer, with no restriction to stationary or deterministic competitors; the forced leaf step and zero-horizon boundary are covered. Under that rule p=1−(b/(b+1))², the leaf transition is inward with certainty, and first-step decomposition of downward passage gives J_i=zp+zqJ_{i+1}J_i with J_h=z, hence denominators positive on [0,1]. Strong Markov gives the product of successive independent crossing PGFs; multiplying by 1/(1−z) converts masses to optimal cumulative deadline probabilities. For h=1 the product is z as required. The uploaded finite verifier was inspected, not executed; no asymptotic or all-policy conclusion is based on its checks.

## originality

PASS

The narrowed simultaneous stochastic-optimality statement and exact evaluation of optimal finite-deadline probabilities survive the prior-law overlap on the inspected evidence. No claim is made that the radial continued-fraction method or the large-height regimes themselves are new.

## value

PASS

A strategy that optimizes a mean may fail at a hard deadline. This result identifies a single policy attaining every finite deadline bound even against history-dependent randomized strategies, and gives those attainable probabilities without building a state space exponential in tree height. That decision guarantee, not the textbook first-step recursion or the covered fluctuation transition, motivates the repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
