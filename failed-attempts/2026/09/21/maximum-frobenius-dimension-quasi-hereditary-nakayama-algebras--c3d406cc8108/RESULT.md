# Maximum Frobenius dimension of quasi-hereditary Nakayama algebras

## Result

Let \(k\) be a field and let \(A\) be a finite-dimensional split basic
quasi-hereditary Nakayama \(k\)-algebra with \(n\ge 2\) isomorphism classes of
simple modules. Put
\[
F(A)=\dim_k\operatorname{Hom}_A(D(A),A),
\qquad D=\operatorname{Hom}_k(-,k).
\]
Then
\[
\boxed{F(A)\le n^2+1.}
\]
The bound is sharp for every \(n\ge2\). In particular, for the connected cyclic
Nakayama algebra with Kupisch series
\[
\boxed{(2,n+1,n,n-1,\ldots,3)}
\]
one has
\[
F(A)=n^2+1.
\]

Consequently, the maximum asked for in Question 2 of the 2020 MathOverflow
question *Frobenius dimensions of Nakayama algebras* is exactly \(n^2+1\)
(for split basic Nakayama algebras).

There is a slightly sharper structural statement. If \(A\) is connected and
linear, then \(F(A)\le n^2\). If \(A\) is connected and cyclic and
quasi-hereditary, then among the \(n^2\) spaces
\(\operatorname{Hom}_A(I_s,P_j)\), at most one has dimension \(2\), and all
the others have dimension at most \(1\).

## Uniserial Hom formula

For a connected cyclic Nakayama algebra, index the simple right modules by
\(\mathbb Z/n\mathbb Z\). Let
\[
M(u,\ell)
\]
denote the indecomposable module with top \(S_u\) and length \(\ell\). If
\(M(v,m)\) is another indecomposable module, then
\[
\dim_k\operatorname{Hom}_A(M(u,\ell),M(v,m))
=
\#\left\{
r:\max(0,m-\ell)\le r<m,\quad v+r\equiv u\pmod n
\right\}. \tag{1}
\]
Indeed, a homomorphism is determined by the image of a top generator. It may
land in a radical layer \(r\) carrying \(S_u\), and the source relation of
length \(\ell\) is respected precisely when \(r+\ell\ge m\). In the split
uniserial setting, each eligible occurrence contributes one independent map.

## Proof of the upper bound: linear case

For a connected linear Nakayama algebra, no indecomposable module contains the
same simple composition factor twice. Hence (1), without cyclic wrap-around,
gives
\[
\dim_k\operatorname{Hom}_A(I_s,P_j)\le1
\]
for every indecomposable injective \(I_s\) and projective \(P_j\). Since
\[
D(A)\cong\bigoplus_{s=1}^n I_s,\qquad
A\cong\bigoplus_{j=1}^n P_j,
\]
we obtain
\[
F(A)\le n^2.
\]

## Proof of the upper bound: cyclic case

Let the Kupisch series be \((c_i)_{i\in\mathbb Z}\), periodically extended by
\(c_{i+n}=c_i\), and put
\[
\rho_i=i+c_i.
\]
The Kupisch inequalities \(c_{i+1}\ge c_i-1\) say exactly that
\[
\rho_i\le\rho_{i+1},
\qquad
\rho_{i+n}=\rho_i+n. \tag{2}
\]

A cyclic Nakayama algebra has no simple projective. By the
Uematsu--Yamagata criterion, a quasi-hereditary cyclic Nakayama algebra
therefore has a simple module of projective dimension \(2\). Rotate indices so
that this simple is \(S_0\), and set
\[
a=c_0=\rho_0.
\]
The first two syzygies are
\[
\Omega S_0=M(1,a-1),
\]
and
\[
\Omega^2S_0
=
M\!\left(a,c_1-a+1\right).
\]
Because \(\operatorname{pd}S_0=2\), the latter module is projective. Thus
\[
c_a=c_1-a+1,
\]
or equivalently
\[
\rho_a=\rho_1.
\]
By monotonicity in (2),
\[
\rho_1=\rho_2=\cdots=\rho_a=:h. \tag{3}
\]
If \(a>n\), then (3) would contain both \(1\) and \(1+n\), contradicting
\(\rho_{1+n}=\rho_1+n\). Hence \(a\le n\). Write
\[
h=a+b.
\]
Since \(b=c_a\ge2\) and
\[
h=\rho_a\le\rho_n=\rho_0+n=a+n,
\]
we also have \(b\le n\).

