# Principal-angle spectra for commutators of Gaussian-Fock composition projections

## Finding

Let \(d\ge1\), let \(E,F\) be arbitrary complex-linear subspaces of \(\mathbb C^d\), and write \(P,Q\) for their orthogonal projections. On the standard Gaussian Fock Hilbert space \(\mathcal F_d\), put \(C_Pf=f\circ P\), \(C_Qf=f\circ Q\), and \(D=[C_P,C_Q]=C_PC_Q-C_QC_P\). Let \(c_1,\ldots,c_r\) be **all strictly positive singular values, with multiplicity**, of \(P|_F:F\to E\); each lies in \((0,1]\). For \(\alpha\in\mathbb N_0^r\), define \(t_\alpha=\prod_{j=1}^r c_j^{\alpha_j}\), including \(t_0=1\). For \(r=0\), the only product is \(t_0=1\).

**Exact singular spectrum.** All strictly positive singular values of \(D\), counting multiplicity, are
\[
 t_\alpha\sqrt{1-t_\alpha^2}\quad\text{twice for every }\alpha\in\mathbb N_0^r\text{ with }0<t_\alpha<1.
\]
There are no other positive singular values. Equivalently, the nonzero eigenvalues of the skew-adjoint \(D\) occur in pairs \(\pm i t_\alpha\sqrt{1-t_\alpha^2}\). Repeated numerical values originating from distinct multiindices retain their multiplicities. In particular,
\[
 \|D\|=\sup_{\alpha:\,0<t_\alpha<1}t_\alpha\sqrt{1-t_\alpha^2}\le\frac12,
\]
where an empty supremum is zero.

**Ideal and essential-norm transition.** For every \(0<p<\infty\), the following are equivalent: \(D\) is compact; \(D\in S_p\); and either \(E\cap F=\{0\}\) or \(P Q=Q P\). If \(E\cap F\ne\{0\}\) and \(PQ\ne QP\), then \(D\) is noncompact and \(\|D\|_{\rm ess}=\|D\|>0\). If \(E\cap F=\{0\}\), then all Schatten quasi-norms are finite and
\[
 \boxed{\quad\|D\|_{S_2}^2=2\left[\prod_{j=1}^{r}(1-c_j^2)^{-1}-\prod_{j=1}^{r}(1-c_j^4)^{-1}\right].\quad}
\]
Empty products are one. In the compact case, the full \(S_p\)-sum is twice the sum of \([t_\alpha\sqrt{1-t_\alpha^2}]^p\) over the indicated nontrivial multiindices.

**Sharp rank-one specialization.** If \(E,F\) are distinct one-dimensional subspaces with ray overlap \(0<c<1\), the positive singular values are \(c^k\sqrt{1-c^{2k}}\), each twice, for every integer \(k\ge1\). Then
\[
 \|D\|_{S_2}^2=\frac{2c^2}{1-c^4},\qquad
 \|D\|=\max_{k\ge1} c^k\sqrt{1-c^{2k}}.
\]
Writing \(q=c^2\), the smallest maximizing degree is the least integer \(k\ge1\) such that \(q^k\le(1+q)^{-1}\); at equality, degrees \(k\) and \(k+1\) tie. In particular, \(\|D\|\to\tfrac12\) as \(c\uparrow1\), although \(D=0\) when the two rays coincide.

## Assumptions and scope

The normalized Gaussian Fock space is the completion of holomorphic polynomials on \(\mathbb C^d\) for the inner product
\[
 \langle f,g\rangle=\pi^{-d}\int_{\mathbb C^d}f(z)\overline{g(z)}e^{-|z|^2}\,dV(z).
\]
The homogeneous degree-\(n\) summand is isometric to the symmetric tensor power \(\operatorname{Sym}^n(\mathbb C^d)\), including the one-dimensional vacuum summand at \(n=0\). The commutator convention is \([A,B]=AB-BA\). No subspace dimensions, transversality, or equal-rank assumptions are imposed, except the finiteness of \(d\). All spaces and operators are complex-linear.

## Proof

**1. Projection and symmetric-power reduction.** For an orthogonal projection \(P\), the reproducing exponentials \(e_w(z)=e^{\langle z,w\rangle}\) obey \(C_Pe_w=e_{Pw}\). The exponential vectors span a dense set. Hence \(C_P\) is the bosonic second quantization \(\Gamma(P)=\bigoplus_{n\ge0}P^{\odot n}\). It is an orthogonal projection onto the embedded Fock space over \(E\), and similarly \(C_Q=\Gamma(Q)\).

