# Independent mathematical audit

## correctness

PASS

The unsigned K₅ incidence matrix has BBᵀ=3I+J, rank 5 and determinant 648. Since 1 is in the row space of B and A=J+I−BᵀB, ker B is exactly the five-dimensional adjacency-1 subspace. The centered projected columns affinely span it; the positive average gives an interior cone apex. Polarity with h=1−4u gives Bu=1 and u≥0. Independent positive-support columns give vertices of this standard-form polytope: a leaf forces an isolated unit edge, and every other component has minimum degree 2 and at most as many edges as vertices, thus is an odd cycle by independence. This gives precisely 12 five-cycle and 10 triangle-plus-edge supports and the complementary 5- or 6-vertex facets. A six-vertex facet has affine dimension 4 and its sole affine dependence has nonzero entries on all six vertices, with signs 3 against 3. The specified three deletions triangulate it; all proper faces are simplices, so local triangulations necessarily agree on common faces without extra vertices. Independent checking confirmed zero mismatches across all 231 facet pairs. It also verified all 42 selected Z row determinants have magnitude 1, all complementary B determinants magnitude 2, and det(ZᵀZ)=162. Thus Zᵀ is an isomorphism on ker B with volume factor sqrt(162), and this is a unimodular star triangulation in the whole stated lattice. Dividing 42/5! by sqrt(162) gives 7/(180 sqrt(2)); each simplex has volume 1/(1080 sqrt(2)). This is the intrinsic orthonormal spectral volume, not the volume of an unnormalized eigenvector basis.

## originality

PASS

Best of knowledge: the precise metric volume and the equal-volume unimodular decomposition were not found in the inspected literature. The configuration, 22 facets, their 12+10 split, and the fractional-matching input are not credited as new. The older same-object literature leaves a concrete priority risk.

## value

PASS

This is a canonical spectral realization used in graphical-design theory, not an arbitrary linear model. The exact metric volume gives a comparison invariant beyond its known face numbers. More significantly, the complete 42-piece triangulation gives unit lattice simplices and translates the Euclidean calculation into integer determinants, an explicit structure potentially usable in further metric or lattice comparisons without assuming a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
