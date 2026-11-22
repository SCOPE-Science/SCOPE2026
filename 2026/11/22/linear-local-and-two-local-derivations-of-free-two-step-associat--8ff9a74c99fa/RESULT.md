# Linear local and two-local derivations of free two-step associative algebras

## Finding

Let \(K\) be any field of characteristic different from \(2\), let \(m\geq2\), and let \(V\) be a vector space of dimension \(m\). Define the nonunital associative algebra
\[
N(V)=V\oplus(V\otimes_KV),\qquad
(v,z)(w,t)=(0,v\otimes w).
\]
It is the positive-degree part of the free associative algebra on \(m\) generators truncated after words of degree two; in particular \(N(V)^2=V\otimes V\ne0\) and \(N(V)^3=0\). For \(A\in\operatorname{End}_K(V)\), write
\[
\rho(A)=A\otimes I_V+I_V\otimes A
\in\operatorname{End}_K(V\otimes V).
\]

A *linear local derivation* is a \(K\)-linear map \(\Delta:N(V)\to N(V)\) such that for each \(x\) there is an ordinary derivation \(D_x\) satisfying \(D_x(x)=\Delta(x)\). A *linear two-local derivation* is a \(K\)-linear map such that each pair of elements admits a **single** ordinary derivation agreeing with \(\Delta\) on both elements.

**Theorem.** Every linear local derivation has the unique expression
\[
\boxed{\Delta_{A,S,F}(v+z)
   =Av+F(v)+\rho(S)z,\quad
 A,S\in\operatorname{End}_K(V),\quad
 F\in\operatorname{Hom}_K(V,V\otimes V).}
\]
Such a map is an ordinary derivation if and only if \(A=S\). Moreover, **every linear two-local derivation is an ordinary derivation**. Thus
\[
\boxed{\begin{aligned}
\dim_K\operatorname{Der}(N(V))&=m^2+m^3,\\
\dim_K\operatorname{LocDer}_{\rm lin}(N(V))&=2m^2+m^3,\\
\operatorname{2LocDer}_{\rm lin}(N(V))&=\operatorname{Der}(N(V)),\\
\dim_K\bigl(\operatorname{LocDer}_{\rm lin}(N(V))/\operatorname{Der}(N(V))\bigr)&=m^2.
\end{aligned}}
\]
The displayed quotient is a vector-space quotient. The theorem separates local from linear two-local derivations in every generator rank \(m\ge2\), over every odd-characteristic field, finite or infinite. It does not address nonlinear two-local maps.

## Assumptions and scope

All tensor products and endomorphisms are over \(K\). No commutativity, algebraic closedness, or finiteness of \(K\) is required; the algebra is deliberately **nonunital** and retains all ordered quadratic words. Throughout \(m\ge2\) and \(2\) is invertible in \(K\). For the two-local condition, the same ordinary derivation must interpolate each ordered pair, but may depend on that pair. The field and generator-rank quantifiers cover every such choice, not merely the finite checks below.

## Proof

**1. All ordinary derivations.** Put \(W=V\otimes V=N(V)^2\). Since \(W\) annihilates \(N(V)\) on both sides, every ordinary derivation preserves \(W\), and its restriction to \(V\) can be written \(v\mapsto Av+F(v)\). Applying the Leibniz identity to \(v w=v\otimes w\) forces
\[
D(v\otimes w)=Av\otimes w+v\otimes Aw
 =\rho(A)(v\otimes w).
\]
Elementary tensors span \(W\). Conversely, for arbitrary \(A,F\), the map
\[
D_{A,F}(v+z)=Av+F(v)+\rho(A)z
\]
satisfies the Leibniz identity, since products with a member of \(W\) are zero. It follows that these are exactly the ordinary derivations. The action \(\rho\) is injective in characteristic different from two: if \(\rho(T)=0\), evaluate at every \(e_i\otimes e_i\) in a basis. Off-diagonal coefficients force all off-diagonal entries of \(T\) to vanish, and the coefficient of \(e_i\otimes e_i\) is twice the \(i\)-th diagonal entry.

**2. A tensor-square pointwise-action lemma.** We prove the following elementary linear-preserver statement: if \(C\in\operatorname{End}(V\otimes V)\) satisfies
\[
\forall z\in V\otimes V\quad
Cz\in\{\rho(T)z:T\in\operatorname{End}(V)\},
\tag{1}
\]
then \(C=\rho(S)\) for a unique \(S\in\operatorname{End}(V)\).

