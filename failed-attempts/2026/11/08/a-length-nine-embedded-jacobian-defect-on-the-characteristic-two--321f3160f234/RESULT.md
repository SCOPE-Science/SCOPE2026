# A length-nine embedded Jacobian defect on the characteristic-two Steiner quartic

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(S\subset\mathbb P^3_k\) be the Steiner quartic
\[
F=X^2Y^2+X^2Z^2+Y^2Z^2+WXYZ=0.
\]
Let \(J\subset S\) be the *scheme-theoretic* singular locus defined by \(F\) and all its first partial derivatives, and put \(L=J_{\mathrm{red}}\). Although \(L\) is the familiar union of three concurrent lines, \(J\) has exactly three embedded zero-dimensional nilpotent defects, located at
\[
P_X=[0:1:0:0],\qquad P_Y=[0:0:1:0],\qquad P_Z=[0:0:0:1]
\]
when projective coordinates are ordered \([W:X:Y:Z]\). Each defect has length \(3\) and nilpotent filtration dimensions \((2,1)\), so the nilradical \(\mathcal N\) of \(\mathcal O_J\) has total length \(9\). In particular, the Hilbert polynomials are
\[
P_{L}(d)=3d+1,\qquad P_J(d)=3d+10.
\]
At every other point of \(J\), including the common triple point, the Jacobian singular scheme is reduced. The nilradical satisfies \(\mathcal N^3=0\) and \(\mathcal N^2\ne0\).

## Assumptions and scope

Everything is scheme-theoretic over an algebraically closed field of **characteristic exactly two**. Coordinates are \([W:X:Y:Z]\); the three points above lie on the coordinate double lines at \(W=0\). The word *embedded* means a zero-dimensional associated contribution of the Jacobian singular scheme, *not* an embedded component of the quartic itself. No comparison statement for other characteristics is asserted. The well-known equation, normalization and reduced singular locus are background, not new findings.

## Proof

Write \(Q=XY+XZ+YZ\). In characteristic \(2\), \(F=Q^2+WXYZ\), and therefore its scheme-theoretic Jacobian ideal in \(k[W,X,Y,Z]\) is
\[
I=(F,\ XYZ,\ WYZ,\ WXZ,\ WXY).
\]
It is essential to retain \(F\): Euler's identity does not make the degree-four defining equation redundant in characteristic \(2\).

On the chart \(W\ne0\), with \(W=1\), the three generators \(XY,XZ,YZ\) make both \(XYZ\) and \(Q^2\) vanish. Hence the chart has the reduced ring
\[
k[X,Y,Z]/(XY,XZ,YZ),
\]
the union of three coordinate axes. In particular the common triple point is reduced as a point of the singular scheme.

By symmetry it remains to analyze \(X\ne0\). Introduce \(a=W/X\), \(b=Y/X\), \(c=Z/X\). The Jacobian quotient is exactly
\[
R_X=k[a,b,c]/(ab,ac,bc,b^2+c^2).
\]
Indeed the equation \(F/X^4=b^2+c^2+b^2c^2+abc\) reduces to \(b^2+c^2\), while the differentiated generators reduce to \(bc,abc,ac,ab\). Its radical is \((b,c)\) and the reduced quotient is \(k[a]\). Set \(N=(b,c)\subset R_X\). The relations imply \(aN=0\), \(bc=0\), \(b^2=c^2\), \(b^3=c^3=0\). Every element of \(R_X\) thus has a unique expression
\[
f(a)+\alpha b+\beta c+\gamma b^2,
\]
with \(f(a)\in k[a]\) and \(\alpha,\beta,\gamma\in k\). Uniqueness follows, for example, by the standard monomials of the Gröbner basis \(c^3,ab,ac,bc,b^2+c^2\) (which holds over the prime field and hence any extension). Thus \(N\) has vector-space basis \(b,c,b^2\), its successive nonzero layers \(N/N^2\) and \(N^2\) have respective lengths \(2\) and \(1\), and it is annihilated by \(a\). This accounts for exactly one length-\(3\) defect at \(a=0\), namely the point \([W:X:Y:Z]=[0:1:0:0]\).

The symmetric \(Y\ne0\) and \(Z\ne0\) charts give precisely two other such defects. These four standard projective charts cover \(\mathbb P^3\), so there are no further associated points or nilpotents. Therefore
\[
0\longrightarrow\mathcal N\longrightarrow\mathcal O_J
\longrightarrow\mathcal O_L\longrightarrow0
\]
is exact, with \(\mathcal N\) supported at three distinct points and total length \(3+3+3=9\). The reduced curve \(L\) is the union of three concurrent projective lines; the union has Hilbert polynomial \(3d+1\), as follows by identifying three copies of \(\mathbb P^1\) at one common point. Since a length-\(9\) skyscraper sheaf contributes the constant \(9\), additivity of Euler characteristics yields \(P_J(d)=3d+10\) for all sufficiently large \(d\).

## Verification

Run `python verify.py` using Python and SymPy. It recomputes the characteristic-two partial derivatives, the projective and affine Gröbner bases, the local nilpotent relations, and Hilbert-function values in degrees \(0\) through \(12\). It verifies
\[
H_J(0),\ldots,H_J(7)=(1,4,10,16,21,25,28,31)
\]
and \(H_J(d)=3d+10\) for each tested degree \(5\le d\le12\). The program prints `ALL_CHECKS_PASSED`. The proof above, rather than a bounded computation, establishes the local exhaustion and the eventual Hilbert polynomial for all algebraically closed fields of characteristic two.

## Relationship to prior work

Hartshorne and Polini [1, Example 6.4] give exactly this homogeneous equation, the Veronese normalization and the *reduced* union of three double lines, and analyze divisor classes. Their principal arguments explicitly assume characteristic zero [1, Introduction]. In particular the term "singular locus" in [1] is not a determination of the characteristic-two scheme cut out by the equation and partial derivatives. Kleiman [2, Introduction, Section B] already explains that in characteristic two the classical pinch-point contributions of the Steiner projection occur with multiplicity two. That established ramification phenomenon is not claimed as new, nor does its length-six ramification cycle state the length-nine nilradical of the **image Jacobian singular scheme**. The relevant new invariant is the embedded scheme structure and its exact local filtration and global Hilbert polynomial.

## Limitations

The result is restricted to the displayed Steiner quartic over fields of characteristic two and does not classify Jacobian schemes of all Veronese projections. The result does not claim a new reduced singular locus or a new ramification count. Independent mathematical validation has not been performed. Historical priority is provisional because specialist literature on characteristic-two projection singularities and some older full texts may contain an equivalent scheme-theoretic calculation.

## References

[1] R. Hartshorne and C. Polini, *Divisor class groups of singular surfaces*, arXiv:1301.3222 (public preprint dated 2013-01-15), Example 6.4 and Introduction. https://arxiv.org/abs/1301.3222 ; complete text: https://ar5iv.labs.arxiv.org/html/1301.3222 .

[2] S. L. Kleiman, *The enumerative theory of singularities*, in *Real and Complex Singularities* (1977), pp. 297–396, DOI 10.1007/978-94-010-1289-8_10, especially Introduction, Section B. https://doi.org/10.1007/978-94-010-1289-8_10 .
