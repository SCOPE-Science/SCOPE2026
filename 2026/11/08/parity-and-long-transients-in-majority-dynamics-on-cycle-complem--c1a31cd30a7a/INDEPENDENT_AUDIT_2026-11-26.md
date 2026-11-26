# Independent mathematical audit

## correctness

PASS

For odd N=2m+1 each vote excludes the center and its two cycle neighbors, and the tie threshold is m−1. With K≤m−1 a 1 sees at most m−2 and a 0 at most m−1, so the next state is all zero, and the complemented statement holds at K≥m+2. At K=m the output ones are exactly the centers of 000 and 010. If there are r zero runs and r one runs, with a long one runs and b long zero runs, the count is (r−a)+(m+1−r−b)=m+1−a−b. A cyclic odd word must have a+b≥1; a+b=1 forces the only long run to be zero of length two (otherwise m+1 zero singletons would force too many one runs). Precisely those N words stay fixed; the remaining layer goes unanimous in two steps, symmetrically for K=m+1. The word 1^m0^(m+1) reaches an intermediate state of positive weight m−1, then unanimity, proving sharpness and excluding any earlier recurrence. For even N at K=m the rule becomes minority of the centered triple. In 1^a(01)^k0^a for a≥2, k≥1 both constant blocks switch, and every site of the alternating segment stays put, including its first 0 and last 1. Those two sites enlarge the new boundary blocks; complementation gives the other transition. Each resulting word is balanced. When k=0 the two blocks switch forever. The count of equal cyclic edges is 2(a−1), strictly increasing in the transient, including in comparison with the steady count at the terminal time; no earlier equality with the second iterate is possible. The complemented cycle has degree N−3, vertex transitivity from shifts, and a common neighbor for each missing edge, so its diameter is two.

## originality

PASS

The even witness's local transient time is covered by the earlier exact cyclic-majority time law once the balanced cycle-complement embedding is made; the local shrinking mechanism is not independently new. General two-period behavior is also known. The supported distinct contribution is the odd cycle-complement all-state fixed-point census and sharp two-update result, together with the global-to-local embedding establishing the contrast in one dense deterministic graph family.

## value

PASS

The exact odd all-state census on a natural vertex-transitive graph complements a constructed linear transient on its even counterpart. This is useful for understanding deterministic worst-case stabilization on almost-complete diameter-two graphs: high degree and vertex transitivity do not give an order-independent bound, even though one parity has a sharp constant bound and no nontrivial two-cycle. The value is the parity comparison and realization, not a rediscovery of one-dimensional local erosion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
