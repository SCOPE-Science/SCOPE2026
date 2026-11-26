# Independent mathematical audit

## correctness

PASS

The basin is the union of initial states reaching all zeros or all ones under synchronous strict open-neighbor majority with tie retention. Unanimity is absorbing; forward iteration until unanimity or a repeated word tests exact membership, independently of the eventual period bound. Independent exhaustive enumeration of all labeled graph masks, all present nonbridges and all initial words reproduced connected-graph counts (1,4,38,728), eligible deletion counts (0,3,84,3140), and gain–loss counts (0,0,0,240) for orders 2 through 5; order 1 has no edges. It reproduced all seven lower-order marked-edge rows, accounting for all 87 eligible pairs through order 4. Canonicalizing each qualifying pair by all simultaneous vertex permutations gave the two stated marked types with 120 labeled pairs each. The diamond with leaf has 26→30, losing 2 and gaining 6; the house has 22→24, losing 2 and gaining 4. Direct application of the update rule also checks the four witness trajectories, including old two-cycles and new fixed nonunanimous states. The frozen checkers were inspected, not executed. Replay the separately written computation with python3 /workspace/branches/aa496d05-0411-4b00-992c-44c11b0e804a/independent_majority_enum.py. Exhaustion is exact only through order 5; larger orders are not needed for the minimum and are not classified.

## originality

PASS

The same pointwise-versus-aggregate phenomenon occurs in the independently indexed Frucht graph census, and deletion nonmonotonicity for a different initial-majority criterion is classical. Neither establishes the sharp order-five cutoff or the full marked-edge classification there. Pass is for those sharp classification claims, not priority for observing generic nonmonotonicity or the phenomenon in arbitrary order.

## value

PASS

The minimum is a natural boundary for a concrete dynamical distinction relevant to changing a network: improvement in total attraction need not preserve attraction for each initial condition. The complete classification identifies two different minimal patterns and exact witness states; it rules out all smaller witnesses without picking an arbitrary cutoff. This supplies compact falsification and regression examples for stronger monotonicity conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
