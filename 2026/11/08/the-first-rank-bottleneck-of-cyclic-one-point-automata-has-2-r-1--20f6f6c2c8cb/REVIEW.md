# Independent mathematical audit

## correctness

PASS

With t rotations elapsed, co-moving holes are obtained by translating the complement of the current image by −t. A b at time t is inert if 0 is missing, and otherwise adds the hole labeled t while deleting the existing label t−r, if present. Up to 2r rotations, n>2r means no timestamp alias and no other possible deletion. Each effective b reduces rank by exactly one and makes 0 absent, so j effective b's need at least j−1 intervening a's. At equality the unique string is alternating; its timestamps 0,…,j−1 have no distance-r pair for j≤r. For T<2r each class modulo r has at most two timestamps, and adding the second displaces the first or is inert. The count of holes stays at most r even when ineffective letters occur. Therefore the next threshold needs at least 2r a's and r+1 b's. At length 3r+1 every b must add a new hole without deleting any; equivalently all b times are distinct and avoid distance-r pairs. The conflict graph on times 0,…,2r has a path 0–r–2r and r−1 disjoint edges. A maximum independent set must use both endpoints of the path and exactly one endpoint per edge; in particular there are no unaccounted leading or trailing a's. This proves existence, the exact literal-word enumeration, and the gap r+2 also at n=2r+1, without a synchronization hypothesis.

## originality

PASS

No verified stronger result covers the exact first rank bottleneck and shortest literal-word census for this cyclic jump family. The examined same-family theorem gives terminal reset behavior; comparable early-rank and count theorems concern different generators, objectives or both.

## value

PASS

The rank threshold of a fixed alphabet is a natural exact invariant even for nonsynchronizing parameters. Beyond the elementary alternating lower bound, the timestamp argument explains the first non-linear cost and the shift from one literal optimizer to 2^(r−1), uniformly over the full cyclic family. It gives a meaningful explicit boundary and a complete optimizer classification not supplied by terminal reset bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
