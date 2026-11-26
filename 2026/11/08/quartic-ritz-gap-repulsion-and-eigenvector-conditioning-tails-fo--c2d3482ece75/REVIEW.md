# Independent mathematical audit

## correctness

PASS

The rechecked result uses the cofactor identity to give z²+uz+conj(u) and D²=|u²−4conj(u)|. Since |u|≤1, the unique discriminant root is the weight barycenter. Modding out the normals by one global phase or sign gives respectively a two-torus or four planes at that point, and diagonal phases/signs commute with A. The Frobenius identity gives norm one at the barycenter, so this is a nonzero nilpotent, not a scalar. Schur triangle eigenvector overlap ν/√(ν²+D²) gives unit-column κ=(√(ν²+D²)+ν)/D, with ν²=1+(|u|²−D²)/2. Compactness excludes other tail contributions. Near zero, D∼2√|u| and κ∼|u|^(−1/2); the affine Jacobian 3√3/2 and Dirichlet weights give center densities 4/(3√3), 1/π. Disks of radii asymptotic to ε²/4 and R^(−2) give the four constants, and the positive R^(−4) tail via layer cake proves the p<4 cutoff including divergence at p=4. Independent script /workspace/branches/d316504f-57b8-4fb1-ad94-dd09de05eafe/independent_check.py and independent_check.txt there give 372 exact barycentric checks and 1,000 direct assertions across 200 planes, including center nilpotence and the conditioning formula. Limits are analytic, not fitted.

## originality

PASS

Best-of-knowledge pass for the exact complex/real gap and condition tails in the equilateral compression, not for the shadow densities, cofactor geometry, or the multiplicity correction as a standalone novelty claim.

## value

PASS

The smallest nontrivial orthogonal compression of a symmetric three-level unitary spectrum is a concrete benchmark for nonnormal behavior from a fixed normal input. Almost-sure simplicity conceals a precise fourth-moment obstruction; comparing real and complex trial planes at the same input isolates distinct quantitative constants. The simultaneous gap and unit-vector conditioning laws give more information than the feasible Ritz region or generic warning about near-defectiveness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
