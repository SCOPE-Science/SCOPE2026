# Exact \(R^{-1}\) tail for Haar rank-one Sylvester projections

## Finding
For a fixed, uniformly separated and uniquely solvable coupled generalized Sylvester system with a rank-one exact solution, independent Haar rank-one trial subspaces in a standard orthogonal Petrov–Galerkin compression produce an almost-surely finite approximate solution whose Frobenius norm has the exact tail
\[
\lim_{R\to\infty}R\Pr(\|\widetilde X\|_F>R)
=\frac{2\operatorname{arsinh}(1)}{\pi^2}=0.178603630135826\ldots.
\]
The same limit holds for the approximation error \(\|\widetilde X-X\|_F\). Consequently, for either random norm, its positive \(p\)-th moment is finite if and only if \(0<p<1\). In particular, both its expected norm and expected squared error are infinite, despite a full Sylvester operator with Frobenius separation exactly one. This is a theorem about independent Haar trial spaces in the general projection framework, **not** about the paper's structured extended/rational Krylov algorithms.

## Assumptions and scope
Work over the real numbers, in exact arithmetic. Write \(e_1=(1,0)^\mathsf T\), \(I=I_2\), and set
\[
E_1=E_2=I,\quad A_1=\operatorname{diag}(1,3),\quad A_2=\operatorname{diag}(2,4),
\quad B_1=e_1,\quad C_1=e_1^\mathsf T,\quad B_2=0,\quad C_2=0.
\]
The coupled matrix equations are
\[
A_1X+YA_2=-e_1e_1^\mathsf T,\qquad X+Y=0.
\]
Choose independent, uniformly distributed unit vectors \(u,v\in\mathbb S^1\), and put all four one-column projection/test bases equal in the corresponding direction: \(\widehat V_x=\widehat V_y=u\), \(\widehat W_x=\widehat W_y=v\). The test-basis prescription \(\widehat V_y=\operatorname{orth}(E_1\widehat V_x)\), \(\widehat W_x=\operatorname{orth}(E_2^\mathsf T\widehat W_y)\) is satisfied, up to harmless column signs. Let \(\widehat x,\widehat y\) solve the two scalar reduced equations, and lift \(\widetilde X=\widehat x uv^\mathsf T\), \(\widetilde Y=\widehat y uv^\mathsf T\).

## Proof
**1. Well-conditioning and exact solution.** Eliminating \(Y=-X\) yields \(A_1X-XA_2=-e_1e_1^\mathsf T\). On the four orthonormal matrix units, the Sylvester operator has eigenvalues \(-1,-3,1,-1\). Its minimal singular value in the Frobenius norm is therefore exactly \(1\), so the coupled equations have the unique solution \(X=e_1e_1^\mathsf T\), \(Y=-e_1e_1^\mathsf T\). Both coefficient matrices are positive definite, and both solutions have rank one and norm one.

**2. The random scalar denominator.** Let \(s=u_2^2\), \(t=v_2^2\). Both are independent \(\operatorname{Beta}(1/2,1/2)\) random variables, with density \(f(z)=[\pi\sqrt{z(1-z)}]^{-1}\) on \((0,1)\). Orthogonal projection gives
\[
(1+2s)\widehat x+(2+2t)\widehat y=-u_1v_1,
\qquad\widehat x+\widehat y=0,
\]
so
\[
\widehat x=-\frac{u_1v_1}{2(s-t)-1},\qquad
Z:=\|\widetilde X\|_F=|\widehat x|
=\frac{\sqrt{(1-s)(1-t)}}{|2(s-t)-1|}.
\]
The denominator is zero only on the line \(s=t+1/2\), a null set for the joint continuous law. Thus the reduced problem is uniquely solvable almost surely.

