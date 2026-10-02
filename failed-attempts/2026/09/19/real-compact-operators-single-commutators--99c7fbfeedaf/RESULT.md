# Real compact operators are single commutators of real compact operators

## Result

Let \(H_{\mathbb R}\) be an infinite-dimensional real Hilbert space and let
\(T\in K(H_{\mathbb R})\). Then there exist **real** compact operators
\(A,B\in K(H_{\mathbb R})\) such that
\[
T=[A,B]=AB-BA.
\]
Moreover there is a universal constant \(C>0\), independent of \(H_{\mathbb R}\)
and \(T\), for which the factors may be chosen with
\[
\max\{\|A\|,\|B\|\}\le C\|T\|^{1/2}.
\]

Thus the commutator-width-one theorem recently proved by Zhichao Liu for
compact operators on complex Hilbert space has a real-Hilbert-space analogue
with the same square-root norm scale.

The nonseparable case follows from the separable one: the closed span of
\(\operatorname{ran}T+\operatorname{ran}T^*\) is separable and reducing, and
one may enlarge it inside the kernel to a separable infinite-dimensional
reducing subspace when necessary.

## Context

Liu proved that every compact operator on a separable infinite-dimensional
**complex** Hilbert space is a commutator of compact operators, with a universal
square-root norm bound. His proof uses a dimension-free finite-matrix commutator
estimate and a quantitative reduction to zero diagonal. The published argument
explicitly works over the complex field.

Independently, Tuan Tran proved a dimension-free commutator theorem over both
\(\mathbb R\) and \(\mathbb C\): every traceless real or complex matrix is a
commutator over the same field, with a dimension-independent product bound.
That theorem supplies the finite-dimensional real input. The remaining
field-sensitive point is the reduction of a real compact operator to zero
diagonal, because the complex proof uses the four phases
\(\{1,-1,i,-i\}\).

The following real balancing lemma replaces that phase argument.

## Lemma 1: real diagonal balancing

Let \(R\) be a compact operator on a real separable Hilbert space. Suppose that
relative to some orthonormal basis \((e_n)\), with
\[
d_n=\langle Re_n,e_n\rangle,
\]
either

1. \(\sum_n |d_n|<\infty\) and \(\sum_n d_n=0\), or
2. \(\sum_n d_n^+=\sum_n d_n^-=\infty\).

Then \(R\) has an orthonormal basis with zero diagonal.

### Proof

In either case the \(d_n\) can be reordered so that the partial sums
\[
s_n=\sum_{j=1}^n d_j
\]
satisfy \(s_n\to0\) and
\[
s_n d_{n+1}\le0
\]
whenever neither term is zero. A greedy ordering suffices: while the current
partial sum is positive, take an unused negative term; while it is negative,
take an unused positive term. In the divergent case the overshoot at each sign
change is bounded by the last selected \(|d_n|\), hence tends to zero. In the
absolutely summable zero-total case the same procedure exhausts the sequence
and converges to the total sum \(0\).

Write \(q(x)=\langle Rx,x\rangle\). Inductively construct orthonormal vectors
\(z_1,z_2,\ldots\) and residual unit vectors \(r_n\) such that
\[
\operatorname{span}\{z_1,\ldots,z_{n-1},r_n\}
 =\operatorname{span}\{e_1,\ldots,e_n\},
\quad
q(z_j)=0,
\quad
q(r_n)=s_n.
\]
Start with \(r_1=e_1\). Since \(q(r_n)=s_n\) and
\(q(e_{n+1})=d_{n+1}\) have opposite signs, continuity of \(q\) on the unit
circle in \(\operatorname{span}\{r_n,e_{n+1}\}\) gives a unit vector \(z_n\)
with \(q(z_n)=0\). Let \(r_{n+1}\) be its orthogonal companion in that
two-dimensional plane. Invariance of the trace of the two-dimensional
compression gives
\[
q(r_{n+1})=s_n+d_{n+1}=s_{n+1}.
\]

