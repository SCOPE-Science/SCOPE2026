# Even-power conjugation quandles of generalized dihedral groups: isomorphisms and full automorphisms

## Finding

Let \(A\) be a finite abelian group, written additively, and let \(m\) be any even integer (including zero or negative values). Define \(G=\operatorname{Dih}(A)=A\rtimes C_2\), with the nonidentity element of \(C_2\) acting by inversion. On the underlying set of \(G\), use the right power-conjugation quandle operation
\[
x*y=y^{-m}xy^m.
\]
Put \(H=(2m)A\), \(d=|H|\), and \(h=|A|/d=|A[2m]|\).

**Exact operation.** Identify the rotation and reflection copies of \(A\) with \(R_a=(a,0)\) and \(F_a=(a,1)\). Then
\[
R_a*R_b=R_a*F_b=R_a,\qquad F_a*F_b=F_a,\qquad F_a*R_b=F_{a-2mb}.
\]
The inner automorphism group is naturally isomorphic to the additive group \(H\). There are \(|A|\) one-element orbits and \(h\) reflection orbits of size \(d\), with the qualification that when \(d=1\) all \(2|A|\) orbits are singletons.

**Complete automorphism group.** If \(d=1\), the operation is trivial and
\[
\operatorname{Aut}(Q)\cong S_{2|A|}.
\]
If \(d>1\), every automorphism uniquely consists of two bijections \(f,g:A\to A\) acting on rotations and reflections, respectively. These pairs are exactly those for which there exists a unique \(\alpha\in\operatorname{Aut}(H)\) satisfying
\[
(-2m)f(b)=\alpha((-2m)b),\qquad
 g(a+t)=g(a)+\alpha(t)
\quad (a,b\in A,\ t\in H).
\]
With noncanonical choices of representatives and labels, this gives
\[
\operatorname{Aut}(Q)\cong
\bigl(S_h^{\,d}\times H^{\,h}\bigr)
\rtimes\bigl(S_h\times\operatorname{Aut}(H)\bigr),
\]
where the outer \(S_h\) permutes the \(h\) copies of \(H\), and \(\operatorname{Aut}(H)\) acts diagonally on them and permutes the \(d\) factors of \(S_h\) through its natural action on \(H\). Thus the exact order is
\[
\boxed{\;|\operatorname{Aut}(Q)|
=|\operatorname{Aut}(H)|\,(h!)^{d+1}d^h\;}\qquad(d>1).
\]

**Isomorphism rigidity of the reduced data.** For two such pairs \((A,m)\) and \((A',m')\), the quandles are isomorphic if and only if \(|A|=|A'|\) and \((2m)A\cong(2m')A'\) as abelian groups. This also covers the trivial case: both image groups are trivial and the cardinalities agree. Hence the underlying groups need not be isomorphic for their quandles to be isomorphic.

For cyclic \(A\cong\mathbb Z/n\mathbb Z\), one can write \(h=\gcd(n,2m)\) and \(d=n/h\); when \(d>1\), the automorphism-group order is \(\varphi(d)(h!)^{d+1}d^h\).

## Assumptions and scope

The finite abelian group \(A\) may have arbitrary invariant factors and arbitrary even- or odd-order torsion. The integer \(m\) is even; no additional coprimality hypothesis is imposed. Throughout \(S_h\) denotes the symmetric group of degree \(h\), \(H^h\) denotes a direct power of the **additive** image group \(H\), and \(A[2m]\) is the kernel of the multiplication-by-\(2m\) map. No representation-theoretic or field hypotheses occur.

## Proof

**1. Computation of the quandle law.** In the semidirect product the group law is
\[
(a,\epsilon)(b,\delta)=(a+(-1)^\epsilon b,\epsilon+\delta\pmod2).
\]
Every reflection has order two. Since \(m\) is even, a reflection's \(m\)-th power is the identity, including for negative \(m\). A rotation \(R_b\) has \(m\)-th power \(R_{mb}\). Conjugating \(F_a\) by \(R_{mb}\) gives \(F_{a-2mb}\), while rotations commute. These observations establish the displayed operation. Its right translations are precisely the translations \(F_a\mapsto F_{a+t}\) by \(t\in H\), fixing the rotation copy pointwise; therefore the inner group is \(H\) and the orbit assertions follow.

**2. Characterizing all automorphisms.** If \(H\) is trivial, every right translation is the identity, so every permutation of the \(2|A|\) points is an automorphism. Suppose henceforth that \(d>1\). The points fixed by every element of the inner group are precisely the rotations \(R_a\), since the translation action of nonzero \(H\) is free on each reflection coset. This property is intrinsic to the quandle, so every automorphism preserves the two copies and has the form \(R_a\mapsto R_{f(a)}\), \(F_a\mapsto F_{g(a)}\) for bijections \(f,g\). The one nontrivial multiplication relation requires and is equivalent to
\[
g(a-2mb)=g(a)-2m f(b)\qquad(a,b\in A).\tag{1}
\]
Let \(\pi:A\twoheadrightarrow H\) be the additive map \(\pi(b)=-2mb\). Equation (1) implies that whenever \(\pi(b)=\pi(c)\) we have \(\pi(f(b))=\pi(f(c))\), since the two translations of \(g(a)\) coincide. Thus \(\alpha(\pi(b))=\pi(f(b))\) is well-defined. Equation (1) says \(g(a+t)=g(a)+\alpha(t)\). Applying this successively for \(t,u\in H\) proves \(\alpha(t+u)=\alpha(t)+\alpha(u)\). As \(\pi\circ f\) is surjective and \(\pi\) is surjective, \(\alpha\) is surjective, hence is an automorphism of the finite group \(H\). Uniqueness is immediate from surjectivity of \(\pi\). Conversely, both identities in the finding imply (1) and hence preservation of every product.

