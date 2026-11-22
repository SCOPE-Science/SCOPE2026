# A uniform four-cycle boundary theorem for open-neighborhood complexes of clique products

## Finding
For every integer \(m\ge4\), the ordinary **open Lovász neighborhood complex** of the Cartesian product \(G_m=K_m\square C_4\) has the integral homotopy type
\[
\boxed{\mathcal N(G_m)\simeq\bigvee^{4m^2-10m+3}S^2\ \vee\ \bigvee^4 S^{m-2}.}
\]
For \(m=4\), coincident dimensions combine to give \(\bigvee^{31}S^2\); for \(m=6\), the result is \(\bigvee^{87}S^2\vee\bigvee^4S^4\). Thus every complex in this family is simply connected and has torsion-free integral homology. The \(m=5\) specialization was independently established previously; the new result is the all-width classification and its uniform symbolic proof, not priority for that specialization.

## Assumptions and scope
All graphs are finite, simple and loopless. Write vertices \(v_{i,a}\), where \(i\in\mathbb Z/4\mathbb Z\) and \(a\in\{0,\ldots,m-1\}\). Two distinct vertices are adjacent if their cycle coordinates agree and colors differ, or their colors agree and cycle coordinates are adjacent. Let \(R_i=\{v_{i,a}:0\le a<m\}\). The *open* neighborhood of \(v_{i,a}\) is
\[
F_{i,a}=\big(R_i\setminus\{v_{i,a}\}\big)\cup\{v_{i-1,a},v_{i+1,a}\}.
\]
A nonempty vertex set is a simplex of \(\mathcal N(G_m)\) precisely when contained in at least one of the \(4m\) sets \(F_{i,a}\); all homotopy types refer to geometric realizations. The fiber boundaries \(B_i=\partial\Delta(R_i)\) are \((m-2)\)-spheres and are simply connected under \(m\ge4\). No closed-neighborhood, graph Čech, total cut or matching-complex convention is used.

## Proof
**1. A different collapse at the short period.** For each center \((i,a)\), write
\[
P_{i,a}=\{v_{i-1,a},v_{i+1,a}\},\qquad h_{i,a}=v_{i,a+1\bmod m},\qquad U_{i,a}=R_i\setminus\{v_{i,a},h_{i,a}\}.
\]
Unlike the case of cycles of length at least five, \(P_{i,a}=P_{i+2,a}\): the two outside vertices have *two* possible centers. The bare diagonal edge \(P_{i,a}\) therefore cannot be removed by a free-face collapse. However any face containing \(P_{i,a}\) and at least one vertex of \(U_{i,a}\) lies in the unique neighborhood generator \(F_{i,a}\): a different center in the same row cannot have both outside vertices of color \(a\), and the opposite center's neighborhood has no vertex of \(R_i\) other than \(v_{i,a}\), which is excluded. For each nonempty \(A\subseteq U_{i,a}\), pair
\[
P_{i,a}\cup A\quad\longleftrightarrow\quad P_{i,a}\cup A\cup\{h_{i,a}\}.
\]
Perform these pairs in decreasing order of \(|A|\), center by center. The lower face's other cofaces within its unique generator were removed earlier; the displayed upper face is its only remaining strict coface. Each pair is an actual elementary simplicial free-face collapse. No two centers share these paired faces. This first stage removes exactly \(4m(2^{m-2}-1)\) pairs, retaining \(P_{i,a}\) and exactly the triangle \(P_{i,a}\cup\{h_{i,a}\}\) at each center.

**2. Single-wing collapses.** For every center \((i,a)\), either outside vertex \(u\in P_{i,a}\), and every \(A\subseteq U_{i,a}\) with \(|A|\ge2\), pair
\[
\{u\}\cup A\quad\longleftrightarrow\quad\{u,h_{i,a}\}\cup A,
\]
in decreasing order of \(|A|\). Because any face containing one outside vertex and two distinct vertices of \(R_i\) has the unique generator \(F_{i,a}\), and every coface containing both outside vertices was already removed, these are again genuine free-face collapses. This stage removes \(8m(2^{m-2}-m+1)\) pairs. The resulting core consists **exactly** of the four row-boundary spheres \(B_i\); for each adjacent pair of rows, all cross edges joining unlike colors and \(2m(m-2)\) surviving single-wing triangles; and, for each opposite pair of rows, the \(m\) same-color diagonal edges \(P_{i,a}\), each incident to the two retained triangles centered at the other two rows. There are no other mixed faces. All claims about free faces and this exact core are also checked directly for several widths by the standalone verifier.

**3. Resolve the four ordinary interfaces.** Consider one adjacent-row interface. Its cross edges are indexed by the \(E=m(m-1)\) edges of the connected crown graph \(K_{m,m}\) with the diagonal matching deleted. Its \(q=2m(m-2)\) wing triangles each relate two cross edges sharing a vertex, the third side lying in a row sphere. The triangles at every fixed endpoint connect its \(m-1\) incident cross edges along a star of \(m-2\) relations. Since the crown graph is connected for \(m\ge4\), the resulting relation graph on all \(E\) cross edges is connected. Select \(E-1\) relation triangles along a spanning tree. In a relative CW presentation these two-cells have unit coefficients on successive cross one-cells, permitting honest \(1\)-\(2\) CW cancellations; choose one cross edge as the surviving bridge between the two row spheres. Because the row spheres are simply connected, the row-side arcs of these triangles contribute no nontrivial loop. The \(q-E+1=m^2-3m+1\) remaining triangles have nullhomotopic attaching loops and split off as two-spheres. The four interfaces meet only along the fiber spheres, so their cancellations may be performed successively without changing the other interfaces. The result *before incorporating the retained opposite-row diagonals* is a cycle of four bridge one-cells, with the four \(B_i\) attached and \(4(m^2-3m+1)\) two-sphere summands.

