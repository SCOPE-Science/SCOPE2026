# Mathematical review

## Correctness — PASS

The written proof reconstructs the centered signed-incidence coordinates and derives the exact rim-extrema radial identity with no normalization ambiguity. Every directed triangle is ruled out by the single local edge constraint; an orientation containing both spoke signs cannot carry a longer directed cycle through the hub because a rim path from a hub-outgoing spoke to a hub-incoming spoke must cross a forbidden direction at a zero-to-one spoke transition. Only four constant-spoke/full-rim directed cycles are removed, giving the exact four-state transfer matrix. A run decomposition forces at least one source per one-run and sink per zero-run, and exactly one of each gives precisely \(m k(m-k)\) orientations. The minimum shell follows after comparing the constant-spoke boundary regimes. The actual accompanying Python verifier independently rebuilds all directed edges, uses Kahn acyclicity tests rather than the local criterion, and compares complete coefficient distributions and squared lengths for all \(4\le m\le9\): 349,440 orientations tested, 29,466 acyclic, 231 extra polynomial/boundary assertions. Finite tests do not replace the proof.

## Originality — PASS (priority provisional)

The nearest published geometric result, *Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes*, was inspected in its complete RESULT.md and proves the **largest** radius of a one-hub cone and farthest-point configurations, rather than the first **smallest vertex** radial shell or its all-radius enumerator. The available abstract of Mühlherr–Poullot focuses on flip-graph Hamiltonicity and an acyclic polynomial. The well-established graphical-zonotope/acyclic-orientation correspondence is credited as background, as are the classical total vertex count and prescribed-source/sink enumerations. Semantically targeted mathematical-record searches and comparison with accessible prior geometric claims found no statement whose implications subsume the joint four-state radial enumerator and sharp inner-shell counting classification. The primary 2026 full manuscript was inaccessible; this residual historical-priority risk is explicit and cannot be ruled out categorically.

## Value — PASS

The center-to-vertex radial distribution is a natural Euclidean invariant of a graphical zonotope, independent of its face-number enumeration or its body inradius. The complete four-state generating function is a uniform finite algebraic encoding of every radial shell for an infinite family, and the sharp first-shell formula exhibits an unexpected polynomial multiplicity with a parity transition. The bijection with uniquely sourced/sunk wheel orientations gives an exact geometric interpretation of its minimizers. This is a structural metric classification, not an isolated routine count.

## Scope and limitations

Unweighted wheels with rim order at least four only; the minimum is taken over **vertices**, not the convex body. No independent audit or external validation has been conducted. A separately indexed general acyclic-orientation-degree-distribution result might imply a formulation not detected in the available comparisons.

Self-review: passed. Independent audit: not yet performed.
