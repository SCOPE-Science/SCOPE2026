# Independent mathematical audit

## correctness

PASS

Available vertices and the mover determine the future game. At a terminal induced graph both scores for additional moves are zero. Otherwise each legal edge counts one move and leaves the induced graph on the available subset minus its endpoints, with the roles alternating. Max takes the maximum of the Min-to-move child values; Min takes the minimum of the Max-to-move child values. This is exhaustive backward induction because each child has two fewer vertices. Fixing two opening moves gives 2 plus the residual value with the original starter on turn. Standard skeletons used include G(10,2) for the dodecahedron and the two staggered pentagonal rings and poles for the icosahedron; regular solids are edge-transitive. Independent check: run python /workspace/branches/6f86c7a1-5ffb-443c-b0b6-aa1ae3f7976d/record4_repro.py; the fresh exact output is record4_results.json in the same directory. After a small smoke test this checked up to 2^20 masks, ordinary terminal extremes and every second reply after each of the 30 openings on both dual solids. It reproduced (2,2), (4,4), (2,3), (8,9), (5,6) in the stated order and terminal extremes (2,2), (3,4), (2,3), (6,10), (5,6). For the dodecahedron the histograms over outcomes (8,9) are (5,20) for Max opening and (17,8) for Min opening. For the icosahedron the histograms over (5,6) are (9,12) and (20,1) respectively. The two supplied checkers and checks.json were inspected, not executed. This is a finite exact result for the standard skeletons, not a positional strategy theorem or independent certification of other polyhedra.

## originality

PASS

Qualified to evaluation of the two Platonic duals and their exact reply sensitivities, not discovery of the game, minimax recurrences, the existence of a reverse first-player penalty, or the known octahedral example. The tetrahedron and cube entries are not credited as separate discoveries.

## value

PASS

The Platonic skeletons form a motivated complete family. Both dual graphs favor going second despite edge symmetry, but the icosahedron reaches a perfect matching only under optimal Min-start play and only one of its replies preserves that outcome, whereas even the better dodecahedral start remains strictly below a perfect matching. The exact reply sensitivities are meaningful finite benchmarks beyond the general one-unit difference bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
