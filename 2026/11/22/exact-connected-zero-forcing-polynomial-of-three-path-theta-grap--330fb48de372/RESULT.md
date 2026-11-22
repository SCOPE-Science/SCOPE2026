# Exact connected zero-forcing polynomial of three-path theta graphs

## Finding

Let \(\Theta(a,b,c)\) be the finite simple graph obtained by joining two distinct terminal vertices \(s,t\) with three internally vertex-disjoint paths having edge lengths \(a,b,c\ge2\). Let \(r_i=a_i-1\) for \((a_1,a_2,a_3)=(a,b,c)\), and \(N=2+r_1+r_2+r_3\). Write \(C_G(z)=\sum_{S\subseteq V(G)}[G[S]\text{ connected and }S\text{ is zero forcing}]z^{|S|}\).

For each \(i\in\{1,2,3\}\), define
\[
P_i(z)=\sum_{j=1}^{r_i}z^j,\quad R_i(z)=\sum_{j=1}^{r_i-1}(j+1)z^j+z^{r_i},\quad F_i(z)=z^{r_i},\quad E_i(z)=R_i(z)-F_i(z).
\]
An empty sum is zero; in particular \(R_i=F_i=z\) when \(r_i=1\). For each nonempty index set \(J\subseteq\{1,2,3\}\), set
\[
T_J(z)=\prod_{i\in J}R_i(z)-\prod_{i\in J}E_i(z).
\]
Then the **complete** connected zero-forcing polynomial is
\[
\boxed{C_{\Theta(a,b,c)}(z)=2z\left(\prod_{i=1}^{3}(1+P_i(z))-1-\sum_{i=1}^{3}P_i(z)\right)+z^2\left(T_{\{1,2,3\}}(z)+\sum_{k=1}^{3}T_{\{1,2,3\}\setminus\{k\}}(z)\right).}
\]
In particular, \(Z_C(\Theta(a,b,c))=3\), and precisely six connected zero-forcing sets have cardinality three, independently of the three path lengths. The polynomial is monic of degree \(N\) and explicitly counts every labelled initial set size.

## Assumptions and scope

Graphs are finite, simple, undirected; the three paths have pairwise disjoint interiors, and every path contains at least one internal vertex. All vertices are distinguished by their graph positions for counting purposes; two different initial vertex sets are counted separately. A zero-forcing process starts with blue vertices \(S\), and a blue vertex with exactly one white neighbor can color that neighbor blue. A set is zero forcing if iterating these moves colors the entire graph. Connectedness is imposed on the **initial induced subgraph** \(G[S]\), not on subsequent states. The formula does not claim to cover a path of length one directly joining the terminals, which would change the initial-connectivity cases.

## Proof

Write each path in order \(s,u_{i,1},\ldots,u_{i,r_i},t\). The internal vertices all have degree two, whereas \(s,t\) have degree three. Partition the initial connected zero-forcing sets according to which of the terminals are blue.

**Neither terminal initially blue.** A connected nonempty blue set lies within the interior of a single path: internal vertices of distinct paths have no edges between them. The other two paths are initially wholly white. Even if the two terminals subsequently turn blue, neither can force into these two empty paths: each terminal then has two white neighbors, one on each empty path, and there are no initially blue internal vertices on either. Therefore no such set succeeds.

**Exactly one terminal initially blue.** By interchanging \(s,t\), suppose \(s\) is blue. Initial connectivity forces the blue vertices on path \(i\) to be exactly a possibly empty contiguous prefix \(u_{i,1},\ldots,u_{i,j_i}\), with \(0\le j_i\le r_i\). If two paths have empty prefix, their first internal vertices cannot be forced: the only possible first entry is via one of the terminals, but each terminal has at least two white path-neighbors, and the interiors of those paths are initially empty. Hence at least two prefixes must be nonempty. Conversely, on any seeded path, its outermost initial blue internal vertex has precisely one white neighbor, unless its entire path is already blue. It can propagate towards \(t\); seeded paths thus fill and turn \(t\) blue. Once the seeded paths are full, a possible remaining empty path is the unique white branch at the terminals and can be forced from its ends. Thus exactly two or three nonempty prefixes are necessary and sufficient. The weight for a nonempty prefix on path \(i\) is \(P_i\); the number of terminal choices is two. This gives the first summand of the boxed formula.

**Both terminals initially blue.** For the initial induced subgraph to be connected, at least one of the three paths must have **all** its internal vertices blue: otherwise the two blue terminals would lie in different components, since internal vertices connect only along their path. On any path, connectivity further forces every selected internal vertex to belong to a prefix from \(s\) or a suffix from \(t\); isolated middle runs cannot occur. Thus the selected internal vertices on path \(i\) are a union of two (possibly empty) end-prefixes. If that union is nonempty but not the full internal path, its size can be any \(1\le j<r_i\), with exactly \(j+1\) possibilities for assigning \(j\) selected vertices between the two ends. If it is full, there is only one choice. This is precisely \(R_i(z)\), with the full-path term \(F_i=z^{r_i}\) and proper nonempty union term \(E_i=R_i-F_i\).

