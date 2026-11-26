# Independent mathematical audit

## correctness

PASS

The finite game is over all two-named-strict-linear-order extensions; rigid marked orders make the one-point types exactly pairs of insertion gaps. A rank-one pair fills all nine cells. To witness rank three, an anchor needs such a partner in each quadrant, where that partner plus the four local open cells require five distinct points. At size 21 the anchor is the unique median of both global orders and each partner the median of both local orders. For any partner, the nine cells consist of its four local cells, two cells in each adjacent quadrant (each adjacent group must straddle the local median in the relevant order), and the occupied opposite quadrant. Thus the four shared-side shuffles and four local permutations are independent and reconstruct the host bijectively. Independently enumerating 5! permutations and the 252 shuffles gives 16 and 180, with failure sets of sizes 42, 42 and intersection 12 for the shuffles; the count is 68,797,071,360,000. A partner's extreme outer cell has a unique point; adding it leaves the subcell between the two points empty, preventing the partner from rank two. Every possible rank-three anchor and its witnessing partners are forced, so the host cannot reach rank four. The bundled checker was inspected, not executed; python3 checker.py in the frozen result directory is the advertised supplementary replay and does not enumerate all length-21 hosts. The universal lower bound and census are proved by the cell argument, not by the checker.

## originality

PASS

The rank and the permutation class are established. Bounded primary and indexed comparisons support a distinct claim for two named orders: the exact rank-three threshold and minimum-host census, including independent side interleavings. The strongest distinct indexed comparison computes the analogous invariant for a single order with named colours, not two independent orders.

## value

PASS

This computes a natural first nontrivial multi-step realization threshold for a permutation extension game and describes every extremal witness by a small product of forced local patterns and nontrivial shuffles. The exact census and proof that no minimum witness already has rank four give usable structural information beyond the existence of a 21-point example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
