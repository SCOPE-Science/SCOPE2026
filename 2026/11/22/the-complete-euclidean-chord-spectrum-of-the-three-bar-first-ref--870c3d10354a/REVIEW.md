# Independent mathematical audit

## correctness

PASS

Sections 4.1 and 4.3 of the primary construction use the direct one-line permutation vector, not positions of the labels. At n=3,k=1 the three copies of each bar must appear in local order and the three first copies must appear in bar order, giving exactly the stated eight precedences. The inclusion of all representatives as vertices follows also from equal squared norm 285: the functional x -> p·x is strictly maximized at p since it equals 285 minus half the squared distance on permutation vectors. The rooted-tree subtree sizes (9,2,1,6,2,1,3,2,1) give 280 linear extensions. A separate exact replay starting from the constraints generated each linear extension by its unique series of available-label choices and counted all 39060 unordered distinct pairs. It verified every one of the 75 CSV rows, support {2,4,...,146,150,152}, 15 pairs at 150, 45 at 152 with 90 distinct degree-one endpoints, 190 isolated vertices, and distance sum 2737080 giving 15206/217. The diameter of the convex hull is attained over vertex pairs, by expressing any two points as convex combinations and applying the triangle inequality to their difference. Thus it is 2 sqrt(38).

## originality

PASS

Pass for the complete Euclidean census of this particular direct-coordinate barcode polytope. The defining barcode paper provides the construction and one of the diametral witness vertices as a nested example, not the other endpoint or the pair census. Known one-skeleton diameters and structure do not determine this metric invariant. The strongest nearby indexed Euclidean diameter comparison is for zigzag Coxeter-element Bruhat intervals: its odd-order formula gives squared diameter 62 in the standard nine-entry embedding, incompatible with this instance's 152; it counts only farthest pairs in that distinct family. A full earlier census remains possible outside the inspected texts and summaries.

## value

PASS

The chosen object is the standard first midpoint refinement for three bars, where the three-way canonical precedence structure yields hundreds of vertices; neither the Euclidean embedding nor the finite cutoff is tuned to the numerical answer. The exact shell data and isolated missing near-diameter shell give benchmarks for geometric comparisons in that realization. In particular the matching on the outermost shell is a structural constraint not obtained from a graph diameter or from the vertex count. The distance thresholds can be used in any Euclidean vertex filtration on this model without pretending to compute its homology or the metric between actual barcodes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
