# Independent Audit — 2026/09/13/053

Audit date: 2026-09-28 (UTC)
Audited tree: `fbdd80ccc2cc6bedac2cdb0ec1141d6f93baa0ea`

## Disposition

**FAILED** — Rejected: exact invariant gap and symmetry calculation survive, but advertised explicit local constants are unsupported and the corrected qualitative theorem is routine/insufficiently novel.

## Correctness

**FAIL**. The exact t=0 invariant spectral statement is sound: the standard CR-sphere eigenvalue formula gives kernel H_(1,0)⊕H_(0,1), anti-diagonal weights exclude that kernel, and the first invariant mean-zero sectors have sub-Laplacian eigenvalue 4, hence L0=4λ-8 has exact gap 8. The symmetry and contact-Hamiltonian calculation is also consistent. However the published theorem and slogan assert explicit persistence/tubular constants (for example δ0=1/10, r0=0.05 and positivity to |t|<1/2) while RESULT.md itself concedes these numbers rest on an uncited crude operator bound and an unspecified Sobolev constant and are merely illustrative. Those quantitative assertions are therefore not proved. A qualitative local implicit-function theorem follows from invertibility and smooth dependence, but that narrower theorem is not what the headline states.

## Originality

**FAIL**. After removing the unsupported constants, the surviving content is a direct symmetry restriction of the classical CR-sphere spectrum plus a routine implicit-function-theorem consequence. The anti-diagonal-versus-Hopf calculation and the vanishing contact Hamiltonian on the Clifford torus are useful observations, but no covering literature check identified a substantial new theorem beyond standard homogeneous Rossi-sphere and CR-Yamabe structure. The package does not establish a new global bifurcation result, weighted Grushin theorem, or classification.

## Scientific value

**FAIL**. The corrected qualitative statement is too close to standard spectral decomposition and local IFT machinery to justify this standalone research record. Its potentially higher-value global dichotomy and weighted quotient analysis remain open, and the only advertised quantitative neighborhood is uncertified.

## Evidence and limitations

Repository files were read from the exact assigned/current tree and GitHub was used only as evidence. The following literature comparisons were inspected from lawful open-access sources:
- https://ems.press/journals/rmi/articles/14297808 — Cheng–Malchiodi–Yang: homogeneous 3D CR structures/Rossi spheres; supports homogeneous curvature background, not the claimed quantitative tubular constants.
- https://arxiv.org/abs/2606.27164 — Afeltra–Ho–Pinamonti: CR Yamabe flow on Rossi spheres; different bubble/dynamical regime.

The qualitative IFT consequence is not rejected merely because the explicit constants fail; the failure disposition reflects the published quantitative headline plus the weak originality/value of the narrowed statement.