Let \(T=P|_F:F\to E\). The restriction of \(\Gamma(P)\Gamma(Q)\) from \(\operatorname{ran}\Gamma(Q)=\mathcal F(F)\) to \(\operatorname{ran}\Gamma(P)=\mathcal F(E)\) is \(\Gamma(T)=\bigoplus_{n\ge0}T^{\odot n}\). Choose a singular-vector basis for \(T\), with positive singular values \(c_1,\ldots,c_r\), and complete it using zero singular directions if needed. In the normalized occupation-number basis of \(\operatorname{Sym}^n(F)\), the nonzero singular values of \(T^{\odot n}\) are exactly
\[
 \prod_{j=1}^r c_j^{\alpha_j},\qquad \alpha_j\in\mathbb N_0,\quad \sum_j\alpha_j=n,
\]
with each occupation multiindex counted separately. Extra zero singular directions contribute only zero. Summing over all \(n\), and including the vacuum, proves that the positive cosines of the principal angles between the two Fock projection ranges are exactly the stated \(t_\alpha\).

**2. A two-projection commutator block.** For any two Hilbert-space orthogonal projections \(R,S\), a principal-angle cosine \(t\in(0,1)\) determines an orthonormal basis on its two-dimensional reducing plane in which
\[
 R=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 S=\begin{pmatrix}t^2&t\sqrt{1-t^2}\\t\sqrt{1-t^2}&1-t^2\end{pmatrix},\quad
 [R,S]=\begin{pmatrix}0&t\sqrt{1-t^2}\\-t\sqrt{1-t^2}&0\end{pmatrix}.
\]
Both singular values of the last block are \(t\sqrt{1-t^2}\), and its eigenvalues are \(\pm i t\sqrt{1-t^2}\). The complementary reducing blocks with angle zero or a right angle give zero commutator. Applying this finite-dimensional two-projection decomposition on each homogeneous degree of \(\mathcal F_d\), using Step 1, proves the complete singular spectrum and the operator-norm formula. This also accounts for collisions of products from distinct occupation indices.

**3. Compactness and Schatten classes.** The multiplicity of the singular value \(1\) of \(T\) equals \(\dim(E\cap F)\): equality in \(\|Px\|\le\|x\|\) holds precisely when \(x\in E\). If the intersection is zero, every positive \(c_j<1\). Put \(q=\max_j c_j<1\) (take \(q=0\) if \(r=0\)). If \(r=0\), then \(D=0\). Otherwise, every nontrivial positive degree-\(n\) product is at most \(q^n\), and there are at most \(\binom{n+r-1}{r-1}\) occupation indices of degree \(n\). Therefore for each \(p>0\), the sum of \([t_\alpha\sqrt{1-t_\alpha^2}]^p\) converges by comparison with a polynomial times \(q^{np}\), showing membership in all \(S_p\).

If \(E\cap F\ne\{0\}\) and \(P,Q\) do not commute, the classical principal-angle decomposition gives at least one \(c_j\in(0,1)\) and another \(c_\ell=1\). Keeping occupation one in the first mode and arbitrary occupation in the second gives the same positive commutator singular value infinitely often. Thus \(D\) is noncompact and outside every \(S_p\). If \(PQ=QP\), the functorial identity \(\Gamma(P)\Gamma(Q)=\Gamma(PQ)\) shows \(D=0\). These arguments prove the equivalences.

For the essential norm in the noncompact case, put \(K=E\cap F\) and decompose \(\mathbb C^d=K\oplus K^\perp\). Both projections act as identity on \(K\); the Fock factorization yields
\[
 D\simeq I_{\mathcal F(K)}\otimes D_0,
\]
where \(D_0\) is the commutator for the restricted projections on \(K^\perp\). Those restricted ranges have zero intersection, so \(D_0\) is compact; it is nonzero because the original projections do not commute. As \(\mathcal F(K)\) is infinite dimensional, orthonormal vectors in its first factor tensored with an almost-norming vector for \(D_0\) show that every compact perturbation of \(D\) has norm at least \(\|D_0\|\). The reverse inequality follows from \(\|D\|=\|D_0\|\), giving \(\|D\|_{\rm ess}=\|D\|\).

