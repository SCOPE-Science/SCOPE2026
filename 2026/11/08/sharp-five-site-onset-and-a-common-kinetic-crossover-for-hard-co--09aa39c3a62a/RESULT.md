# Sharp five-site onset and a common kinetic crossover for hard-core monomer adsorption

## Finding

Consider independent, rate-one irreversible monomer adsorption on a finite simple graph. Every vertex makes an exponential-time first attempt; that vertex becomes occupied exactly when none of its neighbors is already occupied. Write \(M_G(t)\) for the expected number occupied by time \(t\ge0\), and \(M_G(\infty)\) for its jammed mean. For a nonedge \(e\) of \(G\), adding \(e\) means adding an exclusion relation while retaining all site rates.

**Theorem.** For every connected simple graph \(G\) with at most four vertices and every nonedge \(e\),
\[
M_{G+e}(\infty)\le M_G(\infty).
\]
For connected graphs on exactly five vertices, strict reverse inequality holds for precisely two ordered graph-with-marked-edge types, up to isomorphism:
\[
P_5\longrightarrow Q\longrightarrow K_{2,3},
\]
where \(Q\) is a four-cycle with one pendant vertex. Both arrows add exactly one edge; for the first arrow the added edge closes a four-cycle, and for the second it joins the leaf to a vertex of degree two on the four-cycle opposite the degree-three attachment. Every other connected five-vertex one-edge augmentation has nonpositive jammed-mean change.

The exact jammed means along this chain are
\[
M_{P_5}(\infty)=\frac{37}{15},\quad M_Q(\infty)=\frac{38}{15},\quad M_{K_{2,3}}(\infty)=\frac{13}{5}.
\]
In particular, each added exclusion edge raises the mean by \(1/15\).

There is also a common *entire-time* law for both arrows. Set \(p=1-e^{-t}\). Then for each successive pair \((G,H)\) in the chain,
\[
M_H(t)-M_G(t)=\frac{p^2}{30}(7p^3-35p^2+60p-30).
\]
The cubic has exactly one root \(p_*\in(0,1)\), with \(0.849<p_*<0.850\) and \(p_*\approx0.849274782106\). The added bond lowers expected occupation for \(0<t<-\log(1-p_*)\), raises it for \(t>-\log(1-p_*)\), and ties at the unique positive crossover time \(t_*\approx1.892296849\). At \(t=0\), all means also coincide.

## Assumptions and scope

A vertex is occupied at most once and never vacated; all edges are undirected exclusion bonds, and all sites have independent rate-one exponential first-attempt times. Equivalently, each site can have a rate-one Poisson attempt stream, since attempts after the first cannot change its eligibility when previously blocked or already occupied. Graphs are finite, simple, connected before augmentation, and the edge being added is initially absent. The minimality and classification statements concern the terminal expected particle count, *not* an ordering of the full terminal distributions or all-time effects on every smaller graph. The full-time formula concerns only the two identified five-site augmentations.

For a concrete labeling use vertices \(0,1,2,3,4\). The path has edge set \(\{02,04,12,13\}\), the intermediate graph adds \(03\), and the final complete bipartite graph adds \(14\). Thus the exact graph identities and marked added edges do not depend on an informal picture.

## Proof

**First-arrival recursion.** For any induced subgraph \(H\), let \(F(H)\) be the terminal expectation of the same random-order greedy process, with \(F(\varnothing)=0\). The first arriving vertex is uniformly distributed; if it is \(v\), it becomes occupied and excludes its closed neighborhood. Remaining first-attempt times have uniform relative order. Hence
\[
F(H)=1+\frac{1}{|V(H)|}\sum_{v\in V(H)}F(H-N_H[v])
\]
for every nonempty \(H\). This identity is exact, including isolated vertices and disconnected residual graphs.

**Finite sharp classification.** The accompanying self-contained `verify.py` represents every labeled graph on \(n\le5\) vertices by its \(\binom n2\)-bit edge indicator and evaluates the above rational recursion on all induced vertex masks. It examines *every* connected input graph and *every* missing edge. An independent evaluator enumerates all \(n!\) arrival orders and agrees exactly with the recursion on **every labeled graph**, not merely on the displayed witnesses. There are \(1,2,8,64,1024\) labeled graphs for orders \(1,2,3,4,5\), respectively. The number of strictly positive connected augmentations is \(0,0,0,0,180\). For order five, the complete counts by number of existing edges are:

| Existing edges | Connected labeled graphs | Positive labeled one-edge augmentations |
|---:|---:|---:|
| 4 | 125 | 120 |
| 5 | 222 | 60 |
| 6 | 205 | 0 |
| 7 | 120 | 0 |
| 8 | 45 | 0 |
| 9 | 10 | 0 |
| 10 | 1 | 0 |

