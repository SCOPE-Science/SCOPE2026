# Exact counting and uniform generation of optimal Kautz identifying codes

## Finding

Let \(K(2,n)\), \(n\ge2\), be the directed Kautz graph on ternary length-\(n\) strings having unequal adjacent symbols. There is an arc \(u_1\cdots u_n\to u_2\cdots u_nv\) when the appended symbol differs from \(u_n\). A *radius-one identifying code* is a set \(C\) of vertices for which the closed incoming signatures \(I_C(w)=C\cap(\{w\}\cup N^-(w))\) are all nonempty and pairwise distinct. Let \(M_n\) be the number of **labeled** identifying codes of minimum size (the symbols and string positions are fixed, not quotiented by automorphisms).

The minimum size is \(3\cdot2^{n-2}\). All minimum codes are in canonical bijection with directed cycle covers of \(K(2,n-1)\) **having no two-cycles**. Their exact number is

\[
M_n=\begin{cases}
2,&n=2,\\
4,&n=3,\\
27\cdot2^{3\cdot2^{n-3}-6},&n\ge4.
\end{cases}
\]

There is an exact uniform random sampler for this collection using independent local bits, except for three independent two-bit exclusions when \(n\ge4\). Its arithmetic/symbolic cost is linear in the number of vertices, apart from the cost of materializing the length-\(n\) string labels. The accompanying `sampler.py` implements it.

## Assumptions and scope

All vertices and directed edges are distinctly labeled by their ternary strings, and identifying signatures use **incoming** edges plus the vertex itself. A cycle cover is a spanning directed subgraph with exactly one incoming and one outgoing arc per vertex; a two-cycle consists of both directed arcs between two distinct vertices. Only \(n\ge2\) is claimed; in particular, no assertion is made for the nonidentifiable length-one Kautz digraph. Random choices in the sampler are uniform and independent where specified.

## Proof

**1. Sharp lower bound and structure.** Put \(D=K(2,n-1)\). The vertices of \(K(2,n)\) correspond bijectively to the arcs of \(D\) (a word of length \(n\) gives the arc from its prefix to its suffix of length \(n-1\)). For each \(p\in V(D)\), its two outgoing arcs in \(D\) have equal sets of *incoming predecessors* in \(K(2,n)\). If neither outgoing arc is in an identifying code, their signatures coincide. Thus every code uses at least one of these two arcs, implying \(|C|\ge|V(D)|=3\cdot2^{n-2}\).

If equality holds, exactly one outgoing arc at each \(p\) is selected. For the unselected arc from \(p\), its signature consists of the selected arcs entering \(p\); that signature must not be empty. There are exactly \(|V(D)|\) selected arcs and \(|V(D)|\) heads, so each vertex of \(D\) has exactly one selected incoming arc. The selected arcs therefore constitute a cycle cover. Conversely, a cycle cover selects exactly one incoming and outgoing arc at each vertex of \(D\).

**2. Separation condition.** Under a cycle cover, the signature of an unselected arc \(p\to q\) is the singleton containing the unique selected arc entering \(p\). The signature of a selected arc \(p\to q\) is the two-element set consisting of that arc and the selected arc entering \(p\). These elements differ because \(D\) has no loops. All unselected signatures are nonempty and distinct; two selected signatures can be equal only when the two selected arcs are each other's predecessors, exactly a directed two-cycle in the cover. Singleton and two-element signatures cannot coincide. Hence an optimal code is exactly a two-cycle-free cycle cover of \(D\).

**3. Counting the covers.** For \(n=2\), \(D\) is the loopless complete directed graph on three vertices. Its two directed Hamiltonian triangles are its only cycle covers without two-cycles, so \(M_2=2\).

For \(n\ge3\), write \(D=L(H)\), where \(H=K(2,n-2)\) and \(L\) is the line-digraph operation. At each vertex \(x\) of \(H\), a cycle cover of \(L(H)\) is specified by pairing its two incoming arcs bijectively with its two outgoing arcs. There are exactly two such local switches, and switch choices at distinct vertices are independent. The total number of cycle covers before removing two-cycles is thus \(2^{|V(H)|}\).

