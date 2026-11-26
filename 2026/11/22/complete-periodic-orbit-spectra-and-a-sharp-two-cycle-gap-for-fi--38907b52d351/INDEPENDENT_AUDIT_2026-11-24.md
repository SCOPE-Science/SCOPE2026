# Independent mathematical audit

## correctness

PASS

Each comparable edge maps to an equal or adjacent pair, so the increment of a lift is uniquely in {-1,0,1} even for the four-vertex crown. A nonzero winding requires all 2N increments to have the same unit sign, giving exactly the parity-preserving dihedral automorphisms. Zero winding gives a closed lifted walk with range length <=N, because the walk must go from its minimum to its maximum and return. An independent structural proof of the periodic restriction uses the eventual image: every iterated image is graph-connected and lies in the short arc, hence the stabilized image is an interval. Every vertex of the stabilized image is periodic, and the map restricts to an automorphism of that path, necessarily identity or reversal. A nontrivial reversal preserves crown order only when the endpoint sum is even; it has one fixed center and half the edge length in two-cycles. The two displayed fold constructions are order-preserving on every noncollapsed edge, close at the seam, and fix or reverse exactly their image; their required lengths 2 ell and 4 b do not exceed 2N, including equality. The whole-crown reflection instead fixes two vertices, while rotation by 2r has period N/gcd(N,r). The orbit product for zeta follows formally by counting fixed vertices of each iterate. Independently enumerated all monotone maps by local order-compatible vertex assignments, using stable images to extract cycles: totals 36, 234, 1544, 10030, 64044 for N=2..6, with exact claimed signature sets. Replay: python3 -I /workspace/branches/independent-checks/record4.py; record4.log in the same directory. Frozen script inspected, not executed.

## originality

PASS

Credit the exact finite-crown spectrum, in particular sharp nonbijective ranges with every count attained and the quantitative comparison with the whole-crown reflection. The infinite-fence periodic theorems overlap the qualitative local restrictions, and the automorphism component is ordinary dihedral dynamics, also partly present in a distinct same-day cycle-index record. The inspected evidence does not establish prior coverage of the complete finite interval of possibilities and its realization.

## value

PASS

Gives the complete exact set of possible periodic data for the standard finite circle poset. In particular it gives a sharp and attained loss in two-cycle multiplicity under collapse, even though a collapsing map can still preserve a maximal fixed arc; these are natural dynamics questions not answered by counting maps or homotopy classes. Explicit realization for all sizes is part of the value. The formal zeta encoding and dihedral data alone would be routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
