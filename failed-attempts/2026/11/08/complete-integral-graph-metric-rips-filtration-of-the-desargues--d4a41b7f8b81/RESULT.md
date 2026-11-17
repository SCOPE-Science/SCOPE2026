# Complete integral graph-metric Rips filtration of the Desargues graph

## Finding

Let \(D\) be the twenty-vertex Desargues graph, equivalently the bipartite Kneser graph \(H(5,2)\), and give its vertices unit-edge shortest-path distance. The full **inclusive** Vietoris–Rips filtration \(K_r=\operatorname{VR}_{\le r}(D)\), for every real \(r\ge0\), has homotopy types

\[
K_r\simeq
\begin{cases}
\bigvee^{19}S^0,&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
\bigvee^{19}S^2,&2\le r<3,\\
S^3,&3\le r<4,\\
S^9,&4\le r<5,\\
*,&r\ge5.
\end{cases}
\]

Consequently, the **entire reduced integral barcode** consists of nineteen degree-zero intervals \([0,1)\), eleven degree-one intervals \([1,2)\), nineteen degree-two intervals \([2,3)\), one degree-three interval \([3,4)\), and one degree-nine interval \([4,5)\). There are no other nonzero reduced intervals. At every integer threshold \(r\), the integral homology is free.

## Assumptions and scope

Take \(U=\{0,1,2,3,4\}\). There are ten vertices indexed by the two-subsets \(A\subset U\) and ten indexed by the three-subsets \(B\subset U\). The edge \(A-B\) is present exactly when \(A\subset B\). In the verifier, two-subsets appear in lexicographic order as vertices \(0,\dots,9\), followed by three-subsets as vertices \(10,\dots,19\). This determines the twenty-vertex Desargues/Levi graph \(H(5,2)\), not the ten-vertex graph sometimes also called Desargues. Its graph is cubic, connected and bipartite with thirty edges and diameter five.

A finite nonempty subset \(\sigma\) is a face of \(K_r\) iff \(d_D(x,y)\le r\) for every \(x,y\in\sigma\). All distances are integers. The filtration stages at integer thresholds therefore determine every real threshold. This is an integral homotopy and ordinary persistent-homology result; no equivariant or Euclidean-metric assertion is made.

## Proof

**Step 1 (distance construction and all faces).** Run breadth-first search from each of the twenty labeled vertices, forming the threshold graph \(D^r\) for each \(r\in\{1,2,3,4\}\); its edges are pairs at graph distance at most \(r\). A face of \(K_r\) is exactly a clique of \(D^r\). The verifier enumerates *all* cliques by adding vertices in increasing label order and independently by generating the faces of all maximal cliques using a separate Bron–Kerbosch recursion. The two sets agree exactly for each threshold. Their dimension-indexed face vectors (beginning at dimension zero) are

\[
\begin{array}{c|l|r}
r& (f_0,f_1,\ldots)&\text{nonempty faces}\\\hline
1&(20,30)&50\\
2&(20,90,120,30)&260\\
3&(20,150,540,1000,960,450,80)&3200\\
4&(20,180,960,3360,8064,13440,15360,11520,5120,1024)&59048.
\end{array}
\]

**Step 2 (finite acyclic discrete-Morse certificate).** The standalone verifier constructs the full face poset, excluding the empty face. For each integer-labeled vertex \(v=0,\ldots,19\) in increasing order, it visits faces in increasing cardinality and then increasing vertex-bitmask. Any so-far unused face \(\sigma\) not containing \(v\) is paired with \(\sigma\cup\{v\}\) if the latter is a face and is also unused. Both are thereafter marked used. This is a codimension-one matching, with no face repeated. For each Hasse cover \(\sigma\subset\tau\) with \(\lvert\tau\rvert=\lvert\sigma\rvert+1\), orient the edge from lower to upper except that matched covers are reversed. The program enumerates every such cover and runs a full topological sort; this orientation and its global reversal are both acyclic. This is precisely an acyclic matching in discrete-Morse theory.

At thresholds \(1,2,3,4\), the algorithm finds respectively \(19,120,1599,29523\) matched pairs, and \(60,660,13980,393640\) Hasse covers. The only unmatched (critical) cells, recorded as \((\text{dimension},\text{multiplicity})\), are respectively

\[
\{(0,1),(1,11)\},\quad
\{(0,1),(2,19)\},\quad
\{(0,1),(3,1)\},\quad
\{(0,1),(9,1)\}.
\]

