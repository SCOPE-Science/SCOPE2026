# A first adaptive-shattering gap for spanning two-factors and an unbounded connected family

## Finding
Let \(G\) be a finite, undirected simple graph, and let \(\mathcal F_2(G)\) be the binary concept class indexed by all spanning \(2\)-regular subgraphs of \(G\), with one Boolean coordinate per edge of \(G\): an edge has value \(1\) precisely if it belongs to the chosen two-factor. Assume \(\mathcal F_2(G)\ne\varnothing\).

**Theorem.** The number of concepts, the VC dimension, and the Littlestone dimension of \(\mathcal F_2(K_n)\), respectively, are
\[
\begin{array}{c|ccc}
n&|\mathcal F_2(K_n)|&\operatorname{VCdim}&\operatorname{Ldim}\\\hline
3&1&0&0\\
4&3&1&1\\
5&12&3&3\\
6&70&4&5.
\end{array}
\]
Thus six is the least complete-graph order at which edge-membership adaptive shattering is strictly stronger than static shattering for two-factors.

For each integer \(s\ge1\), form \(G_s\) by taking \(s\) vertex-disjoint copies of \(K_6\) and joining successive copies by single edges. In each interior copy choose different attachment vertices for its two incident bridges. The resulting graph is connected and simple, has \(6s\) vertices and maximum degree at most six, and satisfies
\[
|\mathcal F_2(G_s)|=70^s,\qquad
\operatorname{VCdim}(\mathcal F_2(G_s))=4s,\qquad
\operatorname{Ldim}(\mathcal F_2(G_s))=5s.
\]
In particular, the gap is exactly \(s\) and unbounded on connected graphs of uniformly bounded maximum degree.

## Assumptions and scope
A two-factor is a spanning subgraph in which each vertex has degree exactly two, equivalently a vertex-disjoint union of cycles covering every vertex. Concepts are *labeled* edge-incidence vectors, not unlabeled isomorphism classes of factors. VC dimension is the largest number of fixed distinct edge coordinates realizing every Boolean word. Littlestone dimension is the largest depth of a complete binary decision tree with a queried edge at each internal node such that every root-to-leaf binary answer path is realized by at least one two-factor. A path's consistency determines the leaf witness. Repeated queries on a path cannot occur in a nontrivial complete shattered tree. Edge membership of a bridge is always zero in any two-factor.

## Proof
**The four finite orders.** On \(n\in\{3,4,5\}\), a spanning two-factor is necessarily a Hamiltonian cycle. Its number is \((n-1)!/2\), giving \(1,3,12\). On six vertices, there are \(60\) Hamiltonian cycles and \(10\) unions of two disjoint triangles, hence \(70\) two-factors. Counting hypotheses gives universal upper bounds \(\operatorname{VCdim},\operatorname{Ldim}\le\lfloor\log_2 |\mathcal F_2(K_n)|\rfloor\). The supplied witness arrays realize VC dimensions \(0,1,3\) and complete shattered decision trees attain Littlestone dimensions \(0,1,3\) for the first three orders.

**The six-vertex static upper bound.** Suppose five edge coordinates \(S\subseteq E(K_6)\) were shattered. The all-positive labeling yields a two-factor \(T\) containing \(S\). Since every two-factor has exactly six edges, \(S\) consists of five edges of \(T\), namely either (i) a path with five edges on all six vertices (one edge omitted from a Hamiltonian cycle), or (ii) a triangle plus a two-edge path on the other three vertices (one edge omitted from one of two disjoint triangles). In either case \(S\) contains the four path-edges \(ab,bc,de,ef\) with the triples \(\{a,b,c\}\) and \(\{d,e,f\}\) disjoint. The labeling demanding \(ab=bc=1\) and \(de=ef=0\) cannot extend to a two-factor: vertex \(b\) is saturated by \(ab,bc\); if those two edges belong to a triangle, the remaining three vertices must form a triangle, requiring both forbidden edges; if they belong to a Hamiltonian cycle, the remaining three vertices must form a path containing two of \(de,df,ef\), but after forbidding \(de\) and \(ef\) at most one of these remains. The fifth queried edge may be assigned either bit; neither assignment can be realized. This contradicts shattering. Therefore \(\operatorname{VCdim}\le4\). The packaged explicit four-edge query set and its \(16\) witnessed Boolean patterns give equality.

**The six-vertex online bound.** Every two-factor of \(K_6\) contains exactly six edges, and the symmetric group acts transitively on all \(15\) edges. Thus any fixed edge occurs in exactly \(70\cdot6/15=28\) two-factors. A complete depth-six shattered decision tree would require at least \(32\) distinct hypotheses in the positive branch of its first query (because this branch is a complete depth-five subtree). But every positive edge branch has only \(28\) hypotheses, impossible. Thus \(\operatorname{Ldim}\le5\). The packaged depth-five binary decision tree has \(31\) internal queries and \(32\) leaf certificates, each a distinct valid two-factor whose membership answers follow its leaf path. This proves \(\operatorname{Ldim}=5\).

