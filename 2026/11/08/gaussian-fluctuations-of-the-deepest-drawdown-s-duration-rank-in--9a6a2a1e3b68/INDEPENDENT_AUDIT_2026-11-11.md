# Independent mathematical audit

## correctness

PASS

Solved the finite gambler-ruin recurrence to reconstruct the generating function D_h(z) of exact depth and duration; at z=1 depth has geometric exponential tail and H_max=(log n)/alpha+O_P(1). The analytic logarithm of u(e^s) gives conditional duration mean 2h/delta and variance 8pqh/delta^3. The forced initial loss step yields Catalan P(L=2m)=C_(m-1)p^m q^(m-1) and t^(-3/2)exp(-beta t) length tails. Chernoff concentration holds simultaneously across deterministic O(log n) thresholds, avoiding illicit independence at adaptive L_I; this gives O_P(1) rank relation and joint Slutsky limit. Independently checked exact gambler-ruin height laws for h=1..9 at p=3/4, and read source rational checker. No deterministic-calendar-time result.

## originality

PASS

Wu (2026, arXiv:2610.41990) treats this same excursion/rank statistic, and its Theorem 1 and Example 2 *already establish* rank n^(1-rho+o_P(1)) and first-order duration ratio. Perfilev–Wachtel (2019) establish conditional CLT for a single large-height excursion, a prior component. Neither primary paper states the selected empirical rank sqrt(log n) Gaussian or the uniform threshold O_P(1) relation; these are the surviving advances, not the first-order exponent or single-excursion CLT.

## value

PASS

A natural second-order uncertainty law for a widely studied drawdown ranking statistic, including explicit correlation -1 and Catalan logarithmic rank correction; quantifies fluctuation beyond existing first-order exponent and is not a contrived finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
