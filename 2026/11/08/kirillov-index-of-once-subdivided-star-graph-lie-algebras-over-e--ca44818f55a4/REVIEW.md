# Scientific review: Kirillov index of subdivided-star graph Lie algebras

## Correctness — PASS

The construction of Gallo--Videla [GV, Sections 2--4] yields a \(V\oplus A\oplus W\) basis with \(\dim V=2m+1\), \(\dim A=2m\), \(\dim W=m(m+1)/2\), and \(W=Z(\mathfrak n_{T_m})\). The displayed brackets follow by applying the source's length-two-path rules to the tree \(c-u_i-v_i\). The Kirillov matrix has an \(A\times A\) zero block. The \(m\) columns indexed by the outer edges share only the hub row; hence the mixed block has rank at most \(m+1\). Together with parity of alternating ranks this proves the upper bound. The explicitly given functional makes the mixed block rank exactly \(m+1\), while its residual alternating form has \(\lfloor m/2\rfloor\) independent hyperbolic planes. This proves the rank and index formulas over arbitrary fields, including characteristic two. Exact finite-field replay and exhaustive functional checks at small sizes independently corroborate the calculation; they are not substituted for the general proof.

## Originality — PASS (same-model, qualified)

The closest primary paper is [GV], publicly submitted 2026-10-25. Its complete relevant text was inspected, not merely its abstract: the graph bracket rules, tree center and dimensions, explicit path/star examples, classification section, tensor construction and blow-up section. It supplies the ingredients but does not calculate the Kirillov index or coadjoint-form rank for once-subdivided stars. Searches for the exact result and equivalent descriptions (subdivided claw/spider, rank of Kirillov form, coadjoint stabilizer, generic alternating-block rank) did not locate stronger coverage. A relevant published published-finding corpus entry on tree graphical groups treats a different *two-step* graph Lie algebra, not the three-step algebra of [GV]. The accessible owned ledger records graph-Lie-algebra adjoint/Kirillov results for stars and Heisenberg structures, but no stated index formula for once-subdivided stars. This is a comparison by implications, not an inference of uniqueness from a failed search. Priority risk: an unindexed special-family calculation could still exist.

## Mathematical value — PASS

Index is a standard coadjoint invariant whose evaluation is not determined by the published center and lower-central dimensions. The result supplies an exact unbounded-family classification over every field and finds a linear, parity-sensitive excess above the center dimension. The gap is minimal for the two path-like boundaries \(m=1,2\), but grows on genuinely branching once-subdivided stars \(m\ge3\), exposing a structural obstruction to maximal Kirillov rank modulo center. Once-subdivided stars are the canonical first spider family beyond paths and stars; the invariant is independently motivated by representation theory and the geometry of alternating forms. No claim of a general arbitrary-tree classification or a complete functional rank distribution is made.

## Limits and literature

Only the designated family and its maximum Kirillov rank are proved, not distributions of lower ranks. External publication priority is not independently established. [GV] Gallo--Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1 (2026-10-25). The earlier Dani--Mainkar graph construction and character-degree results for two-step graphical groups do not logically imply this three-step index formula. The exact checker is included as `check_index.py`.

Self-review: passed. Independent audit: not yet performed.
