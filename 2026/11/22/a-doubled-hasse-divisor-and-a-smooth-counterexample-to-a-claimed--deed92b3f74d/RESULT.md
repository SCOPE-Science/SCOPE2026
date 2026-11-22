# A doubled Hasse divisor and a smooth counterexample to a claimed Picard ordinarity theorem in characteristic thirteen

## Finding
For every algebraically closed field \(k\) of characteristic \(13\), consider smooth genus-three Picard curves
\[
 C_{a,b,c}:\quad y^3=f(x)=x^4+ax^2+bx+c,
 \qquad (a,b,c)\in k^3.
\]
Define \(T=a^2-8c\) and the quartic discriminant
\[
 \Delta=9c^3+2a^2c^2+ab^2c-b^4+3a^4c-4a^3b^2.
\]
All coefficients are interpreted in characteristic \(13\). The smooth parameter space is \(\Delta\ne0\). On it, the determinant of the coefficient-form Hasse–Witt matrix in the explicitly specified basis equals
\[
 \det H=11T^2\Delta^2.
\]
The nonordinary Hasse divisor is consequently exactly twice the smooth, nonempty hypersurface \(T=0\). The Cartier \(a\)-number is \(0\) if \(T\ne0\) and \(2\) if \(T=0\); values \(1\) and \(3\) never occur. On the coefficient-marked \(\mathbb F_{13}\)-family, there are exactly \(1,884\) smooth ordinary curves and \(144\) smooth curves of \(a\)-number \(2\) (and \(169\) singular parameter triples).

In particular, if \(\alpha^2=8\) in \(\mathbb F_{169}\), the smooth curve \(y^3=x^4+\alpha x^2+1\) has Cartier \(a\)-number \(2\), despite having nonzero constant coefficient and \(13\equiv1\pmod3\). This is a concrete counterexample to the unrestricted conclusion of Nourozi–Rahmati, Theorem 3.1(1), arXiv:2306.07823v1 (13 June 2023). The counterexample is to that stated theorem, not to all related results.

## Assumptions and scope
The base characteristic is exactly \(13\), and \(k\) is algebraically closed, or an arbitrary perfect field for statements about rational coefficient triples. \(a,b,c\) are coefficients of monic depressed quartics, not isomorphism classes. The smooth projective model of \(y^3=f(x)\) has genus three when \(f\) is squarefree because the degree-three cover has five totally ramified branch places (the four simple roots plus infinity). The discriminant \(\Delta\) above is the standard monic quartic discriminant reduced modulo \(13\). The Cartier \(a\)-number is \(3-\operatorname{rank}\mathcal C\), and this is not a claim about the geometric \(13\)-rank or the Newton polygon.

## Proof
Let \(\omega_0=dx/y^2\), \(\omega_1=x\,dx/y^2\), and \(\omega_2=dx/y\). These form a basis of \(H^0(C,\Omega^1)\) by the pole orders at infinity. For \(p=13\), Cartier's identity gives
\[
 \mathcal C(x^i dx/y^2)=y^{-2}\mathcal C(x^if^8dx),\qquad
 \mathcal C(dx/y)=y^{-1}\mathcal C(f^4dx),
\]
where the target coefficients are the thirteenth roots of the ordinary polynomial coefficients. Thus \(H\), the matrix of the thirteenth powers of Cartier's coefficients (with source columns and target rows), is block-diagonal, with a \(2\times2\) block \(M\) and a scalar \(d\):
\[
 M=\begin{pmatrix}[x^{12}]f^8 &[x^{11}]f^8\\ [x^{25}]f^8 &[x^{24}]f^8\end{pmatrix},\qquad d=[x^{12}]f^4.
\]
Here \([x^j]F\) denotes the coefficient of \(x^j\) in \(F\). The order of the first two target basis vectors may transpose the displayed block; its determinant and rank are unchanged. Exact polynomial expansions in \(\mathbb F_{13}[a,b,c]\) establish
\[
 d=6T,\qquad \det M=4T\Delta^2,
\]
which imply \(\det H=24T^2\Delta^2=11T^2\Delta^2\). These are full polynomial identities, not identities only at sampled points. The first verifier independently constructs both sides in a four-variable sparse polynomial ring and asserts exact coefficient equality.

