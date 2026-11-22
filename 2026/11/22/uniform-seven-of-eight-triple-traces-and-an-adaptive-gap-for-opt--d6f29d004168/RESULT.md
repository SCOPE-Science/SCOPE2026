# Uniform seven-of-eight triple traces and an adaptive gap for optimal four-cube domination

## Finding

Let \(Q_4\) have vertex set \(V=\{0,1\}^4\), with vertices adjacent when they differ in one coordinate. Let \(\mathcal D\) be the family of all minimum-cardinality dominating sets of \(Q_4\), viewed as Boolean concepts through the membership predicates \(h_D(v)=\mathbf1_{\{v\in D\}}\). There are exactly 40 concepts, with each concept of cardinality four, in two cube-isometry orbits of sizes 16 and 24.

**Seven-of-eight theorem.** For every three-element query support \(T\subseteq V\), the trace class \(\{D\cap T:D\in\mathcal D\}\) has cardinality **exactly seven**. The absent pattern is the all-positive pattern for exactly 400 of the 560 triples; for the other 160 it has exactly two positive entries. The six geometrical triple types and their multiplicities are characterized in the proof. Every one- and two-element support is shattered, and no triple is shattered. Thus

\[
\Phi_{\mathcal D}(z)=1+16z+120z^2,\qquad
\operatorname{VCdim}(\mathcal D)=2.
\]

The online/adaptive learning dimension is instead

\[
\operatorname{Ldim}(\mathcal D)=3.
\]

The shattering complex is the complete graph on 16 vertices, with integral homotopy type a wedge of 105 circles.

## Assumptions and scope

All sets are labeled subsets of the 16 vertices of \(Q_4\); the graph has no loops. A dominating set is a subset \(D\) such that every vertex lies in \(D\) or is adjacent to a vertex in \(D\). The concept class contains **only** sets having the minimum dominating cardinality, not all dominating sets or inclusion-minimal sets. For a support \(T\), a trace is its intersection with one such \(D\). A support is shattered if all its \(2^{|T|}\) traces occur. The Littlestone dimension is the maximum depth of a full binary adaptive query tree whose root-to-leaf answers are realized by concepts. All exact formulas below concern this one finite, labeled graph, and no claim is made about other cube dimensions.

For explicit representatives, identify a four-bit vector with its integer from 0 to 15 (binary bits in any fixed order). Let \(\overline v=v\oplus 15\), and let \(d(u,v)\) denote Hamming distance.

## Proof

**1. Minimum sets and their structure.** A closed neighborhood in \(Q_4\) contains five vertices, so three vertices can cover at most 15 of the 16 vertices. The four-set \(\{0,1,14,15\}\) is dominating. Hence the domination number is four.

For any four-vertex dominating set \(D\), let \(e\) and \(o\) be its selected even-weight and odd-weight vertices. Each parity class has eight vertices. Covering even vertices gives \(8\le e+4o=16-3e\), and covering odd vertices gives \(8\le o+4e=4+3e\). Thus \(e=o=2\). Write \(E\) and \(O\) for these two-element subsets. Two distinct vertices of the same parity differ in either two or four coordinates.

If the vertices of \(E\) are at distance four, their open neighborhoods already cover all eight odd vertices. The two vertices of \(O\) must also be antipodal: if they were at distance two, their open neighborhoods would miss two even vertices at distance two from each other, while the two vertices of \(E\), available to cover those omissions, are antipodal. Conversely, any antipodal even pair and any antipodal odd pair dominate the entire graph. Each parity class contains four antipodal pairs, yielding \(4\cdot4=16\) sets.

If the vertices of \(E\) are at distance two, their open neighborhoods together cover six odd vertices, and the remaining two odd vertices must be precisely \(O\). Translation and coordinate permutation reduce this to \(E=\{0,3\}\), in which case \(O=\{13,14\}\). Their open neighborhoods miss precisely the two even vertices of \(E\), establishing sufficiency. There are \(8\cdot6/2=24\) even pairs at distance two, giving another 24 sets. In particular, this proves exhaustively that \(|\mathcal D|=40\). The two classes are isometry orbits.

