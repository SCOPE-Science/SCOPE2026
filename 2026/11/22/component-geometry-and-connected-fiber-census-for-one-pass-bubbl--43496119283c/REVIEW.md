# Independent mathematical audit

## correctness

PASS

A left-to-right pass carries the running maximum and emits the smaller of the carry and the next entry. Each change of carry emits the old carry as an output record. Selecting which nonfinal output records arise this way determines the input uniquely by the block substitution in the proof; conversely each selection works because all letters in a block are smaller than its next selected record. An adjacent swap can change only the smaller entry's record status, and by uniqueness an edge must therefore toggle one selection. The two local factors are mu W nu and nu W mu; if no earlier record is selected, W is the entire prefix before mu. These factors differ by an adjacent swap exactly for empty W, i.e. the first bit or an output-record index immediately preceded by a selected record. Thus gaps freeze the initial bits of the later Cartesian factors. In each frozen factor the leading ones and the first zero are fixed and the remaining suffix can be zeroed from left to right, yielding the full component spectrum. The free first bit accounts for the absence of isolates at n >= 2 and contributes 2^(m-1) edges; each allowed later index contributes 2^(m-2). For a connected fiber the nonfinal records form an initial increasing block ending in n-1; with k total records there are binomial(n-2,k-2)(n-k)! such outputs. This proves the count and asymptotic with the n=1 singleton handled separately. A separate input-first enumeration checked exact neighbor sets, component-size multisets and edge counts for every nonempty fiber through n=8; connected totals were 1,1,2,5,16,65,326,1957. The supplied verifier was inspected, not run.

## originality

PASS

The established inverse algorithm and record-subset bijection are not credited as new. The additional claim identifies which adjacent transpositions preserve the pass output, classifies their connected components, and counts the outputs whose fiber graph is connected. The strongest available same-object source does not give these conclusions; its adjacency and aggregate cardinalities do not encode the position gaps. No distinct equivalent result was established in the bounded checks.

## value

PASS

The classical one-pass fibers come with a natural adjacency inherited from the bubble-sort graph. Cardinality alone hides disconnection; the record-gap test decides reachability inside a fiber and supplies all components without searching the factorial ambient graph. The exact all-size census then quantifies how rare the connected case is. The interest lies in these structural and enumerative conclusions, not in renaming the established subset parameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
