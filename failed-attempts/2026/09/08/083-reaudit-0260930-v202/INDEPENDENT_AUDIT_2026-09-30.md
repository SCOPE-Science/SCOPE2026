# Independent mathematical audit — 2026-09-30

## Record

Exact graded Betti tables, regularity, and projective dimension for seven committed edge ideals on 8-10 vertices

## Disposition

failed

## Correctness: PASS

A fresh exact-rational Hochster-formula computation over every vertex subset reproduced every listed graded Betti number for all seven explicit graphs. Independent brute-force induced-matching enumeration reproduced the stated induced-matching numbers 1,1,2,2,1,2,3, and the regularity/projective-dimension values follow from the independently reproduced Betti support.

## Originality: PASS

Targeted Resultary and literature comparison did not surface these exact seven graph tables. Jacques supplies the general Hochster-based machinery and explicit families such as cycles/forests, but the inspected source does not tabulate these committed graphs. The disjoint-edge H to H+e regularity jump is not novel as a mechanism and is explicitly treated as Künneth/tensor-product additivity rather than a new theorem; originality is therefore limited to the exact finite tables.

## Scientific value: FAIL

The final bundle does not identify a mathematically motivated unresolved invariant or boundary that makes these seven small tables worth publishing as a finding. Several objects are explicitly researcher-fixed intermediaries, and the emphasized H/H+e regularity jump is exactly the routine disjoint-component tensor-product phenomenon already acknowledged in the record. Correct computation and reproducibility alone do not overcome the arbitrariness of the slice.

## Limitations and residual risks

- All seven QQ Betti tables and induced-matching values were independently reproduced.
- The scientific rejection is for value, not correctness.
- The H/H+e jump is a routine disjoint-component consequence, and several listed graphs are ad hoc intermediaries rather than a natural classification boundary.

## Sources inspected

- S. Jacques, `Betti Numbers of Graph Ideals`, arXiv:math/0410107.
- The assigned package's RESULT.md, tables.json, and verify_method.py.

This file records a mathematical audit of the scientific claim. It is not an expert attestation or a statement about any separate verification channel.
