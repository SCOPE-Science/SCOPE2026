# Independent mathematical audit

## correctness

PASS

For each coordinate the sign sum is C_n−2U_i, where U_i is the up-step count. In the adjacent swap at positions 2j,2j+1, the preceding height is odd and hence at least one, so the 10↔01 pairs preserve nonnegativity. At positions 2j−1,2j, the only unpaired contribution to U_(2j−1)−U_(2j) is 10 at height zero; its prefix and suffix are arbitrary Dyck paths of sizes j−1 and n−j. The resulting positive increments telescope from U_1=C_n. The increments are symmetric in j. At even n=2m the cumulative value hits C_n/2 at m only, giving the two plateau coordinates n,n+1; the neighboring increments give gap 2C_(m−1)C_m. At odd n=2m+1 the unique central increment is C_m², giving central values with opposite signs and minimum magnitude C_m². This includes n=1.

## originality

FAIL

The exact integral gradient is not asserted verbatim in the earlier mod-four record 84ddf083bb47, but it is mechanically recovered from that same-object record’s marked-up-step decomposition before reducing modulo two. The unsigned combinatorial recurrence is identical over the integers, and the prior displayed algebraic identity lifts by restoring the recurrence’s signs. This is not a claim that congruences alone determine integral counts. The singleton Walsh rewriting and center consequences add no nonmechanical step.

## value

FAIL

The clean singleton formulas may be useful as an exposition or normalization check, but the contribution as frozen is a routine integer extraction from the existing marked-step recurrence, followed by an affine rewrite and comparisons of consecutive positive sums. It provides no new higher-order mode, independent consequence, or other substantive remainder beyond that extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
