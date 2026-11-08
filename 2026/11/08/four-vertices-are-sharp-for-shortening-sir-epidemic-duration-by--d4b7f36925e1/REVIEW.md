# Scientific review

## Correctness — PASS

The model includes every one-edge insertion and every chosen source for graph orders \(1\), \(2\), and \(3\), even when the original graph is disconnected. First-event SIR backward equations terminate because each transition moves one vertex forward in the irreversibility order \(S\to I\to R\). Direct algebra produces eight isomorphism-representative duration differences, each nonnegative on the full domain \(\beta>0\). An exhaustive 38-case labeled symbolic replay checks the missing cases and all coefficient signs. At the four-vertex witness, two algorithmically distinct exact rational evaluations produce the same duration and final-size changes, with strict, correctly signed rational differences. No extrapolation from finite numerical sampling proves the universal portion.

## Originality — PASS (inspected evidence, provisional)

The nearest research is Sharkey et al.'s 2012 exact network SIR tree equations, Holme's 2013 computational study of duration versus contagion in a discrete-time SIR model, and Holme's 2017 exact small-graph work on different node-importance objectives. No inspected theorem or table specifies the sharp four-vertex edge-insertion counterexample or implies the universal three-vertex nonnegative difference. The underlying first-event recursion is standard; the new contribution is the graph-order boundary and its explicit signed contrast. Originality is best-knowledge within examined literature and recorded search results, not a claim to exhaustive historical priority.

## Value — PASS

Expected epidemic lifetime is a natural operational objective distinct from expected number of cases. The established sharp minimal graph order separates a globally valid small-network monotonicity principle from its first possible failure and demonstrates a strict direction-of-effect conflict under adding a single contact. The four-vertex witness is minimal, involves no artificial weights or competing rates, and shows quantitatively why reducing contacts need not shorten the duration of every transient outbreak. The result is a structural benchmark for finite stochastic network models, without an empirical policy recommendation.

## Closest literature and residual limitations

Sharkey et al. derive exact moment equations for stochastic network SIR, not the edge comparison. Holme 2013 reports duration peaking versus transmission rate in a discrete-time fixed-period model, not the same Markovian contact-addition problem. Holme 2017 provides general exact finite-state methodologies and focuses on influence maximization, vaccination and sentinel detection; software capable of calculating duration may encode additional unexamined examples. Earlier exact finite-graph tables or unpublished notes could affect historical attribution. No theorem is asserted for the sign of the difference at every transmission rate on the four-vertex pair.

Self-review: passed. Independent audit: not yet performed.
