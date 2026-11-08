# Maximal edge-open-packing sets in once-subdivided complete graphs

## Finding

Let \(n\ge 3\), and let \(S(K_n)\) be obtained by replacing every edge \(\{i,j\}\) of the labeled complete graph on \([n]\) by a path of length two, through a new vertex \(s_{ij}\). An *edge-open-packing set* is a nonempty edge set containing no two distinct edges that are the first and third edges of a three-edge path, or two edges of a triangle. It is *inclusion-maximal* if no additional graph edge can be inserted while preserving this property. Define
\[
M_n(z)=\sum_{F\text{ inclusion-maximal edge-open-packing}}z^{|F|}.
\]

Identify each edge \(i s_{ij}\) of the subdivision with the directed arc \(i\to j\). Every maximal edge-open-packing set is uniquely one of the following:

1. A collection of vertex-disjoint reciprocal pairs \(i\leftrightarrow j\) covering all \(n\) old vertices, if \(n\) is even, or all but exactly one old vertex, if \(n\) is odd.
2. A collection of \(c\ge0\) vertex-disjoint reciprocal pairs, together with **all** the arcs \(a\to u\) from a nonempty source set \(A\) to a nonempty target set \(U\), where the reciprocal-pair vertices, \(A\), and \(U\) partition \([n]\), and \((|A|,|U|)\ne(1,1)\).

In particular, writing \(a=|A|\) and \(u=|U|\), the complete enumerator is
\[
\boxed{\displaystyle
M_n(z)=\frac{n!}{2^{\lfloor n/2\rfloor}\lfloor n/2\rfloor!}
 z^{2\lfloor n/2\rfloor}
+\sum_{c=0}^{\lfloor(n-2)/2\rfloor}
\ \sum_{\substack{a,u\ge1\\a+u=n-2c\\(a,u)\ne(1,1)}}
\frac{n!}{2^c c!a!u!}\,z^{2c+au}.}
\]
The first summand counts the perfect or near-perfect reciprocal pairing; the second counts the complete source-to-target configurations, without overlap.

The smallest and largest possible maximal-packing cardinalities are exactly
\[
\boxed{\min_F |F|=n-1,\qquad \max_F|F|=\left\lfloor\frac{n^2}{4}\right\rfloor.}
\]
The *entire* cardinality spectrum is the set of exponents appearing in the displayed polynomial (equivalently, use \(2c+au=n-1+(a-1)(u-1)\) in the second family). For odd \(n\), every inclusion-maximal packing has even cardinality. For instance, when \(n=8\), the possible cardinalities are \(7,8,10,11,12,15,16\).

## Assumptions and scope

The graph is finite, simple, and undirected before subdivision; the original \(n\) vertices are distinctly labeled; every original edge is subdivided *once*. The edge-open-packing definition forbids the distinct outer edges of a path on four distinct vertices or of a triangle; edges of a star with common center need not conflict. The polynomial counts labeled edge sets, not isomorphism classes. Results hold for every integer \(n\ge3\); the finite verification covers only stated small cases.

## Proof

**Incidence-arc criterion.** The edges of \(S(K_n)\) are exactly \(i s_{ij}\), represented as arcs \(i\to j\) for ordered distinct \(i,j\in[n]\). The subdivision is bipartite, so has no triangles. For two distinct chosen arcs \(i\to j\) and \(k\to\ell\): if they have the same source, they share the original vertex; if they are reciprocal, their corresponding graph edges share a subdivision vertex. In either case there is no three-edge path with these as the two outer edges. Otherwise their graph edges are disjoint. A third graph edge joins an endpoint of one to an endpoint of the other precisely when \(j=k\) or \(\ell=i\). Thus two nonreciprocal arcs conflict exactly when they form a directed walk of length two with three distinct vertices. This is an if-and-only-if characterization of edge-open-packing feasibility.

**Decomposition.** Suppose \(i\to j\) and \(j\to k\) are both chosen. The criterion forces \(k=i\), yielding a reciprocal pair. No third arc can enter or leave either of these two vertices: it would make a forbidden nonreciprocal directed two-step walk with one of the pair's arcs. Thus reciprocal pairs are vertex-disjoint and isolated from all other chosen arcs. Remove their vertices. Among the remaining vertices, none can have both positive indegree and positive outdegree, as this would give a forbidden directed two-step walk; hence the remaining chosen arcs run from a set \(A\) of sources to a disjoint set \(U\) of targets, with possibly unused vertices.

**Maximality.** If there is any source, each unused vertex can be reached by an additional arc from a source, and every missing arc from an existing source to an existing target can likewise be added. Therefore a maximal packing with at least one nonreciprocal arc has no unused vertices and contains the full directed complete bipartite block \(A\to U\), with \(A,U\ne\varnothing\). Such a block and the isolated reciprocal pairs are always feasible by the incidence-arc criterion.

