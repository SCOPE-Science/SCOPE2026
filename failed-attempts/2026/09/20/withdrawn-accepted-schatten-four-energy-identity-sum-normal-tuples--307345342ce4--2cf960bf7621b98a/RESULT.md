# A Schatten-four energy identity for sum-normal commuting tuples

## Statement

Let \(\mathcal H\) be a complex Hilbert space and let
\[
\mathbf T=(T_1,\ldots,T_d)
\]
be a commuting \(d\)-tuple with \(T_j\in\mathcal S_4(\mathcal H)\) for every \(j\). Put
\[
C_j=[T_j^*,T_j]=T_j^*T_j-T_jT_j^*,
\qquad
D(\mathbf T)=\sum_{j=1}^d C_j.
\]
Then \(C_j\in\mathcal S_2\), and for every \(1\le j,k\le d\),
\[
\boxed{\operatorname{Tr}(C_jC_k)
=\|[T_j^*,T_k]\|_2^2.}
\tag{1}
\]

Consequently, the real symmetric matrix
\[
G(\mathbf T)=\big(\|[T_j^*,T_k]\|_2^2\big)_{j,k=1}^d
\]
is positive semidefinite. More precisely, for every \(c=(c_1,\ldots,c_d)\in\mathbb C^d\),
\[
\boxed{
\left\|\sum_{j=1}^d c_jC_j\right\|_2^2
=
\sum_{j,k=1}^d\overline{c_j}c_k
\|[T_j^*,T_k]\|_2^2.}
\tag{2}
\]
In particular,
\[
\boxed{
\|D(\mathbf T)\|_2^2
=
\sum_{j,k=1}^d\|[T_j^*,T_k]\|_2^2.}
\tag{3}
\]

Thus every commuting Schatten-four sum-normal tuple is doubly commuting and normal:
\[
D(\mathbf T)=0
\quad\Longrightarrow\quad
[T_j^*,T_k]=0
\quad(1\le j,k\le d).
\tag{4}
\]

There is also a positive-cone consequence at the Hilbert--Schmidt level.

**Corollary.** If \(T_j\in\mathcal S_2\) for all \(j\) and \(\mathbf T\) is sum-hyponormal,
\[
D(\mathbf T)\ge0,
\]
then \(\mathbf T\) is doubly commuting and normal.

## Proof of the pair identity

It is enough to prove the following two-variable assertion. Let \(A,B\in\mathcal S_4\) satisfy \(AB=BA\), and set
\[
C_A=A^*A-AA^*,\qquad C_B=B^*B-BB^*,
\qquad X=[A^*,B]=A^*B-BA^*.
\]
Schatten Hölder implies that every product of four factors chosen from
\(A,A^*,B,B^*\) is trace class. Hence all traces below are defined and trace
cyclicity is legitimate.

Expanding the product of the two self-commutators gives
\[
\begin{aligned}
\operatorname{Tr}(C_AC_B)
={}&\operatorname{Tr}(A^*AB^*B)
-\operatorname{Tr}(A^*ABB^*)\\
&-\operatorname{Tr}(AA^*B^*B)
+\operatorname{Tr}(AA^*BB^*).
\end{aligned}
\]
Since \(AB=BA\), and hence \(A^*B^*=B^*A^*\), cyclicity yields
\[
\operatorname{Tr}(A^*ABB^*)
=
\operatorname{Tr}(AA^*B^*B).
\]
Therefore
\[
\operatorname{Tr}(C_AC_B)
=
\operatorname{Tr}(A^*AB^*B)
-2\operatorname{Tr}(AA^*B^*B)
+\operatorname{Tr}(AA^*BB^*).
\tag{5}
\]

