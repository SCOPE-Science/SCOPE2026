# Independent mathematical audit

## correctness

PASS

The tree has N=3+2m+2mℓ vertices. On connected support inverse trace of L+11ᵀ/N minus one is the stated spectral sum, and its second variation is a positively weighted sum of nonzero Laplacian-perturbation squares. A missing edge disconnects a tree and makes the extended objective infinite; compactness of the feasible closure gives existence and strict convexity gives uniqueness. Hence automorphisms force the three orbits for the original unrestricted problem. The three cut sizes are (N−1)/2, 1+ℓ and 1, with multiplicities 2, 2m and 2mℓ. Their products with the complementary sizes give exactly A,B,C. At fixed middle weight y, decreasing cost in the other two weights gives x=min(1/2,1−my), z=(1−y)/ℓ, on 0<y<1/m. The strictly convex resulting function has left and right derivatives at 1/(2m) equal to −4m²T and 4m²(A/m−T). This gives the cases including equality, both stationary formulas, and all holding signs (in particular z<1). Independently checked the integer certificates by forward differences: define D=m(Cℓ−(2m−1)²B), E=D+(2m−1)²A from the cut counts. To replay, use four evaluations in ℓ=0,1,2,3 to recover each cubic by Newton interpolation and recover its coefficients as polynomials of m using m=2,...,8. In the binomial basis in m−2 the leading coefficients of the two ℓ-cubics have positive sign, and all other coefficients have negative sign, with zero trailing terms. Descartes plus the endpoint signs gives one positive root each. For E at ℓ=4m²−8m+5 and +6, and for D at ℓ=4m²−6m+4 and +5, respectively, form the forward-difference rows of the substituted polynomials at m=3,...,12 (degree at most nine). The first entries of successive difference rows are sign-uniform after zeros: (−,7 degree), (+,6), (−,5), (+,7). Thus the signs hold for all integral m≥3 because the binomial basis in m−3 is nonnegative. At m=2, (D,E) at ℓ=5,6,7,8 are (−3872,−596), (−3456,864), (−2224,3284), (16,6856). This proves both cutoffs, the exceptional case and the 2m−1 window, without promoting numerical eigenvalue checks to universal evidence. The supplied script was inspected, not executed. Scope: symmetric uniform-stationary walks on the exact tree, using the inverse spectral normalization specified.

## originality

PASS

Bounded to the exact three-generation three-phase holding law, including both integer boundaries. Effective resistance and convex Kemeny design are established methods. The closest inspected branching threshold is on a distinct, shorter tree and does not establish where holding transfers between two internal levels in this tree.

## value

PASS

The explicit switches identify when unused transition mass moves from the root to the first branching vertices and when neither level holds. The two cutoffs have the same leading quadratic scale but leave a provably distinct linear-width intermediate phase. This is a full active-constraint classification for a natural infinite tree family and supplies the optimizer without solving an edge-sized optimization or relying on a finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
