# The infinitesimal Picard quotient of the Hilario–Schröer generalized Igusa surface

## Finding

Let \(k\) be algebraically closed of prime characteristic \(p\geq3\). Let \(E/k\) be a supersingular elliptic curve containing its usual subgroup scheme \(G=\alpha_p\), acting on \(E\) by translation. Let \(X_p\) be the projective monomial-cusp curve with affine charts \(\operatorname{Spec}k[T^{p-1},T^p]\) and \(\operatorname{Spec}k[T^{-1}]\), equipped with the canonical \(G\)-action
\[
T^{-1}\longmapsto T^{-1}+aT^{-p},\qquad a^p=0.
\]
Let \(S_p=(E\times X_p)/G\), with the diagonal action. Then there are group-scheme isomorphisms
\[
\boxed{(\operatorname{Pic}^{0}_{X_p})^{G}\simeq\alpha_p^{\,p-2}},
\qquad
\boxed{\operatorname{Pic}^{0}_{S_p}/(\operatorname{Pic}^{0}_{S_p})_{\mathrm{red}}\simeq\alpha_p^{\,p-2}}.
\]
Thus the latter infinitesimal group has height one, length \(p^{p-2}\), and Lie dimension \(p-2\). The formula includes the already-known \(p=3\) case and determines the previously undetermined group-scheme structure for every \(p\geq5\).

## Assumptions and scope

Write \(H=\langle p-1,p\rangle\subset\mathbb Z_{\geq0}\), and let \(\mathcal G\) be its finite gap set. Its conductor is \((p-1)(p-2)\) and
\[
\mathcal G=\{jp+i:0\leq j\leq p-3,\ 1\leq i\leq p-2-j\},
\qquad |\mathcal G|=\frac{(p-1)(p-2)}2.
\]
Every gap is prime to \(p\). We use the Picard functor and the gluing description of \(X_p\) established in Proposition 5.4 of Fong–Maccan–Modin. For an arbitrary \(k\)-algebra \(R\), a degree-zero line bundle is represented locally by an invertible Laurent cocycle \(f(T)\), modulo multiplication on the left by units in \(R[T^{-1}]\) and on the right by units in \(R[[T^{p-1},T^p]]\). That proposition also establishes that \(\operatorname{Pic}^{0}_{X_p}\) is smooth, connected, of dimension \(|\mathcal G|\). The induced action on gluing cocycles is the substitution displayed above.

## Proof

