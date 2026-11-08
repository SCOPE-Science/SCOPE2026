# Scientific review

## Correctness — PASS

The support count is exactly Markov with transition \((k)_j{n\brace j}/k^n\). The proof derives one-level holding times, a uniformly small probability of skipping the two-survivor state, and a coupling to its exactly geometric holding time. For the expectation hierarchy, fixed-level hitting probabilities are proved to approach one exponentially fast, while inclusion-exclusion controls each fixed-level exit rate and the entire remaining upper tail. These are analytic arguments valid for all integer \(n\ge2\) and every fixed truncation order \(r\ge2\). An independent finite-state checker passed 2,501 assertions, including complete small ballot enumerations. It does not replace the proof.

## Originality — PASS (qualified historical priority)

The motivating July 2026 paper analyzes power weights with \(\alpha>0\); the new endpoint uses positive-support-only weights, not covered by those assumptions. Standard occupancy theory has the one-step Stirling formula, but it does not by itself state the iterated extinction-time geometric approximation or all fixed-order exponential corrections. Relevant repeated-balls-into-bins processes differ by allowing bins from a fixed location set. Targeted literature and published-finding corpus queries found no directly covering claim. Risk: a prior general theorem about iterated restricted occupancy could subsume the statements; only part of the motivating full text could be retrieved for material inspection.

## Value — PASS

The zero-reinforcement endpoint is a mathematically natural boundary of the reinforced voting model. The theorem establishes not just an exponential order but a full distributional law with an explicit total-variation bound, and identifies an unlimited hierarchy of exponentially separated expected-time contributions. This describes the mechanism of delayed consensus through successive small active sets. The exact recursion makes the finite laws reproducible.

## Limits and evidence

No fixed-positive-exponent result is claimed. The motivating paper's later sections and some potentially relevant occupancy articles were not fully available for examination. The originality assessment is therefore conditional on that material and can be revised by independent historical review. The standalone checker is `check.py`.

Self-review: passed. Independent audit: not yet performed.
