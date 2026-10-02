# Tachikawa reduction at every Nakayama cycle length

## Statement

Let \(R\) be a commutative artinian ring, let \(E\) be an injective envelope of \(R/\operatorname{rad}R\), put \(D=\operatorname{Hom}_R(-,E)\), and let \(\Lambda\) be an artin \(R\)-algebra. For an integer \(r\ge2\), define the cyclic \(r\)-fold trivial extension
\[
T_r(\Lambda)=
\begin{pmatrix}
\Lambda&0&\cdots&0&D\Lambda\\
D\Lambda&\Lambda&\ddots&&0\\
0&D\Lambda&\ddots&\ddots&\vdots\\
\vdots&\ddots&\ddots&\Lambda&0\\
0&\cdots&0&D\Lambda&\Lambda
\end{pmatrix},
\]
where products of two \(D\Lambda\)-entries are zero and mixed products use the natural \(\Lambda\)-bimodule structure on \(D\Lambda\). For \(r=2\) this is Enomoto's two-fold trivial extension. Over a field it is the standard \(r\)-fold trivial extension.

**Theorem.** For every \(r\ge2\), \(T_r(\Lambda)\) is self-injective. If \(T_r(\Lambda)\) satisfies Tachikawa's second conjecture (TC2), then \(\Lambda\) satisfies the Auslander--Reiten conjecture (ARC).

Thus Enomoto's recent reduction through \(T_2(\Lambda)\) is not intrinsically two-fold: every cyclic length \(r\ge2\) gives the same reduction. Equivalently, if \(X\) is a nonprojective ARC counterexample over \(\Lambda\), then for every \(r\ge2\) the induced module
\[
F_rX=X\otimes_\Lambda eT_r(\Lambda)
\]
is a nonprojective self-orthogonal module over the self-injective algebra \(T_r(\Lambda)\), hence a TC2 counterexample.

For finite-dimensional algebras over a field \(k\), this has a sharp Nakayama-theoretic consequence. For every fixed integer \(r\ge2\), the following are equivalent:

1. every finite-dimensional \(k\)-algebra satisfies ARC;
2. every standard \(r\)-fold trivial extension \(T_r(A)\) satisfies TC2;
3. every basic finite-dimensional self-injective \(k\)-algebra whose Nakayama permutation is a disjoint union of \(r\)-cycles satisfies TC2.

Moreover, the cyclic-shift Nakayama automorphism of \(T_r(A)\) has outer order exactly \(r\). Hence, for each prescribed nontrivial finite Nakayama cycle length, TC2 on that single cycle type is already equivalent to universal ARC. In particular, any hypothetical ARC counterexample would generate TC2 counterexamples of every exact nontrivial finite Nakayama outer period \(2,3,4,\ldots\).

## Self-injectivity for every cyclic length

Index the diagonal copies of \(\Lambda\) by \(i\in\mathbb Z/r\mathbb Z\), and write an element of \(T_r(\Lambda)\) as
\[
x=(a_i,\varphi_i)_{i\in\mathbb Z/r\mathbb Z},
\]
where \(a_i\in\Lambda\) is diagonal and \(\varphi_i\in D\Lambda\) is the cyclic off-diagonal entry from layer \(i\) to layer \(i+1\). Define
\[
\ell:T_r(\Lambda)\longrightarrow E,
\qquad
\ell(x)=\sum_i\varphi_i(1).
\]
If \(y=(b_i,\psi_i)_i\), then the cyclic off-diagonal component of \(xy\) is
\[
\varphi_i b_i+a_{i+1}\psi_i,
\]
so
\[
\ell(xy)=\sum_i\bigl(\varphi_i(b_i)+\psi_i(a_{i+1})\bigr).
\]
If \(\ell(xy)=0\) for every \(y\), varying one \(\psi_i\) at a time gives \(\psi_i(a_{i+1})=0\) for every \(\psi_i\in D\Lambda\), hence \(a_{i+1}=0\) because \(E\) is a cogenerator. Varying one \(b_i\) at a time then gives \(\varphi_i=0\). Thus the right-module map
\[
T_r(\Lambda)\longrightarrow D({}_{T_r(\Lambda)}T_r(\Lambda)),
\qquad
x\longmapsto (y\mapsto\ell(xy)),
\]
is injective. The two modules have the same finite \(R\)-length, so it is an isomorphism. Hence \(T_r(\Lambda)\) is self-injective. This is the cyclic analogue of Enomoto's proof for \(r=2\).

## Ext comparison is independent of \(r\)

Let \(\Gamma=T_r(\Lambda)\), and let \(e\) be the diagonal idempotent corresponding to the first copy of \(\Lambda\). Then
\[
e\Gamma e=\Lambda,
\qquad
{}_{\Lambda}e\Gamma\cong \Lambda\oplus D\Lambda.
\]
The second isomorphism follows directly from the first matrix row: it contains the diagonal copy of \(\Lambda\) and one cyclic \(D\Lambda\)-entry, independently of \(r\).

For \(X\in\operatorname{mod}\Lambda\), put
\[
F_rX=X\otimes_\Lambda e\Gamma.
\]
Enomoto's general idempotent-induction lemma applies to any algebra \(\Gamma\) and idempotent \(e\): \(F_r\) is fully faithful, reflects projectivity, and if
\(\operatorname{Tor}^\Lambda_i(X,e\Gamma)=0\) for \(i>0\), then
\[
\operatorname{Ext}^n_\Gamma(F_rX,F_rY)
\cong
\operatorname{Ext}^n_\Lambda(X,Y)
\qquad(n\ge0)
\]
for every \(Y\in\operatorname{mod}\Lambda\).

