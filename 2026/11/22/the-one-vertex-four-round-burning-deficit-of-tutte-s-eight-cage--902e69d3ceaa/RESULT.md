# The one-vertex four-round burning deficit of Tutte's eight-cage

## Finding

Let \(T\) be the thirty-vertex Tutte–Coxeter graph, with the labelled duad–syntheme construction below. For an ordered four-tuple \(\mathbf{x}=(x_1,x_2,x_3,x_4)\) of vertices, define its four-round coverage by
\[
F(\mathbf{x})=B_3(x_1)\cup B_2(x_2)\cup B_1(x_3)\cup B_0(x_4),
\]
where \(B_r(v)=\{w:d_T(v,w)\leq r\}\). This permits arbitrary tuples, including ones that would not be legal successive ignitions.

**Theorem.** Over all \(30^4=810{,}000\) ordered four-tuples, the maximum of \(|F(\mathbf{x})|\) is exactly \(29\). Exactly \(2{,}160\) tuples attain it, and every attaining tuple is a legal four-step sequence of distinct, previously unburned ignition sources. For each initial source \(x_1\), exactly \(72\) optimal four-round partial schedules exist. Each leaves one unburned vertex \(u\), necessarily at distance four from \(x_1\); for every one of the \(30\cdot8=240\) ordered source–survivor pairs at distance four, there are exactly nine attaining schedules. Of all attaining schedules, \(720\) have \(d_T(x_1,x_2)=2\) and \(1{,}440\) have \(d_T(x_1,x_2)=4\). Consequently the ordinary graph burning number is \(b(T)=5\).

The distinction is between an **optimal four-round partial schedule**, which burns 29 vertices, and a **burning sequence**, which burns all 30 vertices. There are no four-round burning sequences on \(T\).

## Assumptions and scope

Take a fixed six-element label set \(\{0,1,2,3,4,5\}\). A **duad** is a two-element subset of this set; a **syntheme** is a partition of the six elements into three duads. The bipartite graph \(T\) has all fifteen duads and all fifteen synthemes as vertices, with a duad adjacent to exactly those synthemes containing it. Thus \(T\) is the incidence graph of the Cremona–Richmond generalized quadrangle of order two, also called the Tutte–Coxeter eight-cage. The vertices are labelled, and all ordered schedules are counted by their actual vertex identities (not modulo symmetry).

In the ordinary synchronous burning process, a new unburned vertex may be ignited at each round, while fire spreads one graph edge per round. A tuple of length \(k\) is a legal choice of ignition sources if \(d_T(x_i,x_j)\geq j-i\) whenever \(1\leq i<j\leq k\). It burns every vertex after \(k\) rounds if and only if \(\bigcup_i B_{k-i}(x_i)=V(T)\). These are the standard source-distance and ball-cover conditions; no altered burning rule or reconfiguration operation is assumed.

## Proof

**1. Distance geometry and the unavoidable survivor.** Fix any vertex \(a\). The incidence construction gives the shell sizes
\[
\bigl(|S_0(a)|,|S_1(a)|,|S_2(a)|,|S_3(a)|,|S_4(a)|\bigr)=(1,3,6,12,8),
\]
with \(S_r(a)=\{v:d_T(a,v)=r\}\), and no vertices at larger distance. The graph is bipartite, cubic and has girth eight. Its layer transitions have one predecessor and two successors at each of distances one, two and three, and three predecessors at distance four. In particular, for any \(z\) with \(d_T(a,z)\) respectively \(0,1,2,3,4\), the ordered pair
\[
\bigl(|B_2(z)\cap S_4(a)|,\ |B_1(z)\cap S_4(a)|\bigr)
\]
is respectively \((0,0),(0,0),(4,0),(2,2),(4,1)\). This follows directly by counting the successors from each distance layer, with no identifications inside a two-step extension because the girth is eight; the same table is also checked for every ordered pair by the standalone verifier.

For any four sources, the first radius-three ball misses the eight vertices of \(S_4(x_1)\). The second radius-two ball covers at most four of these eight; the third radius-one ball covers at most two; and the fourth singleton covers at most one. Thus at least \(8-4-2-1=1\) vertex survives. This bound holds **without imposing** legality on the sources and proves the impossibility of four-round burning.

**2. Exact attaining schedules from a duad first source.** By permutation of the six labels, assume \(x_1=\{0,1\}\), and put \(R=\{2,3,4,5\}\). The eight distant duads are precisely
\[
S_4(x_1)=\{\{0,t\},\{1,t\}:t\in R\}.
\]
To leave just one of these, the second radius-two ball must cover four, the third radius-one ball must cover two **new** distant duads, and the fourth source must be one of the two distant duads left after the third move.

There are two possibilities for the second source.

* At distance two, \(x_2=\{a,b\}\) with \(a,b\in R\), \(a\ne b\). There are six choices. After the second ball, the four distant duads still unburned are \(\{0,a\},\{1,a\},\{0,b\},\{1,b\}\). Exactly two synthemes contain a pair of disjoint duads from this four-set: one contains \(\{0,a\},\{1,b\}\), the other \(\{0,b\},\{1,a\}\). Each syntheme supplies a third source covering exactly two of the four, leaving two choices for the final distant duad. This contributes \(6\cdot2\cdot2=24\) schedules for fixed \(x_1\).

* At distance four, \(x_2\) is one of the eight duads sharing exactly one label with \(\{0,1\}\). Suppose \(x_2=\{0,a\}\), where \(a\in R\); the other orientation is symmetric. After the second ball the four distant duads still unburned are \(\{1,a\}\) and \(\{0,b\}\) for \(b\in R\setminus\{a\}\). A third-source syntheme must contain \(\{1,a\}\) together with one of these three \(\{0,b\}\), and there are exactly three such synthemes. There are again two choices for the last distant duad. This contributes \(8\cdot3\cdot2=48\) schedules.

