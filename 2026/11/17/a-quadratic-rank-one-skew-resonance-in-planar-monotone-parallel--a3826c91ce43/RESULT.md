# A quadratic rank-one–skew resonance in planar monotone parallel sums

## Finding

The following is an exact two-parameter law for the parallel sum of a natural family of nonparamonotone monotone linear operators, including a singular limit where the sum becomes a relation. Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). Fix \(a,b>0\), unit vectors \(u,v\in\mathbb R^2\), and nonzero real numbers \(s_1,s_2\). Define
\[
M_1=a uu^\top+s_1J,\quad M_2=bvv^\top+s_2J,\quad A_j=M_j^{-1},\quad T=A_1\mathbin\square A_2=(M_1+M_2)^{-1}.
\]
Here the inverse in the last expression is the inverse **relation** and \(A\mathbin\square B=(A^{-1}+B^{-1})^{-1}\). Put \(c=|\langle u,v\rangle|\), \(h=s_1+s_2\), and \(d=ab(1-c^2)+h^2\). Each \(A_j\) is an invertible, everywhere-defined, maximally monotone, nonparamonotone linear map. The parallel sum \(T\) is maximally monotone and is paramonotone **if and only if** \(c<1\) or \(h=0\). If \(d>0\) it is a linear map with the exact spectral norm
\[
\boxed{\displaystyle \|T\|_{2\to2}=\frac{\sqrt{(a+b)^2+4h^2}+\sqrt{(a-b)^2+4ab c^2}}{2\,[ab(1-c^2)+h^2]}.}
\]
If \(d=0\), then \(v=\pm u\), \(h=0\), and \(T\) is the paramonotone relation with domain \(\operatorname{span}\{u\}\) and values
\[
T(tu)=\frac{t}{a+b}u+u^\perp,\qquad t\in\mathbb R.
\]
There is a **quadratic resonance** at this singular parameter. Fix \(s_0\ne0\), choose orthonormal coordinates with \(u=e_1\), let \(v_\theta=(\cos\theta,\sin\theta)\), and put \(s_1=s_0\), \(s_2=-s_0+t\). For \(|t|<|s_0|/2\), \((\theta,t)\to(0,0)\) off the origin, and \(|\theta|<\pi/2\),
\[
\boxed{\displaystyle \|T_{\theta,t}\|_{2\to2}\sim\frac{a+b}{ab\,\theta^2+t^2}.}
\]
Yet the resolvents \(R_{\theta,t}=(I+T_{\theta,t})^{-1}\) remain well-defined and obey the sharp first-order, **joint** modulus
\[
\boxed{\displaystyle \|R_{\theta,t}-R_{0,0}\|_{2\to2}=\frac{b|\theta|+|t|}{1+a+b}+O\big((|\theta|+|t|)^2\big),\qquad R_{0,0}=\frac{a+b}{1+a+b}e_1e_1^\top.}
\]
All asymptotics hold along arbitrary paths satisfying the stated restrictions; the second is an additive expansion, not a claim of differentiability of the operator norm at the origin.

## Assumptions and scope

All spaces are real Euclidean two-spaces with standard inner product and operator norm. The parameters \(a,b\) are strictly positive; both individual skew coefficients are nonzero. The parallel sum and every inverse at singular parameters are set-valued graph inverses. A monotone relation \(F\) is paramonotone when equality \(\langle x-y,p-q\rangle=0\) for \((x,p),(y,q)\in\operatorname{gra}F\) implies \((x,q),(y,p)\in\operatorname{gra}F\). No conclusion is asserted about all higher-dimensional operators or arbitrary (nonlinear) monotone operators. The resonance statements concern the indicated fixed-\(a,b,s_0\) two-parameter slice; they make no uniform claim as \(a,b,s_0\) vary.

## Proof

**Individual maps.** Since \(\det(a uu^\top+sJ)=s^2\), each \(M_j\) and \(A_j\) is invertible. The identity
\[
\operatorname{sym}(M^{-1})=M^{-\top}(a uu^\top)M^{-1}
\]
shows that \(A_j\) has rank-one nonzero positive-semidefinite symmetric part and is monotone. It is not paramonotone: for an invertible linear map, paramonotonicity requires its symmetric-part kernel to be contained in its (zero) kernel, which fails here. A continuous, full-domain monotone linear operator is maximally monotone.

**Exact singular-value law.** Write \(H=M_1+M_2=S+hJ\) with \(S=a uu^\top+bvv^\top\). Direct calculation gives
\[
\det H=ab(1-c^2)+h^2=d,\qquad \operatorname{tr}(H^\top H)=a^2+b^2+2ab c^2+2h^2.
\]
The two singular values of \(H\), in decreasing order, satisfy
\[
\sigma_1+\sigma_2=\sqrt{(a+b)^2+4h^2},\quad
\sigma_1-\sigma_2=\sqrt{(a-b)^2+4ab c^2},\quad \sigma_1\sigma_2=d.
\]
These follow by squaring the first two expressions using trace and determinant; all quantities are nonnegative and the ordering is correct. For \(d>0\), \(\|H^{-1}\|=1/\sigma_2=\sigma_1/d\), giving the displayed exact formula.

