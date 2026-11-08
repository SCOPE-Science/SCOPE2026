# A sharp logarithmic spectral-sampling transition for real Cesàro eigenvectors

## Finding
For every \(1<p<2\), let \(q=p/(p-1)\), \(\Delta=1/p-1/q=(2-p)/p\), and consider the real-variable Cesàro operator
\[
(C_pf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt,\qquad 0<x<1.
\]
For each real \(c>0\) and integer \(n\ge1\), set
\[
z_n=\tfrac12+ic\log(n+1),\qquad \lambda_n=z_n^{-1},\qquad v_n(x)=x^{z_n-1}(1-x)^{-z_n}.
\]
Let \(M_c\) be their closed complex linear span in \(L^p(0,1)\). Then
\[
0<c<\frac{\Delta}{\pi}\quad\Longrightarrow\quad M_c=L^p(0,1),
\]
whereas
\[
c>\frac{\Delta}{\pi}\quad\Longrightarrow\quad\operatorname{codim}M_c=\infty.
\]
All \(v_n\) are eigenvectors \(C_pv_n=\lambda_nv_n\). Both conclusions concern a discrete family of eigenvalues tending to the same spectral-boundary point \(0\). No assertion is made for the critical equality \(c=\Delta/\pi\).

## Assumptions and scope
Complex \(L^p(0,1)\) is taken with Lebesgue measure and \(1<p<2\). Its dual is identified with \(L^q(0,1)\) using the bilinear annihilator pairing \(\int_0^1 fg\,dx\). Define the open strip
\[
S=\{z\in\mathbb C: l<\operatorname{Re}z<r\},\qquad l=1/q,\quad r=1/p,\quad r-l=\Delta.
\]
For any \(z\in S\), let \(v_z(x)=x^{z-1}(1-x)^{-z}\) with real logarithms of \(x\) and \(1-x\). Then
\[
\|v_z\|_p^p=\mathrm B\bigl(p(\operatorname{Re}z-l),p(r-\operatorname{Re}z)\bigr)<\infty.
\]
The identity \(\frac{d}{dx}(x/(1-x))^z=z x^{z-1}(1-x)^{-z-1}\) gives \(C_pv_z=z^{-1}v_z\). Since \(l<1/2<r\), every listed eigenvector is legitimate.

## Proof
**1. The annihilator's holomorphic transform.** For \(g\in L^q(0,1)\) define
\[
F_g(z)=\int_0^1g(x)x^{z-1}(1-x)^{-z}\,dx,\qquad z\in S.
\]
By Hölder's inequality and the beta integral, \(F_g\) is analytic on \(S\) and bounded on every strictly smaller closed vertical substrip. In particular it is a bounded analytic function on any centered strip \(S_d=\{|\operatorname{Re}z-1/2|<d/2\}\) with \(0<d<\Delta\). Introduce \(t=\log(x/(1-x))\), so \(x=e^t/(1+e^t)\), \(dx=x(1-x)\,dt\). With \(h(t)=g(x(t))(1-x(t))\),
\[
F_g(z)=\int_{\mathbb R}h(t)e^{zt}\,dt.
\]
If \(F_g\equiv0\) on \(S\), its restriction to \(z=1/2+iy\) is the Fourier transform of the integrable function \(h(t)e^{t/2}\). Uniqueness of the Fourier transform gives \(h=0\), hence \(g=0\) almost everywhere.

**2. Density below the threshold.** Suppose \(0<c<\Delta/\pi\). Choose \(d\) with \(\pi c<d<\Delta\). A conformal map from \(S_d\) onto the disk is
\[
\zeta_d(z)=\frac{w_d(z)-i}{w_d(z)+i},\qquad
w_d(z)=\exp\left(\frac{i\pi}{d}(z-\tfrac12+\tfrac d2)\right).
\]
At the sample points \(z_n\), the map has the values
\[
\zeta_d(z_n)=-\frac{1-u_n}{1+u_n},\qquad u_n=(n+1)^{-\pi c/d}.
\]
Thus \(1-|\zeta_d(z_n)|=2u_n/(1+u_n)\), and the sum over \(n\) diverges because \(\pi c/d<1\). By the classical Blaschke necessary condition for zeros of a nonzero bounded analytic disk function, any bounded analytic \(F_g\) vanishing at every \(z_n\) must vanish identically. Fourier uniqueness from Step 1 then gives \(g=0\). Since there is no nonzero dual annihilator, Hahn–Banach implies \(M_c=L^p(0,1)\).

**3. An annihilator above the threshold.** Suppose \(c>\Delta/\pi\), and choose \(d'\) so that \(\Delta<d'<\pi c\). Let \(S_{d'}\) and \(\zeta_{d'}\) be defined as above. The points \(z_n\) are inside \(S_{d'}\); their disk images are \(-r_n\) where
\[
r_n=\frac{1-u_n}{1+u_n},\qquad u_n=(n+1)^{-\pi c/d'}.
\]
Now \(\sum_n(1-r_n)<\infty\). The convergent Blaschke product
\[
B(z)=\prod_{n\ge1}\frac{\zeta_{d'}(z)+r_n}{1+r_n\zeta_{d'}(z)}
\]
is analytic, bounded by one in modulus, not identically zero, and vanishes at every \(z_n\). Define \(F(z)=e^{z^2}B(z)\) on \(S_{d'}\). For each fixed real \(b\) strictly inside this strip, \(|F(b+iy)|\le e^{b^2-y^2}\). Taking the inverse Fourier transform on the central vertical line, set
\[
h(t)=\frac{e^{-t/2}}{2\pi}\int_{\mathbb R}F(\tfrac12+iy)e^{-iyt}\,dy.
\]
Cauchy's theorem on horizontal rectangles, with the Gaussian horizontal decay, permits shifting the integral to any line \(\operatorname{Re}z=b\) strictly inside \(S_{d'}\). Consequently
\[
h(t)=\frac{e^{-bt}}{2\pi}\int_{\mathbb R}F(b+iy)e^{-iyt}\,dy,
\qquad |h(t)|\le C_b e^{-bt},
\]
where \(C_b<\infty\). Fourier inversion on each line yields \(F(z)=\int_{\mathbb R}h(t)e^{zt}\,dt\) for \(z\in S_{d'}\). Indeed the displayed exponential bounds from two enclosing vertical lines guarantee the absolute convergence, while analyticity extends the inversion identity off a chosen line.

Because \(d'>\Delta\), choose two interior real points \(b_-<l\) and \(b_+>r\). Define \(g(x(t))=h(t)/(1-x(t))\). Direct substitution gives
\[
\int_0^1|g(x)|^q\,dx
=\int_{\mathbb R}|h(t)|^q x(t)(1-x(t))^{1-q}\,dt.
\]
The weight on the right is asymptotic to \(e^t\) at negative infinity and to \(e^{(q-1)t}\) at positive infinity. The bounds \(|h(t)|\le C_{b_-}e^{-b_-t}\) for \(t<0\) and \(|h(t)|\le C_{b_+}e^{-b_+t}\) for \(t>0\) prove integrability, since \(qb_-<1\) and \(qb_+>q-1\). Thus \(g\in L^q(0,1)\), with \(F_g=F\) on \(S\). In particular \(F_g(z_n)=0\) for every \(n\). Since \(F\not\equiv0\), \(g\ne0\), and \(M_c\) is not dense.

**4. Infinite codimension.** For each nonnegative integer \(j\), translate \(h_j(t)=h(t-j)\) and define \(g_j(x(t))=h_j(t)/(1-x(t))\). Each \(g_j\) belongs to \(L^q\) by the same two exponential estimates, and its transform equals \(e^{jz}F(z)\); hence it annihilates every \(v_n\). For any finite scalar family, \(\sum_j a_je^{jz}F(z)\equiv0\) forces every \(a_j=0\), because \(F\not\equiv0\) and distinct exponential monomials are linearly independent on a nonempty open set. Thus the annihilator of \(M_c\) is infinite-dimensional, and \(M_c\) has infinite codimension.

## Verification
The result is analytic and does not rely on finite truncations. The integrability thresholds follow directly from the logistic Jacobian and the strict interior contour choices; the disk-map identities are elementary. The construction invokes only the classical Blaschke zero-condition, convergence of Blaschke products and Fourier inversion with Gaussian-decaying holomorphic data. Explicit strict inequalities are needed in both halves; the equality case is intentionally unproved.

## Relationship to prior work
Belli, Gül, Ross and Siskakis identify \(v_z\), determine the point spectrum of \(C_p\), and explicitly pose the infinite-set eigenvector-span question in Example 6.5 of their 2026 work. Their result does not state a logarithmic sampling threshold. This theorem resolves that question for an intrinsic vertical sampling sequence and quantifies the sharp dense-versus-infinite-codimension transition. Classical strip/Blaschke and bilateral-Laplace facts are tools, not claimed as original; Harper's vertical-strip Laplace representation is relevant general background but does not supply this operator-specific threshold. General weighted exponential completeness theorems remain potential antecedents.

## Limitations
No assertion at \(c=\Delta/\pi\); no full characterization of arbitrary eigenvalue subsets \(E\), no unconditional novelty certification and no independent mathematical audit. The non-density portion gives infinite algebraic codimension, not a formula for a projection or a basis for the quotient.

## References
1. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, “Crescents and the Real Variable Cesàro Operator,” first public preprint 2026-06-07, arXiv:2606.08600; *Integral Equations and Operator Theory* 98, article 42 (2026), doi:10.1007/s00020-026-02865-7, in particular Example 6.5.
2. Z. Harper, “Laplace transform representations and Paley-Wiener theorems for functions on vertical strips,” *Documenta Mathematica* (2010), https://ems.press/journals/dm/articles/8965229. General analytic-strip background.
3. Classical Blaschke zero-set criterion for bounded analytic functions on the unit disk and Fourier inversion uniqueness, as standard analytic tools.
