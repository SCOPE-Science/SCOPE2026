# Scientific review

## Correctness

**PASS.** Character orthogonality proves that the pure graph state's cut spectrum is flat, with rank equal to that of the cut-adjacency matrix over the prime field. The complete integer Smith-factor table follows from exhaustive exact minors on the stated twelve-vertex graph, checked with `verify_smith.py` using only integer arithmetic. A separately constructed graph and prime-field Gaussian elimination in `verify_modular.py` give the full entropy histograms. Hadamard's inequality supplies the rigorous upper bound \(216\) on any nonzero relevant minor and excludes further prime exceptions. Both programs passed the stated tests. No extrapolation from finite graph sizes is made.

## Originality

**PASS on inspected evidence, provisional.** Hein, Eisert and Briegel establish the qubit rank formula; Looi and collaborators establish the qudit construction. Cabello and collaborators and the documented twelve-qubit rank-index database already cover the binary case in principle. Only the integral Smith distribution and the additional characteristic-five entanglement law are assessed as contributions. The full results on generalized Petersen qudit cuts and line-graph qudit cuts do not cover the icosahedron: the latter cannot specialize to it because its vertex neighborhood is a pentagon. Unindexed Smith or qudit tables remain a priority risk. The large binary database archive was not itself inspected.

## Mathematical value

**PASS.** A natural quantum entanglement statistic is resolved completely for all vertex cuts of a highly symmetric canonical network. The characteristic-five loss is not an arbitrary parameter slice; it is tied to the graph's fivefold neighbor pentagons, while a different two-primary phenomenon gives a distinct entropy distribution. The exact integer Smith table supports all prime dimensions simultaneously. It is a reproducible benchmark, not a claim of practical quantum advantage.

## Limits and literature

The conclusion is specific to a pure unit-weight graph state on the twelve-vertex icosahedral skeleton and prime-dimensional qudits. Known binary rank indices are credited, not claimed as original. Relevant primary sources are Hein–Eisert–Briegel (2003), Looi–Yu–Gheorghiu–Griffiths (2007), Cabello–Danielsen–López-Tarrida–Portillo (2010), the documented twelve-qubit rank-index database, and the published generalized Petersen and line-graph qudit results listed in `RESULT.md`. Residual priority uncertainty and absence of independent scientific audit are explicit.

Self-review: passed. Independent audit: not yet performed.
