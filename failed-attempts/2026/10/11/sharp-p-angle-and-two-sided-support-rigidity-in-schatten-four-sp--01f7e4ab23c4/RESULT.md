# Sharp P-angle and two-sided support rigidity in Schatten-four spaces
## Finding
Let \(H\) be a real or complex Hilbert space with
\[
\dim H\ge2,
\]
and let \(\mathcal S_4(H)\) be its Schatten-four class, regarded as a real Banach space. Thus
\[
\|T\|_4=(\operatorname{Tr}|T|^4)^{1/4}.
\]
The Yang--Li P-angle constant is
\[
S_P(X)=\sup_{\substack{A,B\in S_X\\A\ne\pm B}}
\frac{\|A+B\|^2+\|A-B\|^2-4}
{2\|A+B\|\|A-B\|}.
\tag{1}
\]
Then
\[
\boxed{S_P(\mathcal S_4(H))=1-\frac1{\sqrt2}}.
\tag{2}
\]

The theorem has a stronger rigidity statement and a nonnegative operator-valued *defect identity*. For two unit operators \(A,B\) with \(A\ne\pm B\), write
\[
U=A+B,\quad V=A-B,\quad a=\|U\|_4,\quad b=\|V\|_4,
\quad s=\sqrt{a^4+b^4},\quad k=2-\sqrt2,
\]
and
\[
K=U^*V+V^*U.
\]
Then
\[
\boxed{
4-a^2-b^2+kab
=
\frac{2\|UV^*\|_2^2+\|K\|_2^2}{4+s}
+
\frac{2kab(a-b)^2}{s+a^2+b^2-kab}.
}
\tag{3}
\]
Every term on the right is nonnegative. In particular the sharp bound in (2) is attained precisely by the pairs
\[
\boxed{
A=2^{-1/4}(P+Q),\qquad B=2^{-1/4}(P-Q),
}
\tag{4}
\]
where
\[
\|P\|_4=\|Q\|_4=1,
\qquad PQ^*=P^*Q=0.
\tag{5}
\]
The last relations say that \(P,Q\) have *both left and right disjoint supports*.

## Assumptions and scope
The norm and the adjoint use the scalar field of \(H\), which may be real or complex. The P-angle uses the underlying real normed-space structure and requires no complex-angle convention.

The Hilbert--Schmidt norm is
\[
\|T\|_2^2=\operatorname{Tr}(T^*T).
\]
Whenever \(U,V\in\mathcal S_4(H)\), their products \(UV^*\) and \(U^*V+V^*U\) belong to \(\mathcal S_2(H)\). Thus all quantities in (3) are finite. The excluded cases \(A=\pm B\) have a vanishing P-angle denominator; for admissible pairs \(a,b>0\).

The statement holds for every Hilbert-space dimension at least two, including infinite dimension. The one-dimensional case is excluded because two nonzero mutually two-sided-disjoint operators cannot exist there.

## Proof
**Step 1: Exact quartic trace polarization.** For arbitrary \(U,V\in\mathcal S_4(H)\), put
\[
M=U^*U+V^*V,\qquad K=U^*V+V^*U.
\]
Both are self-adjoint Hilbert--Schmidt operators and
\[
(U\pm V)^*(U\pm V)=M\pm K.
\]
Expanding the two fourth powers, using cyclicity of the trace, gives
\[
\begin{aligned}
\|U+V\|_4^4+\|U-V\|_4^4
&=\operatorname{Tr}[(M+K)^2+(M-K)^2]\\
&=2\operatorname{Tr}(M^2+K^2)\\
&=2(\|U\|_4^4+\|V\|_4^4)
+4\|UV^*\|_2^2+2\|K\|_2^2.
\end{aligned}
\tag{6}
\]
In particular, since \(U+V=2A\), \(U-V=2B\), and \(\|A\|_4=\|B\|_4=1\),
\[
32=2(a^4+b^4)+4\|UV^*\|_2^2+2\|K\|_2^2.
\]
Consequently,
\[
16-s^2=2\|UV^*\|_2^2+\|K\|_2^2
\quad\text{and}\quad s\le4.
\tag{7}
\]

**Step 2: Sharp scalar factorization.** The number
\[
k=2-\sqrt2
\]
satisfies
\[
k^2-4k+2=0.
\]
For every \(a,b\ge0\), direct expansion therefore yields
\[
(a^4+b^4)-(a^2+b^2-kab)^2
=2kab(a-b)^2.
\tag{8}
\]
Since
\[
a^2+b^2-kab=(a-b)^2+\sqrt2\,ab\ge0,
\]
we may divide (8) by the positive sum of square roots, obtaining
\[
s-(a^2+b^2-kab)
=\frac{2kab(a-b)^2}{s+a^2+b^2-kab}.
\tag{9}
\]
By (7),
\[
4-s=
\frac{2\|UV^*\|_2^2+\|K\|_2^2}{4+s}.
\tag{10}
\]
Adding (9) and (10) proves the exact decomposition (3), including nonnegativity.

