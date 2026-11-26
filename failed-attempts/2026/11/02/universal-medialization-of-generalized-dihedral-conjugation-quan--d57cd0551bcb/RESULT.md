# Universal medialization of generalized-dihedral conjugation quandles

## Finding

**Theorem.** Let \(A\) be any abelian group, written additively, and let \(G=\operatorname{Dih}(A)=A\rtimes C_2\), where the nonidentity element of \(C_2\) acts by inversion. Give \(G\) its right-conjugation quandle operation \(x*y=y^{-1}xy\). Write \(R_a\) for \(a\in A\) in the rotation component and \(F_a\) for its reflection-component copy, for every \(a\in A\).

The **least quandle congruence making \(\operatorname{Conj}(G)\) medial** has precisely the following identifications:

\[
 R_a\equiv R_b\iff a=b,\qquad
 F_a\equiv F_b\iff a-b\in 4A,\qquad
 R_a\not\equiv F_b.
\]

Consequently its universal medial quotient has underlying disjoint union \(A\sqcup(A/4A)\). Its complete operation table is

\[
\begin{aligned}
 R_a*R_b&=R_a,&R_a*F_{\bar b}&=R_{-a},\\
 F_{\bar a}*R_b&=F_{\overline{a+2b}},&
 F_{\bar a}*F_{\bar b}&=F_{\overline{2b-a}}.
\end{aligned}
\]

Here \(\bar a=a+4A\) and the two components remain disjoint, even when \(A\) has exponent two. In particular, for finite \(A\),

\[
 \bigl|\operatorname{Conj}(\operatorname{Dih}(A))^{\mathrm{med}}\bigr|
 =|A|+|A/4A|.
\]

If \(A\cong\bigoplus_{i=1}^{r}\mathbb Z/m_i\mathbb Z\), this cardinality equals \(\prod_i m_i+\prod_i\gcd(m_i,4)\). For the dihedral group of order \(2n\) it is \(n+\gcd(n,4)\). The original conjugation quandle is already medial precisely when \(4A=0\); this last criterion is also an instance of the previously known general nilpotency-class criterion.

## Assumptions and scope

No finiteness, torsion, or generation hypothesis is imposed on \(A\). Define \(4A=\{4a:a\in A\}\). The generalized-dihedral group is the semidirect product with two *tagged* copies of \(A\), even if inversion on \(A\) is the identity. The medial identity is

\[
 (x*y)*(z*w)=(x*z)*(y*w)
\]

for all four entries. A quandle congruence is an equivalence relation respected by the operation and its right-division inverse, and its medialization is the smallest congruence for which the quotient satisfies the medial identity. These definitions fix both the type and the quantifiers of the assertion.

## Proof

**1. A two-type affine formula.** Identify \(R_a=(0,a)\) and \(F_a=(1,a)\), where the first coordinate belongs to \(\{0,1\}\). Direct semidirect-product multiplication, using \(x*y=y^{-1}xy\), gives

\[
 (\epsilon,a)*(\delta,b)
 =\bigl(\epsilon,(-1)^\delta a+2\epsilon b\bigr).
 \tag{1}
\]

In particular, the type of the output is the type of its first argument. The four specializations of (1) are the claimed multiplication table before quotienting.

**2. The proposed equivalence is a quandle congruence.** Define \(\theta\) to identify no two different rotations, no rotation with a reflection, and two reflections exactly when their indices differ by an element of \(4A\). Formula (1) proves compatibility: changing the first reflection index by \(4a\) changes an output reflection index by \(\pm4a\); changing a right-operand reflection index by \(4b\) changes an output reflection index by \(8b\), and does not change a rotation output. The first-operand type is preserved. The right translations are invertible on the proposed quotient: rotation right operands translate reflection indices by \(2b\), and reflection right operands negate and translate them by \(2b\); on rotation indices they act by identity or inversion. Thus the quotient is a quandle, not merely a binary magma quotient.

**3. The quotient is medial.** Write four inputs as \(x=(\alpha,a)\), \(y=(\beta,b)\), \(z=(\gamma,c)\), and \(w=(\delta,d)\), with all type variables in \(\{0,1\}\), and set \(s_j=(-1)^j\). By two applications of (1), the index of the left side of the medial identity is

\[
 s_\gamma s_\beta a+2\alpha(s_\gamma b+s_\delta c+2\gamma d),
\]

while the index of the right side is

\[
 s_\beta s_\gamma a+2\alpha(s_\beta c+s_\delta b+2\beta d).
\]

Their difference is exactly

\[
 2\alpha\bigl[(s_\gamma-s_\delta)b+(s_\delta-s_\beta)c+2(\gamma-\beta)d\bigr].
 \tag{2}
\]