Every directed two-cycle of \(D\) consists of the two alternating length-\((n-1)\) words on one unordered pair of alphabet symbols. There are exactly three such possible two-cycles. Each occurs if and only if a prescribed choice is made at both corresponding vertices of \(H\). When \(n=3\), the graph \(H\) has three single-symbol vertices. The forbidden two-cycles occur exactly when two different vertices both use the backtracking switch. Thus the admissible switch patterns have at most one backtracking vertex, numbering \(1+3=4\).

When \(n\ge4\), the six vertices of \(H\) obtained from the three unordered symbol pairs and their two alternating length-\((n-2)\) strings are all distinct. For each pair, precisely one of its four two-switch patterns is forbidden, leaving three. The remaining \(|V(H)|-6=3\cdot2^{n-3}-6\) switches are unrestricted. Independence gives \(3^3\cdot2^{3\cdot2^{n-3}-6}\), as claimed. In particular, there is at least one optimal code for every \(n\ge2\).

**4. Uniform generation.** For \(n=2\), choose one of the two directed triangles with equal probability. For \(n=3\), choose one of the four admissible three-bit patterns equally. For \(n\ge4\), for each of the three disjoint alternating vertex pairs in \(H\), choose one of its three allowed two-switch patterns equally and independently; choose every remaining switch as a fair bit. The bijection just established proves each minimum code is sampled with the same probability \(1/M_n\). Construct the selected arcs by joining paired incoming and outgoing arcs at every \(x\). The Python implementation enumerates local incidence lists explicitly; generation is linear in their size with indexed vertices, and \(O(n|V(D)|)\) character work if string labels are assembled.

## Verification

The standalone `verify.py` reconstructs all cycle covers by local incidence bijections and checks the signatures against the Kautz graph definition. It returns \(2,4,27,1728\) optimal codes at \(n=2,3,4,5\), and for \(n\le4\) it independently enumerates all prefix-class selections without using cycle covers. The separate C++ program `independent.cpp` builds closed incoming neighborhoods independently and checks the counts at \(n=3,4,5\). The `sampler.py` program checks valid minimum codes at lengths \(2\) through \(8\). These finite checks corroborate the proof but are not the justification for the all-\(n\) formula; that follows from the bijections and local exclusions above.

Run with `python3 verify.py`, `python3 sampler.py` and `g++ -std=c++17 -O2 independent.cpp -o checker && ./checker`. All three use only standard libraries.

## Relationship to prior work

Boutin, Horan Goliber and Pelto (first arXiv version December 18, 2014) establish general radius-one identification bounds and constructions for directed **de Bruijn** graphs; their theory identifies the prefix-twin mechanism and motivates the network-code invariant. Martínez Barona's 2020 doctoral thesis proves the minimum identifying-code cardinality of Kautz digraphs (Theorem 4.3.5) and gives a general arc-identifying-code criterion for line digraphs (Theorem 4.3.1). Accordingly, the minimum size and the general cycle-cover viewpoint are **not** claimed as discoveries here. The specific contribution is the full **number of optimum labeled codes at every length**, the separate small-length exceptions, and a closed-form, rejection-free uniform sampling method obtained by resolving the three correlated short-cycle obstructions. The inspected pertinent sections do not state that enumerator or sampler. No priority claim is made beyond the identified and inspected sources.

## Limitations

This result treats exactly the ternary-symbol, degree-two Kautz digraph with radius-one *incoming* closed-neighborhood identification. It does not enumerate optima for larger degrees, identify symmetry-orbit counts, or address multiple simultaneous faults or larger radii. The formula concerns labeled codes, not equivalence classes. A 2020 source supplies related structural results; independently checking historical priority against all additional literature remains necessary. The supplied checking programs establish reproducibility of finite cases only, not an independent review of the infinite proof.

## References

1. D. Boutin, V. Horan Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, first arXiv submission December 18, 2014, https://arxiv.org/abs/1412.5842 . Relevant results: Theorems 3.5, 3.8, 3.11.
2. B. Martínez Barona, *\((1,\le\ell)\)-identifying codes in digraphs and graphs*, doctoral thesis, Universitat Politècnica de Catalunya, 2020, https://www.tesisenred.net/bitstream/handle/10803/669726/TBMB1de1.pdf?isAllowed=y&sequence=1 . Relevant results: Theorems 4.3.1, 4.3.2 and 4.3.5.
