# Independent mathematical audit

## correctness

PASS

There are four fixed words and six two-word orbits, giving ten classes. To get unrestricted optimal length independently, I used shortest paths in the product of the last-three-bit automaton and the covered-class mask, starting at all length-three suffixes. Each append creates exactly one new four-window, and all covering words occur as paths; minimum over supersets gives L for each requested mask. The best greedy overlap is the maximum over all pairs, orientations and orders. Memoizing the maximum successor length on sorted representative states is sound by independent orientability and induction on component count. In the independent run, assertions on all maximizing transitions verify no containment in either direction or orientation. Exhausting all 1023 masks gives 4/3, precisely 131,159,183,215,407,663, with (6,8) at 131 and (9,12) at the other five; mask 1023 is (13,16). The full joint census matches the two frozen outputs. Mask 131 also has the direct length-six cover and two legal greedy overlaps 3 and 1 in the proof; at least six symbols are needed for three distinct four-window classes.

## originality

PASS

A distinct same-day all-length theorem already contains the value 4/3 and the exact mask-131 witness for three classes. The retained distinct claim is that no larger subset exceeds that ratio and that exactly five additional masks, all with six classes, meet it. No priority between same-day results is inferred. The ordinary finite censuses and general reverse-complement approximation theorems do not cover that remaining claim.

## value

PASS

Worst-tie behavior of the standard overlap rule is a natural exact benchmark. Length four is a small complete binary class universe that allows enough components to test whether the three-input obstruction actually controls all cardinalities. The absence of any worse larger instance, together with additional extremizers on six classes, is concrete information not available from a single example, full-set calculation or ordinary-SCS baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
