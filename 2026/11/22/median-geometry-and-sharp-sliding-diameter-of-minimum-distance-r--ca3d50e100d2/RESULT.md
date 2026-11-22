# Median geometry and sharp sliding diameter of minimum distance-radius domination on paths

## Finding

Let \(P_n\) be the labelled path on \(1,\ldots,n\), let \(n\ge1\) and let \(r\ge2\) be an integer. A set \(D\) *distance-\(r\) dominates* \(P_n\) when every path vertex has distance at most \(r\) from some vertex of \(D\). Consider all minimum-cardinality such sets, adjacent when one selected vertex moves by one path edge and the new set remains minimum distance-\(r\) dominating.

Put
\[
 k=\left\lceil\frac{n}{2r+1}\right\rceil,
 \qquad d=(2r+1)k-n,\quad 0\le d\le2r.
\]
The resulting reconfiguration graph \(\mathcal G_{n,r}\) is **connected and median**. Its vertex count and diameter are exactly
\[
 |V(\mathcal G_{n,r})|
 =\binom{d+k}{k}-2\mathbf1_{d>r}\binom{d-r-1+k}{k},
 \qquad
 \operatorname{diam}(\mathcal G_{n,r})=kd-2\max\{d-r,0\}.
\]
For \(d=0\), the graph consists of one vertex. Its minimum dimension as an isometric subgraph of a hypercube equals its diameter, \(kd-2\max\{d-r,0\}\).

In fact, every pair of configurations has an explicit optimum token-slide route. Encode each configuration by a sorted length-\(d\) vector \(a=(a_1,\ldots,a_d)\) with entries in \(\{0,\ldots,k\}\), as described below. The exact graph distance is
\[
 \operatorname{dist}_{\mathcal G_{n,r}}(a,b)=\sum_{j=1}^{d}|a_j-b_j|.
\]
The interpretation of this distance in terms of general tree-hitting-set reconfiguration is known; the new structural classification is the explicit median interval, its optimum binary embedding dimension, the cardinality and the sharp endpoint-capacity diameter transition for all \(r\ge2\).

## Assumptions and scope

The path has distinctly indexed vertices. Each configuration is a *set* (no coincident selected vertices) with the minimum size \(k\), and exactly one selected vertex may slide by one edge per move; intermediate sets must retain distance-\(r\) coverage. These are not token-jumping moves, and the adjacency rule is on the **original path** rather than its graph power. All results hold for every integer \(r\ge2\) and \(n\ge1\), including \(k=1\) and the cases where the reconfiguration graph is a singleton. Binomial coefficients with upper argument less than the lower nonnegative argument are interpreted as zero.

For a sorted set \(D=\{p_1<\cdots<p_k\}\), define the \(k+1\) uncovered-between-selected gaps
\[
 g_0=p_1-1,\qquad g_i=p_{i+1}-p_i-1\ (1\le i<k),
 \qquad g_k=n-p_k.
\]
Define capacities \(c_0=c_k=r\), and \(c_i=2r\) for \(1\le i<k\), and define deficits \(h_i=c_i-g_i\). Write the index \(i\) a total of \(h_i\) times, in weakly increasing order, to obtain \(a=(a_1,\ldots,a_d)\). The empty vector is allowed when \(d=0\).

## Proof

**1. Exact configurations and the deficit space.** The selected radius-\(r\) balls cover the path if and only if
\[
0\le g_0,g_k\le r,\qquad 0\le g_i\le2r\quad(1\le i<k).
\]
Indeed, the first ball must cover vertex 1, the last must cover vertex \(n\), and no two successive balls may leave an integer vertex uncovered. A selected vertex covers at most \(2r+1\) vertices, so any covering set has size at least \(k\). Conversely, with that \(k\), the vector of deficits putting \(\min(d,r)\) units at slot zero and any residual units at slot \(k\) is admissible and reconstructs a covering set with exactly \(k\) vertices. Thus the optimum size equals \(k\).

Since \(\sum_i g_i=n-k\) and \(\sum_i c_i=2rk\), the nonnegative deficits satisfy
\[
 \sum_{i=0}^k h_i=d,\quad h_0,h_k\le r,
 \quad h_i\le2r\text{ for }0<i<k.
\]
Because \(d\le2r\), all interior upper bounds are automatic. The gap formula reconstructs the unique ordered selected set; hence there is a bijection between minimum covering sets and weak compositions of \(d\) into \(k+1\) slots with the two endpoint caps \(r\).

A slide \(p_i\mapsto p_i+1\) increases \(g_{i-1}\) by one and decreases \(g_i\) by one, i.e. moves one deficit unit from slot \(i-1\) to slot \(i\). The opposite slide reverses this move. The capacity inequalities ensure that exactly the feasible one-unit adjacent-slot movements occur; this also enforces distinct selected vertices.

**2. Distributive interval and median structure.** For a weakly increasing sorted deficit vector \(a_1\le\cdots\le a_d\), the endpoint caps require at most \(r\) entries equal to zero and at most \(r\) entries equal to \(k\). Consequently its coordinatewise smallest and largest possible values are the sorted vectors
\[
 L=(\underbrace{0,\ldots,0}_{\min(d,r)},
       \underbrace{1,\ldots,1}_{(d-r)_+}),\qquad
 R=(\underbrace{k-1,\ldots,k-1}_{(d-r)_+},
       \underbrace{k,\ldots,k}_{\min(d,r)}).
\]
Here \((x)_+=\max\{x,0\}\). For \(d=0\), both are empty. The feasible sorted vectors are *exactly* the weakly increasing integer vectors \(a\) with \(L\le a\le R\) coordinatewise. This remains true for \(k=1\); the inequality \(d\le2r\) ensures \(L\le R\).

