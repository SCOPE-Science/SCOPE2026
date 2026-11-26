# Independent mathematical audit

## correctness

FAIL

The Finding explicitly says the largest primitive two-cycle exchanges the all-zero and all-one colorings (RESULT.md line 19). This is false: strict-neighbor majority fixes each globally unanimous state. The unique largest cycle exchanges the two opposite bipartition colorings, (0^10,1^10) and (1^10,0^10) in shore coordinates. Every neighbor is on the other shore, so the bits exchange in one update. The basin-size equality is an equality of cardinalities of disjoint basins. Independent exact replay constructs G(10,3), finds and checks a vertex isomorphism to the frozen 30-edge graph, computes the full majority map, seeds the states with F²(x)=x, and propagates basin identifiers and first-entry distances along reverse edges. All 1048576 states are reached; all nine basin classes, both basin-population totals and all five entry counts agree. Under the replay labeling the global states 0 and 1048575 are fixed with basin 51076 each, and 698709 and 349866 exchange with basin 102152. The base G(5,2) replay gives entries (124,260,400,120,120), phase preimage multiplicities (1:72,10:50,226:2), and exactly the two constant base phases of weight 226. Under the cover update T(x,y)=(f(y),f(x)), T⁴ applies the eventual even-phase map to both coordinates. Hence preimage weights multiply per phase, add over distinct phases of a two-cycle, and entry time is the maximum of base entry times. This verifies the census and proof mechanism but not the false orbit identification in the frozen Finding. The obvious wording correction does not leave an original claim, so no repair is submitted.

## originality

FAIL

Published Resultary record b8bcbb0b4dff (2026-11-17) explicitly proves the same nine labelled basin-size classes, the same totals, and a strictly finer entry-time table on the same graph and update rule. Its proof also identifies the weight-226 phases as the two constant Petersen masks and pairs them to obtain the 102152 two-cycle. Thus correcting the frozen orbit label still leaves the main finding covered. General earlier bipartite cycle-count literature is context, not the decisive duplication.

## value

FAIL

A complete transient census on a canonical cubic graph is a reasonable scientific target, but the exact census and a strictly finer table are already available. The frozen result neither uncovers a new invariant nor adds a structural result beyond the earlier computation. Independent reproduction is useful as audit evidence, not a distinct scientific result. Correcting the misnamed oscillator would leave only known consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
