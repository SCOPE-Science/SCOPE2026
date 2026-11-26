# Independent mathematical audit

## correctness

PASS

For any query the positive branch in the full class is a translate of the centers of weight at most two. Within that branch, weights zero and above four are constant and weights three and four have at most six positive centers. For an intersection with a second ball centered at weight one, parameterize the centers by a free distinguished bit and at most one outsider. Queries with two or three outsiders have five or three positive centers; queries with one outsider have a negative branch in a translated star. For a second ball centered at weight two, the centers are arbitrary subsets of the two distinguished bits with no outsider, or exactly one distinguished bit with one outsider. Queries with zero or two distinguished bits have at most five positives when they split, while queries with one distinguished bit and zero or one outsider have star negative branches; with two or three outsiders they have at most three positives. A splitting query on a star has at most three positives, so stars have dimension at most two. These bounds yield depths at most three on the double intersections, four on a ball, and five on the full class. In d=3 and d=4 the negative root branch has 1 and 5 centers; in d=5 the 16-center positive root branch admits no 8/8 cut (intersection sizes 16,10,10,6,6,0). Independent verification checked all 58 certificate paths for depths 1,3,4,5 in dimensions 3,4,5,6; zero-padding proves all larger lower bounds. Distinctness and label consistency were both checked.

## originality

FAIL

The entire submitted invariant is demonstrably covered by a distinct indexed classification, Resultary 31d57fbe632c: projecting its exact VC/Littlestone table to the Littlestone coordinate gives precisely this theorem on the same class in every dimension. Its proof also uses the same double-intersection and translated-star upper-bound structure. The indexed comparison has a later record date; this establishes equivalent existing coverage and lack of distinct theorem content against the current catalogue, not that the frozen finding was predated, copied, or that either entry has proved historical priority.

## value

PASS

On its mathematical merits this is an exact adaptive-learning classification of a natural metric class, not just a finite table: it identifies where five mistakes first become necessary and why no larger ambient cube increases the bound. The dimension-free upper bound via stars and the sharp finite witnesses are useful structural facts. Whether the submission contributes distinct content against the catalogue is the separate failed originality assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
