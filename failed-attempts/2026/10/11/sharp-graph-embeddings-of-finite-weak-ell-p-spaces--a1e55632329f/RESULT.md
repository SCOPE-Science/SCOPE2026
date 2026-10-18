# Sharp graph embeddings of finite weak \(\ell_p\) spaces
## Finding

Let \(\mathbb F\in\{\mathbb R,\mathbb C\}\), let \(p>0\), and let \(m\ge1\). For \(x=(x_1,\ldots,x_m)\in\mathbb F^m\), write
\[
x_1^*\ge x_2^*\ge\cdots\ge x_m^*\ge0
\]
for the decreasing rearrangement of \((|x_1|,\ldots,|x_m|)\), and equip \(\mathbb F^m\) with
\[
\|x\|_{p,\infty}^{(m)}=\max_{1\le j\le m}j^{1/p}x_j^*.
\]

For \(a=(a_1,\ldots,a_m)\in\mathbb F^m\), define
\[
L_a(x)=\sum_{i=1}^m a_i x_i,
\qquad
T_a(x)=\bigl(x_1,\ldots,x_m,L_a(x)\bigr).
\]
If \(a_1^*\ge\cdots\ge a_m^*\) is the decreasing rearrangement of \((|a_1|,\ldots,|a_m|)\), then
\[
T_a:\ell_{p,\infty}^m\longrightarrow\ell_{p,\infty}^{m+1}
\]
is a linear isometry if and only if
\[
\boxed{\sum_{j=1}^m a_j^*j^{-1/p}\le(m+1)^{-1/p}.}
\]

Every \(T_a\) is a codimension-one graph embedding and hence is non-surjective. For \(m\ge2\), an isometric \(T_a\) preserves coordinate disjointness if and only if \(a\) has at most one nonzero coordinate.

For the equal-coefficient slice \(a_1=\cdots=a_m=c\), the condition becomes
\[
|c|\le\frac{(m+1)^{-1/p}}{\sum_{j=1}^m j^{-1/p}}.
\]
At \(m=2\), the boundary value is
\[
c=\frac{3^{-1/p}}{1+2^{-1/p}},
\]
exactly the coefficient in Remark 1.1 of Fang--Gao--Huang--Sukochev.

## Assumptions and scope

The scalar field may be real or complex, and \(p\) may be any positive real number; no triangle inequality is used. The quasi-norm is the natural rearrangement quasi-norm for finite weak sequence spaces.

The classification concerns the codimension-one graph family in which the first \(m\) coordinates are left unchanged and one additional coordinate is a linear functional. It is not a classification of all linear isometric embeddings between finite weak-\(\ell_p\) spaces, nor does it address noncommutative weak-\(L_p\) spaces or weak-\(\ell_p\) operator ideals.

Coordinate disjointness means disjoint supports in the standard basis.

## Proof

Let
\[
B_{p,m}=\{x:\|x\|_{p,\infty}^{(m)}\le1\}.
\]
For every \(x\in B_{p,m}\),
\[
x_j^*\le j^{-1/p}
\qquad(1\le j\le m).
\]
By the finite rearrangement inequality,
\[
|L_a(x)|
\le
\sum_{j=1}^m a_j^*x_j^*
\le
\sum_{j=1}^m a_j^*j^{-1/p}.
\]
Equality is attained by ordering coordinates according to decreasing \(|a_i|\), assigning corresponding coordinate moduli \(1,2^{-1/p},\ldots,m^{-1/p}\), and choosing signs or phases so that all summands in \(L_a(x)\) have one argument. Hence
\[
\sup_{x\in B_{p,m}}|L_a(x)|
=
\sum_{j=1}^m a_j^*j^{-1/p}.
\tag{1}
\]

Assume first that
\[
\sum_{j=1}^m a_j^*j^{-1/p}\le(m+1)^{-1/p}.
\tag{2}
\]
Take \(x\in B_{p,m}\) and put \(z=L_a(x)\). By (1) and (2),
\[
|z|\le(m+1)^{-1/p}.
\]
Let \(y=(x,z)\). For \(1\le j\le m\),
\[
y_j^*\le\max\{x_j^*,|z|\}\le j^{-1/p},
\]
and also
\[
y_{m+1}^*\le|z|\le(m+1)^{-1/p}.
\]
Therefore
\[
\|T_a x\|_{p,\infty}^{(m+1)}\le1.
\]
Adjoining a coordinate cannot decrease any of the first \(m\) order statistics, so
\[
\|T_a x\|_{p,\infty}^{(m+1)}\ge\|x\|_{p,\infty}^{(m)}.
\]
Homogeneity gives equality for every \(x\).

