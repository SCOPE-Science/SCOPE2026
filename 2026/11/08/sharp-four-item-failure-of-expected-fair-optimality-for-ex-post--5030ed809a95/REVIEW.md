# Independent mathematical audit

## correctness

PASS

For two agents and mutually independent Bernoulli(p_j) values on each agent-good pair, per-agent EF1 failure is explicitly enumerable, and cross-agent events multiply. With m=3 an ex-ante EF partition can be parametrized by (x+y,x,y), and balanced singleton probability exceeds alternatives by y² and x²; empty-bundle allocations cannot improve. For m=4 with p=(eps,1/3,2/3,1/3+eps), A={1,3}|{2,4} is exactly ex-ante EF while B={3}|{1,2,4} is not. Computing A and B EF1 probabilities from independent Bernoulli vectors gives difference eps*(19-652eps+48eps²-36eps³)/729; its cubic is strictly decreasing over (0,1/3), with unique positive crossover ~0.0292025. At eps=1/60 the exact excess is 5431/29160000. Integer subset-sum weights (1,20,40,21) confirm A and its complement are all ex-ante EF partitions. Independently computed two-agent joint probabilities by finite exact Fraction enumeration (A=27909869/29160000, B=10339/10800) and verified gap and polynomial simplification. General m<=3 proof is analytic.

## originality

PASS

This is a sharp four-item counterexample to expected-EF optimality for realized EF1 when item probabilities are heterogeneous but common across agents, a different slice from all-agent iid Bernoulli EF1. The primary Igarashi-Oh exact-EF paper is not full-text accessible and remains a priority risk; best-of-knowledge O PASS with qualification.

## value

PASS

A concrete smallest-good-number counterexample disproves a natural probability-optimality extrapolation from ex-ante expected fairness to ex-post EF1. The sharp analytic parameter window and exact unique expected-fair partition make the witness robust and reproducible. Its small numerical gain is not the sole motivation; the precise m<=3 versus m=4 boundary is the mathematical point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