**4. The short-period diagonal relations kill the circle.** There are exactly \(2m\) diagonal one-cells joining equal-color vertices in opposite rows. Every such diagonal is contained in exactly two retained triangles, one via each of the two possible intermediate rows of \(C_4\). After the interface cancellations, the boundary of either triangle is that diagonal one-cell together with a path of two bridges, up to nullhomotopic row paths. Use one triangle for each diagonal to cancel its one-cell with unit incidence. The second triangle for that diagonal then attaches along the concatenation of the two distinct length-two paths between opposite rows. This is a loop of winding number \(\pm1\) around the four-bridge cycle. One of these \(2m\) remaining triangles kills that unique circle by a \(1\)-\(2\) cancellation. All other \(2m-1\) triangles now attach by nullhomotopic loops and split off as two-spheres. No higher attaching maps intervene: every used cell outside the row spheres has dimension at most two, and those spheres have trivial fundamental group.

**5. Count the summands.** The four fiber boundaries survive as \(\bigvee^4 S^{m-2}\). The second-dimensional spheres consist of
\[
4(m^2-3m+1)+(2m-1)=4m^2-10m+3
\]
summands. All cancellations are homotopy equivalences with unit incidence and do not invert any nonunit integer, proving the claimed **integral homotopy type for every integer \(m\ge4\)**. For \(m=4\) the two wedge groups of two-spheres add. This is a genuine all-parameter proof; finite computations below corroborate its local identities, not extrapolate the theorem.

## Verification
Run `python3 verify_neighborhood_four_cycle.py` using standard Python 3. It builds the original graph adjacency independently and generates every open-neighborhood face. For \(m=4,5,6,7\), it checks each individual elementary free-face pair from Steps 1–2 against **all** current strict cofaces, compares the resulting core with an independently constructed core, and tests the connected crown-interface relation graph and its exact surplus count. It also computes full mod-two simplicial boundary ranks directly on the original complex. As an independent check it creates a different, lexicographic acyclic discrete-Morse matching on the original faces, checks the complete directed face-poset for cycles, and counts its critical cells. Expected output is supplied as `verification_output.txt`. All checks pass in all four widths. No modular experiment alone is presented as proof of the infinite theorem or integral homotopy type.

## Relationship to prior work
The published all-width formula for \(\mathcal N(K_m\square C_n)\) at \(m\ge4,n\ge5\) [1] includes one essential circle, \(n\) fiber spheres, and \(n(m^2-3m+1)\) two-spheres. Its uniqueness-of-center proof explicitly requires \(n\ge5\), whereas here opposite-row pairs have two centers. The stronger published result for arbitrary four-cycle-free base graphs [2] also explicitly excludes this base. Thus substituting \(n=4\) is invalid: the circle vanishes and \(2m-1\) additional two-spheres appear. A published single-case calculation [3] already proves the \(m=5\) specialization (53 two-spheres and four three-spheres); **that exact case is prior work**, and its exhaustive computation does not establish this new uniform all-width theorem. The \(m=4\) case yields 31 two-spheres, while \(m=6\) yields 87 two-spheres and four four-spheres.

Chauhan, Shukla and Vinayak [4] study the same graph products but the *total two-cut complex*, a different simplicial complex with facets complementary to nonadjacent pairs; its classification cannot imply this open-neighborhood statement. Shukla [5] treats maximum-degree-at-most-three graphs and four-regular circulants, not this degree-\(m+1\) graph family. Matsushita's fundamental-group correspondence [6] does not supply the sphere multiplicities. Targeted research-record, primary-text and web searches identified no theorem implying the complete present all-width classification. This is a bounded comparison, not a universal publication-priority certificate.

## Limitations
The formula requires exactly the four-cycle base and clique width \(m\ge4\). It is nonequivariant and determines homotopy types, not homeomorphism or canonical automorphism actions. The construction does not classify other four-cycle-containing base graphs; in particular it does not infer an extension to all graph products with short cycles. An unindexed equivalent result remains a residual priority risk. Independent mathematical audit has not been performed.

## References
[1] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, public research record, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c

[2] *Open-neighborhood homotopy of clique fibers over square-free base graphs*, public research record, October 25, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-open-neighborhood-homotopy-of-clique-fibers-over-square-free-bas--8ad90b221ab2

[3] *A mixed-dimensional sphere wedge at the four-cycle boundary of clique-fiber neighborhood complexes*, public research record, November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-mixed-dimensional-sphere-wedge-at-the-four-cycle-boundary-of-c--f164015126af

[4] P. Chauhan, S. Shukla and K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486, first public December 4, 2025, especially Theorem 1.5. https://arxiv.org/html/2512.04486v1

[5] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public February 13, 2018. https://arxiv.org/html/1802.04526v2

[6] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public October 10, 2012. https://arxiv.org/abs/1210.2803
