# Independent Audit — 2026/09/11/047

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `c649683de91b8658d46bd0dae621b38585a9d4ad`  
**Disposition:** **FAILED**

## Correctness

The principal algebra checks independently. Multiplying the four π/2 sector propagators gives tr(M)-2 = (25/4)sin^4(w)-4sin^2(w)-(75/16)sin^2(2w), w=πλ/2, which reduces to s(100s-91)/4 with s=sin^2(w). Hence the smallest positive root is λ_1=(2/π)arcsin(sqrt(91)/10)=0.806026631958..., with the paired root 2-λ_1. The no-decay lemma on a 270-degree cone is also elementary and correct. The source appropriately labels the jump-formula obstruction conditional on the unknown singular coefficient.

## Originality

The leading-exponent calculation is a direct parameter specialization of the classical separation-of-variables/Mellin theory for elliptic transmission problems at interface corners. Once the 4:1, 90°/270° geometry is inserted, the 2x2 sector transfer matrices and determinant condition mechanically produce the displayed scalar polynomial. I found no prior source printing exactly sqrt(91)/10, but a previously unprinted evaluation of a standard characteristic equation at one contrast/angle does not by itself establish research-level originality.

## Scientific value

The exact exponent is a potentially useful benchmark for numerical corner solvers and for checking any proposed smooth-Taylor corner formula in this canonical L-shaped conductivity geometry. The value is narrow and the obstruction remains conditional, but the datum has concrete diagnostic utility even though it does not clear the originality bar as a standalone finding.

## Limitations

- No prior source printing the exact closed form was located; the originality failure is based on the claim being a mechanical specialization of established transmission-corner machinery, not on a duplicate exact table entry.
- The singular coefficient for the specific boundary datum is not certified nonzero, so the claimed obstruction to the jump formula remains conditional.
- The result is fixed to one angle and one contrast.

## Evidence

- [Mirschinka, The double layer potential method for a boundary transmission problem for the Laplace operator in an infinite wedge](https://doi.org/10.1002/mma.1670180703): Classical Laplace transmission analysis on an infinite wedge; establishes that wedge-interface transmission is a standard spectral/characteristic-equation problem.
- [Interface-corner singularity analysis (NASA technical report)](https://ntrs.nasa.gov/api/citations/19970006595/downloads/19970006595.pdf): Explicitly uses r^α angular expansions for scalar interface-corner problems, illustrating the established framework from which fixed-angle/material exponents are obtained.
- [Cakoni–Xiao, On corner scattering for operators of divergence form](https://arxiv.org/abs/1905.02558): Modern divergence-form corner literature relevant to the record’s inverse-problem motivation; it does not make the exact 4:1 reentrant evaluation itself a new general method.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `c649683de91b8658d46bd0dae621b38585a9d4ad`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
