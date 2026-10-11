# Exact Euclidean Banach–Mazur distance of the \(\ell_\infty-\ell_1\) Day–James plane
## Finding
For the real Day–James plane \(X=\ell_\infty-\ell_1\) on \(\mathbb{R}^2\), define
\[
N(x,y)=
\begin{cases}
\max\{|x|,|y|\},&xy\ge 0,\\
|x|+|y|,&xy\le 0.
\end{cases}
\]
Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac43,
\qquad
d_{\mathrm{BM}}(X,\ell_2^2)=\frac2{\sqrt3}.
\]
An optimal Euclidean pullback norm is, up to positive scaling,
\[
|(x,y)|_*^2=x^2-xy+y^2.
\]
Equivalently,
\[
|(x,y)|_*^2\le N(x,y)^2\le \frac43 |(x,y)|_*^2
\qquad ((x,y)\in\mathbb{R}^2).
\]
Yang and Wang computed \(C_{\mathrm{NJ}}(X)=(3+\sqrt5)/4\) for this same Day–James plane. Hence the exact Hilbertian distance found here has the strict gap
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2-C_{\mathrm{NJ}}(X)
=\frac{7-3\sqrt5}{12}>0.
\]

## Assumptions and scope
The scalar field is real and the space is two-dimensional. The norm is exactly the endpoint Day–James norm displayed above. The Banach–Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)=
\inf_T \|T\|\,\|T^{-1}\|,
\]
where the infimum ranges over invertible real linear maps from \(X\) to \(\ell_2^2\). Equivalently, its square is the least distortion \(M/m\) among positive-definite quadratic forms \(q\) satisfying \(m q(z)\le N(z)^2\le M q(z)\) for all \(z\).

The claim does not classify all Day–James spaces, all polygonal norms, or higher-dimensional analogues. The stated comparison with \(C_{\mathrm{NJ}}\) uses Yang–Wang’s published exact value for this same norm.

## Proof
Put
\[
u=\frac{x+y}{\sqrt2},
\qquad
v=\frac{x-y}{\sqrt2}.
\]
Then \(xy=(u^2-v^2)/2\). Directly from the two branches of \(N\),
\[
N(u,v)=
\begin{cases}
(|u|+|v|)/\sqrt2,&|u|\ge |v|,\\
\sqrt2|v|,&|v|\ge |u|.
\end{cases}
\]
The norm is invariant under the coordinate swap \((x,y)\mapsto(y,x)\), which becomes \((u,v)\mapsto(u,-v)\), and under central sign change. Their products therefore give independent sign changes of \(u\) and \(v\).

Let \(q\) be any positive-definite quadratic form with
\[
mq(z)\le N(z)^2\le Mq(z)
\qquad(z\in\mathbb{R}^2).
\]
Average \(q\) over the four sign changes of \((u,v)\). Because each is an isometry of \(N\), the averaged form \(\bar q\) satisfies the same inequalities with the same \(m,M\). The mixed term cancels, so \(\bar q=a u^2+b v^2\) with \(a,b>0\). Scaling does not affect distortion, hence it is enough to study
\[
q_t(u,v)=u^2+t v^2,
\qquad t>0.
\]
This symmetrization is the global reduction from arbitrary Euclidean pullbacks; it is not an ansatz.

By sign invariance take \(u,v\ge0\). In the sector \(0\le v\le u\), set \(s=v/u\in[0,1]\). Then
\[
\rho_t(s)=\frac{N(u,v)^2}{q_t(u,v)}
=\frac{(1+s)^2}{2(1+t s^2)}.
\]
Its derivative has the sign of \(1-ts\). In the sector \(0\le u\le v\), put \(r=u/v\in[0,1]\). Then
\[
\sigma_t(r)=\frac{N(u,v)^2}{q_t(u,v)}
=\frac2{t+r^2},
\]
which is decreasing in \(r\).

