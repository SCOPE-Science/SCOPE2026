# Independent mathematical audit

## correctness

PASS

Checked the tree-lift argument and arithmetic. A cyclic walk determines a deck conjugacy class; a recoloring replaces a backtracking two-step segment because the target is square-free, so it preserves that class and lifts locally. For a nonidentity deck element with translation length L, the endpoint distance in the tree is L plus twice the initial vertex's distance to its axis. Necessity of n≥L and matching parity follows, and the extra steps can be inserted as reversals. If n=L the walk is geodesic, with no recoloring, and such marked closed nonbacktracking walks are exactly the trace terms. If n>L, choose a walk vertex at maximal positive axis distance among one period. Its two neighbors coincide at its parent; replacing it by its grandparent or an adjacent axis vertex strictly decreases the sum of axis distances per period, also at the seam by equivariance. On the axis, swaps within the period connect all sign words of the same net displacement at a fixed origin; a reversal across the seam, available in either direction because both signs occur, moves the origin by two. This proves exactly two lift components, separated by the tree bipartition. All lifts with the same monodromy projecting to the same map differ by its centralizer. The primitive root translates by its primitive length d, swapping the components exactly when d is odd; the component stabilizers are infinite cyclic in either case. Matsushita's equivariant covering/contractibility applies to the nontrivial slack sectors since these source cycles are square-free (the exceptional C₄ has only null image here). This gives K(ℤ,1) components. The even null sector is exactly one connected double-cover type by the square-free-target theorem, and its Betti rank is 30−20+1=11. An odd source cannot have null monodromy. At n=3 there are no maps. Marked primitive period-d repeats contribute d, not the full repeated length, to the trace, giving Möbius inversion. Counting positive multipliers with md≤n−2 and matching parity yields both floors. Independently checked the determinant factors by A²=2I−A+J for the Petersen adjacency matrix, giving eigenvalues 3,1,−2 with multiplicities 1,5,4 for Ihara–Bass. Independent trace and floor computations match through n=13, and independent recoloring distributions match through n=12: in particular the reduced-length-10 circle count at n=12 is 2p₁₀+p₅=240+24=264, and Q₁₀,Q₁₂,Q₁₃ are 100,364,304. These bounded graphs check counts, not the uniform lifted Hom contractibility or geometric types.

## originality

PASS

The homotopy-type theorem, parity of realizable conjugating walks, primitive centralizer description, and transfer-matrix/necklace arithmetic are prior tools. The claim that survives comparison is the explicit aggregate all-length enumeration of the Petersen Hom components by admissible reduced necklaces, with the phase multiplicities inserted in the trace-derived floor sums. Credit the earlier finite Petersen numbers and the prior parity test itself; neither is being rediscovered as a separate finding.

## value

PASS

The exact all-length enumeration gives component multiplicities and integral homotopy types without enumerating exponentially many Hom vertices. For this natural cubic square-free target it unifies disconnected finite calculations and identifies a genuine threshold phenomenon: odd primitive periods can yield single movable phase orbits even when the reduced walk length is even. The advantage is aggregate arithmetic and its explanation, not a check of an additional isolated small length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
