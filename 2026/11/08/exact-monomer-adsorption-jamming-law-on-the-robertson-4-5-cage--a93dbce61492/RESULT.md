# Exact monomer-adsorption jamming law on the Robertson \((4,5)\)-cage

## Finding
Let \(R\) be the Robertson graph defined below. Give its nineteen vertices independent continuous uniform arrival times and occupy a vertex if none of its already occupied neighbors is present. The terminal occupied set \(I\) is a maximal independent set, and its size \(X=|I|\) has the **complete exact distribution**

\[
\Pr(X=5)=\frac{92833}{1256850},\qquad
\Pr(X=6)=\frac{520381}{628425},\qquad
\Pr(X=7)=\frac{913}{9310},
\]

with all other probabilities zero. In particular,
\[
\mathbb E X=\frac{540823}{89775},\qquad
\mathbb E(X/19)=\frac{540823}{1705725}.
\]
The graph has three automorphism orbits, of cardinalities \(12,3,4\). Under the explicit vertex indexing below, the exact probability that a given site is occupied at jamming is, respectively,
\[
\begin{array}{c|c|c}
\text{Orbit} & \text{Sites} & \Pr(v\in I)\\ \hline
A & \{0,2,3,5,6,8,10,11,13,15,16,18\} & \dfrac{1919129}{6032880}\\
B & \{1,7,14\} & \dfrac{31441}{99225}\\
C & \{4,9,12,17\} & \dfrac{3157883}{10054800}
\end{array}
\]
Writing \(p_A,p_B,p_C\) for the three displayed site probabilities, one has the strict inequality \(p_C<p_B<p_A\), despite all sites having degree four and the graph having girth five. Exactly \(24\), \(111\), and \(4\) maximal independent sets have respective sizes \(5\), \(6\), and \(7\).

## Assumptions and scope
The vertex set is \(V=\{0,1,\ldots,18\}\). Begin with the undirected nineteen-cycle containing \(\{i,i+1\bmod19\}\) for every \(i\in V\). In addition, include all edges \(\{i,i+\ell_i\bmod19\}\), with the ordered offset sequence

```text
(8,4,7,4,8,5,7,4,7,8,4,5,7,8,4,8,4,8,4)
```

This is the published LCF realization of the Robertson graph. Repeated directions refer to the same undirected edge. The resulting graph has \(19\) vertices, \(38\) edges, degree four at every site, and girth five. Arrivals have independent identically distributed continuous times; only their order matters, so one may equivalently use a uniformly random permutation of all vertices. The process is irreversible and has *nearest-neighbor exclusion*: an accepted particle occupies its own vertex and prevents future acceptance at its neighbors. The result concerns only this graph and this kinetic rule, not edge-dimer deposition or an equilibrium spin system.

## Proof
For a subset \(S\subseteq V\), write \(N_S[v]=S\cap(\{v\}\cup N(v))\). Consider the remaining eligible vertices after previously occupied vertices and their blocked neighbors have been deleted. The next eligible vertex is uniformly distributed over \(S\), by exchangeability of the independent continuous arrival times. If \(P_S(z)\) is the generating polynomial of the number subsequently accepted, then
\[
P_{\varnothing}(z)=1,\qquad
P_S(z)=\frac{z}{|S|}\sum_{v\in S}P_{S\setminus N_S[v]}(z).
\]
For a fixed site \(u\), its occupation probability \(q_S(u)\) satisfies \(q_S(u)=0\) when \(u\notin S\); otherwise,
\[
q_S(u)=\frac1{|S|}+\frac1{|S|}
\sum_{v\in S\setminus N[u]}q_{S\setminus N_S[v]}(u).
\]
Both recurrences terminate strictly by the cardinality of \(S\), and uniquely determine exact rational outputs. Applying them to \(S=V\) gives the displayed law and all site probabilities. This is a finite exact computation rather than inference from sampled arrival orders.

