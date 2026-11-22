# Sharp seven-point failure of two-arity reconstruction in the homogeneous triangle-free graph

## Finding
Let \(\mathcal H\) denote the countable homogeneous universal triangle-free graph. For every finite, *pointwise-named*, induced parameter graph \(G\subset\mathcal H\), let \(t_r(G)\) be the number of complete types of ordered \(r\)-tuples of distinct new vertices, all outside \(G\), over those parameters. Consider the numerical signature \((|G|,t_1(G),t_2(G))\).

**Sharp reconstruction threshold.** For every pair of nonisomorphic triangle-free graphs on the same number of vertices at most six, the signatures differ. At seven vertices exactly **one unordered pair of nonisomorphic graphs** has the same signature, up to graph isomorphism. These are \(C_6\sqcup K_1\) and the seven-vertex tree \(S(1,2,3)\), the subdivision of a three-leaf star with three arms of respective edge lengths \(1,2,3\). Both satisfy
\[
(t_1,t_2,t_3)=(36,1893,145767)\quad\text{and}\quad (36,1893,145689),
\]
respectively. Thus the first two numerical arities collide, but the third distinguishes the graphs, by exactly \(78\) types.

**Persistent separation.** For each integer \(k\geq0\), the nonisomorphic graphs \(C_6\sqcup K_{k+1}^{\mathrm{ind}}\) and \(S(1,2,3)\sqcup K_k^{\mathrm{ind}}\), where \(K_j^{\mathrm{ind}}\) denotes an edgeless graph on \(j\) vertices, have the same number \(7+k\) of parameters, the same \(t_1\) and \(t_2\), and
\[
 t_1=36\,2^k,\qquad t_2=1296\,4^k+597\,3^k,
 \qquad t_3(C_6\sqcup K_{k+1}^{\mathrm{ind}})-t_3(S(1,2,3)\sqcup K_k^{\mathrm{ind}})=78\,5^k.
\]
The formulae for low-arity types used in the proof are known specializations of general Henson type-counting identities; the new classification concerns the *unique sharp first collision and its indefinitely persistent higher-arity separation*, not the general counting identity itself.

## Assumptions and scope
All graphs are finite, simple and triangle-free; the countable homogeneous limit is used only to interpret types. Parameters are individually named. New coordinates are injective and unequal to parameters; algebraic/equality types are excluded. The signature comparison is among graphs with equal vertex count. The claim is a census through seven vertices plus an explicit infinite construction, not a classification of every larger collision.

Put \(\mathcal I(G)=\{S\subseteq V(G):G[S]\text{ has no edge}\}\), \(I(G)=|\mathcal I(G)|\), and
\[
 C(G)=|\{(S,T)\in\mathcal I(G)^2:S\cap T=\varnothing\}|,\qquad
 J(G)=\sum_{S\in\mathcal I(G)}I(G-S)^2,
\]
where \(G-S\) is the induced subgraph on the complementary vertex set. These quantities count finite diagrams, not random vertices of the infinite graph.

## Proof
**1. Exact arity reduction.** The homogeneous extension property identifies each complete injective tuple type with precisely one triangle-free labelled extension graph. A new vertex's old neighborhood must be an independent subset of \(G\), and every such subset is realized; hence \(t_1(G)=I(G)\). Two new vertices may be nonadjacent (\(I(G)^2\) choices of old neighborhoods) or adjacent (two independent old neighborhoods with empty intersection, \(C(G)\) choices). Consequently
\[
 t_2(G)=I(G)^2+C(G).
\]
For three distinct new vertices, the induced graph on them must be either empty, one edge (three labelled positions), or a two-edge path (three labelled positions). The respective numbers of admissible old attachments are \(I(G)^3\), \(I(G)C(G)\), and \(J(G)\). In the path case, the two leaf-neighborhoods are arbitrary independent sets of \(G-S\) after fixing the middle neighborhood \(S\); they may overlap each other. Therefore
\[
 t_3(G)=I(G)^3+3I(G)C(G)+3J(G).
\]
These identities are special cases of the general Cartesian-product counting identity described in the cited 2026 result; no priority is claimed for the identities alone.

**2. Exhaustive first-collision classification.** The supplied pure-standard-library program `verify.py` constructs, by induction, a complete list of triangle-free graphs up to isomorphism on every vertex count \(0\leq n\leq7\). From every \(n\)-vertex graph it adjoins one new vertex with each possible independent old neighborhood. Conversely every triangle-free graph on \(n+1\) vertices arises in this way after deleting one vertex. Canonicalization sorts vertex degrees and takes the least upper-triangle adjacency encoding among all relabellings *within equal-degree groups*. This is exact: an isomorphism must preserve each degree group, and equality of canonical adjacency encodings supplies an isomorphism. Therefore neither labelled graphs nor isomorphism classes are omitted or conflated. The resulting numbers of classes for \(n=0,1,\ldots,7\) are \(1,1,2,3,7,14,38,107\).