The topological sort processes exactly \(50,260,3200,59048\) vertices of the respective directed Hasse graphs, showing that the matchings are globally acyclic, not just locally valid. By the discrete-Morse CW theorem, each \(K_r\) has the homotopy type of a CW complex containing exactly the critical cells. There is a single zero-cell and no critical cells in the intervening dimensions, so every positive-dimensional cell attaches to the point and the CW model is exactly the displayed wedge of spheres. No inference from numerical Betti numbers to integral homotopy is needed.

**Step 3 (endpoints and structural cross-check).** For \(0\le r<1\), the complex is the discrete space of twenty vertices. At \(r=1\), it is the original connected, triangle-free graph with cycle rank \(30-20+1=11\). The graph diameter is five, hence \(K_r\) is a full simplex for \(r\ge5\). More specifically, each vertex has a **unique** vertex at distance five. These ten unordered antipodal pairs are the only missing edges of \(D^4\), so \(K_4\) is independently the join of ten two-point complexes, the boundary of the ten-dimensional cross-polytope: \(K_4\cong(S^0)^{*10}\cong S^9\). This geometrically corroborates the Morse computation at scale four.

**Step 4 (persistence maps).** At each nontrivial integer stage, reduced homology is nonzero in only the degree displayed. The degrees at consecutive stages are distinct. Therefore every inclusion-induced map in any fixed positive degree, and in reduced degree zero, is zero at the next threshold. The groups are all free, so the stated intervals describe integral persistence as a direct sum of free interval modules, not merely field-level ranks. There are no zero-length intervals in this statement; only groups born and nonzero across half-open real scale ranges are counted.

## Verification

The standalone file `verify.py` runs using Python 3 and only its standard library. It independently enumerates every flag simplex two ways, verifies every matching pair is a real codimension-one face relation, counts every Hasse cover, topologically sorts the fully reoriented Hasse diagram, and checks all critical cells, face vectors, Euler characteristics, metric diameter and antipodes. Run `python verify.py` in the same directory. The bundled `verification_output.txt` is the actual stdout from the packaged code and ends `ALL_CHECKS_PASS`. Every finite certificate is reconstructed from the twenty-vertex incidence definition, without external data or a stale saved computation. The topological deduction uses the standard discrete-Morse CW theorem.

## Relationship to prior work

Adamaszek, *Clique complexes and graph powers* (first public 2011-04-03), defines the graph-metric Rips filtration and develops graph-power homotopy results. Its full accessible text was compared, particularly Sections 2, 3, 5 and 6: the girth criterion for powers up to a fixed scale requires girth at least three times that scale plus one, while the Desargues graph has girth six; the paper's complete classifications concern powers of cycles and line/subdivision constructions, not \(H(5,2)\). Kawamura's 2011 bipartite-relation paper concerns the square of a bipartite graph; its abstract was checked, but the complete paper could not be verified, leaving some uncertainty about any scale-two implication. Neither accessible statement supplies this full five-stage integral filtration.

The relevant published calculation of the Desargues **Čech** nerve at scale three studies intersections of metric balls centered at the graph vertices and obtains \(\bigvee^{49}S^2\). That construction is not the pairwise-distance Rips clique complex \(K_3\simeq S^3\), as evidenced by their different complete face vectors and homology. Other inspected published-finding corpus results calculate Rips filtrations of the truncated octahedron and a scale-three complex of the Tutte–Coxeter graph; these are different graphs. Own earlier accessible findings were compared by object, metric, threshold and implication; none reported this Desargues Rips filtration. Search and deduplication cannot establish absolute priority, and unindexed equivalent results remain possible.

## Limitations

The theorem is specific to the intrinsic unit-edge graph metric on twenty vertices, not the geometric realization's continuous metric or any Euclidean embedding. The proof relies on an independently reproducible exhaustive combinatorial certificate; no uniform classification for other bipartite Kneser graphs, equivariant description or functorial homotopy decomposition is claimed. The Kawamura full paper remained inaccessible in this check and publication priority remains provisional. Independent mathematical audit has not been performed.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (public 2011-04-03), especially Sections 1–3, 5–6, https://arxiv.org/abs/1104.0433.
2. K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, Contributions to Discrete Mathematics 6(2) (2011), https://doi.org/10.55016/ojs/cdm.v6i2.62059 (abstract consulted).
3. *Scale-three Čech nerve of the Desargues graph is a wedge of 49 two-spheres*, published-finding corpus public mathematical record (2026), identifier `2026/10/11/SCOPE-scale-three-ech-nerve-of-the-desargues-graph-is-a-wedge-of-49-tw--eac77c714390` (full `RESULT.md` inspected).
4. *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph*, published-finding corpus public mathematical record (2026), identifier `2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8` (full `RESULT.md` inspected).
5. *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, published-finding corpus public mathematical record (2026), identifier `2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54` (full `RESULT.md` inspected).
