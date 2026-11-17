# The short-perimeter law of random geodesic triangles determines Euler characteristic

## Finding
Let \(M\) be any smooth, compact, connected, boundaryless Riemannian surface, of total area \(A>0\) and Euler characteristic \(\chi(M)\). Sample \(X_1,X_2,X_3\) independently from normalized Riemannian area and put
\[
P=d(X_1,X_2)+d(X_2,X_3)+d(X_3,X_1),
\]
where \(d\) denotes intrinsic minimizing-geodesic distance. As \(\varepsilon\downarrow0\),
\[
\boxed{\mathbb P(P<\varepsilon)=\frac{\pi^2}{42A^2}\varepsilon^4-\frac{\pi^3\chi(M)}{990A^3}\varepsilon^6+o(\varepsilon^6).}
\]
Consequently the *single scalar population law* of \(P\) determines both \(A\) and \(\chi(M)\). The formula is valid for orientable and nonorientable surfaces alike. It has no boundary analogue asserted here.

## Assumptions and scope
The surface is fixed and smooth, with no boundary, and its metric is fixed as \(\varepsilon\to0\). Compactness provides a positive injectivity radius and uniform local Taylor remainders. The vertices are *independent and uniform by intrinsic area*, not boundary points, and every side is the shortest intrinsic distance. Ties have probability zero; sufficiently short triangles lie inside a common normal chart. The strict/weak event distinction is null since the perimeter has no small positive atoms.

## Proof
Fix the first sampled vertex \(p\). When \(P<\varepsilon\), each of the other two vertices is at distance below \(\varepsilon/2\) from \(p\), by the triangle inequality. Write \(X_2=\exp_p(\varepsilon u)\), \(X_3=\exp_p(\varepsilon v)\). On bounded normal-coordinate vectors the Gaussian curvature \(K=K(p)\) gives the uniform expansions
\[
\frac{P}{\varepsilon}=\underbrace{|u|+|v|+|u-v|}_{h(u,v)}-\frac{K\varepsilon^2}{6}\underbrace{\frac{(u_1v_2-u_2v_1)^2}{|u-v|}}_{T(u,v)}+O(\varepsilon^3),
\]
\[
\frac{dA(\exp_p(\varepsilon u))dA(\exp_p(\varepsilon v))}{\varepsilon^4\,du\,dv}=1-\frac{K\varepsilon^2}{6}(|u|^2+|v|^2)+O(\varepsilon^3).
\]
Here \(T(u,u)=0\) by continuity. The distance expansion follows, for example, from the normal-coordinate squared-distance expansion \(d(\exp_p a,\exp_p b)^2=|a-b|^2-K(p)(a\wedge b)^2/3+O((|a|+|b|)^3|a-b|^2)\). The particular remainder bound is uniform on the required compact normal-coordinate region, even near \(u=v\).

Set \(\mathcal D=\{(u,v)\in\mathbb R^4:h(u,v)<1\}\) and define the three universal integrals
\[
I_0=\int_{\mathcal D}du\,dv,\quad I_1=\int_{\mathcal D}(|u|^2+|v|^2)du\,dv,\quad I_2=\int_{h=1}\frac{T}{|\nabla h|}\,dS.
\]
The coarea integral \(I_2\) also equals \(\int_{\mathbb R^4}T\,\delta(1-h)du\,dv\). To justify expansion of the indicator without distributional assumptions, introduce four-dimensional polar coordinates \((u,v)=\rho\omega\). On the unit three-sphere \(h(\omega)\) is bounded away from zero, while \(T(\rho\omega)=\rho^3T(\omega)\). The radial cutoff is uniformly
\[
\rho_*(\omega)=h(\omega)^{-1}+\frac{K\varepsilon^2T(\omega)}{6h(\omega)^4}+o(\varepsilon^2).
\]
Integrating the radial density \(\rho^3\), including its Jacobian correction, therefore yields uniformly in the base point
\[
\mathbb P(P<\varepsilon\mid X_1=p)=\frac{\varepsilon^4}{A^2}\left[I_0+\frac{K(p)\varepsilon^2}{6}(I_2-I_1)+o(\varepsilon^2)\right].
\]

