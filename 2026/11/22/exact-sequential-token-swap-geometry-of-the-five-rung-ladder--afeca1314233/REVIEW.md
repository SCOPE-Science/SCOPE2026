# Independent mathematical audit

## correctness

PASS

The thirteen edge transpositions of the connected open ladder generate every permutation; each gives a distinct successor, and simultaneous relabeling of all tokens preserves edges and distances. FIFO BFS from identity generating all thirteen swaps assigns true shortest-path labels on first discovery. An independent Python implementation reached all 3628800 placements and reproduced every one of the 22 distance shells, all four distance-21 placements, and all nine gap counts (424974,1197510,1259762,598260,132969,14518,790,16,1). A swap can improve the sum of destination graph distances by at most two; that sum is even by bipartiteness and the equal numbers exchanged between the two color classes. The Manhattan formula is the exact ladder distance; using p(i) in the identity-to-p sum is correct by reindexing the token positions. The only gap-8 case is R=(4,3,2,1,0,9,8,7,6,5), with BFS distance 20 and displacement sum 24. For any source pi, relabeling by pi inverse sends sigma to pi inverse composed with sigma and preserves the displacement bound too, so the partners are pi composed with R. R is a fixed-point-free involution on placements under right composition, giving 1814400 unordered shortfall pairs. Equal eccentricities give radius=diameter=21, and four farthest targets from each of 3628800 states give 7257600 unordered diameter pairs.

## originality

PASS

The inspected literature gives the model, a general displacement lower bound, algorithms on transposition trees, and a parallel-round approximation on the same family of ladders. The closest distinct catalogue entries give exact sequential metrics on other base graphs. None of these inspected statements supplies the open 2-by-5 ladder shell census, four diameter placements and the unique shortfall witness. The positive assessment is limited to that finite classification.

## value

PASS

The open ladder is a canonical narrow grid with two rails and no wraparound, already used as a model for routing. The exact sequential benchmark tests the common displacement bound and distinguishes two natural extrema: there are four true antipodes, while the isolated worst shortfall is a different configuration, separate reversal of the rails at distance 20. A researcher testing sharp bounds or algorithms on width-two grids could use the full shells and gap histogram rather than only the diameter or sampled trajectories. The value is this instance's exact benchmark and structural witness, not a scalable ladder theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
