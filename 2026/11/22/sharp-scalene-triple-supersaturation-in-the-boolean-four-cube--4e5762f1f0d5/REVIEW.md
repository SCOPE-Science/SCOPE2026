# Independent mathematical audit

## correctness

PASS

Independently replayed every subset using literal 4-tuples and a mixed-parity vertex tally, not the frozen highest-index recurrence or its triple mask list. Same-parity distances squared are 2,4 and opposite-parity distances squared are 1,3. Thus for a vertex v alone on its parity side of a triple, the number of scalene choices from the other side is d·(b−d) with d selected cube neighbors and b total selected opposite-parity vertices. Summing over either parity for v counts each scalene triple once. /workspace/reviews/cube_replay.py checked all 65,536 distinct subsets using this identity, yielding all minima and counts and testing the equality predicate in both directions for every subset of size at least six. For k=6,…,16 the pairs (minimum,count) were (0,56),(0,16),(0,2),(16,16),(36,48),(60,64),(88,32),(124,64),(164,48),(208,16),(256,1). In a full-parity construction an opposite vertex has four neighbors and four nonneighbors; a selected opposite pair has complementary neighborhoods if antipodal, and neighborhoods with intersection two if at distance two. This independently yields 16r+4 choose(r,2)+4 times the pair count. The four disjoint antipodal pairs minimize it at max(0,r−4). The proof and replay do not classify k≤5 or extend outside Q4. The frozen checker is consistent with this replay; its stated Python 3.8 minimum in RESULT.md is a nonmathematical documentation slip, since int.bit_count requires Python 3.10 or later.

## originality

PASS

The supported distinct claim is the exact offending-triple profile plus all equality cases in the four-cube, not the use of parity or the general question of isosceles Hamming sets.

## value

PASS

In the four-cube the antipodal matching is within each parity class (unlike in the three-cube), producing the additional scalene pattern (1,3,4) and a change of minimizer structure after four opposite vertices. The exact profile quantifies how quickly isosceles avoidance fails and gives concrete equality cases, not merely a small-instance count or an unmotivated particular size. The finite certificate is sufficient for this natural finite problem, not evidence for a higher-dimensional generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