If \(Z=\overline{\operatorname{span}}\{z_n\}\), then
\(\dim Z^\perp\le1\): for \(x\in Z^\perp\), its projection onto
\(\operatorname{span}\{e_1,\ldots,e_n\}\) is a scalar multiple of \(r_n\).
If \(Z^\perp\ne\{0\}\), choose a unit vector \(x\in Z^\perp\); after changing
signs, \(r_n\to x\), and therefore
\[
q(x)=\lim_n q(r_n)=\lim_n s_n=0.
\]
Adding \(x\) completes a zero-diagonal orthonormal basis. \(\square\)

## Lemma 2: real non-trace-class compacts are uniformly similar to zero diagonal

There is a universal \(c_0\) (one may take \(c_0=\sqrt7\)) such that every
\[
T\in K(H_{\mathbb R})\setminus S_1(H_{\mathbb R})
\]
is similar to a zero-diagonal real compact operator:
\[
S^{-1}TS\ \text{has zero diagonal},\qquad
\|S\|,\|S^{-1}\|\le c_0.
\]

### Proof

Choose an orthonormal sequence \((y_n)\) so sparse that
\[
\|Ty_n\|+\|T^*y_n\|\le2^{-n}.
\]
Let \(N=\overline{\operatorname{span}}\{y_n\}\), \(M=N^\perp\), and \(P\) be
the projection onto \(N\). Then
\[
T=(C\oplus0)+K,\qquad C=(I-P)T|_M,
\]
where
\[
K=PT+TP-PTP\in S_1.
\]
Hence \(C\notin S_1\). Split
\[
C=H+J,\qquad
H=\frac{C+C^*}{2},\qquad
J=\frac{C-C^*}{2}.
\]

If \(H\notin S_1\), choose a real orthonormal eigenbasis
\(Hx_n=\lambda_nx_n\) with
\(\sum_n|\lambda_n|=\infty\). Partition the indices into two sets on each of
which \(\sum|\lambda_n|=\infty\), and choose \(q_n\in\{1,-1\}\) so that
\(q_n\lambda_n\) is positive on one set and negative on the other. On
\[
F_n=\operatorname{span}\{x_n,y_n\}
\]
use
\[
S_n=
\begin{pmatrix}
1&1\\
-q_n&1-q_n
\end{pmatrix},
\qquad
S_n^{-1}=
\begin{pmatrix}
1-q_n&-1\\
q_n&1
\end{pmatrix}.
\]
These matrices have determinant \(1\) and
\(\|S_n\|,\|S_n^{-1}\|\le\sqrt7\). Since
\(\langle Cx_n,x_n\rangle=\lambda_n\),
\[
S_n^{-1}
\begin{pmatrix}\lambda_n&0\\0&0\end{pmatrix}
S_n
=
\begin{pmatrix}
(1-q_n)\lambda_n&(1-q_n)\lambda_n\\
q_n\lambda_n&q_n\lambda_n
\end{pmatrix}.
\]
Thus the \(y_n\)-diagonal of the transformed \(C\oplus0\) has infinite
positive and negative mass. The transformed \(K\) is trace class, so its
diagonal is an \(\ell_1\) perturbation and cannot destroy either divergence.
Lemma 1 then gives a zero diagonal after an orthogonal change of basis.

