# Independent mathematical audit

## correctness

PASS

The local fields are X-x_i+y_i and Y-y_i+x_i for open neighborhoods. For even n a balanced row copies its partner and an unbalanced row becomes uniform even at the magnitude-two tie. Thus two balanced rows swap and all other states become fixed in at most two updates. For odd n a row of magnitude at least three becomes permanently uniform; the partner then becomes uniform within two more updates. For weak sums X,Y=±1, the same +1 sums imply a=d+1, b=c for column counts (++,+-,-+,--); the next sums are 2d+1, so only d=0 oscillates, by swapping mismatches. For opposite (+1,-1) sums a=d, b=c+1 and one update leaves only opposite columns with sums (2a-1,1-2a). Thus a=0 is immediately periodic, a=1 gives the sole new predecessor type for this orientation, and larger a leads to uniform rows. Sign reversal handles the other two sign patterns. The multinomial counts give the stated P_2 and B_2. The four uniform pairs, plus the equal balanced rows in the even case, give all fixed states. Checked the sharpness witnesses and the n=2,3 exceptions and substituted Stirling's estimate for the probability asymptotics. The packaged scripts and recorded outputs were read, not executed; an independent direct-field enumeration of all 87,376 initial states for n=2–8 reproduced fixed counts, P_2, B_2 and exact maximum entry times.

## originality

FAIL

The distinct earlier indexed matched-clique record 1963bd6fd34f already treats the same labelled graph, open-neighbor majority and tie retention, and gives the exact even and odd oscillation basins, one-step oscillation predecessors and sharp periodic-entry bounds including small-order exceptions. Its immediate-period count is in unoriented two-cycle orbits; doubling converts it to the frozen record's initial-state count. This is demonstrable prior coverage, not a keyword similarity or an inaccessible-source inference.

## value

FAIL

A full oscillation-basin census would be useful if unavailable, since a generic period bound does not determine it. As submitted this reproduces an already available all-order census with the same transient distinctions. Recounting in labelled states instead of orbits and applying Stirling do not add an independently useful invariant, new method, range, or consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
