# Complete quadratic phase ambiguity and eight-sample intensity reconstruction on Cassini ovals

## Finding

For every \(r>0\), put \(C_r=\{z\in\mathbb C:|z^2-1|=r\}\). If complex polynomials \(p,q\) of degree at most two have identical squared magnitudes everywhere on \(C_r\), then either \(q=\eta p\), \(|\eta|=1\), or both polynomials are even. In the latter case, writing \(p(z)=A+B(z^2-1)\), the complete ambiguity class, modulo constant unimodular factors, is

\[
 p(z),\qquad p^\#(z)=r\overline{B}+\frac{\overline{A}}{r}(z^2-1).
\]

The two possibilities may agree up to phase. Consequently, every polynomial with a nonzero linear coefficient is phaselessly identifiable on a *single* Cassini oval. Universal identification fails: \(z^2-1\) and the constant \(r\) have equal magnitudes there without being scalar multiples.

The real linear space spanned by complete degree-at-most-two intensity profiles restricted to \(C_r\) has dimension exactly eight. Eight generic point measurements, even if all points lie on any chosen nonempty smooth arc of the curve, linearly determine the complete restricted profile. A symmetric version uses eight points \(\pm z_1,\ldots,\pm z_4\), with representatives \(z_j\) generically chosen on any nonempty smooth arc and nonzero. This is sharp for *linear recovery of all intensity profiles*; it is not claimed as a nonlinear measurement lower bound.

## Assumptions and scope

The radius \(r\) is an arbitrary fixed positive real, including \(r=1\), for which the real curve has a crossing at the origin. All polynomials are complex and have degree at most two. The eight-point assertion is generic in the precise sense that the valid ordered tuples contain an open dense set in the product of any smooth real-analytic arc with itself, after excluding repeated points and zero. The claim concerns noiseless exact squared-magnitude data and identification up to a global factor of unit modulus.

## Proof

Write \(u=\overline z\) and introduce the polynomial

\[
 H_r(z,u)=(z^2-1)(u^2-1)-r^2=z^2u^2-z^2-u^2+1-r^2.
\]

**Algebraic restriction lemma.** For \(r>0\), a polynomial \(R(z,u)\) of bidegree at most \((2,2)\) that vanishes on a nonempty smooth arc of \(C_r\) is a complex scalar multiple of \(H_r\). Indeed, \(H_r\), viewed as a primitive quadratic in \(u\) over \(\mathbb C[z]\), is irreducible: its root-squared rational function \((z^2+r^2-1)/(z^2-1)\) has simple poles at \(z=\pm1\), so cannot be a square in \(\mathbb C(z)\). If \(H_r\) did not divide \(R\), their nonzero resultant in \(u\) would vanish at every \(z\)-coordinate of the infinitely many common points on the arc, a contradiction. Bidegree forces the quotient to be constant.

Apply this lemma to \(R(z,u)=p(z)\overline{p(\overline u)}-q(z)\overline{q(\overline u)}\). Its specialization \(u=\overline z\) is the difference of the squared magnitudes. Thus \(R=tH_r\), where \(t\) is real because both sides are Hermitian polynomials. In the ordered coefficient basis \((1,z,z^2)\), the Hermitian matrix of \(H_r\) is

\[
 J_r=\begin{pmatrix}1-r^2&0&-1\\0&0&0\\-1&0&1\end{pmatrix}.
\]

The restriction of \(J_r\) to the \(1,z^2\) coordinates has determinant \(-r^2<0\); hence \(J_r\) has rank two and range exactly the even-coordinate plane. If \(t=0\), equality of the two rank-one outer products forces \(q=\eta p\) with \(|\eta|=1\) (including the zero-polynomial case). If \(t\ne0\), the rank-two matrix \(pp^*-qq^*=tJ_r\) has range \(\operatorname{span}\{p,q\}\), so both coefficient vectors belong to the even-coordinate plane. This proves the claimed necessary alternatives.

