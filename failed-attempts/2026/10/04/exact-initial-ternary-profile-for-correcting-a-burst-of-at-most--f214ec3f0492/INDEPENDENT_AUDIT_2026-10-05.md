# Independent mathematical audit

## correctness

PASS

For each \(n=2,3,4,5\), codewords are compatible exactly when their one-deletion balls and two-consecutive-deletion balls are separately disjoint, so the optimum is the clique number of the explicitly constructed compatibility graph. The submitted branch-and-bound uses a proper greedy coloring only as an upper bound and branches exhaustively. A fresh independently written exact clique computation reconstructed every ternary word and both deletion balls and reproduced the optima \(1,3,7,13\). The displayed codes attain those sizes.

## originality

PASS

The closest nonbinary burst-deletion papers define the same at-most-two consecutive-deletion channel and develop general constructions/nonasymptotic bounds, but no inspected statement fixes these four tiny ternary maxima. Resultary and targeted exact-value searches did not locate the \(1,3,7,13\) profile. Thus the finite computation appears original at the statement level, while the absence of an indexed table is retained as a residual risk.

## value

FAIL

The computation is exact and reproducible, but the cutoff at length five is not mathematically motivated by a first transition, extremal boundary, classification theorem, or other structural breakpoint. It is an arbitrary initial finite slice of four tiny instances. Under the common value bar, exactness and novelty alone do not make this particular cutoff a worthwhile standalone mathematical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
