# Connected odd domination of \(\operatorname{KG}(n,2)\): three exceptional ground-set orders

## Finding
For each integer \(n\ge5\), let \(G_n=\operatorname{KG}(n,2)\) have vertex set \(\binom{[n]}2\), with adjacency precisely between disjoint pairs. A set \(S\subseteq V(G_n)\) is *odd dominating* if \(|N_{G_n}[e]\cap S|\) is odd for every vertex \(e\), and is *connected odd dominating* if, in addition, \(G_n[S]\) is connected. All counts below distinguish the ground-set labels but do not order the selected vertices.

**Theorem.** The minimum size of a connected odd dominating set is \(3\) when \(n=6\), and \(5\) at every other \(n\ge5\). Each minimum set is precisely one of the following edge families of the complete graph on \([n]\):

1. At \(n=6\): any perfect matching \(3K_2\) (\(15\) sets).
2. At every \(n\ge5\) except \(n=6\): every five-cycle \(C_5\), with any remaining ground-set vertices isolated (\(12\binom n5\) sets).
3. Additionally at \(n=8\): every \(K_{1,3}\sqcup 2K_2\) spanning the eight ground-set vertices (\(840\) sets).
4. Additionally at \(n=10\): every perfect matching \(5K_2\) (\(945\) sets).

Thus, if \(a_n\) denotes the number of minimum connected odd dominating vertex sets, then
\[
a_6=15,\qquad a_n=12\binom n5+840\mathbf1_{n=8}+945\mathbf1_{n=10}\quad(n\ge5,\ n\ne6).
\]
For \(n=5\), the twelve minimum sets are the twelve Hamiltonian cycles of \(K_5\). Make a graph on these twelve sets, with edges joining pairs differing by simultaneous replacement of two selected vertices. This *two-replacement graph* is the six-crown
\[
K_{6,6}-M_6.
\]
It has thirty edges and diameter three, whereas the one-vertex-replacement graph has twelve isolated vertices.

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. A copy of \(C_5\), \(3K_2\), \(K_{1,3}\sqcup2K_2\), or \(5K_2\) in the theorem is an *edge-selected* simple graph on the labelled ground set \([n]\), not an induced-subgraph assertion about \(G_n\). In the five-cycle case, the remaining \(n-5\) ground-set vertices are isolated in this selected-edge graph. A connected vertex set means a nonempty set whose induced subgraph is connected. The minimum is taken over connected odd dominating sets, not over arbitrary connected dominating sets, open-neighborhood parity sets, or total dominating sets. The crown statement concerns only \(n=5\) and makes simultaneous replacements of exactly two selected vertices; it does not permit intermediate nonoptimal configurations.

## Proof
**Parity reduction.** Regard a vertex set \(S\subseteq V(G_n)\) as the edge set of an auxiliary simple graph \(H=([n],S)\), and put \(m=|S|\) and \(d_i=\deg_H(i)\). For an arbitrary pair \(e=\{i,j\}\), let \(x_e\) be one if \(e\in S\) and zero otherwise. Selected edges disjoint from \(e\) number \(m-d_i-d_j+x_e\), because a selected \(e\) is subtracted twice. Adding \(e\) itself to the closed neighborhood when selected gives
\[
|N_{G_n}[e]\cap S|=m-d_i-d_j+2x_e\equiv m+d_i+d_j\pmod2.
\]
All these numbers are odd if and only if \(m\) is odd and all \(d_i\) have the same parity. To prove the converse implication from the equations, take any distinct indices \(i,j,k\): subtract the equations for \(\{i,j\}\) and \(\{i,k\}\) to deduce \(d_j\equiv d_k\), hence all degrees have common parity, and substitution forces \(m\equiv1\). Conversely, those two conditions make every displayed closed-neighborhood count odd.

Thus every odd dominating set corresponds to an *odd-edge Eulerian graph* (all degrees even), or, only when \(n\) is even, to an *odd-edge all-odd-degree graph* (every ground-set vertex has odd degree). No set of size one works for \(n\ge5\), and even sizes never work.

**Three-edge support.** An even-degree simple graph with exactly three edges is necessarily a triangle. Its three selected vertices in \(G_n\) are pairwise nonadjacent because the triangle edges pairwise intersect. An all-odd-degree graph with three edges has at most six nonisolated vertices and no isolated vertices are allowed. For \(n\ge5\), the only possibility is \(n=6\), with all six degrees one: a perfect matching \(3K_2\). Its three edges are pairwise disjoint and thus form a triangle in \(G_6\). Consequently the unique possible connected three-element supports occur at \(n=6\); the minimum there is three and their number is \(6!/(2^3 3!)=15\). Every \(n\ne6\) has minimum at least five.

**Five-edge support.** The only loopless simple graph with exactly five edges and all degrees even is a five-cycle: every nontrivial Eulerian component consumes at least three edges, and no partition of five into cycle lengths at least three exists. Every such \(C_5\) yields an induced \(C_5\) in the disjointness graph on its five selected edges, so it is connected and odd dominating for every \(n\ge5\).

An all-odd-degree auxiliary graph with five edges has degree sum ten and all \(n\) degrees at least one. It therefore requires even \(n\le10\). At \(n=8\), the degree sum exceeds eight by two: one degree is three and seven degrees are one, so the selected graph is exactly \(K_{1,3}\sqcup2K_2\). Its five edges form a connected induced subgraph in \(G_8\): both matching edges are disjoint from all three star edges, and the matching edges are disjoint from each other. At \(n=10\), all degrees equal one, so the selected graph is exactly \(5K_2\), inducing \(K_5\) in \(G_{10}\). The case \(n=6\) does not contribute five-element *minimum* sets, because it has three-element solutions. For odd \(n\), common odd degree parity is impossible by the handshaking lemma. For even \(n\ge12\), five edges cannot cover all vertices with positive odd degree. These possibilities exhaust every minimum set.

