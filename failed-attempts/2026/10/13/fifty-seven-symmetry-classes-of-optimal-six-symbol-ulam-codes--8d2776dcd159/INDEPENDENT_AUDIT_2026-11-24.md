# Independent mathematical audit

## correctness

PASS

A pair of distinct six-symbol permutations is compatible exactly when it shares no ordered length-three subsequence. Symbol relabeling takes any chosen anchor to 012345, uniquely; double counting designated words then gives 4N=720*298. The same argument applied in a single orbit counts 180 times the identity-containing multiplicity. The canonicalization minimizes sorted anchored codes over the four anchors and the two choices of global reversal, so equality of keys is exactly equivalence under the specified action. Independent direct dynamic-programming LCS replay at /workspace/branches/a59351b5-95f9-482c-b881-59513f3ae5d1/independent_check.py found 720 words, 132 anchor neighbors, 298 anchored maxima, no extension to five words, 53,640 labeled optima, and 57 canonical classes with orbit sizes 360 (7), 720 (29) and 1440 (21). All 57 CLASS_REPRESENTATIVES.tsv rows match, with correct sizes and canonical keys. Each optimum pair had LCS length two. Independently, LCS length one would force a reversed pair, and a third compatible word would then lack both increasing and decreasing triples relative to the first order, contradicting Erdos–Szekeres. Exhaustion is specific to length six, and the bound four is credited to prior work.

## originality

FAIL

A distinct indexed result gives the exact assigned equality census, under the same action and hypotheses, including the histogram and equidistance. Exact coverage is verified; priority or the relationship between the two packages is not inferred from their same displayed date. The unresolved older directed-design comparison is not the basis of failure.

## value

FAIL

A complete census of equality cases of a natural bound is scientifically useful in principle; the exact count, distance pattern, and classes are natural invariants. For this submitted finding they are already fully represented in the identified census, and no independently valuable mathematical remainder is asserted. Reproducing that classification verifies it but does not add a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
