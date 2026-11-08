# Scientific review: cyclic five-point Lipschitz variance

## Correctness — PASS

The scalar maximizing problem is strictly convex after fixing the translation gauge; vertex extremality is equivalent to a connected saturated-constraint graph. Every possible vertex therefore comes from one of the exactly 2000 signed spanning-tree choices. `CHECK.py` independently enumerates all, tests their exact feasible parameter intervals, and proves the polynomial upper bound on each whole interval. The resulting 70 interior vertices split into five explicit orbits; one is strictly largest throughout the interior, and endpoint counts and equality cases are separately exact. For Hilbert targets, the pairwise upper bound and the exact first five-cycle Laplacian eigenvalue give the two sharp bounds. Explicit orthogonal Fourier embeddings attain the first branch, a regular pentagon attains the second, and equality conditions force the stated dimensions and congruence classes. Algebraic derivatives establish the unique gap maximum.

## Originality — PASS, qualified

Alon–Boppana–Spencer introduce finite metric spread and prove general principles; their graph case concerns integer edge distances and does not compute this two-distance five-point continuum. Addario-Berry–Janson–McDiarmid investigate random-graph spread, rather than the exact cyclic deformation. Naor's general nonlinear spectral-gap comparison does not imply the stated scalar-versus-Hilbert extremizer classification. Related five-cycle graph-metric scalar norms cover the endpoint \(t=2\), which is not asserted to be new; other known finite metric deformation and Hilbert-variance results involve different metric families. Search-based priority is not proof of uniqueness. Residual risk: an earlier paper might hide this exact five-point parameter calculation under a different name.

## Mathematical value — PASS

Finite metric spread is a natural metric concentration invariant; contrasting scalar and Hilbert targets quantifies the cost of target dimension. Here one continuous, highly symmetric metric deformation has a complete exact scalar/Hilbert phase diagram, sharply classified maximizers, a forced rank-four to rank-two transition at a geometric threshold, and a unique worst gap. These properties distinguish the finding from merely recomputing the graph-metric endpoint or enumerating one arbitrary finite metric.

## Verification limits

The finite certificate proves all scalar parameter inequalities exactly, not by sampling, using rational arithmetic over a complete family of active-constraint trees. Hilbert estimates and extremizers have a separate symbolic proof; no separate algebraic-number checker is asserted. Priority is qualified by discoverability of historical literature. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
