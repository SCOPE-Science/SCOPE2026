# Independent mathematical audit

## correctness

PASS

The fourth-moment normalization and Laplace eigenvalue 2d give Dirichlet norm squared 4||A||_F^2/(d+2), while each intrinsic gradient is 2(I-uu^T)Au. A vanishing sampled gradient forces u to be an eigenvector of the complex symmetric A; nonzero pairwise bilinear products force a common eigenvalue. The real simplex span through k<=d vertices has positive definite Gram matrix, so its complexification splits orthogonally from the complementary symmetric block. The trace condition determines the common eigenvalue, giving exactly (d-k)(d-k+1)/2 free parameters, and the full simplex is injective by restriction. For one deletion, the full-frame rescaling and rank-(d-1) downdate have coefficient (d+2)/(2d). For the normalized symmetrized tensor at the deleted vertex, the squared norm of its full evaluation vector is 2(d+1)/d^3 by simplex isotropy; dividing by the low-sector evaluation Gram level (d^2-1)/d^2 gives overlap 2/[d(d-1)]. Polarizing yields orthogonal paired planes. The trace and determinant in the resulting two-by-two block produce both radical branches; the secular polynomial is negative at L_d, the upper root is strictly below H_d, and positivity follows from the kernel calculation. Unpaired dimensions are 1 and d(d-3)/2, so the d=3 condition number uses the upper paired root rather than H_d. The determinant divided by the upper root gives lower-root asymptotic 1/d. An independent rational ambient-hyperplane matrix construction confirmed every retained-cardinality rank and the full and erased characteristic polynomials for d=3,4,5,6; this is corroboration, not the all-dimensional proof.

## originality

PASS

The intact two-level spectrum is already implied by the cited full-configuration Hessian proof and receives no novelty credit. The additional projected overlap with the deleted tangent subspace, the complete downdated spectrum and the exact subset-nullity law were not supplied by the strongest inspected matches. The verdict concerns these erasure results only and is best-of-knowledge, not a priority certificate.

## value

PASS

Node loss is a natural stability question for a minimal spherical-design configuration. The exact nullity law separates injectivity after one loss from unavoidable information loss after two, and the sharp surviving constants distinguish injectivity from an inverse whose squared condition number grows like d. This is substantive additional information beyond the intact two-level spectrum, even without optimizing reweighting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
