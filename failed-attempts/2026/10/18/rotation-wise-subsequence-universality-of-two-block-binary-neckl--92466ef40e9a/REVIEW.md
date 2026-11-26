# Independent mathematical audit

## correctness

PASS

The upper bounds count each letter and the 2r cyclic changes: the 2r+2-letter alternating target would need one disjoint crossing per cyclic change. One-traversal containment is preserved by deletions in each run, so the lower bound reduces to equal run length m=1,2,3. In the periodic word start at the first symbol of the relevant run. For m=1 the step bound is 2. For m=2 the repeated-letter increments are 1 or 3, and changes cost 2−j, giving the telescoping bound 2+h(j′)−h(j) for h=(0,−1). For m=3 repeats cost 1,1,4 and changes cost 3−j; h=(0,0,−1) gives the analogous increment bound with baseline 3. A nonalternating target saves at least one at its first repeat, which is from offset 0; an alternating target saves one by starting at offset 1. Hence for k=2r+1 the endpoint displacement is at most 6r−1. Displacement less than word length is the precise one-traversal condition, including equality of the inclusive span with word length; line 20's 'fewer than ... consecutive positions' is stricter than needed, not a defect in the construction.

## originality

FAIL

The target-dependent one-traversal index differs from ordinary circular universality, but the entire frozen formula is an immediate corollary of the stronger distinct indexed result bcfce8efaaec, Eq. (4). All windows of length r(a+b) in the same infinite periodic word are exactly rotations of the finite host; the universal union of their spectra is precisely the condition addressed by that equation. This is demonstrable mathematical coverage, not an assertion of chronological priority or derivation between the records.

## value

FAIL

The quantifier separation and the threshold for a two-block host are natural, and the short greedy argument is useful exposition. As a distinct exact contribution, however, the frozen result gives only the mechanically extracted full-period threshold of an indexed theorem that already gives all window lengths and every pattern's span. The frozen claim adds no further invariant or boundary beyond that exact cover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
