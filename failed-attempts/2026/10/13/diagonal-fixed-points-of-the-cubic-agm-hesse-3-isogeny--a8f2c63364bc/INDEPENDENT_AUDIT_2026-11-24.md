# Independent mathematical audit

## correctness

PASS

Away from mu^3=1 the denominator is nonzero. Literal equality mu'=mu gives the degree-five polynomial 9mu^3(mu^2+mu+1)-(mu+2)^3, whose product expansion is (mu-1)(3mu^2+2mu+4)(3mu^2+4mu+2). The excluded root is 1 and the two quadratics give the claimed four distinct roots, of moduli sqrt(4/3) and sqrt(2/3). To check the j labels independently, set w=3mu and W=w^3. Reduce W(W+216)^3 and (W-27)^3 in the basis (1,w). Modulo w^2+2w+12 the vectors are (177045504,-164888576) and (-5403,5032), ratio -32768. Modulo w^2+4w+6 they are (234984000,110960000) and (29373,13870), ratio 8000. Each denominator is nonzero at the roots. Sage's documented (field discriminant, conductor, j) entries have conductor one and discriminants -11 and -8. Otsubo Theorem 1.1 applies since both parameters are allowed and equal, giving the endomorphism and the indicated intersection of the kernel line with H(mu). The frozen exact checker was inspected but not executed; the independent reduction used integer arithmetic and the cited isogeny and CM statements were checked separately.

## originality

FAIL

The complex parameter list was not found printed in the checked prior work. Nevertheless Otsubo's stronger result already specifies the full correspondence, maps and kernels, and his j formula specifies the class of every parameter. Restricting those exact formulas to the diagonal requires only elementary univariate factorization and residue substitution, followed by a known CM table. This is coverage by direct implication, not an assertion that the modular-polynomial paper gives the Hesse-parameter lifts.

## value

FAIL

The distinction between a literal parameter loop and a loop up to isomorphism is legitimate. Here the four-point list is a routine diagonal substitution and quadratic solve in a published explicit relation, and the interpretation consists of evaluated known j and CM formulas. No additional structural selection criterion or independently nonmechanical exact computation is demonstrated. The valid list may be pedagogically useful but the surviving difference is not a standalone scientific contribution under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
