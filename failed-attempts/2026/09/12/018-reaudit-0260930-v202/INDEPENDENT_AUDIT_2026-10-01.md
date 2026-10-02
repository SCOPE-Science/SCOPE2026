# Mathematical audit — 2026-10-01

## Final claim

Primitive corank-one E6-to-E7 lattice embedding with complement norm 6 and index-3 discriminant gluing

## Correctness — PASS

PASS. With the explicit Cartan-form definitions in the package, fresh exact arithmetic gives det(E6)=3 and det(E7)=2; the coordinate inclusion is an isometry; the orthogonal vector w=(2,4,6,5,4,3,3) has norm 6; the determinant of the seven-column matrix formed by the inclusion and w has absolute value 3; and the stated order-three gluing relation holds. The supplied upper-triangular Seifert forms also satisfy the claimed pullback identity. These facts establish the lattice calculation actually encoded by the record.

## Originality — FAIL

FAIL. The substance is the standard E6 root lattice sitting inside E7 together with the elementary discriminant/complement arithmetic of that classical inclusion. P8 and X9 are the simple elliptic types corresponding to affine E6 and affine E7, and standard root-lattice/discriminant theory already determines the determinant ratio and gluing. The audited construction is therefore a coordinate realization of classical lattice data, not a new implication.

## Scientific value — FAIL

FAIL. Beyond verifying a particular coordinate convention, the final claim is a routine exceptional-root-lattice inclusion and discriminant calculation. The package does not establish a new singularity-theoretic map, obstruction, boundary, or classification theorem that would make this relabeling of classical E6-to-E7 arithmetic a worthwhile new mathematical finding.

## Sources inspected

- I. A. B. Strachan, Simple Elliptic Singularities: a note on their G-function — https://arxiv.org/abs/1004.2140: IDENTIFICATION_BACKGROUND. Primary abstract/full-text identification of P8, X9, J10 with the simple elliptic affine E6, E7, E8 types.
- W. Ebeling, A. Takahashi, Strange duality of weighted homogeneous polynomials — https://arxiv.org/abs/1003.1590: SINGULARITY_DUALITY_BACKGROUND. Primary abstract on Dolgachev/Gabrielov number duality extending Arnold's strange duality.
- Standard E6/E7 root-lattice discriminant theory — https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/index.html: CLASSICAL_LATTICE_COVERAGE. Reference tables/catalogue context for E6 and E7 lattices and their standard invariants.

## Residual risks

- The record's singularity-theoretic naming is stronger than the coordinate lattice calculation itself; no new canonical P8-to-X9 geometric morphism is established by the package.
- Scientific rejection is for prior coverage and lack of additional value, not a failure of the displayed integer arithmetic.

## Disposition

**failed**
