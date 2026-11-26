# Independent mathematical audit

## correctness

PASS

Reconstructed both the geometric classification and the arithmetic count from RESULT.md 24–45. The affine gradient and the unique smooth point at infinity exclude exactly r²=4. The line at infinity is a hyperflex; all other Y=cZ lines meet there simply. For X=bZ the monic restriction is a square exactly if b³=(r²−4)/4. For X=a(Y+sZ), a≠0, matching cubic, linear and constant terms of the square of a monic quadratic forces its lower coefficients a³/2 and 3s², then a³=9s−s⁻³, with s≠0. The remaining quadratic coefficient gives Q_r(s²)=0. Q_r(0)=−1; at a common root with its derivative, substituting r=−(z²+1)/z gives Q_r(z)=−(z²−1)², forcing r²=4. At z=±1/3, the respective values are 4(r−2)/27 and −4(r+2)/27, so the cube target is never zero on the smooth locus. Thus there are 1+3+24 distinct lines, and their normalized coordinates recover the parameters, so the tower is Frobenius-equivariant. For q≡2 mod 3 each v gives one point (u,v) on v²=u³+1. Duplication with slope 3u²/(2v) gives v(2P)=(v⁴+18v²−27)/(8v³), and R(z)=−2v(2P) with v=3z. The two rational preimages, when present, differ by T=(−1,0); the addition slope v/(u+1) gives v(P+T)/v(P)=−3/(u+1)². Since the discriminant −3 of the primitive-cube-root polynomial is nonsquare, exactly one of the two z's is square. The finite fibre argument in fact holds at r=±2 as well: O and T map to O, not to any finite v, and the special fibres factor as (z−1)³(3z+1) and (z+1)³(3z−1), respectively. Hence the (q−1)/2 nonzero squares z map injectively to parameters; deleting the two singular parameters leaves (q−5)/2 with four rational lines and (q+1)/2 with two. The rationality is that of lines, not contacts. Read VERIFICATION.md, verify.py and examples.csv without executing the uploaded program. Its prime-field data are illustrative; the proof uses no prime-field restriction.

## originality

PASS

The supported distinct finding is the coefficient-marked finite-field frequency theorem, together with the explicit radical description of the non-distinguished bitangents used to prove it. The geometric 28-line count, the 24+3+1 orbit structure, and the four distinguished geometric lines have substantial prior coverage. The inspected primary passages do not give the rational square-fibre calculation or exact population of parameters producing four rational lines.

## value

PASS

Rational bitangents, including hyperflexes, are a natural invariant of a canonical genus-three quartic. A uniform classification over all permitted finite fields and its exact coefficient frequencies address a concrete arithmetic question not settled by the geometric count. The elliptic translation argument explains the rigidity, and the tower gives a reproducible Frobenius computation beyond the base-field count. This is not a count of moduli classes or of rational contact points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
