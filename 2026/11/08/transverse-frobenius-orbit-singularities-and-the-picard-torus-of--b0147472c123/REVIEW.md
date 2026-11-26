# Independent mathematical audit

## correctness

PASS

The known normalization and geometric fiber theorem applies to the coefficient map in RESULT.md:41–53, including its singleton fiber and immersion at infinity. For the d distinct roots of G at a multiple fiber, the first-order coefficient vectors are minus G^(n/d-1) times G/(Z-a_j). Evaluation at the distinct roots proves independence over the geometric field, even when char(k) divides n/d. For the formal step, the completed ambient ring maps into the product of the d normalized branch rings, and its image lies in the subring B of tuples with common constant. The kernel is the completed curve ideal by the finite normalization injection and exactness of completion. The cotangent space of B is the direct sum of the d branch cotangent spaces. Independence makes the ambient cotangent map onto this direct sum; lifting successive degrees in the complete rings gives surjectivity onto B. This also proves smoothness at the immersive singleton fibers. B is the axes ring, seminormal, with conductor the positive-order terms, geometric multiplicity d (its associated graded has d basis vectors in each positive degree) and defect d-1. Over k, faithful base change gives the same gluing modulo the conductor with residue algebras k and k_d; principal units cancel. The normalization sequence for the Picard functor has no further quotient by constants, since the global units on the curve and its normalization are both scalars. The normalized Picard group has trivial connected part, so the connected group is precisely the product of the indicated unit quotients. The augmentation lattice of each factor has no nonzero Frobenius-invariant character, as expected for a nonsplit factor; 'split product' refers to separation of factors, not a split torus. Hilbert 90 gives the rational group orders, and replacing a degree-d closed point by a degree-one point gives the stated point counts and Euler factors. I inspected checks/field_orbits.py and checks/hilbert_functions.py and their frozen logs without executing them. The former really checks field coefficient fibers and ranks, but prints a formula evaluation for the Picard order, not an independent Picard computation; the latter checks finite Hilbert-function values, not a general stabilization bound. Neither is needed for the all-parameter proof.

## originality

PASS

Passes for higher-dimensional independent branch tangents and the resulting local and arithmetic Picard classification, as distinguished in the finding. The normalization, orbit classification, orbit counts and consequent point counts and zeta factors are prior coverage or routine deductions, not credited as new. Degree-two nodes and quotient factors overlap earlier plane-curve work. Neither the identified higher-n fiber theorem nor the general gluing formalism supplies the missing independent directions. No equivalent general-n result was found in the inspected sources; this is a bounded priority assessment.

## value

PASS

The established fibers by themselves leave tangencies and possible additive Picard factors unresolved. The all-characteristic local structure resolves those issues, computes the otherwise unknown normalization defects, and determines the actual algebraic group over the finite field, not just a point count. These are useful intrinsic invariants for an existing family of rational curves with many rational points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
