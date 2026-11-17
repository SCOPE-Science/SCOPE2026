# Scientific review

## Correctness — PASS

The exact domain consists of two specifically defined tournaments on seven vertices, with all 21 oriented edges given by a fixed increasing orientation and one two-step reversal. Their only possible directed cycle is the identified three-cycle. Thus an arc subset is a directed linear forest exactly when each source and target is used at most once and this triangle is absent. The provided standard-library checker exhaustively computes all face sets by separate combination and extension procedures, obtains matching face counts, builds the augmented simplicial chain matrices, verifies squared boundaries are zero, and agrees between row and column Gaussian elimination. The exact rank tables yield the stated reduced \(\mathbb F_2\)-homology. An exhaustive finite proof is sufficient for this finite finding. It does not claim integral homology or infinite extrapolation.

## Originality — PASS, subject to residual bibliographic uncertainty

The 2026 Deshpande–Sawant manuscript treats the same general directed-linear-forest object and includes the known conflict-hypergraph face characterization; no novelty is assigned to that reduction. Its structural results do not cover this particular equal-face-vector/different-homology comparison. Caputi–Collari–Di Trani–Smith calculate the Euler characteristic for transitive tournaments and one reversal of their outermost edge, and establish a sphere-wedge property for intact transitive tournaments. These results do not imply either of the two mod-two rank tables: the present two reversals are interior two-step arcs, and equal Euler characteristics are compatible with distinct Betti ranks. Semantic comparisons against indexed research records and source/alias searches did not identify an equivalent statement. Bibliographic incompleteness remains possible; no independence is claimed.

## Value — PASS

The natural one-arc perturbation of a transitive tournament is a direct stress test of the newly studied directed-linear-forest complex. Seven is the first number of vertices in this two-step reversal family where arc position affects mod-two homology. The two complexes nevertheless have the same entire face vector and the same unique directed-triangle count. Thus face enumeration, all derived face-polynomial invariants, and Euler characteristic fail to determine the graded topology even within this tightly specified perturbation family. This is a motivated boundary example rather than an arbitrary numerical slice. The result does not assert a general tournament classification.

## Closest literature and limitations

Deshpande–Sawant, arXiv:2602.14936 (2026-02-16), Sections 3 and 5.2; Caputi–Collari–Di Trani–Smith, arXiv:2208.04656, *Mathematika* 70 (2024), Sections 3 and 5. Exact mod-two calculation only; integral homology, all-order patterns and homotopy types are not established. A differently formulated prior computation is a residual risk.

Self-review: passed. Independent audit: not yet performed.