**Connected amplification.** Every edge of a two-factor belongs to a cycle, so no bridge of \(G_s\) lies in any two-factor. Therefore restricting a two-factor of \(G_s\) to each \(K_6\) block yields a two-factor of that block, and conversely arbitrary blockwise two-factors combine to give one of \(G_s\). This is an exact Cartesian product of \(s\) copies of the \(70\)-concept class, on disjoint nonconstant coordinate sets; connecting-bridge coordinates are fixed zero. Its concept count is \(70^s\).

For classes on disjoint coordinate domains, VC dimensions add: concatenate shattered coordinate sets for the lower bound; for the upper bound, any shattered union restricts to a shattered coordinate set in each factor. Littlestone dimensions also add. For the lower bound, concatenate complete shattered decision trees from the factors; on each leaf substitute the next factor's tree, and choose independent factorwise witnesses. For the upper bound, recall the finite-class recurrence \(\operatorname{Ldim}(H)=\max_x(1+\min\{\operatorname{Ldim}(H_{x=0}),\operatorname{Ldim}(H_{x=1})\})\), ignoring constant coordinates and taking zero for singleton classes. If one queries a coordinate in factor \(i\), at least one branch reduces that factor's Littlestone rank by at least one. Induction on the sum of factor ranks bounds the product rank by that sum. Therefore the product has dimensions \(4s\) and \(5s\). Interior blocks receive at most two bridges, attached at distinct vertices, so every vertex has degree at most six; connectedness and simplicity are immediate.

## Verification
The accompanying independent programs are `generate_certificates.py` and `verify_certificates.py`, with `two_factor_certificates.json` and `verification_output.txt` as machine-readable witness data and recorded independent replay. The generator enumerates all candidate \(n\)-edge sets of \(K_n\) and retains exactly those with degree two at every vertex. The verifier **independently** enumerates Hamiltonian cycles by permutations modulo reversal and, when \(n=6\), the disjoint unions of two triangles. It checks every VC witness and every internal query and leaf of each complete shattered tree, recomputes the complete Littlestone recurrence, and exhaustively establishes failure to shatter any set of \(\operatorname{VCdim}+1\) edge coordinates for each \(3\le n\le6\). Every verification operation is finite and exact, using integer set/bit operations. To replay with Python 3, run `python3 verify_certificates.py two_factor_certificates.json`; the output should match `verification_output.txt`.

## Relationship to prior work
Axenovich et al. [1, Theorems 1–2] study **polychromatic edge colorings** simultaneously intersecting every spanning one-factor, two-factor, or Hamiltonian cycle of complete graphs. Their theorems do not evaluate the Boolean VC or Littlestone dimensions of membership-incidence classes. Chase and Freitag [2] develop general query-learning and Littlestone-rank bounds; the general framework does not supply this graph-specific six-vertex exact calculation. Mofidi [3, Theorem 3.3] studies static shattering for the hypergraph of **all simple cycles**, not the subclass of spanning two-factors; for example a single cycle need not cover all vertices, whereas every concept here does. An earlier incidence-closure result for Hamiltonian cycles concerns implication/closure of edge sets, not adaptive shattering, and it does not include the disconnected two-triangle two-factors of \(K_6\). Similarly, matroid basis-membership equality results do not subsume the theorem: two-factors are not the bases of a matroid on edges whenever more than one exists, since replacing a single selected edge by another changes degrees and cannot preserve a two-factor. The adaptive decision-tree assertion must therefore be checked separately.

## Limitations
Exact finite dimensions are determined only for complete graphs through six vertices. The connected-family formula applies to the specifically constructed chain of six-vertex blocks, not to arbitrary connected graphs of maximum degree six. The result gives no algorithmic characterization of general two-factor Littlestone dimension, no exact formula for larger complete graphs, and no historical-priority guarantee from bounded literature searches. The finite certificate is a proof of finite exact assertions once independently verified; it is not an infinite structural proof. Independent external audit has not been performed.

## References
[1] M. Axenovich, J. Goldwasser, R. Hansen, B. Lidický, R. R. Martin, D. Offner, J. Talbot, and M. Young, *Polychromatic colorings of complete graphs with respect to 1-, 2-factors and Hamiltonian cycles*, arXiv:1612.03298v1 (first posted 10 December 2016). https://arxiv.org/abs/1612.03298

[2] H. Chase and J. Freitag, *Bounds in Query Learning*, arXiv:1904.10122 (first posted 23 April 2019). https://arxiv.org/abs/1904.10122

[3] A. Mofidi, *On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs*, Bulletin of the Iranian Mathematical Society / Transactions on Combinatorics, https://doi.org/10.22108/toc.2021.127880.1832 .
