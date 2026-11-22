# Independent mathematical audit

## correctness

PASS

Edge vanishing on a segment of a polynomial extends to the supporting line. After scaling the cube to [-1,1]^3, sign-flip averaging decomposes each candidate harmonic polynomial into eight parity sectors x^epsilon1 y^epsilon2 z^epsilon3 Q_epsilon(u,v,w), where u=x²-1 etc. Vanishing on every supporting coordinate line is exactly Q_epsilon in J=(uv,uw,vw). The degree<=6 bound restricts each Q degree: triple-odd sector vanishes by degree, six non-even sectors have only uv,uw,vw and an invertible 3x3 Laplacian coefficient matrix with determinant -2(2+4e1)(2+4e2)(2+4e3). The even sector has ten monomials in J of degree<=3; transformed Laplacian has a 9x10 coefficient matrix with a nonzero 9x9 minor 110592, so its kernel is at most one-dimensional. I independently used exact SymPy algebra to confirm this minor, rank 9, all parity determinants and harmonicity and twelve edge-line restrictions of V=(u-v)(u-w)(v-w). Therefore the kernel is span{(x²-y²)(x²-z²)(y²-z²)}; degree-six existence and nonexistence below six follow for all real/complex nonhomogeneous polynomials, not by sampling isolated edges.

## originality

PASS

PASS best of knowledge for minimum degree six and one-dimensional degree-at-most-six kernel, not for Vasilyev’s pre-existing sextic witness. Read primary arXiv:2506.24116 Theorem 1 and discussion: construction exists in all dimensions and identifies the Vandermonde harmonic sextic for d=3, but does not assert a lower bound or full minimal-degree classification. Published cubic sampling results evaluate vertices, which are weaker than vanishing on edge lines.

## value

PASS

The classical Wavre cube-edge harmonic-polynomial question has a known explicit construction. Its minimum possible degree and uniqueness among all polynomials without imposing cubic symmetry are natural sharp complexity and rigidity invariants of that same geometrically motivated existence problem. The finite algebraic classification is complete in the exact natural onset range, not an arbitrary table or a trivial reexpression of the witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
