# Independent Audit — 2026/09/14/017

Audit date: 2026-09-28 (UTC)
Audited tree: `ad8032a27a5d679dcd163dc57527e918cf35ebb2`

## Disposition

**FAILED** — Rejected for correctness: the package never derives the actual non-equivariant Skyrme Euler–Lagrange principal structure needed by the claimed global theorem, and its verifier checks generic/model null-form identities rather than the stated system.

## Correctness

**FAIL**. The record asserts a specific decomposition of the full 3+1 SU(2) Skyrme Euler–Lagrange system and then invokes quasilinear null theory, but neither RESULT.md nor the artifact derives that system or its top-order symmetric energy structure. The verifier tests standard Q0/Qmunu identities and a “model quasilinear term”; in particular its C4 contraction of an antisymmetric Q^{mu nu} with a symmetric Hessian is identically zero for every input, so it does not validate an actual Skyrme principal term. The remaining bootstrap is a schematic rate count. That is insufficient to certify a new non-equivariant global-existence theorem with the stated energy and sharp decay.

## Originality

**UNRESOLVED**. Lawful open-access searches found the established equivariant Skyrme small-data theorem of Geba–Nakanishi–Rajeev and related Faddeev/null-structure work, but no source inspected was shown to contain exactly the claimed non-equivariant small-ball theorem. Absence of a covering hit is not proof of novelty, so originality is left unresolved rather than inferred from search failure.

## Scientific value

**FAIL**. A full non-equivariant small-data Skyrme theorem would be scientifically valuable, but the submitted package does not establish it. Because the load-bearing PDE reduction and top-order estimates are only asserted schematically, the record cannot be validated as a research finding in its present form.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/1106.5750 — Geba–Nakanishi–Rajeev prove global existence/scattering for equivariant classical Skyrme and Adkins–Nappi wave maps.
- https://arxiv.org/abs/1203.2696 — Lei–Lin–Zhou treat an evolutionary Faddeev model with null structure, not the submitted full SU(2) theorem.
- https://arxiv.org/abs/2108.01163 — Alejo–Maulén study decay for global Skyrme wave-map solutions in a radial/equivariant setting.

Independent checks:
- Read the verifier source: its C4 “model quasilinear term” contracts an antisymmetric two-form with a symmetric Hessian and hence vanishes identically, so it cannot certify the actual principal nonlinearity.

No inaccessible material is represented as read. Literature absence was not treated as proof of novelty; where exact prior coverage remained uncertain, the originality axis is explicitly marked unresolved.
