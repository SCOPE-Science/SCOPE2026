# Review: critical-radius binary de Bruijn identifying codes

## Correctness

PASS. For every length \(n\), each prefix twin pair \(u0,u1\) requires at least one sensor, yielding the \(2^{n-1}\) lower bound by disjoint counting. Explicit 16-, 64-, and 256-element witnesses attain this bound, and `verify.py` exhaustively checks all in-ball identifiers for the respective 32, 128, and 512 target vertices using both reverse-graph exploration and overlap formulas. Finite verification is complete for the three claimed values only; no broader computational inference is made.

## Originality

PASS (qualified). The directly inspected 2014 foundational preprint states the lower bound but explicitly leaves the sharp threshold \(n=2t-1\) unresolved after its larger construction. Its small \((3,2)\) case requires seven vertices, whereas the three new cases attain the lower bound. Searches over the published published-finding corpus index, directly relevant titles did not identify the same finite triple. This absence is not a uniqueness proof: other equivalent graph-code or network-monitoring constructions might be unindexed. The classification is graph-theoretic monitoring in a computer-network topology, assigned 68R10.

## Value

PASS. The three exact optima answer the initial nontrivial cases of a parameter boundary explicitly singled out as open in the primary literature. They give provably minimum sensor costs, show that the exceptional excess at radius two does not persist at radii three to five, and offer verified benchmarks for attempts at the general threshold problem. This is not an arbitrary finite computation or a claim about all radii.

## Closest literature and limitations

Boutin–Horan Goliber–Pelto, arXiv:1412.5842, Theorems 3.5 and 3.9 and the statement that the \(n=2t-1\) optimum remains open. Exact equivalence with other network-code parameterizations is a residual historical-priority risk. The result has no scope beyond the stated alphabet, direction, and three parameter pairs.

Self-review: passed. Independent audit: not yet performed.
