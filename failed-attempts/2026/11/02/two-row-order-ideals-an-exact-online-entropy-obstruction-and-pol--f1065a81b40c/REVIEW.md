# Independent mathematical audit

## correctness

PASS

Ideals correspond bijectively to the triangular set of row lengths, and the width equals VC dimension since downward closure realizes all labels on an antichain. A cell query is a threshold cut on one coordinate. Both children of every proper cut are smaller interval-triangle states; the max of one plus the smaller child depth is necessary and sufficient by the two complete subtrees at the root. The endpoint count yields the claimed arithmetic complexity. An independent translated-state program, with separated product states evaluated directly, reproduced all 60 rows and ten thresholds. At n=7 the maximal smaller child among the fourteen possible first queries has size 15, too few for depth four, and a 4-by-4 product subfamily realizes depth four. The balanced product subfamily gives the all-size lower bound: for X=floor(n/2)+1, Y=ceil(n/2)+1, the concept count is less than 2XY, and rounding the two logarithms costs at most one additional bit.

## originality

FAIL

The October 26 Resultary record 6262182a47f2 is directly prior coverage of the same membership-query family, normalized four-bound recurrence, its complexity, and the identical ten jump thresholds. Its explicit lower and upper bounds also imply the two-bit inequality by the elementary rounding calculation, and its table implies exactly the first strict information-bound failure at seven columns. A direct first-query count is a different proof certificate, not a new obstruction.

## value

FAIL

The first online entropy obstruction is a natural mathematical boundary, but the frozen finding chiefly recomputes a known recurrence and threshold table. The residual branch census is an elementary direct certificate of an already determined value, and the two-bit form simply rounds already stated bounds; neither yields an independently useful new invariant or boundary in this claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
