# Independent mathematical audit

## correctness

PASS

For the defined simple cubic GP(10,2), a block is eligible exactly when it is independent and no outside vertex has two neighbors in it. The least-uncovered-vertex recurrence counts partitions of fixed vertices without ordering the blocks. A separately written exhaustive implementation reproduced the polynomial 1+20t+100t^2+120t^3+90t^4+10t^6, no four-block partition, and 212 five-block partitions with the three profiles 60, 100 and 52. At most three blocks cannot cover 20 vertices (each block has size at most six). Exactly two five-block partitions are square colorings. Independently, fixing the colors on the even inner pentagon as 0,...,4, the even outer vertices at 2a are restricted to a±2 mod 5. The distance-two constraints around this outer five-cycle force a constant choice of sign. The odd outer vertices are then forced by their two adjacent even outer and two distance-two even inner vertices; their colors are a+4 for the plus sign and a+2 for the minus sign at 2a+1. The odd inner colors are then forced to a+1 and a, respectively. Both assignments satisfy the constraints. The modulo-five quotient is locally bijective, so counts of each neighbor color pull back; Petersen has minimum six, independently reproduced. Thus the decrease is strict and 210 of the 212 optimal partitions fail to color the square.

## originality

PASS

Passes for the dodecahedral invariant and enumerative refinement and the specific strict covering example, not for the Petersen value or the general implication from square coloring. Crediting the exact Petersen theorem sharpens the citation without changing the finding.

## value

PASS

For a canonical cubic planar graph, the census makes the distinction between two natural coloring constraints measurable even when their minimum color numbers coincide. The 210-versus-two split and size profiles, together with a strict covering example, are useful exact data not inferred from the generic bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
