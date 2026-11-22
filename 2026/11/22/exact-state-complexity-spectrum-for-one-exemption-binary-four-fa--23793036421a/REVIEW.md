# Research review

## Correctness: PASS

The invariant for the explicit finite factor-mask automaton establishes recognition for every finite binary input. Breadth-first construction proves that all \(19{,}205\) reachable states are included. Recursive Moore refinement equates states exactly when they agree on acceptance under all suffixes up to increasing depth; stable refinement is exactly the full Myhill–Nerode congruence. The separate numeric-suffix Hopcroft-style implementation gives the same sixteen values. Executed tests include both positive length-eighteen witnesses and negative direct evaluations, explicit acceptance/transition congruence tests, and sharp suffix-depth termination. These are genuine finite exhaustive certificates for all input words, rather than finite-length extrapolation.

## Originality: PASS against inspected evidence

The 2026 shortest-absent-substrings paper addresses the detection and computation of absent factors, not the state complexity of monitors with one specified permitted absence. OEIS A375919 contains the fully universal baseline \(13{,}212\) states, which does not imply the sixteen state counts here. Published factor-spectrum and cyclic-cover computations involve different quantified properties. Relevant semantic searches did not reveal a result covering the entire one-exemption language family or its reversal asymmetry. Residual risk: a specialized unindexed DFA census may contain the values; the factor-spectrum full text was inaccessible and was not claimed to have been read in full.

## Value: PASS

Allowing one prescribed four-factor to be missing is a natural robustness modification to a universal substring monitor. Its exact minimal memory requirements depend substantially on *which* factor is exempt, with a sharp eight-valued classification, identifiable extremizers and unexpected reversal asymmetry. The result is a complete natural finite classification, not just a single routine state count or a reinterpretation of an existing all-factors baseline.

## Scope and limitations

The claim covers only binary four-factors, no multiple exemptions or higher-order asymptotics. Both finite certificate implementations are replayable and no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
