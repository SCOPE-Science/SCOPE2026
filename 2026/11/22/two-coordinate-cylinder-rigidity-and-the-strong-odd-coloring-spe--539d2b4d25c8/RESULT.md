# Two-coordinate cylinder rigidity and the strong odd coloring spectrum of the Clebsch graph

## Finding
Let \(C\) be the sixteen-vertex Clebsch graph in its even-parity binary representation. A *strong odd coloring* is a proper vertex coloring in which every color occurring in the open neighborhood of a vertex occurs there an odd number of times. Let \(P_C(z)\) count all strong odd vertex-color partitions of \(C\), by their number of nonempty color classes, with graph vertices fixed and color names forgotten. Then
\[
P_C(z)=70z^4+360z^7+300z^{10}+40z^{13}+z^{16}.
\]
In particular \(\chi_{\mathrm{so}}(C)=4\), with precisely \(70\) optimal unlabelled partitions, or \(1680\) optimal assignments using four distinct named colors.

Every nonempty strong-odd-admissible color class is either a singleton or a four-element *two-coordinate cylinder*: the even-parity five-bit words having prescribed bits in some specified pair of coordinate positions. There are exactly \(40\) such four-element classes. Of the \(70\) optimal partitions, \(10\) use a single coordinate pair throughout and \(60\) use two coordinate pairs sharing one position. No optimal partition uses three or more coordinate pairs.

## Assumptions and scope
The vertices of \(C\) are the \(16\) words \(x\in\mathbb F_2^5\) whose coordinate sum is even. Distinct vertices \(x,y\) are adjacent precisely when their Hamming distance equals \(4\). This specifies a simple \(5\)-regular graph with \(40\) edges, isomorphic to the Clebsch graph. Every vertex is distinguished by its binary word; isomorphic relabelings are not divided out. Graph color classes are unlabeled blocks, so the coefficients count set partitions, not permutations of color names.

An *odd independent set* is an independent vertex set \(S\) such that every vertex has either zero or an odd number of neighbors in \(S\). The nonempty color classes of a strong odd coloring are exactly the odd independent sets. All statements concern this single finite graph and the ordinary open-neighborhood (not closed-neighborhood) condition.

## Proof
**1. Classification of admissible blocks.** Let \(S\) be a nonempty odd independent set. The graph is invariant under addition of any even-parity word, so translate one member of \(S\) to the zero word. All other words in \(S\) must be nonneighbors of zero. They therefore have Hamming weight \(2\), and can be regarded as edges of the complete graph on the five coordinate positions. Write \(F\) for this edge family. The independence of \(S\) implies that any two edges of \(F\) intersect: two disjoint two-subsets have symmetric difference of size \(4\) and would represent adjacent vertices.

For each coordinate \(i\), let \(g_i\) be the weight-four word whose sole zero is at \(i\). This word is outside \(S\). It is adjacent to zero, and it is adjacent to the vertex represented by the two-subset \(\{j,k\}\) if and only if \(i\in\{j,k\}\). Consequently
\[
|N(g_i)\cap S|=1+\deg_F(i).
\]
The odd-neighborhood requirement forces every degree of \(F\) to be even. A family of pairwise-intersecting distinct edges is contained in a star or is the three edges of a triangle. Every nonempty star has a vertex of odd degree (a leaf). Thus \(F\) is empty or is a complete triangle. The first possibility gives a singleton, and the second gives
\[
S=\{0,e_a+e_b,e_a+e_c,e_b+e_c\}
\]
for some three coordinate positions \(a,b,c\).

The latter set consists precisely of all even-parity words with the other two coordinates fixed to zero. Its translates are the two-coordinate cylinders, with the chosen two coordinates fixed to arbitrary bits. For any such cylinder, its vertices have no internal edges. Relative to the three remaining coordinates, the five possible adjacency steps have outside-coordinate profiles distributed as \(3,1,1\) over the three other cylinder cosets. Hence every vertex outside the cylinder has exactly \(1\) or \(3\) neighbors inside it. Every such cylinder is therefore odd independent. There are \(\binom52\cdot4=40\) distinct cylinders (four bit assignments for each of ten coordinate pairs), proving the classification.

**2. Disjoint-cylinder criterion.** A cylinder fixes two coordinate positions. Two cylinders using the same pair are disjoint exactly when their assignments differ. Two cylinders using distinct coordinate pairs are disjoint exactly when the pairs share one coordinate and the two fixed bits at that shared coordinate are opposite. Indeed, compatible assignments on at most four positions always extend to an even-parity five-bit word, and therefore yield a common vertex. In particular, cylinders with disjoint coordinate pairs always intersect.