For a full block \(A\to U\), an additional arc touching a reciprocal-pair vertex conflicts with that pair. A new arc within \(A\) would make a forbidden directed walk into \(U\); a new arc within \(U\) would make one from \(A\). A reverse arc \(u\to a\), with \(u\in U\) and \(a\in A\), makes a forbidden two-step walk if \(|U|\ge2\) (through \(a\) into another target) or if \(|A|\ge2\) (from another source through \(u\)). If \(|A|=|U|=1\), however, that reverse arc is legal and completes a reciprocal pair. Hence precisely this one-by-one block is not maximal. If no nonreciprocal arc exists, the packing consists solely of disjoint reciprocal pairs, and can be extended whenever at least two old vertices are unused; with at most one unused vertex it is maximal. This exhausts both families and proves their disjointness and uniqueness.

**Counting.** With \(c\) reciprocal pairs, the number of ways to choose those unordered pairs and then disjoint ordered-labeled sets \(A,U\) of sizes \(a,u\), satisfying \(2c+a+u=n\), is
\[
\frac{n!}{2^c c!\,a!\,u!}.
\]
Each choice gives a distinct maximal packing of \(2c+au\) incidence edges. With no block, a perfect or near-perfect pairing has \(n!/(2^{\lfloor n/2\rfloor}\lfloor n/2\rfloor!)\) choices and \(2\lfloor n/2\rfloor\) incidence edges. These counts give the polynomial.

**Extrema and parity.** In the block family \(n=2c+a+u\) and
\[
2c+au=n-1+(a-1)(u-1)\ge n-1.
\]
The pairing-only family has size \(n\) when \(n\) is even, and \(n-1\) when odd. A block with \(c=0\), \(a=1\), \(u=n-1\) attains \(n-1\). For the maximum, \(au\le(n-2c)^2/4\), and
\[
\frac{n^2}{4}-\left(2c+\frac{(n-2c)^2}{4}\right)=c(n-c-2)\ge0
\]
because \(0\le c\le(n-2)/2\). The pairing-only sizes are also at most \(\lfloor n^2/4\rfloor\) for \(n\ge3\). Taking \(c=0\) and a balanced bipartition \((a,u)=(\lfloor n/2\rfloor,\lceil n/2\rceil)\) attains the bound. When \(n\) is odd, \(a+u=n-2c\) is odd, so \(a,u\) have opposite parity, and \((a-1)(u-1)\) is even. The pairing-only size \(n-1\) is likewise even. The remaining spectrum assertions follow directly.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The checker constructs the subdivision graph from scratch, independently tests every possible connecting third edge, enumerates every candidate subset for orders \(n=2,3,4,5\), and compares the exact maximal-set families and every polynomial coefficient. For \(2\le n\le8\), it generates every configuration in the theorem, verifies their cardinalities and coefficients, and independently tests each generated configuration for pairwise feasibility and one-edge maximality. On the tested version it prints:

`VERIFY_OK raw_bridge_conflicts=PASS exact_families_n2_to5=PASS maximal_generated_n2_to8=PASS subset_masks= 1052740 exhaustive_maximal= 132 generated= 6945`

Enumeration at finitely many orders does not prove the universal result; the preceding argument supplies the proof. In particular, maximality is tested by adding individual edges, which is sufficient because edge-open-packing feasibility is hereditary under deleting chosen edges.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan (2022) introduced edge-open-packing sets and determined maximum sizes for several standard families, including complete multipartite graphs, but not this full maximal-set distribution of once-subdivided complete graphs. Brešar and Samadi (first publicly posted March 1, 2024) established complexity, tree algorithms, and structural bounds for the same invariant, without the present enumeration in the inspected full text. Earlier injective-edge-coloring results motivate the object; enumerating inclusion-maximal single color classes is different from determining a minimum number of colors in a coloring. The argument here uses the standard definition and proves the new full structural classification and labeled enumerator directly.

## Limitations

The formulas apply only to one subdivision of **every** edge of a complete graph. They do not classify analogous configurations for arbitrary base graphs, multiple subdivision lengths, or weighted edge-open-packings. Publication priority is subject to later discovery of equivalent, stronger, or unindexed results. The directly related injective-edge-coloring work of Priyamvada and Panda on graph operations, including subdivision, was available only by abstract during comparison, so this source remains a specific residual priority risk. The included computational tests certify only the finite ranges reported; no independent mathematical audit is claimed.

## References

1. G. Chelladurai, K. Kalimuthu, S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO—Operations Research* **56** (2022), 3765–3776. DOI: `10.1051/ro/2022171`. Open article: https://www.numdam.org/articles/10.1051/ro/2022171/ .
2. B. Brešar, B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:`2403.00750` (first submitted 2024-03-01), https://arxiv.org/abs/2403.00750 .
3. Priyamvada and B. S. Panda, “Injective edge coloring of some standard graph products,” *Discrete Mathematics, Algorithms and Applications*, DOI: `10.1142/S1793830923500416`. Only abstract-level material inspected.
