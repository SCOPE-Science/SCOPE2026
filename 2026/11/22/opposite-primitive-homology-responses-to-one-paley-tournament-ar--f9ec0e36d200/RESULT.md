# Opposite primitive homology responses to one Paley tournament arc fault

## Finding
Let \(P\) be the quadratic-residue tournament on \(\mathbb F_{11}\), with \(u\to v\) exactly when \(v-u\in Q=\{1,3,4,5,9\}\). Let \(P-e\) be obtained by removing any arc \(e\), and let \(P^{\leftrightarrow e}\) be obtained by reversing that arc. For a loop-free digraph \(D\), define the **directed out-neighborhood complex** \(\mathcal N^+(D)\) by declaring every nonempty subset of an out-neighborhood to be a simplex. Set
\[
X=\mathcal N^+(P),\qquad Y=\mathcal N^+(P-e),\qquad Z=\mathcal N^+(P^{\leftrightarrow e}).
\]
Then for every choice among the fifty-five arcs,
\[
|X|\simeq\bigvee^{21}S^2,\qquad
|Y|\simeq\bigvee^{18}S^2,\qquad
|Z|\simeq\bigvee^{17}S^2.
\]
The evident simplicial inclusions \(Y\hookrightarrow X\) and \(Y\hookrightarrow Z\) have respective homotopy cofibers
\[
|X|/|Y|\simeq\bigvee^3S^2,
\qquad |Z|/|Y|\simeq S^3.
\]
Consequently, in **integral** reduced degree-two homology, the first inclusion is a primitive injection with cokernel \(\mathbb Z^3\), whereas the second is a primitive surjection with kernel \(\mathbb Z\). After suitable, not canonically specified, wedge-sphere identifications, these maps are respectively the standard inclusion of eighteen into twenty-one two-sphere summands and the standard projection of eighteen onto seventeen summands. No statements about simultaneous arc faults or larger tournaments are asserted.

## Assumptions and scope
All complexes are finite abstract simplicial complexes on the labelled vertices \(\mathbb F_{11}=\{0,\ldots,10\}\); their geometric realizations and ordinary integral homology are meant. The out-neighborhood of \(v\) is \(N^+(v)=\{w:v\to w\}\), without \(v\) itself. This construction is neither the directed flag complex nor the undirected Lovász neighborhood complex. The homotopy cofiber of an inclusion of simplicial complexes is its quotient, with the subcomplex collapsed to one point. The inclusions exist because arc deletion removes one outgoing neighbor and reversal then adds a different outgoing neighbor. The quadratic residues form a multiplicative group, so all arcs belong to a single affine orbit under \(t\mapsto at+b\), \(a\in Q\), \(b\in\mathbb F_{11}\). It suffices to analyze the arc \(0\to1\).

## Proof
**1. Complete finite complexes.** The eleven out-neighborhoods in the intact tournament are the translates \(t+Q\). Distinct blocks meet in exactly two vertices: the nonzero differences of elements of \(Q\) each occur twice. Hence every simplex of dimension at least two belongs to a unique block, and the intact complex has face vector \((11,55,110,55,11)\), in dimensions zero through four. Removing \(0\to1\) replaces the block \(Q\) by \(Q\setminus\{1\}\) and leaves the other ten blocks fixed. Reversing that arc subsequently adjoins \(0\) to the block \(1+Q=\{2,4,5,6,10\}\). Direct finite subset enumeration gives respectively
\[
\begin{array}{c|rrrrrr}
&f_0&f_1&f_2&f_3&f_4&f_5\\\hline
X&11&55&110&55&11&0\\
Y&11&55&104&51&10&0\\
Z&11&55&109&61&15&1.
\end{array}
\]
The accompanying standard-library verifier independently constructs all simplices from those exact blocks; no table lookup is used.

**2. Three absolute homotopy certificates.** On the full face poset of each complex, repeatedly remove an elementary free pair consisting of a codimension-one face and its unique remaining maximal coface. If none remains, mark and delete a maximal cell as critical. The deterministic priority rules and all assertions are in `verify.py`. This process gives, respectively for \(X,Y,Z\), \(110,106,117\) matched pairs and the critical-cell profiles
\[
\{0:1,\,2:21\},\quad\{0:1,\,2:18\},\quad\{0:1,\,2:17\}.
\]
The verifier checks for each chosen pair that the smaller face has **no other coface of any dimension** in the then-current poset, checks exact exhaustion of every enumerated simplex, and independently tests absence of directed cycles in the full reversed-matching Hasse graph. Thus these are genuine acyclic discrete-Morse matchings, not merely numerical ranks. The corresponding Morse CW complexes have one zero-cell, no one-cells and only the stated number of two-cells. All two-cell attaching maps are constant, proving the three wedge-of-spheres homotopy equivalences integrally.

