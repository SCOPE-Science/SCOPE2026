# A one-dimensional two-local derivation defect for free two-step nilpotent Lie algebras

## Finding

Let \(k\) be any field of characteristic different from \(2\), and let \(V\) be a vector space of dimension \(m\geq 3\). Give
\[
L(V)=V\oplus\bigwedge^2 V
\]
the Lie bracket \([v,w]=v\wedge w\), with \(\bigwedge^2V\) central. A **linear 2-local derivation** is a \(k\)-linear map \(\Delta:L(V)\to L(V)\) such that, for every ordered pair \(x,y\), there exists a single ordinary derivation \(D_{x,y}\) satisfying both \(\Delta(x)=D_{x,y}(x)\) and \(\Delta(y)=D_{x,y}(y)\).

Define \(S(v+z)=z\) for \(v\in V\), \(z\in\bigwedge^2V\). Then the **complete classification** is
\[
\operatorname{2LocDer}_{\mathrm{lin}}(L(V))
=\operatorname{Der}(L(V))\oplus kS.
\]
The summands are disjoint and the left side is a vector space. Equivalently every linear 2-local derivation has the unique expression
\[
\Delta(v+z)=Bv+f(v)+B^{[2]}z+\lambda z,
\quad B\in\operatorname{End}_k(V),\quad
f\in\operatorname{Hom}_k(V,\bigwedge^2V),\quad\lambda\in k,
\]
where \(B^{[2]}(v\wedge w)=Bv\wedge w+v\wedge Bw\). Consequently
\[
\dim_k\operatorname{2LocDer}_{\mathrm{lin}}(L(V))
=\frac{m^2(m+1)}2+1,
\qquad
\dim_k\operatorname{Der}(L(V))=\frac{m^2(m+1)}2.
\]
The inclusions
\[
\operatorname{Der}(L(V))\subsetneq\operatorname{2LocDer}_{\mathrm{lin}}(L(V))
\subsetneq\operatorname{LocDer}_{\mathrm{lin}}(L(V))
\]
are strict for every \(m\geq3\). Moreover, when \(m=3\), every linear endomorphism of \(L(V)\) preserving its three-dimensional center is local, and
\[
\dim\operatorname{LocDer}_{\mathrm{lin}}(L(V))=27,
\quad\dim\operatorname{2LocDer}_{\mathrm{lin}}(L(V))=19,
\quad\dim\operatorname{Der}(L(V))=18.
\]
The two-generator boundary is the three-dimensional Heisenberg algebra, for which all center-preserving linear maps are 2-local and its dimensions are \(7,7,6\), respectively; this boundary case is provided for comparison, not asserted as a new classification.

## Assumptions and scope

All quantifiers range over arbitrary (not necessarily algebraically closed or infinite) fields of characteristic other than two, all integers \(m\geq3\), all linear maps \(\Delta\), and every ordered pair of elements of the free class-two nilpotent Lie algebra \(L(V)\). The term 2-local refers to simultaneous evaluation at **two inputs**, not to continuity or to preserving a Lie product at a single input. No classification is asserted for nonadditive or nonlinear 2-local maps, arbitrary two-step quotient Lie algebras, or characteristic two. The explicit formula for the full local-derivation dimension is only claimed for \(m=3\).

## Proof

**Ordinary derivations.** For \(m\geq2\), \(Z(L)=[L,L]=\bigwedge^2V\): if \(v\ne0\) one may choose \(w\) independent of \(v\), so \([v,w]\ne0\). Every derivation preserves the center. Writing its block action on the complement as \(D(v)=Bv+f(v)\), the Leibniz rule on \([v,w]=v\wedge w\) forces
\[
D(z)=B^{[2]}z,\qquad B^{[2]}(v\wedge w)=Bv\wedge w+v\wedge Bw.
\]
Conversely every such pair \((B,f)\) defines a derivation, because the central brackets vanish. The dimension is \(m^2+m\binom m2\).

