# Three balanced homology classes of shortest cycles in the Paley-13 flag torus

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\), with an edge \(\{u,v\}\) exactly when \(v-u\in Q=\{1,3,4,9,10,12\}\) modulo \(13\), and let \(K\) be its flag (clique) simplicial complex. The well-known \(K\) is a triangulated torus with face vector \((13,39,26)\). Give every edge length one and count simple unoriented cycles up to cyclic rotation and reversal. Then its mod-two homological one-systole is exactly **four edges**. There are exactly **39** simple cycles attaining this length and representing a nonzero element of \(H_1(K;\mathbb F_2)\cong \mathbb F_2^2\). Each of the **three nonzero homology classes** is represented by exactly **13** of the cycles.

The natural affine symmetry group \(G=\mathbb F_{13}\rtimes Q\) has order \(78\), and acts transitively on these \(39\) essential four-cycles. Its translation subgroup has exactly three orbits of size \(13\), one for each nonzero mod-two class. There are precisely \(78\) distinct unoriented simple four-cycles in total. The other \(39\) are nullhomologous and constitute the second affine orbit, also of size \(39\).

## Assumptions and scope
All calculations use the specific labelled graph above and the complete clique complex \(K\), not merely a chosen embedding of the graph. A graph cycle is a closed simple edge path, identified under cyclic relabeling and reversal; its length counts edges. Nonzero means nonzero in **simplicial** \(H_1(K;\mathbb F_2)\). The natural affine symmetries are maps \(t\mapsto at+b\) for \(a\in Q\), \(b\in\mathbb F_{13}\). No claim concerns longer cycles, the entire marked integral length spectrum, or other Paley graphs.

## Proof
**1. The torus and its homology.** The quadratic residues modulo \(13\) are \(Q=\{1,3,4,9,10,12\}\). Direct inspection of this six-element set gives \(39\) graph edges, \(26\) triangles, no four-cliques, two triangles incident to every edge, and a six-cycle link at every vertex. The complex is thus a closed connected triangulated surface with Euler characteristic \(13-39+26=0\). Its torus structure is also identified explicitly in Jones–Mačaj, Example 6 [2]. The mod-two simplicial boundary of the 26 triangles has rank \(25\), as verified by integer bit-vector row reduction. The graph is connected, so the one-cycle space has dimension \(39-13+1=27\). Therefore
\[
\dim_{\mathbb F_2} H_1(K;\mathbb F_2)=27-25=2.
\]

**2. All four-cycles.** Two adjacent vertices of \(P_{13}\) have exactly \(2\) common neighbors, and two nonadjacent vertices have exactly \(3\), each equality checked directly from \(Q\). There are \(39\) adjacent and \(39\) nonadjacent unordered vertex pairs. Counting pairs of opposite vertices in a simple four-cycle, then dividing by two because each cycle has two such pairs, gives
\[
\#C_4=\frac{39\binom22+39\binom32}{2}=78.
\]

**3. The two affine orbits.** Set \(c_0=(0,1,4,3)\) and \(c_1=(0,1,2,3)\), denoting cycles by their successive vertices modulo \(13\). For each, its orbit under the \(78\) maps \(t\mapsto at+b\) has size \(39\); this is a finite equality checked by direct residues and also replayable with `check_paley13.py`. The two orbits are disjoint: \(c_0\) is the boundary (over \(\mathbb F_2\)) of the sum of triangles \((0,1,4)\) and \((0,3,4)\), whereas \(c_1\) has nonzero cohomological pairing, as shown below. Their cardinalities exhaust all \(78\) cycles. Therefore exactly \(39\) are nullhomologous and exactly \(39\) are essential.

**4. Two explicit cocycle witnesses and the three classes.** Identify an unoriented edge by its increasing endpoints. Define \(1\)-cochains \(w_1,w_2\) over \(\mathbb F_2\) to have coefficient one on the following edge sets and zero elsewhere:

\(w_1:\) `(2,3), (2,12), (3,6), (6,7), (7,10), (7,11), (8,11), (11,12)`;

\(w_2:\) `(5,9), (6,9), (6,10), (7,10), (7,11), (8,9), (8,11), (8,12)`.

For all \(26\) triangles the sum of coefficients on its edges is even; thus \(\delta w_1=\delta w_2=0\). Their evaluation on the four-cycles
\[
 c_1=(0,1,2,3),\qquad c_2=(0,1,5,9),\qquad c_3=(0,3,6,9)
\]
is respectively \((1,0)\), \((0,1)\), and \((1,1)\). Since \(\dim H_1=2\), these pairings completely classify mod-two homology classes; in particular the cycles are essential. Each \(c_i\) has a translation orbit of size \(13\), and the three orbits are disjoint and together comprise the essential affine orbit of \(39\) cycles. Translation acts trivially on \(H_1(K;\mathbb F_2)\): its induced representation has order dividing \(13\), but \(|GL_2(\mathbb F_2)|=6\). Hence the three translation orbits represent three distinct nonzero classes, exactly \(13\) cycles each.

**5. Minimality.** A simple graph has no loops or two-edge simple cycles. Every three-edge cycle of \(P_{13}\) is one of the \(26\) triangular faces, hence is nullhomologous. Since \(c_1\) is essential, the shortest nonzero simple cycle has length \(4\), completing the claimed classification.

## Verification
Run `python3 check_paley13.py` using only the Python standard library. The embedded checker reconstructs the graph and clique triangles from quadratic residues, computes the mod-two second-boundary rank, enumerates all unoriented simple four-cycles canonically, checks both cocycles on every triangle and on three representative cycles, and checks affine and translation orbit sizes. It prints `PALEY13_FLAG_TORUS_SYSTOLE_EXACT_OK`. All enumerations are bounded over the explicit \(13\)-vertex graph; the proof uses the same exact finite structure and does not infer an infinite-family statement.

## Relationship to prior work
The existence and geometry of the \(13\)-vertex toroidal Paley map, including its affine symmetry group and \((13,39,26)\) face vector, are established in Jones–Mačaj [2]; **these are prior results, not new claims**. Delecroix–Ebbens–Lazarus–Yakovlev [1] develop general algorithms for length spectra of combinatorial tori. Their algorithms apply in principle to this torus but do not state the particular enumeration, its two affine orbits, or the three equally populated mod-two homology classes. The classification here is an explicit graph-specific computation with cohomology witnesses and a symmetry proof, rather than a new algorithm or a new torus construction.

## Limitations
The claim classifies **unoriented simple four-edge** cycles and the mod-two systolic shell only; it does not give the full integral marked length spectrum or determine lengths in every integral homology class. An equivalent computation may exist in classical regular-map literature or in unindexed material; no claim of exhaustive bibliographic uniqueness is made. The checks are finite and self-contained, but independent external validation has not been performed.

## References
[1] Vincent Delecroix, Matthijs Ebbens, Francis Lazarus, Ivan Yakovlev, *Algorithms for Length Spectra of Combinatorial Tori*, first public arXiv version 14 March 2023, arXiv:2303.08036, https://arxiv.org/abs/2303.08036. General length-spectrum framework and methods.

[2] Gareth A. Jones, Martin Mačaj, *Regular dessins with primitive automorphism groups*, first public arXiv version 21 March 2023, arXiv:2303.11808, Example 6, https://arxiv.org/abs/2303.11808. The established Paley-13 torus embedding, face vector, and affine symmetries.
