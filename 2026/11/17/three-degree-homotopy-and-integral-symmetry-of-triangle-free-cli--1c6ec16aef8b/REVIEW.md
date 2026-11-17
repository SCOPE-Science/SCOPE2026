# Scientific review

## Correctness: PASS

The face partition is exhaustive: no central vertex permits two outer vertices in one block; one central vertex permits at most one per block; two central vertices permit no outer vertices; and three central vertices are forbidden. Consequently the complex is exactly a union of joins plus discrete central edges. The zero- and one-skeleta of a simplex have the stated free integral homology, so the join products and their connectivity bounds are valid for all quantified parameters. Both attaching maps from the connected intersection are nullhomotopic, giving the nonequivariant wedge splitting. The natural relative homology sequences identify the integral automorphism modules without requiring an equivariant wedge splitting. Transfer after barycentric subdivision proves the quotient's rational acyclicity. The actual standalone verifier independently checked six cases and 255 oriented Lefschetz equalities. No extrapolation from finite tests is used in the symbolic proof.

## Originality: PASS, with risks

The closest 2026 source, Ghosh--Selvaraja, proves shellability for diamond-free chordal graphs; the new family is chordal but contains an induced diamond, and that paper does not give the stated homotopy or group modules. Namiq's chordal clique-skeleton theorems concern different complexes and do not imply the triangle-avoiding subset construction. The generalized split-join edge-ring literature concerns graph independence complexes; its full text was not accessible, so an implicit result is a residual risk. The single-universal-vertex windmill result does not cover the larger central clique, its new circle module, or the central permutation module in middle homology. Actual searches of the relevant mathematics index and publicly available primary literature did not identify equivalent or stronger coverage. The absence of a search hit is not a novelty proof; equivalence in unindexed sources remains possible.

## Value: PASS

This natural clique-join graph is chordal but has overlapping triangles, so existing diamond-free shellability statements do not settle its topology. The theorem identifies three distinct nonzero integral homology dimensions with exact multiplicities for arbitrary nonuniform outer-clique widths, supplies a complete integral automorphism-module structure, and yields a rationally acyclic symmetry quotient. These structural facts are not implied by face counts, shellability criteria, or prior single-center cases. The example with two central vertices and two three-vertex blocks already exhibits three different homology degrees.

## Sources and scientific limits

Primary full text inspected: Ghosh--Selvaraja, arXiv:2602.09623v1, especially Sections 1, 3, 4; Namiq, arXiv:2603.17776v2, especially Sections 1--4 and the Alexander-dual distinction. The abstract of Rather, arXiv:2606.24822, was read, but its full text could not be retrieved. Residual originality risk persists for unindexed, inaccessible or unpublished work. The finite checker only verifies selected cases and signed traces; the all-parameter claim requires the written proof. No integral orbit-space classification or equivariant homotopy splitting is claimed.

Self-review: passed. Independent audit: not yet performed.
