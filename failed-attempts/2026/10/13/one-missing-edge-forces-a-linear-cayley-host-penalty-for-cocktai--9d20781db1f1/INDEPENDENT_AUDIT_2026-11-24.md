# Independent mathematical audit

## correctness

PASS

Deleting a cross-part edge from the cocktail-party graph adds an edge between two matching components in the complement, giving P₄ disjoint union (r−2)K₂, with n=2r vertices and m=r+1 edges. In a d-regular complementary induced host, d≥2. If t vertices lie outside the copy, the selected vertices send exactly nd−2m edges across the cut and the outside vertices can receive at most td. Thus t≥n−2m/d≥n−m=r−1. This works for all regular hosts, whether connected or not. The cycle of length 3r−1 realizes the complement pattern by arranging the required path blocks cyclically with one skipped vertex per block, including the wraparound; for r=2 this is P₄ in C₅. Complementing gives a circulant host with steps other than 0 and ±1, so the lower bound is attained in both classes. The undeleted graph needs exactly 2r vertices because it is already Cayley by excluding steps 0 and r modulo 2r and every induced embedding is injective.

## originality

FAIL

After complementation the graph is a nonregular linear forest, and the exact vertex budget is a routine specialization of the Erdős–Kelly induced regularization theorem and its deficiency bound. In degree two the optimal regularization can simply be made one cycle by linking the path ends through one outside vertex per component. Regular hosts of larger degree cannot improve the deficiency bound, as n−2m/d increases in d. Thus passing from the exact minimum degree-two regularization to a cyclic Cayley host needs no new obstruction or realization theorem. This is prior implication plus an elementary cycle specialization; no verbatim prior cocktail-party deletion theorem is asserted.

## value

FAIL

Sensitivity of minimum induced Cayley order to edge deletion is a natural theme. In this particular family, however, the operation just joins two matching components into a path in the complement, turning the cost into the known degree-two deficiency calculation with one cyclic gap per component. This does not supply an independently difficult or previously undetermined host constraint beyond that routine specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
