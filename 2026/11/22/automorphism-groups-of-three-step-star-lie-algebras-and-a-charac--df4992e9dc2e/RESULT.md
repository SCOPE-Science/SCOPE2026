# Automorphism groups of three-step star Lie algebras and a characteristic-two symmetry jump

## Finding

Let \(m\ge3\), let \(k=\mathbb F_q\) be any finite field, and put \(w=\binom m2\). For the class-three Lie algebra \(L_m(k)\) attached to the star \(K_{1,m}\), its full group of \(k\)-linear Lie automorphisms has order

\[
|\operatorname{Aut}_k(L_m(k))|=q^{(m+1)(w+1)}(q-1)\begin{cases}m!(q-1)^m,&\operatorname{char} k\ne2,\\\prod_{i=0}^{m-1}(q^m-q^i),&\operatorname{char} k=2.\end{cases}
\]

More structurally, its action on \(L_m/[L_m,L_m]\) is precisely the block-diagonal group \(k^\times\times H_m(k)\), where \(H_m(k)\) is the monomial subgroup of \(\operatorname{GL}_m(k)\) in odd characteristic and all of \(\operatorname{GL}_m(k)\) in characteristic two. The kernel has order \(q^{(m+1)(w+1)}\) in both characteristics. Thus the characteristic-two linear symmetry enlargement is exact, not merely the existence of extra automorphisms.

## Assumptions and scope

The algebra has \(k\)-basis \(h,u_1,\dots,u_m,a_1,\dots,a_m,w_{ij}\ (1\le i<j\le m)\), with \(w_{ji}=w_{ij}\). Its only nonzero brackets among basis vectors, up to antisymmetry, are

\[
[h,u_i]=a_i,\qquad [u_i,a_j]=w_{ij}\quad(i\ne j),
\]

with \([u_i,a_i]=0\) and the \(w_{ij}\) central. This is the star specialization of the vertex/edge/two-path construction of Gallo and Videla [1]. In particular \(L_m'=A\oplus W\), \([L_m,L_m']=W\), \(Z(L_m)=W\), and \(\dim L_m=1+2m+w\). Brackets and automorphisms are over \(k\); this result does not assert a formula for other graphs or for nonlinear group automorphisms.

## Proof

Set \(V=L_m/L_m'\), with the images of \(h,u_1,\ldots,u_m\) as basis, and let \(U\subset V\) be the span of the leaf images. The induced \(L_m'/W\)-valued bracket satisfies

\[
[\alpha h+u,\beta h+v]\pmod W=\alpha v-\beta u\quad(u,v\in U),
\]

