\
# Every proper Euler-characteristic subgroup obstructs object cotorsion completeness

## Status and provenance

The mathematical theorem in this record is correct, but its original originality framing requires correction.

Repository history shows that the broader SCOPE record

`2026/09/19/euler-subgroup-cotorsion-obstruction--9b38fc18ec20`

was committed at 2026-09-19 14:38:25 UTC in commit
`81c308dba558c2b01e559071d8b93a2dc2c4e76e` and already states the same
Euler-subgroup theorem, the same truncated-Euler criteria, the same sharp boundary
for object completeness, and the same idempotent-completion conclusion. The present
record first appears in the later commit sequence beginning at 2026-09-19 15:01:20 UTC
(commit `a3ae9bd05f06929391752cb5ca88b6c423e39f30`).

Accordingly, this record is retained as an alternate proof and corroborating
presentation. Its useful distinguishing feature is the uniform correction-stalk
argument below, which handles all subgroups \(B\le\mathbb Z\), including \(B=\{0\}\),
without separating finite-index and zero cases. No separate discovery-priority claim
is made relative to the earlier SCOPE record.

## Theorem

Let
\[
\mathcal D=\operatorname{Ch}^{b}(\operatorname{vect}_k)
\]
with the degreewise split exact structure, and write
\[
\chi(X)=\sum_n(-1)^n\dim_k H^n(X).
\]
For an additive subgroup \(B\le\mathbb Z\), put
\[
\mathcal A_B=\{X\in\mathcal D:\chi(X)\in B\}.
\]
Inside \(\mathcal A_B\), let
\[
\mathcal F_B=\{X:H^n(X)=0\text{ for }n\ge1\},\qquad
\mathcal C_B=\{X:H^n(X)=0\text{ for }n\le1\},
\]
and
\[
\mathcal I_B=\{f:H^n(f)=0\text{ for }n\ge1\},\qquad
\mathcal J_B=\{g:H^n(g)=0\text{ for }n\le1\}.
\]

Then:

1. \(\mathcal A_B\) is an essentially small, Hom-finite, weakly idempotent complete
   Frobenius exact category. Its projective-injective objects are the contractible
   complexes.
2. \(\mathcal I_B=\langle\mathcal F_B\rangle\) and
   \(\mathcal J_B=\langle\mathcal C_B\rangle\), and
   \[
   {}^\perp\mathcal J_B=\mathcal I_B,\qquad
   \mathcal I_B^\perp=\mathcal J_B.
   \]
   The ideal cotorsion pair \((\mathcal I_B,\mathcal J_B)\) is complete.
3. For \(A\in\mathcal A_B\), a special object sequence
   \[
   0\to C\to F\to A\to0,\qquad C\in\mathcal C_B,\ F\in\mathcal F_B,
   \]
   exists exactly when
   \[
   \chi(H^{\le0}(A))\in B.
   \]
   Dually, a sequence
   \[
   0\to A\to C\to F\to0,\qquad C\in\mathcal C_B,\ F\in\mathcal F_B,
   \]
   exists exactly when
   \[
   \chi(H^{\ge2}(A))\in B.
   \]
4. Hence the associated object cotorsion pair
   \((\mathcal F_B,\mathcal C_B)\) is complete if and only if \(B=\mathbb Z\).
   Every proper \(B<\mathbb Z\) fails both special precovering and special
   preenveloping.
5. If \(B<\mathbb Z\), then \(\mathcal A_B\) is not idempotent complete and its
   idempotent completion is all of \(\mathcal D\).

The Ren--Wang parity example is exactly the specialization \(B=2\mathbb Z\), because
total cohomology dimension and Euler characteristic agree modulo two.

## Uniform correction stalks

For \(r\in\mathbb Z\), define zero-differential complexes
\[
R_-(r)=
\begin{cases}
S^0(k^r),&r\ge0,\\
S^{-1}(k^{-r}),&r<0,
\end{cases}
\qquad
R_+(r)=
\begin{cases}
S^2(k^r),&r\ge0,\\
S^3(k^{-r}),&r<0.
\end{cases}
\]
Then
\[
\chi(R_-(r))=\chi(R_+(r))=r,
\]
with \(R_-(r)\) supported in degrees \(\le0\) and \(R_+(r)\) supported in degrees
\(\ge2\). These objects are the only extra device needed to treat every subgroup
uniformly.

## Proof

Euler characteristic is additive on degreewise split conflations, so \(\mathcal A_B\)
is extension closed. If a split monomorphism \(X\to Y\) has ambient complement \(Z\),
then \(\chi(Z)=\chi(Y)-\chi(X)\in B\); hence \(\mathcal A_B\) is weakly idempotent
complete. Contractible complexes have Euler characteristic zero, and the standard
contractible cone sequences for each \(X\) stay in \(\mathcal A_B\). They give enough
projectives and injectives, and the usual retract argument shows that the
projective-injective objects are precisely the contractibles.

