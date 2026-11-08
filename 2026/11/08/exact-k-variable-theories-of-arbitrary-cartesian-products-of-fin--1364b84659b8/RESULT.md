# Exact \(k\)-variable theories of arbitrary Cartesian products of finite cliques

## Finding

Let \(r=(r_1,\ldots,r_d)\) be any nonempty finite sequence of integers \(r_i\ge2\), and let
\[
X(r)=K_{r_1}\mathbin{\square}\cdots\mathbin{\square}K_{r_d}
\]
be its rectangular Hamming graph. Its vertices are words with coordinate \(i\) in an alphabet of size \(r_i\); two distinct words are adjacent if and only if they differ in exactly one coordinate. There are no vertex labels, edge labels, coordinate names, or counting quantifiers. All equivalences below concern the pure undirected graph language with equality and unrestricted quantifier depth.

**Theorem.** For any two such sequences \(r=(r_1,\ldots,r_d)\) and \(s=(s_1,\ldots,s_e)\), the following give a complete classification of equivalence under counting-free first-order sentences that use at most \(k\) variable names.

* At width one, every \(X(r)\) has the same theory.
* At width two, \(X(r)\) and \(X(s)\) have the same theory exactly when \(d=1\iff e=1\).
* At every width \(k\ge3\),
\[
X(r)\equiv_{\mathrm{FO}^{k}}X(s)
\quad\Longleftrightarrow\quad
\{\!\{\min(r_i,k):1\le i\le d\}\!\}
=
\{\!\{\min(s_j,k):1\le j\le e\}\!\}.
\]
Here braces with doubled delimiters denote multisets: multiplicity matters but coordinate order does not.

In particular, fixing \(d\ge1\), the number of width-\(k\) theories realized by products of exactly \(d\) nontrivial cliques is \(\binom{d+k-2}{k-2}\) for every \(k\ge3\). The least variable width that distinguishes any given \(X(r)\) from every nonisomorphic rectangular Hamming graph is exactly \(1+\max_i r_i\).

## Assumptions and scope

All factors are complete, simple graphs of finite order at least two; the product is the graph-theoretic Cartesian product. Factor order may vary arbitrarily from coordinate to coordinate. The number of factors is positive but unbounded. First-order formulas have equality and a single symmetric irreflexive adjacency relation; no counting quantifiers, distinguished coordinates, additional relations, or bounded quantifier-rank restriction. This theorem concerns equivalence of the stated family, not definability of that family among arbitrary finite graphs.

## Proof

**1. Widths one and two.** With one variable, a nonempty simple graph can test only the universally fixed atomic facts \(x=x\) and \(\neg E(x,x)\); quantification cannot differentiate these graphs. With two variables, all the products are vertex-transitive and every vertex has a distinct neighbor. When \(d=1\), the graph is complete, so no vertex has a distinct nonneighbor. When \(d\ge2\), each vertex has both a distinct neighbor and a distinct nonneighbor: change one or two coordinates, respectively. Within each of these two cases, Duplicator can preserve the equality/adjacency type of two pebbles after every move: when one pebble is stationary, all required types remain available. The sentence \(\exists x\exists y\,(x\ne y\land\neg E(x,y))\) separates the complete case from the noncomplete case.

**2. The sufficiency at every width \(k\ge3\).** Suppose the truncated factor-size multisets agree. After reordering coordinates, assume \(d=e\) and \(\min(r_i,k)=\min(s_i,k)\) for every \(i\). Maintain, for each coordinate separately, exactly the equality pattern among the at most \(k\) current pebble values. Suppose Spoiler lifts one pebble and leaves at most \(k-1\) stationary pebbles. In coordinate \(i\), a newly selected symbol either equals one of the symbols already represented or is fresh. If \(r_i<k\), then \(s_i=r_i\) and the two alphabets admit precisely the same equality patterns. Otherwise \(r_i,s_i\ge k\), so a fresh choice is possible in both alphabets despite at most \(k-1\) stationary symbols. Make the required choice independently in every coordinate, preserving all coordinatewise equalities. Consequently equality of whole vertices and the number of differing coordinates between any two pebbled vertices are preserved; in particular adjacency, meaning exactly one differing coordinate, is preserved. The invariant is permanent, establishing equivalence for arbitrarily many rounds and hence unrestricted quantifier depth.

**3. Intrinsically identifying factor-size classes using \(k\) variables.** For \(2\le t\le k\), define \(L_t(x,y)\) to mean that the two distinct adjacent vertices \(x,y\) belong to some clique of order \(t\). This has a formula using exactly \(t\) variable names: existentially choose the other \(t-2\) distinct vertices and require all pairwise edges. Take \(L_2(x,y)=E(x,y)\). Every clique of size at least three in a Cartesian product of cliques lies inside one coordinate fibre: if \(x\) differs from \(y\) in coordinate \(i\) and from \(z\) in a different coordinate \(j\), then \(y,z\) differ in two coordinates and cannot be adjacent. Hence an edge changing coordinate \(i\) belongs to an order-\(t\) clique exactly when \(t\le r_i\).

Define intrinsic edge-colour formulas
\[
C_t(x,y)=\begin{cases}
L_t(x,y)\land\neg L_{t+1}(x,y),&2\le t<k,\\
L_k(x,y),&t=k.
\end{cases}
\]
They use at most \(k\) variable names and, on \(X(r)\), select exactly the edges changing coordinates \(i\) with \(\min(r_i,k)=t\). The colours are not supplied in the signature: they are definitions in the pure adjacency language.

