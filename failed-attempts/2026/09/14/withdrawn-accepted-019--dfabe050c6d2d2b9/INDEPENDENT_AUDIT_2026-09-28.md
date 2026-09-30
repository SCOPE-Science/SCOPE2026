# Independent Audit — 2026/09/14/019

Audit date: 2026-09-28 (UTC)
Audited tree: `f22d5be1016b1c71051a5cfad33f68e4c107cc0c`

## Disposition

**FAILED** — Rejected on originality and value: the coordinate identities and 7-dimensional incidence calculation are correct, but the subgroup/Goh mechanism and the decisive free-step-3 codimension count are already present in the Sard literature; the new coordinate equations are incremental.

## Correctness

**PASS**. The central algebraic calculations independently check. On the stated chart K(s,t), substituting x=(a1,a2,sa1+ta2), y=beta(1,t,-s), and z=g1 Z1+g2 Z2 gives both Q=x1 c-x2 b+x3 a=0 and the displayed E1=-a z2+b z1=0 identically; the seven-parameter incidence map has Jacobian rank 7 at the stated test point. This supports a 7-dimensional closure for the union of the 5-dimensional rank-2 step-3 subgroups over Gr(2,3). The supplied verifier does check rank 7, although its named E polynomial is a different higher-degree vanishing relation; that mismatch does not invalidate E1 because E1 was independently checked.

## Originality

**FAIL**. The structural core is already in the published Sard literature. Le Donne–Montgomery–Ottazzi–Pansu–Vittone show the free rank-3 step-3 group has Algebraic Sard and, for step-3 Goh/strictly abnormal minimizers, place curves in proper Carnot subgroups; their Remark 6.1 gives the Grassmannian rank-(r-1) subgroup codimension count r^2-r+1. Boarotto–Vittone’s later dynamical treatment explicitly recovers Goh singular curves in the free rank-3 step-3 group as arbitrary curves in a 2-generator subgroup. The submitted exact Q,E1 equations and a rank-7 chart are an incremental coordinate sharpening of that established mechanism rather than a distinct new theorem.

## Scientific value

**FAIL**. Explicit defining equations can be useful, but the package’s main advertised “exact codimension 7” follows from the already-known rank-2 subgroup family plus a routine rank computation. Without a broader classification, new geometric invariant, or consequence beyond the existing Goh/Sard framework, the coordinate refinement is too incremental for a standalone validated finding.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/1503.03610 — Le Donne et al., Sard Property for the endpoint map on some Carnot groups; includes F_{3,3}, the Goh-to-subgroup mechanism for step 3, and Remark 6.1’s Grassmannian codimension count.
- https://arxiv.org/abs/1908.11120 — Boarotto–Vittone, A dynamical approach to the Sard problem in Carnot groups; treats rank-3 step-3 Goh singular curves and their two-generator subgroup realization.

Independent checks:
- SymPy substitution independently gave Q=0 and E1=0 on the submitted chart and Jacobian rank 7. Open-access PDF pages for the 2016 Sard paper were also visually inspected, including Theorem 1.2 and Remark 6.1.

No inaccessible material is represented as read. Literature absence was not treated as proof of novelty; where exact prior coverage remained uncertain, the originality axis is explicitly marked unresolved.
