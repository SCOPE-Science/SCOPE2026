# Independent mathematical audit

## correctness

PASS

Classes are pairwise-intersecting edge families. A nonstar family must contain a triangle and can contain no other edge; a star of r edges has r+1 ground labels so a common disjoint pair exists iff r≤n−3. The n−2 class capacities at n=5,6,7 are 9,12,20, below the respective totals 10,15,21. The displayed n−1 partitions at n=5,6,7 were independently checked for coverage, properness and common disjoint-pair witnesses. For the optimum normal form, take t triangle classes and n−2−t star classes, designating an arbitrary valid centre for a singleton. There are at least t+2 noncentres, whose mutual edges require triangle classes, so binom(t+2,2)≤3t forces t=1 or 2. The latter would partition all edges of a K4 into two triangles, impossible. Hence t=1 and there are exactly three noncentres and distinct star centres; all triangle-to-centre edges are forced and remaining edges orient uniquely toward assignment to their tail class. This separately verifies the prior structural premise. The cap 3+d⁺(s)≤n−3 is necessary and sufficient, and near-regular tournaments satisfy it for m=n−3≥5 since ceil((m−1)/2)≤m−3. The ordinary chromatic bound is n−2. The independent enumerator /workspace/branches/be07c5a9-b777-4256-97bf-ec74e3df2db7/independent_check_record4.py exhausts 2^10 and 2^15 labelled tournaments and gives 24 and 5184, respectively; multiplying by binom(n,3) gives 1344 and 435456. Each unlabelled partition has (n−2)! distinct name assignments. Replay also at RESULT.md lines 14–29. The frozen Python verification was inspected, not executed; the cited C++ checker was not among the frozen support and the counts do not rely on it.

## originality

PASS

The triangle-plus-stars normal form and unrestricted tournament encoding are prior. The supported distinction is the solution to the class-wise dominated-colouring problem on KG(n,2): the small-order obstruction, exact onset of ordinary-optimal size, and score-cap classification of the resulting optima. The numerical counts support the classification but do not carry the originality judgment.

## value

PASS

The result answers an explicit problem in the literature for a natural infinite family and pinpoints when the extra common-neighbour requirement costs a colour. The characterization classifies every optimum beyond that threshold and links their enumeration to a precise tournament condition. This is useful beyond the two small numerical counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
