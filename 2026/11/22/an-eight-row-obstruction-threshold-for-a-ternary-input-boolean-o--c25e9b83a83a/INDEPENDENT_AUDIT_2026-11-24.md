# Independent mathematical audit

## correctness

PASS

Under lax splitting the two downward-closed witnesses can be made disjoint. The first side selects at most one y per x, and moving all matching rows there cannot create a violation on either side. Satisfiability is therefore exactly the existence of a selection that leaves at most one z-value per y unselected. An unmixed fibre is irrelevant, and four mixed fibres already give a failing subteam by taking one row of each output from each: the three x-values cannot cover the four fibres. Thus every minimal failure has at most four used fibres, and if four then exactly eight rows. The independently reproduced finite census exhausts multisets of the 49 mixed Boolean states (49, 1225, 20825, 270725 candidates), up to renaming only y. It confirmed the size distributions: k=1 empty; k=2 {4:3,6:6,7:12}; k=3 {6:36,7:12,8:102}; k=4 {8:135}. Testing all single deletions is sufficient by downward closure; explicit witnesses of each allowed size were separately verified by direct split enumeration. Zero or one mixed fibre cannot fail. This proves the spectrum, the count 306 and sharpness of eight for unbounded finite Y.

## originality

PASS

The same chained dependence formula and the binary-determinant obstruction problem are prior work. The inspected sources do not cover the ternary/Boolean domain slice, its two additional obstruction sizes, or the complete 306-pattern census.

## value

PASS

The chained functional-dependency split is a canonical incoherent two-atom formula; the ternary/Boolean promise is a natural finite-domain step beyond the sharp binary-determinant theorem. Eight is an explicit sharp local witness bound independent of the intermediate-domain size, and the complete catalogue gives usable obstruction information beyond a decision procedure or a nonsharp bound, including the unexpected exclusion of size five and the emergence of sizes seven and eight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