Reversing coordinates, the row lengths \(a_d,a_{d-1},\ldots,a_1\) are those of an order ideal in the \(d\)-by-\(k\) grid poset (Young diagram convention). The interval between the ideals corresponding to \(L\) and \(R\) is isomorphic to the lattice of order ideals of the *induced difference poset* \(I(R)\setminus I(L)\). Each feasible one-unit slide adds or removes precisely one poset element: it is an edge of this lattice's Hasse graph. Hence the reconfiguration graph is the Hasse graph of a finite distributive lattice, and therefore a median graph. The ideal-incidence indicator vector gives an isometric binary embedding with
\[
 |I(R)\setminus I(L)|=\sum_{j=1}^{d}(R_j-L_j)=kd-2(d-r)_+
\]
coordinates. In an order-ideal lattice, deleting elements maximal outside the target and inserting missing elements minimal in the target yields a shortest path of length \(|I(a)\triangle I(b)|=\sum_j|a_j-b_j|\). This proves the stated all-pairs metric and connectivity.

**3. Sharp diameter and binary dimension.** For any feasible \(a,b\), their coordinate bounds give
\[
 \sum_j|a_j-b_j|\le\sum_j(R_j-L_j)=kd-2(d-r)_+.
\]
The configurations \(L\) and \(R\) attain equality. Hence this is the exact diameter. Any binary isometric embedding must have at least as many coordinates as the distance between \(L\) and \(R\); the ideal-incidence embedding constructed above uses exactly that many. Thus the minimum isometric hypercube dimension equals the diameter. The term \(2(d-r)_+\) records the sharp loss of mobility when both endpoint deficit stacks would exceed capacity \(r\).

**4. Exact state count.** There are \(\binom{d+k}{k}\) nonnegative weak compositions of \(d\) into \(k+1\) parts. Each illegal event \(h_0\ge r+1\) or \(h_k\ge r+1\) has \(\binom{d-r-1+k}{k}\) solutions when \(d>r\). The two events cannot occur together because \(d\le2r\). Subtracting yields the vertex-count formula.

## Verification

The standalone `checker.py` constructs **actual minimum radius-\(r\) dominating sets**, independently checks the domination condition and actual single-edge token slides, and uses breadth-first searches for every source state. It compares the resulting graph connectivity, all ordered-pair distances, vertex counts and diameters to the formulas above. Executing `python checker.py` passes 90 parameter cases with \(r=2,3,4,5\), and 183,806 ordered-pair distance comparisons. This is finite corroboration only; the preceding symbolic proof establishes the unbounded statement.

## Relationship to prior work

Banerjee and Hoang (arXiv:2310.00241, first posted 2023-09-30) introduced and studied radius-\(r\) domination reconfiguration for \(r\ge2\), proving reachability algorithms and complexity results. Their tree result under token jumping does not classify the exact *minimum-cardinality token-sliding* state graph of paths.

Křišťan and Svoboda (arXiv:2307.10847, first posted 2023-07-20) proved shortest token sliding for subtree-hitting sets on trees. Radius-\(r\) path domination can be modeled using interval-shaped balls, so their stronger theorem already guarantees the general transport-optimal metric phenomenon. We do **not** claim that broad geodesic principle as new. Instead, the present deficit-space identification gives a specific distributive interval, a median-graph classification, an exact count, a sharp all-parameter diameter with its endpoint-saturation transition, and a minimal binary dimension; these are not supplied by the cited general algorithm.

The 2020 work of Lemańska and Żyliński treats minimum ordinary domination on trees (radius one), yielding general sliding-diameter bounds. It does not cover the present distance-\(r\) result for \(r\ge2\). The classical theory of order ideals and partial cubes underlies the median-graph implications; the construction of the relevant induced difference poset for distance-\(r\) minimum dominating sets is the specific contribution.

## Limitations

The formula concerns only minimum-cardinality radius-\(r\) dominating sets on paths and slides along the *original* path. It does not classify larger dominating sets, cycles, arbitrary trees, token jumping, or slides along powered-path edges. General transport-optimal geodesics on tree hitting-set problems and the abstract order-ideal-lattice facts are acknowledged as prior knowledge. An earlier indexed or unindexed graph-isomorphism description of these exact feasible sets could limit historical originality; the searches below do not constitute a proof of uniqueness in the literature. No independent audit has been performed.

## References

1. N. Banerjee and D. A. Hoang, *The Complexity of Distance-\(r\) Dominating Set Reconfiguration*, arXiv:2310.00241 (first public 2023-09-30), https://arxiv.org/abs/2310.00241.
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847 (first public 2023-07-20), https://arxiv.org/html/2307.10847v1.
3. M. Lemańska and P. Żyliński, *Reconfiguring Minimum Dominating Sets in Trees*, J. Graph Algorithms Appl. 24 (2020), 47–61, https://doi.org/10.7155/jgaa.00517.
4. Standard finite distributive-lattice/order-ideal representation and associated median-graph/partial-cube facts.
