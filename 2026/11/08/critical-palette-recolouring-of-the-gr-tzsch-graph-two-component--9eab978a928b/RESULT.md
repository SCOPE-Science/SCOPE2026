# Critical-palette recolouring of the Grötzsch graph: two components and sixty diametral pairs

## Finding
Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph. Write \(R_4(G)\) for the graph whose vertices are all proper assignments of four **named** colours to the vertices of \(G\), with an edge when one vertex is recoloured while propriety is retained. The following complete finite metric classification holds:

* The \(12{,}480\) colourings form precisely **two isomorphic connected components**, each with \(6{,}240\) vertices. The total number of undirected recolouring edges is \(45{,}240\).
* Each component has **radius \(15\)** and **diameter \(17\)**. Within each component, exactly \(1{,}080\), \(5{,}100\), and \(60\) vertices have eccentricities \(15\), \(16\), and \(17\), respectively.
* Across both components there are exactly **\(60\) unordered diametral pairs**. Every one of the \(120\) peripheral vertices has **exactly one** other vertex at distance \(17\). Those \(120\) peripheral vertices constitute a single orbit under the natural colour-permutation and pentagon-dihedral automorphisms.

In particular, the full graph \(R_4(G)\) is disconnected, so the diameters above are **componentwise** and do not assign a finite distance between configurations in different components. The number of proper four-colourings is classical and is not asserted as a new enumeration.

## Assumptions and scope
Use zero-based labels \(v_0,\ldots,v_4,u_0,\ldots,u_4,w\), in that order. Indices on \(v_i,u_i\) are taken modulo \(5\). The edges of \(G\) are \(v_iv_{i+1}\), \(u_iv_{i-1}\), \(u_iv_{i+1}\), and \(u_iw\) for each \(i\in\{0,1,2,3,4\}\). These are twenty distinct undirected edges. The palette is exactly \(\{0,1,2,3\}\), and colours are *named*: globally permuted colourings are different vertices in \(R_4(G)\). A move changes exactly one coordinate to a different colour that occurs at none of its neighbours. The distance of a pair is its minimal number of moves, only defined when the two configurations lie in the same connected component.

## Proof
A finite exhaustive proof has two independently implemented enumerations, plus a symmetry reduction whose validity can be verified directly from the edge formula. The embedded `verification/exhaustive.cpp` and `verification/symmetry.py` contain the complete enumeration and assertions/results described here.

**Complete state enumeration.** The first program visits all \(4^{11}\) possible assignments by backtracking, allowing colour \(c\) at vertex \(i\) precisely when it is different from the colours on already assigned neighbours. This enumerates every and only proper colouring exactly once. It records each colouring as an integer with eleven two-bit digits; the bijection is injective. The independent program first enumerates proper assignments to the pentagon \(v_0,\ldots,v_4\), chooses the apex colour, and then independently chooses each \(u_i\) from the colours absent at \(w,v_{i-1},v_{i+1}\). Those are all the constraints involving \(u_i\), since no two shadow vertices are adjacent. It checks \(12{,}480\) distinct states and rechecks all twenty edge constraints.

**Exact moves and components.** For each state, the first program tests all eleven vertices and all four alternative colours, accepting exactly those absent from the neighbourhood. Lookup of the resulting two-bit word determines its endpoint. The second program instead modifies tuple coordinates and independently looks them up. Both construct \(45{,}240\) undirected edges and find precisely two components of size \(6{,}240\). The second program explicitly checks that every move has its reverse. The first program additionally obtains the degree histogram \(5:480,6:2640,7:3840,8:4320,9:1200\).

**Exact shortest paths.** For each of the \(12{,}480\) states, the first program runs ordinary breadth-first search in the finite, unweighted graph just constructed. Breadth-first search visits vertices by nondecreasing path length and therefore returns exact minimum numbers of legal moves. All componentwise eccentricities and unordered pair counts follow by taking maxima and counting each pair once. This is an exhaustive finite proof, not sampling. The second program uses a different method to cross-check the full distance distribution: the ten automorphisms \(i\mapsto \pm i+b\pmod 5\) act simultaneously on the pentagon and shadow indices, and the twenty-four permutations of the four named colours also preserve the graph and its moves. The combined \(240\) operations partition the states into exactly \(56\) orbits (forty-eight of size \(240\) and eight of size \(120\)). One breadth-first search per orbit gives the same distance distribution, as each automorphism is an isometry. An orbit-by-orbit endpoint check finds precisely one orbit of size \(120\) with eccentricity \(17\), whose members each have exactly one state at distance \(17\). Counting ordered pairs and dividing by two yields \(60\) unordered diametral pairs.