**3. Count disjoint cylinder families.** A family of \(q\) mutually disjoint cylinders determines a unique strong odd coloring by using these cylinders as blocks and leaving every other vertex as a singleton. The resulting number of color classes is \(16-3q\). Let \(A_q\) be the number of such unordered cylinder families. Clearly \(A_0=1\) and \(A_1=40\), and \(q\le4\).

For \(q=2\), choosing two assignments of the same coordinate pair gives \(10\binom42=60\). There are \(30\) unordered pairs of distinct coordinate pairs sharing exactly one position. For each, the shared bit must be opposite (two possibilities), and each of the two nonshared bits is free (four possibilities together). These give \(30\cdot8=240\). Thus \(A_2=300\).

For \(q=3\), there are three cases. A single coordinate-pair support contributes \(10\binom43=40\). Exactly two supports contribute \(60\cdot2\cdot2=240\): choose the ordered majority and minority supports, the common bit of the two majority cylinders, and the unused bit of the minority cylinder. With three distinct supports, they must intersect pairwise. Three two-subsets that intersect pairwise form either a star or a triangle. The star cannot have three pairwise opposite binary assignments on its common coordinate; a triangle is possible and has \(2^3\) valid bit assignments. There are \(\binom53=10\) triangles, contributing \(80\). Therefore \(A_3=360\).

For \(q=4\), four cylinders cover all sixteen vertices. If all supports agree, there are \(10\) partitions. If exactly two supports occur, each must appear twice; the two supports must intersect, and the four cylinders are the two assignments in one shared-coordinate half together with the two assignments in the opposite half. There are \(30\cdot2=60\) such partitions. Three distinct supports cannot occur: the only pairwise-compatible support pattern is a triangle on coordinates \(a,b,c\); after three disjoint cylinders of this pattern are chosen, the remaining four vertices have the two complementary three-bit patterns on \(a,b,c\), so no coordinate is constant on all four remaining vertices. That remainder is not a two-coordinate cylinder. It cannot complete a four-cylinder partition. Thus \(A_4=10+60=70\).

It follows that \((A_0,A_1,A_2,A_3,A_4)=(1,40,300,360,70)\). Substituting the corresponding color counts \(16,13,10,7,4\) proves the polynomial. A four-cylinder partition exists (take all four assignments on one fixed coordinate pair), while no odd independent block has more than four vertices. This proves \(\chi_{\mathrm{so}}(C)=4\) and all optimizer statements. Distinct named-color assignments multiply the unlabelled count by \(4!\).

## Verification
Two self-contained programs accompany this result. Run `python3 verify_direct.py` to enumerate all \(2^{16}-1\) nonempty vertex subsets using graph adjacency defined directly by Hamming distance four, retain the odd independent subsets, and count all unordered partitions using a least-vertex recurrence. Its output confirms \(16\) singleton classes, \(40\) four-element classes and the coefficient sequence \((70,360,300,40,1)\) by increasing number of colors. This program also independently finds \(1190\) proper four-color partitions, of which \(70\) are strong odd.

Separately, run `g++ -O2 -std=c++17 verify_affine.cpp -o verify_affine && ./verify_affine`. This program builds the forty cylinders by their fixed coordinates and enumerates disjoint cylinder families. It confirms \((A_0,A_1,A_2,A_3,A_4)=(1,40,300,360,70)\) and the \(10+60\) partition-type split. The preceding structural proof, not the finite programs alone, establishes why these enumerations exhaust all admissible classes.

## Relationship to prior work
Kwon and Park introduced strong odd coloring in their 2024 preprint, gave general bounds for sparse graphs and discussed its relationship to square coloring. Caro, Petruševski, Škrekovski and Tuza (2024) treated planar classes and graph products. Their statements do not supply the four-element class classification or the Clebsch census above. A later paper by Caro and collaborators (2025), on odd independent sets, develops general bounds and mentions the Clebsch graph among triangle-free strongly regular graphs, but does not state the cylinder classification or the complete strong odd coloring polynomial. The direct theorem here concerns an exact finite structural census rather than a general upper bound.

## Limitations
This theorem concerns the unique named sixteen-vertex Clebsch graph, not all strongly regular graphs or all folded cubes. Only open-neighborhood strong odd colorings are counted. A structural proof and two independently written finite checks are provided; neither constitutes independent external mathematical validation. Priority assessment remains provisional, particularly for potentially equivalent results phrased in affine partitions or finite-geometry language.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, first publicly posted 2024-01-22, arXiv:2401.11653, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, first publicly posted 2024-10-03, arXiv:2410.02336, https://arxiv.org/abs/2410.02336.
3. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, first publicly posted 2025-09-25, arXiv:2509.20763, https://arxiv.org/abs/2509.20763.
