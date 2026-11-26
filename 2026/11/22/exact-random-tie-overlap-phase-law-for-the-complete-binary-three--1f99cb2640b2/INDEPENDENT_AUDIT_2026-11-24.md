# Independent mathematical audit

## correctness

PASS

A legal transition removes two current strings and inserts their literal merge. Averaging over every maximal-overlap ordered pair, before identifying equal successor states, is the exact conditional law. The substring-free invariant also follows directly: a third string newly contained in a merge but contained in neither parent must cross the entire glued interval and extend both ways; this yields a suffix-prefix overlap with the left parent greater than the chosen maximum. Containment of the merge in a third string would imply containment of a parent. Any outgoing overlap of the merge longer than its right parent would embed that parent in the other string, and the incoming argument uses the left parent symmetrically. Shorter overlaps are endpoint overlaps and are bounded by the old maximum. Thus the maximum never exceeds the initial two and there are exactly seven merges. A separate exact forward DP on literal strings, annotating each path by its phase counts, reproduced all seven cells and the five length probabilities, normalization and mean 167269939/14968800, independently of the endpoint-index calculation. Length starts at 24 and each merge removes exactly its overlap. Eight distinct three-windows require at least ten characters; 0001011100 contains all eight. In the length-fourteen witness the first four choices have overlap two, after which only the two indicated overlap-one moves and a final overlap-zero move are needed, all legal. The exact table gives positive mass at both extremes and no length outside 10 through 14.

## originality

PASS

The endpoints 10 and 14 are already covered for the identical input; neither is credited as new. The distinct finding is the exact distribution over all tie histories, including the seven overlap-count cells and their length probabilities. The strongest inspected prior same-input census reports only worst legal ties, and the closest same-day probabilistic result is for a different 4-mer input. The primary literature inspected provides an endpoint reduction and worst-case bounds, not the exact pushforward.

## value

PASS

The complete binary three-word universe is a natural fixed de Bruijn instance, not a selected collection with arbitrarily tuned tie behavior. The exact law distinguishes how often greedy is optimal from how badly it can fail and separates histories with the same output length, including length 12 with and without a zero-overlap merge. These are useful repeatable benchmarks for random tie policies that the known extrema cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
