# Hexagonal-block rigidity and the exact extremal census of external one-types in outerplanar graphs

## Finding
Let \(G\) be any finite simple outerplanar graph and let \(A\subseteq V(G)\) be a **labelled** set of \(m=2t+1\geq3\) distinguished vertices. Define the external open-neighbourhood one-type family
\[
\mathcal T(G,A)=\{N_G(v)\cap A:v\in V(G)\setminus A\}.
\]
The sharp number of such types is the previously bounded extremal value
\[
|\mathcal T(G,A)|\leq m+1+3t=(5m-1)/2.
\]
**Equality classification.** Equality holds if and only if \(\mathcal T(G,A)\) consists of the empty set, all \(m\) singleton sets, and the non-singleton supports described by a *three-uniform hypertree* on \(A\): its \(t\) three-point hyperedges have an incidence tree, and every hyperedge \(\{a,b,c\}\) contributes independently exactly one of the following four three-support packets:
\[
\begin{aligned}
&\{\{a,b\},\{a,c\},\{b,c\}\},\\
&\{\{a,b,c\},\{a,b\},\{a,c\}\},\\
&\{\{a,b,c\},\{a,b\},\{b,c\}\},\\
&\{\{a,b,c\},\{a,c\},\{b,c\}\}.
\end{aligned}
\]
Conversely, every such packet assignment is realizable by a finite outerplanar graph with that labelled parameter set.

In particular, the number of **distinct labelled extremal type families** (not the number of host graphs) for \(m=2t+1\geq3\) is exactly
\[
\boxed{\mathcal E_{2t+1}=4^t\,\frac{(2t)!}{2^t t!}(2t+1)^{t-1}=\frac{2^t(2t)!}{t!}(2t+1)^{t-1}.}
\]
The first values at \(m=3,5,7\) are \(4,240,47040\). For \(m=1\) the unique extremal type family is \(\{\varnothing,\{a\}\}\).

The equality classification and the exact extremal-family count, rather than the already-established linear bound, are the new claims assessed here.

## Assumptions and scope
All graphs are finite, undirected, simple and outerplanar; disconnected graphs are permitted. The marked vertices are individually named and distinct. The external universe contains only vertices **outside** \(A\), and the types are **open** neighbourhoods. Families are sets of subsets of \(A\), so repeated external witnesses are not counted. A three-uniform hypertree on \(2t+1\) labelled vertices has \(t\) distinct triples, with connected acyclic vertex–hyperedge incidence graph. Its triples may share one vertex, but neither two nor more.

## Proof
**1. An incidence bound with a strict equality case.** Let \(H=(A,B;E)\) be a bipartite outerplanar graph whose \(B\)-vertices have degree at least two and pairwise different neighbourhoods in \(A\). We prove
\[
2|B|\leq 3(|A|-1).
\]
For a connected component containing \(B\), root its block–cut tree at an arbitrary \(A\)-vertex. A bridge is treated as a two-vertex block. Orient blocks away from the root: each block has one parent vertex already introduced, and all its other vertices are new. Give a block charge \(3a-2b\), where \(a,b\) are its numbers of newly introduced \(A\)- and \(B\)-vertices. These charges add to \(3(|A|-1)-2|B|\) in a connected component.

A bridge with an \(A\)-parent introduces one \(B\) and has charge \(-2\); a bridge with a \(B\)-parent introduces one \(A\) and has charge \(+3\). A nonbridge block is a two-connected bipartite outerplanar graph, hence its outer Hamilton cycle has equally many vertices in the two shores, say \(s\geq2\) each. With an \(A\)-parent the charge is \(s-3\), which is negative only for \(s=2\) (charge \(-1\)); with a \(B\)-parent the charge is \(s+2\geq4\).

Every negative bridge introduces a new \(B\)-vertex that has degree one in that block; its global degree at least two forces some child block rooted at this \(B\)-vertex. Every negative four-cycle with \(A\)-parent introduces two new \(B\)-vertices having the same two \(A\)-neighbours inside that block. Because their full neighbourhoods must differ, at least one has a child block. In either case, associate a negative block with one such child block rooted at a newly introduced \(B\)-vertex. Associated child blocks are distinct for distinct negative blocks. Each costs at least \(+3\), strictly exceeding the magnitude of its associated negative charge. All unassociated charges are nonnegative. The total charge is nonnegative, and equals zero only when **every block has zero charge**.

Zero-charge blocks are precisely the nonbridge blocks with \(s=3\) and an \(A\)-parent. Their six-vertex spanning outer cycles are hexagons, and bipartiteness plus outerplanarity allows at most one opposite-part chord. Hence any connected equality case is a tree of six-vertex blocks, each a hexagon with zero or one chord, glued exclusively at \(A\)-vertices. Conversely these blocks have charge zero and pairwise distinct \(B\)-neighbourhoods (each block meets the rest in at most one \(A\)-vertex).

If \(H\) is disconnected, applying the connected inequality to all components with \(B\)-vertices gives \(2|B|\leq3(|A|-c)\), where \(c\) is the number of components after including isolated \(A\)-vertices. Equality in \(2|B|=3(|A|-1)\) forces \(c=1\), apart from the trivial \(|A|=1,|B|=0\) case. Thus the zero-charge classification holds for the entire incidence graph.

