# Independent Audit — 2026/09/12/077

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `9231a406cd293f6b71f1094f61abc8faf3e1a38c`
- Disposition: **FAILED**

## Correctness

**PASS** — The fiber-symmetry obstruction is valid: for the 2-2 extension requirement, every candidate vertex is fixed by a fiber transposition that exchanges one required neighbor with one required non-neighbor, so full fiber-permutation invariance contradicts the Rado extension property. The shift-invariant existence construction is also sound: at each finite requirement one may choose a fresh fiber and fresh translation differences, assign the required pair-pattern values together with their symmetric counterparts, and avoid all earlier constraints. Enumerating the requirements yields a shift-invariant graph with the extension property.

## Originality

**FAIL** — The shift-invariant half is a standard Fraisse/Cayley-style construction already part of the classical random-graph toolkit. The obstruction half is an immediate orbit-stabilizer consequence of imposing the full symmetric group on four fiber indices: the stabilizer of a candidate identifies a demanded neighbor and non-neighbor. It is a useful diagnostic for one attempted coding architecture, but it does not introduce a new random-graph construction or descriptive-set-theoretic invariant.

## Scientific value

**FAIL** — The theorem blocks only one very rigid product presentation and explicitly leaves the motivating simultaneous-conjugacy smoothness problem untouched. Because alternative non-uniform codings and turbulence/hardness routes remain completely open, this elementary obstruction plus a textbook contrast is too narrow to support the record as an independent research finding.

## Sources

- The random graph (Peter J. Cameron): https://arxiv.org/abs/1301.7544 — Survey background for the Rado extension property, highly symmetric presentations, and standard random-graph constructions.
- Wreath product in automorphism groups of graphs (M. Grech; A. Kisielewicz): https://arxiv.org/abs/1910.11811 — Background on product/fiber symmetry in graph automorphism groups.

## Limitations

- The correctness conclusion is for the two stated elementary theorems, not for the motivating smoothness dichotomy, which the record itself does not resolve.
- No claim is made that the exact four-fiber obstruction sentence has previously appeared verbatim in the literature.

GitHub was read only as evidence. No GitHub mutation, dispatcher completion call, or separate publication/report action was performed by this audit chat.