Here is an exact evaluation of the three integrals. Put \(a=|u|\), \(b=|v|\), \(c=|u-v|\), and introduce nonnegative Heron variables \(x=(a+c-b)/2\), \(y=(a+b-c)/2\), \(z=(b+c-a)/2\), with \(w=x+y+z\). Then \(h=2w\), and integrating angular orientations gives
\[
du\,dv=4\pi\frac{(x+y)(y+z)(z+x)}{\sqrt{wxyz}}\,dx\,dy\,dz.
\]
Set \((x,y,z)=w(p,q,r)\), where \(p+q+r=1\), and \(F=(p+q)(q+r)(r+p)\). The simplex density \(1/\sqrt{pqr}\) has normalizing integral \(2\pi\), and its normalized Dirichlet \((1/2,1/2,1/2)\) moments give
\[
\mathbb E[F]=\frac4{21},\qquad \mathbb E[F((p+q)^2+(q+r)^2)]=\frac{32}{165}.
\]
Integrating \(0<w<1/2\) gives
\[
I_0=\frac{\pi^2}{42},\qquad I_1=\frac{2\pi^2}{495}.
\]
For the boundary term, \((u\wedge v)^2=4wxyz\), so homogeneity and the delta constraint \(2w=1\) reduce it to
\[
I_2=\frac\pi8\int_{p+q+r=1}(p+q)(q+r)\sqrt{pqr}\,dp\,dq.
\]
The Dirichlet \((3/2,3/2,3/2)\) normalizer is \(2\pi/105\), and the expectation of \((p+q)(q+r)\) is \(14/33\). Hence the last integral is \(4\pi/495\) and \(I_2=\pi^2/990\). Thus
\[
\frac{I_2-I_1}{6}=-\frac{\pi^2}{1980}.
\]
Average the conditional formula over the uniform first point \(p\). By Gauss--Bonnet, \(\int_M K\,dA=2\pi\chi(M)\); therefore the coefficient of \(\varepsilon^6\) is exactly \(-\pi^3\chi(M)/(990A^3)\), as claimed. The first nonzero coefficient separately determines \(A\), so the next one determines \(\chi(M)\).

## Verification
Run `python checker.py` with SymPy. It evaluates the Dirichlet moment identities and beta-integral for \(I_0,I_1,I_2\), and independently expands the exact short-side density of random triangles on the round unit sphere. Its expected success line is `SHORT_TRIANGLE_TOPOLOGY_CHECKS_OK`.

For the unit sphere, \(A=4\pi\), \(\chi=2\), giving
\[
\mathbb P(P<\varepsilon)=\frac{\varepsilon^4}{672}-\frac{\varepsilon^6}{31680}+O(\varepsilon^8).
\]
The sphere series is separately recovered by expanding the exact spherical side-coordinate density in trigonometric Heron variables. On any flat torus, below the injectivity scale, the law is exactly \(\pi^2\varepsilon^4/(42A^2)\), with zero sixth-order term. The symbolic check validates algebra; the uniform normal-coordinate and radial-cutoff arguments above provide the proof for general surfaces.

## Relationship to prior work
Finch and Jones, *Random Spherical Triangles* (first public September 27, 2010), and earlier Jones--Benyon-Tinker work give the full perimeter density of three points on the *round sphere*. Thus the sphere-specialized expansion above follows from prior formulas and is only an independent correctness check, not a priority claim. The finding here is the explicit sixth-order curvature integral for **every** smooth closed Riemannian surface and the resulting Euler-characteristic recovery. Philip's 2014 study treats round-sphere random triangle perimeter. Existing curvature probes using short pair distances or points on a shrinking prescribed geodesic circle measure different random observables; the general three-area-point perimeter coefficient is not implied by their displayed statements. These comparisons do not establish definitive historical priority.

## Limitations
The expansion has a surface-dependent remainder \(o(\varepsilon^6)\); no uniform estimate over varying metrics, finite-sample estimator, or boundary correction is proved. Reconstructing topology requires exact small-threshold population probabilities, and the Euler characteristic alone does not classify arbitrary nonorientable/connected surfaces without additional information. The sphere's full perimeter law predates this result. Unindexed classical integral-geometric literature and independent mathematical verification remain open priority and validation risks.

## References
- Steven R. Finch and Antonia J. Jones, *Random Spherical Triangles*, arXiv:1009.5329 (first publicly posted 2010-09-27), https://arxiv.org/abs/1009.5329 ; inspected full open HTML https://arxiv.org/html/1009.5329v3 .
- Johan Philip, *The Area and Perimeter of a Random Spherical Triangle* (2014), https://www.diva-portal.org/smash/get/diva2%3A724390/FULLTEXT01.pdf .
- Classical geodesic normal-coordinate Taylor expansions and the Gauss--Bonnet theorem (standard background, used in the proof).