An **independent proof by integration** uses each independent dominating set \(I\): these are exactly the possible terminal states. Fix such a set with \(k\) vertices. The greedy algorithm outputs \(I\) precisely when every \(w\notin I\) arrives after at least one of its neighbors in \(I\). Condition on an ordering \(\pi=(v_1,\ldots,v_k)\) of the arrival times of the sites in \(I\), namely \(0<t_1<\cdots<t_k<1\). Let \(c_j(\pi)\) count the outside vertices whose *first* adjacent member of \(I\) in this ordering is \(v_j\). Conditional on these times, the required event for all outside vertices has probability \(\prod_{j=1}^k(1-t_j)^{c_j}\). Integrating each ordered simplex gives exactly
\[
\Pr(I\text{ is selected})=
\sum_{\pi\in\operatorname{Sym}(I)}
\prod_{j=1}^k\left((k-j+1)+\sum_{i=j}^k c_i(\pi)\right)^{-1}.
\]
The denominator follows by substituting \(u_j=1-t_j\), then integrating \(1>u_1>\cdots>u_k>0\) from the last variable backward. This method does not use the first-eligible recurrence.

Exhaustively considering all \(2^{19}\) vertex subsets, retaining those that are simultaneously independent and dominating, gives exactly \(24\) sets of size five, \(111\) of size six and \(4\) of size seven. Summing the exact integral over those \(139\) sets gives the same three rational size probabilities as the first recurrence. Summing those individual-set probabilities over sets containing each vertex gives the same nineteen site probabilities. The total is exactly one, providing an independent normalization check.

For the orbit partition, two explicit adjacency-preserving permutations are included in `verify.py`. They generate a group of order \(24\) with orbits precisely \(A,B,C\). All vertices in these three classes respectively lie in \(33\), \(32\), and \(30\) six-cycles. These distinct rooted cycle counts prevent any automorphism from mixing the classes; hence the three listed classes are the full automorphism orbits, not just subgroup orbits.

## Verification
Run `python3 verify.py` using only the Python standard library. The program reconstructs the graph from the LCF offsets; checks degrees, edge count and absence of triangles and four-cycles; checks the two generating automorphisms, all site-orbit classes and six-cycle counts; evaluates the two logically different rational counting algorithms; enumerates every independent dominating subset; verifies the full distribution and every site probability, normalization and expectation. The exact independent-set enumeration examines every integer mask from zero through \(2^{19}-1\). No sample data or floating-point comparisons are used to establish the rational equalities.

## Relationship to prior work
Pippenger's 1989 work introduced and analyzed this random-order monomer process on regular graphs, including large-girth density behavior. Gamarnik and Goldberg (arXiv:0807.1277, first public July 8, 2008) prove regular-graph greedy bounds and finite-girth corrections; these concern aggregate bounds and asymptotic behavior rather than the evaluated nineteen-site distribution or three site orbits. Later local-limit work by Krivelevich, Mészáros, Michaeli and Shikhelman develops asymptotic principles for random greedy independent sets rather than this cage's exact finite probability law. The Robertson graph itself and its LCF presentation are not new. In particular, the tree-limit degree-four occupation probability \(1/3\) is not an exact finite-cage value: the cage's mean site coverage is \(540823/1705725\), smaller by exactly \(27752/1705725\). The general rational recurrences are elementary and are not asserted to be new; what is asserted is their exact evaluation and the orbit-resolved kinetic inequality on the named minimal cage.

## Limitations
This is an exact result for a single finite graph, not a thermodynamic limit or a general theorem for every regular graph. The arrival-time dynamics before saturation, higher joint-site correlation functions, and other exclusion radii are not determined here. An earlier exact, unindexed tabulation of this particular cage and monomer process might exist; historical priority requires independent literature review, particularly of Pippenger's inaccessible complete text. The exact numbers, proof and executable finite census establish mathematical correctness of the stated finite model, not independence or historical uniqueness. Independent audit has not been performed.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277 (first posted 2008-07-08). https://arxiv.org/abs/0807.1277
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401. https://doi.org/10.1137/0402034
3. SageMath graph generators, `RobertsonGraph` and its nineteen-entry LCF sequence. https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/smallgraphs.html
4. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms **64** (2024), 986–1015. https://doi.org/10.1002/rsa.21200
5. N. Robertson, *The smallest graph of girth 5 and valency 4*, Bulletin of the American Mathematical Society **70** (1964), 824–825.