**Paramonotonicity and the singular graph.** If \(c<1\), then \(S\) is positive definite, so \(\operatorname{sym}(H^{-1})=H^{-\top}SH^{-1}\) is positive definite; consequently \(T=H^{-1}\) is strongly monotone and paramonotone. If \(c=1\) and \(h\ne0\), \(H\) is invertible while \(\operatorname{sym}(H^{-1})\) has rank one; since \(H^{-1}\) has zero kernel, it cannot be paramonotone. If \(c=1,h=0\), \(H=(a+b)uu^\top\). Graph inversion gives the stated domain and values. Given graph points \((tu,\frac{t}{a+b}u+z)\), \((ru,\frac{r}{a+b}u+w)\) for \(z,w\in u^\perp\), their monotonicity pairing is \((t-r)^2/(a+b)\), so equality forces \(t=r\) and cross-membership holds. Inversion of the continuous full-domain maximal monotone \(H\) preserves maximal monotonicity, including this endpoint.

**Quadratic and resolvent laws.** In the selected coordinates,
\[
H_{\theta,t}=a e_1e_1^\top+bv_\theta v_\theta^\top+tJ,\qquad \det H_{\theta,t}=ab\sin^2\theta+t^2.
\]
The exact norm formula has numerator tending to \(a+b\) as \((\theta,t)\to0\). The determinant is asymptotic to \(ab\theta^2+t^2\) uniformly along all nonzero paths, yielding the quadratic law. For the resolvent, put \(Q_{\theta,t}=(I+H_{\theta,t})^{-1}\). Monotonicity of \(H\) gives \(\|Q_{\theta,t}\|\le1\). The relation definition implies
\[
R_{\theta,t}=H_{\theta,t}(I+H_{\theta,t})^{-1}=I-Q_{\theta,t}
\]
even at \((0,0)\). The resolvent identity bounds its difference from the endpoint by \(\|H_{\theta,t}-H_{0,0}\|\le b|\sin\theta|+|t|\). More sharply, set \(q=(1+a+b)^{-1}\), \(Q_{0,0}=\operatorname{diag}(q,1)\), and \(\varepsilon=|\theta|+|t|\). Since matrix inversion is analytic near \(I+H_{0,0}\),
\[
R_{\theta,t}-R_{0,0}
=Q_{0,0}(H_{\theta,t}-H_{0,0})Q_{0,0}+O_{\|\cdot\|}(\varepsilon^2)
=q\begin{pmatrix}0&b\theta-t\\b\theta+t&0\end{pmatrix}+O_{\|\cdot\|}(\varepsilon^2).
\]
The spectral norm of the displayed off-diagonal matrix is \(q\max\{|b\theta-t|,|b\theta+t|\}=q(b|\theta|+|t|)\). The operator-norm reverse triangle inequality transfers the \(O(\varepsilon^2)\) remainder to the asserted scalar norm expansion. This completes all cases.

## Verification

A standalone Python checker, `CHECKER.py`, performs \(72\) independent exact-rational parameter checks, including the determinants, symmetric parts, trace and singular-value identities, and resolvent identity; it additionally checks three asymptotic probes numerically. Execute `python CHECKER.py` with Python and NumPy installed. The finite checks are corroboration only. The proof of every universal and asymptotic statement is the preceding direct matrix and graph calculation; no finite test substitutes for it.

## Relationship to prior work

Alwadani, *On Parallel Sums of Set-Valued Operators: Monotonicity, Paramonotonicity, and Decomposition Invariance* (arXiv:2611.05523v1), gives general monotonicity and inheritance of paramonotonicity when **both** summands are paramonotone (Theorems 3.4–3.5). Here **neither** input is paramonotone, and the classified output may or may not become so. The already-established kernel characterization of paramonotone linear operators, discussed in the classical Attouch–Théra/operator-splitting literature (Bauschke–Boţ–Hare–Moursi, arXiv:1110.4877), implies the *qualitative* matrix paramonotonicity test once the matrices are specified. That characterization is not presented as new. The proposed contribution is the complete explicit rank-one–skew parallel-sum model together with its spectral-norm law, quadratic two-parameter degeneracy and sharp first-order resolvent modulus across a multivalued endpoint. Existing perturbation theory for Hermitian positive-semidefinite parallel sums covers a different operator class and does not by itself imply this nonsymmetric singular law.

## Limitations

This is a precise finite-dimensional family, not a general classification of all monotone linear operators. The asymptotic constants depend on fixed positive \(a,b\), and no estimates uniform as they degenerate are asserted. The relation \(T_{0,0}\) is unbounded as a single-valued full-domain operator because it is not such an operator; its maximal-monotone resolvent nevertheless exists on all of \(\mathbb R^2\). Qualitative paramonotonicity criteria and basic resolvent nonexpansiveness are already known; the novelty assessment concerns only the combined sharp family-specific laws. Literature searching cannot rule out an unindexed or differently formulated earlier computation; this remains a priority risk. No independent audit has been performed.

## References

1. S. T. Alwadani, *On Parallel Sums of Set-Valued Operators: Monotonicity, Paramonotonicity, and Decomposition Invariance*, arXiv:2611.05523v1, first public 3 November 2026. https://arxiv.org/html/2611.05523v1
2. H. H. Bauschke, R. I. Boţ, W. L. Hare, W. M. Moursi, *Attouch–Théra duality revisited: paramonotonicity and operator splitting*, arXiv:1110.4877v1 (2011). https://arxiv.org/html/1110.4877v1
3. J. A. Fill and D. E. Fishkind, *The Moore–Penrose Generalized Inverse for Sums of Matrices*, SIAM Journal on Matrix Analysis and Applications 21 (2000), 629–635, https://doi.org/10.1137/S0895479897329692 (abstract inspected; not a source for the theorem above).
