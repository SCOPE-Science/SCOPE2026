# Independent mathematical audit

## correctness

PASS

The uncovered point and line sets must be incidence-free. Three points meet at least nine lines, so leaving three points uncovered cannot coexist with at least five uncovered lines. This excludes size at most six and forces exactly two uncovered points at size seven. Exactly seven lines meet that pair, so each is covered once, as is each other point; every optimum is a matching. The common line's flag is forced. The two remaining triples of lines meet across directions except for the three parallel pairs. Their cross-incidence graph is K(3,3) minus a perfect matching, whose subdivision by the six off-line points is a twelve-cycle with exactly two perfect matchings. Conversely those two matchings extended by the forced flag dominate, because the uncovered sets are incidence-free. A separate exhaustive run used the four line-coordinate maps x, y, x+y, x−y over F3 and the union of closed flag neighborhoods as the domination test. It tested all subsets of sizes 0–7, including all 8,347,680 of size seven. It found no smaller sets and precisely 72 at size seven, with two for each omitted point pair. Pairwise intersections of sizes 0, 1, 2, 3 occurred 612, 900, 756, 288 times with none larger, and every source had zero unreached vertices and distance levels (1,8,32,28,3) in the four-exchange graph. This reproduces the sharp threshold, size, degree and diameter.

## originality

PASS

A known design bound already yields the lower bound seven, and the minimum maximal matching interpretation is classical. The surviving contribution is the classification of every minimum edge-dominating set and the sharp exchange structure for those configurations. The closest same-graph result uses vertex domination, not edge domination.

## value

PASS

This is a natural small affine plane on which the general lower bound is sharp. The omitted-pair/twelve-cycle description organizes the entire optimum family, and the first nonzero batch mobility immediately permits global connectivity. The complete overlap and distance data provide a reproducible benchmark for reconfiguration among minimum maximal matchings, not merely another low-order scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