On the other hand,
\[
X^*X
=
(B^*A-AB^*)(A^*B-BA^*),
\]
so
\[
\begin{aligned}
\operatorname{Tr}(X^*X)
={}&\operatorname{Tr}(B^*AA^*B)
-\operatorname{Tr}(B^*ABA^*)\\
&-\operatorname{Tr}(AB^*A^*B)
+\operatorname{Tr}(AB^*BA^*).
\end{aligned}
\]
Using \(AB=BA\), \(A^*B^*=B^*A^*\), and cyclicity, the four terms become,
respectively,
\[
\operatorname{Tr}(AA^*BB^*),\quad
\operatorname{Tr}(AA^*B^*B),\quad
\operatorname{Tr}(AA^*B^*B),\quad
\operatorname{Tr}(A^*AB^*B).
\]
Comparing with (5) proves
\[
\operatorname{Tr}(C_AC_B)=\operatorname{Tr}(X^*X)=\|X\|_2^2.
\]
Taking \(A=T_j\) and \(B=T_k\) gives (1).

Because each \(C_j\) is self-adjoint,
\[
\left\langle C_j,C_k\right\rangle_{\mathcal S_2}
=
\operatorname{Tr}(C_kC_j)
=
\operatorname{Tr}(C_jC_k),
\]
so (1) identifies \(G(\mathbf T)\) with the Gram matrix of
\(C_1,\ldots,C_d\) in \(\mathcal S_2\). This proves (2), and setting
\(c_1=\cdots=c_d=1\) gives (3). If \(D(\mathbf T)=0\), then the right-hand
side of (3) vanishes, so every cross-commutator \([T_j^*,T_k]\) vanishes.
This proves (4).

For the Hilbert--Schmidt corollary, \(T_j\in\mathcal S_2\) implies
\(T_j^*T_j,T_jT_j^*\in\mathcal S_1\), so \(D(\mathbf T)\in\mathcal S_1\).
Cyclicity of the trace gives
\[
\operatorname{Tr}D(\mathbf T)
=
\sum_{j=1}^d
\big(\operatorname{Tr}(T_j^*T_j)-\operatorname{Tr}(T_jT_j^*)\big)
=0.
\]
A positive trace-class operator with trace zero is zero. Hence
\(D(\mathbf T)=0\); since \(\mathcal S_2\subset\mathcal S_4\), (3) then
forces all cross-commutators to vanish.

## Relation to recent work

Chavan, Reza and Sequeira introduced and studied sum-normal and
sum-hyponormal commuting tuples in arXiv:2609.19287v1 (submitted
2026-09-16). Their Question 1.3(ii) asks whether every sum-normal commuting
tuple is normal, and their concluding remarks state that the existence of a
nonnormal sum-normal tuple remains unknown. Their Remark 4.2 observes that a
sum-hyponormal tuple of trace-class operators is sum-normal, by trace
cyclicity.

The identity above answers Question 1.3(ii) affirmatively on the full
Schatten-four class and strengthens the trace-class observation in a
different direction: Hilbert--Schmidt entries already suffice to turn
sum-hyponormality into doubly commuting normality.

Earlier multivariable self-commutator work includes Curto--Jian's matricial
identity for commuting tuples and Misra--Pramanick--Sinha's determinant and
trace inequalities for the block commutator matrix. Those results concern
different matrix/determinant structures. To the best of our knowledge, the
exact Schatten-four energy identity (1)--(3), and its sum-normal and
Hilbert--Schmidt sum-hyponormal consequences above, are not stated in the
literature located for this comparison.

## Limitations

The Schatten-four assumption is a sufficient hypothesis ensuring that the
quartic trace manipulations are legitimate; no sharpness is claimed. In
particular, this does not resolve whether arbitrary compact sum-normal
tuples are normal, nor whether arbitrary compact sum-hyponormal tuples are
normal. No counterexample is supplied beyond \(\mathcal S_4\), and no
optimal Schatten threshold is asserted. Older literature on Hilbert
modules, cross-commutators, or trace identities could contain equivalent
special cases of the pair identity.

## References

1. S. Chavan, M. R. Reza, S. S. Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287v1 (2026). https://arxiv.org/abs/2609.19287
2. G. Misra, P. Pramanick, K. B. Sinha, *A Trace Inequality for Commuting d-Tuples of Operators*, Integral Equations and Operator Theory 94 (2022), Article 16. https://doi.org/10.1007/s00020-022-02693-5
3. R. E. Curto, R. Jian, *A Matricial Identity Involving the Self-Commutator of a Commuting n-Tuple*, Proc. Amer. Math. Soc. 121 (1994), 461--464. https://doi.org/10.2307/2160422