Comparing the sector extrema gives the exact squared distortion
\[
D(t)=
\frac{\sup_{z\ne0} N(z)^2/q_t(z)}
     {\inf_{z\ne0} N(z)^2/q_t(z)}
=
\begin{cases}
4/t,&0<t\le3,\\
(t+1)^2/(4t),&t\ge3.
\end{cases}
\]
For \(0<t\le3\), the upper extremum is \(2/t\) and the lower extremum is \(1/2\). For \(t\ge3\), the upper extremum is \((t+1)/(2t)\) and the lower extremum is \(2/(t+1)\). The first branch decreases, while the second is increasing for \(t\ge3\). Thus the unique minimizing parameter is \(t=3\), with \(D(3)=4/3\).

Finally,
\[
u^2+3v^2=2(x^2-xy+y^2).
\]
Rescaling the quadratic form yields \(|(x,y)|_*^2=x^2-xy+y^2\), and the sharp inequalities are
\[
|(x,y)|_*^2\le N(x,y)^2\le\frac43 |(x,y)|_*^2.
\]
Sharpness is visible at explicit vectors: the lower ratio equals \(1\) at \((1,1)\) and \((1,0)\), while the upper ratio equals \(4/3\) at \((1,-1)\). The symmetrization step shows that no nonsymmetric Euclidean pullback can have smaller distortion.

## Verification
The proof is exact and analytic. The bundled checker replays the coordinate identity, the branch value at the minimizing parameter, and the equality witnesses using rational arithmetic; it is supplementary and is not used as a substitute for the global calculus argument.

For \(t=3\), the two one-variable formulas have global ratio \(4/3\). The positive-definiteness of \(x^2-xy+y^2\) follows from its matrix eigenvalues \(1/2\) and \(3/2\). Boundary points with \(xy=0\) are consistent because the two defining branches of \(N\) agree there.

## Relationship to prior work
Yang and Wang introduced the coefficient used to compute the von Neumann–Jordan constant of this exact \(\ell_\infty-\ell_1\) Day–James plane and proved
\[
C_{\mathrm{NJ}}(X)=\frac{3+\sqrt5}4.
\]
Their inspected article defines the same norm and derives this constant, but does not discuss Banach–Mazur distance; full-text searches for “Banach–Mazur” and “Mazur” returned no occurrence.

A later 2019 proceedings treatment of Day–James spaces defines Banach–Mazur distance and gives a sufficient equality regime \(d_{\mathrm{BM}}(X,\ell_2^2)=\sqrt{C_{\mathrm{NJ}}(X)}\) for parameters with finite \(p\). The displayed statement assumes \(p<\infty\), so it does not cover the endpoint \(p=\infty\) studied here. The present formula shows that at this endpoint the squared Banach–Mazur distance is strictly larger than the known von Neumann–Jordan constant.

Semantic searches of the published-record index for the exact endpoint, its aliases, the Euclidean distance, and the constant comparison did not return a statement implying the formula above. Those negative searches are supportive only; originality assessment rests principally on statement-level comparison with the inspected sources.

## Limitations
The result is restricted to the real two-dimensional \(\ell_\infty-\ell_1\) Day–James norm. It does not assert a formula for neighboring finite parameters, complex scalars, or higher dimensions. The literature search cannot logically exclude every obscure equivalent formulation, so an unlocated older convex-geometric computation of the same optimal ellipse remains a residual bibliographic risk. No independent audit has been performed.

## References
1. C. Yang and F. Wang, “On a new geometric constant related to the von Neumann–Jordan constant,” *Journal of Mathematical Analysis and Applications* 324 (2006), 555–565. DOI: 10.1016/j.jmaa.2005.12.009. Available online 18 January 2006.
2. 2019 proceedings contribution on Day–James spaces and Banach–Mazur distance, relevant discussion on the Day–James family and the finite-parameter equality criterion, https://bm.skr.jp/r19/proceedings.pdf.
