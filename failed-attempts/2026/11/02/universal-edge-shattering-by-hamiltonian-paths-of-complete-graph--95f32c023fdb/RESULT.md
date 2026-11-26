# Universal edge shattering by Hamiltonian paths of complete graphs

## Finding

Let \(K_n\) be the simple complete graph on \(n\) labeled vertices, \(n\ge1\), and let \(\mathcal H_n\subseteq 2^{E(K_n)}\) consist of the edge sets of all *undirected spanning Hamiltonian paths* (with reversed vertex orders identified). An edge-query support \(S\subseteq E(K_n)\) is **shattered** when, for every \(T\subseteq S\), some \(H\in\mathcal H_n\) satisfies \(H\cap S=T\). A **linear forest** is a disjoint union of paths, including isolated vertices.

**Theorem.** For every \(n\ge4\), \(S\) is shattered by \(\mathcal H_n\) **if and only if** \((V(K_n),S)\) is a linear forest. Equivalently, if \(S\) is a linear forest and \(T\subseteq S\), there is a Hamiltonian path containing every edge of \(T\) and avoiding every edge of \(S\setminus T\).

Consequently, for \(n\ge4\),
\[
\operatorname{VCdim}(\mathcal H_n)=\operatorname{Ldim}(\mathcal H_n)=n-1.
\]
Every maximum shattered support is itself the edge set of a Hamiltonian path; there are exactly \(n!/2\) such supports on labeled vertices. For \(n=1,2\) both dimensions are zero; for \(n=3\) both are one, and the shattered supports are the empty set and the three singleton edge supports.

The known exponential generating function for labeled linear forests therefore also counts shattered edge supports for every \(n\ge4\). Including the small exceptions, its bivariate form is
\[
\sum_{n\ge0}\frac{z^n}{n!}\sum_{S\text{ shattered}}t^{|S|}
 =\exp\!\left(z+\frac{z^2t}{2(1-zt)}\right)-\frac{z^2t}{2}-\frac{z^3t^2}{2},
\]
where the zero-vertex term is interpreted formally as the one empty support. This enumeration is an immediate corollary of the structural theorem, not an additional independent novelty claim.

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled. The hypotheses are *spanning paths only*: neither arbitrary subpaths, all cycles, Hamiltonian cycles, nor arbitrary spanning trees are interchangeable with \(\mathcal H_n\). Edges are membership queries, not vertex queries. The Littlestone dimension uses complete binary trees of adaptive edge-membership queries in the realizable deterministic model; repeated queries are allowed, but remembered labels have no new uncertainty.

## Proof

**Necessity.** If \(S\) is shattered then the all-positive pattern is realized by a Hamiltonian path, so \(S\) is a subgraph of that path, hence a linear forest.

**Sufficiency for \(n\ge4\).** Fix a linear forest \(S\) and an arbitrary demanded-positive subset \(T\subseteq S\). Regard \(T\) as a graph on all \(n\) vertices, with isolated vertices included. Its \(k\) components \(B_1,\ldots,B_k\) are vertex-disjoint paths. Contract each component of \(T\) to a block. The negative edges \(S\setminus T\) join distinct blocks and yield a linear forest \(Q\) on the \(k\) blocks. Every pair of blocks joined by an edge of \(Q\) is joined by **exactly one** negative edge: the original forest \(S\) has no cycle. To realize the prescribed trace, place the \(k\) path blocks in an order, choosing either orientation for each nontrivial block, and concatenate their vertex orders. Edges internal to blocks are exactly \(T\). We need only make the \(k-1\) joining edges different from \(S\setminus T\).

For \(k\ge4\), extend the linear forest \(Q\) to some spanning path on its blocks (concatenate its component paths), and label the blocks \(1,\ldots,k\) in that order. Use block order \(2,4,6,\ldots\), followed by \(1,3,5,\ldots\), each subsequence increasing. Adjacent indices in this new order differ by at least two, including at the even-to-odd junction, because \(k\ge4\). Since every negative interblock edge connects consecutive indices of the original order, **no new interblock joining pair belongs to \(Q\)**. Any orientations of the blocks work.

For \(k=3\), if \(Q\) has at most one edge, its complement contains a spanning path, and ordering blocks along that path avoids all negative interblock edges. If \(Q\) is the three-block path, at least one block \(B\) contains at least two vertices because \(n\ge4\). Arrange the blocks so exactly one consecutive block pair belongs to \(Q\), with \(B\) one member of that pair: put the two neighbors of \(B\) consecutively in the appropriate order if \(B\) is the middle block, or put \(B\) between the two other blocks if it is an end block. One of the two blocks involved in this sole forbidden pair is the nontrivial path \(B\). Exactly one edge of \(S\setminus T\) joins this pair. Orient \(B\) so that its endpoint used for this join is **not** the endpoint of that one forbidden edge. Its two endpoints are distinct, so this is possible. The other join is between nonadjacent blocks of \(Q\) and is unrestricted.

