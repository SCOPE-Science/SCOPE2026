# The five-robust clique complexes of all five-square sequences are wedges of seven-spheres

## Finding
For every finite simple graph \(G\) obtainable from one four-cycle by exactly four successive edge or corner gluings of four-cycles (as in Definition 8 of Filakovský), the five-robust clique complex satisfies
\[
\mathsf{Cliq}_5(G)\simeq \bigvee^{b(G)} S^7,\qquad 0\le b(G)\le5.
\]
There are exactly 179 graph-isomorphism types in this class. The numbers of types with \(b(G)=0,1,2,3,4,5\), respectively, are \(67,27,34,16,2,33\). The zero-sphere wedge means a contractible space. In particular, all reduced integral homology vanishes outside degree seven, and the degree-seven group is free of rank \(b(G)\).

## Assumptions and scope
Graphs are finite, simple and unlabelled up to isomorphism. A square sequence starts with \(C_4\). At each step a fresh \(C_4\) meets the existing graph along precisely one edge (two new vertices) or along a path of two edges (one new vertex). These are the two constructions from Definition 8 in the cited paper. The clique complex \(\mathsf{Cliq}_5(G)\) has as its faces all vertex subsets \(W\subseteq V(G)\) for which the induced graph \(G[W]\) has independence number less than five. The statement concerns exactly five squares, not arbitrary sequence length.

## Proof
The complete enumeration and all simplicial-certificate checks are specified by the standalone `verify.py`, with `networkx==3.6.1` as its declared sole external dependency. The following explains why the executable checks constitute an exhaustive finite proof.

**Exhaustive graph generation.** The starting list contains a single \(C_4\). From each representative, the algorithm adds a new square in every possible way: (i) append a length-three path between endpoints of any existing edge, using two new vertices; or (ii) add one new vertex adjacent to both endpoints of any length-two path. These exhaust the edge and corner attachments, respectively. Each generated graph is assigned a Weisfeiler–Lehman hash only for bucketing, and every possible collision is resolved with an exact graph-isomorphism test; isomorphic graphs have equal hash. Induction on the number of squares proves coverage and absence of duplicate isomorphism classes. The successive counts are exactly \(1,2,7,29,179\) for one through five squares.

**Complete face enumeration.** Every graph in the family is bipartite. Any subset of at least nine vertices contains at least five in one bipartition class and so fails the independence-number condition. Thus faces have at most eight vertices. The verifier enumerates every subset up to size eight and tests for containment of any independent five-set, giving the complete face poset rather than a sample.

**Discrete Morse certificate.** On the augmented poset, for pivot vertices in the fixed labelling order, match every currently unmatched face not containing the pivot to its pivot-adjoined face whenever both remain. Remove each such pair before advancing to the next pivot. The augmented empty-face pair is discarded, leaving its singleton as a critical zero-cell. For *each* of the 179 cases, the verifier exhaustively constructs the entire Hasse graph, reverses the matching edges, and confirms by a full topological sort that there is no directed cycle. It also checks that the remaining critical faces consist of precisely one zero-cell and \(b(G)\) seven-cells, with **no other critical dimensions**. Across all cases, it processes 255,727 nonempty faces and 127,616 matching pairs; the critical seven-cell distribution is exactly that in the Finding. The alternating face-count Euler characteristic is checked independently against every computed \(b(G)\).

The finite acyclic matchings are valid discrete Morse matchings. By the discrete Morse theorem, each complex is homotopy equivalent to a CW complex with a single zero-cell and \(b(G)\) seven-cells, and no cells in any other positive dimension. Every seven-cell attaches to the point, giving the asserted wedge of seven-spheres integrally. The program has finite loops bounded by the explicit five-square graph and face enumerations, so no extrapolation from sampled parameters occurs.

## Verification
Install the dependency from `requirements.txt` and run `python verify.py` in the same directory. The expected output is in `verifier_output.txt`. The verifier checks all 179 nonisomorphic cases, every face and every Hasse cover incidence, acyclicity of every constructed matching, critical dimensions and counts, and the independent Euler identity. The recorded run passes all assertions with isomorphism-type counts \((1,2,7,29,179)\), and critical seven-cell multiplicity frequencies \((67,27,34,16,2,33)\).

## Relationship to prior work
Filakovský (arXiv:2602.11365, initially public February 11, 2026) defines square-sequence graphs, establishes analogous wedge decompositions for \(k=2,3\) and for arbitrary \(k\) under edge-only gluing, and explicitly conjectures the wedge property with corner gluings for all \(k\). The present finite result gives all five-square graph types at the first considered \(k=5\) threshold, including mixed edge and corner gluings, with exact counts; it does not prove the unbounded conjecture. Earlier reported four-robust finite classifications, including a six-square census, concern a different threshold and do not determine the five-robust complexes. Searches did not identify this exact classification, but absence from search results is not a guarantee of priority.

## Limitations
The argument uses an exhaustive, independently replayable finite certificate, not a uniform theorem for arbitrary square-sequence length. The available comparison to the published six-square four-robust census was through its recorded scientific summary, not its full text; that bibliographic limitation and the possibility of unindexed equivalent work remain. No independent mathematical audit has been performed.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first version February 11, 2026, https://arxiv.org/html/2602.11365.
2. *Six-square census for four-robust clique complexes with unrestricted square gluing*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-six-square-census-for-four-robust-clique-complexes-with-unrestri--b12691741e94 (record summary inspected; full text not accessible).
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete Morse theorem).