If \(d_T(x_1,x_2)\) is zero, one or three, its radius-two ball covers at most two of the distant eight, so the four-round coverage cannot reach 29. In either successful case, no point vertex can serve as the third source and cover two new distant duads, since a radius-one ball about a duad contains only that one duad in the point bipartition. All listed choices are legal: the third syntheme lies at distance three from \(x_1\); the fourth duad lies at distance four from \(x_1\), is nonincident with the third syntheme, and has distance four from the second duad. Consequently all required source-separation inequalities hold.

For each duad first source, the exact number is \(24+48=72\), with the second-source distance split stated in the theorem. The stabilizer of the first duad, which swaps its two labels and permutes the other four, acts transitively on its eight distance-four duads. The \(72\) schedules are therefore distributed uniformly over their unique survivors, nine per survivor.

**3. Syntheme first sources and total count.** The incidence configuration is self-dual: an incidence-preserving involution interchanges its duad and syntheme sides. An explicit thirty-entry involution for the lexicographic labelling in the included Python checker is
\[
(15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,0,9,14,11,7,2,12,1,8,4,6,10,5,3,13).
\]
The checker verifies both involutivity and preservation of all forty-five edges. Together with arbitrary permutations of the six base labels, this establishes vertex transitivity. Hence every first source, including any syntheme, has precisely \(72\) attaining schedules with the same one-survivor and second-source-distance properties. Summing over all thirty sources gives \(30\cdot72=2{,}160\) schedules, divided as \(30\cdot24=720\) and \(30\cdot48=1{,}440\). Each of the \(30\cdot8\) ordered antipodal source–survivor pairs has nine schedules.

**4. Five rounds suffice.** Every vertex has eccentricity four. More concretely, the five duads
\[
\{0,1\},\ \{0,2\},\ \{0,3\},\ \{0,4\},\ \{0,5\}
\]
are pairwise at graph distance four. Igniting them in that order is legal, and the radius-four ball around the first source alone covers the graph after five rounds. Combined with the four-round obstruction, this proves \(b(T)=5\).

## Verification

Two standalone, independently written programs are provided: `verify_python.py` (Python standard library) and `verify_cpp.cpp` (C++17). Both construct all fifteen duads and fifteen synthemes without external graph packages, recompute all thirty breadth-first-search distance rows and the four source-radius masks, and enumerate all \(30^4=810{,}000\) four-tuples without symmetry reduction. Both return maximum coverage 29; exactly 2,160 maximizers; a second-source split of 720 at distance two and 1,440 at distance four; 72 maximizers per first source; nine per ordered distance-four initial-source/survivor pair; and zero maximizers violating the strict source legality conditions. Python additionally verifies the five-source construction, the intersection table for all 900 vertex pairs and a point–line duality automorphism.

Reproduction commands from the extracted files are `python3 verify_python.py`, followed by `g++ -std=c++17 -O2 verify_cpp.cpp -o check_cpp && ./check_cpp`. Neither program requires network access. Finite enumeration checks the exact labelled thirty-vertex instance; the mathematical proof above supplies the structural reason for the one-vertex deficit and the local counts.

## Relationship to prior work

Bonato, Janssen and Roshanbin introduced ordinary graph burning in their 2014 conference paper and gave the foundational neighborhood-cover viewpoint. Their subsequent 2015 arXiv preprint of *How to Burn a Graph* states the complete source-distance characterization and the universal radius-plus-one upper bound. The present finding uses these definitions and does not claim them as new. Bonato's 2020 survey discusses burning bounds, graph products, circulants, generalized Petersen graphs and related graph families. The 2015 mathematical account of the Tutte–Coxeter graph by Baez explains the classical duad–syntheme model and its self-duality; that construction is likewise not new.

The asserted new contribution is the sharp **one-survivor** four-round coverage theorem for this thirty-vertex cage and the complete count and antipodal stratification of every attaining four-source schedule, not the abstract definition of graph burning, the distance-regular structure or the radius bound. Searches of mathematical findings and external literature for this exact cage, its generalized-quadrangle alias, four-round schedules, and possible stronger burning classifications found related but non-implying results on cycles, circulant graphs, and other cubic graph families. Those negative searches do not establish absolute priority.

## Limitations

The theorem is specific to the uniquely defined Tutte–Coxeter graph, not a statement about all cubic cages, all generalized quadrangles or all distance-regular graphs. The near-complete schedules are not genuine shortest burning sequences, since each still leaves one vertex unburned; genuine shortest burning sequences require five rounds. The exact finite count is established by the structural case split and verified by complete enumeration, without extrapolating from a sample. Literature priority is assessed from accessible primary papers, survey text and indexed mathematical searches; inaccessible or unindexed historical computations could contain an equivalent result. No independent external audit has been performed.

## References

1. A. Bonato, J. Janssen and E. Roshanbin, *Burning a Graph as a Model of Social Contagion*, Algorithms and Models for the Web Graph (WAW 2014), LNCS 8882, pp. 13–22 (2014), DOI: `10.1007/978-3-319-13123-8_2`, https://math.ryerson.ca/~abonato/papers/BJR_WAW14_Sept12.pdf.
2. A. Bonato, J. Janssen and E. Roshanbin, *How to Burn a Graph*, initial arXiv posting 2015-07-23, `arXiv:1507.06524`, https://arxiv.org/abs/1507.06524.
3. A. Bonato, *A Survey of Graph Burning*, initial arXiv posting 2020-09-22, `arXiv:2009.10642`, https://arxiv.org/abs/2009.10642.
4. J. Baez, *Tutte–Coxeter Graph*, AMS Visual Insight, 2015-08-15, https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/.
