# The seven-good threshold for failure of descending-order cumulative-envy greedy allocation

## Finding

**Theorem.** Let \(m\ge 1\) goods with nonnegative common values arrive in the fixed order \(w_1\ge w_2\ge\cdots\ge w_m\ge0\). Two agents have identical additive values, and each good is assigned irrevocably upon arrival. Let \(L_{i,t}\) denote agent \(i\)'s allocated total after \(t\) arrivals. Define cumulative maximum envy by
\[
C=\sum_{t=1}^{m}|L_{1,t}-L_{2,t}|.
\]
The **least-loaded greedy rule**, which gives each arriving good to a currently least-loaded agent, minimizes \(C\) for every such input if \(1\le m\le6\). This universal guarantee is sharp in the number of goods: with the ordered seven-good values \((6,5,5,4,4,1,1)\), greedy has \(C=20\) while the exact minimum is \(18\).

## Assumptions and scope

The values are identical across the two agents, additive, real, finite, and nonnegative. The arrival order is fixed and nonincreasing; the allocator may know all future values. Zero-valued goods and ties are permitted. A greedy tie may be resolved arbitrarily: it never affects the absolute load difference. We optimize the sum of worst pairwise envy at all prefixes, not final envy, makespan, or envy-freeness up to one good. The classification varies the number of goods and holds uniformly over all allowable real weights.

## Proof

**Reduction to signed prefixes.** Put \(D_t=L_{1,t}-L_{2,t}\), initially \(D_0=0\). Assigning good \(t\) to one of the two agents adds \(\sigma_t w_t\) to \(D_t\), where \(\sigma_t\in\{-1,1\}\). Thus every allocation has cost \(\sum_t|\sum_{j\le t}\sigma_jw_j|\). Interchanging agent labels allows \(\sigma_1=1\), leaving precisely \(2^{m-1}\) candidate sign assignments. Greedy has discrepancy magnitude \(d_0=0\), \(d_t=|d_{t-1}-w_t|\).

**Universal bound for one through six goods.** For \(m=1\), both assignments have the same cost. When \(2\le m\le6\) and \(w_1>0\), divide all weights by \(w_1\), so \(w_1=1\); rescaling costs restores the general case. If \(w_1=0\), all weights and costs vanish. For each binary greedy branch \(h_2,\dots,h_m\in\{-1,1\}\), set \(h_1=-1\), \(g_0=0\), and
\[
g_t=h_t(g_{t-1}-w_t),\qquad g_t\ge0.
\]
On the polyhedral region defined by these inequalities, \(g_t=d_t\) exactly, including all tie boundaries. For each candidate allocation sign vector \(\sigma_1=1\), \(\sigma_2,\dots,\sigma_m\in\{-1,1\}\), define linear signed prefixes \(S_t=\sum_{j\le t}\sigma_jw_j\). Introduce unrestricted auxiliary variables \(y_t\) with \(y_t\ge S_t\) and \(y_t\ge-S_t\). The objective
\[
F=\sum_{t=1}^{m}y_t-\sum_{t=1}^{m}g_t
\]
is then at least the allocation's actual cost minus greedy cost, with equality upon taking \(y_t=|S_t|\).

Write \(x=(w_1,\ldots,w_m,y_1,\ldots,y_m)\). The constraints consisting of \(w_{i+1}-w_i\le0\), \(-w_m\le0\), \(-g_t\le0\), and \(\pm S_t-y_t\le0\), in that exact order, form an integer matrix inequality \(Ax\le0\), together with \(w_1=1\). The objective has an integer coefficient vector \(c\) with \(F=c^\mathsf T x\). For **every** greedy branch and competing sign vector, the attached exact certificate supplies nonnegative rational multipliers \(z\) and \(\eta\) such that
\[
c=-A^\mathsf Tz+\eta e_1,\qquad \eta\ge0.
\]
Consequently every feasible \(x\) satisfies \(F=-z^\mathsf T Ax+\eta\ge0\). This shows that the greedy cost is no greater than any competing allocation cost on every branch. The attached verifier reconstructs the integer matrices independently and checks each displayed dual identity in exact rational arithmetic. The certificate covers \(\sum_{m=2}^{6}4^{m-1}=1364\) cases, with none omitted. Therefore greedy is globally optimal for all ordered nonnegative real inputs with at most six goods.

**Sharpness at seven goods.** For \((w_t)=(6,5,5,4,4,1,1)\), the greedy absolute discrepancy sequence is \((6,1,4,0,4,3,2)\), which sums to \(20\). The alternative signs \((+,-,+,-,-,+,+)\) give absolute discrepancies \((6,1,6,2,2,1,0)\), which sum to \(18\). Exhausting all \(2^6=64\) sign allocations with \(\sigma_1=1\) gives exact minimum \(18\). Thus the universal greedy property fails at seven and nowhere earlier.

## Verification

Run `python3 certificates/verify_duals.py` in the extracted package directory, using only Python's standard library. It reconstructs each integer inequality matrix and objective from its sign code, checks positivity of all rational dual coefficients, verifies each coordinate of every exact dual identity, checks that all sign-code pairs for each length were included, and independently enumerates all 64 seven-good allocations. The certificate generation may use floating-point optimization, but the supplied proof check uses exact `Fraction` arithmetic and does not trust optimizer output. Success prints two `PASS` lines. File integrity can be checked using the SHA-256 and byte counts of the containing distribution record.

## Relationship to prior work

Goldberg, Robinson, and Teh introduced cumulative maximum envy as an objective, proved hardness for fixed arrival orders, and provided generic dynamic programming and approximation results. They discuss shortest-processing-time-first ordering for their sequencing variant and recognize longest-processing-time-first (descending) greedy as a classical rule with EFX consequences, but do not supply its precise fixed-descending-order cumulative-cost optimality threshold for two identical agents. Their exact algorithm could evaluate particular finite instances; it does not by itself imply the uniform real-valued sharp theorem proved here. Elkind and colleagues' temporal EF1 results concern existence of prefix-fair allocations rather than optimal minimization of summed envy. Classical longest-processing-time scheduling analyzes makespan and other load statistics, not this prefix sum objective.

## Limitations

The six-good conclusion depends on both **two** agents and the fixed **nonincreasing** order. It does not establish optimality for increasing or arbitrary orders, or any positive approximation bound at longer horizons. The seven-good example proves the earliest possible failure, not a maximal approximation ratio. The computer-assisted finite step has a human-reconstructible linear-programming reduction and a complete exact rational certificate; independent external assessment has not been conducted. Prior publication could contain an equivalent formulation not identified during the literature search.

## References

- P. W. Goldberg, I. Robinson, N. Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items*. Public presentation, 19th SAGT, September 16, 2026, [conference program](https://www.uni-augsburg.de/de/fakultaet/fai/conferences/sagt-2026/); open manuscript first posted October 7, 2026, [arXiv:2610.09843](https://arxiv.org/abs/2610.09843).
- E. Elkind, A. Lam, M. Latifian, T. Y. Neoh, N. Teh, *Temporal Fair Division of Indivisible Items*, [arXiv:2410.14593](https://arxiv.org/abs/2410.14593), October 18, 2024.
- F. Della Croce, R. Scatamacchia, *Longest Processing Time rule for identical parallel machines revisited*, [arXiv:1801.05489](https://arxiv.org/abs/1801.05489), 2018 (different objective: makespan).