**3. Counting and group structure.** Fix \(\alpha\in\operatorname{Aut}(H)\). Each of the \(d\) fibers of \(\pi\) has size \(h\), so \(f\) may map each fiber bijectively onto the fiber indexed by its \(\alpha\)-image, independently in \(h!\) ways. Hence there are \((h!)^d\) possible \(f\). For \(g\), \(A\) is a disjoint union of \(h\) free transitive \(H\)-sets (cosets of \(H\)). An \(\alpha\)-equivariant bijection chooses a permutation of these \(h\) cosets, then an arbitrary image of one representative in each target coset (\(d\) choices per coset), and the equivariance fixes its values elsewhere. Thus there are \(h!d^h\) possible \(g\). Multiplying by \(|\operatorname{Aut}(H)|\) yields the formula.

To identify the abstract group, choose a label set of cardinality \(h\) for each fiber of \(\pi\) and a representative for each \(H\)-coset in \(A\). Then every automorphism corresponds to \((\alpha,(\sigma_t)_{t\in H},\rho,(u_c)_{c=1}^{h})\) with \(\sigma_t\in S_h\), \(\rho\in S_h\) and \(u_c\in H\). The subgroup with \(\alpha=1\) and \(\rho=1\) is \(S_h^d\times H^h\); the subgroup with all \(\sigma_t=1\) and all \(u_c=0\) is \(S_h\times\operatorname{Aut}(H)\). The evident actions are those specified in the finding, proving the semidirect product (the choices make this identification noncanonical).

**4. Isomorphism classification.** Any isomorphism preserves the total number of elements, so \(|A|=|A'|\), and conjugates their intrinsic inner automorphism groups, so \(H\cong H'\). Conversely, suppose these two conditions hold, choose a group isomorphism \(\alpha:H\to H'\), and note that the maps \(\pi:A\to H\) and \(\pi':A'\to H'\) have fibers of the same size \(h\). Choose any bijection \(f:A\to A'\) matching each \(\pi\)-fiber with the \(\alpha\)-corresponding \(\pi'\)-fiber. Both reflection layers are disjoint unions of \(h\) free transitive actions of \(H\) and \(H'\), respectively, so choose an \(\alpha\)-equivariant bijection \(g:A\to A'\) by matching the orbits and sending representatives arbitrarily. Then \((R_a\mapsto R'_{f(a)},F_a\mapsto F'_{g(a)})\) respects all products by (1). If \(H=1\), both quandles are trivial, and any bijection works. This proves necessity and sufficiency.

## Verification

The standalone `check.py` constructs the generalized-dihedral multiplication, powers, conjugation operation, and right translations without using the derived quandle formula as input. It compares the latter to the symbolic law on twelve finite abelian-group/exponent configurations, including negative and zero even exponents, including groups with two-primary torsion and noncyclic groups. In the nine small configurations, it checks the automorphisms using all permutations of the intrinsically distinguishable layers (or the entire symmetric group when the quandle is trivial) and compares their number with the theorem. In the larger configurations it checks the group law, formula, and induced automorphisms but does not exhaust all possible quandle automorphisms. The exact order in all degrees follows from the proof, not the finite tests. Execute `python3 check.py` from this directory and compare its output with `output.txt`.

## Relationship to prior work

Sangare (arXiv:2602.03080, first public February 3, 2026), Section 2, studies when group automorphisms and antiautomorphisms induce automorphisms of power-conjugation quandles, and provides general subgroups of their automorphism groups. It does not supply the complete even-power generalized-dihedral count or isomorphism criterion. Bardakov and Sangare (arXiv:2610.18676, first public October 13, 2026; primary MSC2020 20N02) classify automorphisms of certain Alexander quandles and analyze other conjugation-quandle constructions, but do not derive the present formula. Bardakov–Nasybullov–Singh (arXiv:1705.10607) treat **ordinary** conjugation quandles and their automorphism subgroups. Salix–Wood (arXiv:2510.26673) provide general small-quandle automorphism census results, rather than an all-order group-theoretic classification of this family. The known general statements and finite tabulations are not claimed as new. The contribution is the all-order exact even-power family classification.

## Limitations

The classification applies to **even** powers of conjugation in generalized dihedral groups with finite abelian rotation subgroup. Odd exponents do not obey the displayed operation. No claim about power-conjugation quandles of arbitrary nonabelian groups is made. Historical priority is qualified: an equivalent result might exist under the terminology of permutation quandles, constant-action orbit quandles, or translation-set quandles. The finite tests are corroborative and do not certify the infinite theorem or originality.

## References

1. B. Sangare, *Automorphisms and antiautomorphisms of quandles*, arXiv:2602.03080, originally posted February 3, 2026, https://arxiv.org/abs/2602.03080 .
2. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676, originally posted October 13, 2026, https://arxiv.org/abs/2610.18676 .
3. V. G. Bardakov, T. R. Nasybullov and M. Singh, *Automorphism groups of quandles and related groups*, arXiv:1705.10607, https://arxiv.org/abs/1705.10607 .
4. Q. J. M. Salix and P. P. Wood, *More Automorphism Groups of Quandles*, arXiv:2510.26673, https://arxiv.org/abs/2510.26673 .
