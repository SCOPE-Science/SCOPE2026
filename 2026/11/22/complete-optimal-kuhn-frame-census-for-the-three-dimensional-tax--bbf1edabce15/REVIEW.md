# Independent mathematical audit

## correctness

PASS

Independently embed R^3 into R^4 by taking dot products with (+++),(+--),(-+-),(--+). This is an l1-to-linf isometry onto the hyperplane with coordinate sum zero. If the vertex coordinate ranges are [l_i,u_i], a fitting center at radius r exists exactly when each interval [u_i-r,l_i+r] is nonempty and their product meets the hyperplane, i.e. the sum of lowers is <=0<= the sum of uppers. This verifies the exact opposite-pair and parity bounds without assuming the list of dual extreme points. Each nonempty column subset sum occurs as an edge in some ordering; integrality gives a width cutoff of 2 below 3/2 and 3 at 3/2, with parity-sum cutoffs of 5 and 6 respectively. An independent bounded sweep tested three orders per frame, the other three being central reflections of these tetrahedra in the packet midpoint. Below 3/2 there were 24 necessary independent candidates, all index 2, and none fit; the unit frame fits the radius-3/2 cube ball. At 3/2 the prefilter yielded 512/408/288/56 candidates at indices 1/2/3/4, and 512/408/0/8 passed. The separate orbit regeneration matched all 23 CSV rows including sizes and representatives. Replay: python3 -I /workspace/branches/independent-checks/record2.py; output at /workspace/branches/independent-checks/record2.log. Original checker was inspected, not executed.

## originality

PASS

Credit only the complete optimum-frame census, index-three exclusion, and orbit classification. The value 3/2 is already an exact specialization of Xue's formula, and Lian–Xue's determinant theorem already gives the index ceiling and an index-four optimizer. Neither determines the full equality set. No distinct indexed or inspected primary claim was found that gives or implies this census.

## value

PASS

The natural normalized octahedral Kuhn fitting problem already has an optimum and sharp determinant bound; the census answers the outstanding equality-set question. In particular, it proves a missing determinant class even while the next higher determinant occurs. The complete canonical table permits reuse in further exact geometry without rebuilding the enumeration. The point is not the prior numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
