# Independent mathematical audit

## correctness

PASS

In a finite unit-edge tree, any all-positive triple center projects to its tripod. If one support vertex is on the path between the others, a point equidistant from the ends projects to their midpoint and is strictly closer to the interior vertex. Otherwise a projection off the median at depth j on one arm forces the other arms to have equal length h and that arm to have length h+2j. The midpoint of the longer-arm/shorter-arm path is this same depth-j vertex; any center realizing the pair projects there, and its path to the third support vertex goes through the midpoint, forcing all three positive. Thus a shattered triple has equal arms h>0, and t=r−h>0 since t=0 allows only the median for pairs. An all-positive center needs a fourth branch reaching depth t. A singleton center must be in its own branch and, after projecting at depth j≥1, must travel off the arm by t+j; its other two distances are r+2j. Truncating this path from the median at depth t gives exactly the complementary pair, since it shares a positive initial segment with the omitted vertex's path. The median gives the empty trace. In a shattered quartet, two triples sharing a pair force a common midpoint and common h. Equal distances for all triples force four separate branches, and a center including a specified pair would have to include at least one of the other two. For the order bound, three arms, the fourth witness branch and the three off-arm spurs are disjoint away from their attachment points and give 1+3h+t+3(t+1)=3r+t+4≥3r+5. The given h=r−1 example realizes all traces using the median, its fourth leaf, the first vertex on each arm for pairs, and each length-two spur endpoint for singletons. At r=1 the tripod condition is impossible, and centers 1,5,3,2 of P_5 realize respectively only vertex 2, only vertex 4, both and neither. The supplied finite verifier was inspected, not executed; its recorded result does not prove the universal order bound.

## originality

PASS

The distinct same-day exact-distance-two record matches the r=2 specialization, including the eleven-vertex cutoff; no priority ordering is inferred from the date. The frozen record expressly excludes that special case from its new contribution. This pass is for the general fixed-integer-radius tripod criterion and sharp all-radius bound, in particular the regime r≥3 not treated in the same-day comparison.

## value

PASS

The theorem gives an all-radius structural description of the trace set of a natural distance predicate. It identifies which branching resources are needed, not merely that shattering is bounded; those resources give the sharp minimum order and a matching witness for each r≥2. The explicit bound and classification for r≥3 extend beyond a known finite special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
