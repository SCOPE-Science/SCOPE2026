# Scientific review

## Correctness — PASS

The statement fixes a concrete \(16\)-vertex Cayley graph and the ordinary three-cut convention. The verifier builds every cut face using a Boolean-zeta method and independently retests membership by exhaustive disconnected-triple scanning. It finds \(384\) disconnected triples and \(65{,}162\) nonempty faces. A sequential element matching yields exactly one critical vertex, thirteen critical eleven-cells and two critical twelve-cells. The complete \(519{,}328\)-incidence directed Hasse graph admits a topological ordering; the matching is therefore acyclic. An exact signed gradient-path recursion gives a \(13\times2\) integral boundary matrix with a unit minor of order two, so both Smith invariant factors are \(1\). Hurewicz in dimension \(11\) identifies the attaching maps with this matrix, giving the eleven-sphere wedge. The independent Alexander-dual calculations confirm the rank over four fields but are not substituted for the integral proof.

## Originality — PASS against inspected evidence

The foundational 2023 cut-complex paper [1] and its 2024 continuation [2] give general constructions and other families, not this homotopy classification; the former's complete-skeleton criterion fails for this graph. The previously indexed rook-graph family [3] establishes the **comparison** rank \(27\) but cannot imply the Shrikhande rank \(11\) because the clique/rectangle structure differs. A published Shrikhande independence-complex computation [4] is a different functor and supplies no reduction. The 2026 strongly regular clique-complex paper [5], inspected at abstract level, likewise studies a different complex. Searches of public research records and the current accessible claims found no equivalent or stronger Shrikhande three-cut result. The possibility of unindexed equivalent work is not excluded.

## Value — PASS

This is an exact integral homotopy type for a canonical strongly regular graph, not a small numerical improvement. The Shrikhande and rook graphs have identical parameters \((16,6,2,2)\), yet their ordinary three-cut complexes have different eleventh Betti numbers, \(11\) versus \(27\). The contrast is controlled by distinct four-vertex connectivity patterns: the Alexander dual has \(60\) versus \(44\) tetrahedra despite the same counts of connected three-vertex sets. This supplies a motivated topological distinction in a standard pair of cospectral graphs, advancing the graph cut-complex classification beyond the rook and other existing families. No larger classification or equivariant action is asserted.

## Closest literature and scientific limits

The closest same-functor work is [3], whose rook-only description cannot be transported across the strongly regular parameter coincidence. The key finite computations are provided as executable programs, including exact integer cancellation. The proof does not generalize automatically to Doob graphs or other cut sizes. An independent mathematical audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
