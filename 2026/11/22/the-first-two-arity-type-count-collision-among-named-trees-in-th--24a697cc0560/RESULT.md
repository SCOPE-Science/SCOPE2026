# The first two-arity type-count collision among named trees in the triangle-free homogeneous graph

## Finding
Let \(H_3\) be the countable homogeneous universal triangle-free graph, and let \(T\) range over finite *unlabelled trees* embedded as induced subgraphs, with every vertex individually named. Write \(t_r(T)\) for the number of complete types of ordered, mutually distinct \(r\)-tuples of new vertices outside the named set. Then the numerical signature \((|T|,t_1(T),t_2(T))\) determines every tree on at most nine vertices up to isomorphism. Among the 106 unlabelled trees on ten vertices, **exactly one unordered pair** has the same signature; that pair has
\[
(t_1,t_2)=(160,34249).
\]
The two trees also have identical degree multisets \((3,3,2,2,2,2,1,1,1,1)\), but distinct ternary counts:
\[
\{t_3(T),t_3(T')\}=\{9982531,9984403\}.
\]
Hence arity three distinguishes the entire unique first collision. This is a **finite sharp cutoff statement for trees**, not a claim of reconstruction of arbitrary graphs or all larger trees.

## Assumptions and scope
All graphs are finite, simple, undirected. The structure \(H_3\) is the Fraïssé limit of the finite triangle-free graphs. An ordered type includes the complete adjacency/nonadjacency pattern of distinct new vertices both among themselves and to every named vertex; repetitions and equality with parameters are excluded. The one-, two-, and three-type counts refer to the pointwise stabilizer, not to averages over random graph vertices.

For a finite graph \(G\), write \(\mathcal I(G)\) for its independent subsets (including the empty subset), and define
\[
 I(G)=|\mathcal I(G)|,\quad D(G)=|\{(A,B)\in\mathcal I(G)^2:A\cap B=\varnothing\}|,\quad
 J(G)=\sum_{S\in\mathcal I(G)}I(G-S)^2.
\]
The expression \(G-S\) means the subgraph induced by \(V(G)\setminus S\).

## Proof
**1. Translation from types to finite combinatorics.** Homogeneity and the finite-extension property identify each complete injective tuple type with one labelled triangle-free extension of its named induced base. For one new vertex, its parameter neighborhood is precisely an independent subset, so \(t_1(G)=I(G)\). For an ordered pair of new vertices, if they are nonadjacent their neighborhoods are arbitrary independent subsets (\(I(G)^2\) possibilities); if adjacent, their independent parameter neighborhoods must also be disjoint (\(D(G)\) possibilities). Therefore
\[
 t_2(G)=I(G)^2+D(G).
\]
For ordered triples, the internal graph must be one of the seven labelled triangle-free graphs: the edgeless graph (one pattern), a single edge (three patterns), or a two-edge path (three patterns). Their respective numbers of legal parameter-neighborhood assignments are \(I(G)^3\), \(I(G)D(G)\), and \(J(G)\), giving
\[
 t_3(G)=I(G)^3+3I(G)D(G)+3J(G).
\]
These universal identities are preexisting finite-extension consequences and are not claimed as new. They make the specific sharp tree-collision question an exact finite question about \((I,D)\).

**2. Exhaustive isomorphism-free tree construction.** Start with the one-vertex tree. Given one representative of each unlabelled \(n\)-vertex tree, attach a new labelled leaf at *each* old vertex and deduplicate the resulting \((n+1)\)-vertex trees by their exact canonical unlabelled code: for each possible root encode a rooted tree recursively as a matching pair of parentheses containing the lexicographically sorted codes of all children; take the lexicographically smallest code over all roots. Equality of this code is equivalent to unrooted tree isomorphism, because equal recursively defined rooted codes exhibit an isomorphism and any unrooted isomorphism carries root codes to root codes. Every tree of order at least two has a leaf, whose removal gives a smaller tree; hence the augmentation is exhaustive by induction. No sample or external tree table is used for completeness. It produces precisely \(1,1,1,2,3,6,11,23,47,106\) distinct trees for orders one through ten.

**3. Exact invariant census and witness.** For each constructed tree enumerate all \(2^n\) vertex masks and retain a mask if no edge has both endpoints selected. Count the retained masks to get \(I\) and count every ordered pair of retained masks with bitwise-disjoint intersection to get \(D\). The fully reproducible script `verify.py` evaluates these integers for every unlabelled tree through ten vertices. It finds no repeated \((I,D)\) within a fixed order \(n\le9\), and **exactly one doubleton fibre** within order ten. No other collisions occur at order ten. The full 106-row ten-vertex census, including canonical codes and edge lists, is provided in `census_10.csv`.

One representative \(T_A\) of the collision has vertices \(0,\ldots,9\) and edges
\[
 (01),(02),(03),(14),(15),(26),(47),(68),(79).
\]
The other \(T_B\) has edges
\[
 (01),(02),(03),(14),(15),(26),(37),(68),(89).
\]
Here the strings \((uv)\) denote an edge between vertices labelled \(u\) and \(v\), not ordered pairs of types. Both trees have two adjacent degree-three vertices. The respective multisets of other arm lengths at those hubs are \(\{\{1,3\},\{1,3\}\}\) and \(\{\{1,1\},\{2,4\}\}\). These are isomorphism invariants and are different, proving the two trees nonisomorphic independently of the canonical code.

Exact enumeration yields
\[
 I(T_A)=I(T_B)=160,\qquad D(T_A)=D(T_B)=8649.
\]
Consequently their unary and binary counts are \(160\) and \(160^2+8649=34249\).

**4. Ternary separation.** Directly summing \(I(G-S)^2\) over independent \(S\) yields \(J(T_A)=578337\) and \(J(T_B)=578961\). Thus
\[
 t_3(T_A)=160^3+3\cdot160\cdot8649+3\cdot578337=9982531,
\]
\[
 t_3(T_B)=160^3+3\cdot160\cdot8649+3\cdot578961=9984403.
\]
An *independent* three-neighborhood transfer recurrence, which does not use the independent-set pair enumeration, confirms the separate contributions \(I^3\), \(ID\) and \(J\). For an internal three-vertex pattern with edge set \(F\), let \(\sigma_v\) be the subset of new coordinates adjacent to an old vertex \(v\). At each old vertex, \(\sigma_v\) must be independent in \(F\), and across each old tree edge the two states must be disjoint. On a rooted tree, the number of state assignments for a root state \(\sigma\) is the product over child subtrees of the sums over states disjoint from \(\sigma\). This exact finite recurrence independently computes the six displayed witness contributions. Together, these facts prove the theorem.

## Verification
The standalone Python 3 standard-library script `verify.py` contains both the complete unlabelled-tree leaf-augmentation census and the independent three-state-set transfer recurrence. Run `python3 verify.py` in the folder containing the script. The recorded console output is embedded as `verification_output.txt`. It certifies the class counts \(1,1,1,2,3,6,11,23,47,106\), absence of collisions through nine vertices, a single ten-vertex collision pair, the exact \((I,D,J)\) values, the arity-three separation, and six independently recomputed internal-three-pattern counts. `census_10.csv` lists every ten-vertex isomorphism class and the two counted statistics. The finite census is exhaustive *because of the proved leaf-augmentation and canonical-code arguments*, not because a heuristic graph database happened to be consulted.

## Relationship to prior work
Henson (1971) establishes the homogeneous triangle-free structure; Conant (2014, Section 3) supplies the finite graph consistency/type framework. Existing published results give the general higher-arity independent-set-product identity, and an earlier exhaustive reconstruction result proves a **seven-point collision among arbitrary triangle-free graphs** (between a disconnected cycle with an isolate and a tree), with a ternary separation. That prior result supplies the general \(I,D,J\) identities and does **not** establish the sharp *tree-to-tree* threshold: its seven-point witness includes a nontree, and it does not classify eight-, nine- or ten-vertex tree fibres. The present claim is only the isomorphism-free complete classification up to order ten within trees.

Wagner and Wang (first published 2013, Theorem 3.1 and Corollary 4.1) show that various graph invariants, including the full independence polynomial, can fail jointly to reconstruct sufficiently large trees using pseudo-twin constructions. Their theorem does not imply the **first ten-point collision of the joint pair \((I,D)\)**, its uniqueness through ten points, or its specific ternary separation; the extra \(D\) invariant is a disjoint pair of independent neighborhoods, not the ordinary independence polynomial. Related tree-homomorphism recurrences provide counting methods but no such finite exhaustive classification. Exhaustive computation with precise isomorphism logic is essential to the new cutoff.

## Limitations
This is a finite exact classification through ten old vertices, not an infinite classification or a general separation theorem for all trees at higher order. The first collision within trees is later than the known first collision among arbitrary triangle-free graph bases; no new general identity for all graph types is claimed. The fact that three-types separate the unique minimal pair does not imply universal three-arity reconstruction. Independent mathematical audit has not been performed. Historical priority of the specific joint invariant/census remains a residual uncertainty pending further expert inspection.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* **38** (1971), 69–83. https://doi.org/10.2140/pjm.1971.38.69
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570v1, first public 2014-01-08, Section 3. https://arxiv.org/html/1401.1570v1
3. S. Wagner and H. Wang, “Indistinguishable Trees and Graphs,” *Graphs and Combinatorics* **30** (2014), 1593–1605; first published online 2013-09-04. https://doi.org/10.1007/s00373-013-1360-6 ; lawful author copy https://math.sun.ac.za/swagner/indistinguishable.pdf
4. “Higher-arity Henson type enumeration and exact-counting hardness,” publicly indexed result (2026-10-25), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6/RESULT.md
5. “Sharp seven-point failure of two-arity reconstruction in the homogeneous triangle-free graph,” previously published finite-collision result; general \(I,D,J\) identities and earlier all-graph cutoff. A prior finding, not a new contribution here.
