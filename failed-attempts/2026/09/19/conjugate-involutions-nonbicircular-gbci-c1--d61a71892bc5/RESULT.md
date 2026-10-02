# Conjugate involutions generate non-bicircular generalized bi-circular idempotents

## Statement

Let
\[
X=C^1[0,1],\qquad \|f\|_\sigma=|f(0)|+\|f'\|_\infty .
\]
For distinct \(\lambda_1,\lambda_2\in\mathbb T\), let \(T:X\to X\) be a
conjugate-linear surjective isometry satisfying \(T^2=I\). Define
\[
P_1=\frac{T-\lambda_2 I}{\lambda_1-\lambda_2},
\qquad
P_2=\frac{\lambda_1 I-T}{\lambda_1-\lambda_2}.
\]
Then \(P_1,P_2\) are distinct nonzero real-linear idempotents with
\[
P_1P_2=P_2P_1=0,\qquad P_1+P_2=I,
\qquad \lambda_1P_1+\lambda_2P_2=T.
\]
Thus every conjugate-linear isometric involution produces a family of generalized
bi-circular idempotents for **every** distinct phase pair, including non-antipodal
pairs \(\lambda_1+\lambda_2\ne0\).

For the Form IV isometries in Kumar--Kumar--Abu Baker,
\[
(Tf)(t)=c\,\overline{f(0)}
 +\int_0^t\beta(s)\,\overline{f'(\phi(s))}\,ds,
\tag{1}
\]
with \(|c|=|\beta|=1\) and \(\phi\) a homeomorphism of \([0,1]\), this gives the
exact criterion
\[
\{P_1,P_2\}\text{ is a GBCI associated with }T
\iff
T^2=I
\iff
\begin{cases}
\phi^2=\mathrm{id},\\
\beta(t)\overline{\beta(\phi(t))}=1\quad(t\in[0,1]).
\end{cases}
\tag{2}
\]
No family obtained from a Form IV conjugate-linear isometry in this way is
bi-circular.

Consequently, the headline dichotomy in arXiv:2609.18967v1 -- that a GBCI on
this \(C^1[0,1]\) either has \(\lambda_1+\lambda_2=0\) or is bi-circular -- is
false.  The same semilinear obstruction also invalidates the bi-circular
conclusions in the paper's Form II and Form III cases.

## An explicit counterexample

Take the pointwise conjugation
\[
Tf=\overline f,
\]
which is a conjugate-linear surjective isometry of \(X\) and satisfies \(T^2=I\).
Choose
\[
\lambda_1=1,\qquad \lambda_2=i.
\]
Then
\[
P_1f=\frac{\overline f-if}{1-i},
\qquad
P_2f=\frac{f-\overline f}{1-i}.
\tag{3}
\]
Writing \(f=u+iv\) with real-valued \(u,v\),
\[
P_1f=u+v,\qquad P_2f=(i-1)v.
\tag{4}
\]
Hence \(P_1^2=P_1\), \(P_2^2=P_2\), \(P_1P_2=P_2P_1=0\), and
\(P_1+P_2=I\), while
\[
P_1+iP_2=T
\]
is a surjective isometry.  Moreover \(1+i\ne0\).

The family is not bi-circular.  For the constant function \(f\equiv i\),
\[
\|f\|_\sigma=1,\qquad
(P_1-P_2)f=2-i,
\]
so
\[
\|(P_1-P_2)f\|_\sigma=\sqrt5\ne1.
\]
Thus the phase choice \((1,-1)\) does not give an isometry.

## Semilinear interpolation lemma

The mechanism is elementary but differs decisively from the usual
complex-linear polynomial argument.

Let \(X\) be any complex vector space and let \(T:X\to X\) be conjugate-linear.
For distinct \(\lambda_1,\lambda_2\in\mathbb T\), put
\[
\delta=\lambda_1-\lambda_2,\qquad
P_1=\delta^{-1}(T-\lambda_2I),\qquad P_2=I-P_1.
\]
Then
\[
P_1^2=P_1
\quad\Longleftrightarrow\quad
T^2=I.
\tag{5}
\]
Indeed, if \(T^2=I\), then
\[
TP_1x
 =\frac{x-\overline{\lambda_2}\,Tx}{\overline\delta}.
\]
Since
\[
\overline\delta=-\frac{\delta}{\lambda_1\lambda_2},
\]
the right side equals \(\lambda_1P_1x\).  Therefore
\[
P_1^2x
=\frac{TP_1x-\lambda_2P_1x}{\delta}
=P_1x.
\]
Conversely, expanding \(P_1^2=P_1\) while respecting conjugate-linearity gives
\(T^2=I\).  Equivalently, if \(P_1,P_2\) are already complementary idempotents
and \(T=\lambda_1P_1+\lambda_2P_2\) is conjugate-linear, then
\[
T^2x
 =\overline{\lambda_1}\,TP_1x
  +\overline{\lambda_2}\,TP_2x
 =P_1x+P_2x=x.
\tag{6}
\]
The phase pair disappears from the involution condition.  This is exactly what
fails if one treats a conjugate-linear block as though it were complex-linear.

## Form IV: exact replacement

Under the isometric identification
\[
J:X\longrightarrow \mathbb C\oplus_1 C[0,1],
\qquad
Jf=(f(0),f'),
\tag{7}
\]
the Form IV map (1) becomes
\[
JTJ^{-1}=J_c\oplus W,
\qquad
J_c(a)=c\overline a,\qquad
(Wh)(t)=\beta(t)\overline{h(\phi(t))}.
\tag{8}
\]
Both blocks are conjugate-linear.  Since \(|c|=1\), \(J_c^2=I\).  Also
\[
(W^2h)(t)
=\beta(t)\overline{\beta(\phi(t))}\,h(\phi^2(t)).
\]
Hence \(W^2=I\) exactly under the two conditions in (2).  The semilinear
interpolation lemma then proves the GBCI assertion for every distinct phase
pair.

To see that such a family is never BCI, restrict to the constant functions.
There \(T\) is \(a\mapsto c\overline a\), so \(P_1,P_2\) restrict to two
nonzero complementary real rank-one projections on the Euclidean plane
\(\mathbb C\).  If every \(\alpha P_1+\gamma P_2\), with
\(\alpha,\gamma\in\mathbb T\), were an isometry, choose nonzero
\(u\in\operatorname{ran}P_1\), \(v\in\operatorname{ran}P_2\).  Then
\[
|\alpha u+\gamma v|^2
=|u|^2+|v|^2+2\operatorname{Re}(\alpha\overline\gamma\,u\overline v)
\]
would have to be independent of the phases.  This is impossible because
\(u\overline v\ne0\).

## Mixed linear/conjugate-linear blocks

The same coordinate model explains the paper's Forms II and III without
assuming a false global complex-linearity.

For Form II,
\[
JTJ^{-1}=J_c\oplus V,
\qquad
(Vh)(t)=\beta(t)h(\phi(t)),
\tag{9}
\]
where \(J_c\) is conjugate-linear and \(V\) is complex-linear.  The
interpolation maps \(P_i\) are complementary idempotents exactly when
\[
(V-\lambda_1I)(V-\lambda_2I)=0.
\tag{10}
\]
The scalar conjugate block imposes no additional phase restriction because
\(J_c^2=I\).  In particular, taking \(V=I\) and
\((\lambda_1,\lambda_2)=(1,i)\) gives a non-antipodal GBCI.  It is not BCI
already on the constant subspace, by the same two-real-line argument above.

For Form III,
\[
JTJ^{-1}=cI\oplus W,
\tag{11}
\]
with \(W\) conjugate-linear.  Here the exact blockwise GBCI criterion is
\[
c\in\{\lambda_1,\lambda_2\},
\qquad
W^2=I.
\tag{12}
\]
For example, \(c=1\), \(W(h)=\overline h\), and
\((\lambda_1,\lambda_2)=(1,i)\) satisfy (12); taking \(f(t)=it\) shows that
the resulting family need not be BCI.

These block criteria do not challenge the paper's purely complex-linear Form I
analysis.  They isolate the failure to the semilinear cases.

## Relation to the recent paper

Kumar, Kumar and Abu Baker define GBCI without assuming linearity and record
that an associated isometry is real-linear.  Their Miura classification
contains four isometry forms: Form I is complex-linear; Form IV is
conjugate-linear; Forms II and III mix one complex-linear and one
conjugate-linear block under (7).  Nevertheless, the paper's abstract states
the antipodal-or-BCI dichotomy, and Theorems 3.2--3.4 assert corresponding
BCI conclusions in the semilinear forms.  The counterexample (3) satisfies
the paper's definitions and contradicts the abstract dichotomy directly.

There is important historical context.  Botelho and Miura's 2019 corrigendum
to their 2018 paper already explains that an earlier classification of GBCIs
on differentiable-function spaces was incomplete and that an omitted case
produces additional examples.  That fact is prior art and is not claimed as
new here.  The contribution here is the explicit diagnosis of the current
arXiv:2609.18967v1 semilinear failure, the universal conjugate-involution
lemma (5), and the corrected Form IV and blockwise criteria above.

## Limitations

This record is a correction of the current arXiv v1, not a classification of
all generalized bi-circular idempotents on arbitrary Banach spaces.  It does
not claim that every theorem in arXiv:2609.18967v1 is false; in particular,
the Form I case is not challenged.  The elementary semilinear interpolation
lemma may be known implicitly in the nonlinear-idempotent literature.  The
originality claim is therefore restricted to the documented correction and
the explicit corrected criteria, to the best of our knowledge.

## References

1. H. Kumar, H. Kumar, A. Bin Abu Baker, *Structure of Generalized
   bi-circular idempotents and isometric reflections on \(C^1[0,1]\)*,
   arXiv:2609.18967v1 (2026).
   https://arxiv.org/abs/2609.18967
2. F. Botelho, T. Miura, *Examples of generalized bi-circular idempotents on
   spaces of continuously differentiable functions*, J. Math. Anal. Appl.
   465 (2018), 795--802. DOI: 10.1016/j.jmaa.2018.05.022.
3. F. Botelho, T. Miura, *Corrigendum to "Examples of generalized
   bi-circular idempotents on spaces of continuously differentiable
   functions"*, J. Math. Anal. Appl. 474 (2019), 1481--1487.
   DOI: 10.1016/j.jmaa.2019.02.032.
