# The two nonordinary strata in the characteristic-seventeen cyclic-eight plane-quintic family

## Finding

Over an algebraically closed field \(k\) of characteristic \(17\), consider the smooth plane quintics
\[
C_r:\quad X^5+Y^4Z+XZ^4+rX^3Z^2=0,\qquad r\in k,\quad r^2\ne4.
\]
Write \(f(C_r)\) for the \(17\)-rank (the \(p\)-rank of its genus-six Jacobian), and \(a(C_r)=\dim_k\operatorname{Hom}(\alpha_{17},\operatorname{Jac}(C_r)[17])\) for its \(a\)-number. Then the **complete** stratification of this family is
\[
\boxed{
(f(C_r),a(C_r))=\begin{cases}
(2,4),&r^2=5,\\
(4,2),&r^2=13,\\
(6,0),&r^2\notin\{4,5,13\}.
\end{cases}}
\]
In particular, the only nonordinary geometric isomorphism classes in this one-parameter family are those with \(r^2=5\) and \(r^2=13\), both with full geometric automorphism group cyclic of order eight. The family contains no superspecial curve in characteristic \(17\). The isomorphism-class assertion uses the established classification of the cyclic-eight quintic locus, not a new classification of all plane quintics.

## Assumptions and scope

All curves and ranks are geometric (over \(k=\overline{\mathbb F}_{17}\)). The characteristic is exactly \(17\); no assertion is made for other characteristics or for rational models over a particular subfield. The parameter restriction excludes precisely the two singular plane quintics. The superspecial classification and the family equation originate in Ohashi, who treats all primes above thirteen; Badr--Bars introduced the automorphism-group model. We calculate the entire ordinary/nonordinary locus and both numerical invariants, which are not inferred merely from non-superspeciality.

Using the change of variables in Ohashi, Section 3.3, write a geometrically isomorphic superelliptic model
\[
D_t:\quad y^4=x(x^2-1)(x^2-t),\qquad t\in k\setminus\{0,1\},
\]
where \(r^2=t+t^{-1}+2\). The same source establishes that two members are geometrically isomorphic precisely when their \(t\)-parameters are related by \(t\mapsto t^{-1}\), equivalently when their \(r^2\)-parameters coincide. The quintic is smooth and has genus six: the map to the \(x\)-line has six fully ramified branch points (five finite, one at infinity), so Riemann--Hurwitz gives \(2g-2=-8+6\cdot3=10\).

## Proof

**Holomorphic differentials.** Let \(F_t(x)=x(x^2-1)(x^2-t)\). At the unique point above infinity, \(v(x)=-4\), \(v(y)=-5\), and \(v(dx)=-5\). The six regular differentials are
\[
\omega_{i,a}=\frac{x^a\,dx}{y^i},\qquad i\in\{1,2,3\},\quad 0\le a<i.
\]
Their distinct pole-order conditions at infinity and the genus count show that they form a basis.

**Exact Cartier coefficients.** Since \(17\equiv1\pmod4\), for each \(i\) put \(N_i=4i\). In characteristic \(17\),
\[
\frac{x^a\,dx}{y^i}=\left(\frac1{y^i}\right)^{17}x^aF_t(x)^{N_i}\,dx.
\]
Writing \(c_i(j)=[x^j]F_t(x)^{4i}\), the matrix \(B_i\) with row \(b\) and column \(a\) given by
\[
(B_i)_{b,a}=c_i\bigl(17(b+1)-1-a\bigr),\quad 0\le a,b<i,
\]
is the entrywise seventeenth power of the corresponding Cartier matrix. Hence it has the same rank and the same zero pattern. Coefficients are computed by the finite binomial identity
\[
[x^{4i+2s}]F_t(x)^{4i}=
\sum_{u+v=s}\binom{4i}{u}\binom{4i}{v}(-1)^{8i-u-v}t^{4i-v},
\]
with \(0\le u,v\le4i\), and all other exponents absent.

