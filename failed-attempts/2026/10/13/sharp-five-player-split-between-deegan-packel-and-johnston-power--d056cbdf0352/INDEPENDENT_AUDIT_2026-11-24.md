# Independent mathematical audit

## correctness

PASS

Properness is equivalent to prohibiting both elements of every complementary coalition pair from winning. The independent exact replay assigns neither/one/the other winner to each such pair, fixes the grand coalition as winning and filters for monotonicity. This exhausts proper winning truth tables without the frozen antichain generator. For each game the DP score divides a minimal winner's unit equally, while Johnston divides a winning coalition's unit among the intersection of the minimal winners contained in it, if that intersection is nonempty: a player is critical exactly when removing it destroys every minimal win inside that coalition. Normalizing either vector by a positive common factor preserves the signs of all pair differences. The replay confirms labeled counts 1,3,11,80,2645 and class counts 1,2,5,14,86, with zero divergences up to four. At five, the counts of labeled games/classes are 420/7 refining two ties, 60/2 refining four ties, and 300/4, 120/3, 40/2 respectively reversing one, two, three strict comparisons; there are no other divergent signatures. It verifies the witness vectors and dummy counts 940 divergent and 2330 total dummy-free games (no null players). Thus 940/2645=188/529 and 940/2330=94/233. Replay: python3 /workspace/branches/66580048-48cd-4cd7-866b-bc8b4d0755e5/dp_johnston_pair_trit_replay.py 5; saved output replay_n5_classes.out in the same directory.

## originality

FAIL

Two distinct indexed exact class censuses account for both strata. This is not just an empirical coincidence of totals or orbit sizes: Shapley–Shubik and Penrose–Banzhaf give the same weak order on this entire domain by the elementary pair-swing formula. With that bridge, the two published class tables and their types determine the full DP–Johnston first layer. This is a statement-level coverage judgment, not a claim about scheduling or priority.

## value

FAIL

The ordinal distinction between these power measures is well-motivated, and the computations are correct. However, the two known class censuses determine exactly the two advertised strata via the same simple baseline, leaving the combined census and witnesses a mechanical recombination rather than a distinct useful unknown classification. The dummy denominator is a direct inclusion–exclusion count from known sizes. No independently valuable new remainder of this record was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
