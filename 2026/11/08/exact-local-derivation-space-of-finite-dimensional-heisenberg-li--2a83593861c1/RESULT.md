# Exact local-derivation space of finite-dimensional Heisenberg Lie algebras

## Finding

For every field \(K\) and every integer \(m\ge1\), all linear local derivations of the \((2m+1)\)-dimensional Heisenberg Lie algebra are **exactly** the endomorphisms preserving its derived line. More precisely,
\[
\operatorname{LocDer}(H)=\{T\in\operatorname{End}_K(H):T(Kz)\subseteq Kz\}.
\]
Every such map has the unique block form
\[
T(v+tz)=Mv+(\phi(v)+\lambda t)z,
\quad M\in\operatorname{End}_K(V),\ \phi\in V^*,\ \lambda\in K.
\]
The ordinary derivations are exactly the blocks satisfying the additional conformal-symplectic identity
\[
\omega(Mv,w)+\omega(v,Mw)=\lambda\omega(v,w)
\quad\text{for all }v,w\in V.
\]
Consequently,
\[
\dim_K\operatorname{LocDer}(H)=4m^2+2m+1,\qquad
\dim_K\operatorname{Der}(H)=2m^2+3m+1,
\]
with difference \(m(2m-1)\). For \(K=\mathbb F_q\), the exact counts are \(q^{4m^2+2m+1}\) and \(q^{2m^2+3m+1}\), respectively. The fraction of local derivations satisfying the global derivation identity is \(q^{-m(2m-1)}\).

## Assumptions and scope

Let \(K\) be any field, possibly of characteristic two, and let \(V\) have dimension \(2m\) with \(m\ge1\). Fix a nondegenerate alternating bilinear form \(\omega:V\times V\to K\). Define \(H=V\oplus Kz\) with \([u+az,v+bz]=\omega(u,v)z\). This is a Lie algebra in every characteristic; by nondegeneracy, its center and derived subalgebra coincide and equal \(Kz\). We use *linear local derivation* in the pointwise sense: a \(K\)-linear map \(T:H\to H\) such that for every \(x\in H\) a possibly \(x\)-dependent Lie derivation \(D_x\) satisfies \(T(x)=D_x(x)\). No assertion is made about nonlinear pointwise maps or two-local derivations.

## Proof

**Step 1: ordinary derivations.** The derived line \(Kz=[H,H]\) is characteristic under every derivation. Hence any derivation has form \(D(v+tz)=Av+(\psi(v)+\mu t)z\) with \(A\in\operatorname{End}(V)\), \(\psi\in V^*\), \(\mu\in K\). Applying the derivation identity to \([v,w]=\omega(v,w)z\) gives exactly
\[
\omega(Av,w)+\omega(v,Aw)=\mu\omega(v,w)
\quad(\forall v,w\in V).
\]
Conversely, this equation ensures the derivation identity for every bracket because all brackets are central and brackets involving \(z\) vanish. Thus it is necessary and sufficient.

A symplectic (Lagrangian) decomposition \(V=P\oplus Q\) exists over any field. With \(\dim P=\dim Q=m\), the map \(A_\mu\) which scales \(P\) by \(\mu\) and annihilates \(Q\) satisfies the equation with multiplier \(\mu\). The kernel of the multiplier functional is the symplectic Lie algebra \(\mathfrak{sp}(V,\omega)\). In symplectic bases, its matrices are
\[
\begin{pmatrix}X&Y\\ Z&-X^{\mathsf T}\end{pmatrix},
\qquad Y=Y^{\mathsf T},\quad Z=Z^{\mathsf T}.
\]
This description also works in characteristic two and gives dimension \(m^2+2\binom{m+1}{2}=m(2m+1)\). Therefore \(\dim_K\operatorname{Der}(H)=m(2m+1)+1+2m=2m^2+3m+1\).

**Step 2: the pointwise symplectic evaluation lemma.** Fix nonzero \(v\in V\) and arbitrary \(w\in V\). Choose \(t\in V\) with \(\omega(t,v)=1\). For \(a,b\in V\), define
\[
S_{a,b}(x)=\omega(a,x)b+\omega(b,x)a,\qquad
R_a(x)=\omega(a,x)a.
\]
These operators lie in \(\mathfrak{sp}(V,\omega)\): for any \(x,y\), direct expansion shows \(\omega(S_{a,b}x,y)+\omega(x,S_{a,b}y)=0\) and likewise for \(R_a\), using only skew-symmetry of an alternating form (valid also in characteristic two). Set
\[
A=S_{t,w}-\omega(w,v)R_t.
\]
Then \(Av=w+\omega(w,v)t-\omega(w,v)t=w\). Hence the evaluation map \(\mathfrak{sp}(V,\omega)\to V\), \(A\mapsto Av\), is surjective for every nonzero \(v\), over every field.

