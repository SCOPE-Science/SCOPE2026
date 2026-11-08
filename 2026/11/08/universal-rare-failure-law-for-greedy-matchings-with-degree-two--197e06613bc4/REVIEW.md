# Scientific review

## Correctness — PASS

The theorem is restricted to even orders \(N\ge6\), simple forbidden graphs of maximum degree at most two, and random feasible-edge sampling. For every fixed set of up to four vertices, a one-step hazard estimate proves a uniform \(O((s/N)^k)\) survival bound. Its application to the exact survival ratio of one missing edge bounds each recurrence perturbation by \(O(s/N^3)\). The isolated-edge reference factors telescope to \(3/(N^2-1)\), and all perturbations sum to \(O(\log N/N^3)\). No step uses false independence of the residual vertices. The standalone exact-rational checker passed 28,833 assertions, including an independent small-instance exhaustive edge-priority method. These finite assertions do not establish the asymptotic theorem; the analytic moment bounds do.

## Originality — PASS, with residual priority risk

Arnosti (2021; https://doi.org/10.1287/stsy.2021.0082) studies the same RANDOM-EDGE rule but compares algorithms on random bipartite inputs; its theorems do not bound individual forbidden-pair survival on arbitrary deterministic near-complete nonbipartite inputs. Dyer and Frieze (1991; https://doi.org/10.1002/rsa.3240020104) introduced the general random feasible-edge algorithm, with published descriptions focusing on approximation guarantees and forests; complete inspection was not possible. Tang, Wu and Zhang (2019; https://arxiv.org/abs/1907.05135) study different vertex-first algorithms. An exact special-case law for the deletion of a perfect matching does not imply the present arbitrary degree-two-deletion result, even though the new theorem includes that example. A finding with the same shape-uniform failure constant and conditional location law was not identified in the checked sources or mathematical-research records. This is a best-knowledge originality assessment, not proof of worldwide priority.

## Value — PASS

The leading constant is not the naive probability that two uniformly sampled vertices form a missing edge: it is \(3/2\) times that value. Crucially, the amplification does not depend on the number and lengths of forbidden path/cycle components, and conditional failure locations become uniform over the actual deleted edges. This resolves a natural structural question about the reliability and localization of random greedy matching failure in dense imperfect graphs. Uniformity over all degree-two defects is a substantive extension beyond symmetric matching-deletion cases, not merely another finite-parameter computation.

## Limitations and source access

The proof does not cover maximum forbidden degree greater than two, alternative greedy selection rules, or sharp explicit finite-size error constants. The 1991 foundational primary paper was available only in abstract/metadata form despite searches for lawful full text. Hence historical priority remains a residual risk. The checked Arnosti primary paper was accessible in full, including theorem statements, algorithms, proofs, discussion and appendices. The computation has no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
