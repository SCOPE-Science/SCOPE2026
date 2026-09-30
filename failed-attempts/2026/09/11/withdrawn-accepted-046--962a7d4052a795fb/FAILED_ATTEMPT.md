# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/11/046`  
Independent audit date: 2026-09-28 (UTC)  
Task: `9a4a1ee6d59331d187826b573a7b6f7b`

This package is not accepted as a validated research finding under the three-axis audit. It is retained intact for provenance and should be relocated to the assignment-designated failed path.

## Correctness

The core impossibility argument is correct under the stated interior-support setup. Harmonic interior regularity makes the localized background-gradient map compact; the conductivity perturbation is supported strictly inside the disk, so the relative NtD term factors through interior fields and is compact as well. Thus the restricted linearized operator is compact on an infinite-dimensional Hilbert trace space, and after a Riesz identification 0 belongs to its spectrum. A uniform strictly positive spectral floor such as +0.05 is therefore impossible. The numerical section is appropriately labeled corroborative rather than essential.

## Originality

The headline is a direct consequence of standard facts already built into the inverse-problem setting: relative boundary maps for conductivities that agree near the boundary are smoothing/compact, localized Fréchet derivative forms factor through compact interior restriction, and every compact operator on an infinite-dimensional space has 0 in its spectrum. The half-boundary restriction and the particular squares do not create a new mechanism; they only instantiate this general compactness obstruction.

## Scientific value

As a consistency check on a badly posed target, the argument is useful, but it does not establish a new inverse-problem theorem, quantitative regime, or computational phenomenon. The +0.05 floor is ruled out before the geometry, Carleman weight, or detailed PDE numerics matter. That makes the package suitable as target triage or exposition, not as a standalone validated research finding.

## Consequence

The computational and documentary materials may remain useful as examples or diagnostics, but the package's research headline must not be represented as independently validated without resolving the issues above.

## Evidence

- [Hyvönen–Piiroinen–Seiskari, Point measurements for a Neumann-to-Dirichlet map and the Calderón problem in the plane](https://arxiv.org/abs/1204.0346): For conductivities equal to one near the boundary, the relative NtD data have strong analytic regularity; this is representative of the standard smoothing structure behind the compactness used in the record.
- [Kenig–Sjöstrand–Uhlmann, The Calderón problem with partial data](https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n2-p05.pdf): Foundational partial-data Calderón framework; the record’s impossibility does not require a new partial-data uniqueness mechanism beyond standard boundary/operator facts.