When \(\Delta\ne0\) and \(T\ne0\), both \(M\) and \(d\) are invertible. When \(T=0\), the determinant vanishes, but \(M\) is nonzero on the smooth locus. Indeed, when \(c\ne0\), scale the quartic variables over \(k\) to arrange \(c=1\); this preserves whether the Cartier block is zero. In this normal form \(T=0\) means \(a^2=8\), and the coefficients become
\[
 M_{10}=b(4-a^2),\qquad M_{11}=5a^4-a^2-ab^2+2.
\]
Since \(a^2=8\ne4\), \(M_{10}\ne0\) whenever \(b\ne0\). If \(b=0\), \(M_{11}=2\ne0\). If \(c=0\), then \(a=0\), and squarefreeness of \(x^4+bx\) forces \(b\ne0\); in that case \([x^{11}]f^8=8b^7\ne0\). Consequently \(\operatorname{rank}H=1\) everywhere on \(T=0,\Delta\ne0\), giving \(a=2\). Since \(\partial T/\partial c=-8\ne0\), the underlying divisor \(T=0\) is reduced and smooth, while its determinant multiplicity is exactly two.

For \(k=\mathbb F_{13}\), there are \(13^3-13^2=2028\) monic squarefree depressed quartics, by translation eliminating the cubic term in the space of all monic quartics. For the \(169\) marked triples on \(T=0\), exactly \(25\) have \(\Delta=0\): the sole singular \(a=0\) triple has \(b=0\); for each \(a\in\mathbb F_{13}^{\times}\), substituting \(c=5a^2\) into \(\Delta\) gives \(7a^6+a^3b^2-b^4\), and the zero condition is \((b^2/a^3)^2-(b^2/a^3)-7=0\), whose roots are \(5,9\). Exactly one of \(5a^3\) and \(9a^3\) is a nonzero square, giving exactly two values of \(b\) per nonzero \(a\). Therefore \(169-25=144\) nonordinary smooth triples and \(2028-144=1884\) ordinary ones. The exact polynomial verifier checks these finite counts independently.

For the explicit smooth counterexample, \(c=1,b=0,a^2=8\) makes \(\Delta=9\), \(d=0\), and \(M=\operatorname{diag}(0,2)\), hence \(\operatorname{rank}\mathcal C=1\) and \(a(C)=2\).

## Verification
Run the two self-contained, Python-3-standard-library-only programs `verify_picard13_global.py` and `verify_picard13.py`. The first independently expands the complete four-variable coefficient identities, checks the full \(13^3\) marked census, and evaluates the exhibited smooth counterexample. Its terminal certificate is `PICARD13_GLOBAL_VERIFIED`. The second uses a different three-variable polynomial representation specialized to \(c=1\), checks the factorization there, and exhaustively enumerates \(\mathbb F_{169}\)-parameters in two different quadratic-field presentations. Its terminal certificate is `PICARD13_CARTIER_VERIFIED`. The programs enumerate only the stated finite fields; the proof of the geometric statement is the exact polynomial identities and rank argument, not the finite census.

## Relationship to prior work
Nourozi and Rahmati's arXiv:2306.07823v1, Theorem 3.1(1), asserts \(a(C)=0\) for smooth Picard curves with nonzero constant term when \(p\equiv1\pmod3\); the formula above exhibits an explicit smooth exception in characteristic \(13\). Their work establishes the standard Cartier basis but does not contain the correct determinant stratification. The arithmetic Picard-curve framework and depressed quartic models precede this calculation (Bouw–Koutsianas–Sijsling–Wewers). Laga's later bielliptic Picard-curve work, and the recorded calculation of superspecial Prym points, treat the subfamily \(b=0\); the present classification includes all \(b\) and the exact entire coefficient-marked census. Takizawa's older hypergeometric point-count formulas address a different invariant. This result does not claim first discovery of any individual \(b=0\) example. Searches did not locate an already-published identical full characteristic-thirteen stratification, but database search cannot prove uniqueness.

## Limitations
No independent audit has been performed. The classification is for coefficient-marked depressed quartics, not distinct geometric isomorphism classes. It determines the first Cartier rank and the divisor, but not complete Cartier iterates, the geometric \(13\)-rank, Newton polygons, or all Ekedahl–Oort types. Unindexed historical tables or a corrected journal version of the 2023 preprint could affect the historical-priority comparison; these do not affect the direct polynomial calculation.

## References
1. V. Nourozi and F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, arXiv:2306.07823v1, 13 June 2023, Theorem 3.1, https://arxiv.org/abs/2306.07823.
2. I. Bouw, D. Koutsianas, J. Sijsling and S. Wewers, *Conductor and discriminant of Picard curves*, https://doi.org/10.1112/jlms.12323.
3. F. Takizawa, *The number of rational points of a family of Picard curves over a finite field*, arXiv:1608.07474, https://arxiv.org/abs/1608.07474.
4. V. Laga, work on bielliptic Picard curves, https://doi.org/10.1112/jlms.70347.