Put
\[
q=a+b-n.
\]
From (3),
\[
c_i=n+q-i\qquad(1\le i\le a). \tag{4}
\]
For \(i\ge a\), monotonicity and periodicity give
\[
\rho_i\le \rho_n=a+n\le i+n,
\]
so \(c_i\le n\). Together with \(c_0=a\le n\), equation (4) shows that the
projectives of length strictly greater than \(n\) are exactly
\[
P_1,\ldots,P_{q-1} \tag{5}
\]
when \(q\ge2\); if \(q\le1\), there are none. Moreover every projective has
length at most \(2n-1\).

Now describe the injectives. For an integer lift \(s\), define
\[
\lambda_s=\min\{i\in\mathbb Z:\rho_i>s\}.
\]
Then the indecomposable injective with socle \(S_s\) is
\[
I_s=M(\lambda_s,s-\lambda_s+1).
\]
Its length is greater than \(n\) if and only if
\[
\lambda_s\le s-n
\iff
\rho_{s-n}>s
\iff
\rho_s-s>n
\iff
c_s>n.
\]
Thus the long injectives have the same residue indices as in (5). For
\(1\le s\le q-1\),
\[
\rho_{-n}=a-n\le0\le s,\qquad
\rho_{1-n}=h-n=q>s,
\]
so
\[
\lambda_s=1-n,\qquad
I_s=M(1-n,n+s). \tag{6}
\]
In particular every long injective has top \(S_1\), and every injective has
length at most \(2n-1\).

Formula (1) now gives
\[
\dim_k\operatorname{Hom}_A(I_s,P_j)\le2
\]
for all \(s,j\). Dimension \(2\) is possible only if both source and target
have length \(>n\), hence only when
\[
1\le s,j\le q-1.
\]
By (6), the source top is \(S_1\). For \(j\ge2\), the module
\[
P_j=M(j,n+q-j)
\]
contains \(S_1\) only once: the first occurrence is at radical position
\(n+1-j\), while a second occurrence would be at \(2n+1-j\), which lies
outside \(P_j\) because \(q\le n\). Therefore a two-dimensional Hom space can
only target \(P_1\).

Finally,
\[
P_1=M(1,n+q-1)
\]
contains \(S_1\) at positions \(0\) and \(n\). For
\(I_s=M(1-n,n+s)\), formula (1) permits position \(0\) precisely when
\[
n+s\ge n+q-1,
\]
that is, precisely when \(s=q-1\). Hence there is at most one
two-dimensional space:
\[
\operatorname{Hom}_A(I_{q-1},P_1).
\]
All other \(n^2-1\) Hom spaces have dimension at most \(1\). Therefore
\[
F(A)\le (n^2-1)\cdot1+2=n^2+1.
\]

## Sharpness

Consider the cyclic Kupisch series
\[
(c_0,c_1,\ldots,c_{n-1})
=
(2,n+1,n,n-1,\ldots,3).
\]
It is admissible. Moreover,
\[
\Omega S_0=S_1,\qquad
\Omega^2S_0=\operatorname{rad}P_1\cong P_2,
\]
so \(S_0\) has projective dimension \(2\); hence the algebra is
quasi-hereditary.

