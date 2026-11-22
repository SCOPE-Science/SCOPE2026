# Likelihood-ratio domination through ten vertices in subcubic parking graphs

## Finding
Let \(G\) be any finite, simple, **connected** graph with \(1\le |V(G)|\le10\) and maximum degree \(\Delta(G)\le3\). Define \(U_G\) as the cardinality of a uniformly chosen maximal independent set, and \(S_G\) as the number of vertices occupied by random sequential parking: repeatedly select an available vertex uniformly, occupy it, and exclude its closed neighborhood. Write \(u_G(k)=\Pr(U_G=k)\) and \(s_G(k)=\Pr(S_G=k)\).

**Theorem (finite exhaustive likelihood-ratio order).** For all integers \(k<\ell\) with \(u_G(k)u_G(\ell)>0\),
\[
s_G(k)u_G(\ell)\le s_G(\ell)u_G(k).
\]
Equivalently, the ratios \(s_G(k)/u_G(k)\) increase weakly over their common support. In particular \(U_G\le_{\mathrm{st}}S_G\), but the conclusion is stronger than first-order stochastic dominance. The connected-graph census contains exactly \(2,571\) isomorphism classes through ten vertices, with no likelihood-ratio violation. For the three previously unreported sizes \(8,9,10\), the respective class counts are \(194,531,1733\). Among the ten-vertex classes, \(1687\) have different occupancy-size distributions in the two models and \(46\) have identical size distributions.

## Assumptions and scope
The graph is finite, loopless, simple, connected and unweighted; every vertex has degree at most three and the order is at most ten. Selections are uniform over the still-available vertices, with no returns, weights, or early stopping. A maximal independent set is independent and dominates every vertex. All maximal independent sets occur with positive sequential probability, since an ordering that puts their elements first realizes them, so the two size laws have exactly the same support. No assertion is made for eleven or more vertices, or for disconnected graphs under likelihood-ratio order.

## Proof
**1. Complete inductive graph census.** Every finite connected graph with at least two vertices has a non-cut vertex: take a leaf of a spanning tree and delete it, leaving a connected spanning subtree. Thus each connected subcubic graph \(H\) with \(n+1\) vertices can be obtained by deleting such a vertex \(v\) and then reattaching it to \(1\), \(2\), or \(3\) different vertices of the connected subcubic graph \(H-v\). Those attachment vertices have degree at most two in \(H-v\). Starting with the unique one-vertex graph, the algorithm `verify_census.py` generates every such attachment and retains one member of each graph-isomorphism class. Its isomorphism test performs an explicit bijection search, preserving adjacency in both directions. Degree profiles, neighbor-degree profiles and iterative color-refinement signatures are used only as *necessary* prefilters for isomorphism: graphs with distinct signatures cannot be isomorphic, and every pair within one signature class is compared by an exact backtracking bijection. Thus the generation is exhaustive by induction and neither a hash collision nor a distinct representation can suppress a missing isomorphism type.

**2. Exact probability computation.** For an induced available vertex subset \(A\), let \(f_A(k)\) be the sequential probability of ultimately selecting \(k\) vertices, with \(f_\varnothing(0)=1\). Conditioning on the first selected available vertex gives the exact finite recurrence
\[
f_A(k)=\frac{1}{|A|}\sum_{v\in A}f_{A\setminus N_G[v]}(k-1),\qquad A\ne\varnothing.
\]
The implementation memoizes the recurrence over vertex bitmasks and uses exact rational arithmetic. For the static model it considers every subset \(I\subseteq V(G)\), accepts it if and only if \(I\) is independent and \(I\cap N_G[v]\ne\varnothing\) for every \(v\), and counts accepted subsets by size. This is exactly uniform selection from all maximal independent sets.

**3. Exhaustive inequality certificate.** The code evaluates the two laws for every generated class, sorts the shared cardinality support, and checks with exact fractions that \(s_G(k)/u_G(k)\) is nondecreasing at every adjacent pair in that support. Adjacent inequalities imply all the displayed inequalities. No floating-point tolerance or sampling is used for the acceptance test. The complete enumerated counts are:

| \(|V(G)|\) | Connected subcubic classes | Different size laws | Equal size laws | Likelihood-ratio failures |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 0 |
| 2 | 1 | 0 | 1 | 0 |
| 3 | 2 | 1 | 1 | 0 |
| 4 | 6 | 3 | 3 | 0 |
| 5 | 10 | 5 | 5 | 0 |
| 6 | 29 | 20 | 9 | 0 |
| 7 | 64 | 55 | 9 | 0 |
| 8 | 194 | 172 | 22 | 0 |
| 9 | 531 | 508 | 23 | 0 |
| 10 | 1733 | 1687 | 46 | 0 |

The inference to first-order stochastic domination is the standard single-crossing consequence of monotone likelihood ratios on a common finite support. This completes a **finite computer-assisted proof**, not an inference about unbounded graph order.

## Verification
Run `python3 verify_census.py 10` with a standard-library Python installation to reproduce all graph classes, exact distributions and inequality checks. Its terminal output is included in `census_output.txt`. Independently, `python3 verify_orders.py` enumerates every priority permutation for all \(49\) connected subcubic graph classes on at most six vertices and checks the resulting rational laws against a separately implemented first-choice recurrence; the results appear in `orders_output.txt`. An additional NetworkX-based independently implemented enumerator returned the same class counts \(194,531,1733\) at orders \(8,9,10\), but is not needed by the standalone proof. The verifier is deterministic and uses no external graph census, numerical probability approximation, or network access.

## Relationship to prior work
Higuita-Diaz, López and Roldán-Correa (arXiv:2611.14718v1, first publicly submitted November 10, 2026) prove first-order stochastic dominance on paths and cycles, report general connected-graph comparability through order seven, and conjecture first-order dominance for all maximum-degree-three graphs. Their accompanying public repository describes random tests of the degree-three conjecture and exhaustive general-graph search, but the inspected paper does not give this likelihood-ratio statement or the exhaustive order-eight-through-ten subcubic census. Prior related studies of random-greedy versus uniform maximal-independent-set measures describe individual-configuration uniformity on cycles and clique bouquets; those are different from the occupancy-size likelihood-ratio inequalities claimed here. Literature indexing and unpublished computational outputs may nonetheless contain stronger or equivalent results.

## Limitations
This is an exact *finite* bound, not a proof of the conjecture for all subcubic graphs. Likelihood-ratio order of the total size is not an assertion of uniformity over individual maximal independent sets. The certificate depends on the correctness of a small deterministic finite program and its mathematically justified generation and recursion; direct-order enumeration independently checks only sizes through six. Exhaustive external historical priority cannot be established from available sources, and independent mathematical audit has not been performed.

## References
1. R. Higuita-Diaz, L. López and A. Roldán-Correa, *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1 (November 10, 2026), https://arxiv.org/html/2611.14718v1.
2. L. López, accompanying code repository, *Stochastic Dominance DPP Graphs* (2026), https://github.com/lykoslopezrivera-blip/Stochastic_Dominance_DPP_Graphs.
3. Related published mathematical records: *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles* (October 18, 2026), and *Exact greedy-law balance and infinite non-equicardinal uniform clique bouquets* (October 18, 2026), available through published-finding corpus research records.