**3. Relative collapse certificates.** For the pair \((X,Y)\), there are eleven relative simplices, with cardinality distribution \((6,4,1)\) in dimensions two, three, four. Four elementary relative free-face pairs eliminate all but three triangles. Explicitly the pairs, written (lower face; upper face), are
\[
\begin{array}{ll}
\{1,3,4,5\};&\{1,3,4,5,9\},\\
\{1,3,4\};&\{1,3,4,9\},\\
\{1,3,5\};&\{1,3,5,9\},\\
\{1,4,5\};&\{1,4,5,9\}.
\end{array}
\]
The surviving relative triangles are \(\{1,3,9\},\{1,4,9\},\{1,5,9\}\), whose entire boundaries belong to \(Y\). This proves \(X/Y\simeq\bigvee^3S^2\).

For \((Z,Y)\), twenty-one relative simplices form ten legal elementary relative free-face pairs, leaving the single tetrahedron \(\{0,2,4,10\}\); all four of its faces are in \(Y\). Thus \(Z/Y\simeq S^3\). The ten pairs are reconstructed and all codimension-one incidences verified by the same standalone procedure; its exact deterministic ordering is part of the executable certificate. In both cases the actual quotient simplicial face posets are exhaustively checked, including whether each unmatched face remains critical.

**4. Maps on integral homology.** Since \(\widetilde H_j(X),\widetilde H_j(Y),\widetilde H_j(Z)\) vanish outside degree two and are free there, the long exact sequences of the two pairs give
\[
0\longrightarrow\mathbb Z^{18}\longrightarrow\mathbb Z^{21}
\longrightarrow\mathbb Z^3\longrightarrow0
\]
for \((X,Y)\), and
\[
0\longrightarrow\mathbb Z\longrightarrow\mathbb Z^{18}
\longrightarrow\mathbb Z^{17}\longrightarrow0
\]
for \((Z,Y)\). The quotients on the right are free, so the corresponding image and kernel sublattices are primitive. A homotopy class of maps between wedges of two-spheres is determined by its integer degree matrix, and unimodular basis changes are realized by homotopy equivalences. The indicated standard inclusion and projection descriptions follow. The affine action carries the representative arc to every arc \(e\), completing the proof for all fifty-five choices.

## Verification
Run `python3 verify.py` using Python 3.9 or later, with no third-party dependencies. The executable (i) reconstructs the quadratic residues and all eleven out-neighbor blocks at three stages, (ii) enumerates and counts every nonempty simplex (respectively 242, 231 and 252), (iii) constructs and checks 110, 106 and 117 complete absolute Morse pairs, including full face-poset acyclicity, (iv) checks four and ten genuine relative free pairs and their residual critical cells, (v) independently computes all mod-two simplicial boundary ranks, and (vi) proves by enumeration that the fifty-five arcs are exactly one affine orbit. The required marker is `PASS: all 55 arcs, three absolute Morse models, and two relative collapse certificates`. This finite computation is exhaustive for the precisely specified eleven-vertex structures; it makes no assertion about arbitrary larger graphs.

## Relationship to prior work
Dochtermann and Singh introduce the directed out-neighborhood construction and its relation to directed Hom complexes, and discuss possible tournament homotopy types. The two published computations of the **intact** Paley eleven-vertex tournament out-neighborhood complex already establish \(X\simeq\bigvee^{21}S^2\) and its affine rational homology character. The present finding **does not claim the intact calculation as new**: it establishes instead the missing-arc and reversed-arc homotopy types and, crucially, their contrasting **integral inclusion maps** and homotopy cofibers. Those conclusions cannot be inferred from the intact homotopy type or affine character alone, and neither prior result's inspected proof treats arc deletion or reversal. Literature about Paley tournament directed flag complexes, oriented triangle Hom complexes, or undirected Paley graph neighborhood complexes has different defining face predicates and does not imply this fault response.

## Limitations
The result concerns only the directed quadratic-residue tournament of order eleven, only one faulty arc at a time, and ordinary (non-equivariant) homotopy types and integral maps. Wedge identifications are noncanonical. Absolute literature uniqueness cannot be guaranteed for unindexed work. No independent audit or computer-assisted formal proof by a separate system is asserted; the executable is a reproducible exact finite certificate and the mathematical arguments above give its topological interpretation.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, publicly posted 2021-08-24, Definition 4.1, Theorem 4.3, Sections 5 and 7.1. https://arxiv.org/abs/2108.10948
2. *The homotopy type and affine homology character of the Paley-11 tournament neighborhood complex*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-homotopy-type-and-affine-homology-character-of-the-paley-11--baff484d9f6d
3. *The Paley eleven-vertex tournament has an out-neighborhood complex of twenty-one two-spheres*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-paley-eleven-vertex-tournament-out-neighborhood-spheres-and-affi--70ec12667504
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
