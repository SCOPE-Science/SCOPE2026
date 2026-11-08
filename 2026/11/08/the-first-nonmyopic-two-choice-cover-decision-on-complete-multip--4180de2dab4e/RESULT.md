# The first nonmyopic two-choice cover decision on complete multipartite graphs

## Finding

Consider the two-choice random walk on a finite connected unweighted graph. At each step, the walker independently samples two neighbors of its current vertex, uniformly **with replacement**, and a controller selects one to minimize the expected additional steps until every vertex has been visited. An *unseen-first* action means selecting an unvisited proposed neighbor whenever one of the two offered neighbors is unvisited and the other has already been visited.

**Sharp finite cutoff.** For each connected complete multipartite graph on at most eight vertices, and for every state consisting of a visited set and current vertex, an unseen-first action is optimal whenever the two candidates differ in visited status (ties are allowed). There are exactly 58 such graph isomorphism types. Among the 29 connected complete multipartite isomorphism types on nine vertices, a strictly better visited-first action exists **only** for \(K_{1,2,6}\). In that graph, up to automorphisms, there are exactly three offending decision states, with visited-count profiles \((0,1,1)\), \((0,2,1)\), and \((0,2,2)\), the walker in the six-vertex part, the unseen offer in the singleton part, and the seen offer in the two-vertex part.

For the last profile, let \(Q_{\mathrm{new}}\) and \(Q_{\mathrm{old}}\) denote the respective **optimal expected remaining times after taking the proposed move**. Then

\[
Q_{\mathrm{new}}=\frac{863502507888814}{58892405629491},\qquad
Q_{\mathrm{old}}=\frac{136185927932950168179443}{9289655025356352195549},
\]

and

\[
\boxed{Q_{\mathrm{new}}-Q_{\mathrm{old}}=\frac{3210462360632365129}{1327093575050907456507}>0.}
\]

Thus visiting an already visited vertex is **strictly preferable** to visiting a new one, despite the immediate loss of an opportunity to increase the number of covered vertices. The initial step of the choice is common and cancels in this comparison.

## Assumptions and scope

A complete multipartite graph \(K_{n_1,\dots,n_r}\) has \(r\ge2\) nonempty parts and an edge precisely between vertices in different parts. Starting at a previously visited vertex, the controller knows the entire visited set and both proposed neighbors and may use arbitrary history-dependent policies; expected cover time is minimized over all such policies. The state space contains all vectors of partwise visited counts, whether or not a particular profile is reachable from a given start. The stated nine-vertex witness **is reachable** with positive probability: starting in the two-vertex part, traverse a path through alternately the two-vertex and six-vertex parts, visiting two vertices from each while avoiding the singleton part, then finish in the six-vertex part. Required steps can be forced by both offers agreeing on the next vertex.

The classification is within complete multipartite graphs, not all graphs. No claim of optimality for every unseen-first policy is made: when two **unvisited** candidates are offered, their relative priority may also matter.

## Proof

**1. Exchangeability reduction.** For a fixed part-size vector \(\mathbf n=(n_1,\ldots,n_r)\), let \(\mathbf x=(x_1,\ldots,x_r)\), with \(0\le x_j\le n_j\), denote the visited counts; let \(i\) be the part containing the current vertex, so \(x_i>0\). By permutations within each part that preserve visited/unvisited labels, the optimal expected remaining cover time depends only on \(\mathbf x\) and \(i\). Denote this value by \(V_{\mathbf x}(i)\). At full coverage, \(V_{\mathbf n}(i)=0\).

From part \(i\), neighbors in another part \(j\ne i\) are sampled in two types: a visited vertex in part \(j\) with probability \(x_j/(N-n_i)\), and an unseen vertex in part \(j\) with probability \((n_j-x_j)/(N-n_i)\), where \(N=\sum_jn_j\). Let \(\mathcal A_i(\mathbf x)\) be these nonzero types, and let \(q_i(a)\) be their probabilities. The continuation values are exactly

\[
C_{\mathbf x}(j,\mathrm{old})=V_{\mathbf x}(j),\qquad
C_{\mathbf x}(j,\mathrm{new})=V_{\mathbf x+\mathbf e_j}(j).
\]

Hence the stochastic shortest-path Bellman equations are