where \(A=L_m'/W\) is identified with \(U\). Every subspace on which this bracket vanishes and which contains a vector with nonzero \(h\)-coefficient has dimension at most one. Hence, for \(m\ge2\), \(U\) is the unique isotropic subspace of dimension at least two that is maximal by inclusion. It is characteristic. Every automorphism therefore acts on \(V\) in the form

\[
h\longmapsto\lambda h+t,\qquad u\longmapsto Mu,
\]

with \(\lambda\in k^\times\), \(t\in U\), and \(M\in\operatorname{GL}_m(k)\). Choose arbitrary lifts \(h'=\lambda h+t+b+z\) and \(u'_i=Mu_i+b_i+z_i\) with \(b,b_i\in A\) and \(z,z_i\in W\). Since \([h,[h,u_i]]=0\), the relation \([h',[h',u'_i]]=0\) reduces to \(\lambda[t,Ma_i]=0\) in \(W\). The bilinear pairing \(U\times A\to W\) has zero left radical for \(m\ge2\): if a nonzero coefficient of \(t\) occurs at index \(i\), pair \(t\) with an \(a_j\) for \(j\ne i\) to obtain a nonzero \(w_{ij}\)-coefficient. Because \(M\) is invertible, \(t=0\). Thus the quotient action is block diagonal.

Next use the defining identity \([u,[h,u]]=0\) for every basis leaf \(u_i\). For \(u=\sum x_i u_i\),

\[
[u,[h,u]]=2\sum_{i<j}x_ix_jw_{ij}.
\]

In odd characteristic its zero locus in \(U\) is exactly the union of the \(m\) coordinate axes. The induced map \(M\) must preserve this union, hence maps the coordinate axes bijectively to themselves and is monomial. In characteristic two the identity vanishes identically, so this condition imposes no restriction.

Every candidate in these stated groups actually lifts. Given \(\lambda\ne0\) and \(M\) monomial (odd characteristic) or arbitrary invertible (characteristic two), define \(h'=\lambda h\), \(u'_i=\sum_j M_{ji}u_j\), and determine \(a'_i=[h',u'_i]\), \(w'_{ij}=[u'_i,a'_j]\). The defining relations are preserved: \([u'_i,u'_j]=[h',a'_i]=0\), and \([u'_i,a'_i]=0\) follows from monomiality when \(2\ne0\), and from the factor \(2\) when \(2=0\). Moreover the action on \(W\) is \(\lambda\bigwedge^2 M\), which is invertible. These images thus extend to an automorphism. The quotient image is exactly \(k^\times\times H_m(k)\).

It remains to count the kernel of the action on \(V\). Such an automorphism has generator lifts

\[
h'=h+b+z,\qquad u'_i=u_i+\sum_{k=1}^m c_{ki}a_k+z_i,
\]

with arbitrary \(b\in A\), \(z,z_i\in W\), subject only to \([u'_i,u'_j]=0\). Fix three distinct indices \(i,j,k\). The coefficient of \(w_{ik}\) in this relation forces \(c_{kj}=0\), so every off-diagonal \(c_{kj}\) is zero since \(m\ge3\). The coefficient of \(w_{ij}\) then forces \(c_{ii}=c_{jj}\). Hence the matrix \((c_{ki})\) is \(cI\), with one free scalar \(c\in k\). Conversely \(h'=h+b+z\), \(u'_i=u_i+ca_i+z_i\) preserve all brackets, and induce the identity on \(V\) and on the highest central layer; they are automorphisms because their induced maps on the lower central filtration are identities. The independent parameters are \(m\) coordinates of \(b\), \((m+1)w\) central coordinates of \(z,z_i\), and one scalar \(c\). Consequently

\[
|\ker(\operatorname{Aut}(L_m)\to\operatorname{GL}(V))|=q^{m+(m+1)w+1}=q^{(m+1)(w+1)}.
\]

Multiplying by \((q-1)|H_m(k)|\), with \(|H_m(k)|=m!(q-1)^m\) or \(|\operatorname{GL}_m(q)|\), proves the formula. All deductions hold over arbitrary finite fields of the asserted characteristic, including nonprime fields.

## Verification

The accompanying standalone `verify_star_aut.py` implements the bracket on the \(1+2m+w\) basis elements, checks every defining bracket after 30 seeded random automorphism lifts for each of \((q,m)=(2,3),(2,4),(3,3),(3,4),(5,3)\), and computes the exact linear constraint rank for the kernel over these fields. Its exhaustive enumeration of all \(2^9\) and \(3^9\) three-by-three matrices confirms 168 allowed invertible leaf actions over \(\mathbb F_2\) and 48 over \(\mathbb F_3\). This finite computation checks the proof but does not substitute for the all-field argument above. The checker is deterministic and uses only the Python standard library.

## Relationship to prior work

Gallo and Videla [1], first submitted 2026-10-25 UTC, introduce the class-three graph Lie construction, explicitly discuss star brackets in Section 3, derive the lower-central dimensions, and prove graph-isomorphism rigidity in characteristic not two. Their results do not state a full automorphism-group order for stars or the exact characteristic-two quotient-action jump. In particular, isomorphism rigidity between two different graph Lie algebras does not determine the automorphism group of any fixed algebra. Chakrabarti, Mainkar and Swiatlowski [2] analyze automorphisms in a distinct class-two construction based on edge-colored complete graphs; that narrower graph setting and nilpotency class do not imply this class-three star formula. Related graph Lie algebra automorphism frameworks remain possible historical overlap risks; these have not been ruled out exhaustively.

## Limitations

This theorem is restricted to branching stars with \(m\ge3\). The kernel constraint has different dimension for \(m=2\). The proof concerns field-linear Lie automorphisms, not Lie group, abstract group, derivation, or Lie algebra scheme automorphisms. The result is a direct algebraic proof with finite computational cross-checks, not a machine-certified theorem. Historical priority relative to unindexed or inaccessible structural classifications is provisional. No independent mathematical audit has been performed.

## References

[1] A. L. Gallo and D. E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1 (first public 2026-10-25), https://arxiv.org/abs/2610.33963 .

[2] D. Chakrabarti, M. Mainkar, and S. Swiatlowski, *Automorphism Groups of nilpotent Lie algebras associated to certain graphs*, arXiv:1812.09439 (2018), https://arxiv.org/abs/1812.09439 ; *Communications in Algebra* 48 (2020), 263–273, https://doi.org/10.1080/00927872.2019.1640239 .
