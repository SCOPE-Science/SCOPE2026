# Scientific review: four-periodic rigidity on cycles

## Correctness — PASS

The statement concerns all labelled simple cycles of length at least three and the exact expansion/contraction rule for inclusion-minimal dominating sets. The proof reduces minimality to a local run condition: zero-runs and one-runs have length at most two, and a double-one run is flanked by two-zero runs. It then gives explicit legal moves for every configuration containing singleton one-runs, and shows that all-double configurations are exactly the periodic \(1100\) states. Every candidate move from those periodic states fails minimality when the cycle has at least eight vertices. Small cycles of lengths three and four are treated separately. Thus the proof is not a finite extrapolation. A separate local finite-state automaton has a unique recurrent directed four-cycle, and direct enumeration confirms the claim through length eighteen. Both accompanying standard-library programs executed and passed.

## Originality — PASS, with residual priority risk

Beaton's 2024 article introduces the exact expansion/contraction rule, proves connectedness for trees and split graphs, identifies disconnected prism-type examples and works out \(C_5\), but does not classify rigid minimal dominating configurations across all cycles. Adaricheva and colleagues' 2021 modulo-four result concerns a different reconfiguration graph, with **all** dominating sets under addition/removal and Hamilton-path existence as its property; it implies neither the present state classification nor rigidity. The closest published published-finding corpus four-periodic classification covers *minimum isolating sets* under unrestricted one-replacement, a different predicate and move rule. Searches of equivalent formulations, cycle patterns and index records did not identify a covering statement. An unindexed or later equivalent is still possible; this is not a claim of guaranteed global priority.

## Value — PASS

The 2024 introduction of expansion/contraction asked how inclusion-minimal solutions behave when different numbers of tokens are permitted. This theorem supplies a sharp infinite-family mobility obstruction, including the exact number and form of all frozen configurations and the small-cycle exception. Unlike a count for an arbitrary selected graph, it answers a natural structural question for every cycle and provides an explicit move certificate for every other state. The result does not establish the connectedness or diameter of the remaining states, nor any bound for arbitrary graphs.

Self-review: passed. Independent audit: not yet performed.
