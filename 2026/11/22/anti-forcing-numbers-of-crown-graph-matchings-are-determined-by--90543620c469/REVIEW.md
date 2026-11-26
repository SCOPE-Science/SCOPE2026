# Independent mathematical audit

## correctness

PASS

Fix a derangement π and index matched pairs by their left endpoint. A nonmatching edge a_i b_{π(j)} gives i→j; the only absent loopless arcs are π(j)→j, forming c(π) disjoint directed cycles, including possible directed 2-cycles. An alternate matching exists exactly when the surviving arcs have a directed cycle. In each topological order at least one absent arc per cycle points forward, so at most binom(n,2)−c(π) available forward arcs can survive. Reverse cyclic order in each block attains that bound. Equality forces retention of every available forward arc and exactly one absent forward arc in each cycle; this proves the deletion-set characterization without asserting unique orders or counting witnesses. Subtraction from n(n−2) gives the formula. Labelled cycles of lengths ≥2 yield the EGF; removal of n from a cycle of length ≥3 or from a transposition gives the recurrence for n≥2 and the stated bases. Taking k−1 transpositions and one remaining cycle gives every possible k, and the extreme types give the coefficient counts including n=3. The frozen checker was inspected, not executed: its direct competing-matching transversal check covers n=3,4, its order optimization n=3–6, and n=7 is a census with formula-assigned weights. The proof, not those bounds on testing, establishes all orders.

## originality

PASS

The general matching/alternating-cycle framework and the derangement cycle enumerator are established ingredients. The inspected comparators do not give the crown-specific exact optimum for each derangement, its equality conditions or its weighted matching distribution.

## value

PASS

For the canonical dense bipartite family obtained by deleting a matching, there is a nonconstant fixed-matching optimum which global bounds cannot resolve. The cycle law identifies precisely how the omitted diagonal interacts with a chosen matching and describes all optimal deletion structures. The resulting exact spectrum with multiplicities supplies a natural family-wide benchmark, not just isolated small-order counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