\[
V_{\mathbf x}(i)=1+\sum_{a,b\in\mathcal A_i(\mathbf x)}q_i(a)q_i(b)
\min\{C_{\mathbf x}(a),C_{\mathbf x}(b)\}.
\tag{1}
\]

**2. Properness and uniqueness.** Under any policy, from a current vertex to any prescribed unvisited vertex of a different part there is a one-edge route; to an unvisited vertex in the same part there is a two-edge route through any other part. At each required edge, the offered pair can consist of two copies of the next prescribed neighbor. Such an event has strictly positive probability independent of the policy. Therefore each missing vertex has a geometric-tailed waiting time in blocks of at most two steps, uniformly over all states and strategies. Every policy has finite expected cover time, and (1) has a unique finite optimal solution. A finite-state stationary deterministic Bellman-minimizing policy is optimal.

**3. Finite exact certificate.** Process visited-count vectors in descending order of \(\sum_jx_j\). Values reached by a new vertex are already determined. For a fixed \(\mathbf x\), only values of revisits within the same layer are unknown. Freeze the choice that minimizes a provisional continuation estimate for each ordered pair of offers, solve the resulting rational linear system for those unknown values, and repeat policy improvement until every equation (1) holds exactly. All probabilities and linear operations are rational, so the comparisons and all claimed fractions are exact. Properness makes the policy-evaluation matrices nonsingular; the finite-state policy-improvement method terminates at the unique Bellman solution. The accompanying `choice_multipartite_exact.py` implements this method using integer/rational operations and verifies the full Bellman equation at every processed state, not merely a sampled selection.

**4. Exhaustion and the witness.** A connected complete multipartite graph is specified, up to isomorphism, by an integer partition of its order having at least two parts. The exact checker enumerates all 58 such partitions of orders \(2\) through \(8\), evaluating 7,391 rational Bellman states and comparing every mixed-status offer. No strictly improving seen-first action occurs. It then exhausts all 29 partitions of order \(9\) (11,956 more Bellman states), finding the unique offending part profile \((1,2,6)\), with exactly the three stated visited-count/current-part/offer-type profiles. In particular the \((0,2,2)\) state returns the two exact fractions above, whose difference reduces to the displayed strictly positive rational number. This gives both the lower cutoff and the nine-vertex counterexample.

## Verification

Run `python choice_multipartite_exact.py` from a directory containing the included checker. It uses only the Python standard library and exhausts the indicated graph types. Run `python choice_multipartite_independent.py` for a separate **floating-point** check using labeled vertex subsets (requires NumPy); it does not enter the proof. That check converges in 183 value-iteration sweeps and reproduces both witness continuation values to better than \(10^{-9}\). The exact certificate, not that approximate computation, supplies the proof of strict inequality and minimality.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced and studied this with-replacement two-choice random walk, including the NP-hardness of an optimal cover-time next-step decision on general graphs (their Theorem 1.7). The present result resolves a different, finite structural question: the first order and isomorphism type **within complete multipartite graphs** where a locally available new vertex can be strictly inferior to a visited one, with an exact certificate. The broad NP-hardness theorem neither fixes the graph family nor implies the sharp nine-vertex classification. The earlier literature on greedy walks using unvisited edges and on locally balancing visit counts uses different transition rules or optimization criteria.

## Limitations

This is a **computer-assisted finite theorem** with an exact rational certificate, not a hand-derived symbolic inequality for all graph orders. It does not assert unseen-first optimality on multipartite graphs with ten or more vertices or on arbitrary graphs. It concerns the **conditional optimal cover-time decision** from a particular visited state, not the difference between two whole fixed strategies initialized at an arbitrary vertex. The independent floating-point cross-check is not a substitute for exact Bellman verification. No independent mathematical audit or comprehensive historical-priority certification has been performed.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170 (first public version 12 November 2019), https://arxiv.org/html/1911.05170v2 ; *Combinatorics, Probability and Computing* 31 (2022), 73–100, https://doi.org/10.1017/S0963548321000183.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, https://doi.org/10.4230/LIPIcs.ITCS.2020.76.
3. C. Avin and B. Krishnamachari, *The Power of Choice in Random Walks: An Empirical Study*, *Computer Networks* 52 (2008), 44–60, https://doi.org/10.1016/j.comnet.2007.09.012.
