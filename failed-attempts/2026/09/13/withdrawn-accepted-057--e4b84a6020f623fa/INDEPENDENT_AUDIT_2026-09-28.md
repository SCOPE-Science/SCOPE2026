# Independent Audit — 2026/09/13/057

Audit date: 2026-09-28 (UTC)
Audited tree: `cdfad3e267ec55b67680f389a6b233d82c49c568`

## Disposition

**FAILED** — Rejected: finite counts may be correct, but the package never identifies the relevant endomorphism ring or proves ascending edges, so the advertised volcano obstruction is not established; the order count itself is elementary.

## Correctness

**FAIL**. The finite algebra computations can be correct while the advertised volcano obstruction does not follow. The three partial-diagonal F4-subalgebras of F4³ are indeed the three minimal two-dimensional F4 over-algebras of the diagonal, and the supplied finite Ore computation may certify two rational l-neighbours of the displayed module. But RESULT.md explicitly admits that it does not compute End(phi), does not realize the local order O=A+lO_K as that endomorphism ring, and does not prove either neighbour is ascending. Consequently the sentence that 'a module with End=O would have three ascending directions' and the headline's graph-theoretic obstruction are conditional, not established for the exhibited vertex. At most the package shows that the quadratic-order chain proof mechanism cannot be transplanted naively to a split cubic local order.

## Originality

**FAIL**. The order-lattice part is elementary: F4-subalgebras of F4³ containing the diagonal correspond to set partitions of three coordinates, giving the three partial diagonals without exhaustive search. The small GF(4) neighbour census may be new data, but absent endomorphism-ring and ascent information it is not an original volcano theorem or counterexample.

## Scientific value

**FAIL**. A tiny neighbour census plus a standard split-algebra observation is insufficient as a standalone research result when the crucial realization and ascending-edge questions are left open. Those missing steps are precisely what would turn the computation into information about rank-3 volcano structure.

## Evidence and limitations

Repository files were read from the exact assigned/current tree and GitHub was used only as evidence. The following literature comparisons were inspected from lawful open-access sources:
- https://arxiv.org/abs/2511.21329 — Chen: generalized/CM Drinfeld volcano structure; highlights that ascent claims require endomorphism-level control.
- https://arxiv.org/abs/2009.11578 — Endomorphism orders of Drinfeld modules over finite fields; relevant to the missing realization step.
- https://arxiv.org/abs/2209.15033 — Karemaker–Katen–Papikian on isomorphism classes/endomorphism rings; contextual evidence that endomorphism-ring identification is substantive, not automatic from local subalgebra counts.

The audit does not infer ascendingness from an inaccessible or uncomputed endomorphism ring. The unresolved realization/ascent steps are treated as decisive gaps, exactly as the source record itself acknowledges.
