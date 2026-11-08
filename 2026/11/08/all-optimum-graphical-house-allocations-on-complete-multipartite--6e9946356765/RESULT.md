# All optimum graphical house allocations on complete multipartite networks

## Finding
Let \(G=K_{n_1,\ldots,n_q}\) be a complete multipartite graph with \(q\ge3\) nonempty labeled parts, \(n_i\ge1\), and \(N=\sum_i n_i\) vertices. Assign the \(N\) distinct houses of common values \(0\le v_1<\cdots<v_N\), one house per vertex. The total graphical envy is the sum over graph edges of the absolute difference between the assigned values (equivalently, the sum of directional envy under identical valuations).

For each part \(i\), form the strictly descending priority list
\[
   w_{i,k}=n_i-2k-1,\qquad 0\le k<n_i.
\]
Sort the union of all \(N\) priorities into \(w_1\ge\cdots\ge w_N\), retaining multiplicities. For the \(r\)-th cheapest house, let \(c_r\) denote the part receiving it, and let \(x_i(r)\) be the number of earlier houses assigned to part \(i\).

**Complete characterization.** An allocation minimizes total envy if and only if, at every rank \(1\le r\le N\),
\[
    n_{c_r}-2x_{c_r}(r)-1=w_r.
\]
Thus all optimizers result from sorting the priority multiset and independently choosing the order of different parts within each tied priority level. The optimizer set depends only on the part sizes and on the ordering of the houses, not on their positive valuation gaps.

If \(m_w\) is the number of parts whose priority list contains the level \(w\), the exact number of optimal part-label strings is
\[
    \prod_{w}m_w!,
\]
and the exact number of allocations to **labeled vertices** is
\[
    \left(\prod_{i=1}^{q}n_i!\right)\left(\prod_{w}m_w!\right).
\]
Every part contributes at most one occurrence to a given level. Writing \(\Delta_r=v_{r+1}-v_r>0\), the minimum total envy is
\[
   \operatorname{Env}_{\min}(G,v)=\sum_{r=1}^{N-1}\Delta_r\left[r(N-r)-\sum_{j=1}^{r}w_j\right].
\]
In particular, balanced parts \(n_i=m\) yield exactly \((q!)^m\) optimal part-label strings. For \(K_{2,2,2}\) there are \(36\) such strings, or \(288\) allocations to individually labeled vertices.

## Assumptions and scope
An allocation is a bijection between the \(N\) distinct houses and graph vertices. Each vertex has the same additive utility for a single house, equal to that house's value. Under identical values, the sum of directed positive envy along each undirected edge is exactly the absolute value difference on that edge. There are no edges within a part and all edges between different parts. The valuations are finite real numbers strictly increasing in the displayed house order; positive gaps are essential for the *only if* direction. The theorem is stated for \(q\ge3\) to distinguish it from the known complete bipartite classifications.

