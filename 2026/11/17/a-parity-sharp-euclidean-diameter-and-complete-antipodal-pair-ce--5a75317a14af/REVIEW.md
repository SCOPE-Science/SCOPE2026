# Scientific review

## Correctness — PASS

The flow decomposition proves that all vertices are path indicators. The distance is exactly their arc-set symmetric difference, and inserting any uncovered internal vertex strictly improves the distance. Removing an internal vertex of an adjacent common-vertex pair likewise strictly improves it, so the extremizers are controlled by maximum independent sets of a path. The proof explicitly handles endpoint conventions, \(N=3,4\), and counts unordered pairs without duplicate cores. Strict convexity excludes every nonvertex pair. Independent bitset enumeration covers 2,794,155 vertex pairs for \(N=3,\dots,13\) and verifies 4,800 random larger pairs. Limitation: finite computations do not prove the general statement; the displayed exchange argument does.

## Originality — PASS, priority provisional

The 2024 Dugan preprint's full Introduction, Definitions 2.7–2.9, Propositions 5.1–5.3 and final remarks were inspected. It identifies the same flow polytope and its path vertices but studies its f-vector and face support. An f-vector is invariant under affine deformation and does not determine this edge-coordinate Euclidean diameter or the complete equality classification. The 2017 Corteel–Kim–Mészáros paper addresses volume and lattice quantities. Related published records on complete-flow Euclidean inballs, all-acyclic-flow Minkowski asymmetry and complete-layered-path skeleton diameter concern distinct mathematical invariants, not this squared chord maximum. Web searches for the exact parity formula, arc-incidence symmetric-difference maximizers, and Chan–Robbins–Yuen Euclidean diameter found no equivalent statement. Priority is not certified: unindexed results or alternative presentations may exist; the 1992 monotonic shortest-path polytope work was available as an abstract only and concerns the graph metric.

## Mathematical value — PASS

The Chan–Robbins–Yuen family is a longstanding naturally embedded family with exponentially many vertices and a large face lattice; the result computes a sharp Euclidean geometric invariant and identifies **every** pair attaining it. The alternating-core rigidity in odd order versus a linearly movable core in even order yields a nontrivial exact antipodal census, rather than a numerical bound or a single small instance. The result is intentionally restricted to the natural arc metric, not to arbitrary affine realizations.

## Closest literature and limitations

The primary reference is Dugan (arXiv:2409.15519v1), with the earlier flow and volume constructions of Chan–Robbins–Yuen and Corteel–Kim–Mészáros. The strongest adjacent metric records concern inballs and affine asymmetry, not pairwise Euclidean distances. Historical priority remains provisional, and all finite tests are only supporting evidence.

Self-review: passed. Independent audit: not yet performed.