Every bounded complex over a field splits as its cohomology plus a contractible
summand. If \(f\in\mathcal I_B\), write the source as
\[
X\cong H^{\le0}(X)\oplus H^{\ge1}(X)\oplus Q.
\]
The high-cohomology part of \(f\) is zero on cohomology and differs from zero by a
null-homotopic map, hence factors through a contractible object. The remaining map
factors through
\[
H^{\le0}(X)\oplus
R_-(-\chi(H^{\le0}(X))),
\]
whose Euler characteristic is zero and whose cohomology lies in degrees \(\le0\).
Thus \(\mathcal I_B=\langle\mathcal F_B\rangle\). The dual argument with \(R_+\)
gives \(\mathcal J_B=\langle\mathcal C_B\rangle\).

For \(X,Y\in\mathcal A_B\), the degreewise split extension calculation is
\[
\operatorname{Ext}^1_{\mathcal A_B}(X,Y)
\cong\bigoplus_n\operatorname{Hom}_k(H^n(X),H^{n+1}(Y)).
\]
This immediately gives
\(\operatorname{Ext}^1(\mathcal I_B,\mathcal J_B)=0\).
If \(f\notin\mathcal I_B\), some \(H^n(f)\ne0\) for \(n\ge1\); the zero-Euler test
object \(S^{n+1}(k)\oplus S^{n+2}(k)\in\mathcal C_B\) detects a nonzero extension
map. Dually, \(S^{m-1}(k)\oplus S^{m-2}(k)\in\mathcal F_B\) detects every
\(g\notin\mathcal J_B\). Hence
\[
{}^\perp\mathcal J_B=\mathcal I_B,\qquad
\mathcal I_B^\perp=\mathcal J_B.
\]

For ideal completeness, write
\[
A\cong L\oplus U\oplus Q,\qquad
L=H^{\le0}(A),\quad U=H^{\ge1}(A),
\]
with \(Q\) contractible. If \(P(U)\to U\) is a standard contractible deflation, set
\[
E_A=L\oplus P(U)\oplus R_+(\chi(U))\oplus Q.
\]
The evident map \(E_A\to A\), zero on the correction stalk, has kernel
\[
U[-1]\oplus R_+(\chi(U)),
\]
which has Euler characteristic zero and lies in \(\mathcal C_B\); the map itself
lies in \(\mathcal I_B\). This is a special ideal precover. The dual construction,
using \(V=H^{\le1}(A)\) and \(R_-(\chi(V))\), gives a special ideal preenvelope.

For object approximations, if
\[
0\to C\to F\to A\to0
\]
has \(C\in\mathcal C_B\) and \(F\in\mathcal F_B\), the long exact cohomology sequence
identifies \(H(F)\) with \(H^{\le0}(A)\), so
\(\chi(H^{\le0}(A))=\chi(F)\in B\). Conversely, when that truncated Euler
characteristic lies in \(B\), the ordinary undistorted cone sequence for
\(H^{\ge1}(A)\) lies entirely in \(\mathcal A_B\) and supplies the required object
precover. The preenvelope criterion is dual.

If \(B<\mathbb Z\), then \(1\notin B\). Both
\[
S^0(k)\oplus S^1(k),\qquad S^1(k)\oplus S^2(k)
\]
have Euler characteristic zero, but their relevant truncated Euler characteristics
are one, so they obstruct the two object approximation directions. If \(B=\mathbb Z\),
the criteria are automatic.

Finally, for proper \(B\), projection
\[
S^0(k)\oplus S^1(k)\to S^0(k)
\]
is an idempotent in \(\mathcal A_B\) whose image is not an object of \(\mathcal A_B\),
so the category is not idempotent complete. Every \(X\in\mathcal D\), however, is a
summand of \(X\oplus R\) for a zero-differential \(R\) chosen so that
\(\chi(X\oplus R)=0\). Hence the Karoubi envelope is all of \(\mathcal D\).

## Literature context and corrected originality scope

Ren and Wang, arXiv:2609.18681, give the parity case \(B=2\mathbb Z\). Wang, Wang
and Zhu, arXiv:2609.14382, give a different counterexample that is not weakly
idempotent complete. General ideal-approximation theory is due to Fu, Guil Asensio,
Herzog and Torrecillas and others.

Within SCOPE, the complete subgroup theorem appeared first in
`euler-subgroup-cotorsion-obstruction--9b38fc18ec20`. The present record therefore
does not claim independent discovery of the subgroup theorem. Its retained
scientific contribution is the uniform correction-stalk proof and an independent
same-day corroboration of the earlier record.

## Limitations

The construction is specific to bounded complexes of finite-dimensional vector
spaces with the degreewise split exact structure. It does not classify completeness
descent in arbitrary exact categories. Equivalent abstraction in older
\(K_0\)-theoretic language remains possible.

## References

1. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion
   pairs*, arXiv:2609.18681 (2026).
2. Q. Wang, Y. Wang and H. Zhu, *A Counterexample to the Open Question on Object
   Ideals*, arXiv:2609.14382 (2026).
3. X. H. Fu, P. A. Guil Asensio, I. Herzog and B. Torrecillas,
   *Ideal approximation theory*, Advances in Mathematics 244 (2013), 750–790.
4. SCOPE record
   `2026/09/19/euler-subgroup-cotorsion-obstruction--9b38fc18ec20`,
   first committed 2026-09-19 14:38:25 UTC.
