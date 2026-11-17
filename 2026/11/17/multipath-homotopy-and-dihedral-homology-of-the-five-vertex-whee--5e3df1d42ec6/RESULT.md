# Multipath homotopy and dihedral homology of the five-vertex wheel

## Finding
For the five-vertex wheel \(W=C_4\vee K_1\), with each edge replaced by its two directed arcs, the integral homotopy type of the multipath complex \(X(D)\) and the complete rational dihedral action on its reduced homology are
\[
X(D)\simeq\bigvee^{19}S^2\vee\bigvee^{8}S^3,
\qquad
\chi_{\widetilde H_2}=(19,3,-1,1,1),\quad
\chi_{\widetilde H_3}=(8,0,0,0,0).
\]
The character order is the identity, half-turn, either quarter-turn, either reflection through opposite rim vertices, and either reflection through opposite rim edges. Therefore the third rational homology is one regular \(D_4\)-representation. Writing \(A_1,A_2\) for the one-dimensional representations with quarter-turn \(+1\) and reflection \(+1,-1\), \(B_1,B_2\) for those with quarter-turn \(-1\) and reflection \(+1,-1\), and \(E\) for the two-dimensional geometric square representation, the second rational homology is
\[
3A_1\oplus2A_2\oplus3B_1\oplus3B_2\oplus4E.
\]

## Assumptions and scope
The undirected wheel has vertex set \(\{0,1,2,3,4\}\), square-rim edges \(01,12,23,30\) and hub edges \(40,41,42,43\). The sixteen directed arcs are all ordered pairs above these eight edges, sorted lexicographically. A multipath face is a set of arcs for which each original vertex has at most one selected incoming and at most one selected outgoing arc, and for which no directed cycle occurs (including two-cycles). Equivalently, the components are vertex-simple directed paths or isolated vertices. The group acts by \(r(i)=i+1\pmod4\), \(s(i)=-i\pmod4\) for rim vertices, fixing \(4\). The homotopy statement is integral and nonequivariant; the representation statement is rational only.

## Proof
**Finite complex and acyclic matching.** Identify a nonempty arc subset with its sixteen-bit mask, with bit \(j\) corresponding to arc \(j\) in the above ordering. Exhaustively enumerate all \(2^{16}-1\) nonempty masks, retaining exactly those meeting the indegree/outdegree and directed-acyclicity conditions. This produces precisely \(260\) faces, with face vector \((16,76,120,48)\).

Process arc indices in the fixed order
\[
(10,8,12,0,1,13,3,14,7,11,4,6,5,15,9,2).
\]
At each step, scan currently unmatched faces not containing that arc in increasing order of cardinality and then integer mask, and match a face \(\alpha\) with \(\alpha\cup\{j\}\) when both are still unmatched. This defines exactly \(116\) matching pairs. The unmatched faces consist of one vertex, nineteen two-dimensional faces and eight three-dimensional faces. Orient each Hasse incidence downward except for the \(116\) matched incidences, which are oriented upward. The attached program constructs all \(704\) nonempty-to-nonempty codimension-one incidences and topologically sorts this graph, visiting all \(260\) faces. The matching is therefore acyclic and yields a CW model with exactly the specified critical cells.

**Integral Morse differential.** Orient every simplex by increasing arc index. Its signed boundary uses \((-1)^k\) for deletion of its \(k\)-th arc. Let \(P\) project chains onto critical cells by discrete Morse reduction: \(P(\alpha)=\alpha\) for critical cells; \(P(\beta)=0\) for every matched upper cell; and, for a matched lower cell \(\alpha\) paired with upper cell \(\beta\), with incidence unit \(u=[\partial\beta:\alpha]\), set
\[
P(\alpha)=-u^{-1}\sum_{\gamma\ne\alpha}
[\partial\beta:\gamma]P(\gamma).
\]
Acyclicity makes the recursion finite. The Morse boundary of a critical cell \(c\) is \(P(\partial c)\). Direct integer evaluation of all eight critical three-cells gives the zero \(19\times8\) matrix. No other differential can be nonzero, because there are no critical one-cells. Thus the model consists of a single zero-cell, nineteen two-cells attached at that point, and eight three-cells whose degree vectors on the two-spheres vanish. The Hurewicz map \(\pi_2(\bigvee^{19}S^2)\to H_2(\bigvee^{19}S^2;\mathbb Z)\) is an isomorphism. Therefore all eight three-cell attaching maps are nullhomotopic, giving the asserted integral wedge of spheres.

**Dihedral characters.** The full signed simplicial boundary \(\partial_3:C_3\to C_2\) is a \(120\times48\) integer matrix of rank \(40\). Rational row reduction gives a basis of its eight-dimensional kernel, equal to the third rational homology since no four-simplices exist. For each of the eight square symmetries, permute arcs and include the orientation sign on each simplex. Exact rational linear algebra on that kernel gives character \(8\) at the identity and \(0\) at every other group element. For second homology, compute the reduced Lefschetz number of each symmetry as the signed sum over its invariant nonempty simplices minus \(1\); since only degrees two and three contribute, it equals \(\chi_2-\chi_3\). This yields \(\chi_2=(19,3,-1,1,1)\). Character orthogonality with class sizes \((1,1,2,2,2)\) gives multiplicities \((3,2,3,3,4)\) for \(A_1,A_2,B_1,B_2,E\), respectively. The third character is exactly that of the regular module.

## Verification
Run `python3 verify_wheel.py` using only the Python standard library. It independently reconstructs the arc sets and faces, performs the indicated matching, checks each of the \(704\) directed Hasse incidences for acyclicity, evaluates the exact signed Morse differential, computes the full third-boundary kernel over rational numbers, checks all eight signed symmetry characters, and decomposes them into irreducibles. It also computes independent mod-two simplicial boundary ranks \((15,61,40)\) in degrees \((1,2,3)\). The recorded output is in `verification_output.txt` and terminates in `WHEEL_MULTIPATH_EXACT_PASS`.

## Relationship to prior work
Caputi, Collari and Smith (2026), arXiv:2601.05670, give connectivity and integral homology for **bidirected paths and polygons**, and describe oriented-edge T-operations; their results do not cover the cone over a four-cycle with all spokes bidirected. Deshpande and Sawant (2026), arXiv:2602.14936, explicitly identify directed-linear-forest complexes with multipath complexes, but their vertex-decomposability criteria for acyclic digraphs and forest or cycle underlying graphs do not classify this cyclic wheel. An indexed computation of the **discrete Morse complex of a wheel** studies an entirely different complex, whose vertices are graph-incidence matchings, not directed arcs. An accessible same-topic indexed result on **bidirected double stars** has a different underlying graph with no rim cycle. Neither implies the homotopy type or the dihedral character established here.

## Limitations
This is an exact finite classification for one graph, not a classification of all wheel sizes or orientations. The rational representation decomposition does not assert an integral direct-sum decomposition of \(D_4\)-lattices. Independent mathematical validation has not been performed. Unindexed equivalent work remains possible.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public 2026-01-09), Sections 1–3. https://arxiv.org/html/2601.05670v1
2. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1 (first public 2026-02-16), Sections 1–5. https://arxiv.org/abs/2602.14936
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse theorem).
4. A. Hatcher, *Algebraic Topology*, Chapter 4 (the Hurewicz theorem and CW attaching maps).
