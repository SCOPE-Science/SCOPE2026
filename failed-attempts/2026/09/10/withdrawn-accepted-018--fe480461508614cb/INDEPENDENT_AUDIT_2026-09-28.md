# Independent Audit — 2026/09/10/018

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `799da66c0dea98937f7b6ba510d57f5386384c24`  
**Disposition:** **FAILED**

## Correctness

The lower-bound computation is correct. Recentring gives u^3-v^2 up to affine terms; on the cap |u|<=R^(-1/3), |v|<=R^(-1/2), the coherence box has volume 0.008 R^(11/6), the L^2 norm is 2 R^(-5/12), and the resulting L^(7/2)/L^2 ratio grows like an explicit constant times R^(3/28). The same scaling yields the necessary exponent q>=22/5. The finite-R constants and ball containment are consistent.

## Originality

The headline obstruction is not original as a research result. Ikromov–Müller prove the sharp necessary restriction condition p' >= 2 h^r(phi)+2 (and, in adapted coordinates, p'_c=2h(phi)+2) by a Knapp argument for finite-type hypersurfaces. For the recentered phase u^3-v^2, the Newton height is h=6/5, giving exactly p'>=22/5. Thus the record's principal threshold and anisotropic cap are a direct specialization of an existing general theorem, not a new transfer obstruction.

## Scientific value

The explicit finite-R constants are a useful pedagogical/reproducibility exercise, but once the general sharp theorem is applied they do not establish a new theorem, new range, or new phenomenon. As packaged as a research finding, scientific value is insufficient.

## Limitations

- The calculation remains valid as an example of the known Knapp/Newton-height necessary condition.
- The record should not describe the 22/5 obstruction or failure of the nondegenerate range as a newly discovered research boundary.

## Evidence

- [Ikromov–Müller, Fourier restriction for hypersurfaces in three dimensions and Newton polyhedra, Part I](https://arxiv.org/abs/1208.6090): Theorem 1.7/Proposition 1.9 identify the sharp critical restriction exponent from restriction height; Proposition 13.1 proves the Knapp necessary condition p' >= 2 h^f(phi)+2. For u^3-v^2, h=6/5, hence 22/5.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `799da66c0dea98937f7b6ba510d57f5386384c24`; no repository writes were made by this audit.