For \(k=2\), \(Q\) has at most one edge. If that edge exists, at least one block is nontrivial because \(n\ge4\); orient it to use at the join the endpoint opposite the unique forbidden edge. Otherwise join freely. For \(k=1\), no join is needed. Thus every labeling is realized by a spanning path.

**Dimensions.** A shattered support cannot contain more than \(n-1\) edges, and a Hamiltonian-path support itself is a linear forest of that size, so its VC dimension equals \(n-1\) for \(n\ge4\). Static shattering gives a complete mistake tree by presenting these \(n-1\) edges in a fixed order, proving the matching Littlestone lower bound. For the upper bound, an online learner remembers all previously observed edge labels, predicts those on repeat queries, and predicts negative on every unqueried edge. Against any target Hamiltonian path it errs at most once per target-positive edge, of which there are exactly \(n-1\). Therefore Littlestone dimension is at most \(n-1\).

All maximum shattered supports have \(n-1\) edges and are linear forests, hence connected spanning paths. The number of labeled undirected paths is \(n!/2\). For \(n\le3\), direct enumeration of the one or three possible path edge sets yields the stated small cases, with \(\operatorname{Ldim}\le\lfloor\log_2|\mathcal H_n|\rfloor\).

**Enumeration.** An undirected labeled path component of order \(j\ge2\) has \(j!/2\) labelings and \(j-1\) edges, while a singleton has one. The labeled exponential formula therefore yields \(\exp(z+\sum_{j\ge2}z^j t^{j-1}/2)\), equal to the displayed exponential. Remove the single \(n=2\) one-edge support and the three \(n=3\) two-edge supports, giving the two correction terms.

## Verification

The standalone standard-library program `hamiltonian_path_shattering_verifier.py` enumerates all labeled undirected Hamiltonian paths and checks every candidate linear-forest support through seven vertices. Through six vertices it also enumerates **every possible edge subset**, checking the converse independently of the all-positive argument. It reports, for \(n=4,5,6,7\), respectively \(34,206,1486,12412\) shattered supports and \(12,60,360,2520\) maximum supports. Run `python3 hamiltonian_path_shattering_verifier.py` and compare with `VERIFIER_OUTPUT.txt`.

These are finite corroborations. The unrestricted result follows from the constructive proof above, not from extrapolating the enumerations.

## Relationship to prior work

Mofidi's cycle- and spanning-tree-hypergraph study gives structural conditions for shattering by **all cycles** and by **all spanning trees**, including an extremal \(n-1\) cycle-hypergraph result for complete graphs. Neither family equals the **Hamiltonian-path** incidence class analyzed here, and realizations in these larger classes need not themselves be spanning paths. Kranakis, Krizanc, Ruf, Urrutia, and Woeginger study path-induced VC set systems more generally; the accessible abstract does not resolve the present edge-incidence question with the Hamiltonian-spanning restriction. Literature on prescribed linear forests in faulty hypercubes concerns different host graphs and endpoint/fault constraints.

The ordinary labeled-linear-forest generating function is classical and was not independently discovered here. The central statement is its **universal positive/negative Hamiltonian-path completion interpretation**, yielding a full shattering classification for this restricted concept class and the exact adaptive dimension.

## Limitations

The proof uses completeness of the host graph and does not assert the same realization property in arbitrary Hamiltonian graphs. The complete 1997 path-VC article was not available for full-text comparison, and historical priority remains uncertain; neither unsuccessful searches nor the finite verifier certify novelty. No independent scientific validation is claimed.

## References

- A. Mofidi, “On the Number of Cycles of Graphs and VC-Dimension,” *Facta Universitatis, Series Mathematics and Informatics* (2022), DOI: `10.22190/FUMI210301011M` (publicly indexed date 2022-04-12; a separate bibliographic index gives 2022-05-10).
- A. Mofidi, “On the VC-Dimension, Covering and Separating Properties of the Cycle and Spanning Tree Hypergraphs of Graphs,” *Transactions on Combinatorics* 11 (2022), 29–43, DOI: `10.22108/TOC.2021.127880.1832` (Section 3 and Theorem 3.3 inspected).
- E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, and G. J. Woeginger, “The VC-Dimension of Set Systems Defined by Graphs,” *Discrete Applied Mathematics* 77 (1997), 237–257, DOI: `10.1016/S0166-218X(96)00137-0` (abstract and bibliographic metadata inspected; complete text not obtained).
- Y. Yang, J. Li, and S. Wang, “Embedding Fault-Free Hamiltonian Paths with Prescribed Linear Forests into Faulty Ternary n-Cubes,” *Theoretical Computer Science* 767 (2019), 1–15, DOI: `10.1016/j.tcs.2018.09.020` (abstract inspected).
