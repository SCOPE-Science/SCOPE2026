# Complete local-derivation spaces of free two-step nilpotent Lie algebras

## Finding
For a field \(K\) with \(\operatorname{char}K\ne2\) and an integer \(n\ge4\), let \(V=K^n\), \(W=\bigwedge^2 V\), and \(L=V\oplus W\). Define the Lie bracket by \([u+w,v+z]=u\wedge v\). This is the free two-step nilpotent Lie algebra on \(n\) generators.

A **local derivation** means a **linear** map \(\Delta:L\to L\) such that for each \(x\in L\), some (possibly \(x\)-dependent) ordinary derivation \(D_x\) satisfies \(D_x(x)=\Delta(x)\). For \(A\in\operatorname{End}_K(V)\), denote its exterior-square **Lie action** by
\[
 R(A)(u\wedge v)=Au\wedge v+u\wedge Av.
\]
This is not the functorial map \(u\wedge v\mapsto Au\wedge Av\).

**Theorem.** Every local derivation, and only a local derivation, is uniquely
\[
 \Delta_{P,Q,A}(v+z)=Pv+Qv+R(A)z,
 \qquad P,A\in\operatorname{End}_K(V),\quad Q\in\operatorname{Hom}_K(V,W).
\]
The three parameters are independent. Such a map is an ordinary derivation precisely when \(P=A\). Consequently
\[
 \dim_K\operatorname{LocDer}(L)=2n^2+n\binom n2,\quad
 \dim_K\operatorname{Der}(L)=n^2+n\binom n2,\quad
 \dim_K(\operatorname{LocDer}(L)/\operatorname{Der}(L))=n^2.
\]
Over every odd-order finite field \(\mathbb F_q\), the respective numbers of local and ordinary derivations are \(q^{2n^2+n\binom n2}\) and \(q^{n^2+n\binom n2}\).

## Assumptions and scope
The field is arbitrary except for \(2\ne0\), not necessarily algebraically closed. The rank is \(n\ge4\); the theorem does not assert classification for rank \(2\) or \(3\), or characteristic \(2\). The center and derived ideal both equal \(W\). No Lie-group or analytic hypothesis is used.

## Proof
**1. Ordinary derivations.** Because \(W=[L,L]\), every derivation preserves \(W\). Write its action on \(V\) as \(v\mapsto Cv+Bv\) and its action on \(W\) as \(S\). The derivation identity on \([u,v]=u\wedge v\) forces \(S(u\wedge v)=Cu\wedge v+u\wedge Cv=R(C)(u\wedge v)\). Conversely every pair \((C,B)\), with \(C\in\operatorname{End}(V)\) and \(B\in\operatorname{Hom}(V,W)\), defines an ordinary derivation. This also proves that a local derivation necessarily preserves \(W\).

**2. Tangent-space rigidity lemma.** Suppose \(T:\bigwedge^2V\to\bigwedge^2V\) is linear and obeys
\[
 T(u\wedge v)\in u\wedge V+v\wedge V\quad\text{for every }u,v\in V.
\]
We prove that \(T=R(A)\) for a unique \(A\in\operatorname{End}(V)\). Fix a basis \(e_1,\ldots,e_n\). For distinct \(i,j\), the condition at \(e_i\wedge e_j\) says every basis term of \(T(e_i\wedge e_j)\) meets \(\{i,j\}\). In oriented notation, for distinct \(i,j,k\), let the coefficient of \(e_i\wedge e_k\) be \(a_{kj}^{(i)}\). For distinct \(i,r,j,k\), applying the condition to \((e_i+e_r)\wedge e_j\) and reducing modulo \(e_j\wedge V+(e_i+e_r)\wedge V\) shows \(a_{kj}^{(i)}=a_{kj}^{(r)}\). Thus this coefficient depends only on \(k,j\); call it \(a_{kj}\). The analogous coefficients of \(e_k\wedge e_j\) are the same \(a_{ki}\). As \(n\ge4\), all needed distinct indices exist. Define \(A_0e_j=\sum_{k\ne j}a_{kj}e_k\). By construction, \(T-R(A_0)\) is diagonal on the wedge basis:
\[
 (T-R(A_0))(e_i\wedge e_j)=\alpha_{ij}e_i\wedge e_j,\qquad\alpha_{ij}=\alpha_{ji}.
\]
It retains the tangent condition. Apply it to the decomposable bivector \((e_i+e_k)\wedge(e_j+e_l)\), where the four indices are different. Wedge the result with this bivector, obtaining
\[
 \alpha_{ij}+\alpha_{kl}=\alpha_{il}+\alpha_{kj}.
\]
These are the four-point additive relations. Choose three distinct indices \(a,b,c\), put \(s_a=(\alpha_{ab}+\alpha_{ac}-\alpha_{bc})/2\), \(s_b=\alpha_{ab}-s_a\), and \(s_c=\alpha_{ac}-s_a\). For each other index \(i\), put \(s_i=\alpha_{ai}-s_a\). The four-point relations on \(\{a,b,c,i\}\) imply \(\alpha_{bi}=s_b+s_i\) and \(\alpha_{ci}=s_c+s_i\); those on \(\{a,b,i,j\}\) then imply \(\alpha_{ij}=s_i+s_j\) for all remaining pairs. Thus \(T-R(A_0)=R(\operatorname{diag}(s_i))\). Uniqueness: the off-diagonal entries of \(A\) are recovered from coefficients with three distinct indices, while \(R(A)=0\) for diagonal \(A\) forces \(s_i+s_j=0\) for all \(i<j\), and hence every \(s_i=0\) because \(2\ne0\). This proves the lemma over every allowed field, without a closure assumption.

