# Minimum independent domination on the Desargues graph has five doubled-hexagon slide components

## Finding

Let \(D\) be the twenty-vertex Desargues graph, equivalently the bipartite Kneser graph \(H(5,2)\) whose two parts are copies of the ten two-subsets of \([5]\), joined when the two subsets are disjoint. A state is a *minimum independent dominating set* of \(D\), and a transition replaces one selected vertex by an adjacent unselected vertex while preserving independent domination. Let \(M\) be the multigraph obtained by doubling every edge of the ordinary six-cycle, and let \(\operatorname{Sub}(M)\) be the simple graph obtained by subdividing every one of its twelve edges once. Then the independent domination number is \(6\), exactly \(100\) minimum independent dominating sets exist, and their token-slide graph is \(10K_1\sqcup5\operatorname{Sub}(M)\). It has exactly \(120\) edges; the ten isolated states are the pairs of identical triangles on three elements of \([5]\); each eighteen-state component is indexed by a four-element subset of \([5]\), is self-centered of eccentricity six, and has six degree-four and twelve degree-two vertices. The token-jump graph on this same minimum layer coincides with the token-slide graph. No statement is made about other hosts or nonminimum maximal independent sets.

The components are described without ambiguous multigraph notation as follows: take a six-cycle, put two parallel copies of each of its six edges, then insert a new vertex into each of the twelve edges. The resulting graph has six vertices of degree four and twelve of degree two; there are five such components and ten isolated states. The exact degree distribution is ten states of degree zero, sixty of degree two, and thirty of degree four. The component diameter and radius are both six for every nontrivial component.

## Assumptions and scope

Write \(E=\binom{[5]}{2}\), a ten-element edge set. Model the Desargues graph \(D\) as two disjoint labelled copies \(L=\{L_e:e\in E\}\) and \(R=\{R_e:e\in E\}\), with \(L_eR_f\) an edge if and only if \(e\cap f=\varnothing\). This is the standard bipartite Kneser presentation of the Desargues graph, isomorphic to \(GP(10,3)\); an explicit vertex permutation checking the two models is given below. An independent dominating set is a subset that contains no edge and whose closed neighborhood is all of \(V(D)\). Only sets of minimum possible cardinality are states. A legal move preserves size, domination, and independence at every step; for token sliding, the outgoing and incoming graph vertices must be adjacent.

For any \(A\subseteq E\), set
\[
F(A)=\{e\in E: e\cap a\neq\varnothing\text{ for every }a\in A\}.
\]
The convention for \(A=\varnothing\) is \(F(\varnothing)=E\). A state supported in \(L\cup R\) is represented by the pair \((A,B)\) selecting \(\{L_a:a\in A\}\cup\{R_b:b\in B\}\).

## Proof

**Galois-closure criterion.** For every pair of edge families \(A,B\subseteq E\), \((A,B)\) is independent and dominating in \(D\) if and only if \(B=F(A)\) and \(A=F(B)\). Independence says every selected right edge meets each selected left edge, hence \(B\subseteq F(A)\). If a right edge \(b\) is not selected, domination requires it to be disjoint from at least one selected left edge, so \(b\notin F(A)\). Thus \(B=F(A)\). The same argument with the two parts exchanged proves \(A=F(B)\). Conversely these equalities give independence and both domination conditions. The criterion is exact, including empty-side configurations.

**Complete finite closure enumeration.** Index the ten edges of \(K_5\) lexicographically. Every independent dominating set is uniquely determined by a ten-bit mask \(A\) satisfying \(F(F(A))=A\), with the other side \(B=F(A)\). This is a finite domain of exactly \(2^{10}=1024\) masks. Applying the displayed necessary-and-sufficient test to all masks gives the following complete table, indexed by \((|A|,|B|)\):

| Profile | Number of closed pairs |
|---|---:|
| \((0,10)\) | 1 |
| \((1,7)\) | 10 |
| \((2,4)\) | 15 |
| \((2,5)\) | 30 |
| \((3,3)\) | 70 |
| \((4,2)\) | 15 |
| \((4,4)\) | 5 |
| \((5,2)\) | 30 |
| \((7,1)\) | 10 |
| \((10,0)\) | 1 |

The entries sum to \(187\), and the minimum profile sum is six, attained exactly \(15+70+15=100\) times. The full loop that establishes the table is included as `verify_closure.py`, with an independent, direct twenty-vertex subset enumeration in `verify_gp.cpp`. This is a **complete finite verification**, not a statistical observation or an infinite-family inference.

**Explicit classification.** A minimum state has one of these forms:

1. For a three-element set \(T\subset[5]\), both \(A\) and \(B\) are the three edges of the triangle on \(T\). There are ten such pairs.
2. For a four-element set \(Q\subset[5]\) and one of its three perfect matchings \(P\), take \((A,B)=(P,E(Q)\setminus P)\) or its reversal. This gives six states for each \(Q\).
3. For a four-element set \(Q\subset[5]\), take \(A\) to be the three edges of one of the twelve Hamiltonian paths of \(K_4\) on \(Q\) and \(B=F(A)\). This gives twelve states for each \(Q\).