For this family the co-Kupisch series is
\[
(n,n+1,2,3,\ldots,n-1).
\]
Every indecomposable injective has top \(S_1\). For \(j=0\) or \(j\ge2\), the
unique occurrence of \(S_1\) relevant to (1) is the last composition factor of
\(P_j\), so every \(\operatorname{Hom}_A(I_s,P_j)\) is nonzero. For \(j=1\),
the occurrence at radical position \(n\) is always eligible, and the occurrence
at position \(0\) is eligible only for \(I_1\). Consequently
\[
\dim_k\operatorname{Hom}_A(I_s,P_j)=1
\]
for all pairs except
\[
\dim_k\operatorname{Hom}_A(I_1,P_1)=2.
\]
Thus
\[
F(A)=n^2+1.
\]

If disconnected split basic Nakayama algebras are allowed, apply the connected
argument to each component. Frobenius dimension is additive under finite
products, and for component sizes \(n_t\) the elementary inequality
\[
\sum_t n_t^2+\#\{\text{cyclic components}\}\le n^2
\]
holds whenever there is more than one component. Hence disconnected algebras
cannot improve the connected maximum.

## Context and literature

The 2020 MathOverflow question explicitly asked for the maximal Frobenius
dimension of a quasi-hereditary Nakayama algebra with \(n\) simple modules and
reported the values
\[
5,10,17,26,37,50,65,
\]
conjecturing \(n^2+1\). The page remains unanswered at the time of this record.

Uematsu and Yamagata proved the criterion that a Nakayama algebra is
quasi-hereditary if and only if it has a simple module of projective dimension
\(0\) or \(2\). Marczinzik and Sen restated this criterion and developed
further characterizations of quasi-hereditary Nakayama algebras.

The 2026 preprint *Bounds on Frobenius dimension* gives general bounds in terms
of the vector-space dimension of an algebra, low-dimensional classifications,
and formulas for truncated path algebras. Its full text contains no occurrence
of “Nakayama” or “quasi-hereditary” and does not state the bound above.

To the best of our knowledge, the \(n^2+1\) theorem and the structural
“at most one double Hom” mechanism above have not previously been published.

## Limitations

- The statement is formulated for split basic finite-dimensional Nakayama
  algebras over a field.
- This resolves Question 2 of the cited 2020 MathOverflow post, not Question 1
  about whether \(F(A)\ge\operatorname{gldim}(A)\) for every finite-global-
  dimension Nakayama algebra.
- Originality is to the best of our knowledge. The proof uses standard
  uniserial-module combinatorics and a classical quasi-heredity criterion, so
  an implicit or differently phrased antecedent in older serial-ring
  literature remains possible.

## Reproducibility

`artifacts/verify_small.py` performs an exact finite check for cyclic
quasi-hereditary Kupisch series for \(2\le n\le6\). It computes projective
dimensions by syzygies, computes co-Kupisch lengths and the uniserial Hom
dimensions from (1), and confirms the maximum \(n^2+1\) in every tested size.
The symbolic proof above does not depend on this enumeration.

## References

1. MathOverflow, *Frobenius dimensions of Nakayama algebras* (2020):
   https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras
2. M. Uematsu and K. Yamagata, *On serial quasi-hereditary rings*,
   Hokkaido Math. J. 19 (1990), 165--174:
   https://www.math.sci.hokudai.ac.jp/hmj/page/19-1/HMJ_19_1_1990_165-174.html
3. R. Marczinzik and E. Sen, *A new characterisation of quasi-hereditary
   Nakayama algebras and applications*, Communications in Algebra 50 (2022),
   4288--4302; arXiv:2109.03441:
   https://arxiv.org/abs/2109.03441
4. D. Artenstein, A. González and M. Lanzilotta, *Constructing nearly
   Frobenius algebras*, Algebras and Representation Theory 18 (2015),
   339--367; arXiv:1306.3964:
   https://arxiv.org/abs/1306.3964
5. D. Artenstein, J. Cóppola, J. Finot, A. González and G. Mata,
   *Bounds on Frobenius dimension* (2026), arXiv:2607.15999:
   https://arxiv.org/abs/2607.15999