**4. Defining the count of factors of each colour.** Fix \(t\in\{2,\ldots,k\}\). Let \(P_{t,h}(x,y)\) assert the existence of a walk of length at most \(h\) whose every edge satisfies \(C_t\). For each fixed finite \(h\), \(P_{t,h}\) is expressible with the same \(k\) variable names. Start with \(P_{t,0}(x,y)\equiv(x=y)\) and use
\[
P_{t,h+1}(x,y)\equiv P_{t,h}(x,y)\lor
\exists z\bigl(P_{t,h}(x,z)\land C_t(z,y)\bigr).
\]
Only three variables are free across the two conjuncts. Bound variables inside each binary subformula can be alpha-renamed among the remaining \(k-2\) names, including the name of the outer variable absent from that subformula, without capture. Thus the recurrence stays within \(\mathrm{FO}^k\) for every \(k\ge3\).

Let \(m_t(r)=|\{i:\min(r_i,k)=t\}|\). The graph with precisely the \(C_t\)-edges has connected components obtained by fixing all coordinates outside that class, and each component is a Cartesian product of exactly \(m_t(r)\) complete graphs. Consequently its component diameter is \(m_t(r)\): one step changes at most one such coordinate, and each coordinate can be changed in one step. For each integer \(h\ge1\), the \(\mathrm{FO}^k\) sentence
\[
\exists x\exists y\bigl(P_{t,h}(x,y)\land\neg P_{t,h-1}(x,y)\bigr)
\]
is true exactly when \(m_t(r)\ge h\). Indeed, within a component there exist vertices at distance exactly \(h\) if and only if at least \(h\) such coordinates exist; vertices in different components do not satisfy \(P_{t,h}\). The complete theory therefore recovers each multiplicity \(m_t(r)\), proving necessity of the multiset equality.

**5. Enumeration and sharp isolation width.** For fixed factor count \(d\) and width \(k\ge3\), each multiset of size \(d\) drawn from the \(k-1\) possible truncated orders \(2,\ldots,k\) is realized, and all are inequivalent by step 4. Stars and bars gives \(\binom{d+k-2}{k-2}\). Put \(R=\max_i r_i\). At width \(R\), increasing one maximal factor from \(R\) to \(R+1\) produces a nonisomorphic but equivalent graph: if \(R\ge3\), use step 2; if \(R=2\), use step 1 or 2 according to whether there is one factor or at least two. At width \(R+1\), every original factor size is below the cutoff, so step 4 reconstructs their exact multiset. Cartesian products of nontrivial complete graphs are isomorphic precisely when their factor-size multisets agree (uniqueness of connected Cartesian prime factorization; each nontrivial clique is Cartesian-prime). Hence the isolation width is \(R+1\).

## Verification

The standalone standard-library program `check_rectangular_logic.py` checks 392 coordinate extension-table parameter cases at widths three through six, for single-coordinate alphabet orders two through eight with matching truncated orders. It independently constructs finite Cartesian products, recovers the intrinsic edge-colours from common-neighbour cliques, and checks that the diameters of all coloured components equal the corresponding factor multiplicities, in 90 additional graph/width/colour parameter cases. Every check passes; the exact stdout is in `check_output.txt`. This computation is finite corroboration only, not an exhaustive proof over all products or all \(k\). The proof above covers all parameter ranges.

## Relationship to prior work

Klavžar and Peterin (2005) characterize subgraphs, induced subgraphs, and isometric subgraphs of Cartesian products of complete graphs, and provide their coordinate/edge-label viewpoint; they do not derive counting-free finite-variable equivalence. Grohe and Otto (2012) establish general relationships between plain pebble equivalence and logic/linear-equation methods, but not this factor-multiset classification. Cai, Guo, Gavrilyuk, and Ponomarenko (2024) study Cartesian products using coherent configurations and counting Weisfeiler–Leman methods, including examples with Hamming graphs; their counting-logic invariants are strictly finer than the counting-free equivalences here and their theorems do not imply the stated collapse.

Restricted cases had previously been obtained for equal-size Hamming factors and for the two-factor rook graphs. The statement here covers arbitrary finite lengths and arbitrary heterogeneous factor-size multiplicities simultaneously. Its additional proof ingredient is that each truncated factor-size class is intrinsically definable by an edge-clique formula, and its **number of coordinates**, not simply the presence of the class, is then recoverable via bounded-variable formulas for coloured component distances. The earlier restricted cases do not by themselves classify arbitrary products with three or more differently sized factors. The exact historical priority of the general statement remains subject to further independent literature review.

## Limitations

No extension to products with non-complete factors, product coordinates of size one (which are invisible), arbitrary additional edge labels, counting quantifiers, or arbitrary finite graphs is claimed. A formula distinguishes each fixed finite factor count, but no uniform finite sentence is claimed to recover an unbounded count. The coding tests do not replace the arbitrary-parameter pebble-game argument. The mathematical assessment is not an independent audit, and literature searches cannot establish novelty conclusively.

## References

1. S. Klavžar and I. Peterin, *Characterizing Subgraphs of Hamming Graphs*, Journal of Graph Theory **49** (2005), 302–312. First publicly available journal version dated 2005-04-08. DOI: 10.1002/jgt.20084; full author-hosted text: https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf.
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, LIPIcs **16**, 289–304. DOI: 10.4230/LIPIcs.CSL.2012.289; https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289.
3. J. Cai, J. Guo, A. L. Gavrilyuk, and I. Ponomarenko, *Cartesian products of graphs and their coherent configurations*, arXiv:2411.02689 (2024), https://arxiv.org/abs/2411.02689.
