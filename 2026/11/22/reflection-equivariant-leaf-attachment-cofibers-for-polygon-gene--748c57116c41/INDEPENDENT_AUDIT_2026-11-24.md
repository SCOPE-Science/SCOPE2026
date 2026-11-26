# Independent mathematical audit

## correctness

PASS

The rim is isometric in the tadpole. A pair on the same arm has a vertex between the leaf and the farther vertex; a pair containing 0 or the even antipode likewise makes a forbidden triple with the leaf. Both antipodal shortest paths must be counted. Opposite nonantipodal arms give allowed pairs, and no three rim vertices can all pair with the leaf because the bipartite link has no triangle. Thus the link is exactly K_{h,h} plus p isolated vertices, with shore swap and each isolate fixed. The cofiber of the simplicial inclusion is the unreduced suspension of the link. Contracting a tree in the connected component gives p circles and (h-1)^2 two-spheres; this includes h=1 for n=3,4. Orient edges left to right: the cycle group is the kernel of row and column sums, exactly U_h tensor U_h by the split augmentation sequence over Z. Reflection reverses each edge and interchanges the indices, so acts by negative transpose; components give trivial relative H1. Each off-diagonal tensor pair gives two integral eigenlines of index 2 in its rank-two block; each diagonal is a negative eigenline. This yields the ranks and index, nontrivial first for n=7. The reflection preserves suspension coordinates; on the link quotient, off-diagonal edges give K_h and reversed diagonals become pendant intervals ending at fixed midpoints, not loops. Its connected component has cycle rank binom(h-1,2), giving the claimed geometric quotient by suspension without using an integral coinvariant argument. Replay `python /workspace/independent_checks.py 5` corroborates metric triples and genuine edge orbits through n=40; the frozen script's bounded incidence-rank test is modulo a prime and is not the proof of the integral lattice.

## originality

PASS

The bounded comparison supports the explicit one-leaf link, relative cofiber and reflection structure as distinct. Prior cycle and corona counting, absolute GP homology, and analogous tree or permutation lattices do not compute the same inclusion with its involution. Same-day indexed comparisons are substantive comparisons, not a priority ranking.

## value

PASS

Adding a single leaf is a natural local graph change, and the cofiber measures precisely its relative topology without pretending to give the absolute homotopy type. The result yields both a parity-sensitive circle count and a growing integral obstruction that is invisible in rational eigenspace ranks. Correct identification of folded intervals in the geometric quotient makes the result directly useful as an example of why orbit geometry matters in a leaf-attachment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