At most one internal path can be initially empty: with two empty paths, each terminal has at least two white neighbors in their interiors, and these paths can never receive a first force. Conversely, if no more than one path is empty, any nonfull but seeded path can fill from its selected boundary toward the white gap using degree-two forces; after those paths have filled, the possible single initially empty path can be filled from the terminals. Therefore, in this case, the initial set is connected and forcing exactly when (i) all selected internal vertices are endpoint unions, (ii) at least one path is full, and (iii) at most one path is empty. For a specified set \(J\) of nonempty paths, the condition of at least one full path contributes \(T_J=\prod R_i-\prod E_i\). There are either three nonempty paths or exactly two nonempty paths (three choices of the omitted path). Multiplying by \(z^2\) for the two selected terminals gives the second summand.

The cases are mutually disjoint and exhaustive. Every set counted by their local descriptions is both initially connected and can force the entire graph, proving the exact polynomial. Finally, the one-terminal case has exactly \(2\binom{3}{2}=6\) sets of size three (the terminal plus the first internal vertex on either two paths). The both-terminal case needs at least two nonempty internal paths, so cannot have size three. No smaller connected forcing set exists. The coefficient of \(z^N\) is one, since the entire vertex set is the only initial set of full size.

## Verification

Run `python CODE/verify_theta.py` in a directory containing the included standalone Python checker. It independently constructs each graph as an adjacency bitmask, enumerates **every** nonempty initial vertex set, verifies connectivity by a reachability search, and simulates the ordinary zero-forcing rule until closure. It separately expands the polynomial expression by integer convolution and checks equality of the full coefficient vectors for 68 nondecreasing triples of path lengths from 2 through 8 with total edge-length sum at most 18 (including 37 triples with repeated lengths). Exactly 1,886,304 potential vertex subsets were traversed. All tests passed with `VERIFY_OK`; examples include \(C_{\Theta(2,2,2)}=6z^3+5z^4+z^5\) and \(C_{\Theta(2,2,3)}=6z^3+11z^4+6z^5+z^6\). These are finite corroborations; the proof for all admissible lengths is the structural case analysis above, not extrapolation.

## Relationship to prior work

Mukherjee and Ray, arXiv:2611.10985v1, public 2026-11-07, determine the connected zero-forcing polynomial for **trees** and explicitly formulate the wider graph-enumeration question (Problem 5.4, with a separate unicyclic problem 5.2). Their arguments do not cover three-path theta graphs, which are 2-connected and bicyclic. Boyer and collaborators, arXiv:1801.08910v1, introduce the ordinary zero-forcing polynomial, which counts sets **without** requiring initial induced connectivity. Davila, Henning, Magnant and Pepper (arXiv:1605.02124) establish bounds on the connected forcing **number**, a scalar parameter: the full theta coefficient enumeration is not implied by scalar bounds. A 2020 paper of Premodkmuar, Dominic and Chacko studies connected forcing numbers, again distinct from a coefficient census. The relationship to these results is a natural extension of the counting question, not a claim that zero forcing or the minimum parameter is newly introduced. Searches against bibliographic indices and mathematical-result records located no matching full coefficient formula for three-path theta graphs. Such searches cannot prove global priority.

## Limitations

The theorem is restricted to exactly three internally disjoint terminal paths, all of edge length at least two. It makes no claims about graphs with extra chords, attached trees, direct edges between terminals, more than three paths, or disconnected initial forcing sets. It counts vertex subsets and not automorphism orbits, and it does not resolve general-graph connected zero-forcing enumeration. Direct enumeration verifies only finite path-length triples, while correctness for all lengths comes from the proof. An unindexed or differently named exact enumerator could predate this formulation; historical priority has not been independently certified.

## References

1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985v1, first public 2026-11-07, https://arxiv.org/abs/2611.10985 . In particular, Section 5, Problems 5.2 and 5.4.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, 2018-01-26, https://arxiv.org/abs/1801.08910 .
3. R. Davila, M. Henning, C. Magnant and R. Pepper, *Bounds on the connected forcing number of a graph*, arXiv:1605.02124, https://arxiv.org/abs/1605.02124 .
4. K. P. Premodkmuar, C. Dominic and B. Chacko, *Connected k-forcing sets of graphs and splitting graphs*, J. Math. Comput. Sci. 10 (2020), 656–680, https://doi.org/10.28919/jmcs/4446 .
