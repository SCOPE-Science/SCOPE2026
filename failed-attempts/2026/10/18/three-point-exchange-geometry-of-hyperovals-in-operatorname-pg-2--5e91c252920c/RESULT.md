# Three-point exchange geometry of hyperovals in \(\operatorname{PG}(2,4)\)

## Finding
A hyperoval is a six-point subset of the projective plane \(\operatorname{PG}(2,4)\) containing no three collinear points. Define the exchange graph \(\mathcal{H}\) whose vertices are all hyperovals and whose edges join two distinct hyperovals when exactly three points are replaced, equivalently when their intersection contains three points.

The graph \(\mathcal{H}\) has 168 vertices, is 40-regular, and has 3,360 edges. It is connected, with radius and diameter two. For two distinct hyperovals \(B,C\), their number of common neighbours in \(\mathcal{H}\) is determined exactly by the overlap:
\[
|N(B)\cap N(C)|=\begin{cases}4,&|B\cap C|=0,\\5,&|B\cap C|=1,\\16,&|B\cap C|=2,\\11,&|B\cap C|=3.\end{cases}
\]
There is no move replacing at most two points between distinct hyperovals. Thus three is the sharp minimum allowed replacement size giving connectivity, and any two hyperovals become mutually reachable in at most two three-point moves.

The graph has a canonical three-partition into classes of 56 hyperovals, with zero edges inside each class and 20 neighbours in each other class. Its complete adjacency spectrum is
\[
40^{(1)},\qquad 12^{(20)},\qquad 0^{(105)},\qquad (-6)^{(40)},\qquad (-20)^{(2)}.
\]
Superscripts in this display denote multiplicities, not powers. The graph contains exactly 12,320 triangles.

## Assumptions and scope
The field \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\) is represented by \(\{0,1,t,t+1\}\). The 21 points of \(\operatorname{PG}(2,4)\) are the nonzero triples of \(\mathbb F_4^3\) modulo common nonzero scalar, and the 21 lines are kernels of nonzero homogeneous linear forms, each having five points. All hyperovals are **labelled by these 21 projective points**, and the exchange graph does not quotient by projective automorphisms. The only allowed operation simultaneously deletes and adds the same number of distinct points, and each completed state must again be a six-point hyperoval. An edge uses precisely three replacements. All statements here concern the order-four Desarguesian plane, not general even-order planes.

## Proof
Choose the unique representative of each projective point whose first nonzero coordinate is one. For every unordered six-subset \(S\) of the 21 representatives, test the 21 lines: it is a hyperoval if and only if \(|S\cap L|\le 2\) for each line \(L\). These tests are exhaustive since every collinear triple lies on a projective line. Evaluating the complete set of \(\binom{21}{6}=54,264\) candidates produces 168 hyperovals.

The alternate construction enumerates all four-point sets containing no collinear triple. There are 2,520 of these quadrangles. For each, it tests every possible pair of added points; exactly one pair yields a hyperoval. Every hyperoval has exactly \(\binom64=15\) quadrangles, hence the 2,520 uniquely completed quadrangles give precisely 168 distinct hyperovals. In particular, two distinct hyperovals cannot share four points: the completion of that four-arc would have to be the same. Therefore replacements of one or two points cannot connect distinct states, and exactly-three-point replacements correspond exactly to the intersection-size-three relation.

Build the symmetric 168-by-168 zero-one adjacency matrix \(A\), with \(A_{B,C}=1\) exactly when \(|B\cap C|=3\). Enumerating all \(\binom{168}{2}=14,028\) unordered pairs gives overlap counts 840, 6,048, 3,780 and 3,360 for intersection sizes 0, 1, 2 and 3 respectively. Each row has forty ones, so the graph has \(168\cdot40/2=3,360\) edges. Computing \(\sum_D A_{B,D}A_{D,C}\) for every distinct pair yields respectively 4, 5, 16 and 11 for these four overlap types; the full pair counts are independently repeated by a second construction. In particular, every nonadjacent pair has a common neighbour, giving distance exactly two, while adjacent pairs have distance one. The graph is not complete, so every vertex has eccentricity two. The adjacent-pair common-neighbour count of 11 yields \(3,360\cdot11/3=12,320\) triangles.