Every one of the 180 positive labeled augmentations has exact increase \(1/15\). The checker applies every one of the \(5!\) vertex relabelings to each positive *marked augmentation*, and shows that the 120 four-edge cases are isomorphic to \(P_5\to Q\) and the 60 five-edge cases are isomorphic to \(Q\to K_{2,3}\). This is a finite exhaustive proof of the full stated minimality and classification, not an inference from sampling.

**Time-dependent identity.** Let \(\mu_k(G)\) be the expected number accepted after exactly \(k\) vertices from a uniform arrival permutation have been inspected. The triple of exact \(\mu_k\)-rows for \(k=0,1,2,3,4,5\), obtained by exhaustive permutation enumeration, is
\[
\begin{array}{c|rrrrrr}
&0&1&2&3&4&5\\\hline
P_5&0&1&8/5&2&34/15&37/15\\
Q&0&1&3/2&19/10&67/30&38/15\\
K_{2,3}&0&1&7/5&9/5&11/5&13/5
\end{array}
\]
Because each independent exponential first attempt has occurred by \(t\) with probability \(p=1-e^{-t}\), the number attempted is binomial and its conditional inspection order is uniform. Therefore
\[
M_G(t)=\sum_{k=0}^5 \binom5k\mu_k(G)p^k(1-p)^{5-k}.
\]
Each consecutive pair of rows has the same difference \((0,0,-1/10,-1/10,-1/30,1/15)\). Substituting and expanding yields the asserted common polynomial difference, with no numerical approximation in the proof.

Finally the derivative of \(q(p)=7p^3-35p^2+60p-30\) is \(21p^2-70p+60\), whose discriminant is \(-140\) and whose leading coefficient is positive. Hence \(q\) increases strictly on \(\mathbb R\); moreover \(q(0)=-30\) and \(q(1)=2\). It has exactly one zero in \((0,1)\). Exact rational evaluations at \(849/1000\) and \(850/1000\) bracket that zero. Since \(p(t)\) increases strictly from zero to one, the advertised sign reversal and uniqueness follow.

## Verification

Execute `python3 verify.py` (Python standard library only). It asserts exact rational agreement between the induced-graph first-arrival recurrence and direct enumeration of all vertex permutations for every labeled graph of order at most five; checks all connected one-edge augmentations and marked-graph isomorphism types; verifies the six-point attempted-prefix table and both identical polynomial differences; and proves the cubic root bracket by rational evaluation. Its final line is `PASS exact finite classification and time-dependent law`. The theorem's domain has at most five vertices for the classification, so the enumeration is exhaustive. The argument for all real times follows symbolically from the exact polynomial and the cubic's discriminant, not from time sampling.

## Relationship to prior work

Pippenger's 1989 graph-adsorption work introduces and analyzes random-sequential occupancy and dimer analogues, principally in regular, locally tree-like settings. Brightwell, Janson and Luczak (first public preprint 19 October 2015) study greedy independent sets on random graphs with prescribed degree sequences, with asymptotic laws rather than this finite marked-edge classification. Krivelevich, Mészáros, Michaeli and Shikhelman (arXiv first version 16 July 2019), Section 8, explicitly demonstrate that expected greedy independent-set size need not be monotone under edge deletion, using two stars joined at their centers, giving examples starting at six vertices. **The existence of edge-augmentation enhancement is therefore not claimed as new.** The present contribution is the *sharp order-five onset*, its exact two-type classification among connected graphs, and the common finite-time crossover polynomial. The cited six-vertex construction alone does not imply any of these sharpenings.

## Limitations

The graph census is exact only through five vertices; it does not classify larger graphs or establish a general graph-order limit. The enhancement is for mean occupation, not necessarily stochastic dominance. The full text of Pippenger's 1989 article was not accessible through the examined routes; an earlier unindexed five-vertex computation cannot be excluded. Searching titles and abstracts cannot certify priority, and the claims warrant independent review before publication.

## References

1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393 ff. DOI: https://doi.org/10.1137/0402034. Full article not materially inspected.
2. G. Brightwell, S. Janson and M. Luczak, “The greedy independent set in a random graph with given degrees,” arXiv:1510.05560v1, 19 October 2015. https://arxiv.org/abs/1510.05560.
3. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, “Greedy maximal independent sets via local limits,” arXiv:1907.07216, first public 16 July 2019; Section 8, especially the counterexample to edge-deletion monotonicity. https://arxiv.org/abs/1907.07216.
