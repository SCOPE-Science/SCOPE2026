# Sharp small-area law for three sphere-uniform Euclidean chord vertices

## Finding
Let \(X,Y,Z\) be independent points uniformly distributed with respect to normalized surface area on the unit sphere \(S^2\subset\mathbb R^3\). Set the ordinary **Euclidean planar** triangle area
\[
T=\frac12\|(Y-X)\times(Z-X)\|.
\]
Then the sharp lower-tail law is
\[
\boxed{\Pr(T\le t)=C_*t^{5/3}+o(t^{5/3}),\qquad t\downarrow0,}
\]
where
\[
\boxed{C_*=\frac{\mathrm B(1/3,3/2)\,\mathrm B(1/3,1/3)}{2^{2/3}\pi}=2.682312638526963\ldots.}
\]
Here \(\mathrm B(a,b)=\int_0^1s^{a-1}(1-s)^{b-1}\,ds\). This is the Euclidean chord-triangle area, not the area of a spherical geodesic triangle; the latter is a different observable.

## Assumptions and scope
The three vertices are independent and uniformly distributed over the full unit two-sphere. The event of degeneracy has probability zero. The assertion is only a leading asymptotic at the zero-area endpoint. Scaling the sphere's radius by \(R>0\) multiplies the planar area by \(R^2\), and therefore divides the leading coefficient by \(R^{10/3}\) at fixed dimensional area threshold.

## Proof
**Exact disintegration.** Condition on \(X,Y\) and put \(\ell=\|Y-X\|\). For two independent points of \(S^2\), \(\ell\) has density \(\ell/2\) on \((0,2)\). Choose the first coordinate in the two-dimensional plane perpendicular to \(Y-X\) along the projection of \(X\). Its projected coordinate is \((h,0)\), where \(h=\sqrt{1-\ell^2/4}\). The orthogonal projection \((U,V)\) of an independent uniform sphere point to this plane has density
\[
f(u,v)=\frac{\mathbf1_{u^2+v^2<1}}{2\pi\sqrt{1-u^2-v^2}}.
\]
The perpendicular distance from \(Z\) to the affine chord line through \(X,Y\) is \(\sqrt{(U-h)^2+V^2}\). Consequently, **for every** \(t>0\),
\[
\Pr(T\le t)=\int_0^2\frac{\ell}{2}\int_{\substack{u^2+v^2<1\\(u-h)^2+v^2\le(2t/\ell)^2}}\frac{du\,dv}{2\pi\sqrt{1-u^2-v^2}}\,d\ell.\tag{1}
\]
This exact representation fixes the normalization independently of any asymptotic argument.

**Concentration at a cubic collision scale.** Write \(\delta=2t/\ell\) and let \(J(\ell,t)\) denote the inner conditional probability in (1). The projected measure of the intersection of the unit disk with any disk of radius \(\delta\) is at most \(K\min(1,\delta^{3/2})\) for an absolute constant \(K\). One way to verify this elementary uniform boundary-layer bound is to use \(f(u,v)\lesssim\operatorname{dist}((u,v),\partial\mathbb D)^{-1/2}\) and the fact that a circular boundary layer of thickness \(s\le\delta\) occupies at most \(K\delta s\) within a disk of radius \(\delta\), then integrate the density by layers. It follows that for every \(\eta>0\),
\[
\int_0^{\eta t^{1/3}}\frac{\ell}{2}J(\ell,t)\,d\ell\le Kt^{5/3}\eta^{1/2}.\tag{2}
\]
Conversely, if \(\ell\ge Rt^{1/3}\), for fixed sufficiently large \(R\), then \(\delta\le\ell^2/16\). Throughout the relevant projected disk one has \(1-u^2-v^2\ge c\ell^2\). Therefore \(J(\ell,t)\le K\delta^2/\ell\), and
\[
\int_{Rt^{1/3}}^2\frac{\ell}{2}J(\ell,t)\,d\ell\le Kt^{5/3}/R.\tag{3}
\]
Thus the leading contribution comes from \(\ell\asymp t^{1/3}\), neither generic chord lengths nor an arbitrarily tighter double collision.