Conversely, assume \(T_a\) is an isometry. Choose the equality vector from (1), so that
\[
\|x\|_{p,\infty}^{(m)}=1,
\qquad
|L_a(x)|=\sum_{j=1}^m a_j^*j^{-1/p},
\]
and the original coordinate moduli are precisely
\[
1,2^{-1/p},\ldots,m^{-1/p}.
\]
Each is strictly larger than \((m+1)^{-1/p}\). If
\[
|L_a(x)|>(m+1)^{-1/p},
\]
then all \(m+1\) coordinate moduli of \(T_a x\) are strictly larger than \((m+1)^{-1/p}\), so
\[
(m+1)^{1/p}(T_a x)_{m+1}^*>1,
\]
contradicting isometry. Thus (2) is necessary.

Finally, \(T_a(\mathbb F^m)\) is an \(m\)-dimensional graph in \(\mathbb F^{m+1}\), hence is never surjective. If two coefficients \(a_i,a_j\) are nonzero, then the disjoint basis vectors \(e_i,e_j\) have images sharing the nonzero last coordinate, so disjointness fails. If \(a\) has at most one nonzero coordinate, two disjoint vectors cannot both give a nonzero value under \(L_a\); their images therefore remain disjoint.

## Verification

The proof uses finite rearrangement and order-statistic arguments only. The critical support-function identity (1) was reconstructed explicitly, including its equality case over both scalar fields. The necessity step uses an equality vector whose every original coordinate lies strictly above the added-coordinate threshold.

As a supplementary stress check, random coefficient vectors were scaled to the boundary in dimensions \(1,2,3,5,8\) and for \(p\in\{0.3,0.8,1,1.5,2,5\}\); random vectors preserved the quasi-norm to numerical tolerance. This finite check is not used as proof.

## Relationship to prior work

Fang, Gao, Huang, and Sukochev study extreme points and isometries of noncommutative quasi-Banach Marcinkiewicz spaces. Their introduction restricts the main weak-\(L_p\) isometry analysis to surjective isometries because disjointness can fail without surjectivity. Remark 1.1 gives the concrete map from two-dimensional weak \(\ell_p\) into three-dimensional weak \(\ell_p\)
\[
e_1\mapsto f_1+\frac{3^{-1/p}}{1+2^{-1/p}}f_3,
\qquad
e_2\mapsto f_2+\frac{3^{-1/p}}{1+2^{-1/p}}f_3,
\]
and states that it is a non-surjective, non-disjointness-preserving isometry.

The present result identifies that coefficient as an extremal boundary point of a complete coefficient-body criterion for every dimension and every added functional. Earlier work of Arazy and of Aminov--Chilin concerns surjective isometries of symmetric sequence spaces; those results do not imply this non-surjective graph classification.

Targeted searches for weak-\(\ell_p\) graph embeddings, identity-plus-functional embeddings, coefficient-vector criteria, codimension-one embeddings, and the exact coefficient from Remark 1.1 did not locate an equivalent statement.

## Limitations

No claim is made about arbitrary isometric embeddings \(\ell_{p,\infty}^m\to\ell_{p,\infty}^n\) when \(n>m\), about nonlinear isometries, or about analogous graph embeddings in noncommutative weak-\(L_p\) spaces. The coefficient condition is exact only for the graph family whose first \(m\) coordinates are the identity.

The closest older isometry literature located in the search is formulated for surjective isometries. An older equivalent codimension-one observation could exist under different finite-dimensional Lorentz or Marcinkiewicz terminology.

## References

1. K. Fang, Y. Gao, J. Huang, F. Sukochev, *Extreme points of the unit ball and isometries of noncommutative quasi-Banach Marcinkiewicz spaces*, arXiv:2610.01043v1, 1 October 2026.
2. B. R. Aminov, V. I. Chilin, *Isometries and Hermitian operators on complex symmetric sequence spaces*, Siberian Advances in Mathematics 27 (2017), 239--252, DOI 10.3103/S1055134417040022.
3. J. Arazy, *Isometries of complex symmetric sequence spaces*, Mathematische Zeitschrift 188 (1985), 427--431, DOI 10.1007/BF01159187.
