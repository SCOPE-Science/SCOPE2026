# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-017  
**Original source path:** `2026/09/07/017`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `bf5c1b14eb21ac0b1208b8e390c7651ded2c397c`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

The record states that the general-position rectilinear crossing number of `K(5,7)` is 36, using Kleitman's topological lower bound together with a straight-line integer-coordinate drawing having exactly 36 crossings.

## Correctness — PASS

The theorem is correct. The published coordinate witness was independently recounted during this campaign using exact orientation predicates and gives 36 proper crossings with no three vertices collinear. Kleitman's theorem `cr(K(5,n))=Z(5,n)` gives the lower bound 36 for `n=7`, while any straight-line drawing is also a topological drawing. Thus the displayed witness establishes equality.

## Originality — FAIL

The theorem is not new. Kleitman's result gives `cr(K(5,n))=Z(5,n)` for all `n`. Independently, the classical Zarankiewicz construction is a straight-line drawing of `K(m,n)` with exactly
`floor(m/2) floor((m-1)/2) floor(n/2) floor((n-1)/2)` crossings. Combining these two known facts immediately yields the rectilinear equality `bar-cr(K(5,n))=Z(5,n)` for every `n`, including `n=7`. Therefore the record's theorem is a direct specialization of pre-existing results, not a new finite case that required search for existence.

Searches included `rectilinear crossing number K(5,n) Zarankiewicz`, `Kleitman K5n crossing number straight line`, and the classical Zarankiewicz drawing literature. The coordinate set is a different witness, but a new drawing of a theorem already implied for all `n` is not a new mathematical result.

## Scientific value — FAIL

The integer coordinates and dual crossing counters are useful as a regression example, but they do not improve the known bound, classify optimal drawings, lower coordinate size, or resolve an open rectilinear case. Once the general classical implication is recognized, the residual is only one small explicit witness and is not scientifically substantial enough for the validated-finding collection.

## Repair assessment

No bounded wording repair rescues novelty without replacing the central theorem. A meaningful retry would require a genuinely unresolved rectilinear family, optimal-coordinate theorem, classification, or another new structural statement.

## Final disposition

**FAILED.** Correct, but the theorem is an immediate known corollary and the residual witness lacks sufficient novelty/value.