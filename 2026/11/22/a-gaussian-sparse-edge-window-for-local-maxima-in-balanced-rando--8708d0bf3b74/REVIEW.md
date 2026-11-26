# Independent mathematical audit

## correctness

PASS

Each cross-edge is examined only by its later endpoint, so conditional independence in a given side word is exact. The degree argument integrates E[1/(1+D)] = integral_0^1 (1−p+px)^n dx, giving the finite mean, even for p=1. Reconstructed the crucial variance independently by a Doob martingale: given the first i fair letters with counts A_i,B_i, the expected future sum of q^{opposite count} is (q^{A_i}+q^{B_i})/p. Thus the martingale increments take the two equally likely values ±(q^{A_i}−q^{B_i}) at the next position. Their squared expectations sum over i≥0 to 2 sum_i[((1+q²)/2)^i−q^i] = 2/(1+q). L² convergence of the conditional-expectation martingale follows from M in L² (Minkowski bounds its L² norm by the convergent sum of ((1+q²)/2)^((j−1)/2)). Therefore p[M(q)−M(q²)]→1 and sqrt(p)(M(q)−2/p)→0 in L². Conditional Bernoulli Berry–Esseen is valid for the countable sum by finite truncation; conditional variances are asymptotically 1/p in probability, and mixing this bound plus Slutsky proves the infinite model CLT. In the finite balanced word the next-step sign probability differs by at most (j−1)/(2(2n−j+1)); the matched-prefix probability therefore tends to one for K=ceil(20 log(1/p)/p). The finite tail bound uses Maclaurin on n weights q and n−1 weights 1 after conditioning on the side at j; both tails are O(p^9). The exact finite mean differs from 2/p by o(p^−1/2). Lemma 1 of the source applies to the specified recoloring rule, using reversal of the uniform ordering convention when needed. The frozen checker was inspected, not executed; its finite enumeration corroborates the conditional law, not the CLT.

## originality

PASS

Best-of-knowledge pass for the balanced varying-p result and exact environmental cancellation. The key source explicitly leaves the bipartite p→0 regime open; its assertion about variance contributions is not valid for the infinite balanced environment as p→0.

## value

PASS

It resolves a quantified portion of a real sparse-regime question for a known random-order graph statistic. The bounded exact environmental variance is the main structural contribution: it explains why leading fluctuations here are Bernoulli edge noise, in contrast to the generic interleaving heuristic. The coupling window is sufficient, not shown optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
