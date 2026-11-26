# Independent mathematical audit

## correctness

PASS

The empty and singleton sets fail, and for two landmarks the first and last edges of a shortest path collide, with the adjacent-landmark case covered by minimum degree two. For the infinite construction use the three top-rail columns 0,j,N, with j=2 for even N>=6 and j=3 for odd N>=9. In the right region each signature has the distinguished j-spaced pair (q-j,q) and third entry N-q+c with c in {-1,0,1}; equal distinguished pairs identify the edge. A collision with different pairs forces c'=c-j and 2q=N+c-j, impossible for j=3 and impossible by parity for j=2. In the left region the listed triples are distinct and only the first rung has a j-spaced pair. Its pair (0,j) would force q=j on the right, where the third entry is strictly below N. Independent BFS and subset enumeration of the exceptional orders checks all subsets at n=2,3,4 and all sizes through four at n=5,6,8. It reproduces the infinite dimensions, absence of smaller bases at 5,6,8, and the 4,20,80 basis counts; it also found four three-sets at n=7. The referenced finite_obstructions.json is absent in the frozen package and was not validated; the independent enumeration establishes the required finite facts without it.

## originality

PASS

The exact Resultary entry is the frozen result itself. The closest primary results use the same invariant on different graph families, or different invariants; none of the inspected statements implies the classification or the finite basis multiplicities.

## value

PASS

The two-row Cartesian grid is a basic test family for an order-insensitive distance invariant. The result separates nonexistence from low finite dimension, supplies a uniform construction, and shows a genuine isolated reversal of the naïve monotonicity expectation at eight columns. Exact labelled basis multiplicities quantify that exceptional regime rather than merely producing isolated witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
