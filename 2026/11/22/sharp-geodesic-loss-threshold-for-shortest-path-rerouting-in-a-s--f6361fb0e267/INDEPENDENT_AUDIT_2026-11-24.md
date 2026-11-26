# Independent mathematical audit

## correctness

PASS

A B-before-A geodesic exists, so puncturing the cube leaves distance n between endpoints. All shortest routes flip each label once and changing one intermediate vertex exchanges adjacent flips. A route is forbidden exactly when all A labels precede all B labels. Every valid ordering can bubble all B labels left without losing its cross inversion, then sort within blocks, proving connectivity. The k!(n−k)! forbidden permutations each have exactly one edge to a valid neighbor, by swapping across the block boundary; the neighbor uniquely recovers its forbidden predecessor. The degree and edge counts follow, including the single degree-zero vertex at n=2. For a singleton A, inserting the non-A first target label never places A first; the rest of adjacent insertion realizes Kendall distance. Reversal handles singleton B. In the interior four-label witness the two fixed A-before-B orders make the initial and final opposite cross inversions mutually exclusive. A four-swap path could change only discordant pairs and would have to lose one cross inversion before obtaining the other; all external labels retain their orders, so the intervening state is forbidden. Parity rules out length five, and the six displayed adjacent swaps retain at least one cross inversion at every step. Independent direct enumeration of cube vertex sequences corroborated counts, both extreme-layer isometries, and the existence of distance-4-versus-6 pairs through n=6; the proof establishes all n.

## originality

PASS

The distinct supported claim is the single-vertex-deletion metric classification, with the explicit exact detour. The unrestricted permutation model and Kendall formula are credited to prior work; deleting a facet can change the induced metric. Indexed adjacent results help delimit the contribution but do not establish this classification. Primary theorem passages and some comparator bodies were not accessible; exact priority is not guaranteed.

## value

PASS

The natural first fault in a standard shortest-path reconfiguration model can preserve the length and connectivity of routes while changing the metric between them. The exact extreme-versus-interior classification and smallest parity-allowed detour witness are structural information not supplied by the simple counts or unrestricted metric. They pinpoint the first dimension and layers where the distinction matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