**Boundary blow-up and coefficient.** In (1) introduce
\[
\ell=t^{1/3}a,\qquad u=h+t^{2/3}U,\qquad v=t^{2/3}V.
\]
For fixed \(a>0\), the rescaled integration domain approaches
\[
U^2+V^2<4/a^2,\qquad U<a^2/8,
\]
and \(1-u^2-v^2=t^{2/3}(a^2/4-2U+o(1))\). The square-root singularity is locally integrable. For \(a\) in any compact subset of \((0,\infty)\), the rescaled cutoff domain is bounded, the slope of the exact disk boundary in the \(U\) coordinate stays uniformly away from zero, and the integral within a strip of \(U\)-width \(s\) along that boundary is \(O(\sqrt s)\), uniformly for small \(t\). Away from the strip, dominated convergence applies. This proves convergence of the integrals on compact \(a\)-ranges. The cutoff estimates (2)–(3) then yield
\[
C_*=\frac1{4\pi}\int_0^\infty a\,da\iint_{\substack{U^2+V^2<4/a^2\\U<a^2/8}}\frac{dU\,dV}{\sqrt{a^2/4-2U}}.\tag{4}
\]
To evaluate it without any numerical inference, set \(U=(au-u^2)/2\). Each monotone branch \(u<a/2\) or \(u>a/2\) has absolute Jacobian \(|dU|/\sqrt{a^2/4-2U}=|du|\). The integrand is symmetric under \(u\mapsto a-u\); averaging the two inverse branches thus transforms the whole \(U\)-integral into one half of the \(u\)-integral. Formula (4) becomes
\[
C_*=\frac1{8\pi}\int_0^\infty a\,da\int_{\mathbb R}\!du\int_{\mathbb R}\!dv\;\mathbf1\left\{a^2\left[v^2+\frac{u^2(u-a)^2}{4}\right]<4\right\}.\tag{5}
\]
Integrate in \(v\), then substitute \(u=aw\). One obtains
\[
C_*=\frac1{2\pi}\int_{\mathbb R}\!dw\int_0^{(4/|w(w-1)|)^{1/3}}\!a\sqrt{1-a^6w^2(w-1)^2/16}\,da.
\]
The inner integral is \(4^{2/3}|w(w-1)|^{-2/3}\mathrm B(1/3,3/2)/6\). Splitting the real line into \(( -\infty,0),(0,1),(1,\infty)\) gives
\[
\int_{\mathbb R}|w(w-1)|^{-2/3}\,dw=3\mathrm B(1/3,1/3).
\]
Substitution produces the stated positive finite constant. Since the limits of (2) and (3) can independently be sent to zero after the compact-range limit, this proves the full asserted asymptotic.

## Verification
A standalone reproducibility program `verify.py` evaluates the beta-function constant, the exact two-stage conditional integral (1) through an independent one-dimensional arcsine slice formula, and a direct geometric sample of Euclidean chord-triangle areas. The limiting relation rests on the analytical cutoff and change-of-variables proof, not on finite numerical sampling.

## Relationship to prior work
Finch and Jones, *Random Spherical Triangles*, concern spherical geodesic triangles and **spherical excess**, not the planar Euclidean area here. Akopyan, Edelsbrunner and Nikitenko derive the spherical Blaschke–Petkantschin shape/size factorization and metric means for random inscribed polytopes; their examined relevant sections do not state the sharp lower-tail power \(5/3\) or this beta-product coefficient. Earlier isotropic-random-simplex moment theory is a potentially broader antecedent whose complete scope could not be resolved from accessible primary text. The new assertion is solely the explicit, sharp endpoint law under the specified sampling model, not any general shape/size decomposition or known moment formula.

## Limitations
The result concerns a fixed dimension, a full unit sphere, and three independent surface-uniform points. No uniformity in dimension, nonuniform sampling generalization, or second asymptotic coefficient is asserted. Numerical convergence is slow because the next contributions arise outside the cubic collision regime. Historical priority remains provisional, notably relative to older inaccessible complete texts on isotropic random simplices and spherical-triangle shape densities; their abstracts alone cannot settle the implication comparison.

## References
- S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, initially posted 2010-09-27. https://arxiv.org/abs/1009.5329
- A. Akopyan, H. Edelsbrunner and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783, 2020. https://arxiv.org/abs/2007.07783
- R. E. Miles, *Isotropic Random Simplices*, Advances in Applied Probability 3 (1971), 353–382. https://doi.org/10.2307/1426176
- H. Le, *Random Spherical Triangles II: Shape Densities*, Advances in Applied Probability 21 (1989), 581–594. https://doi.org/10.2307/1427637