**3. Necessity.** Let \(\Delta\) be local. By step 1, \(\Delta(W)\subset W\), so its matrix relative to \(L=V\oplus W\) has blocks \((P,0;Q,T)\). For decomposable \(z=u\wedge v\), choose an ordinary derivation agreeing with \(\Delta\) at \(z\); its central block is \(R(C_z)\). Therefore \(T(z)=C_zu\wedge v+u\wedge C_zv\in u\wedge V+v\wedge V\). The lemma gives a unique \(A\) such that \(T=R(A)\), with no relation between \(A\) and \(P\) or \(Q\).

**4. Sufficiency.** Take any such triple and \(x=v+z\). If \(v=0\), the derivation \(D_{A,0}\) agrees with \(\Delta\) at \(x\). If \(v\ne0\), choose \(C\in\operatorname{End}(V)\) with \(Cv=Pv\), and choose \(B\in\operatorname{Hom}(V,W)\) with
\[
 Bv=Qv+R(A)z-R(C)z.
\]
Both choices exist because a linear map can be assigned an arbitrary value on one nonzero vector. The ordinary derivation \(D_{C,B}\) agrees with \(\Delta\) at \(x\). Hence \(\Delta\) is local. Comparison with step 1 and injectivity of \(R\) shows \(\Delta\) is ordinary exactly when \(P=A\).

**5. Dimension.** The parameter map \((P,Q,A)\mapsto\Delta_{P,Q,A}\) is a linear isomorphism by uniqueness. Counting its dimensions and imposing \(P=A\) gives the formulas; finite-field counts are their powers of \(q\).

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The script independently constructs exterior-square coefficient matrices and the linear equations for the tangent-space condition at every \(\mathbb F_p\)-rational two-plane in reduced-row-echelon form. It checks that the kernel of the full system equals the span of the exterior Lie action for \((n,p)=(4,3),(4,5),(5,3)\): the respective tangent-system nullities are \(16,16,25\), matching the ranks of \(R(\operatorname{End}(V))\). The verifier is finite corroboration only; the arbitrary-field proof is above.

## Relationship to prior work
Hao and Chen's June 2026 manuscript on pointwise invariant sets (later related to arXiv:2609.09198) proves general Lie-closure of local-derivation spaces. It does not supply the rank-parametric matrix description, dimension, or finite-field count in this theorem. Their December 2025 computations describe low-dimensional nilpotent examples, including rank-three free class-two examples of dimension six; our range begins at rank four and dimension ten. Khudoyberdiyev and Jumaniyozov (2024) show existence of proper local derivations for two-step nilpotent Lie algebras of characteristic different from two, not classification of the whole space. Burde, Dekimpe, and Verbeke study almost-inner derivations, which are ordinary derivations satisfying a pointwise inner constraint, not the local-derivation condition used here. The exterior-square lemma is also naturally interpreted as an infinitesimal Grassmannian tangent-preserver statement; its elementary proof is included rather than claiming the general geometry is new.

## Limitations
No result is asserted for characteristic two or ranks less than four; finite checks do not prove the general claim. Originality is limited to this explicit family-wide classification and its numerical consequences, not to the definition of local derivations, existence of nonordinary local derivations, general Lie-closure, or classical tangent geometry. Although the most relevant openly accessible primary results were compared, an equivalent earlier treatment under another algebraic-reflexivity terminology may exist.

## References
1. Z. Hao and L. Chen, *Two conjectures and applications on local and almost inner derivations*, author-provided manuscript publicly uploaded 2026-06-10, https://www.researchgate.net/publication/406832793_TWO_CONJECTURES_AND_APPLICATIONS_ON_LOCAL_AND_ALMOST_INNER_DERIVATIONS .
2. Z. Hao and L. Chen, *Local derivations is a Lie algebra*, arXiv:2609.09198 (first arXiv posting 2026-09-04), https://arxiv.org/abs/2609.09198 .
3. Z. Hao and L. Chen, *A computational approach to local derivations and almost inner derivations*, publicly uploaded 2025-12-22, https://www.researchgate.net/publication/398952066_A_computational_approach_to_local_derivations_and_almost_inner_derivations .
4. A. Khudoyberdiyev and D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebra*, arXiv:2405.04209 (2024), https://arxiv.org/abs/2405.04209 .
5. D. Burde, K. Dekimpe, and B. Verbeke, *Almost inner derivations of Lie algebras*, arXiv:1704.06159 (2017), https://arxiv.org/abs/1704.06159 .
