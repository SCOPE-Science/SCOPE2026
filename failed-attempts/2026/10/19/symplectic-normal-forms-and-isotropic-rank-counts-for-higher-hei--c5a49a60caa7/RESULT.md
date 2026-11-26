# Symplectic normal forms and isotropic-rank counts for higher Heisenberg group Rota–Baxter operators

## Finding

For every odd prime \(p\) and every \(m\geq2\), all weight-one Rota–Baxter operators on the extraspecial exponent-\(p\) Heisenberg group of order \(p^{2m+1}\) have a unique symplectic-matrix normal form. In two extreme central-character strata, the exact rank-refined numbers of operators are given by counts of isotropic Grassmannians and linear surjections.

Fix a \(2m\)-dimensional space \(V=\mathbb F_p^{2m}\) with nondegenerate alternating form \(\omega\). Define \(H(V)=V\times\mathbb F_p\) with product
\[
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
A map \(B:H(V)\to H(V)\) satisfies the group Rota–Baxter identity when
\[
B(g)B(h)=B\bigl(gB(g)hB(g)^{-1}\bigr)
\qquad(g,h\in H(V)).
\]
All such maps are uniquely
\[
\boxed{B(v,z)=\bigl(Av,cz+\ell(v)-\tfrac c2\omega(Av,v)\bigr)},
\]
where \(A\in\operatorname{End}_{\mathbb F_p}(V)\), \(c\in\mathbb F_p\), and \(\ell\in V^*\), subject exactly to
\[
\boxed{(1+c)\omega(Av,Aw)=c\,\omega((I+A)v,(I+A)w)
\quad\text{for all }v,w\in V.}
\tag{1}
\]
Equivalently, for a matrix \(J\) representing \(\omega\), \((1+c)A^{\mathsf T}JA=c(I+A)^{\mathsf T}J(I+A)\).

For \(c=0\), the allowed \(A\)'s are exactly those with totally isotropic image. For \(c=-1\), the allowed \(A\)'s are exactly those for which \(\operatorname{im}(I+A)\) is totally isotropic. Set \(r=\operatorname{rank}A\) in the former stratum and \(r=\operatorname{rank}(I+A)\) in the latter. For each \(0\leq r\leq m\), the number of distinct operators **in each stratum** is
\[
\boxed{p^{2m}\,
\frac{\prod_{i=0}^{r-1}(p^{2m-i}-p^i)}{\prod_{i=0}^{r-1}(p^r-p^i)}
\prod_{i=0}^{r-1}(p^{2m}-p^i).}
\tag{2}
\]
Empty products are \(1\). No operators in these two strata have larger corresponding rank.

As a further description of a generic component, if \(c\notin\{0,-1\}\) and \(I+A\) is invertible, then \(T=A(I+A)^{-1}\) lies in the group of symplectic similitudes with multiplier \(c/(1+c)\), and \(I-T\) is invertible. Conversely every such \(T\) defines \(A=T(I-T)^{-1}\). No invertibility assumption is made in the main classification.

## Assumptions and scope

The characteristic is odd, \(p\) is prime, \(m\geq2\), and the group law and group Rota–Baxter convention are precisely those displayed above. Operators are counted as maps, not up to conjugacy or equivalence. The two exceptional strata are disjoint for odd \(p\). The central parameter \(c\) and linear parameter \(\ell\) range freely subject only to equation (1), which contains no \(\ell\).

## Proof

**Step 1: the center is preserved.** Taking the second argument to be the identity in the Rota–Baxter equation forces \(B(e)=e\). Let \(z\) denote a fixed nonidentity central generator, and set \(t=B(z)\). The Rota–Baxter identity with a central second argument gives \(B(gz^j)=B(g)t^j\) for every \(g\) and integer \(j\). In particular \(B(z^j)=t^j\). Applying the identity instead with \(g=z\) and arbitrary \(h\), write \([t,h]=z^k\); then
\[
tB(h)=B(zh[t,h])=B(h)t^{1+k}.
\]
The left commutator \([t,B(h)]\) is central because the group has nilpotency class two. Taking the quotient by the center shows \(k\bar t=0\) in the elementary abelian quotient. If \(t\) were noncentral, nondegeneracy of \(\omega\) would give \(h\) with \(k\ne0\), a contradiction. Therefore \(t\) is central, and \(B(0,z)=(0,cz)\) for a uniquely determined \(c\in\mathbb F_p\).

**Step 2: linearity on the quotient.** Modulo the center, \(gB(g)hB(g)^{-1}\) equals the product of the quotient classes of \(g,h\). Consequently the quotient map of \(B\) is a homomorphism of the additive group \(V\), hence an \(\mathbb F_p\)-linear map \(A\). Using \(B((v,z)(0,t))=B(v,z)B(0,t)\), write \(B(v,z)=(Av,cz+Q(v))\) for a unique \(Q:V\to\mathbb F_p\) satisfying \(Q(0)=0\).

**Step 3: the central equation.** For \(g=(v,z)\), \(h=(w,t)\), the right input to \(B\) is
\[
(v+w,z+t+\omega(Av,w)+\tfrac12\omega(v,w)).
\]
Comparison of central coordinates gives
\[
Q(v+w)-Q(v)-Q(w)
=\tfrac12\omega(Av,Aw)-c\omega(Av,w)-\tfrac c2\omega(v,w).
\tag{3}
\]
The left side is symmetric in \(v,w\). Antisymmetrizing (3) gives precisely (1). Under (1), the right side of (3) simplifies to
\[
-\tfrac c2\bigl(\omega(Av,w)+\omega(Aw,v)\bigr),
\]
which is the polarization of \(Q_0(v)=-\tfrac c2\omega(Av,v)\). Thus \(Q-Q_0\) is additive and equals a unique \(\mathbb F_p\)-linear functional \(\ell\). Conversely these formulas imply (3), hence the full Rota–Baxter identity. This proves necessary-and-sufficient parametrization and uniqueness.

**Step 4: exact counts.** When \(c=0\), (1) is \(\omega(Av,Aw)=0\), equivalent to \(\operatorname{im}A\) totally isotropic. When \(c=-1\), (1) is \(\omega((I+A)v,(I+A)w)=0\), giving the second statement. An \(r\)-dimensional totally isotropic subspace is determined by an ordered isotropic independent \(r\)-frame modulo \(\operatorname{GL}_r(\mathbb F_p)\). The number of such frames is
\[
\prod_{i=0}^{r-1}(p^{2m-i}-p^i),
\]
while the number of ordered bases of its \(r\)-space is \(\prod_{i=0}^{r-1}(p^r-p^i)\). For each isotropic image, the number of surjections \(V\to U\) is \(\prod_{i=0}^{r-1}(p^{2m}-p^i)\). Finally \(\ell\) has \(p^{2m}\) choices. For \(c=-1\), translation \(A\mapsto I+A\) bijects the two matrix sets and preserves the analogous rank. This yields (2). Since a totally isotropic subspace has dimension at most \(m\), higher ranks do not occur.

**Step 5: optional similitude chart.** For \(c\ne0,-1\) and invertible \(I+A\), multiply (1) on both sides by \((I+A)^{-1}\), obtaining \(T^{\mathsf T}JT=(c/(1+c))J\), with \(T=A(I+A)^{-1}\) and \(I-T=(I+A)^{-1}\). All steps are reversible.

## Verification

A dependency-free exact-arithmetic checker is supplied as `verify_rb_heisenberg.py`. It tests all \(2{,}187\) parameter triples \((A,c,\ell)\) for \(m=1,p=3\) against the group identity for all \(27^2\) ordered group-element pairs, confirming the correct specialization to the previously studied rank-one case. It checks \(18\) parameter choices with \(m=2,p=3\) against all \(243^2\) pairs and checks \(1{,}000\) deterministic pairs for a nondegenerate \(m=2,p=5\) case. It independently computes the isotropic-rank factors: at \(p=3,m=2\), the numbers of matrices of ranks \(0,1,2\) are \(1,3{,}200,249{,}600\). Therefore each exceptional central-character stratum has \(81\), \(259{,}200\), \(20{,}217{,}600\) operators in the three respective ranks. These finite checks corroborate but do not replace the proof.

Run: `python verify_rb_heisenberg.py`.

## Relationship to prior work

Savelyev, *Rota—Baxter operators on extraspecial groups* (arXiv:2608.28291v1, public August 28, 2026), establishes center preservation and classifies the extraspecial groups of order \(p^3\), including the three-dimensional finite Heisenberg group. Its rank-one matrix identity agrees with (1) when \(m=1\). Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group* (arXiv:2402.15428, public February 23, 2024), concerns the three-dimensional Heisenberg Lie algebra and associated group. Neither inspected source supplies the higher-rank \(m\ge2\) universal matrix parametrization together with its two exact isotropic-rank distributions. The general operator definition and the link with brace theory are prior results.

## Limitations

The classification does not cover characteristic two or exponent-\(p^2\) extraspecial groups, and formula (2) does not enumerate all operators for \(c\notin\{0,-1\}\); equation (1) still classifies them exactly. The result is not a conjugacy classification or a count of brace isomorphism classes. The new proof is self-contained; the experimental checker is not an independent proof for unbounded parameters. Possible unindexed equivalent higher-rank classification remains a bibliographic risk. Independent review has not been performed.

## References

1. Andrey Savelyev, *Rota—Baxter operators on extraspecial groups*, arXiv:2608.28291v1 (August 28, 2026), https://arxiv.org/abs/2608.28291.
2. Nishant Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (February 23, 2024), https://arxiv.org/abs/2402.15428.
3. L. Guo, H. Lang, Y. Sheng, foundational definition of group Rota–Baxter operators, as cited in the two papers above.