First take a decomposable tensor \(z=u\otimes v\). The right side of (1) is contained in \(V\otimes v+u\otimes V\), so
\[
C(u\otimes v)\in V\otimes v+u\otimes V.
\tag{2}
\]
We show that a linear map satisfying (2) for every pair \(u,v\) must equal \(A_0\otimes I+I\otimes B_0\), with \(A_0,B_0\in\operatorname{End}(V)\). Choose a basis \(e_1,\ldots,e_m\). Equation (2) on \(e_i\otimes e_j\) allows only terms of the form \(e_a\otimes e_j\) or \(e_i\otimes e_b\). Now apply (2) to \(e_i\otimes(e_j+e_l)\) for distinct \(j,l\). For each \(a\ne i\), the coefficient on \(e_a\otimes e_j\) in \(C(e_i\otimes e_j)\) must equal the coefficient on \(e_a\otimes e_l\) in \(C(e_i\otimes e_l)\). These are the off-diagonal entries of a single matrix \(A_0\). Similarly, applying (2) to \((e_i+e_h)\otimes e_j\) for distinct \(i,h\) shows that the coefficients on \(e_i\otimes e_b\), \(b\ne j\), depend only on the input index \(j\); these are the off-diagonal entries of one matrix \(B_0\). Subtract the corresponding tensor-sum action. The remaining map is diagonal on every tensor basis vector:
\[
C'(e_i\otimes e_j)=d_{ij}\,e_i\otimes e_j.
\]
For \(i\ne h\) and \(j\ne l\), apply (2) to \((e_i+e_h)\otimes(e_j+e_l)\). Its four coefficients can lie in the tangent space only if
\[
d_{ij}+d_{hl}=d_{il}+d_{hj}.
\]
These relations imply \(d_{ij}=\alpha_i+\beta_j\) (for example fix \(\alpha_i=d_{i1}\) and \(\beta_j=d_{1j}-d_{11}\)), and hence \(C'=\operatorname{diag}(\alpha)\otimes I+I\otimes\operatorname{diag}(\beta)\). This proves the asserted tensor-sum form.

Return to the stronger condition (1) at \(z=u\otimes u\). Every \(\rho(T)(u\otimes u)\) is invariant under the tensor flip. Thus for every \(u\)
\[
(A_0-B_0)u\otimes u=u\otimes(A_0-B_0)u.
\]
For \(u\ne0\), this means \((A_0-B_0)u\) is proportional to \(u\). Every vector is therefore an eigenvector of \(A_0-B_0\), so it is a scalar matrix \(\lambda I\) (use \(e_i+e_j\)). Since \(2\) is invertible,
\[
C=\rho\bigl(B_0+\tfrac{\lambda}{2}I\bigr).
\]
Injectivity of \(\rho\) supplies uniqueness. This completes the lemma.

**3. Classification of linear local derivations.** Every local map \(\Delta\) sends \(W\) into \(W\), because every derivation preserves \(W\). Consequently it has a block form
\[
\Delta(v+z)=Av+F(v)+Cz.
\]
Applying locality only to the points \(z\in W\) gives (1), and the tensor-square lemma yields \(C=\rho(S)\). Conversely, any displayed \(\Delta_{A,S,F}\) is local. At \(v=0\), the derivation \(D_{S,0}\) agrees with it at \(z\). At \(v\ne0\), choose an arbitrary linear \(G:V\to W\) with
\[
G(v)=F(v)+(\rho(S)-\rho(A))z.
\]
Such a \(G\) always exists, and then the ordinary derivation \(D_{A,G}\) agrees with \(\Delta_{A,S,F}\) at \(v+z\). Thus the parameters are independent, and a local map is an ordinary derivation precisely when \(A=S\). Counting dimensions yields the first, second, and fourth displayed formulas.

**4. Linear two-local rigidity.** Let \(\Delta_{A,S,F}\) be a linear two-local derivation. Fix a basis of \(V\) and let
\[
z_D=\sum_{i=1}^{m}d_i e_i\otimes e_i,
\qquad d_i\in K^\times.
\]
Identify \(V\otimes V\) with matrices, so \(z_D\) corresponds to an invertible diagonal matrix \(D=\operatorname{diag}(d_1,\ldots,d_m)\). For any \(v\in V\), apply two-locality to the pair \(z_D,\ v+z_D\). A single derivation \(D_{T,G}\) agrees with \(\Delta\) at both points. Subtracting the two image equations and comparing the \(V\)-components gives
\[
T v=A v,\qquad \rho(T-S)z_D=0.
\]
Set \(R=T-S\) and \(M=A-S\). The second equality is the matrix identity
\[
R D+D R^{\mathsf T}=0,
\]
so \(D^{-1}R\) is skew-symmetric. The first equality gives \(Rv=Mv\). Therefore, for every \(v\in V\) and every invertible diagonal \(D\),
\[
0=v^{\mathsf T}D^{-1}R v
 =v^{\mathsf T}D^{-1}M v.
\tag{3}
\]
Take \(v=e_i\) in (3) to conclude that every diagonal entry of \(M\) is zero. For distinct \(i,j\), put \(v=e_i+e_j\). Equation (3) becomes
\[
d_i^{-1}M_{ij}+d_j^{-1}M_{ji}=0.
\]
Fix all other diagonal entries and compare \((d_i,d_j)=(1,1)\) and \((1,-1)\). Characteristic different from two implies both \(M_{ij}\) and \(M_{ji}\) vanish. Therefore \(M=0\), i.e. \(A=S\), and \(\Delta\) is an ordinary derivation. Conversely every ordinary derivation is two-local (the same derivation works for all pairs). This proves the final assertion.

## Verification

The standalone script `CHECKER.py` uses exact modular linear algebra. Over \(\mathbb F_3\) and \(\mathbb F_5\) in generator rank two, it enumerates every nonzero quadratic tensor, constructs the possible derivation values directly from \(\rho\), and computes the entire linear algebraic reflexive hull. Its dimension is four in both fields, as predicted by the lemma. In rank three over \(\mathbb F_3\), all \(169\) projective rank-one tensors alone impose constraints whose solution space has dimension nine, proving the equality of that finite-field reflexive hull with \(\rho(\operatorname{End}V)\). Finally, for both rank-two fields it explicitly tests every nonzero matrix \(M=A-S\) against the invertible-diagonal two-point obstruction (3) and excludes all \(80\) and \(624\), respectively. A successful execution prints `ASSOCIATIVE_LOCAL_DERIVATION_CHECKS_OK`.

These computations are finite illustrations only. The arbitrary-field, all-rank conclusions follow from steps 1–4, not from extrapolation from the sampled or exhaustive finite tests.

## Relationship to prior work

Atajonov, Khudoyberdiyev and Yusupov (arXiv:2610.40348v1, first submitted October 29, 2026) treat local maps on finite-dimensional nilpotent **Lie and Leibniz** algebras, rather than the associative tensor-square product above. Abdurasulov, Ayupov and Yusupov (arXiv:2305.15339) study local and two-local derivations of **null-filiform, filiform, and naturally graded quasi-filiform associative** algebras. The algebra here has \(\dim N(V)=m+m^2\) and \(\dim N(V)^2=m^2\); for \(m\ge2\), it is not in the filiform-type families of their classification.

A published result titled *Idempotent derivations and a sharp half-rank bound in free two-step associative algebras* gives the same underlying ordinary-derivation normal form for this algebra and counts **composition-idempotent ordinary derivations**. That result does not classify local derivations or linear two-local maps. Published classifications for the free two-step **Lie** algebra use the exterior-square action on \(\bigwedge^2 V\) and show a nontrivial one-dimensional linear two-local derivation defect in ranks at least three. In contrast, the present associative theorem uses the unsymmetrized tensor square and proves zero linear two-local defect. In particular, the exterior-square theorem cannot imply the tensor-square rigidity result merely by relabeling its parameters.

Classical work on *locally nilpotent derivations* of the infinite free associative algebra concerns a different predicate (nilpotence under iteration of a single derivation), not pointwise or two-point derivation interpolation. The present theorem is a structural calculation of the local evaluation hull and its two-point analogue. It does not claim that all possibly nonlinear two-local maps are ordinary derivations.

## Limitations

The result makes no claim in characteristic two, for the one-generator algebra, for quotient algebras with additional quadratic relations, or for nonlinear two-local derivations. Exact finite checks cannot certify the all-field theorem on their own. Literature search and the inspected accessible publications do not establish definitive historical priority against every unindexed result, including possible general theorems on tensor-square operator reflexivity. Independent mathematical review has not been performed.

## References

1. K. Atajonov, A. Khudoyberdiyev and B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (2026-10-29), https://arxiv.org/abs/2610.40348.
2. K. K. Abdurasulov, Sh. A. Ayupov and B. B. Yusupov, *Local and 2-local derivations on filiform associative algebras*, arXiv:2305.15339v1 (2023-05-24), https://arxiv.org/abs/2305.15339.
3. *Idempotent derivations and a sharp half-rank bound in free two-step associative algebras*, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-idempotent-derivations-and-a-sharp-half-rank-bound-in-free-two-s--e1791f7dab62.
4. *Local derivations of free two-step nilpotent Lie algebras*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-local-derivations-of-free-two-step-nilpotent-lie-algebras--ba6a85ab40e2.
5. *A one-dimensional two-local derivation defect for free two-step nilpotent Lie algebras*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-one-dimensional-two-local-derivation-defect-for-free-two-step--9aecdcbb9415.
6. V. Drensky and L. Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two*, arXiv:1909.13262 (2019), https://arxiv.org/abs/1909.13262.