**3. Exact first-order tail.** Put \(r=\sqrt{1-s}\in(0,1)\); its density is \(g(r)=2/[\pi\sqrt{1-r^2}]\). Conditional on \(t\), write \(a=1/2-t\), \(d=\sqrt{1-t}/(2R)\). The tail event is precisely
\[
\{Z>R\}=\{|r^2-a|<dr\}.
\]
For \(0<t<1/2\), the allowable interval is \((r_-,r_+)\) where
\[
r_\pm=\frac{\sqrt{d^2+4a}\pm d}{2},\qquad r_+-r_-=d.
\]
For every \(R\ge2\), these intervals lie in a fixed compact subset of \([0,1)\), so \(g\) is uniformly bounded there; this gives a uniform \(O(R^{-1})\) bound on the conditional tail. As \(R\to\infty\), both endpoints tend to \(\sqrt a\), hence
\[
\lim_{R\to\infty}R\Pr(Z>R\mid t)
=\frac{\sqrt{1-t}}{\pi\sqrt{t+1/2}},\qquad 0<t<1/2.
\]
If \(t>1/2\), write \(c=t-1/2>0\). The tail condition becomes \(r^2-dr+c<0\), which requires \(d^2>4c\); thus \(0<c<1/(16R^2)\). Its root interval is at most \(d\le1/(2R)\) wide, within \(r\le1/(2R)\). Since the density of \(t\) is bounded near \(1/2\), the entire \(t>1/2\) contribution is \(O(R^{-3})\). Dominated convergence on \((0,1/2)\), using the integrable arcsine density of \(t\), therefore yields
\[
\begin{aligned}
\lim_{R\to\infty}R\Pr(Z>R)
&=\frac1{\pi^2}\int_0^{1/2}\frac{dt}{\sqrt{t(t+1/2)}}\\
&=\frac{2\operatorname{arsinh}(1)}{\pi^2}=:C>0.
\end{aligned}
\]
The last integral follows by substituting \(t=\sinh^2(q)/2\), for \(0\le q\le\operatorname{arsinh}(1)\).

**4. Error tails and moment cutoff.** Since \(\|X\|_F=1\), the reverse triangle inequality gives \(|\|\widetilde X-X\|_F-Z|\le1\). Comparing tails at thresholds \(R-1\) and \(R+1\) establishes the same constant \(C\) for the error. For either nonnegative random variable \(W\), the layer-cake identity
\[
\mathbb E W^p=p\int_0^\infty R^{p-1}\Pr(W>R)\,dR
\]
implies finite moments exactly when \(0<p<1\), because \(\Pr(W>R)\sim C/R\). It also gives the logarithmic truncated first-moment law \(\mathbb E\min(W,R)\sim C\log R\) and the linearly truncated second-moment law \(\mathbb E\min(W,R)^2\sim2CR\).

## Verification
Run `python verify.py` with Python, NumPy, SymPy and SciPy. The script checks both original coupled equations and all four exact Sylvester spectral gaps, reconstructs the scalar projection denominator and the hyperbolic integral, and numerically evaluates the **exact one-dimensional conditional-probability integral** for several finite tail thresholds. Numerical quadrature supports but does not replace the analytic proof of the \(R\to\infty\) limit.

## Relationship to prior work
Zulfiqar (2026), Sections 2.1–2.4, introduces this general coupled Petrov–Galerkin framework and proves a sufficient **disjoint field-of-values** condition for every projected problem to be uniquely solvable. Here \(\mathcal F(A_1)=[1,3]\) and \(\mathcal F(A_2)=[2,4]\) intersect, so that sufficient hypothesis does not apply, even though the full coefficient spectra are disjoint. The new point is the precise random-projection tail and moment cutoff, not the general possibility of projected near-resonance. Beckermann, Kressner and Tobler (2013) analyze tensor-Galerkin errors under a positive-definite full Kronecker operator and rational Krylov spaces, rather than the present indefinite operator and Haar trial spaces. Beckermann (2011) studies rational Galerkin residual/error bounds. Fasi and Hashemi (2026) examine conditioning of the **exact** Sylvester solution, a different conditioning question. Broader historical priority for reciprocal-gap tails is not ruled out.

## Limitations
This exact constant requires the displayed two-dimensional diagonal pair, rank-one forcing, independent real Haar trial directions and exact arithmetic. The conclusion does not imply failure of rational/extended Krylov algorithms, does not cover arbitrary random projection designs or higher reduced ranks, and does not show any finite-precision behavior. The almost-sure existence of the reduced solution is compatible with its infinite mean absolute norm; a simulated finite sample cannot establish divergence of a population moment. No independent mathematical review has been performed.

## References
- Umair Zulfiqar, *Numerical Solution of Large-Scale Low-Rank Coupled Generalized Sylvester Equations*, arXiv:2610.30804v1 (first submitted 2026-10-22), https://arxiv.org/abs/2610.30804 .
- Bernhard Beckermann, Daniel Kressner, and Christine Tobler, *An Error Analysis of Galerkin Projection Methods for Linear Systems with Tensor Product Structure*, SIAM J. Numer. Anal. 51 (2013), 3307–3326, https://doi.org/10.1137/120900204 .
- Bernhard Beckermann, *An Error Analysis for Rational Galerkin Projection Applied to the Sylvester Equation*, SIAM J. Numer. Anal. 49 (2011), 2430–2450, https://doi.org/10.1137/110824590 .
- Massimiliano Fasi and Behnam Hashemi, *Conditioning of solutions to the Sylvester equation*, arXiv:2609.04050v1 (2026), https://arxiv.org/abs/2609.04050 .
