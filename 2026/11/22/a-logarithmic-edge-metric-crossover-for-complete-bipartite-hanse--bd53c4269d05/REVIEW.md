# Independent mathematical audit

## correctness

PASS

Read the frozen proof and supporting files. In either horizontal face the two coordinate cubes are faces; only their Hamming-distance-one edges qualify within a cube. Each nonempty mixed pair is exposed by giving the two supports tied positive score, with negative scores elsewhere. Across layers an exposing functional exists exactly when the base functional has a unique maximum S and unique minimum T; shifting its height coefficient ties the chosen vertices. For nonempty mixed pairs take +1 on S, −1 on T, small negative weights on the rest of S's class, and small positive weights on the rest of T's class. For a common class the cube forces strict complementary signs, and weights in the other class can be made smaller in total magnitude than either nonzero extremum. When one endpoint is empty, all coordinates must have the same strict sign at that extremum; the other endpoint must fill a class and can be made the unique opposite extremum by choosing that class dominant. Both empty is impossible. This verifies the four edge types and their squared lengths. The longest two are the cross-layer full-class pairs (p+q+4); the norm bound and antipodality give diameter squared 4(q+1), strictly larger since p≤q. Dividing the three class counts by q·2^q at finite c gives weights proportional to 1,4c,0; at c=∞ dividing by 2^(p+q) shows cross-class dominance. For any nonzero cross-class limiting mass both part sizes diverge, so independent conditioned binomial sizes give concentration at normalized length 1/2. The c=0 endpoint needs no such conditional concentration. Independent bounded integer-score enumeration agreed for (2,2),(2,3),(3,3), giving opposite-layer totals 26,54,114 and total edge counts 60,128,260. Witness scores were restricted to [−4,4]; this is supporting evidence only. The shipped clique checker was inspected, not executed.

## originality

PASS

The base skeleton and twisted-prism construction are antecedents. The searched sources do not give the full length-weighted twisted-prism skeleton in this realization or its crossover. The passage from known base edges to opposite-layer edges and normalized metric weights is explicitly verified, not treated as a rescaling of an established metric formula.

## value

PASS

A full metric census for a standard embedding is useful beyond an ordinary edge count: it makes the competing edge populations explicit and proves a sharp imbalance scale where both short and dimension-scale squared lengths retain positive probability. The complete result includes two very different endpoint regimes and distinguishes the longest edges from the vertex diameter. It requires no arbitrary length cutoff or finite-instance conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