For each representative the program enumerates all independent bitmasks, forms \((I,C)\), and groups equal signatures. There are no collisions through six vertices, and precisely one two-element class at seven vertices, with \((I,C)=(36,597)\). The degree sequences and edge sets of its representatives identify \(C_6\sqcup K_1\) and \(S(1,2,3)\). This exhaustive finite argument proves the cutoff; an arbitrary partial sample of small graphs would not suffice.

**3. Exact witness values without reliance on the census.** The two graphs each have \(I=36\). Indeed \(I(C_6)=18\), the additional isolated vertex doubles it, while the spider has \(2\cdot3\cdot5+1\cdot2\cdot3=36\) independent sets by conditioning on the central vertex. For \(C\), use three states at each old vertex: neither, first new point, second new point. Adjacent old vertices cannot both occupy either of the two nonzero states. The transfer matrix is
\[
 M=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]
Then \(C(C_6\sqcup K_1)=3\operatorname{tr}(M^6)=3\cdot199=597\), whereas \(C(S(1,2,3))=\sum_{s=0}^2(M\mathbf1)_s(M^2\mathbf1)_s(M^3\mathbf1)_s=357+120+120=597\).

For \(J\), use the five states \(\varnothing,\{1\},\{2\},\{3\},\{1,3\}\), the independent sets of the three-new-vertex path, and the symmetric compatibility matrix \(Q\) with \(Q_{UV}=1\) exactly when \(U\cap V=\varnothing\). Direct integer matrix multiplication gives
\[
 J(C_6\sqcup K_1)=5\operatorname{tr}(Q^6)=5\cdot2309=11545,\qquad
 J(S(1,2,3))=\sum_U(Q\mathbf1)_U(Q^2\mathbf1)_U(Q^3\mathbf1)_U=11519.
\]
The preceding three-point identity now gives the displayed values \(145767\) and \(145689\).

**4. Infinite propagation.** Adjoining an isolated named parameter doubles \(I\), triples \(C\), and multiplies \(J\) by five. These are the numbers of its admissible adjacency choices in the empty, one-edge, and path internal new-vertex diagrams. Thus equality of \(I,C\) persists under any number of isolated parameters, while the initial \(J\) difference of \(26\) becomes \(26\cdot5^k\), yielding the difference \(78\cdot5^k\) in \(t_3\). The graphs remain nonisomorphic because their nontrivial connected components are respectively a cycle and a tree.

## Verification
Run `python3 verify.py` in a Python 3 environment. It uses only the Python standard library and checks complete canonical generation and exact collision multiplicities through seven vertices, as well as independent-mask values and the third-arity witness separation. The captured output is included in `verification_output.txt`; the terminal line is `EXHAUSTIVE_FRAISSE_COLLISION_OK`. Separately, an independently organized enumeration using NetworkX's 1,253-graph atlas through seven vertices was used to cross-check the 107 triangle-free seven-vertex classes and the single collision. The symbolic proof of the arity formula and the isolate-propagation identity are not inferred from the finite output.

## Relationship to prior work
Henson's original paper proves the homogeneous universal \(K_3\)-free graph and the corresponding extension property (1971, §2). Conant's first arXiv version (2014) develops types and graph-theoretic consistency in Henson structures. Earlier published work identifies one-point Henson type counts with independence polynomials, and a 2026 result proves the full Cartesian-product identity \(t_r(G)=\sum_{F\text{ labelled triangle-free on }[r]}I(G\square F)\), together with counting complexity. Those results supply the counting framework; neither inspected result states a first collision classification for \((|G|,t_1,t_2)\), the unique seven-point pair, or its third-arity separation family. General evaluability does not itself supply the exhaustive isomorphism census or the exceptional pair.

The graph-invariant translations are \(I(G)\) (Merrifield–Simmons index) and \(C(G)\) (a three-state graph-homomorphism partition function). Searches under these equivalent formulations also did not identify the sharp seven-vertex collision. An unindexed historical table or a differently phrased graph-invariant result could still supersede the priority claim.

## Limitations
This is an exact classification only up to the first collision size of seven; it gives one persistent family for larger sizes, not all larger collision classes. The answer depends on the *numbers* of injective tuple types, not their labelled formulas, graph degree refinement, or automorphism-group action. The finite cutoff relies on the complete canonical enumeration program, independently testable but not an externally certified formal proof. The historical novelty assessment is provisional, and independent mathematical audit has not been performed.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83, DOI: 10.2140/pjm.1971.38.69, https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf .
2. G. Conant, “Forking and dividing in Henson graphs,” first public arXiv version 2014-01-08, arXiv:1401.1570, https://arxiv.org/abs/1401.1570 .
3. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” published 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650 .
4. “Higher-arity Henson type enumeration and exact-counting hardness,” published 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6 .
5. L. Song, W. Staton and B. Wei, “Independence polynomials of k-tree related graphs,” *Discrete Applied Mathematics* 158 (2010), 943–950, DOI: 10.1016/j.dam.2010.01.002 (background on independence-set graph invariants).