Here \(E(Q)=\binom{Q}{2}\). All displayed states pass the closure criterion. The explicit construction contains exactly \(10+5(6+12)=100\) distinct states, and its equality to the complete closure enumeration is checked by the same two representations. Triangle states use exactly three labels; all others use exactly the four labels of their uniquely determined \(Q\).

**All transitions and components.** A direct move between distinct states must have symmetric difference exactly two and must swap adjacent original graph vertices. Enumerating these swaps from the displayed one-hundred-state list gives: triangle states have degree zero; within each four-label class \(Q\), three \((2,4)\) and three \((4,2)\) states have degree four, and the twelve \((3,3)\) path states have degree two. Every path state is adjacent to two high-degree states, one of each type. Among the three matching-index states on each side, every pair of *different* matching indices is joined by precisely two length-two paths, and equal matching indices are not joined. Hence suppressing the twelve degree-two vertices and retaining edge multiplicity yields the doubled six-cycle: the simple underlying graph is \(K_{3,3}\) minus a perfect matching, which is \(C_6\). No transition crosses distinct \(Q\)'s. The ten triangle states are isolated. Each active component has \(6+12=18\) states, \(24\) edges, and all eighteen vertices have eccentricity six. This proves the claimed disjoint union and the overall edge count \(5\cdot24=120\).

**Jump-versus-slide observation (not claimed as a new general theorem).** On *any* graph, if independent dominating sets of the same size differ by replacing one vertex \(u\) with \(v\), then \(u\) and \(v\) are adjacent: otherwise \(v\), being unselected in the first set, has a selected neighbor that survives the replacement, contradicting independence of the second set. Thus every legal one-token jump between these states is necessarily a slide.

For exact cross-representation checking, the indices \(0,\ldots,9\) of \(GP(10,3)\) denote its outer vertices and \(10,\ldots,19\) its inner vertices. The following code-list gives their image indices in the above bipartite Kneser presentation, with \(0,\ldots,9\) the lexicographic first part and \(10,\ldots,19\) its second part:

```
0 17 6 11 9 10 7 16 1 19 18 3 12 5 14 8 13 2 15 4
```

Checking all thirty graph edges against this permutation is a finite direct isomorphism verification.

## Verification

Run `python3 verify_closure.py` with Python 3.8 or later; compile `verify_gp.cpp` using `g++ -std=c++17 -O2 verify_gp.cpp -o verify_gp` and run `./verify_gp`. Both programs contain assertions for every claimed finite invariant. The first verifies the closure theorem, the complete 1024-mask table, independent generation of all one hundred states from triangles/matchings/paths, all legal moves, the five doubled-hexagon components, and eccentricity six. The second independently enumerates all \(2^{20}\) subsets in the \(GP(10,3)\) model, checking independent domination up to size six, directly generates slides and jumps, and reconstructs component types and eccentricities. Neither program requires online resources, third-party Python packages, hidden data, or input files. The local outputs are embedded as `closure_output.txt` and `gp_output.txt`.

## Relationship to prior work

Independent domination of cubic and generalized Petersen graphs is studied by Kazemi (2010) and Dorbec, Henning, Montassier and Southey (2015); their stated bounds do not determine this exact optimal-state graph. Suzuki, Mouawad and Nishimura (2014) consider dominating-set reconfiguration via addition/deletion with variable size, which is a different transition model and does not impose independence. The standard Desargues graph is identified with the bipartite Kneser graph in the MathWorld graph entry. The present result concerns the complete, fixed-size, independent-dominating reconfiguration structure of this one graph, not the bounds or graph presentation already in the literature.

## Limitations

This is an exact theorem for the single twenty-vertex host \(D\), not a classification of every generalized Petersen graph. The counts are validated by full finite-domain enumeration, with independent implementations; no asymptotic or infinite-family claim is drawn from the computations. The literature review is not a guarantee against unindexed or unpublished prior work, and a broadly relevant cubic-graph article was only accessible at abstract level.

## References

- A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714, first posted 2014-01-22. https://arxiv.org/abs/1401.5714
- A. P. Kazemi, *On the Independent Domination Number of the Generalized Petersen Graphs*, African Diaspora Journal of Mathematics (2010); author-provided full text at https://www.researchgate.net/publication/254211834_On_the_Independent_Domination_Number_of_the_Generalized_Petersen_Graphs
- P. Dorbec, M. A. Henning, M. Montassier and J. Southey, *Independent Domination in Cubic Graphs*, Journal of Graph Theory, first online 2015-02-04, DOI:10.1002/jgt.21855.
- E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html.