**Step 3: necessity of preserving the center.** If \(T\) is a local derivation, then \(T(z)=D_z(z)\) for some derivation \(D_z\). Step 1 gives \(D_z(z)\in Kz\). Therefore \(T(Kz)\subseteq Kz\).

**Step 4: sufficiency.** Let \(T\) preserve \(Kz\), with its unique expression \(T(v+sz)=Mv+(\phi(v)+\lambda s)z\). For any noncentral \(x=v+sz\) (so \(v\ne0\)), Step 2 gives a symplectic infinitesimal operator \(A\) satisfying \(Av=Mv\). Select \(\psi\in V^*\) with \(\psi(v)=\phi(v)+\lambda s\), possible because \(v\ne0\). Then the derivation \(D_x\) from Step 1 with base map \(A\), multiplier \(0\), and functional \(\psi\) satisfies \(D_x(x)=T(x)\). At a central point \(x=sz\), use the conformal derivation with \(A=A_\lambda\), multiplier \(\lambda\) and \(\psi=0\), obtaining \(D_x(sz)=\lambda sz=T(sz)\). The zero point is automatic. Hence \(T\) is local.

**Step 5: numerical consequences.** The block parameters \(M,\phi,\lambda\) are independent and range over spaces of dimensions \(4m^2,2m,1\). Subtracting the ordinary-derivation dimension gives \(m(2m-1)\). A \(d\)-dimensional vector space over \(\mathbb F_q\) contains \(q^d\) elements, producing the exact counts and proportion above.

## Verification

The standalone file `verify.py` constructs the derivation-defining linear system directly from the Heisenberg Lie brackets over prime fields, computes its nullspace by modular Gaussian elimination, and independently checks evaluation ranks at **every** algebra element in six field/rank configurations. The cases \((m,p)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\) total \(563\) inputs. The derivation-space dimensions were \(6,6,6,15,15,28\). Evaluation ranks were zero at the zero element, one at each nonzero center element, and \(2m+1\) at every noncentral element. The program's output is preserved as `VERIFY_OUTPUT.txt`. The proof above, rather than the finite computations, covers all fields and ranks.

## Relationship to prior work

Atajonov, Khudoyberdiyev and Yusupov (arXiv:2610.40348v1, first public 2026-10-29) establish that every nonabelian finite-dimensional complex nilpotent Lie algebra has a proper local derivation, using existence constructions. They do not state the complete pointwise evaluation classification or the exact dimensions for this Heisenberg family. Khudoyberdiyev and Jumaniyozov (arXiv:2405.04209v1, first public 2024-05-07) give a concrete proper local derivation on a complex Heisenberg algebra in Example 3.2, without an entire-space classification; they explicitly highlight characteristic-two complications in general nilpotent Lie algebras. Ayupov and Kudaybergenov (arXiv:1508.03939v1, 2015) establish existence of proper local derivations in nilpotent examples and semisimple rigidity, not the stated rank-uniform Heisenberg formula. Atajonov, Sultonboyev and Yusupov (arXiv:2609.24113v1) classify local derivations of larger conformal Galilei semidirect products with Heisenberg-type radicals; their rigidity results apply to different Lie algebras, not to their Heisenberg ideals considered alone.

The main exact-space statement is distinct from an earlier classification of **local automorphisms** of finite Heisenberg Lie algebras. Local automorphisms are invertible pointwise maps with automorphism witnesses; local derivations need not be invertible and have derivation witnesses. In the smallest binary case their local-global rigidity behavior differs, showing why one cannot replace the above argument by an automorphism-group count.

## Limitations

The theorem concerns linear pointwise local derivations of *Heisenberg Lie algebras*, and does not determine nonlinear or two-local derivations, other class-two nilpotent Lie algebras, or arbitrary central extensions. Its originality assessment is limited to searched and inspected sources, not a proof of historical priority. The available finite-field computations use prime fields, not all field extensions, and support but do not establish the general theorem.

## References

1. Kh. Atajonov, A. Khudoyberdiyev, B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (2026-10-29), https://arxiv.org/abs/2610.40348.
2. A. Khudoyberdiyev, D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebras*, arXiv:2405.04209v1 (2024-05-07), https://arxiv.org/abs/2405.04209.
3. Sh. Ayupov, K. Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939v1 (2015-08-17), https://arxiv.org/abs/1508.03939.
4. Kh. Atajonov, B. Sultonboyev, B. Yusupov, *Local Derivations on Conformal Galilei Algebras and Their Central Extensions*, arXiv:2609.24113v1 (2026-09-21), https://arxiv.org/abs/2609.24113.