Parity of overlap among hyperovals is an equivalence relation here, verified across all 168 states: it has precisely three classes of size 56. Within each class all distinct intersections have size zero or two; between classes they have size one or three. Each vertex has precisely twenty neighbours in each other class, proving the claimed three-partition and its regular cross-incidence.

For the spectrum, integer matrix multiplication verifies the exact zero-matrix identity
\[
A(A+6I)(A-12I)(A+20I)(A-40I)=0.
\]
Its five possible roots are distinct. The five exact traces \(\operatorname{tr}(A^j)\), \(j=0,1,2,3,4\), are respectively \(168,0,6720,73920,3346560\). Since the Vandermonde matrix on the five distinct roots is nonsingular, these five moments determine the eigenvalue multiplicities uniquely as \(105,40,20,2,1\) at roots \(0,-6,12,-20,40\). The integer identity and moments are checked against the explicitly constructed matrix, rather than inferred from approximate floating-point eigenvalues.

## Verification
Two separately implemented Python programs are included. `verify_direct.py` constructs the field by polynomial multiplication and first-nonzero-coordinate normalization, tests all 54,264 potential six-point sets, forms the complete adjacency matrix, calculates every common-neighbour count and exact integer spectral identity. It prints `direct_output.json`. `verify_quadrangles.py` instead uses a literal field multiplication table and last-nonzero-coordinate normalization, constructs the 168 sets by unique completion of all 2,520 four-arcs, then independently checks all 14,028 pair overlaps and common-neighbour counts, and performs breadth-first searches from each of 168 vertices. It prints `quadrangle_output.json`. Both programs map back to the same canonical 168-set certificate, SHA-256 `02ec2a9578cdf81b7773f1feeda922c745a0e539c8dbce7a8f76e91cd61d3694`.

Run `python3 verify_direct.py > direct_output.json` with Python 3 and NumPy, and `python3 verify_quadrangles.py > quadrangle_output.json` with Python 3 only. The included JSON outputs record the actual checks. All finite-domain loops and asserted invariants are explicit in the included source; neither an isolated sample nor a stochastic search is used as a substitute for exhaustive verification.

## Relationship to prior work
The total of 168 hyperovals and their splitting into three \(\operatorname{PSL}(3,4)\) orbits of 56, together with the even-intersection statistics within one orbit, are classical and are described by Devillers (2005), Section 3.10. Published hyperoval-intersection literature also provides the per-hyperoval overlap counts; these are treated here as background consistency checks, not as newly discovered enumerations. Betten (2005) develops geometric-code representations of these hyperovals, while Caullery and Schmidt (2014) study polynomial classification of hyperovals in even-order planes. These sources do not provide the specifically three-point exchange graph's full common-neighbour structure, sharp connectivity threshold, two-step diameter, or full adjacency spectrum in their examined relevant material. This is a finite, computationally exhaustive reconfiguration refinement of known hyperoval geometry, not a new classification of hyperovals.

## Limitations
The result is restricted to \(\operatorname{PG}(2,4)\). No generalization to other plane orders, a geometrically conceptual derivation of the common-neighbour table, or independent external proof review is claimed. Spectral calculations use exact signed 64-bit integer arithmetic at magnitudes for which overflow does not occur; they are reproducible with the displayed code. Published association-scheme tables or unindexed records could conceivably contain an equivalent exchange-graph spectrum; a negative literature search cannot establish absolute publication priority.

## References
1. A. Devillers, *A classification of finite partial linear spaces with a primitive rank 3 automorphism group of almost simple type*, Innovations in Incidence Geometry **2** (2005), 129–175, §3.10. DOI: 10.2140/iig.2005.2.129; https://msp.org/iig/2005/2-1/iig-v2-n1-p08-s.pdf.
2. A. Betten, *Geometric Codes and Hyperovals* (2005), https://www.math.colostate.edu/~betten/pub/betten33.pdf.
3. F. Caullery and K.-U. Schmidt, *On the classification of hyperovals* (first arXiv release 2014-03-12), arXiv:1403.2880v1, https://arxiv.org/abs/1403.2880.
4. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf, §6.2 (classical hyperoval intersections are background).