**Distinguished-vector bivector lemma.** For any nonzero \(v\in V\) and any \(z\in\bigwedge^2V\), there exists \(C\in\operatorname{End}(V)\) such that
\[
Cv=0,\qquad C^{[2]}z=z.
\]
Indeed, the alternating normal form of a bivector gives a direct-sum decomposition \(V=E\oplus F\) with \(z\in E\wedge F\) and \(v\in E\): first take symplectic pairs \((a_i,b_i)\) spanning the image of the contraction map of \(z\). If \(v\) belongs to that image, choose the first symplectic basis vector \(a_1=v\) and extend to a symplectic basis; otherwise choose a complement of the image containing \(v\). In either case, put every \(a_i\) and the remaining complementary vectors into \(E\), and every \(b_i\) into \(F\). The projection \(C\) onto \(F\) along \(E\) kills \(v\), while on every \(a_i\wedge b_i\) it acts as the identity under \(C^{[2]}\). This also covers \(z=0\).

**The extra 2-local map.** Show \(S(v+z)=z\) is 2-local. Fix \(x=v+z\) and \(y=w+t\). If \(v,w\) are linearly independent, use the derivation with \(B=0\) and choose \(f(v)=z\), \(f(w)=t\). If both are zero, use \(B=\tfrac12\operatorname{id}_V\), so \(B^{[2]}=\operatorname{id}_{\bigwedge^2V}\). Otherwise, after interchanging the inputs if necessary, write \(v\ne0\), \(w=av\). Apply the preceding lemma to \(t-az\), obtaining \(Bv=0\) and \(B^{[2]}(t-az)=t-az\). Choose \(f(v)=z-B^{[2]}z\), extended linearly. Then the associated derivation sends \(x\) to \(z\) and \(y\) to \(t\), as required. Since the sum of an ordinary derivation and a scalar multiple of a 2-local derivation is 2-local, every displayed formula is 2-local.

**Necessity of the displayed formula.** A linear 2-local map is local (pair its input with zero), so it preserves \(Z(L)\), as every derivation does. Thus \(\Delta(v+z)=Bv+f(v)+Tz\) for some \(B,f,T\). Fix nonzero \(v\in V\) and arbitrary \(z\in\bigwedge^2V\). Applying 2-locality to \(v\) and \(v+z\) gives one derivation \(D_{A,g}\) with \(Av=Bv\) and \(A^{[2]}z=Tz\): the two equations have the same \(g(v)\) term, which cancels. Hence for \(R=T-B^{[2]}\), and \(C=A-B\),
\[
Cv=0,\qquad Rz=C^{[2]}z.
\]
For independent \(v,w\), take \(z=v\wedge w\). It follows that \(Rz\in v\wedge V\). Repeating with \(w\) in place of \(v\) gives \(Rz\in w\wedge V\). Their intersection equals \(k(v\wedge w)\); therefore **every nonzero decomposable bivector is an eigenvector of \(R\)**. To show the eigenvalue is constant, choose a basis \(e_1,\ldots,e_m\). Then \(R(e_i\wedge e_j)=\lambda_{ij}(e_i\wedge e_j)\). Since \(e_i\wedge(e_j+e_k)\) is decomposable, \(\lambda_{ij}=\lambda_{ik}\) for distinct \(i,j,k\); the connectedness of the index-pair graph for \(m\ge3\) gives one scalar \(\lambda\) on all basis bivectors. Thus \(R=\lambda\operatorname{id}\), proving the classification and its uniqueness. Finally \(S\) is not a derivation, since it kills every generator \(v\) but does not kill their brackets.

**Strictness and the three-generator local census.** Take a rank-one projection \(P:V\to V\), and define \(\Theta(v+z)=Pv\). This is local: at an input with \(v\ne0\), choose a derivation with quotient action \(P\), and choose its free central map \(f_v\) to cancel \(P^{[2]}z\); for purely central inputs use the zero derivation. But when \(m\ge3\), \(P^{[2]}\) is neither zero nor scalar (it acts by one on \(e_1\wedge e_i\) and by zero on \(e_i\wedge e_j\) for \(i,j>1\)). Necessity therefore excludes \(\Theta\) from the 2-local class.

When \(m=3\) and the characteristic is not two, the action map \(\operatorname{End}(V)\to\operatorname{End}(\bigwedge^2V)\), \(A\mapsto A^{[2]}\), is a vector-space isomorphism: relative to a volume form it is conjugate to \(A\mapsto(\operatorname{tr}A)I-A^{\mathsf T}\), whose inverse exists because \(2\) is invertible. Any center-preserving map \((B,f,T)\) is therefore local. For a central input, use a derivation with \(A^{[2]}=T\). For a noncentral input \(v+z\), choose any \(A\) satisfying \(Av=Bv\), then freely prescribe \(g(v)=f(v)+Tz-A^{[2]}z\). Conversely locality preserves the center. Counting block coefficients gives \(9+9+9=27\).

