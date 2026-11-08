# Scientific review

## Correctness — PASS

The main statement is for every integer \(p,q\ge2\), every \(h\ge0\), and every strictly convex real filter on \([0,\infty)\) with \(f(0)=1\), for the directly actuated coordinate system specified in RESULT.md. The four orthogonal Laplacian eigenspaces were reconstructed from the block Laplacian. For two uncontrolled vertices on one side, a local difference vector is always an eigenvector. For one omitted on each side, every nonzero supported vector activates three distinct Laplacian spectral levels when the side sizes differ; strict convexity forbids identification of all three. In the balanced case, exactly the two indicated level-pair collisions admit an eigenvector supported on the omitted pair. The one-omission case is always controllable for positive steps. This supplies both necessity and sufficiency and handles the zero-step boundary separately. Exact cubic factorization and derivative signs prove uniqueness of the RK4 exceptional steps. A standalone standard-library checker passed 100 exact-rational step matrices, 1,884 exact Kalman-rank checks and 1,584 pair-omission checks; these are finite corroboration, not an infinite proof.

## Originality — PASS on inspected evidence

The published foundations of coordinate and graph controllability explain PBH and zero forcing, while cograph results cover original Laplacian dynamics. The March 2015 source studies polynomial spectral filters and, in particular, balanced and unbalanced complete bipartite graphs, but frames the problem as consensus convergence and spectral clustering. The present result concerns the exact *minimum number and placement of independent coordinate actuators* for every strictly convex filter and the two resonance exceptions on balanced graphs, including positive stochastic RK updates that lose minimum-input controllability. Direct comparison of the mathematical implications of those papers does not supply the stated all-filter classification. Its proof uses classical tools credited as such. The residual risk is unindexed publication-priority overlap in discrete-time graph controllability; a self-review is not independent certification.

## Mathematical value — PASS

A graph controller whose implementation applies a polynomial spectral filter can lose controllability even when its state-transition matrix is strictly positive, stochastic and contracting away from consensus. For all unequal complete bipartite networks, the sharp \(N-2\)-input budget is immune to every positive-step resonance of a strictly convex filter; for every balanced graph, a closed pair of scalar equalities gives the exact actuator-budget jumps. These are natural infinite-family classification and stability-of-actuation results, with explicit practically reproducible RK2 and RK4 examples; neither a finite parameter slice nor a mere renamed PBH test.

## Closest literature and limits

- Apers and Sarlette, arXiv:1503.01269v1 (2015): polynomial filtering and balanced/unbalanced bipartite spectra, but not the specified minimum coordinate-control resonance classification.
- Monshizadeh, Zhang and Camlibel, arXiv:1403.4868v1 (2014): zero-forcing and qualitative graph-pattern controllability, rather than a fixed filtered Laplacian state matrix.
- Burgarth et al., arXiv:1111.1475v1 (2011): zero forcing and graph-based controllability foundations.
- Mousavi, Haeri and Mesbahi, arXiv:1802.03599 (2018): original cograph Laplacian controllability; does not itself address filter eigenvalue collisions.

The theorem does not concern transformed discretized inputs for a controlled ODE, nonconvex filters, arbitrarily weighted graphs or robust numerical controllability. Prior art beyond the inspected sources may exist.

Self-review: passed. Independent audit: not yet performed.
