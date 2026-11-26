# Independent mathematical audit

## correctness

PASS

The exact neighborhood count is row plus column minus twice the tested entry for its own colour. Two colours force equality of the two neighbor counts, giving R_i+C_j-2ε_ij=0. Summing gives (b-2)R_i+S=(a-2)C_j+S=0. If both parts exceed two, all entries would be constant, impossible. For a=2<b this forces S=R_i=0 and identical entries in each column, namely a balanced split of the b columns. For a=b=2 the balance equations are precisely the two row and two column assignments. A one-colour assignment violates the cap. Constant columns cycling three labels work for a=2,b≥3. For a,b≥3, the mod-3 matrix works when the sum of ceilings is at most the cap, which holds at a+b≥14 by the integral left side and the (a+b+4)/3 upper bound. Checking the finitely many lower sums gives the four listed exceptions to that sufficient bound. The two displayed three-colour matrices pass the actual neighborhood test, and mod 4 gives the two claimed four-colour upper bounds. A single class at K_(3,4) has size ≤4 by double counting; a feasible four-edge class is forced into two columns by a row of degree two, then into the same two rows by column-degree constraints. Three rectangles cannot account for odd column degree. At K_(4,5), row degrees ≥4 violate the cap; a column of degree four forces all row degrees ≤1, while a column of degree three forces the remaining row empty and the other rows of degree ≤2. With columns of degree ≤2, a row of degree three forces two empty columns and hence ≤6 edges. Otherwise both sides have degrees ≤2, and any degree-two column must meet every degree-two row, so again there are ≤6 edges (or at most five if a side lacks a degree-two vertex). Three classes cannot cover twenty edges. These arguments prove the full classification and census independently of the priority issue.

## originality

FAIL

A distinct earlier-dated published Resultary record, 0d70fcb97654, states the same exact values on the entire frozen domain under the identical all-colours rule and also treats stars. Its structural two-colouring classification immediately gives both labelled counts, including the row and column cases at K_(2,2). Moreover K_(3,4) is expressly reported and proved in Pękała–Przybyło v1, Observation 9, contrary to the frozen record's novelty attribution. K_(4,5) is covered as acknowledged in the frozen result. The different calculations and explicit printing of a binomial count do not leave a distinct valuable claim to repair. This is demonstrated earlier coverage, not just failure to establish priority or mathematical incorrectness of the theorem.

## value

PASS

An exact structural classification is mathematically useful for this natural two-parameter family, particularly the low-degree boundary missed by high-degree upper bounds. The extremal shape of a colour class explains the exceptional graphs, and the rigidity theorem identifies all optimal two-colour configurations. This is value of the mathematics, not of repeating a covered result; the immediate labelled census alone is not a valuable distinct repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
