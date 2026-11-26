# Independent mathematical audit

## correctness

PASS

For any fixed set of two-labelled vertices the unique cheapest completion labels an outside vertex one exactly when it has no neighbour in that set. I independently encoded only the two-label membership bits, with 4 column symbols and 256 overlapping four-column states, charging the optimized central-column weight on each of 1024 arcs. Synchronous relaxation stabilized and all arc slacks were checked. Exactly seven of the 244 tight arcs have a tight return path; they are precisely the arcs of the period-seven word in the finding. This proves the bound for every length by telescoping, and forces any minimum of weight 8k to follow that cycle. Each starting phase gives a distinct labelled function and the optimized completion recovers the stated labels. Direct checks give eight discrepancies for each nonzero shift in one period, hence 8k overall. The argument applies at k=1 as well: the spoke and two inner offsets in the local rule are exactly the stated neighbours.

## originality

FAIL

Distinct indexed record 74c79c34fad1 explicitly classifies the same seven minima for the same labelled graphs and gives the identical period word up to rotation. As a direct comparison of the displayed labels shows eight discrepancies for each of the six shifts, the Hamming claim is mechanically implied even though not printed there. The weight formula and exhibited period-seven construction are older still. The matching indexed classification has a later catalogue date than the frozen record, so this is present-day coverage, not a finding about who had priority.

## value

FAIL

Rigidity at all multiples of seven is a meaningful improvement over knowing only the optimum weight, but the same rigidity is already in the indexed record. The stated separation is an elementary read-off from that result's exact seven-word classification. The frozen result supplies no distinct structural or exact-invariant contribution beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