## Proof
**Cut decomposition.** For any allocation, put \(x_i(r)=\#\{s\le r:c_s=i\}\), so \(\sum_i x_i(r)=r\). The number of edges joining a vertex among the first \(r\) assigned houses to a vertex among the remaining \(N-r\) houses is
\[
 C_r=r(N-r)-\sum_{i=1}^{q}x_i(r)(n_i-x_i(r)).
\]
This subtracts the pairs lying within a common part from all \(r(N-r)\) cross-cut vertex pairs. For an edge whose two houses have ranks \(a<b\), its absolute value difference is \(v_b-v_a=\sum_{r=a}^{b-1}\Delta_r\). Exchanging the sums over edges and valuation gaps proves
\[
 \operatorname{Env}(c)=\sum_{r=1}^{N-1}\Delta_r C_r.
\]

**Simultaneous optimality of every cut.** Fix \(r\). Minimizing \(C_r\) is equivalent to maximizing
\[
 F_r=\sum_i x_i(r)(n_i-x_i(r))
 =\sum_i\sum_{k=0}^{x_i(r)-1}(n_i-2k-1).
\]
For a fixed part the successive summands decrease strictly by \(2\). Hence maximizing \(F_r\) over the integer counts \(0\le x_i\le n_i\), \(\sum_i x_i=r\), amounts to choosing the largest \(r\) elements of the multiset of priorities: these chosen elements can always be prefix-closed within each part because each part's list is strictly descending. Consequently \(F_r\le\sum_{j=1}^{r}w_j\) for every allocation.

Now order the part labels by the sorted priority list, breaking ties between parts arbitrarily. That order is a legitimate length-\(N\) assignment word: within each part its priorities occur in their prescribed decreasing order. At *every* prefix \(r\) its selected priorities are exactly the largest \(r\) globally. It therefore simultaneously attains equality in every cut bound. Inserting these equalities into the cut decomposition gives the stated formula for \(\operatorname{Env}_{\min}\).

**Necessity, sufficiency, and enumeration.** All gaps \(\Delta_r\) are strictly positive. Therefore no increase in any \(C_r\) above its individual lower bound can be offset by another cut: a global optimizer must attain every individual minimum. An assignment word attains all prefix maxima if and only if its next selected priority is the next largest remaining element, including an arbitrary choice among ties, which is precisely the rank-by-rank condition stated above. Within each part a priority level occurs at most once, and every choice of permutations of different part labels within tied levels is legal. Thus each level \(w\) contributes exactly \(m_w!\) choices of assignment word, independently. Finally each part's assigned houses can be bijectively permuted over its \(n_i\) labeled vertices in \(n_i!\) ways without changing any cross-part edge cost. Multiplication yields the labeled-allocation formula. For balanced parts each level is shared by all \(q\) parts, at exactly \(m\) different levels, producing \((q!)^m\) words. This proves every assertion.

## Verification
The accompanying standalone Python 3 program `verify.py` enumerates all part-label assignment words for \(106\) finite instances across complete multipartite graphs with at most \(9\) vertices and between \(3\) and \(5\) nonempty parts, under two strictly increasing valuation patterns. For each instance, it calculates total edge cost directly (without using the cut formula for evaluation), identifies all minimizing words, and compares the optimum set and minimum cost with the theorem. All \(215{,}126\) examined full words were classified correctly. Run `python3 verify.py`; it requires only Python's standard library. The infinite-family conclusion follows from the proof, not from these finite tests.

## Relationship to prior work
Hosseini, Payan, Sengupta, Vaish, and Viswanathan, *Graphical House Allocation* (arXiv:2301.01323, first posted January 3, 2023), characterize all optimal allocations for complete bipartite networks in Theorems 4.5–4.7, including the two-part counting formula. The present result addresses connected complete multipartite networks with three or more parts, provides a common marginal-priority description, and counts all optimal labeled allocations for unequal part sizes and arbitrary strictly increasing valuations. The proof uses the cut interpretation associated with the linear-arrangement objective.

Earlier embedding literature includes Rajan, Rajalaxmi, Liu, and Sethuraman, *Wirelength of embedding complete multipartite graphs into certain graphs* (2020), which reports exact minimum path-embedding wirelength, corresponding to equally spaced valuations. This preexisting numerical optimization overlap is acknowledged: the claim here is the complete optimizer characterization and multiplicity for *all* strictly increasing value vectors, not a new discovery of the equally spaced scalar minimum. The full text of that relevant work was not accessible during the comparison, so its possible stronger optimizer results remain a material priority risk. Shalini, Delaila, and Julie (2020) give a Turán-graph (balanced multipartite) linear-arrangement optimum; that special-case numerical result is likewise prior work.

## Limitations
This proof requires identical house valuations and strict ordering of distinct houses. With tied values, zero gaps can permit additional optimal allocations not characterized by the displayed if-and-only-if rule. No claim is made about nonidentical utilities, arbitrary social networks, or an unreviewed complete literature priority determination. The numerical equally spaced case intersects previous complete multipartite wirelength work, whose inaccessible full text leaves the exact extent of precedent uncertain. The checker tests finite instances and does not certify the theorem independently of the mathematical proof.

## References
- H. Hosseini, J. Payan, R. Sengupta, R. Vaish, and V. Viswanathan, *Graphical House Allocation*, arXiv:2301.01323 (first version January 3, 2023). https://arxiv.org/abs/2301.01323 ; full text https://arxiv.org/html/2301.01323v2
- R. Sundara Rajan, T. M. Rajalaxmi, J.-B. Liu, and G. Sethuraman, *Wirelength of embedding complete multipartite graphs into certain graphs*, Discrete Applied Mathematics 280 (2020), 221–236. https://doi.org/10.1016/j.dam.2018.05.034
- A. J. Shalini, J. N. Delaila, and J. M. Julie, *Optimal Linear Arrangement of Turán Graphs*, International Journal of Recent Technology and Engineering 8(6) (2020), 3618–3621. https://doi.org/10.35940/ijrte.F8964.038620
