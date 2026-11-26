# Independent mathematical audit

## correctness

PASS

The involutions give the two stated quotient maps, and the pulled-back regular differentials span the odd and even powers in a basis of H⁰(C,Ω¹); the norm map is therefore a separable isogeny, with dual the sum of pullbacks. Inversion t=1/u and z=w/u³ sends the second quotient to z²=1−t⁵; its hyperelliptic twist changes the Frobenius sign, while the curve isomorphism after adjoining √−1 respects the canonical polarization on Jacobians. Independent finite computation used the quadratic character on F₁₁ and, on F₁₂₁, the F₁₁ quadratic character of the norm a²+b² for a+bi. Summing the characters over all u and adding one point at infinity for the degree-five models, two for the degree-ten model, gives (16,118), (8,118), (12,114) for the two quotients and C. The power sums −4,4 give middle coefficient 6; the functional equation gives the two stated quartics (and hence L_C and order 14080). The mod-3 reduction T⁴+2T³+T+1 has no root and has nonzero remainders against T²+1,T²+T+2,T²+2T+2, the three irreducible monic quadratics. Irreducibility forces base-field simplicity, the unequal polynomials rule out base-field isogeny, and 6≠0 mod 11 gives ordinarity. The degree-two isomorphism follows from the twist, and degree one is ruled out by nonisogeny. This does not prove absolute simplicity or a polarized product decomposition of J(C). The character sums and remainder tests give an exact replay independent of the frozen verify.py, which was inspected but not executed.

## originality

FAIL

The local polynomial singled out as the numerical witness is explicitly tabulated for the very same curve, not just predicted by a general algorithm: the LMFDB curve 160000.c.800000.1 is y²=x⁵−1 and its L-function lists the p=11 polynomial 1+4T+6T²+4pT³+p²T⁴ and class 2.11.e_g. The other factor is determined from this row by the explicit quadratic twist. In the known geometric square decomposition the elementary quotient maps identify those two curves. The arithmetic nonisogeny, simplicity, ordinarity, quadratic identification and product numerator then follow directly from that row and the quotient/twist identities, without a distinct further arithmetic claim. This is a coverage judgment, not an allegation that one earlier source states the assembled result verbatim or that its computations are false.

## value

FAIL

The geometric object and distinction between arithmetic and geometric decomposition are well motivated, but the exact witness at 11 is an existing equation-specific table entry and all claimed companion invariants follow by the elementary quotient and twist and standard readings of the tabulated polynomial. No further motivated unknown invariant or new descent mechanism survives simply omitting the recounted coefficients. The result is a correct worked example, not a new exact invariant under the audit standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