**2. All pair and triple traces.** By translation and coordinate permutation, ordered vertex pairs have one orbit for each distance \(d=1,2,3,4\). Enumerating the preceding two types of dominating set gives the following exact number of concepts producing each pair trace, in order \((00,01,10,11)\):

| Pair distance | Number of unordered pairs | Four trace multiplicities |
|---|---:|---|
| 1 | 32 | \((21,9,9,1)\) |
| 2 | 48 | \((21,9,9,1)\) |
| 3 | 32 | \((24,6,6,4)\) |
| 4 | 8 | \((24,6,6,4)\) |

Every entry is positive, so every pair is shattered.

Similarly, translation followed by coordinate permutations maps two unordered triples to one another exactly when the sorted list of their three pairwise distances agrees. Indeed, after translating one point to zero, the weights of the other two and their intersection size are determined by the three distances; a coordinate permutation then identifies the pairs. The six possible distance types exhaust \(\binom{16}{3}=560\) triples. The next table gives representatives \((u,v,w)\), the number of such unordered triples, the eight trace multiplicities in the order \((000,001,010,011,100,101,110,111)\), and the unique absent trace for each representative.

| Distances | Representative | Count | Eight trace multiplicities | Absent trace |
|---|---|---:|---|---|
| \((1,1,2)\) | \((0,1,2)\) | 96 | \((13,8,8,1,8,1,1,0)\) | \((1,1,1)\) |
| \((1,2,3)\) | \((0,1,6)\) | 192 | \((16,5,5,4,8,1,1,0)\) | \((1,1,1)\) |
| \((1,3,4)\) | \((0,1,14)\) | 64 | \((18,3,6,3,6,3,0,1)\) | \((1,1,0)\) |
| \((2,2,2)\) | \((0,3,5)\) | 64 | \((13,8,8,1,8,1,1,0)\) | \((1,1,1)\) |
| \((2,2,4)\) | \((0,3,12)\) | 48 | \((16,5,5,4,8,1,1,0)\) | \((1,1,1)\) |
| \((2,3,3)\) | \((0,3,13)\) | 96 | \((18,3,6,3,6,3,0,1)\) | \((1,1,0)\) |

Every row is obtained by substituting the sixteen antipodal-pair sets and twenty-four distance-two even-pair sets from Part 1 and testing the three representative vertices. This is an exhaustive six-case finite calculation, independently reproduced by both standalone verification programs. Exactly one of eight trace counts vanishes in every row; four rows totaling 400 triples omit the all-positive trace, and two rows totaling 160 triples omit a pattern with two positives. Therefore no triple is shattered. Downward closure of shattering then excludes all larger supports. The polynomial and static dimension follow.

**3. Sharp adaptive dimension.** Each vertex lies in ten members of \(\mathcal D\), by symmetry and the count \(40\cdot4/16=10\). Fix a vertex \(u\). The pair table shows that, after a positive answer at \(u\), testing any different vertex \(v\) divides the ten remaining concepts as \((1,9)\) when \(d(u,v)\le2\), or \((4,6)\) when \(d(u,v)\ge3\). In the latter case, the four concepts containing both \(u\) and \(v\) have four pairwise disjoint two-element remainders after deleting \(u,v\). This is checked directly from the two structural types in Part 1; by isometry it suffices to use \((u,v)=(0,7)\) and \((0,15)\), whose remainders are respectively

\[
\{8,15\},\{9,14\},\{10,13\},\{11,12\}
\]

and

\[
\{1,14\},\{2,13\},\{4,11\},\{7,8\}.
\]

Consequently every nonconstant next query on this four-concept branch has a child of size at most one, so that branch has adaptive dimension at most one. A \((1,9)\) branch likewise has a singleton child. No query of the ten-concept class conditioned on \(u\) positive can have both children of adaptive dimension two; therefore the positive-conditioned class has adaptive dimension at most two. Any depth-four tree for the full class would, on its positive root branch, require adaptive depth three, a contradiction. Thus \(\operatorname{Ldim}(\mathcal D)\le3\).

For the converse, query vertex 0 first. After a positive answer, query 7; if this second answer is positive query 8, and otherwise query 1. After a negative answer at vertex 0, query 1, followed in either case by vertex 2. This is a full depth-three tree. The following concepts witness its eight leaf paths, in their displayed order of the three answers:

