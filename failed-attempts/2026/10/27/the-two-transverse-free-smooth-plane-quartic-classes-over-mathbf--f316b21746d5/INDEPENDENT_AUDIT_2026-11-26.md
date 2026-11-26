# Independent mathematical audit

## correctness

PASS

The 15-dimensional coefficient space has 32,767 nonzero masks and no nontrivial scalar equivalence. On each of the seven lines, a binary quartic is squarefree iff its one-variable dehomogenization has degree at least three (no multiple root at infinity) and gcd one with its derivative. In coefficients a,b,c,d,e from U^4 to V^4, the derivative at V=1 is bU^2+d, recovering the three stated cases, including checking a at infinity when b=0. Fresh exact substitution found 2,559 transverse-free masks, with 25 surviving the necessary Jacobian test at rational points. All 75 affine-chart ideals (F, F_X, F_Y, F_Z) on these 25 have Gröbner basis {1}, establishing geometric smoothness over the algebraic closure. Fresh substitution by the 168 invertible matrices identifies orbits of masks 6438 and 20181, with sizes 24 and 1, point counts 7 and 0, and stabilizers 7 and 168. All seven restrictions of 20181 equal the square of U^2+UV+V^2, the unique monic irreducible binary quadratic with no rational root in rational basis coordinates, so the property holds in every rational basis. Every line in the filling case has three rational intersection points and its residual divisor of degree one is rational, hence repeats one of them. Smooth plane quartic genus is three. The warning that pointlessness alone does not suffice also holds: the sum of the six square monomials X^4,Y^4,Z^4,X^2Y^2,Y^2Z^2,Z^2X^2, plus X^3Y+XY^3+X^2YZ, is 1 at every rational point. Its common gradient zeros can only be (0:0:1) and (1:0:1), neither on it, and the line Z=0 has squarefree restriction with all five coefficients one. Fresh replay: python3 /workspace/branches/de0a8fef-b547-4c63-9c89-469146641e3d/independent_recheck.py with SymPy; the shipped scripts were inspected rather than executed.

## originality

FAIL

The closest indexed rational-line Bertini spectrum explicitly includes the identical two-class census, with the same singleton, and gives a broader spectrum. The ancillary orbit sizes, stabilizers, line mechanisms and pointlessness warning are elementary consequences of that classification and its supplied representatives; this is not just a possible historical overlap.

## value

FAIL

The zero-bin dichotomy is a natural and worthwhile question at the sharp Bertini degree, but it has already been answered within a broader exact spectrum. The successful replay strengthens confidence, not the scientific scope. The remaining line and stabilizer facts are immediate implications, so no independently useful unknown classification or repair survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