Every difference of two signs \(s_j\) is even, so (2) lies in \(4A\) whenever \(\alpha=1\), and is zero when \(\alpha=0\). Both sides have output type \(\alpha\). Therefore they coincide modulo \(\theta\), establishing mediality for every abelian group \(A\), including infinite groups and groups with two-torsion.

**4. Minimality and universal property.** Consider any quandle congruence \(\rho\) for which the quotient is medial. For arbitrary \(a,b\in A\) substitute

\[
 x=F_b,\quad y=R_a,\quad z=F_0,\quad w=R_0
\]

into the medial identity. Using the operation table from (1), its left side is \(F_{-b-2a}\), and its right side is \(F_{-b+2a}\). Consequently

\[
 F_{u}\equiv_\rho F_{u+4a}
 \quad\text{for every }u,a\in A.
\]

All pairs of reflections whose indices differ by \(4A\) must therefore be identified by \(\rho\). In other words \(\theta\subseteq\rho\). Step 3 proves that \(\theta\) itself makes the quotient medial, so \(\theta\) is precisely the least medial congruence. The claimed universal factorization through \(A\sqcup(A/4A)\) follows: every homomorphism from the original quandle to a medial quandle kills \(\theta\), and the factorization is unique.

**5. Counts and boundary.** The quotient has \(|A|\) distinct rotations and \(|A/4A|\) reflection classes. For \(A\cong\bigoplus_i\mathbb Z/m_i\mathbb Z\), the size of \(A/4A\) is \(\prod_i\gcd(m_i,4)\). The congruence is trivial precisely when \(4A=0\), yielding the claimed boundary criterion. For \(A=\mathbb Z/n\mathbb Z\), the count simplifies to \(n+\gcd(n,4)\). All claims follow. \(\square\)

## Verification

Run `python3 verify.py` from this artifact directory. The script independently constructs the generalized-dihedral group multiplication and its right-conjugation quandle operation, then exhaustively generates every medial-identity pair on twelve finite abelian groups, closes those pairs under the quandle operation, and compares the resulting partition with the exact predicted equivalence classes. It returns `VERIFY_OK` when all tested instances match. Among the test groups are cyclic groups with odd and even orders and noncyclic groups, including \(\mathbb Z/2\mathbb Z\oplus\mathbb Z/4\mathbb Z\) and \((\mathbb Z/3\mathbb Z)^2\).

These finite checks do not establish the infinite-group statement; the quantified calculation in (2), together with the four-element medial witness in Step 4, supplies the general proof. No external computation or unprovided artifact is needed.

## Relationship to prior work

Bardakov and Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1, Theorem 5.4, establish that a group's conjugation quandle is medial precisely for nilpotency class at most two, give lower bounds for the medialization, and explicitly compute its four-element medialization for \(S_3\). The present result agrees with that case, since \(S_3\cong\operatorname{Dih}(\mathbb Z/3\mathbb Z)\), but supplies the complete universal quotient for every generalized dihedral group, not merely those bounds. Their \(\operatorname{Conj}(G/\gamma_3(G))\) quotient generally identifies rotations that the quandle medialization retains, so it does not give the present classification.

Fan, *Signature Modules and the Dihedral Conjugation-Quandle Counting Invariant*, arXiv:2609.13326v1, Section 3 and Theorem 10.1, provides the two-type conjugation formula and studies link-coloring modules, including general abelian rotation kernels. This algebraic setup is acknowledged; the universal medial-congruence calculation and its \(4A\) classification are not part of its link-coloring result.

Jedlička, Pilitowska, Stanovský, and Zamojska-Dzienio, *The structure of medial quandles*, arXiv:1409.8396v2, develop general affine-mesh structure theory for medial quandles. That representation applies to the **output** once a quotient is known, but does not specify the least medial congruence of the present nonmedial input family. The result here is therefore an explicit reflection computation rather than a claim of new general medial-quandle representation theory.

## Limitations

The theorem does not classify medializations of arbitrary semidirect products, arbitrary conjugation quandles, or other quandle identities. For the finite cardinalities, the invariant-factor formula assumes a chosen decomposition of the abelian rotation kernel, but the quotient itself is canonical. Comparison with unindexed older quandle literature cannot guarantee historical priority.

## References

1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (first posted 2026-10-13), especially Section 5, Theorem 5.4. https://arxiv.org/abs/2610.18676
2. Z. Fan, *Signature Modules and the Dihedral Conjugation-Quandle Counting Invariant*, arXiv:2609.13326v1 (first posted 2026-09-11), especially Sections 3 and 10. https://arxiv.org/abs/2609.13326
3. P. Jedlička, A. Pilitowska, D. Stanovský, and A. Zamojska-Dzienio, *The structure of medial quandles*, arXiv:1409.8396v2 (2015), especially Sections 2–3 and 9. https://arxiv.org/abs/1409.8396
