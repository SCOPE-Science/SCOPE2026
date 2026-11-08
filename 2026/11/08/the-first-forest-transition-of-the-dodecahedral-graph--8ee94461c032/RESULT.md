# The first forest transition of the dodecahedral graph

## Finding
For the dodecahedral graph \(D=\operatorname{GP}(10,2)\), the first two forest-filtration stages and their quotient satisfy
\[
\mathcal F_0(D)\simeq\bigvee^4 S^5,\qquad
\mathcal F_1(D)\simeq S^6,\qquad
\mathcal F_1(D)/\mathcal F_0(D)\simeq\bigvee^5 S^6.
\]
The inclusion \(\mathcal F_0(D)\hookrightarrow\mathcal F_1(D)\) is null-homotopic. The stage-zero homotopy type is previously available and is independently recomputed here; the new assertion is the complete first positive stage and the resulting transition.

## Assumptions and scope
Write the vertex set as \(\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\), with undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), for every index modulo ten. This is the simple, connected cubic dodecahedral graph, with twenty vertices and thirty edges. For each nonnegative integer \(d\), define \(\mathcal F_d(D)\) as the abstract simplicial complex of vertex subsets whose induced graph is a forest of maximum degree at most \(d\). The empty set is included. In particular, the first stage is the two-independence or dissociation complex: each component has one or two vertices. Its faces are exactly the subsets containing no three-vertex path, equivalently no vertex with two selected neighbors. All homotopy equivalences concern ordinary, nonequivariant CW homotopy types over the integers.

## Proof
**Exact face census.** Enumerate all \(2^{20}=1{,}048{,}576\) subsets. The degree-at-most-one predicate, and independently the exclusion of the sixty centered three-vertex paths (three possible unordered neighbor-pairs at each of twenty degree-three vertices), produce the same 63,143 faces, including the empty face. In dimensions \(-1\) through 11 the face counts are
\[
(1,20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5).
\]
The maximal faces occur in dimensions 7, 8, 9 and 11, in counts 25, 60, 420 and 5 respectively. Hence the complex is nonpure and has simplicial dimension 11.

**Finite acyclic Morse matching.** In vertex order \(u_0,\ldots,u_9,v_0,\ldots,v_9\), successively match every two still-unmatched faces differing by addition of the current vertex, whenever both faces are present. This matches 31,566 disjoint pairs, including the empty face. It leaves exactly one critical five-cell, six critical six-cells and four critical seven-cells. Reverse vertex order gives another matching with two critical five-cells, six critical six-cells, and three critical seven-cells. In each case, the oriented Hasse diagram (unmatched incidences downward and matched incidences upward) is explicitly verified acyclic by a full topological sort through all 63,143 faces and all 410,520 covering incidences. Forman's discrete Morse theorem yields a CW complex with one base vertex and only the displayed positive-dimensional cells.

**Integral attaching degrees.** Orient each face by increasing vertex order. For a critical cell \(c\), project its simplicial boundary to critical cells by eliminating matched pairs. If a lower matched face \(q\) is paired with the upper face \(w\), the relation \(\partial w=\varepsilon q+\sum_{p\ne q}[w:p]p\), with \(\varepsilon=[w:q]\in\{\pm1\}\), gives
\[
P(q)=-\varepsilon^{-1}\sum_{p\ne q}[w:p]P(p).
\]
A critical face projects to itself, and an upper matched face projects to zero. Acyclicity makes these substitutions terminate and gives the exact integral cellular Morse differential. In ascending order, with critical masks sorted numerically within each dimension, the only nonzero differentials are
\[
\partial_6=A=\begin{pmatrix}0&0&-1&0&1&0\end{pmatrix},\quad
\partial_7=B=\begin{pmatrix}
1&1&0&0\\
0&0&0&-1\\
0&1&0&0\\
0&-1&1&0\\
0&1&0&0\\
0&0&-1&0
\end{pmatrix}.
\]
Direct multiplication yields \(AB=0\). Matrix \(A\) has an entry equal to \(-1\), and the determinant of the top four-by-four submatrix of \(B\) equals \(-1\). Thus both maps have primitive images of ranks 1 and 4, respectively, and \(\operatorname{im}B\subseteq\ker A\). The resulting reduced integral homology is \(\widetilde H_6\cong\mathbb Z\), with all others zero and no torsion. The opposite-order reduction independently gives ranks 2 and 3 with unit maximal minors, and the same homology.

**Homotopy, not just homology.** The Morse complex has one 5-cell, six 6-cells and four 7-cells over a point. Attaching 6-cells to a wedge of 5-spheres is classified by the integer degree matrix \(A\): since an entry is a unit, an integral cellular basis change cancels one 5/6 pair, leaving a wedge of five 6-spheres. Attaching the four 7-cells is then classified by the integral degree map into \(\pi_6(\bigvee^5 S^6)\cong\mathbb Z^5\). The primitive rank-four image of \(B\) in \(\ker A\) permits four 6/7 cancellations after unimodular basis changes. One 6-sphere remains. This proves \(\mathcal F_1(D)\simeq S^6\), not just a homology equivalence.

**Transition.** Independently enumerating the independence complex \(\mathcal F_0(D)\) gives 5,828 faces. Ascending element matching leaves four critical five-cells and no other positive-dimensional critical cells, proving \(\mathcal F_0(D)\simeq\bigvee^4 S^5\). Since \(\pi_5(S^6)=0\), every map from this wedge to the first forest stage is null-homotopic, in particular the simplicial inclusion. The simplicial inclusion is a cofibration, and the cofiber of a null map splits up to homotopy as \(\mathcal F_1(D)\vee\Sigma\mathcal F_0(D)\simeq\bigvee^5 S^6\).

## Verification
Run `python3 dodecahedral_f1_verifier.py` with Python 3.10 or later; the program uses only the standard library. It independently compares every possible vertex subset with two face tests, constructs and topologically checks both Morse matchings, recomputes the signed integral matrices by terminating gradient-path elimination, verifies their unit minors and chain identity, and separately certifies the stage-zero Morse reduction. `VERIFIER_OUTPUT.txt` contains the exact recorded standard output. This is finite exhaustive computation, not an unproved extrapolation to a family.

## Relationship to prior work
Deshpande–Singh introduce and calculate higher-independence complexes for complete multipartite graphs, fully whiskered graphs, cycles, paths and perfect rooted trees. Carnero Bravo defines the forest filtration and calculates its stages for paths, cycles, double stars, cactus graphs, certain joins and products. Neither inspected set of formulas covers the dodecahedral graph or implies its first-stage homotopy type. The previously calculated ordinary dodecahedral independence complex coincides with our stage zero and is not the new theorem. The dodecahedral matching complex uses edges rather than vertex subsets and is a different object. See references below.

## Limitations
The theorem is a single exact finite graph calculation; it does not classify first forest stages for all generalized Petersen graphs, assert equivariant homotopy equivalence, or determine any higher forest stage. Two independently ordered matchings confirm the integral result, but independent external verification and an exhaustive search of unindexed literature have not been performed. A bibliographically equivalent calculation could exist outside the inspected sources.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (initial public posting 2020-01-15), especially Sections 2–5. https://arxiv.org/abs/2001.05448
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (initial public posting 2023-07-25), especially Sections 3–4. https://arxiv.org/abs/2307.13271
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. **134** (1998), 90–145. Used only for standard discrete-Morse correspondence.
