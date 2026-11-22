# Exact dimer-jamming probabilities and strict matching-size dominance on the dodecahedral graph

## Finding
Let \(D\) be the twenty-vertex dodecahedral graph \(\operatorname{GP}(10,2)\). Assign independent identically distributed continuous random priorities to its thirty edges, and, in increasing-priority order, accept an edge exactly when neither endpoint belongs to an earlier accepted edge. Write \(J\) for the terminal number of accepted edges. Its exact law is
\[
\begin{array}{c|ccccc}
 k&6&7&8&9&10\\ \hline
 \Pr(J=k)&\frac{1}{3125}&\frac{91294494167}{2756754000000}&\frac{1796566904214749}{4862914056000000}&\frac{2544405065946811}{4862914056000000}&\frac{123231298227}{1667666000000}
\end{array}
\]
with all other values impossible. In particular,
\[
\mathbb E J=\frac{42002246692500247}{4862914056000000},\qquad
\Pr(J=10)=\frac{123231298227}{1667666000000}.
\]

There are exactly \(3781\) maximal matchings of \(D\); their size multiplicities for \(k=6,7,8,9,10\) are respectively \(5,420,2280,1040,36\). Let \(U\) be the size of a uniformly sampled maximal matching (not a matching weighted by random priorities). Then the greedy law **strictly first-order stochastically dominates** this uniform-maximal law:
\[
\Pr(J\le k)<\Pr(U\le k),\qquad k\in\{6,7,8,9\}.
\]
In particular, a perfect matching is \(\frac{155312512865429}{20011992000000}\) times as likely under greedy adsorption as under the uniform-maximal model, approximately \(7.761\) times.

## Assumptions and scope
The dodecahedral graph is the generalized Petersen graph \(\operatorname{GP}(10,2)\) with vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and thirty edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+2}\), taking indices modulo ten. It is the graph of the smallest fullerene, with twenty vertices and twelve pentagonal faces. An edge's priority is almost surely distinct from every other priority, so only its relative order matters. The output is a maximal matching, because every rejected edge has an endpoint already occupied. The comparison variable \(U\) samples every *labeled edge set* that is a maximal matching with equal probability. No averaging over graph isomorphisms, automorphism classes, or graph substrates is involved.

## Proof
Write \(A\) for any currently unoccupied vertex set, \(E(A)\) for the original edges with both endpoints in \(A\), and \(m(A)=|E(A)|\). Let \(F_A(z)=\mathbb E[z^{J_A}]\) be the generating polynomial of the number of additional accepted edges from that state. By exchangeability of unprocessed independent priorities, the next accepted edge, when one exists, is uniform on \(E(A)\). Hence
\[
F_A(z)=\begin{cases}1,&m(A)=0,\\
\frac{z}{m(A)}\displaystyle\sum_{\{u,v\}\in E(A)}F_{A\setminus\{u,v\}}(z),&m(A)>0.
\end{cases}
\]
Each transition removes two vertices; thus this is an exact finite backward induction, with no approximation. At the initial state \(A=V(D)\), the recurrence has \(94940\) reachable states and yields the five rational probabilities displayed above.

For an independent exhaustive route, enumerate each matching by taking the smallest unassigned vertex, either leaving it unmatched or pairing it to a still-unassigned neighbor. At the terminal branch retain a matching if and only if its remaining unmatched vertices form an independent set. This is equivalent to maximality: a new disjoint edge exists precisely when two unmatched vertices are adjacent. Each maximal matching is generated exactly once, giving the size multiplicities \((5,420,2280,1040,36)\).

To calculate the chance of each such output by a distinct recurrence, for any partial matching \(S\) define \(q(S)\) as the probability that the *first* \(|S|\) accepted edges, unordered, are exactly \(S\). Set \(q(\varnothing)=1\). Decomposing by which member of \(S\) is the last accepted edge gives
\[
q(S)=\sum_{e\in S}\frac{q(S\setminus\{e\})}{m(V(D)\setminus V(S\setminus\{e\}))}.
\]
The denominators are positive because the edge \(e\) is still available. For a maximal matching \(M\), the event counted by \(q(M)\) is exactly that the final accepted matching is \(M\). Summing \(q(M)\) over all maximal matchings of each size produces precisely the same rational law as the vertex-state recurrence. This second method uses \(111376\) matching prefixes and distinguishes individual outputs, rather than only occupied vertex sets.

