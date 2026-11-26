# Independent mathematical audit

## correctness

PASS

Square dihedral maps preserve the diagonal attack condition. In the barycentric subdivision each flag vertex has a distinct original-face size, and all eight symmetries preserve that size. If two points of a closed flag simplex are identified, their supports have the same sizes and use the same vertices within that flag, so their barycentric coordinates agree. Thus each cell closure embeds in the geometric orbit space, and deleting the i-th vertex contributes the sign (-1)^i; different deletions have different rank sets. This is not a naive face-orbit poset. A fresh coordinate enumeration independently found 728 nonempty faces, 158328 nonempty flags and quotient-cell counts (100,1210,4530,7260,5280,1440). The integral unreduced boundaries square to zero. A different valid free-face sequence removes 8963 pairs and leaves (70,479,877,468,0,0) cells; each upper cell was maximal and each removed facet had that sole remaining coface. Integral unit pivots split off isomorphism pairs in adjacent degrees, leaving chain ranks (1,0,2,3) and d3=[[-2,2,0],[2,-2,2]]. Its nonzero Smith factors are 2 and 2 from the entry gcd 2 and maximal-minor gcd 4. Hence reduced H2=(Z/2)^2 and H3=Z with all other reduced groups zero. Replay: python3 /workspace/branches/82c42184-13bc-411c-ae61-43f6fa62f47f/bishop4_independent.py --n 4; saved results in independent_run.txt in the same directory. The fresh computation does not replay the frozen collapse order or treat finite field ranks as a Smith certificate. For pi1, the two color classes have connected nonattacking-pair graphs (both with 8 reached vertices); attack preserves color, so their join is simply connected. Transpose fixes (0,0), and row reversal fixes the midpoint of the allowed edge {(0,0),(3,0)}. The two reflections generate D4, so the fixed-point normal subgroup in the finite-group orbit-space theorem is all of D4. The frozen verifier and recorded results were inspected but not executed. Nothing here computes the full homotopy type.

## originality

PASS

The exact new invariant under comparison is for the ordinary full-square D4 quotient of the four-by-four bishop complex, not for the unquotiented bishop complex or other pieces and actions. There is material indexed overlap in methods and the two-torsion phenomenon, but the strongest inspected exact analogues concern distinct attack rules or group actions. The identical record hit was not counted as prior independent evidence.

## value

PASS

The natural standard four-by-four board has an established simple absolute homotopy type, motivating the effect of quotienting by all its board symmetries. The result identifies precisely the integral obstruction that the quotient introduces, two independent order-two classes alongside a top free class, and determines simple connectivity. This is an exact reusable orbit invariant, not a known absolute recount or an inferred complete homotopy classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
