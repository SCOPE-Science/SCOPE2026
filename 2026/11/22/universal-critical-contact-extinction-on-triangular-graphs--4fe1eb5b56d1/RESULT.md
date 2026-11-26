# Exact extinction-time distributions on the first two extinguishing triangular graphs

## Finding

Let \(T(n)=L(K_n)=J(n,2)\), the graph whose sites are the edges of \(K_n\) and whose adjacent sites share an endpoint. For the synchronous three-state Greenberg–Hastings rule at the half-degree contact threshold \(n-2\), the maximum first time to all rest is **exactly four updates** on both \(T(5)\) and \(T(6)\). The full labelled state counts by first time to all rest are:

| Graph | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| \(T(5)\) | 1 | 1,023 | 24,548 | 29,797 | 3,680 |
| \(T(6)\) | 1 | 32,767 | 5,733,037 | 8,327,727 | 255,375 |

These two consecutive orders are the first at which critical-contact extinction is universal on the triangular-graph family; the preceding two orders have nonzero periodic orbits. The recurrent classification identifies the onset of universal extinction, but does not give its settling time or how many initial states attain that time. For a uniformly sampled labelled initial configuration the table gives, in particular, the exact probability of requiring the full four updates: \(3680/59049\) and \(255375/14348907\), respectively.

## Assumptions and scope

Each site has state 0 (rest), 1 (excited), or 2 (refractory). At each simultaneous update, \(1\mapsto2\mapsto0\); a resting site becomes excited if at least \(n-2\) distinct neighbors were excited before the update, and otherwise remains at rest. The threshold is exactly half of the degree \(2(n-2)\). The all-rest state is absorbing, and its own first-hit time is zero. Counts distinguish all vertex labels; they do not quotient by graph automorphisms. The finite settling-time result is for \(n=5,6\) only.

## Exact calculation

Represent a state as disjoint edge sets \((X,Y)\), excited and refractory, in \(K_n\). Write \(d_X(v)\) for the degree of \(v\) in the edge set \(X\). For fixed \(X\), set
\[
E(X)=\bigl\{uv\notin X:d_X(u)+d_X(v)\ge n-2\bigr\}.
\]
For \(uv\notin X\), the two endpoint stars share no excited edge, so their degree sum counts each excited neighbor of \(uv\) once. The exact transition is therefore
\[
(X,Y)\longmapsto(E(X)\setminus Y, X).
\]

For each \(X\subseteq E(K_n)\) and each subset \(Z\subseteq E(X)\), count the first-step successor \((Z,X)\) with multiplicity \(2^{\binom n2-|X|-|E(X)|}\). Indeed, to have this successor the initial \(Y\) must contain \(E(X)\setminus Z\), avoid \(X\cup Z\), and be arbitrary on the remaining edges. Thus these groups form a disjoint partition of all \(3^{\binom n2}\) initial states. From each grouped successor, apply the displayed transition to first reach \((\varnothing,\varnothing)\), counting the initial grouped transition as one update. The sole initial all-rest state is corrected from time one to time zero. The replay enumerates 14,476 groups with total weight 59,049 for \(n=5\), and 1,662,308 groups with total weight 14,348,907 for \(n=6\); no group requires more than four updates. The Python implementation `verification/exact_grouped.py` uses only exact integer operations.

Explicit witnesses start with no refractory sites. In endpoint notation the successive excited sets, through the last nonempty set, are:

- \(n=5\): \(\{12,13,14,23\}\), then \(\{15,24,34\}\), then \(\{45\}\).
- \(n=6\): \(\{12,13,14,15,23,24,25\}\), then \(\{16,26,34,35,45\}\), then \(\{36,46,56\}\).

At time three the excited set is empty but the last nonempty excited set is still refractory. At time four both sets are empty, proving sharpness in each case.

## Relationship to other results and limitations

The triangle-locking and Johnson-graph classification [1] already supplies universal eventual extinction on \(T(n)\) for \(n\ge5\) and the two three-cycles on \(T(4)\). Its triangle theorem also gives the two three-cycles on \(T(3)=K_3\) via the six proper colorings. The general integral-spectrum criterion [2], applied with half-degree \(r=n-2\) and spectrum \(\{2r,n-4,-2\}\), likewise covers the eventual-extinction statement for \(n\ge5\). Those claims are background, not part of the contribution here. Neither recurrent-mode classification gives the exact transient data or the sharp four-update cutoff. No settling-time bound or full histogram for \(n>6\) is asserted. The counts concern a deterministic synchronous rule, not asynchronous or stochastic excitation.

## References

1. [*Triangle-locked critical excitation and the Johnson-graph extinction dichotomy*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-triangle-locked-critical-excitation-and-the-johnson-graph-extinc--76b9562220e5/RESULT.md), triangle-locking theorem and Johnson-graph application.
2. [*A twelve-step spectral ceiling for critical excitation on integral graphs*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-twelve-step-spectral-ceiling-for-critical-excitation-on-integr--3ebebc11989a/RESULT.md), §3; the ceiling concerns recurrent periods.