Here is the complete distribution of unordered finite-distance pairs across both components, indexed by distance \(1,2,\ldots,17\):
\[
(45240,164280,409080,807600,1371600,2103600,2978040,
3904800,4766640,5471760,5871600,5428440,3680400,
1552080,346200,29940,60).
\]
Its sum is \(38{,}931{,}360=2\binom{6240}{2}\), accounting for every distinct connected pair exactly once.

**Explicit sharpness witness.** In the vertex order fixed above, take
\[
a=(3,2,0,3,2,3,1,1,1,2,0),\qquad
b=(2,3,1,2,3,2,0,0,0,3,1).
\]
Both are proper. A path from \(a\) to \(b\) consists of the following seventeen pairs `(vertex_index, new_colour)`, applied successively:
```
(0,0), (5,1), (1,3), (2,2), (3,0), (4,3), (9,3),
(0,2), (10,2), (5,0), (6,0), (8,0), (2,1), (3,2),
(7,0), (10,1), (5,2)
```
The independent verifier checks that each move is legal, that the final state is \(b\), and that its complete breadth-first distance from \(a\) is exactly \(17\). The path alone proves an upper bound for this pair; the exhaustive BFS establishes its lower bound and all claimed global upper bounds.

## Verification
From the directory holding the extracted files, run:
```
g++ -O3 -std=c++17 verification/exhaustive.cpp -o exhaustive
./exhaustive
python3 verification/symmetry.py
```
The C++ program uses only C++17 standard-library features and performs all-source shortest-path searches; the Python program uses only the Python standard library and independently checks symmetry-orbit distance distributions, antipodes, and a literal shortest path. Both were executed from their actual source files, and the reported counts agree. Their algorithms enumerate **all** finite states or rigorously equivalent orbit representatives; no infinite or extrapolated claim is made.

## Relationship to prior work
The Grötzsch graph is the classical Mycielski construction applied to the pentagon, and its chromatic number and four-colouring count are established facts. The prior count of \(12{,}480\) is used as a check, not treated as a new result. Cereceda, van den Heuvel and Johnson prove that the \(k\)-recolouring graph of a \(d\)-degenerate graph is connected for \(k\ge d+2\). The Grötzsch graph is \(3\)-degenerate, so this supplies **five-colour connectivity**, but it does not apply to its critical four-colour graph. Johnson and collaborators develop algorithms and complexity results for shortest recolouring paths, not the exact two-component metric of this fixed graph. Other work on graph reconstruction from colouring-reconfiguration graphs likewise does not state these particular finite componentwise eccentricity and antipode counts. Only the **four-colour critical-palette metric classification** is proposed as new.

## Limitations
The result is exact for the single specified labelled graph and the fixed four-colour palette only; it gives no theorem for larger Mycielski graphs, the five-colour diameter, or other allowed moves. No historical-priority or independent scholarly certification is claimed: equivalent computations may appear in unindexed or inaccessible literature. An earlier July 2005 report has month-level date evidence rather than a verified exact day; the dated archival source used for the classification's literature scope is the March 25, 2014 preprint noted below. Computational correctness is supported by full finite enumeration, two independent implementations and an explicit witness, but remains subject to ordinary implementation and specification risk.

## References
1. L. Cereceda, J. van den Heuvel, M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, LSE-CDAM-2005-11 (July 2005), https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf.
2. M. Johnson et al., *Finding Shortest Paths between Graph Colourings*, arXiv:1403.6347v1 (public preprint dated 2014-03-25), https://arxiv.org/abs/1403.6347.
3. *Determining a graph from its reconfiguration graph*, arXiv:2504.19783v1 (public preprint dated 2025-04-28), https://arxiv.org/abs/2504.19783. Later related methodological context only.
