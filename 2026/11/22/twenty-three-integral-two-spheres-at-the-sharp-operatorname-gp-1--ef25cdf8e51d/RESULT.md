# Twenty-three integral two-spheres at the sharp \(\operatorname{GP}(18,3)\) radius-two boundary

## Finding

Let \(G=\operatorname{GP}(18,3)\) have vertices \(u_i,v_i\), with \(i\in\mathbb Z/18\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Give the 36 graph vertices unit-edge shortest-path distance, and define \(\operatorname{VR}(G;2)\) as the inclusive Vietoris–Rips complex whose nonempty faces are subsets of pairwise graph distance at most two. Then, **integrally and up to homotopy equivalence**,

\[
\boxed{\operatorname{VR}(G;2)\simeq \bigvee^{23} S^2.}
\]

In particular, \(\pi_1(\operatorname{VR}(G;2))\) is trivial, \(\widetilde H_2(\operatorname{VR}(G;2);\mathbb Z)\cong\mathbb Z^{23}\), and all other reduced integral homology groups vanish. At radius one the complex is the graph \(G\), with \(H_1(G;\mathbb Z)\cong\mathbb Z^{19}\). The finite 18-step case is a sharp boundary to the previously established formula \(\operatorname{VR}(\operatorname{GP}(n,3);2)\simeq S^1\vee\bigvee^n S^2\) for every \(n\ge19\). The previously available calculation for \(n=18\) already gave mod-two second Betti number 23; the **new assertion is its integral homotopy type and the mechanism by which the circle disappears**.

## Assumptions and scope

All indices below are modulo 18. The metric is on the 36 vertices of the graph, *not* on the continuous geometric realization of its edges. All Rips inequalities are inclusive; thus \(\operatorname{VR}(G;2)\) equals the clique complex of the graph square. A graph hexagon means a simple cycle of six edges, with its vertices listed in cyclic order. The claim concerns this exact graph and radius; it does not assert a new classification for other generalized Petersen parameters or higher radii.

Let \(B\) be the union of the 36 full tetrahedral simplices on closed graph neighborhoods \(N_G[w]\). Because \(G\) has girth six, each distance-two pair has a unique common graph neighbor. Write \(K=\operatorname{VR}(G;2)\).

## Proof

**1. Exhaustive short-cycle and clique structure.** The graph is cubic with 36 vertices and 54 edges. Any simple cycle with no spoke lies either on the outer 18-cycle or in one of the three length-six inner cycles. A simple cycle using spokes has an even number of spokes and at least one horizontal edge between consecutive spokes. Thus a simple cycle with at most six edges has exactly two spokes. Its intervening outer and inner path lengths \(a,b\ge1\), respectively, satisfy \(a+b+2\le6\) and \(\pm a\pm3b\equiv0\pmod{18}\). Since \(a+3b\le12<18\), equality modulo 18 reduces to equality of integers, which is possible only for \(a=3,b=1\) in the six-edge case. Hence the graph has no cycles of length three, four, or five, and has precisely these 21 hexagons:

\[
\gamma_i=(u_i,u_{i+1},u_{i+2},u_{i+3},v_{i+3},v_i,u_i),\quad 0\le i<18,
\]
\[
\delta_j=(v_j,v_{j+3},v_{j+6},v_{j+9},v_{j+12},v_{j+15},v_j),\quad j=0,1,2.
\]

In a girth-six graph, a triple of pairwise distance at most two not contained in one closed neighborhood is necessarily formed by the alternating vertices of a simple six-cycle: all three pairs have distance two and three distinct midpoints, which together form the cycle. In this graph the 42 alternating triples, two from each of the 21 cycles, are distinct and maximal faces of \(K\). An explicit exhaustive check, implemented in `verify.py`, independently enumerates **every** clique on the 36 vertices and certifies that these are the only faces outside \(B\); this finite check also verifies that no alternating triangle extends to a larger clique. It yields the complete nonempty face vector

\[
(f_0,f_1,f_2,f_3)=(36,162,186,36).
\]

In detail, 36 closed-neighborhood tetrahedra have 144 distinct triangle faces; the 42 extra triangles account for all 186. The 54 original graph edges and 108 distance-two edges account for all 162 edges. These are exact finite enumerations, not extrapolations from experimental samples.

**2. Collapse the neighborhood subcomplex.** For a vertex \(w\) with neighbors \(a,b,c\), the triangle \(\{a,b,c\}\) is a free face of the tetrahedron \(N_G[w]\), since a distance-two pair has a unique center. After removing that pair, the three centered triangles \(\{w,a,b\},\{w,a,c\},\{w,b,c\}\) each pair with and collapse onto removal of their corresponding distance-two edge. Repeating for all 36 centers gives precisely \(36+3\cdot36=144\) elementary simplicial collapses

\[
B\searrow G,
\]

preserving the original graph edges. The verifier checks each pair's unique-coface condition against the full *current* face set and confirms that the final complex is exactly \(G\). Under this deformation retraction, a distance-two edge is represented by the two-edge path through its unique graph midpoint.

**3. Two disks per hexagon.** The 42 additional triangular two-simplices have boundaries in \(B\). After transporting their attaching maps along the homotopy equivalence \(B\to G\), the two alternating triangles of a hexagon attach along the same six-edge graph cycle, up to reversing orientation. Indeed each of their three distance-two edges is replaced by the two-step path through its corresponding midpoint. Homotopy invariance of CW cell attachment therefore gives a CW complex with \(G\) and **two two-disks along each of the 21 loops** \(\gamma_i,\delta_j\). Attach one disk for each loop first and call the resulting CW complex \(W\). Once the first disk fills a loop, attaching the second disk to that nullhomotopic loop adds a wedge of one two-sphere. Thus

\[
K\simeq W\vee\bigvee^{21}S^2.
\]

This is a homotopy-pushout replacement, **not** a claim that the collapses of \(B\) can be performed unchanged inside \(K\), where the exceptional triangles also meet distance-two edges.

**4. The 18 outer-spoke loops eliminate the inner edges.** First attach the disks for all \(\gamma_i\). Each \(\gamma_i\) contains the inner edge \(v_i v_{i+3}\), which belongs to none of the other 17 outer-spoke loops \(\gamma_k\). In the corresponding two-dimensional cellular presentation, each such disk and its uniquely incident inner edge form a free elementary CW pair. Collapse these 18 pairs. The remaining graph is the outer 18-cycle plus 18 pendant spokes, hence deformation retracts to the outer circle. Therefore the first 18 disk attachments reduce \(G\) to a copy of \(S^1\).

**5. The three inner hexagons fill that remaining circle three times.** The preceding collapse replaces the oriented inner edge \(v_i\to v_{i+3}\) by the forward outer three-edge path \(u_i\to u_{i+1}\to u_{i+2}\to u_{i+3}\), with the spoke endpoints joined and then retracted. Traversing \(\delta_j\) therefore gives six consecutive forward outer paths, each of length three. They traverse each of the 18 outer edges exactly once, with positive orientation. Hence **each** of \(\delta_0,\delta_1,\delta_2\) has degree \(+1\) on the remaining circle. The first inner-hexagon disk fills that circle and leaves a contractible CW complex; each of the other two disks attaches along a now-nullhomotopic loop and contributes a two-sphere. Consequently \(W\simeq S^2\vee S^2\). Combining with Step 3 gives

\[
K\simeq (S^2\vee S^2)\vee\bigvee^{21}S^2\simeq\bigvee^{23}S^2.
\]

The argument is integral at every step and classifies the homotopy type, not just homology over a field. The three extra inner cycles exactly remove the surviving stable-range circle and replace it by two additional two-sphere classes.

## Verification

The fully standalone Python 3 script `verify.py` and its captured `verification_output.txt` reproduce the following exact finite checks, without third-party libraries: all 36 graph-vertex distance tables; complete enumeration of all simplices; all 21 simple six-cycles; distinctness and maximality of the 42 exceptional triangles; all 144 free-face collapses from \(B\) to the graph; occurrence and unique-edge conditions of the outer-spoke loops; and degree-one traversal of the inner loops after the graph retraction. The script additionally checks a separate exact cellular presentation: 36 initial tetrahedron–triangle collapses, a 35-edge spanning tree, 127 legal unit-generator Tietze eliminations of the 150 remaining triangular two-cells, ending with 23 trivial two-cell attaching words. These are genuine elementary two-complex homotopy reductions, not inferences from finite-field ranks. Exact signed simplicial boundary elimination over the primes two, three, and five also independently produces boundary ranks \((35,127,36)\). The terminal output must be `PASS`.

## Relationship to prior work

Adamaszek and Adams [1] give a motivating exact integral Rips classification for **hypercube** shortest-path metrics; their theorem is not about the generalized Petersen graph. Adamaszek's graph-power results [2] include a collapse theorem for girth at least seven and a closed-neighborhood-cover result; the present graph has girth exactly six, and its 42 exceptional triangles preclude either direct hypothesis. Metric-gluing results [3] concern different decomposition conditions and do not classify these overlapping hexagons.

The closest published hexagon result [4] **already** proves the stable \(n\ge19\) family and explicitly gives only the mod-two ranks \(\widetilde\beta_1=0,\widetilde\beta_2=23\) at \(n=18\), expressly withholding an integral homotopy classification there. Those ranks do **not** imply simple connectivity, absence of torsion, or a wedge-of-spheres homotopy type. The 21-loop CW argument above supplies the missing stronger conclusion. The other hexagon-packing classification [5] assumes pairwise edge-disjoint hexagons, whereas every outer edge here belongs to three of the outer-spoke cycles. Results for the \(\operatorname{GP}(n,2)\) family [6] concern a different inner step and do not cover this graph. No inspected source entails the stated integral homotopy equivalence; an unindexed stronger result remains a bibliographic possibility.

## Limitations

This is the integral homotopy type of the single scale-two, 36-vertex complex; it is **not** a classification of the higher-radius filtration, an equivariant decomposition, or a theorem for neighboring values of \(n\). The first and second mod-two Betti numbers at this boundary were already published and are not claimed as new. The exact finite clique facts were checked by exhaustive code over all vertices of this graph, while the homotopy argument uses the explicit CW reductions; checks over several primes alone would not certify integral homotopy. The literature assessment does not constitute a proof of uniqueness, and no independent mathematical audit has been performed.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first public 1 March 2021. https://arxiv.org/abs/2103.01040.
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public 3 April 2011, especially Proposition 2.2 and Theorem 3.1. https://arxiv.org/abs/1104.0433.
3. *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, first public 18 December 2017, especially Theorem 3.15. https://arxiv.org/abs/1712.06224.
4. *Persistent hexagon spheres in generalized Petersen graph thickenings*, published 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-persistent-hexagon-spheres-in-generalized-petersen-graph-thicken--c6f4ddebbf06.
5. *A hexagon-packing classification of scale-two graph Rips complexes*, published 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb.
6. *Five exceptional scale-two Rips homotopy types for \(\operatorname{GP}(n,2)\)*, published 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-five-exceptional-scale-two-rips-homotopy-types-for-gp-n-2--d4c834641f87.
