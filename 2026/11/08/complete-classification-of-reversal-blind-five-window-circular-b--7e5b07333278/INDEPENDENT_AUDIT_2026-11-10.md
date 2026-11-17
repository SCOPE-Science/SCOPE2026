# Independent mathematical audit

## correctness

PASS

There are 20 reversal-equivalence classes of 5-bit words (8 palindromes, 12 reversal pairs), so a circular identifier with distinct classes has 5<=k<=20. Every circular binary word corresponds to a closed walk in the 4-bit de Bruijn graph with edges labeled by 5-bit reversal classes. The assigned verify_graph.py explores both possible bits from every 4-bit state while forbidding class reuse, exhaustively reaches 3242 recursion nodes, and canonicalizes every closed walk. Independent reconstruction returned 20 rotation classes with counts by lengths 6:2,7:4,8:4,9:4,10:2,12:4; none at other k. Their same-length class masks overlap pairwise, proving capacity at most one at each viable k. The length<=20 proof makes finite enumeration an exhaustive proof, not extrapolation.

## originality

PASS

The earlier circular robot-ID study uses ordered windows and additionally distinguishes read direction, while classical orientable sequences disallow palindromes. Unoriented de Bruijn sequences instead seek shortest (often linear) coverings of all reversal classes, not maximum no-reuse circular cycles or a same-length codebook packing. Related ordered five-window capacity bounds cannot be specialized by simple parameter change because reversal merges edges. The 1993 orientation literature unread original is an explicit residual risk.

## value

PASS

The position-only, reversal-blind observation model is a natural distinct sensor-identification constraint. The full sharp length support, exact 20-word necklace census and codebook-capacity-one obstruction are independently usable finite combinatorial classifications, not arbitrary negative tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