**4. Exact Hilbert--Schmidt norm.** With zero intersection, Step 2 gives
\[
 \tfrac12\|D\|_{S_2}^2
 =\sum_{\alpha\in\mathbb N_0^r}(t_\alpha^2-t_\alpha^4)
 =\prod_{j=1}^r\left(\sum_{m\ge0}c_j^{2m}\right)
 -\prod_{j=1}^r\left(\sum_{m\ge0}c_j^{4m}\right).
\]
The geometric series converge since every \(c_j<1\), yielding the stated determinant-product formula. The vacuum and all zero/right-angle contributions vanish automatically.

**5. Rank-one maximizer and discontinuity.** For one principal cosine \(c\in(0,1)\), the spectrum in Step 2 gives the rank-one formulas. Write \(q=c^2\) and \(a_k^2=q^k(1-q^k)\). Then
\[
 a_{k+1}^2-a_k^2=(1-q)q^k\bigl((1+q)q^k-1\bigr),
\]
which changes sign once and proves the maximizing-degree rule, including ties. As \(q\uparrow1\), integer powers \(q^k\) can approach \(1/2\) arbitrarily closely, so \(\max_k a_k\to1/2\); when \(c=1\), both projections coincide and their commutator is zero.

## Verification

The included standalone `checker.py` uses only Python's standard library and exact fractions. For twelve successive homogeneous degrees it builds the nonorthonormal monomial matrices of two rank-one Fock projections, checks weighted self-adjointness, the cubic commutator identity, and second/fourth trace moments. It also checks finite-degree truncations of the two-angle Hilbert--Schmidt generating function. The program's successful output is `FOCK_PROJECTION_PRINCIPAL_ANGLES_EXACT_OK 1705 rank_one_c=3/5 two_angle_S2_squared= 480625/100368`. This is a finite diagnostic; the all-degree formulas are established by the analytical proof above.

## Relationship to prior work

Bayart--Wang--Yao (2026) study linear-symbol composition operators and their iteration and semigroup structure; their primary-\(47B33\) work supplies the natural Fock composition setting but does not give this two-projection commutator singular spectrum. Jiang--Prajitura--Zhao (2016) classify ordinary Fock composition operators and show that compact ones belong to all Schatten classes, and cite the earlier compact-difference criterion. The qualitative compactness equivalence for the difference \(C_{PQ}-C_{QP}\), when the two symbols differ, follows from Choe--Izuchi--Koo (2010) and the corresponding Fock--Sobolev theorem of Cho--Choe--Koo (2014); **it is not claimed as a new independent criterion**. The quantitative contribution here is the entire principal-angle-product singular spectrum, exact Schatten norms, the trace formula, and essential-norm multiplicity mechanism. Standard two-projection and symmetric-tensor techniques are acknowledged as ingredients, not themselves new results.

## Limitations

The one-particle space is finite dimensional; no assertion is made for arbitrary infinite-dimensional subspaces or general affine symbols. The compactness and Schatten membership dichotomy is included to contextualize the exact spectrum, not claimed as new beyond published difference theorems. An earlier quantitative treatment under second-quantization terminology may exist; publication priority and independent verification have not been established. The 2010 and 2014 compact-difference articles were identifiable through their published abstracts, but their full texts were not available for inspection here. No finite computation substitutes for the proof.

## References

1. F. Bayart, M. Wang, X. Yao, *Semigroup of composition operators on the Fock space of several complex variables*, arXiv:2610.26349, first posted 2026-10-19; https://arxiv.org/abs/2610.26349.
2. L. Jiang, G. T. Prajitura, R. Zhao, *Some Characterizations for Composition Operators on the Fock Space*, arXiv:1608.05955 (2016); https://arxiv.org/abs/1608.05955.
3. B. R. Choe, K. H. Izuchi, H. Koo, *Linear sums of two composition operators on the Fock space*, J. Math. Anal. Appl. 369 (2010), 112–119, DOI 10.1016/j.jmaa.2010.02.029.
4. H. R. Cho, B. R. Choe, H. Koo, *Linear combinations of composition operators on the Fock-Sobolev spaces*, Potential Anal. 41 (2014), 1223–1246, DOI 10.1007/s11118-014-9417-6.
5. J. Stochel, J. B. Stochel, *Composition operators on Hilbert spaces of entire functions with analytic symbols*, J. Math. Anal. Appl. 454 (2017), 1019–1066, DOI 10.1016/j.jmaa.2017.05.021 (bibliographic/abstract inspection only).
