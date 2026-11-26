# Independent mathematical audit

## correctness

PASS

The bound graphs match the pentagon Mycielskian and the explicit Chvátal edge list, the latter checked against the standard NetworkX generator. Independent exhaustive ordinary colouring with dynamic vertex ordering excludes three colours for each original and two for every deletion, and finds proper colourings with four and three respectively. For the game, each proper partial colouring has its turn fixed by occupancy parity. Completion is Alice-winning; a blocked uncoloured vertex is irrecoverable because no colours can be removed. On the remaining states the disjunction on Alice turns and conjunction on Bob turns give exact backward induction by decreasing uncoloured count. Equivalence under global palette permutations justifies canonical keys and keeping only one unused-colour representative; no vertex symmetry or monotonicity of wins with palette size is assumed. Read both frozen source programs and checked a separately written bit-state search and its full output: four-colour wins for both originals, and across all 23 deletions Bob wins at three colours and Alice at four. The ordinary lower bounds exclude every smaller palette not examined as a game. These are exact results for the stated rules and labelled graphs.

## originality

PASS

Credit ordinary criticality and the full Grötzsch game number as known. The contribution assessed is the whole vertex-deletion persistence classification for the Alice-first game on both graphs: ordinary chromatic number drops, while the game number does not. The closest prior deletion result supplies only the ordinary Chvátal values; the closest exact game results concern different graphs or the original unmodified Grötzsch graph.

## value

PASS

These are classical small triangle-free, ordinarily 4-critical graphs, so the deletion family is intrinsic, not an arbitrary sample. The precise divergence of ordinary and adversarial criticality is established on every deletion in both examples, supplying reusable witnesses and exact benchmarks in the ordinary Alice-first game. This is stronger than observing a discrepancy on one labelled vertex and cannot be read off from known ordinary colourings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