For even polynomials set \(w=z^2-1\). As \(z\) ranges over \(C_r\), \(w\) covers \(|w|=r\). The identity \(|A+Bw|=|A'+B'w|\) on this circle is equivalent to \(|A|^2+r^2|B|^2=|A'|^2+r^2|B'|^2\) and \(A\overline B=A'\overline{B'}\). The unordered pair \(\{|A|^2,r^2|B|^2\}\) is determined by its sum and product. Accordingly either \((A',B')\) equals \((A,B)\) up to a common unimodular factor, or equals \((r\overline B,\overline A/r)\) up to one. This includes vanishing coefficients. The reflected choice satisfies \(p^\#(z)=\frac{w}{r}\overline{p(z)}\) on \(C_r\), which verifies its equal modulus.

For the sampling claim, the real vector space of all Hermitian polynomials \(\sum_{j,k=0}^2h_{jk}z^j\overline z^k\) has dimension nine. It is spanned by rank-one forms \(|p(z)|^2\) by Hermitian polarization. The algebraic restriction lemma says that its kernel on \(C_r\) is exactly the one-dimensional real span of \(H_r\), so the restricted intensity-profile span has dimension eight. One convenient real basis on the curve is

\[
 1,\ \Re z^2,\ \Im z^2,\ |z|^2,\ \Re z,\ \Im z,\ |z|^2\Re z,\ |z|^2\Im z.
\]

It is independent because no nonzero combination can equal a multiple of \(H_r\): the latter has a nonzero \(z^2u^2\) coefficient, absent from these eight forms. On any smooth analytic arc these functions remain linearly independent by the same lemma. It follows by successive choice of evaluation nodes that eight samples can give an invertible real evaluation matrix, and its determinant is a nonzero real-analytic function of eight node parameters. Hence invertible tuples are open dense on any chosen arc.

For the antipodal construction, the first four basis functions are even under \(z\mapsto-z\), while the other four are odd. Taking sums and differences of measurements at \(\pm z_j\) block-diagonalizes the evaluation system into two \(4\times4\) matrices. Each block consists of four linearly independent real-analytic functions on any nonempty smooth arc. Their determinants are nonzero analytic functions of four node parameters; their simultaneous nonvanishing is open dense. Thus four generic antipodal pairs give eight-point intensity-profile reconstruction. The dimension eight proves that fewer than eight scalar samples cannot reconstruct every profile by a linear inverse, with no conclusion asserted about nonlinear identification minimality.

## Verification

The companion `CHECKER.py` verifies the defining Cassini relation, the reflected even-polynomial ambiguity, and full rank of the symmetric eight-point interpolation matrices at three values \(r=1/2,1,2\). Its tests use direct evaluations and standard complex arithmetic. The infinite continuum statements, the genericity assertion, and the all-radius quantifiers rest on the algebraic proof above, not on numerical experiments. Reproduction: `python3 CHECKER.py` in a standard Python 3 installation, with no third-party packages.

## Relationship to prior work

Chalendar and Partington, *Phase retrieval on circles and lines* (arXiv:2403.16255, first public March 24, 2024), treat intersecting line segments and configurations of one or two circles for analytic functions, including finite-data consequences for Blaschke products. Their full manuscript's Sections 2.1--2.4 do not provide a classification for the quartic Cassini level curves, the rank-two polynomial-intensity kernel, or the exceptional even quadratic stratum. Przybyłek and Siedlecki, *A note on the complexity of a phaseless polynomial interpolation* (arXiv:1907.09371), study algorithms for choosing unrestricted complex sampling points; their Section 4 does not impose a Cassini-curve geometry or establish this constrained eight-point/ambiguity dichotomy.

Related finite interpolation rules on ellipses, parabolic arcs and geometric spirals have different curve equations and different uniqueness conditions. In particular, an ellipse allows universal finite-degree polynomial phase retrieval under suitable sampling, whereas the polynomial lemniscate here has an unavoidable, *completely classified* even-polynomial ambiguity. The number eight here is not represented as an improvement over the known general complex phase-retrieval count: the constrained Cassini measurement family is never universally phase retrieving for degree two.

## Limitations

The result is restricted to complex polynomials of degree at most two, the Cassini family \(|z^2-1|=r\), and fixed positive \(r\). It does not assert stable reconstruction uniformly in sampling geometry or as \(r\) approaches zero, nor does it classify higher-degree ambiguity families. Its eight-point lower bound concerns linear recovery of all intensity profiles only; four or more unconstrained complex phase-retrieval measurements need not obey that linear lower bound. The result has not received independent verification.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first submitted March 24, 2024), https://arxiv.org/abs/2403.16255.
2. M. R. Przybyłek and P. Siedlecki, *A note on the complexity of a phaseless polynomial interpolation*, arXiv:1907.09371 (first submitted July 22, 2019), https://arxiv.org/abs/1907.09371.