| Query answers | Witness dominating set |
|---|---|
| \((0^+,7^+,8^+)\) | \(\{0,7,8,15\}\) |
| \((0^+,7^+,8^-)\) | \(\{0,7,9,14\}\) |
| \((0^+,7^-,1^+)\) | \(\{0,1,14,15\}\) |
| \((0^+,7^-,1^-)\) | \(\{0,2,13,15\}\) |
| \((0^-,1^+,2^+)\) | \(\{1,2,12,15\}\) |
| \((0^-,1^+,2^-)\) | \(\{1,3,12,14\}\) |
| \((0^-,1^-,2^+)\) | \(\{2,3,12,13\}\) |
| \((0^-,1^-,2^-)\) | \(\{3,4,8,15\}\) |

Every witness is a four-vertex dominating set, as verified by Part 1. Hence \(\operatorname{Ldim}(\mathcal D)\ge3\), completing the equality.

**4. Shattering topology.** The shattered-support complex consists of all 16 vertices and all \(\binom{16}{2}=120\) edges, and has no higher faces. It is the connected graph \(K_{16}\); collapsing a spanning tree yields a wedge of \(120-16+1=105\) circles. This identifies its integral reduced homology, not merely its mod-two ranks.

## Verification

Two standalone and independently implemented direct enumerators are embedded with this result. Execute `python3 verify_python.py`, and separately `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp`. Each starts from the graph adjacency rule and exhaustively checks all 65,536 candidate vertex sets up to the discovered optimum; neither imports a precomputed list. Both obtain 40 optimum sets, the 16/24 split, the pair-trace distributions, the six triple categories and the adaptive dimension three. The C++ program has 28,409 memoized online-learning states. The Python program independently tests the eight adaptive witness leaves. Recorded successful output is included. The mathematical proof above does not treat a finite sample as proof of an infinite assertion: the universe itself has exactly 16 vertices and the enumerations are exhaustive.

## Relationship to prior work

The 2020 preprint of Adler, Benediktsson and Macpherson investigates VC dimension and density for **open-neighborhood** concepts of Johnson and Hamming graphs; its Hamming Theorems 4.6–4.8 do not consider membership in minimum dominating sets. The 2019 paper by Griggs treats hypercube domination and connected dominating sets, not traces or Littlestone dimension of all optimum dominating sets. The 2000 paper of Östergård and Weakley classifies small optimal binary covering codes, a stronger prior source relevant to the optimizer classification: the count and structural orbit description are **not** asserted as new independently of that classification. The new claim here concerns the uniform seven-of-eight triple trace law and sharp adaptive-versus-static gap for their **entire** optimum concept family; those learning properties were not located in the materials actually accessible. The original 2000 full text could not be inspected, so historical priority for an equivalent trace computation remains unsettled. Related published finite-graph domination-shattering results for other graphs address different query systems.

## Limitations

This result is confined to \(Q_4\). It does not classify minimum dominating sets of larger binary cubes, establish asymptotic VC or Littlestone dimensions, or establish independence from all unindexed previous computations. The radius-one covering-code family and its two isometry types may already be known as objects; novelty is claimed only for the explicit learning/tracing assertions under the literature comparison stated above. The 2000 covering-code classification is a material priority risk because its full text was inaccessible; its abstract verifies scope but not the absence of additional trace or online-learning statements.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (first public 2020-07-31), https://arxiv.org/pdf/2007.16042. In particular Sections 2 and 4 and Theorems 4.6–4.8.
2. J. R. Griggs, *Spanning Trees and Domination in Hypercubes*, arXiv:1905.13292v1 (first public 2019-05-30), https://arxiv.org/pdf/1905.13292.
3. P. R. J. Östergård and W. D. Weakley, *Classification of binary covering codes*, J. Combin. Designs 8 (2000), 391–401, DOI: 10.1002/1520-6610(2000)8:6<391::AID-JCD1>3.0.CO;2-R (abstract and public bibliographic material inspected; full text not accessed).
4. W. D. Weakley, *Optimal binary covering codes of length powers of two*, J. Combin. Designs 14 (2006), 1–13, DOI:10.1002/jcd.20081 (abstract inspected).
