# Scientific assessment

## Correctness

The closed-neighborhood lower bound is attained by a word with one pair of consecutive occupied columns. Any optimum has two excess coverage incidences, which excludes a column with two selected vertices. This leaves a single same-row adjacent pair and alternating colors across empty columns. In a one-token replacement only the adjacent pair can supply the departing token, and domination forces the destination to be the opposite row of a neighboring column. The resulting permutation of pair position and color is a single cycle of length $2n$. Finite enumerations are supporting checks, not the all-length proof.

## Relation to earlier results

The ordinary minimum-size and minimum-state counts are known. The independent-domination exchange theorem covers both move graphs for lengths divisible by four and lengths congruent to three modulo four with $n\ge7$, since the ordinary minimum sets in those cases are independent and the two minimum sizes coincide. The finding is narrowed to $n\equiv1\pmod4$, $n\ge5$, where the ordinary minima are not independent and the independent optimum has a different size. The known word language in this class gives a starting point, but the inspected enumeration does not state the two exchange graphs. A previously unlocated equivalent analysis remains possible.

## Value and limits

The exact contrast between complete slide immobility and a connected jump cycle with linear diameter holds for an entire natural congruence class. It is a fixed-cardinality result at the minimum domination threshold, not a claim about addition/deletion moves or the excluded prism sizes.