**2. Reduction from one-types.** From every different external trace of size at least two choose one external representative. Keep just its edges into \(A\). The resulting bipartite graph \(H=(A,B)\) is outerplanar and satisfies the preceding assumptions. It has at most \(3(m-1)/2\) representatives. There are at most \(m\) singleton traces and one empty trace. Hence the announced type bound. When \(m=2t+1\) and equality holds, all \(m+1\) small traces must occur and \(2|B|=3(m-1)\), so \(H\) has exactly the hexagonal-block structure of Step 1.

For a six-vertex hexagonal block with parameter shore \(\{a,b,c\}\), the three opposite-shore vertices correspond to the three pairs \(ab,ac,bc\). The unique possible chord enlarges exactly one of these pairs to the full triple; this gives precisely the four packets displayed in the theorem. Contracting each hexagonal block to a triple records a three-uniform hypertree on \(A\). The block decomposition makes this record unique.

**3. Converse and sharpness.** Given any such hypertree, replace each triple by its alternating six-cycle between the three parameter vertices and three fresh external vertices, and optionally add the chord prescribed by its packet. Different blocks intersect only at parameter cut vertices. Their block sum is outerplanar; the external neighbourhoods from different blocks are distinct because distinct hypertree triples meet at most once. Add one external pendant vertex adjacent to each parameter and one isolated external vertex. This realizes all the specified types and attains \((5m-1)/2\).

**4. Enumeration.** Root the hypertree at any fixed labelled parameter vertex \(r\). Orient every triple toward \(r\). The two vertices farther from the root in each triple form one unordered pair. These pairs partition the other \(2t\) vertices in \((2t)!/(2^t t!)\) ways. For any fixed pairing, a generalized leaf-pair Prüfer deletion records an arbitrary sequence of \(t-1\) parameter labels: repeatedly delete the lexicographically first leaf pair and record its parent, leaving one final pair attached to \(r\). Conversely, from an arbitrary word of length \(t-1\), repeatedly take the lexicographically first remaining pair with neither member in the remaining word, attach it to the first letter, remove that letter, and ultimately attach the last pair to \(r\). A pair exists at each stage by pigeonhole; this is a bijection. Thus the number of labelled three-uniform hypertrees is \((2t)! (2t+1)^{t-1}/(2^t t!)\). Each triple independently has four packets; the incidence block decomposition uniquely recovers both hypertree and packet choices from the type family. Multiplication by \(4^t\) proves the formula.

## Verification
Run `python verify.py` after installing `networkx`. The checker verifies explicit sharp constructions for parameter counts one through twelve, exhaustively enumerates outerplanar maximum-size incidence support families for parameter counts one through five (yielding four at three and 240 at five), and independently enumerates labelled triangle-block hypertrees for three, five and seven parameters (one, fifteen and 735). Output ends with `VERIFY_OK`. The proof above, not finite enumeration, establishes the classification and formula for all sizes.

## Relationship to prior work
Rall and Slater (1984) already proved a sharp outerplanar locating-dominating inequality, yielding the numerical external type bound after adding one possible empty trace. The bound, its sharpness and the existence of extremal outerplanar examples are **not** claimed as new. Berthe, Foucaud, Lehtilä and Parreau (arXiv:2607.16889, first submitted 18 July 2026) survey this inequality and develop neighbourhood complexity of bounded treewidth and pathwidth. Beaudou and collaborators (arXiv:2501.08895) study broader distance-profile estimates for excluded minors and outerplanar graphs. The distinct contribution here is a complete *equality-type family classification and labelled extremal count* in the external open-neighbourhood setting for odd parameter sizes. Their stated bounds do not alone determine the equality structure or multiplicities.

## Limitations
The theorem concerns only the odd-cardinality maximum layer of **external** open-neighbourhood profiles. It does not classify even-cardinality maxima, all host graphs realizing a type family, closed neighbourhoods or arbitrary-radius distance profiles. The original full text of Rall and Slater (1984) was not obtained; an earlier unlocated equality classification or hypertree enumeration remains a priority risk. Computational evidence is finite, and independent validation has not been performed.

## References
1. G. Berthe, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889 (initial public submission 18 July 2026), https://arxiv.org/abs/2607.16889.
2. L. Beaudou, J. Bok, F. Foucaud, D. A. Quiroz, J.-F. Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs*, arXiv:2501.08895 (initial public submission 15 January 2025), https://arxiv.org/abs/2501.08895.
3. D. F. Rall, P. J. Slater, *On location-domination numbers for certain classes of graphs*, Congressus Numerantium 45 (1984), 97–106, https://www.researchgate.net/publication/264911602_On_location-domination_numbers_for_certain_classes_of_graphs.
4. N. Bousquet, Q. Deschamps, T. Lehtilä, A. Parreau, *Locating-dominating sets: From graphs to oriented graphs*, Discrete Mathematics 346 (2023), article 113124, https://doi.org/10.1016/j.disc.2022.113124.
