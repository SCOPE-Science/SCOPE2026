# Local derivations of free two-step nilpotent Lie algebras

## Finding
Let \(k\) be any field of characteristic different from \(2\), let \(n\geq3\), let \(V=k^n\), and put \(Z=\Lambda^2V\). Give \(L=V\oplus Z\) the free two-step nilpotent Lie bracket \([v+z,w+t]=v\wedge w\). For \(B\in\operatorname{End}_k(V)\), denote the induced infinitesimal exterior-square action by
\[
\rho(B)(v\wedge w)=Bv\wedge w+v\wedge Bw.
\]
Then **every linear local derivation** of \(L\) has a unique normal form
\[
\boxed{T_{A,B,f}(v+z)=Av+f(v)+\rho(B)z,\quad A,B\in\operatorname{End}(V),\ f\in\operatorname{Hom}(V,Z).}
\]
The map \(T_{A,B,f}\) is an ordinary derivation precisely when \(A=B\). Consequently,
\[
\boxed{\dim\operatorname{LocDer}(L)=2n^2+n\binom n2,\quad
\dim\operatorname{Der}(L)=n^2+n\binom n2,\quad
\dim(\operatorname{LocDer}(L)/\operatorname{Der}(L))=n^2.}
\]
As Lie algebras under commutator, \(\operatorname{LocDer}(L)\) is the semidirect product of \(\operatorname{Hom}(V,Z)\) by two independent copies of \(\mathfrak{gl}(V)\); the action of \((A,B)\) on \(f\) is \(f\mapsto\rho(B)f-fA\). The ordinary derivations form the subalgebra where the two copies are diagonal. The quotient above is a **vector-space quotient**, not asserted to be a Lie-algebra quotient.

## Assumptions and scope
All maps are \(k\)-linear, and \(k\) need not be finite or algebraically closed. A linear map \(T:L\to L\) is a *local derivation* when for every \(x\in L\) there exists an ordinary derivation \(D_x\) with \(T(x)=D_x(x)\); this does not require one derivation to work at all points. The restrictions \(n\ge3\) and \(\operatorname{char}k\ne2\) are essential to the stated uniqueness argument. The result does not describe nonlinear or two-local maps. The free rank-two case is the three-dimensional Heisenberg algebra and is not claimed here.

## Proof
**1. Derivations.** The commutator ideal of \(L\) is \(Z\), hence it is invariant under every derivation. Writing a derivation on \(V\) as its \(V\)-component \(B\) plus a central component \(g:V\to Z\), the Leibniz rule on \([v,w]=v\wedge w\) forces its restriction to \(Z\) to be exactly \(\rho(B)\). Conversely, arbitrary \(B\) and \(g\) define a derivation
\[
D_{B,g}(v+z)=Bv+g(v)+\rho(B)z,
\]
as is checked directly on the generating brackets. Therefore the displayed list of ordinary derivations is exhaustive.

**2. Locality separates the noncentral and central inputs.** Every local derivation preserves \(Z\), because every derivation does. Consequently an arbitrary candidate is uniquely expressible as
\[
T(v+z)=Av+f(v)+Sz
\]
with \(A:V\to V\), \(f:V\to Z\), \(S:Z\to Z\). For any \(v\ne0\) and any desired output \(a+c\in V\oplus Z\), select \(B\) with \(Bv=a\), and then select \(g\) with \(g(v)=c-\rho(B)z\). Such choices exist because evaluation at a nonzero vector is surjective for both Hom-spaces. Thus no locality condition involving \(v\ne0\) constrains \(A,f,S\). The remaining condition, at the points \(z\in Z\), is
\[
Sz\in\{\rho(B)z:B\in\operatorname{End}(V)\}\quad\text{for every }z\in Z.\tag{1}
\]

**3. Infinitesimal decomposable-bivector lemma.** We prove that for \(n\ge3\), over any field of characteristic other than two, any linear \(S:Z\to Z\) satisfying (1) is \(S=\rho(B)\) for a *unique* \(B\in\operatorname{End}(V)\). Only decomposable bivectors are needed. For independent \(u,v\), condition (1) implies
\[
S(u\wedge v)\in u\wedge V+v\wedge V.\tag{2}
\]
For \(n=3\), the linear map \(\rho:\operatorname{End}(V)\to\operatorname{End}(\Lambda^2V)\) is an isomorphism. Indeed, upon identifying \(\Lambda^2 V\) with \(V^*\) using a volume form, its matrix is \((\operatorname{tr}B)I-B^{\mathsf T}\); the inverse is obtained from \(\operatorname{tr}B=\tfrac12\operatorname{tr}\rho(B)\). This establishes the lemma in dimension three.