Assume now that
\[
\operatorname{Ext}^i_\Lambda(X,X\oplus\Lambda)=0
\qquad(i>0).
\]
Using the exact duality \(D\) and \(DD\Lambda\cong\Lambda\),
\[
D\operatorname{Tor}^\Lambda_i(X,D\Lambda)
\cong
\operatorname{Ext}^i_\Lambda(X,DD\Lambda)
\cong
\operatorname{Ext}^i_\Lambda(X,\Lambda)=0.
\]
Hence \(\operatorname{Tor}^\Lambda_i(X,D\Lambda)=0\), and therefore
\[
\operatorname{Tor}^\Lambda_i(X,e\Gamma)=0
\qquad(i>0).
\]
It follows that
\[
\operatorname{Ext}^i_\Gamma(F_rX,F_rX)
\cong
\operatorname{Ext}^i_\Lambda(X,X)=0
\qquad(i>0).
\]
If \(\Gamma\) satisfies TC2, self-injectivity of \(\Gamma\) forces \(F_rX\) to be projective. Since induction along \(e\) reflects projectivity, \(X\) is projective. This proves ARC for \(\Lambda\).

The proof isolates the reason the layer number disappears: the entire homological comparison sees only the first row \(eT_r(\Lambda)\cong\Lambda\oplus D\Lambda\), which is identical for every \(r\ge2\).

## Nakayama cycle structure over a field

Now let \(R=k\) be a field. Chan--Darpö--Iyama--Marczinzik record that the standard \(r\)-fold trivial extension is self-injective and that its Nakayama automorphism \(\nu_r\) is the cyclic one-step shift of the matrix layers.

Let \(I\) be the square-zero ideal consisting of all off-diagonal \(DA\)-entries. Then
\[
T_r(A)/I\cong A^r,
\]
and \(\nu_r\) induces the cyclic permutation of the \(r\) direct factors. Thus \(\nu_r^r=1\). If \(0<d<r\) and \(\nu_r^d\) were inner, then its induced automorphism on \(A^r\) would also be inner. But inner automorphisms fix the center pointwise, while the induced shift moves the central idempotent
\((1,0,\ldots,0)\). Therefore no proper positive power of \(\nu_r\) is inner, and
\[
\operatorname{ord}_{\operatorname{Out}(T_r(A))}([\nu_r])=r.
\]

If \(A\) is basic with primitive idempotents \(e_1,\ldots,e_m\), then \(T_r(A)\) is basic and the Nakayama permutation sends the copy of \(e_j\) in layer \(s\) to the copy of \(e_j\) in layer \(s+1\). Its cycle decomposition therefore consists of \(m\) cycles, each of length \(r\).

## Fixed Nakayama cycle length is already universal-hard

Universal ARC immediately implies TC2 for every self-injective finite-dimensional algebra, so condition (1) above implies (2) and (3). The theorem gives (2) \(\Rightarrow\) (1).

For (3) \(\Rightarrow\) (1), let \(A\) be arbitrary and replace it by a basic Morita-equivalent algebra \(B\). ARC is Morita invariant. The algebra \(T_r(B)\) is basic and self-injective, and its Nakayama permutation is a disjoint union of \(r\)-cycles. By (3), \(T_r(B)\) satisfies TC2. The theorem then gives ARC for \(B\), hence for \(A\).

Combining this with Enomoto's equivalence cycle among the universal ARC, generalized Nakayama, Auslander--Gorenstein, Nakayama, Gorenstein-projective, and TC2 conjectures shows that, for every fixed \(r\ge2\), any one of those universal conjectures is also equivalent to TC2 restricted to the above single Nakayama cycle type.

## Relation to prior work

Enomoto proved in arXiv:2609.19172v1 that TC2 for the two-fold trivial extension \(T_2(\Lambda)\) implies ARC for \(\Lambda\), and deduced the universal implication TC2 \(\Rightarrow\) ARC. His arbitrary-idempotent Ext lemma is the homological input used here.

Chan--Darpö--Iyama--Marczinzik developed \(r\)-fold trivial extensions earlier. They record the standard \(r\times r\) matrix form over a field, self-injectivity, and the cyclic Nakayama automorphism. These structural facts are prior work. The new point is that Enomoto's recent TC2-to-ARC mechanism works unchanged for every cyclic layer number \(r\ge2\), and therefore makes each prescribed nontrivial Nakayama cycle length a universal test class.

## Limitations and originality

Originality is claimed only to the best of our knowledge. Searches for combinations of “Tachikawa”, “TC2”, “Auslander--Reiten”, “r-fold trivial extension”, “Nakayama permutation”, and prescribed Nakayama order did not locate the all-\(r\) reduction or the fixed-cycle-length equivalence above. The two main ingredients are individually known: Enomoto's \(r=2\) reduction and the established structure of \(T_r(A)\). Because the extension is short once these are placed side by side, independent contemporaneous observation is a significant residual risk.

No specific inaccessible source gave concrete evidence of prior coverage. Older work on repetitive categories and orbit algebras may use different language for the cyclic construction, but the relevant structural source above was inspected directly. Enomoto's preprint is very recent, so unindexed follow-up work is an additional residual risk.

The result does not prove ARC or TC2. It proves a family of reductions. The case \(r=1\), i.e. the ordinary symmetric trivial extension \(T(A)\), is not covered by this idempotent argument and no claim is made that TC2 restricted to symmetric algebras is equivalent to universal ARC.

## References

1. H. Enomoto, *Tachikawa's second conjecture implies the Auslander--Reiten conjecture*, arXiv:2609.19172v1 (2026).
2. A. Chan, E. Darpö, O. Iyama, R. Marczinzik, *Periodic trivial extension algebras and fractionally Calabi--Yau algebras*, arXiv:2012.11927v4; Ann. Sci. Éc. Norm. Supér. 58 (2025).
