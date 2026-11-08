# Self-review

## Correctness — PASS
The result is restricted to homogeneous coherent hopping, one rank-one absorber, and the unique missing-edge partner as initial site. The graph is correctly reduced to an invariant three-state space with distinct eigenvalues and no trap-orthogonal eigenvector; therefore all amplitude in the initial state is absorbed. The explicit \(3\times3\) integrated-state matrix satisfies the Lyapunov equation exactly, proving the unconditional mean time formula for all \(n\ge2\). A symbolic certificate and 33 independent finite matrix calculations passed. There is no extrapolation from finite tests to the infinite family.

## Originality — PASS on examined evidence
The general cyclic/bright trapping-subspace method and, in particular, capture-probability projections are pre-existing. The claim's distinguishing invariant is the *mean first absorption time* and its optimum on all cross-polytope networks from the unique nonneighbor. Razzoli–Paris–Bordone (arXiv:2011.13794, sections on strongly regular graphs and conclusions) determine capture efficiencies but do not supply this mean time; the dimension-reduction method makes the present calculation feasible but is not itself the stated lifetime identity. Alterman–Berman–Strauch (arXiv:2309.00164, sections III–V and Appendix) solve a different complete-graph adjacency model, not one with a deleted perfect matching. Rebentrost et al. (arXiv:0807.0929, model and applications) supply the earlier physical context. A published cross-polytope coherent state-transfer result concerns unitary fidelity, not lossy lifetime. Searches of the available prior research ledger and research index found no claim covering this exact lifetime. This is not proof of historical uniqueness, and unindexed or inaccessible papers remain a priority risk.

## Mathematical value — PASS
The graph is a canonical growing strongly regular family. It exhibits an especially sharp transport anomaly: starting at the only vertex not directly linked to the absorber leads to certain capture within \(O(1)\) mean time uniformly in graph size, whereas starting at any neighboring site captures only with probability \(1/(2n-2)\). The exact mean and absorber-strength minimizer distinguish accessible and protected subspaces quantitatively. Such selectivity is relevant to designing trap-based coherent transport benchmarks and cannot be inferred merely from graph degree or distance. The result is not claimed to establish a macroscopic phase transition.

## Closest literature and limits
The closest explicit graph transport framework is arXiv:2011.13794; the closest mean-transfer-time comparison is arXiv:2309.00164, which treats fully connected networks. The model omits dephasing, random disorder, interactions and multiple absorbers. This mathematical review cannot establish absolute historical priority or experimental validation.

Self-review: passed. Independent audit: not yet performed.
