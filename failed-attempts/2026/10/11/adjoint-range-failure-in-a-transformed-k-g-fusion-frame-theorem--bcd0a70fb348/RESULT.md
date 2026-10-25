# Adjoint-range failure in a transformed \(K\)-\(g\)-fusion frame theorem

## Finding
Theorem 4 of Ahmadi--Rahimlou--Sadri--Zarghami Farfar asserts that, when \(K\) has closed range and
\[
R(U)\subseteq R(K),
\]
a transformed \(K\)-\(g\)-fusion family is a \(K\)-\(g\)-fusion frame exactly when
\[
\|U^*f\|\ge\delta\|K^*f\|
\]
for some \(\delta>0\) and all \(f\).

This is false.

Let
\[
H=\mathbb C^2,
\qquad
K=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]
Take one \(g\)-fusion component
\[
W_1=H,\qquad v_1=1,\qquad \Lambda_1=K.
\]
The original family is Parseval relative to \(K\), because
\[
\|\Lambda_1f\|^2=\|K^*f\|^2
\]
for every \(f\in H\).

Moreover,
\[
R(U)=\operatorname{span}\{e_1\}=R(K),
\]
so the range hypothesis in the theorem holds. Since
\[
U^*=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\]
one has
\[
\|U^*f\|=\|K^*f\|
\]
for all \(f\). Thus the claimed lower comparison holds with the best possible value \(\delta=1\).

But
\[
KU^*=0.
\]
The transformed subspace is
\[
UW_1=R(U)=\operatorname{span}\{e_1\},
\]
and the transformed coefficient operator vanishes on it. Hence the transformed family has zero coefficient energy for every vector. At \(f=e_1\),
\[
\|K^*e_1\|^2=1,
\]
so no positive lower \(K\)-\(g\)-fusion bound exists.

## Assumptions and scope
The counterexample is finite-dimensional and uses a single component. All ranges are closed, every projection is explicit, and there are no convergence or measurability issues.

The example satisfies the theorem's printed hypotheses exactly:
\[
K
\]
has closed range,
\[
R(U)\subseteq R(K),
\]
the original family is a \(K\)-\(g\)-fusion frame, and the displayed \(\delta\)-condition holds.

The exact corrected characterization below is stated for the transformed family associated with an original \(K\)-\(g\)-fusion frame with frame operator \(S_\Lambda\).

## Proof
For the original family,
\[
W_1=H
\]
so \(\pi_{W_1}=I\). Therefore
\[
\|\Lambda_1\pi_{W_1}f\|^2
=
\|Kf\|^2
=
\|K^*f\|^2,
\]
because \(K=K^*\) is an orthogonal projection. Thus the frame is Parseval relative to \(K\).

For the operator \(U\),
\[
Uf=(f_2,0),
\qquad
U^*f=(0,f_1).
\]
Consequently
\[
R(U)=\operatorname{span}\{e_1\}
\]
and
\[
\|U^*f\|=|f_1|=\|K^*f\|.
\]

On the other hand,
\[
KU^*
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}
=0.
\]
Thus every coefficient of the transformed one-component family is zero.

The proof in the source uses
\[
U^*f=(K^\dagger)^*K^*U^*f.
\]
For a closed-range operator,
\[
(K^\dagger)^*K^*
\]
is the orthogonal projection onto \(R(K)\). Hence this equality is valid for every \(f\) precisely when
\[
R(U^*)\subseteq R(K).
\]
The source assumes only
\[
R(U)\subseteq R(K).
\]
In the example,
\[
U^*e_1=e_2\notin R(K),
\]
so the proof identity fails maximally:
\[
(K^\dagger)^*K^*U^*e_1=0
\]
while
\[
U^*e_1=e_2.
\]

For the exact operator criterion, let \(S_\Lambda\) be the original frame operator. The standard projection identity for the transformed subspaces gives
\[
\sum_j v_j^2
\|\Lambda_j\pi_{W_j}U^*\pi_{UW_j}f\|^2
=
\sum_j v_j^2
\|\Lambda_j\pi_{W_j}U^*f\|^2
=
\langle S_\Lambda U^*f,U^*f\rangle.
\]
Therefore
\[
S_\Gamma=US_\Lambda U^*.
\]
The transformed family is a \(K\)-\(g\)-fusion frame exactly when
\[
US_\Lambda U^*\ge c\,KK^*
\]
for some \(c>0\). By Douglas' factorization theorem this is equivalent to
\[
R(K)\subseteq R(US_\Lambda^{1/2}).
\]

## Verification
The published article was inspected at the complete statement and proof of Theorem 4. The sufficiency proof explicitly inserts the Moore--Penrose factor
\[
(K^\dagger)^*K^*
\]
in front of \(U^*f\) using only the stated hypothesis \(R(U)\subseteq R(K)\).

The earlier related 2018 preprint was also inspected. It does not contain this published iff theorem; its nearby construction theorem has a different statement. Thus the verified first public date for the present theorem is the 2020 publication date.

A later 2021 paper on \(K\)-\(g\)-fusion weaving uses the adjoint-range condition
\[
R(U^*)\subseteq R(K)
\]
in the corresponding transformation argument. That hypothesis is exactly what makes the disputed Moore--Penrose projection identity valid.

All calculations in the counterexample are exact \(2\times2\) matrix identities.

## Relationship to prior work
The closest published operator-range observations for \(K\)-frames concern compression of frame operators to \(R(K)\) or other range-sensitive reconstruction questions. They do not imply this transformed-family counterexample.

The later woven \(K\)-\(g\)-fusion result adopts the corrected adjoint-range geometry, but it does not state that the 2020 theorem is false and does not give the counterexample above.

The exact criterion
\[
US_\Lambda U^*\ge c\,KK^*
\]
is the direct operator form of the transformed lower frame inequality. Douglas' theorem converts it into the range inclusion
\[
R(K)\subseteq R(US_\Lambda^{1/2}).
\]

## Limitations
The finding corrects Theorem 4 only. It does not reassess the paper's other constructions or duality results.

The replacement
\[
R(U^*)\subseteq R(K)
\]
is a clean sufficient repair for the published proof. The exact necessary-and-sufficient condition is the operator domination above and can hold in special cases without that range inclusion.

A nonindexed erratum or informal correction may contain the same observation.

## References
1. R. Ahmadi, G. Rahimlou, V. Sadri and R. Zarghami Farfar, *Constructions of \(K\)-\(g\)-fusion and their dual in Hilbert spaces*, Bulletin of the Transilvania University of Brașov, Series III, Mathematics, Informatics, Physics 13(62)(1) (2020), 17--32, DOI 10.31926/but.mif.2020.12.61.1.2.
2. V. Sadri, G. Rahimlou and R. Ahmadi, *\(K\)-\(g\)-fusion woven in Hilbert spaces*, TWMS Journal of Applied and Engineering Mathematics 11(3) (2021), 947--958.
3. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.