**Counting.** Choose the five vertices for \(C_5\) in \(\binom n5\) ways, then choose one of \((5-1)!/2=12\) unoriented Hamiltonian cycles. At \(n=8\), choose the unique degree-three center in eight ways, its three leaves in \(\binom73\) ways, and a perfect matching of the remaining four vertices in three ways: \(8\binom73\cdot3=840\). At \(n=10\), the matching count is \(10!/(2^5 5!)=945\). Different types have different degree sequences, so there is no overcounting.

**Crown geometry at \(n=5\).** Each optimal set is a Hamiltonian cycle of \(K_5\). Fix ground-set element zero and represent an unoriented cycle by \((0,a,b,c,d)\), where reversing \((a,b,c,d)\) yields the same cycle. The sign of the permutation \((a,b,c,d)\) is well-defined under reversal, since reversing four entries has six inversions. There are six cycles of each sign. Two distinct Hamiltonian cycles cannot share four edges: the four common edges form a spanning path whose only possible closing edge is the fifth original edge. Sharing three edges, on the other hand, means removing two nonadjacent edges of the first cycle and reconnecting to another Hamiltonian cycle. Exactly five pairs of nonadjacent cycle edges are possible, each yielding a distinct two-replacement neighbor. This standard two-edge switch reverses a consecutive block of two or three symbols in the fixed-zero representation, and so changes permutation sign. Hence the graph is bipartite on six cycles of each sign, and is five-regular. A simple five-regular bipartite graph with six vertices on either side is necessarily \(K_{6,6}\) minus a perfect matching. Its diameter is three. No one-vertex replacement can preserve optimality by the four-edge sharing argument.

## Verification
Two independent finite verifiers are supplied as `check_direct.py` and `check_parity.cpp`. They use different tests: the first computes every closed-neighborhood parity and induced connectivity directly in \(G_n\), while the second checks the auxiliary-degree parity criterion and disjointness connectivity. Both exhaust all odd candidate cardinalities one, three, and five for each \(5\le n\le10\), with no sampling. The Python verifier also constructs the twelve-state two-replacement graph at \(n=5\), checks its bipartition and missing perfect matching, and confirms distance layers \((1,5,5,1)\). The programs are independently readable; their shared expected values are compared against the proof rather than used as an assumption of a general theorem.

Run `python3 check_direct.py`, then compile with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_parity.cpp -o check_parity` and execute `./check_parity`. The finite checks are not the all-order proof. The preceding argument proves the theorem for every integer \(n\ge5\), including orders not enumerated.

## Relationship to prior work
Odd domination with *closed-neighborhood* parity is classical, including Caro--Goldwasser--Klostermeyer (2001) and Caro--Klostermeyer (2003). Caro--Klostermeyer--Yuster (2005) introduced and investigated *connected* odd dominating sets, including grids, complements of powers of cycles, complete partite graphs, and algorithmic questions. Their general observation that induced connected odd dominating subgraphs are Eulerian is consistent with all four support families here, but does not classify \(\operatorname{KG}(n,2)\). The \(n=5\) Petersen graph is also \(\operatorname{GP}(5,2)\); an existing complete odd-domination weight enumerator gives the coefficient twelve at weight five, so that numerical coefficient is **not** claimed as independently new. Earlier classifications of ordinary/minimal total-dominating sets of rank-two Kneser graphs include some of the same auxiliary five-cycles and three-matchings, but those conditions are not equivalent to closed-neighborhood parity plus connectedness. A previously published connected odd-domination classification specifically for rank-two Kneser graphs or its exceptional even-order supports was not located in the compared material. The new contribution is the uniform parity-support characterization of all connected minima, the exceptional \(n=8,10\) families, and the optimum exchange geometry at \(n=5\).

## Limitations
No claim is made for higher-rank Kneser graphs or for all connected odd dominating sets of nonminimum size. The finite check covers only \(n\le10\); the arbitrary-order classification follows from the explicit proof, not from extrapolation. Historical publication priority cannot be guaranteed: some older records and the complete 2003 source text were not accessible, and the publicly indexed mathematical findings may be incomplete. The shared five-cycle and Petersen-weight-count special cases are credited to previous work where applicable. No independent scholarly validation has been carried out.

## References
1. Y. Caro, J. L. Goldwasser, W. F. Klostermeyer, *Odd and residue domination numbers of a graph*, Discussiones Mathematicae Graph Theory 21 (2001), 119--136, doi:10.7151/DMGT.1137; https://bibliotekanauki.pl/articles/743442.pdf.
2. Y. Caro, W. F. Klostermeyer, *The odd domination number of a graph*, J. Combin. Math. Combin. Comput. 44 (2003), 65--83; https://combinatorialpress.com/jcmcc-articles/volume-044/the-odd-domination-number-of-a-graph/.
3. Y. Caro, W. F. Klostermeyer, R. Yuster, *Connected odd dominating sets in graphs*, Discussiones Mathematicae Graph Theory 25 (2005), 225--239, doi:10.7151/DMGT.1276; https://www.academia.edu/15251680/Connected_odd_dominating_sets_in_graphs.
4. M. G. Cornet, P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603 (2023); https://arxiv.org/abs/2308.15603. This concerns nonparity multiple domination and is not a source for the theorem above.
