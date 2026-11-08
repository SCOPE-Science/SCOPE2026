# Scientific review

## Correctness — PASS

The exact claim concerns a recursively defined, labelled tree of triangular blocks, synchronous three-state threshold-one dynamics, and states of least period three from time zero. The proof first establishes that on a connected graph each such nonzero state is an everywhere-advancing three-phase coloring, then partitions rooted-subtree configurations by whether the root receives an internal successor. Nine explicitly enumerated local color pairs give both quadratic recurrences, with base counts \((2,1)\). Root support yields \(P_h=3A_h\) and the global color shift gives orbit size three. The bounded ratio recursion proves existence of the entropy constant and provides an exact strict inequality with the chain base. The included C++17 program tested the actual update over 14,351,121 finite states; the independent Python enumerator reconstructed the nine-case polynomial and the entropy approximation. Finite checks support, but do not replace, the infinite-height proof.

## Originality — PASS (qualified)

The October 2016 source by Gravner–Lyu–Sivakoff concerns activity and synchronization, not an exact line-graph tree periodic-state count. The full accessible 2018 treatment by Doba derives convergence and excitation rates without the present branching polynomial. The closest earlier triangular cactus chain has a linear (not quadratic binary-branching) transfer recurrence. A general initial-coloring **eventual activity** count cannot imply exact immediate period-three populations: its positive-activity set includes preperiodic trajectories. Mathematical-record searches did not identify equivalent published counts, but nonindexed priority remains a risk. The result is an exact graph-family formula, not a claim that the general successor-neighbor characterization is newly discovered.

## Mathematical value — PASS

Finite trees themselves synchronize under this model, whereas their line graphs acquire triangular excitation sources; this construction isolates the effect of branching in the simplest clique-block networks. The full-depth quadratic census, exact entropy series, and strict branching-versus-chain entropy separation answer a motivated structural question for an infinite family rather than tabulating isolated small examples. The comparison uses equal vertex density per triangle and does not claim arbitrary tree extremality.

## Sources, checks, and limitations

Primary sources inspected include Gravner–Lyu–Sivakoff (2016 preprint; open 2018 full text, in particular model definitions, Theorems 3 and 5, concluding remarks) and Doba (2018 complete article, in particular model, convergence, phase differences and activity results). Historical comparisons also include the triangular-chain recurrence and the cactus eventual-rate criterion. The present exact binary-branching calculation is not a stated corollary of either general activity theorem. The residual risks are literature indexing gaps and independent verification not yet conducted; the assertion does not extend to entrance times or to arbitrary line graphs of trees.

Self-review: passed. Independent audit: not yet performed.
