# Independent mathematical audit

## correctness

PASS

For cell means in [0,1], the second iterate is the expectation under P_x=b_n(x)A, where the stochastic matrix A averages Bernstein basis functions on successive cells. The increasing ratios of binomial basis functions give nonnegative two-by-two minors for both the x-indexed kernel and the averaged matrix (integrate the same minors over ordered cells); Cauchy–Binet preserves the signs in P. Its positive entries give a single negative-to-positive crossing of P_y−P_x for x<y, so its TV is the maximum upper-tail difference. Those upper tails are nondecreasing in x by the same ordering, making x=0 and 1 extremal. At the endpoints A's first and last rows are reflections; comparing t^j(1−t)^(n−j) and its reflected power on the first cell puts the positive part of P_1−P_0 exactly at j>n/2. The cell indicator therefore attains the TV upper bound with essential oscillation one. One step has disjoint endpoint cells modulo null sets. On the relevant upper half, consecutive p_{n,j} have ratio ≤1/n, so the first central term gives the even deficit and twice the first above-center term gives the odd deficit, both up to relative O(1/n). Rescaling by t=u/(n+1), the beta-density weight (j+1)u^j has E(1−u)=1/(j+2); the remaining factor (1−u/(n+1))^(n−j) differs from exp(−(n−j)u/(n+1)) by relative O(1/n) uniformly, and its average is exp(−1/2)(1+O(1/n)). This verifies both leading constants and the logarithmic order. Independent rational integration reproduced the six listed values, including n=1.

## originality

PASS

Endpoint TV and total positivity are shared techniques, not new principles. The supported distinct result is the exact endpoint overlap for the second iterate of the classical Kantorovich kernel with its parity-dependent, super-exponential deficit. The strongest catalogue and published matches inspected do not establish that specialization and asymptotic.

## value

PASS

The first power shows no uniform oscillation contraction, whereas the second has a strictly positive deficit; the exact scale and even/odd constants quantify how weak that first uniform contraction becomes as degree grows. The formula and explicit extremizing input provide sharp information for Markov or approximation estimates that a qualitative mixing result cannot give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
