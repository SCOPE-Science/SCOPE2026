# Independent mathematical audit

## correctness

PASS

The frozen proof is correct. Augmenting by empty and full traces permits an induction on the binary union/join decomposition. With both marked child sets nonempty the two augmented families lose one overlap (empty at a union, full at a join) and gain at most one opposite extreme. An unmarked child adds only an extreme, and the singleton has augmented size two. The threshold witness creates t-m chosen prefix traces of sizes different from m-1 alongside the m distinct marked clique traces. The repair uses the same constructions at their exact orders: for t<=m the edgeless graph, star, or (t-1)-clique plus isolates on m marked vertices work; for t>=m one adds t-m witnesses to the marked clique, with the marked singleton and marked edge handling m=1. To see the prefix graph is threshold, add clique vertices as dominating vertices in descending index and each prefix witness as an isolate just before its largest indexed neighbor (length 0 goes last). Each constructed graph has max(m,t) vertices, the trivial lower bound from one trace per vertex and the need for m markings. To increase order without changing t, substitute an independent set for a single vertex, mark no new copies, and observe its open trace and the old traces are unchanged. The graph remains a cograph by replacing the corresponding cotree leaf. The complement map transfers the theorem to closed traces at each fixed order, not within one fixed graph. The original VC dimension result follows at m=3 and m=2. Replay: repairs/3/RESULT.md; a separate standard-library enumeration in /workspace/branches/independent_checks.py checked both augmented bounds on 535 labeled cographs and 15475 nonempty marked pairs through five vertices. The uploaded verifier was inspected, not executed.

## originality

PASS

Fresh assessment only of the repaired order-dependent result, not a PASS for the frozen claim of a new sharp augmented 2m bound or its already implied VC dimension. The matching same-day original states the identical all-vertex bound and proves the identical augmented inequality, but its witness-order theorem requires all witnesses to be external and obtains 3m. In the repair the exact minimum max(m,t) for every attainable count, equivalently the spectrum conditioned on total order, uses different witnesses with the marked vertices contributing distinct traces. That stronger control of order does not follow from the matched external construction or the class-wide bound. Chronological priority between the same-day records is not asserted.

## value

PASS

Graph order is a genuine resource constraint when vertices both name parameters and witness traces. The repair determines how many vertices are needed for every achievable count and how much reuse of marked vertices is possible, in contrast to the larger external-only witness requirement. A researcher with a graph-order cap can use the complete interval immediately; this is not a new claim about general first-order types or a relabeling of the sharp coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
