# Independent Audit — 2026/09/14/037

Audit date: 2026-09-29 (UTC)
Audited tree: `2ce2454f1930da85619909c35152b8bc6b23c011`

## Disposition

**FAILED** — Rejected on originality and value: the fixed rigid K4 conclusion follows directly from standard split-reduction, M0,3 rigidity, and the local smoothing-coordinate rescaling.

## Correctness

**PASS**. The rigid-graph and special-fiber part is sound. Distinct edge lengths 1,...,6 force every metric automorphism of K4 to preserve each edge; the four incident-length signatures are distinct. For a Mumford curve the stable reduction is split totally degenerate, and with the graph fixed each component is a genus-zero component with three individually fixed rational nodes, hence is P1 with a rigid ordered triple (M0,3 is a point). Locally a smoothing xy=5^L u with u in Z5^× is Q5-isomorphic to xy=5^L by rescaling one coordinate, so local annulus/inertia data cannot depend on the unit. These facts support constancy of the stated verticial-plus-local-break package. The deformation-theoretic sharpness claim is also consistent with a six-dimensional smoothing space and trivial labelled automorphism group.

## Originality

**FAIL**. The result is assembled almost mechanically from standard ingredients: triviality of the metric automorphism group for the arbitrarily distinct labels 1,...,6; rigidity of three-pointed P1; uniqueness of stable reduction; and the coordinate rescaling xy=5^L u ~= xy=5^L. Lepage/Mochizuki reconstruction provides the standard vertex/edge interpretation. Once these ingredients are instantiated, the claimed constancy is immediate; no new anabelian reconstruction theorem, ramification theorem, or moduli classification is proved.

## Scientific value

**FAIL**. The example can be pedagogically useful as a sanity check, but the choice of a K4 with six pairwise distinct lengths deliberately kills all graph symmetry and every component has no moduli. The negative conclusion therefore follows from a rigid test configuration rather than exposing a new phenomenon or reusable invariant. The unit-parameter sharpness is standard deformation theory. This does not clear the threshold for a standalone research finding.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/0811.3169 — Lepage, Tempered fundamental group and metric graph of a Mumford curve: geometric tempered reconstruction of graph/metric background.
- https://arxiv.org/abs/2107.07884 — Schottky spaces and universal Mumford curves over Z: general deformation/moduli background, not a source of the exact fixed-K4 claim.

Independent checks:
- Independently enumerated the K4 incident signatures {1,2,3}, {1,4,5}, {2,4,6}, {3,5,6}; they are pairwise distinct and force the metric automorphism group to be trivial.
- Checked the local node model directly: xy=5^L u is carried to x'y=5^L by x'=u^{-1}x, so the unit is not local annulus data.
- Used only standard stable-curve facts for the special-fiber uniqueness step; no computational output was needed for that deduction.

Limitations:
- The precise global terminology “upper-numbering break invariant along an incident annulus” is not standardized uniformly across the literature; the correctness judgment covers the intrinsic local inertia filtration meant by the record.
- No inaccessible source is represented as read.

