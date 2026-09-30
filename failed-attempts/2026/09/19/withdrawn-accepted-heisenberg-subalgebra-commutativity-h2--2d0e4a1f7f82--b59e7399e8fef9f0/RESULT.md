# Subalgebra commutativity of the five-dimensional Heisenberg algebra

Let \(H_m(\mathbb F_q)=V\oplus \mathbb F_q z\) be the \((2m+1)\)-dimensional Heisenberg Lie algebra over a finite field, where \(V\) is a \(2m\)-dimensional symplectic space with nondegenerate alternating form \(\omega\) and
\[
[v+az,w+bz]=\omega(v,w)z.
\]
For a finite-dimensional Lie algebra \(L\) over a finite field, write
\[
\operatorname{sd}(L)
=
\frac{\#\{(A,B)\in\mathcal L(L)^2:[A,B]\subseteq A+B\}}
{|\mathcal L(L)|^2}
\]
for its subalgebra commutativity degree.

The recent preprint arXiv:2609.19086v1 introduces this invariant, asks for the values on Heisenberg algebras, and computes \(H_1(\mathbb F_p)\). The result below gives a uniform symplectic reduction for every \(m\) and an exact closed formula for the next case \(H_2\), over every finite field.

## The symplectic reduction

**Proposition.** Every subalgebra of \(H_m(\mathbb F_q)\) is of exactly one of the following two types.

1. \(W\oplus \mathbb F_qz\), where \(W\le V\) is an arbitrary vector subspace.
2. A graph
   \[
   A(W,f)=\{w+f(w)z:w\in W\},
   \]
   where \(W\le V\) is totally isotropic and \(f\in W^*\).

If one of two subalgebras contains \(z\), the pair is permutable. For two graph subalgebras,
\[
A=A(W,f),\qquad B=A(U,g),
\]
the pair is nonpermutable if and only if
\[
f|_{W\cap U}=g|_{W\cap U}
\quad\text{and}\quad
\omega(W,U)\ne0.
\]

**Proof.** If \(z\in A\), subtracting central components shows
\(A=(A\cap V)\oplus\mathbb F_qz\), and every such vector subspace is a Lie subalgebra because all brackets lie in \(\mathbb F_qz\).

If \(z\notin A\), projection \(H_m\to V\) is injective on \(A\). Hence \(A\) is the graph of a unique linear functional \(f:W\to\mathbb F_q\) on its image \(W\). Closure under brackets is equivalent to
\(\omega|_{W\times W}=0\), because \(A\cap\mathbb F_qz=0\).

For two graphs, \(z\in A+B\) exactly when there is \(w\in W\cap U\) with
\(f(w)\ne g(w)\), i.e. when the two restrictions to \(W\cap U\) differ. If this happens, then \([A,B]\subseteq\mathbb F_qz\subseteq A+B\). If the restrictions agree, then \(z\notin A+B\), while
\([A,B]=\omega(W,U)z\); thus permutability is equivalent to \(\omega(W,U)=0\). \(\square\)

This also gives the total number of subalgebras:
\[
|\mathcal L(H_m(\mathbb F_q))|
=
\sum_{r=0}^{2m}{2m\brack r}_q
+
\sum_{r=0}^{m}q^r I_{m,r}(q),
\]
where
\[
I_{m,r}(q)
=
{m\brack r}_q\prod_{j=0}^{r-1}(q^{m-j}+1)
\]
is the number of \(r\)-dimensional totally isotropic subspaces of a \(2m\)-dimensional symplectic space.

For \(m=1\), the same reduction recovers and slightly extends the formula of arXiv:2609.19086v1 from prime fields to every finite field:
\[
\operatorname{sd}(H_1(\mathbb F_q))
=
\frac{3q^3+12q^2+16q+16}{(q^2+2q+4)^2}.
\]

## Exact formula for \(H_2\)

Let
\[
N=(q+1)(q^2+1).
\]
In a four-dimensional symplectic space there are \(N\) isotropic lines and \(N\) Lagrangian planes. The subalgebras containing \(z\) are indexed by all subspaces of \(V\), while the graph subalgebras are indexed by an isotropic subspace together with a functional. Consequently
\[
|\mathcal L(H_2(\mathbb F_q))|
=
q^5+3q^4+5q^3+6q^2+4q+6
=:S(q).
\]

To count nonpermutable ordered pairs, only graph subalgebras with underlying dimensions \(1\) or \(2\) can contribute.

For two isotropic lines, a fixed line has exactly \(q^3\) nonorthogonal lines. Their intersection is zero, so there are \(q^2\) pairs of functionals satisfying the restriction condition. This contributes
\[
Nq^5.
\]

For a line and a Lagrangian plane, orthogonality is equivalent to containment of the line in the plane. Exactly \(q+1\) Lagrangian planes contain a fixed line, so there are
\[
N-(q+1)=q^2(q+1)
\]
nonorthogonal planes. Their intersection with the line is zero, and there are \(q^3\) functional pairs. Both orientations contribute
\[
2Nq^5(q+1).
\]

For two Lagrangian planes, two distinct planes are always nonorthogonal. For a fixed plane \(W\), exactly \(q(q+1)\) other Lagrangians meet \(W\) in a line and exactly \(q^3\) are disjoint. Agreement of the two functionals contributes \(q^3\) choices in the first case and \(q^4\) in the second. Thus the plane-plane contribution is
\[
N\bigl(q^4(q+1)+q^7\bigr).
\]

Therefore the number of nonpermutable ordered pairs is
\[
\begin{aligned}
B(q)
&=
N\left(q^5+2q^5(q+1)+q^4(q+1)+q^7\right)\\
&=
q^4(q+1)(q^2+1)(q^3+2q^2+4q+1).
\end{aligned}
\]

**Theorem.** For every prime power \(q\),
\[
\boxed{
\operatorname{sd}(H_2(\mathbb F_q))
=
1-
\frac{q^4(q+1)(q^2+1)(q^3+2q^2+4q+1)}
{(q^5+3q^4+5q^3+6q^2+4q+6)^2}
}
\]
or equivalently
\[
\boxed{
\operatorname{sd}(H_2(\mathbb F_q))
=
\frac{
3q^9+12q^8+34q^7+62q^6+91q^5+111q^4+108q^3+88q^2+48q+36
}{
(q^5+3q^4+5q^3+6q^2+4q+6)^2
}.
}
\]

In particular,
\[
\operatorname{sd}(H_2(\mathbb F_q))=\frac{3}{q}+O(q^{-2}).
\]

## Verification

A standalone exhaustive enumerator is included as `artifacts/verify_h2.py`. It constructs every vector subspace of \(\mathbb F_q^5\) in reduced row-echelon form, retains exactly the Lie subalgebras, and tests \([A,B]\subseteq A+B\) directly. It verifies
\[
(q,S(q),B(q))=(2,158,6000)
\]
and
\[
(q,S(q),B(q))=(3,693,187920).
\]
The general theorem does not depend on these finite checks.

## Relation to prior literature

Muhie, Otera and Russo, arXiv:2609.19086v1, define \(\operatorname{sd}(L)\), explicitly ask for values on \(H_m\), and prove the \(m=1\) prime-field formula. Their paper also proves compatibility with subgroup commutativity degree under the Lazard correspondence in its stated range.

The subgroup commutativity degree of finite groups predates this Lie-algebra invariant; for example, Tărnăuceanu, arXiv:1312.0296, studies finite \(P\)-groups. That family is different from the extraspecial groups corresponding to Heisenberg Lie algebras. Targeted searches for subgroup-commutativity formulas for extraspecial groups and for the displayed \(H_2\) polynomials did not locate an earlier equivalent formula.

The classification of Heisenberg subalgebras by isotropic subspaces, and the standard counts of totally isotropic subspaces in finite symplectic spaces, are not claimed as new by themselves. The claimed contribution is the permutability criterion above and its use to obtain the exact \(H_2\) subalgebra commutativity degree, together with the all-\(m\) reduction.

## Limitations

Originality is asserted only to the best of our knowledge. Because the Lazard correspondence transfers this invariant to subgroup commutativity degree for appropriate odd-prime Heisenberg groups, an older formula for extraspecial \(p\)-groups under group-theoretic terminology could imply the prime-field specialization; no such formula was located in the inspected literature. The source preprint is very recent, so a later revision or independent contemporaneous computation may also overlap.

No closed polynomial formula for \(\operatorname{sd}(H_m)\) for arbitrary \(m\ge3\) is claimed here. The symplectic criterion reduces that problem to finite incidence counts but does not by itself evaluate all of them.

## References

- S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (2026), https://arxiv.org/abs/2609.19086v1.
- M. Tărnăuceanu, *The subgroup commutativity degree of finite \(P\)-groups*, arXiv:1312.0296; Bull. Aust. Math. Soc. 93 (2016), 37–41, https://arxiv.org/abs/1312.0296.
