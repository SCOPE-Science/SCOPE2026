# Scientific review: size-resolved \(P_3\)-convex subsets of open ladders

## Correctness — PASS

The exact claim is the displayed rational generating function in `RESULT.md`, including its equivalent polynomial recurrence for all ladder lengths. The local rule for an outside vertex is exactly the three-column predicate. Its open end conditions use virtual zero columns, so the one-rung case and the end rungs are included without assuming a periodic boundary. Row exchange provides a genuine ten-orbit quotient of the sixteen-state automaton. The exact determinant of the quotient is certified by 231 integer interpolation evaluations with proved degree bounds, and ten exact initial polynomial identities fix the entire numerator by the adjugate degree bound. Direct exhaustive vertex-subset checks on ladders of lengths one through eight are corroboration, not the unrestricted proof. All matrix operations and coefficient checks are reproduced by `artifacts/verify.py`, without external dependencies.

## Originality — PASS, subject to historical-priority risk

The March 5, 2026 preprint of Dourado–Grippo–Lin–Protti studies \(P_3\)-convex counting, general hardness, tree and threshold-graph algorithms and exact exponential methods; its accessible complete text does not supply a ladder cardinality enumerator. The **unweighted** two-row ladder counts, their order-five scalar recurrence, and a scalar generating function are already public in OEIS A231376 (Hardin, 2013; Barker, 2018). Those results and the corresponding OEIS A231382 table are specifically acknowledged and are not re-claimed. The present theorem determines every coefficient of the two-variable size enumerator, an invariant not fixed by the known evaluation at \(z=1\). Relevant searches for weighted strict-majority arrays and bootstrap-percolation closed configurations did not reveal that refined identity, although unindexed equivalents remain possible. Earlier mathematical records on \(P_3\)-convex cycle powers and on a different kind of restricted domination in open ladders do not imply this new graph-property count.

## Mathematical value — PASS

The complete cardinality distribution is the natural refinement of the number of closed infection configurations in the two-neighbor model. It allows exact questions conditioned on the size of the initial infected set, which are invisible in the already-known scalar count; the ten-state symmetry reduction and short order-five polynomial recurrence make these quantities computable for arbitrarily long strips in linear polynomial-arithmetic work. This is an infinite-family size-refined enumeration, not a marginal scalar increment, recasting the algorithmic counting problem in a canonical fixed-width grid. The value does not rely on claiming that the pre-existing scalar recurrence is new.

## Scope and priority limits

Only open ladders of width two are covered. Published scalar enumeration constitutes a strong prior result; another exact weighted enumeration might already exist under strict-majority binary-array or bootstrap terminology. Relevant source comparisons and limits are documented in `AUDIT.json`. No independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