If \(H\in S_1\), then \(J\notin S_1\). A compact real skew-adjoint operator has
an orthogonal decomposition into two-dimensional blocks
\[
\begin{pmatrix}0&-s_n\\ s_n&0\end{pmatrix},
\qquad s_n>0,
\]
with \(\sum_ns_n=\infty\). On each nonzero block use the fixed real shear
\[
R_0=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Then
\[
R_0^{-1}
\begin{pmatrix}0&-s_n\\ s_n&0\end{pmatrix}
R_0
=
\begin{pmatrix}-s_n&-2s_n\\ s_n&s_n\end{pmatrix}.
\]
Hence the transformed skew part already has diagonal masses
\(-s_n,+s_n\). The transformed \(H+K\) is trace class and contributes only an
\(\ell_1\) diagonal perturbation. Lemma 1 again produces a zero diagonal.
The shear and its inverse have norm \(<2\), so the uniform bound
\(\sqrt7\) covers both cases. \(\square\)

## Lemma 3: real zero-diagonal compacts have compact commutator factors

There is a universal \(C_1\) such that every zero-diagonal real compact operator
\(R\) can be written
\[
R=[A,B],\qquad A,B\in K(H_{\mathbb R}),
\qquad
\|A\|\,\|B\|\le C_1\|R\|.
\]

Indeed, Liu's zero-diagonal construction reduces the problem to uniformly
controlled commutators of finite trace-zero diagonal blocks and to real
Sylvester equations with positive scalar spectral shifts. Tran's theorem gives
the needed real finite-dimensional commutator estimate. The remaining steps
are Neumann-series solutions of real operator equations and block norm
estimates, so the construction stays over \(\mathbb R\) without alteration.

Combining Lemmas 2 and 3 proves the theorem outside \(S_1\).

## Trace-class operators

Three cases complete the proof.

* If \(T\in S_1\) and \(\operatorname{Tr}T=0\), then in any orthonormal basis
  the real diagonal is absolutely summable with sum zero. Lemma 1 makes the
  diagonal zero, and Lemma 3 applies.

* If \(T\) has finite rank, Anderson's rank-one commutator construction can be
  taken over the reals: the explicit block matrices reproduced by
  Beltiţă--Patnaik--Weiss have only real entries. Liu's tensor amplification
  therefore gives real compact factors for an arbitrary finite-rank real
  operator, with a universal square-root norm bound.

* Let \(T\in S_1\) have infinite rank and nonzero trace. Liu's
  trace-concentration lemma also works over the reals. Its only field-sensitive
  opening step is the choice of \(u\) with
  \(\langle Tu,u\rangle\ne0\): here
  \[
  \operatorname{Tr}\frac{T+T^*}{2}=\operatorname{Tr}T\ne0,
  \]
  so such a real unit vector exists. The real Riesz representation theorem and
  the remaining idempotent/block manipulations give, after a uniformly bounded
  real similarity,
  \[
  \widehat T=
  \begin{pmatrix}D&E\\F&G\end{pmatrix},
  \]
  where \(D\) has finite rank and \(G\in S_1\) has trace zero. The preceding two
  bullets give a real compact commutator representation for \(D\) and a
  zero-diagonal real basis for \(G\). Liu's gluing lemma then carries over:
  its finite trace-zero blocks are handled by Tran's real matrix theorem, and
  its Sylvester equations use real positive shifts. This yields real compact
  factors for \(\widehat T\), hence for \(T\).

All estimates involved are dimension-free. Thus
\[
\|A\|\,\|B\|\le C_2\|T\|
\]
for a universal \(C_2\). Reciprocal rescaling by a positive real scalar makes
the factor norms equal and gives
\[
\max\{\|A\|,\|B\|\}\le C\|T\|^{1/2}.
\]

## Why complexification alone is insufficient

Complexifying a real \(T\) and applying the complex theorem does not by itself
produce real factors: complex factors need not commute with the canonical
conjugation. Taking real and imaginary parts generally turns one complex
commutator into a sum or difference of real commutators, not a single one.
The real balancing step and the real finite-matrix theorem are therefore
substantive field-preserving ingredients.

## Originality and limitations

To the best of our knowledge, the inspected literature does not state the
single-commutator theorem for arbitrary compact operators on real Hilbert
space. Liu's current theorem is explicitly complex, whereas Tran's theorem is
real and complex but finite-dimensional. The older Anderson construction gives
the real rank-one ingredient, not the general result.

The proof is not claimed to optimize the universal constant. The result is
specific to infinite-dimensional real Hilbert spaces; in finite dimensions a
commutator has trace zero, so arbitrary matrices cannot satisfy the conclusion.
No assertion is made here about sharper ideal membership of the factors or
about analogous statements for general real Banach spaces.

## References

1. Z. Liu, *Every compact operator is a commutator of compact operators*,
   arXiv:2609.20672v1 (2026).
2. T. Tran, *Quantum expanders and dimension-free commutator bounds*,
   arXiv:2609.20161v1 (2026).
3. D. Beltiţă, S. Patnaik, G. Weiss, *\(B(H)\)-Commutators: A Historical
   Survey II and recent advances on commutators of compact operators*,
   arXiv:1303.4844 (2013).
4. J. Anderson, *Commutators of compact operators*, J. Reine Angew. Math.
   291 (1977), 128--132.
5. P. Fan, C.-K. Fong, *Operators similar to zero diagonal operators*,
   Proc. Roy. Irish Acad. Sect. A 87A (1987), 147--153.
