# Scientific assessment

## Correctness — PASS

The exact domain is every finite connected simple unicyclic graph and every prime-power field order for the alternating-rank statement, restricted to odd field order only for its representation-theoretic character conversion. The proof establishes a weight-preserving invertible leaf-plane split, the matching-exchange identity, the odd-core rank, the even-core Pfaffian cancellation with a nonzero next principal minor, and the exact count of nonzero weights satisfying a single multiplicative equation. A standalone implementation checks 126,870 exhaustively enumerated matrices across fifty-two field/graph configurations, including a nonprime field, plus 1,200 further deterministic samples. The proof, not finite enumeration, supports all quantified claims.

## Originality — PASS (provisional)

The archived 2014 Li–Yu paper gives support for pendant and matching rank mechanisms but only fixed-edge oriented graph matrices, not complete arbitrary finite-field support-conditioned rank distributions. The documented earlier cycle and tree character enumerators are the special cases without attached trees and without cycles, respectively. A more general one-vertex graph-amalgamation result can calculate polynomial rank distributions recursively; therefore computing the marginal character census alone is **not** an independently original claim. The specific nonrecursive support-wise criterion and universal conditional cancellation fraction, which explain exactly the dependence on nonzero edge values, are not stated in the compared sources and form the assessed additional assertion. This originality finding carries residual risk from equivalent weighted Pfaffian or rooted-tree formulas under different vocabulary; independent validation is not performed.

## Value — PASS

The support-conditioned classification is a natural structural refinement of the matching-number description of skew rank: it identifies the sole obstruction to rank depending only on edge support and quantifies that obstruction exactly for any finite field and any arrangement of branches. It turns an arbitrary weighted-matrix census into a uniform support polynomial and determines which unicyclic graphs have no coefficient-sensitive rank for any assignment. This is useful for graphical nilpotent Lie algebras and their character degree statistics and is not merely a known cycle count repeated for a specific numerical graph.

## Scientific limitations

The graph is unicyclic and simple; multiple cycles can create interacting Pfaffian constraints. The character statement uses odd characteristic. A general rooted amalgamation recurrence may implicitly yield the marginal rank polynomial; only the support-conditioned refinement is advanced as the novel assertion. Historical priority remains provisional and no external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