**1. Additive coordinates on the curve Picard group.** For a normalized cocycle \(f(T)\) with invertible constant coefficient define the formal logarithmic derivative
\[
W_f(T)=-T\frac{f'(T)}{f(T)}=\sum_{n\in\mathbb Z}w_n(f)T^n.
\]
For each positive gap \(g\in\mathcal G\), the coefficient \(w_g\) is unaffected by the allowed changes of cocycle. Indeed, the logarithmic derivative of a unit in \(R[T^{-1}]\) has no positive powers, whereas the logarithmic derivative of a unit in \(R[[T^{p-1},T^p]]\) has support in \(H\). This is valid even for nonreduced test rings. Moreover \(W_{fg}=W_f+W_g\), so the \(w_g\) define an additive group morphism
\[
\Phi:\operatorname{Pic}^{0}_{X_p}\longrightarrow\mathbb G_a^{\,\mathcal G}.
\]
It is an isomorphism. To check this scheme-theoretically, use the morphism from affine space to the Picard group defined by the cocycle \(f=1+\sum_{g\in\mathcal G}c_gT^g\). On this affine space, the coefficient identity \(W_ff=-Tf'\) gives
\[
w_g=-g c_g+P_g(c_h:h<g).
\]
Each diagonal coefficient \(-g\) is a unit in characteristic \(p\), so \(\Phi\) composed with this cocycle morphism is a triangular polynomial automorphism. This supplies a section of \(\Phi\). Since a section of the separated group-scheme morphism \(\Phi\) is a closed immersion, and its image has the full dimension of the smooth connected (hence irreducible) Picard group, the section is surjective. Thus \(\Phi\) is a group-scheme isomorphism, not merely a bijection of geometric points.

The characteristic-\(p\) identity
\[
w_{pm}=w_m^p\qquad(m\geq1)
\]
holds for every normalized unit. For instance, factor \(f(T)=\prod_{d\geq1}(1-u_dT^d)\) formally and use \(w_n=\sum_{d\mid n}d\,u_d^{n/d}\). Summands with \(p\mid d\) vanish and Frobenius gives the displayed identity. The argument is universal over arbitrary characteristic-\(p\) coefficient rings.

**2. The exact coaction.** The action on \(T\) is
\[
T\longmapsto T'=\frac{T}{1+aT^{1-p}},\qquad a^p=0.
\]
The chain rule, in characteristic \(p\), yields
\[
W_{f(T')}(T)=\frac{1}{1+aT^{1-p}}\,W_f\!\left(\frac{T}{1+aT^{1-p}}\right).
\]
For a gap \(g=jp+i\) as in the scope, expansion of the coefficient of \(T^g\) gives, using \(\binom{g+mp}{m}\equiv\binom{i}{m}\pmod p\) for \(0\leq m<p\),
\[
\sigma(w_{jp+i})=
\sum_{m=0}^{i-1}(-1)^m\binom{i}{m}a^m
w_{(j+m)p+i-m}
+(-1)^i a^i w_{j+i}^{p}.
\tag{1}
\]
The intermediate indices in the sum are gaps, and the final index before Frobenius is \((j+i)p\); the ghost Frobenius identity was used for that term. Terms with \(m>i\) vanish modulo \(p\). Formula (1) is a formula in the entire coordinate ring tensored with \(k[a]/(a^p)\), not only on geometric points.

**3. The scheme-theoretic fixed locus.** Because \(G=\alpha_p\) is a height-one group scheme, a point is fixed exactly when the vector field given by the coefficient of \(a\) vanishes. More explicitly, if the coefficient of \(a\) is zero on all coordinate functions, its associated derivation is zero after evaluation, and all higher coefficients of the restricted exponential coaction vanish as well (the factorials below \(p\) are invertible). From (1), this vector field satisfies
\[
D(w_{jp+i})=
\begin{cases}
-i\,w_{(j+1)p+i-1},&i\geq2,\\
-w_{j+1}^{p},&i=1.
\end{cases}
\]
As \((j,i)\) ranges over the gaps, the first type exhausts all \(w_g\) with \(g\in\mathcal G\) and \(g\geq p\), while the second exhausts \(w_1^p,\ldots,w_{p-2}^p\). Consequently the defining ideal of the full fixed subgroup is
\[
I=\bigl(w_g:g\in\mathcal G,\ g\geq p\bigr)
+\bigl(w_1^p,\ldots,w_{p-2}^p\bigr).
\]
Since the \(w_g\) are additive group coordinates, the fixed subgroup scheme is
\[
\operatorname{Spec}\frac{k[w_1,\ldots,w_{p-2}]}{(w_1^p,\ldots,w_{p-2}^p)}
\simeq\alpha_p^{p-2}
\]
as a group scheme. This determines nilpotent structure, not just dimension or reduced support.

**4. Transfer to the surface.** On the smooth chart with coordinate \(u=T^{-1}\), the action is \(u\mapsto u+a u^p\). Thus the smooth point \(u=0\) is \(G\)-fixed (the singular cusp need not be fixed as a section). Corollary 5.2 of Fong–Maccan–Modin, a consequence of the quotient-Picard theorem of Jensen, identifies the infinitesimal quotient of \(\operatorname{Pic}^{0}_{S_p}\) with the infinitesimal quotient of \((\operatorname{Pic}^{0}_{X_p})^G\). The latter is already finite and infinitesimal, so it equals its own infinitesimal quotient. This proves the asserted surface formula.

## Verification

The auxiliary `verify_ghost.py` provides independent finite-prime checks in characteristics \(3,5,7,11,13\): the gap decomposition; direct formal logarithmic-derivative recurrences for random normalized cocycles; the complete coefficient identity (1) in the truncated parameter ring; the Frobenius ghost identity; and the generators of the fixed-point ideal. It passes in all five characteristics. These tests support but do not replace the preceding general proof.

For illustration, when \(p=5\), the gap set is \(\{1,2,3,6,7,11\}\). The first-order equations force \(w_6=w_7=w_{11}=0\) and \(w_1^5=w_2^5=w_3^5=0\), giving exactly \(\alpha_5^3\), of length \(125\).

## Relationship to prior work

Fong, Maccan and Modin, Proposition 5.4, establish the smooth additive Picard group of \(X_p\) and its induced \(\alpha_p\)-action. Their Theorem D establishes its infinitesimal Lie dimension \(p-2\), and their Remark 5.9 explicitly leaves the group-scheme structure for the Hilario–Schröer examples as a question. Their Proposition 5.5 treats the \(p=3\) quasi-bielliptic instance, where the answer \(\alpha_3\) is already known. The new input here is the ghost-coordinate coaction (1), giving the entire nonreduced fixed subgroup simultaneously for all \(p\geq5\). Hilario and Schröer constructed the underlying monomial-cusp curves and infinitesimal actions; their work does not give this fixed Picard subgroup classification.

## Limitations

The statement requires an algebraically closed field, the specific Hilario–Schröer \(X_p\) with its indicated canonical \(\alpha_p\)-action, and the contracted product with a supersingular elliptic curve. It classifies the infinitesimal Picard quotient, not the total Picard scheme or different actions and different compactifications. The finite-prime program is not a formal proof and does not address generalizations beyond this family. Publication-priority uncertainty remains for unindexed treatments of the same special fixed-point scheme.

## References

1. P. Fong, M. Maccan, L. Modin, *Generalizations of Igusa surfaces*, arXiv:2611.12201 (first submitted 2026-11-09), particularly Proposition 5.4, Corollary 5.2, Remark 5.9. https://arxiv.org/abs/2611.12201
2. C. Hilario, S. Schröer, *Generalizations of quasielliptic curves*, arXiv:2303.12324 (first submitted 2023-03-22), particularly Section 5. https://arxiv.org/abs/2303.12324
3. S. T. Jensen, *Picard schemes of quotients by finite commutative group schemes*, Math. Scand. 42 (1978), 197–210, Theorem 2.1. https://doi.org/10.7146/math.scand.a-11748
