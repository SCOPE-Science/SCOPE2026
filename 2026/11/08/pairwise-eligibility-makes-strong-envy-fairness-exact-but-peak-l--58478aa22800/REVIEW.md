# Scientific review

## Correctness — PASS

The argument is a direct complete proof: the last-job invariant gives arbitrary-weight online strong EF1, unit pairwise inequalities force half-splits, the odd residual jobs reduce exactly to a capacitated graph orientation, and a capacitated Hall argument gives the subset density optimum. The star construction supplies both fair and unconstrained optimal values. All quantifiers and distinct weight regimes are explicit. The bundled independent enumeration agrees in every stated finite case; no finite test is treated as a universal proof.

## Originality — PASS, with residual risk

The October 2026 primary source proves general strong-EF1 nonexistence and a three-machine online obstruction requiring an all-three-eligible job; its Section 5 and Appendix D do not give the rank-two online guarantee or the exact unit-case optimal makespan. The February 2026 graphical-orientation primary source analyzes different fairness definitions (proportionality and ordinary envy) and does not imply strong pair-restricted fairness. Hakimi/Frank–Gyárfás provide the classical orientation-feasibility lemma, which is expressly credited, rather than claimed new. Targeted literature searches and the available related-claim index did not reveal a stronger theorem implying this entire joint fairness/optimization result; absence of a match does not prove uniqueness. The chief residual risk is an unindexed graph-based scheduling note applying the classical orientation lemma to exactly these strong-envy constraints.

## Value — PASS

The result isolates a natural, application-driven structural escape from the source's online impossibility: jobs eligible to at most two machines. It does more than give existence, classifying *all* unit-size strong-EF1 assignments, determining the exact best peak load and giving a polynomial-time optimizer. A family of realistic parallel pair-eligible jobs shows why online fairness does not guarantee throughput efficiency: the fair makespan ratio diverges linearly. These are motivated quantities and complete statements, not arbitrary finite instances or a renamed graph theorem.

## Relationship and limitations

The positive guarantee is for pair-restricted strong EF1/EFX, not for the ordinary EF1 notion in graphical chores. The explicit maximum formula requires unit processing times; unequal weights retain only the online strong-EF1 theorem. The star example is not a universal price-of-fairness upper bound. Relevant references, source comparisons and the exact reproducible tests are in `RESULT.md`, `AUDIT.json` and `VERIFICATION.md`.

Self-review: passed. Independent audit: not yet performed.
