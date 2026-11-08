# The five-by-six toroidal hard-square independence complex is a five-sphere

## Finding
The ordinary simplicial independence complex of the 30-vertex, fully periodic five-by-six square grid has the exact integral homotopy type
\[
\boxed{\operatorname{Ind}(C_5\square C_6)\simeq S^5.}
\]
In particular, \(\widetilde H_5(\operatorname{Ind}(C_5\square C_6);\mathbb Z)\cong\mathbb Z\) and all other reduced integral homology groups vanish. This is an integral **homotopy** classification, rather than just a Betti-number or Euler-characteristic calculation.

## Assumptions and scope
The graph is the Cartesian product \(C_5\square C_6\), with vertex set \(V=(\mathbb Z/5\mathbb Z)\times(\mathbb Z/6\mathbb Z)\). Vertices \((r,c)\), \((r',c')\) are adjacent if and only if \(r=r'\) and \(c'=c\pm1\pmod6\), or \(c=c'\) and \(r'=r\pm1\pmod5\). **Both** directions are periodic; no diagonals are present. Every vertex has four neighbors. The simplices of \(\operatorname{Ind}(G)\) are precisely the vertex subsets containing no adjacent pair; the empty simplex is included in the face poset. Under the Chinese remainder identification of the vertex set with \(\mathbb Z/30\mathbb Z\), the graph is also the circulant on 30 vertices with undirected jump lengths five and six. No claim is made about other torus dimensions or general graph products.

## Proof
The following explicit, finite discrete-Morse construction proves the statement. Code vertices as \(6r+c\) and a face as a 30-bit mask. Starting with the empty face, process the vertices in increasing order; for each current independent face \(\sigma\), adjoin \(v\) exactly when no neighbor of \(v\) is in \(\sigma\). Each independent face appears exactly once, by its unique sequence of processed vertex choices. The resulting face set contains exactly **199,821** faces including empty; its face numbers in dimensions zero through eleven are
\[
(30,375,2560,10545,27450,46230,51000,37080,17790,5580,1080,100).
\]
A logically distinct enumeration counts valid cyclic six-bit row patterns with no adjacent occupied sites, and retains tuples of five rows if adjacent rows have disjoint occupied columns, including the last-to-first interface. It reproduces the first enumeration **in every cardinality**.

Form a matching on the augmented face poset as follows. At each pivot \(v=0,1,\ldots,29\) in order, pair every currently unmatched face \(\sigma\) without \(v\) with \(\sigma\cup\{v\}\) whenever this upper face is also unmatched, then remove both. Each pair is a genuine Hasse covering relation; disjointness is ensured by immediate removal. The empty face pairs with the vertex-zero singleton. The algorithm produces **99,910** pairs and leaves **one** unmatched simplex: binary mask `4342820`, containing six vertices, hence of dimension five.

For acyclicity, the verifier traverses **every** cover relation of the augmented face poset, precisely **1,347,900** incidences. Orient each unmatched incidence downward and each matching incidence upward. Kahn's topological-sort algorithm visits all **199,821** faces; therefore the complete directed Hasse graph is acyclic. This is exhaustive and finite, not a heuristic or a random sample. The complete deterministic algorithms and exact output are embedded in `verify.py` and `verification_output.txt`.

By augmented discrete Morse theory, matching the empty face and having exactly one critical nonempty face of dimension five yields a pointed CW model with one implicit zero-cell and one five-cell, with no cells in intermediate positive dimensions. Its attaching map is necessarily constant, and the CW model is \(S^5\). Thus the asserted integral homotopy equivalence follows. Independently, the alternating face sum gives reduced Euler characteristic \(-1\), as required for a five-sphere.

## Verification
Run `python3 verify.py` from a directory containing the embedded source. It uses only the Python standard library. The program checks four-neighbor undirected periodic adjacency, two independent enumeration methods and their degree-by-degree agreement, matching-pair disjointness and completeness, exact unmatched-cell dimension, all directed face-incidence relations, exhaustive topological sorting, and reduced Euler characteristic. Successful output agrees byte-for-byte with the embedded `verification_output.txt` and finishes with `ALL_CHECKS_PASS`. The software is the explicit finite proof certificate for this one graph, not a claim of an infinite classification.

## Relationship to prior work
Jonsson's 2006 hard-square theorem studies **exactly this fully toroidal Cartesian-cycle product**, proving that its reduced Euler characteristic is \(-1\) because the two cycle lengths are coprime; this alone cannot imply the homotopy type. The paper explicitly explains that its tiling method supplies little homological information. Bousquet-Mélou, Linusson and Nevo classify the homotopy type of several **open and cylindrical** square grids, rather than fully periodic products; Matsushita and Wakatsuki likewise study path-by-path grid graphs, citing Jonsson for the toric Euler invariant.

Adams and coauthors (2025) already establish that \(\operatorname{VR}(T_{5,5};3)\simeq\bigvee^9 S^4\). This is equivalent to the **different** ordinary independence complex \(\operatorname{Ind}(C_5\square C_5)\): the forbidden distance-four pairs in the five-by-five torus grid have displacement vectors \(\pm(2,2),\pm(2,-2)\), generating a graph isomorphic to \(C_5\square C_5\). That known equal-width homotopy calculation is not claimed as new here, and it does not imply the five-by-six result. The latter remains a natural next-width case.

Jonsson's 2010 publication concerning cross-cycles on grid independence complexes is materially close, but only its abstract was accessible; it reports a range of possible nonzero homology degrees for lattice quotients, not this exact five-by-six homotopy theorem. Neither full-text priority against that work nor absolute publication priority is asserted.

## Limitations
Only the specified fully periodic five-by-six Cartesian grid is classified. No equivariant homotopy, general toric-width formula, integral representation decomposition or persistence map is established. Its isomorphism with a 30-vertex circulant does not extend the result to other circulants. Full text of the relevant 2010 cross-cycle article could not be inspected, leaving unresolved publication-priority risk; independent assessment has not been performed.

## References
1. J. Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, Electronic Journal of Combinatorics 13 (2006), R67, publicly released 2006-08-07, DOI: 10.37236/1093. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r67/pdf/
2. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890 (2007); Journal of Algebraic Combinatorics 27 (2008), 423–450. https://arxiv.org/abs/math/0701890
3. T. Matsushita and S. Wakatsuki, *Independence complexes of (n × 4) and (n × 5)-grid graphs*, arXiv:2203.16391 (2022). https://arxiv.org/abs/2203.16391
4. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v2 (2025), §7 (known equal-width, different-graph result). https://arxiv.org/html/2502.07134v2
5. J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grids*, Discrete & Computational Geometry 43 (2010), 927–950, DOI: 10.1007/s00454-009-9224-9 (abstract inspected; full paper inaccessible).
