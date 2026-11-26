# Independent mathematical audit

## correctness

PASS

At most two selected cells occur per row or column because the collinear geodesic is unique. Manhattan diameter ≤3 bounds the span in each coordinate. For a row span of three, the extremes are singletons on the same column, so equality at six forces two cells in each intermediate row; the extremes forbid columns farther than one away, and their vertical geodesic forbids their own column on the intermediate rows. For smaller row span, six requires three consecutive rows of two cells; width two is too small and width three would leave one omitted cell per row and column. Such omissions cannot hit both opposite-corner pairs, since any two corners chosen from distinct opposite pairs share a row or column. The only remaining span is three in the column coordinate, giving the transposed equality argument. The listed six geodesic representatives for H cover all pairs under the two reversals and certify feasibility, and no orientation/translation is counted twice. On 3×3, a center-containing five-set would need two adjacent corners and two edge midpoints. With top corners, these midpoints must be bottom and left or right; in either case all monotone paths from the corresponding top corner to the bottom midpoint hit the center or the chosen side midpoint. Without the center, one corner and four midpoints is blocked by the midpoint on the corner-to-opposite-side-midpoint path; two adjacent corners prohibit the intervening midpoint and thus force all other midpoints. The feasible sets are the four rotations of B. Independent BFS subset enumeration found exactly the expected optimizer families on 3×3, 3×4, 4×3 and 4×4.

## originality

FAIL

An independently proved indexed polynomial result already gives the maxima and multiplicities on a larger domain, with exactly one anchored six-set in the only possible box up to transposition. The H,V coordinates are obtained by verifying the displayed feasible example in that singleton anchored class. This is exact coverage and direct implication, not a similar parameter or merely a shared subject. No historical priority inference is needed.

## value

FAIL

The natural radius-three rigidity question has mathematical interest and the elementary span proof is explanatory, but the submitted finding gives the same optimizer invariant already fixed by the complete exact table. Naming the unique local configurations and counting placements does not leave a distinct valuable claim once that table is available; no new structural extension or independently useful remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