**Step 3: P-angle upper bound.** By (3),
\[
a^2+b^2-4\le kab.
\]
As \(a,b>0\), division by \(2ab\) gives
\[
\frac{a^2+b^2-4}{2ab}\le\frac{k}{2}
=1-\frac1{\sqrt2}.
\tag{11}
\]
Taking the supremum in (1) establishes the upper bound in (2).

**Step 4: Exact equality and two-sided support disjointness.** Since \(a,b>0\), equality in (11) forces \(a=b\) by the second summand in (3), and forces
\[
UV^*=0,\qquad U^*V+V^*U=0
\tag{12}
\]
by the first summand. The relation \(UV^*=0\) says that the right support subspaces of \(U,V\), namely the closures of the ranges of \(U^*,V^*\), are orthogonal. Let \(P_U,P_V\) be the orthogonal projections onto these subspaces. Then
\[
P_UP_V=0,
\quad
U^*V=P_U(U^*V)P_V,
\quad
V^*U=P_V(V^*U)P_U.
\]
Multiplying the second relation in (12) on the left by \(P_U\) and on the right by \(P_V\) gives
\[
U^*V=0.
\]
Thus \(U,V\) have both left and right disjoint supports. Equation (7) now implies \(s=4\); together with \(a=b\), this gives
\[
a=b=8^{1/4}=2^{3/4}.
\]
Setting
\[
P=2^{-3/4}U,
\qquad Q=2^{-3/4}V
\]
gives (4)--(5).

Conversely, if \(P,Q\) obey (5), their sum and difference satisfy
\[
\|P\pm Q\|_4^4=\|P\|_4^4+\|Q\|_4^4=2.
\]
The operators in (4) are therefore unit. Their sum and difference are respectively
\[
A+B=2^{3/4}P,
\qquad A-B=2^{3/4}Q,
\]
so \(a=b=2^{3/4}\) and (11) is an equality. Such \(P,Q\) exist when \(\dim H\ge2\): take orthogonal rank-one projections. This establishes (2) and the entire equality classification.

**Quantitative consequence.** Define
\[
D=2ab\left(1-\frac1{\sqrt2}-\cos\operatorname{ang}_P(A+B,A-B)\right).
\]
Then (3) proves
\[
\|UV^*\|_2^2\le4D,
\qquad
\|U^*V+V^*U\|_2^2\le8D,
\]
and, since both denominators are positive and bounded, it also controls the chord imbalance \(a-b\). This supplies an exact stability certificate for proximity to the maximizing geometry.

## Verification
The standalone checker `verify.py` contains an exact symbolic expansion of the scalar identity (8) and exact rational-matrix trace tests of (6) in sizes two through four. It checks the scalar coefficients, the normalized diagonal equality pair, and supplementary noncommuting examples of (3). The general proof is the trace expansion and the scalar factorization above, not finite enumeration.

## Relationship to prior work
Yang and Li introduced the P-angle constant in 2022 and obtained general estimates and examples on sequence spaces. Their full text does not address Schatten ideals or classify noncommuting maximizing pairs.

Classical Clarkson--McCarthy inequalities imply the nonnegative operator contribution in (6); the 2019 work of Bottazzi and coauthors examines related equality/disjoint-support conditions in Schatten ideals. Alrimawi, Hirzallah and Kittaneh give refined Clarkson inequalities for matrix norms. Their full texts do not state the P-angle value (2), the joint operator-and-scalar decomposition (3), or the maximizing-pair parametrization (4)--(5).

The exact P-angle constant previously determined for \(\ell_4\) has the same numerical value because diagonal Schatten-four operators form an isometric copy of \(\ell_4\). That scalar-space result gives only a lower bound on the noncommutative Schatten-four constant; it does not control arbitrary noncommuting operators or imply the nonnegative support-overlap identity.

## Limitations
The sharp defect identity and equality classification here use the fourth power. No formula is asserted here for general Schatten exponents other than four. The equality classification requires only \(\dim H\ge2\), but it does not classify near-maximizers in operator norm; the displayed stability bounds measure Hilbert--Schmidt support overlap and chord imbalance.

An exact equivalent P-angle formula might be implicit in earlier general operator inequalities under a different name. Searches of the defining P-angle and relevant Schatten full texts revealed no covering statement, but no literature search establishes absolute novelty.

## References
1. Zhijian Yang and Yongjin Li, "New Geometric Constant Related to the P-angle Function in Banach Spaces," arXiv:2208.11239v1, first publicly posted 24 August 2022. Mathematics Subject Classification 46B20.
2. T. Bottazzi, C. Conde, M. S. Moslehian, P. Wójcik and A. Zamani, "Orthogonality and parallelism of operators on various Banach spaces," *Journal of the Australian Mathematical Society* 106 (2019), 160--183, doi:10.1017/S1446788718000150.
3. F. Alrimawi, O. Hirzallah and F. Kittaneh, "Norm Inequalities Related to Clarkson Inequalities," *Electronic Journal of Linear Algebra* 34 (2018), 163--169, doi:10.13001/1081-3810.3642.
