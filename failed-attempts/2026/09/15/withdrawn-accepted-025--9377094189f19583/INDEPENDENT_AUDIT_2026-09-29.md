# Independent Audit — 2026/09/15/025

Audit date: 2026-09-29 (UTC)
Audited tree: `a32d6df4467953aae493bf77f94456171df70abb`

## Disposition

**FAILED** — The mathematics of the tilting label is correct, but the central result is a mechanical consequence of the cited MSS framework and does not clear originality or standalone scientific value.

## Correctness

**PASS**. The structural label U≅T(2^3,1^4) is correct. MSS’s Morita reduction sends the problem to Delta(1^7)⊗Delta(1^3); exterior-power Weyl modules are tilting, their tensor product is tilting, and its indecomposable direct summands are tilting. In the p=3,k=7,j=3 case, Henke’s criterion gives exactly two summands; the simple L(2,1^8) lies in the separate block, so the remaining five-factor block summand U is indecomposable and tilting. Its highest Weyl factor is Delta(2^3,1^4), forcing U to be the unique indecomposable tilting T(2^3,1^4). The record properly does not claim to have determined the unresolved Loewy layers. The Rule-15 computations are consistent with the supplied scripts and do exhibit Weyl modules with more than two factors.

## Originality

**FAIL**. The main identification is a short formal consequence of information already assembled in Muth–Speyer–Sutton. Their paper explicitly singles out Example 5.21 as the p=3,k=7,j=3 difficult case, works through the same Schur-algebra tensor product, and supplies the Morita equivalence, tilting closure, summand count/block information, and the three Weyl factors. Once these published ingredients are put together, naming the remaining indecomposable summand T(2^3,1^4) follows immediately from standard highest-weight uniqueness; it does not require a new theorem or computation. The Rule-15 witness scan is likewise a direct evaluation of the paper’s decomposition criterion.

## Scientific value

**FAIL**. The observation that the unresolved summand carries the tilting-module label is a useful clarification, but it does not resolve the hard part highlighted by MSS—the Loewy/Alperin structure—or determine the missing graded internal structure. The finite Rule-15 scan only demonstrates why one existing stacking proof cannot be copied verbatim. As packaged, these are helpful deductions about an open example rather than a standalone advance of sufficient research value.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/2101.11175 — Muth–Speyer–Sutton, Decomposable Specht modules indexed by bihooks II: provides the Morita equivalence, tilting framework, almost-semisimple theorem, and Example 5.21 motivating exactly p=3,k=7,j=3.
- https://doi.org/10.1007/s10468-021-10093-3 — Published version of the same MSS paper in Algebras and Representation Theory.

Independent checks:
- Recomputed the Rule-15 decomposition rows reported in verify_target.py for n=10,p=3 and the two-summand Henke count.
- Checked the block separation of L(2,1^8) from the three simples occurring in the five-factor summand using the submitted 3-core calculation.
- Used closure of tilting modules under tensor products/direct summands plus highest-weight uniqueness to confirm U≅T(2^3,1^4).
- Inspected verify2.py and confirmed that the record itself correctly warns that the two displayed Alperin diagrams are not proved exhaustive without Ext^1 data.

Limitations:
- Donkin’s 1998 source was not independently represented as read; the central tilting-label conclusion and the originality/value disposition do not depend on independently re-reading that inaccessible source.
- The rejection is not for mathematical falsity: the tilting identification is correct, but mechanically follows from established ingredients and does not settle the Loewy problem.