For strict stochastic dominance, compute exactly the differences \(\Pr(U\le k)-\Pr(J\le k)\) at the four nontrivial thresholds:
\[
\begin{array}{c|c}
k&\Pr(U\le k)-\Pr(J\le k)\\ \hline
6&\frac{11844}{11815625}\\
7&\frac{823100515754893}{10423286874000000}\\
8&\frac{5746573892635665283}{18386678045736000000}\\
9&\frac{405901562596287}{6305445146000000}
\end{array}
\]
All four are strictly positive. At all other thresholds the cumulative laws are jointly zero or jointly one, proving the stated dominance. The perfect-matching bias factor is the exact ratio \(\Pr(J=10)/(36/3781)\).

## Verification
Run `python3 verify_dodeca.py` using Python 3.10 or later and only its standard library. The program constructs \(\operatorname{GP}(10,2)\) directly by modular arithmetic, checks cubic degree and the thirty edges, evaluates both exact-rational recurrences, checks every one of the \(3781\) maximal matchings, confirms their individual probabilities sum to one, and proves all four strict cumulative inequalities using exact fractions. The verified counts are \(94940\) vertex-mask states and \(111376\) matching prefixes. This exhaustive computation is a valid finite proof because the recurrences and unique enumeration exhaust every possible state and matching, not a Monte Carlo sample.

## Relationship to prior work
Penrose and Sudbury (2005) formulate dimer random sequential adsorption on graphs and establish general probabilistic results, without giving this exact twenty-site law. Gamarnik and Goldberg (2008) investigate random greedy matchings on regular graphs, including girth-dependent bounds, but do not specialize their theorems to a complete dodecahedral distribution. Andova, Kardoš and Škrekovski (2014) show the dodecahedral graph has saturation number six; the minimum size itself is prior work, not part of the novelty claim. Other established dodecahedral matching-complex computations enumerate the thirty-edge graph's matchings, including its thirty-six perfect matchings, and compute topological invariants; these unweighted counts do not imply the probabilities of this random edge-priority process. A published exact Petersen-graph dimer-adsorption law is closely related methodologically, but concerns the nonisomorphic ten-vertex graph and does not determine the present distribution or four stochastic-order inequalities. The contribution is the exact evaluated dodecahedral kinetic law and its strict comparison with the uniform distribution on maximal matchings.

## Limitations
The statement concerns one distinguished finite fullerene graph; no analogous result for other fullerenes or universal dominance principle is claimed. In fact, dominance of random greedy matching over uniform maximal matchings can fail even for a connected six-vertex graph: for edges \(\{01,12,14,15,23,24,25\}\) there are eight maximal matchings (one of size one, seven of size two), while the greedy probability of size one is \(1/7>1/8\). The dodecahedral inequality therefore does not follow merely from the definition of greedy matching. The exact fractions are finite mathematical predictions, not measured physical adsorption rates. No independent validation has yet been performed. An unindexed equivalent dodecahedron table remains a residual priority risk.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519, first public 2005-03-24, https://arxiv.org/abs/math/0503519.
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277, first public 2008-07-08, https://arxiv.org/abs/0807.1277.
3. V. Andova, F. Kardoš and R. Škrekovski, *Sandwiching saturation number of fullerene graphs*, arXiv:1405.2197, first public 2014-05-09, https://arxiv.org/abs/1405.2197.
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034 (abstract and bibliographic information consulted; full text not inspected).
5. *Mod-\(2\) homology of the dodecahedral matching complex* (published exact matching-count calculation, 2026), and *The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres* (published matching-count and topology calculation, 2026); these results already give ordinary matching multiplicities, but not random-order kinetic probabilities.
6. *Exact dimer-jamming kinetics on the Petersen graph* (published exact ten-site adsorption law, 2026).
