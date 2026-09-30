# Independent audit — Exact transverse stability equation for antiphase growth in a branched double pendulum

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/transverse-antiphase-stability-branched-double-pendulum--4a64ba4e55cb`  
**Audited tree:** `caa03106b637ec52ae9ecac386cf20eb5da4be88`

## Disposition

**FAILED — NOT A VALIDATED FINDING.**

## Correctness

**PASS.** The mathematics is correct. Direct Euler–Lagrange linearization of the displayed transformed mass matrix and potential gives M2 d¨+[G2 cos y+μ cos(y−x) x˙²−μ sin(y−x) x¨]d=0. Eliminating x¨ with the symmetric-sector equations reproduces the stated acceleration-free Q exactly. A separate quadratic small-amplitude expansion reproduces qΣ and q0, and the repository artifact reports zero symbolic residuals and the same numerical frequencies and coefficients.

## Originality

**FAIL.** FAIL because the core theorem was already published in SCOPE before this record. `2026/09/19/antiphase-normal-equation-branched-double-pendulum--bfc3fd510d22` was created at 2026-09-19T11:52:28Z, whereas the assigned record's result was first committed at 2026-09-19T22:54:34Z. The earlier record states the identical exact scalar normal variational equation, an equivalent state-only acceleration elimination, the conserved-Wronskian/Hill interpretation, and the complete quadratic combination spectrum with the same sum-frequency channel. Its verification output already contains Kmean=-0.0335490281885 and Ksum=0.00589770175709; division by M2=0.00071071819 gives q0=-47.20440346194 and qΣ=8.29822824303, numerically identical to the assigned record. The assigned acceleration-free normalization and coefficient notation are therefore repackaging of an earlier SCOPE result, not an original theorem.

## Scientific value

**FAIL.** FAIL as a standalone validated finding. The source-specific transverse stability interpretation is scientifically useful, but the repository already contains a stronger earlier package that includes the exact normal equation, state-only evaluation, release-stiffness analysis, and full quadratic forcing spectrum. The later record adds no sufficiently distinct scientific contribution to justify a second validated finding.

## Independent checks

- Re-derived the transverse Euler–Lagrange equation symbolically from the record's mass matrix and potential.
- Solved the symmetric-sector equations for x¨ and algebraically matched every term of the acceleration-free stiffness Q.
- Expanded the stiffness to O(A²) and recovered the stated sum-frequency coefficient.
- Compared against the earlier SCOPE artifact: Kmean/M2 and Ksum/M2 exactly reproduce this record's q0 and qΣ.
- Checked GitHub commit history: the earlier normal-equation record predates the assigned record by about eleven hours.

## Evidence and literature

- https://arxiv.org/abs/2609.20688 — Toda–Ooshida source preprint; establishes the branched-pendulum model and observed antiphase energy transfer.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/antiphase-normal-equation-branched-double-pendulum--bfc3fd510d22 — Earlier SCOPE record containing the same exact normal equation and quadratic forcing structure.
- https://doi.org/10.11316/jpsgaiyo.79.2.0_3613 — Accessible 2024 meeting abstract on experimentally generated antiphase oscillations; background only.

## Limitations

- The rejection is for originality and standalone value, not mathematical correctness.
- The exact equation concerns infinitesimal transverse perturbations of the ideal conservative symmetric model; damping, asymmetry, and finite-amplitude saturation remain outside scope.

## Repository identity

The assigned source-tree SHA `caa03106b637ec52ae9ecac386cf20eb5da4be88` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
