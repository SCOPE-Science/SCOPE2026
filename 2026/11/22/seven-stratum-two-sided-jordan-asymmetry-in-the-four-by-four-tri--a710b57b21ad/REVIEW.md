# Independent mathematical audit

## correctness

PASS

The matrix units with fixed column give the leading principal blocks for L_x; those with fixed row give the transposed trailing blocks for R_x. The common size-four block (and the common zero size-one block) cancel in all rank differences. Write d_i=rank(L_x^i)-rank(R_x^i) and let alpha and gamma indicate a,c nonzero. If b is nonzero, the leading and trailing size-three blocks have ranks 1+alpha and 1+gamma, and their squares have ranks alpha and gamma. Adding the size-two rank contributions yields d_1=2(alpha-gamma), d_2=alpha-gamma, d_3=0. Thus the block-multiplicity differences are Delta_3=d_2 and Delta_2=d_1-2d_2=0. The count for each nonzero sign is q^3(q-1)^2. If b=0, d_2=0 and d_1 is the difference of two independent scores of (a,d) and (c,e), each score having 1, q-1, q(q-1) choices at values 0,1,2. Including the free f gives q^2(q-1) and q(q-1)(q^2-q+1) per signed score difference of magnitude two and one respectively. Subtraction from q^6 gives the stated zero count, and division by q^6 gives the similarity probability. Equal dimension forces Delta_1=-3Delta_3-2Delta_2, and Delta_4=0. This argument uses only rank and indicator tests, applies also in characteristic two and to extension fields, and makes all seven strata nonempty for q>=2. For T_3, canceling the common size-three block leaves at most one size-two block per side, confirming the two first-occurrence claims for the triangular family.

## originality

PASS

The distinct result supported by the comparisons is the signed two-sided regular-action law for all radical elements of T_4, including its exact similarity probability and the support strata. Neither the available general single-matrix Jordan counting theorem nor the closely related two-sided cyclic-radical census determines it. The known sign symmetry from diagram reversal explains equality of opposite fibers, not their seven counts or their support conditions.

## value

PASS

The directed chain is the elementary noncommutative incidence algebra where one can ask if opposite full regular actions give the same Jordan type at the same element. Size four is the first chain allowing a discrepancy in size-three blocks or a size-two discrepancy of magnitude two. The exact law separates the mechanism with nonzero b from the b=0 one, and gives the chance of similarity rather than just a counterexample or the sign symmetry forced by duality. This is a concrete baseline for two-sided Jordan statistics, not an arbitrary parameter slice or a census of the individual defining Jordan types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
