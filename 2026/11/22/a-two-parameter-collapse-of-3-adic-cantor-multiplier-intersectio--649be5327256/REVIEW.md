# Independent mathematical audit

## correctness

PASS

A first gap shorter than r between successive support positions gives exactly two terms, with no prior carry, when the translated length-r repunit blocks first intersect. Thus the first constraint gives r-spacing. If h is the first remaining gap shorter than k, then r≤h≤k−1 and all blocks from earlier 1s end strictly before the first of the two 1s bounding h. For B={0,…,k−r−1}∪{k−1}, the two B-translates intersect at the second 1 when h≤k−r−1, and otherwise no later than k−1−h positions after the second 1. In the latter case 0≤k−1−h≤min(r−1,k−r−1). At the first intersection, the next 1 has not yet started a block (r-spacing), so exactly two contributions occur and there is no incoming carry. This prohibits h even for an infinite support because the decisive digit is at a finite index. The converse follows by disjoint translates for all supports of span at most k−1, including that of L_k. A valid prefix extends by zeros; conditioning on its first digit gives the exact recurrence and initial conditions. The associated k-spacing graph has a zero loop and a k-step 1-return cycle, spectral radius satisfying β^k−β^(k−1)=1; the standard path-set dimension is log_3 β. The decisive uniform proof is at RESULT.md lines 28–44. The supporting finite checker and its 75,600 reported comparisons were inspected, not executed, and are not needed for the proof.

## originality

PASS

The spacing language, prefix growth and dimension on the right are already known. The k=4,r=2 illustration is also implied by the older labeled automaton for multiplier 31 once the L_2 no-adjacent-ones constraint is applied. The contribution supported here is the uniform two-parameter equality with the interior sparse-block multiplier, including the first-carry argument that makes the difference-support observation decisive. Credit the earlier individual points, repunit-only collapses and related sparse-family comparisons separately.

## value

PASS

Replacing a simultaneous pair of multiplier constraints by a single canonical spacing constraint identifies the actual arithmetic set, not only its dimension, for an infinite interior parameter family. It gives a direct way to read membership and prefix extension without building multiplier-specific carry graphs, and isolates how one multiplier's imposed minimum spacing prevents problematic carry overlaps in the other.

The dated certificate retains the supplied scientific assessment, sources and limitations.