For \(n\ge4\), choose a basis \(e_1,\dots,e_n\). Applying (2) to \(e_i\wedge e_j\) first shows that every nonzero coefficient of \(S(e_i\wedge e_j)\) is on a basis bivector that contains index \(i\) or \(j\). Applying (2) to \((e_i+e_h)\wedge e_j\), with \(i,h,j\) distinct, shows that for \(k\notin\{i,h,j\}\) the coefficient on \(e_i\wedge e_k\) in \(S(e_i\wedge e_j)\) equals the corresponding coefficient on \(e_h\wedge e_k\) in \(S(e_h\wedge e_j)\). Equivalently, the coefficient that replaces \(j\) by \(k\) depends only on \((k,j)\), not on \(i\). The analogous test \(e_i\wedge(e_j+e_h)\) gives the same independence when replacing the first index. These relations assign the off-diagonal entries of a matrix \(B_0\), and subtracting \(\rho(B_0)\) removes all terms that replace exactly one input index. What remains is diagonal on the bivector basis:
\[
(S-\rho(B_0))(e_i\wedge e_j)=c_{ij}e_i\wedge e_j,\quad c_{ij}=c_{ji}.
\]
For four distinct indices, apply (2) to \((e_i+e_k)\wedge(e_j+e_l)\) and project its image modulo the two-space wedge tangent. Comparing the coefficient of \(e_i\wedge e_j\wedge e_k\wedge e_l\) in the exterior product of the input with its image gives
\[
c_{ij}+c_{kl}=c_{il}+c_{kj}.\tag{3}
\]
Set \(b_1=(c_{12}+c_{13}-c_{23})/2\), \(b_2=(c_{12}+c_{23}-c_{13})/2\), \(b_3=(c_{13}+c_{23}-c_{12})/2\), and \(b_i=c_{1i}-b_1\) for \(i\ge4\). Relation (3) gives \(c_{ij}=b_i+b_j\) for every pair. Hence the diagonal remainder is \(\rho(\operatorname{diag}(b_1,\dots,b_n))\), establishing existence. To see uniqueness, the off-diagonal coefficients of \(\rho(B)(e_i\wedge e_j)\) recover every off-diagonal entry of \(B\) (choose a third index), while the equations \(b_i+b_j=0\) for all distinct \(i,j\) force every diagonal entry to be zero because \(n\ge3\) and \(2\) is invertible. This proves the lemma.

**4. Completion.** By the lemma, (1) is equivalent to \(S=\rho(B)\). Conversely every \(T_{A,B,f}\) is local: at \(v=0\), take \(D_{B,0}\), and at \(v\ne0\), use the independent choices of the derivation's quotient and central components from step 2. The map is a derivation iff its restriction to \(Z\) equals \(\rho(A)\), equivalently \(A=B\) by injectivity of \(\rho\). The parameter spaces are independent, giving the dimensions. Block multiplication of
\[
T_{A,B,f}=\begin{pmatrix}A&0\\f&\rho(B)\end{pmatrix}
\]
gives the stated semidirect Lie algebra and finishes the proof.

## Verification
Run `python3 verify.py` in the directory containing this result. The standalone checker uses exact modular arithmetic and no external Python dependencies. It constructs \(\rho\) directly from exterior products. Over \(\mathbb F_3\), it exhaustively tests every central vector for \(n=3,4\), forming the linear equations on a possible central map \(S\) imposed by its value being in \(\{\rho(B)z\}\). The computed solution-space dimensions are \(9\) and \(16\), respectively, as predicted. Independent samples of decomposable bivectors recover the expected dimension \(25\) for \(n=5\) over \(\mathbb F_3\), and \(16\) for \(n=4\) over \(\mathbb F_5\). Separately, 2,250 explicit pointwise witness checks over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) verify that the normal forms are local in small dimensions. These finite checks are corroborative, not an exhaustive proof over all fields or ranks.

## Relationship to prior work
Atajonov, Khudoyberdiyev and Yusupov (arXiv:2610.40348v1, October 29, 2026), Theorem 3.5, prove that every nonabelian finite-dimensional complex nilpotent Lie algebra admits a proper local derivation. Theorem 3.5 is an **existence** statement and does not specify the entire local-derivation space for free two-step nilpotent algebras or its dimension. Khudoyberdiyev and Jumaniyozov (arXiv:2405.04209v1, Theorem 3.1) establish proper local derivations for two-step nilpotent Lie algebras in characteristic not two, again without the present full parameterization. Hao and Chen's 2026 pointwise-invariant-set work establishes structural closure properties of local derivations but its accessible discussion does not give this exterior-square classification. Burde, Dekimpe and Verbeke study *almost inner derivations*, which are ordinary derivations satisfying a different pointwise restriction. The present statement calculates the complete local-derivation space on a natural infinite family, not merely existence or a special witness. The rank-two free member is the previously treated Heisenberg case and is not claimed as a new case.

## Limitations
No statement is made in characteristic two, for rank less than three, or for nonlinear local maps. The elementary tangent-preserver lemma uses invertibility of two. The uniqueness of \(B\) also fails for rank two. Priority relative to inaccessible or unindexed articles is not independently certified, and computation does not establish novelty. No independent audit has been performed.

## References
1. K. Atajonov, A. Khudoyberdiyev, B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1, submitted October 29, 2026. https://arxiv.org/abs/2610.40348
2. A. Khudoyberdiyev, D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebra*, arXiv:2405.04209v1, submitted May 7, 2024. https://arxiv.org/abs/2405.04209
3. Z. Hao, L. Chen, *Two conjectures and applications on local and almost inner derivations*, 2026 preprint, available at https://www.researchgate.net/publication/408607392_TWO_CONJECTURES_AND_APPLICATIONS_ON_LOCAL_AND_ALMOST_INNER_DERIVATIONS
4. D. Burde, K. Dekimpe, B. Verbeke, *Almost inner derivations of Lie algebras*, arXiv:1704.06159v1, 2017. https://arxiv.org/abs/1704.06159