Put \(q(t)=t^2-3t+1\) and \(h(t)=(t-2)(t+8)q(t)\), interpreted in \(\mathbb F_{17}[t]\). Exact polynomial arithmetic gives
\[
B_1=(6q(t)),\qquad
B_2=\operatorname{diag}\bigl(2t^4h(t),\ 2h(t)\bigr).
\]
In \(B_3\), only indices of equal parity interact. Its middle diagonal entry and the determinant of the even-indexed \(2\times2\) block are respectively
\[
(B_3)_{1,1}=-2t^2(t-1)^8q(t),\qquad
\det\begin{pmatrix}(B_3)_{0,0}&(B_3)_{0,2}\\(B_3)_{2,0}&(B_3)_{2,2}\end{pmatrix}
=5t^{10}(t-1)^8.
\]
The standalone exact-arithmetic verifier derives these identities from the coefficient formula without a computer-algebra library. They also give the full determinant identity
\[
\det(B_1\oplus B_2\oplus B_3)
=-2t^{16}(t-1)^{16}(t-2)^2(t+8)^2q(t)^4.
\]

**Ranks, including stable ranks.** Because \(t\ne0,1\), the even-indexed block of \(B_3\) is always invertible. The other four pieces are singleton Cartier-invariant summands. On a singleton, the semilinear Cartier map is either zero or bijective; on the even-indexed summand it is bijective. Therefore its rank already equals the stable Cartier rank, which is the Jacobian \(17\)-rank. Its kernel dimension is the \(a\)-number.

When \(t\in\{2,9\}\), the two singleton entries of \(B_2\) vanish, while the other pieces are invertible, giving \((f,a)=(4,2)\). When \(q(t)=0\), all four singleton pieces vanish, leaving only the invertible two-dimensional block, giving \((f,a)=(2,4)\). At all other admitted parameters all six dimensions are bijective, giving \((6,0)\). There are no additional cases since the factorizations list all zero factors.

**Geometric parameters.** In \(\mathbb F_{17}\), \(-8=9=2^{-1}\). The two roots of \(q(t)\) are distinct, nonzero, reciprocal, and not \(1\), since its discriminant \(5\) is nonsquare in \(\mathbb F_{17}\). The transformation \(r^2=t+t^{-1}+2\) therefore sends \(\{2,9\}\) to \(13\), and the two roots of \(q\) to \(5\). Both values are nonzero and distinct from \(4\), so both curves have the exact cyclic-eight automorphism group in the cited classification. The two reciprocal pairs yield precisely two distinct geometric isomorphism classes. This proves the claimed stratification and count.

## Verification

Run `python3 verify.py` with Python 3.9 or later. It prints `CERTIFICATE_OK` if all exact identities and finite-field checks pass; the code has no third-party dependencies. Its input is the coefficient identity above, not a precomputed matrix. The proof of the all-parameter statement additionally uses the displayed invariant-block structure, the binomial identity, and standard Cartier/\(p\)-rank facts. Direct coefficient verification is an exact polynomial identity over \(\mathbb F_{17}[t]\), not a finite sampling argument.

## Relationship to prior work

Ohashi, *Superspecial plane quintics with large automorphism groups*, arXiv:2605.29624 (first posted May 28, 2026), gives this family, its superelliptic form, superspeciality conditions, and isomorphism parameters; the paper focuses on superspeciality and its enumeration rather than a full \(p\)-rank and \(a\)-number stratification in characteristic seventeen. Badr--Bars, *Automorphism groups of non-singular plane curves of degree 5*, arXiv:1510.06190 (2015), classifies the cyclic-eight automorphism locus over characteristic zero; it does not calculate the positive-characteristic Cartier strata. The present result is not a reclassification of automorphisms or a new general Cartier formula: its claim is the exact two-point nonordinary locus and the distinct invariants of its two members.

## Limitations

This is the first admissible characteristic in the motivating treatment, not an all-prime theorem. It does not determine the full Ekedahl--Oort types, Newton polygons, fields of definition of all twists, or \(17\)-torsion group schemes. A specialist historical-priority comparison may uncover implicit coverage by more general Cartier-rank formulas; the asserted novelty is only the explicit full stratification of this natural parameter line. No independent mathematical audit has been performed.

## References

- R. Ohashi, *Superspecial plane quintics with large automorphism groups*, arXiv:2605.29624v1, May 28, 2026, especially Section 2 and Section 3.3, equations (3.7)--(3.8), Lemma 3.8, Proposition 3.10, and Theorem 3.12.
- E. Badr and F. Bars, *Automorphism groups of non-singular plane curves of degree 5*, arXiv:1510.06190, October 21, 2015, especially the cyclic-eight case in Section 3.