For the boundary \(m=2\), the center has dimension one; every center-preserving map has \(T=B^{[2]}+\lambda I\), so the above construction proves it 2-local. Its dimension is \(4+2+1=7\).

## Verification

The accompanying independent finite-field verifier `checker.py` builds the derivation action matrices directly from the generator brackets, solves simultaneous linear witness equations over each tested prime field, and tests the central projection \(S\) against ordered pairs. It exhausts all \(27^2=729\) ordered pairs in the two-generator algebra over \(\mathbb F_3\); it also checks 2,500 sampled pairs in rank three over \(\mathbb F_3\), 600 in rank three over \(\mathbb F_5\), and 350 in rank four over \(\mathbb F_3\). It directly detects a pair with no common derivation witness for \(\Theta\) in each rank at least three.

The second checker, `rank_check.py`, constructs linear constraints on **all linear endomorphisms** that follow from simultaneous two-point witnesses. Already 16 sampled ordered pairs in rank three over \(\mathbb F_3\) give 17 independent constraints on the 36-dimensional full endomorphism space, leaving dimension 19. Analogous independent constraint ranks are 2, 17 and 59 for ranks and fields \((2,3)\), \((3,5)\), and \((4,3)\), giving dimensions 7, 19 and 41. Because the constructive proof supplies a 2-local subspace of the corresponding full predicted dimension, these finite-field rank checks are exhaustive for the **linear-map space** despite using only a subset of ordered input pairs. The infinite-field theorem rests on the proof, not the sampling.

Run with a Python 3 interpreter, without third-party packages: `python checker.py` and `python rank_check.py` (the latter imports the former from the same directory). Output records are in `checks.txt`.

## Relationship to prior work

Bardakov and Singh, *Extensions and automorphisms of Lie algebras*, arXiv:1508.01850v1 (first public date 2015-08-08), treat the free class-two Lie algebra and the induced exterior-square action for automorphisms, not the present linear two-local derivation space. Ayupov and Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939v1 (2015-08-17), establish the local-vs-global distinction and provide filiform examples, but no classification of linear two-local maps on the free class-two family. The 2015 article by Ayupov, Kudaybergenov and Rakhimov, *2-Local derivations on finite-dimensional Lie algebras*, gives general existence of nonglobal 2-local maps in nilpotent Lie algebras; its full text was not available for this comparison. Khudoyberdiyev and Jumaniyozov, arXiv:2405.04209v1 (2024-05-07), construct proper local derivations in all two-step nilpotent Lie algebras, including projections related to \(S\). Atajonov, Khudoyberdiyev and Yusupov, arXiv:2610.40348v1 (2026-10-29), generalize **existence** of proper local maps; their inspected theorem does not classify linear 2-local maps on this family. The new assessed statement is the complete one-dimensional **two-point** defect and strict local/2-local hierarchy for all generator ranks at least three over odd-characteristic fields, not the existence of a central projection alone. The rank-two Heisenberg boundary agrees with prior classifications and is not asserted as new.

## Limitations

The proof excludes characteristic two because simultaneous central inputs are witnessed by the half-scaling derivation; the characteristic-two classification is not claimed. It does not classify nonlinear 2-local maps, all linear local maps for generator ranks greater than three, or arbitrary two-step nilpotent quotients. Some older literature, especially the full text of the 2015 general 2-local derivations article, could contain a stronger implication; historical priority therefore remains provisional. These statements have not undergone independent mathematical review.

## References

1. V. G. Bardakov and M. Singh, *Extensions and automorphisms of Lie algebras*, arXiv:1508.01850v1 (2015-08-08), https://arxiv.org/abs/1508.01850 .
2. S. Ayupov and K. Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939v1 (2015-08-17), https://arxiv.org/abs/1508.03939 .
3. S. Ayupov, K. Kudaybergenov and I. Rakhimov, *2-Local derivations on finite-dimensional Lie algebras*, Linear Algebra and its Applications 474 (2015), 1–11, https://doi.org/10.1016/j.laa.2015.01.016 .
4. A. Khudoyberdiyev and D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebra*, arXiv:2405.04209v1 (2024-05-07), https://arxiv.org/abs/2405.04209 .
5. K. Atajonov, A. Khudoyberdiyev and B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (2026-10-29), https://arxiv.org/abs/2610.40348 .
