# Radial symmetry defect and marked near-collinearity for anchored random triangles

## Finding
Let \(K\subset\mathbb R^2\) be any compact convex body of positive area \(A\), and fix \(z\in\operatorname{int}K\). Choose \(X,Y\) independently and uniformly by area from \(K\). Put \(D=|\det(X-z,Y-z)|/A\). Write \(\rho(\theta)\) for the radial distance from \(z\) to \(\partial K\) in direction \((\cos\theta,\sin\theta)\). Then
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(D<\varepsilon)}{\varepsilon}
=8-\frac1A\int_0^{2\pi}[\rho(\theta)-\rho(\theta+\pi)]^2\,d\theta.
\]
The coefficient lies strictly above \(4\), and at most \(8\); equality at \(8\) holds **if and only if** \(K\) is centrally symmetric about \(z\). The strict lower bound \(4\) is sharp as \(z\) approaches a boundary point of any fixed \(K\). Both \(D\) and the coefficient are invariant under nonsingular affine maps applied to the body and anchor.

A stronger conditional law identifies *which* configurations produce this rare near-collinearity. Given \(D<\varepsilon\), write the polar radii and angles of \(X-z,Y-z\) as \((R,\Theta),(S,\Phi)\). Choose the unique \(B\in\{0,1\}\) giving the nearer angular line \(\Theta+B\pi\) modulo \(2\pi\), let \(\Sigma\in\{-1,1\}\) be the sign of that signed small angular displacement, and set \(Q=D/\varepsilon\). As \(\varepsilon\downarrow0\), the law of \((\Theta,B,R,S,Q,\Sigma)\) converges in **total variation** to the probability density
\[
\frac{\mathbf1_{\{0<r<\rho(\theta),\ 0<s<\rho(\theta+b\pi),\ 0<q<1\}}}{2H}
\quad\text{with respect to }d\theta\,dr\,ds\,dq\text{ and counting measure in }(b,\sigma),
\]
where \(H=\int_0^{2\pi}\rho(\theta)[\rho(\theta)+\rho(\theta+\pi)]\,d\theta\). Thus the normalized determinant \(Q\) is asymptotically uniform on \((0,1)\), the side mark \(\Sigma\) is an independent fair sign, and conditional on the direction and parallel/antiparallel branch, the two radii are independent uniforms on the corresponding radial intervals. In particular, the limiting probability of the parallel branch is \(2A/H\), and that of the antiparallel branch is \(\int\rho(\theta)\rho(\theta+\pi)\,d\theta/H\).

## Assumptions and scope
The body is planar, convex, compact, with \(0<A<\infty\); no boundary smoothness or strict convexity is required. The anchor is strictly interior, and the points are independent area-uniform samples. The orientation \(\theta\) is defined relative to any fixed orthonormal frame. The angular difference \(\Phi-\Theta\) has a unique closest multiple of \(\pi\) except on a null set; that closest multiple determines \(B\), and its signed residual determines \(\Sigma\). Angular coordinates are taken modulo \(2\pi\). All limits are at fixed \(K,z\), and the preceding integral and conditional density are exact, with no unstated genericity assumptions. The value of \(\operatorname{sign}\) on the null event of zero displacement is arbitrary.

## Proof
1. Convexity and the interior anchor imply that the radial function \(\rho\) is continuous, strictly positive and bounded. Polar Lebesgue measure gives \(A=\frac12\int_0^{2\pi}\rho(\theta)^2d\theta\). Write \(\rho_\pi(\theta)=\rho(\theta+\pi)\), \(I=\int\rho\rho_\pi\), and \(H=2A+I\).

2. Fix a nonzero first vector \(x=r(\cos\theta,\sin\theta)\). The allowable second point for \(|\det(x,Y-z)|<t\) is the intersection of \(K-z\) with the strip of normal width \(2t/r\) around the through-origin line at angle \(\theta\). By Fubini along lines parallel to this line, the strip area divided by \(t\) converges to \(2[\rho(\theta)+\rho_\pi(\theta)]/r\). This follows from continuity of the chord length through the interior point. That strip area is at most \(2t\operatorname{diam}(K)/r\), since every chord length is bounded by the diameter. When integrating with the first point's density \(r\,dr\,d\theta/A\), the bound is integrable, including near \(r=0\). Dominated convergence therefore gives
\[
\lim_{t\downarrow0}\frac{\Pr(|\det(X-z,Y-z)|<t)}{t}
=\frac{2}{A^2}\int_0^{2\pi}\rho(\theta)[\rho(\theta)+\rho_\pi(\theta)]\,d\theta
=\frac{2H}{A^2}.
\]
Choosing \(t=A\varepsilon\) proves the normalized coefficient \(2H/A=4+2I/A\). Since
\(\int(\rho-\rho_\pi)^2=4A-2I\), the advertised defect formula follows.

3. Since \(\rho,\rho_\pi>0\), \(I>0\). The inequality \(2\rho\rho_\pi\le\rho^2+\rho_\pi^2\) yields \(I\le2A\), with equality iff \(\rho(\theta)=\rho(\theta+\pi)\) almost everywhere. Continuity upgrades this to every direction, equivalent to \(K-z=-(K-z)\). If anchors \(z_j\) approach a boundary point of fixed \(K\), their radial functions converge in almost every direction to boundary-based radial lengths. Except possibly the two directions tangent to a supporting line, at least one of the antipodal boundary-based radial lengths vanishes. The radial lengths remain bounded by \(\operatorname{diam}(K)\), so dominated convergence implies \(I(z_j)\to0\), proving sharpness of \(4\). An invertible linear map multiplies both the determinant and area by the same absolute determinant, and translations preserve centered differences, proving affine invariance.

4. For the marked law, the exact joint polar density before conditioning is \(rs/A^2\) on \(0<r<\rho(\theta),0<s<\rho(\phi)\). For \(b\in\{0,1\}\), \(\sigma\in\{-1,1\}\), and \(0<q<1\), the angular substitution on each nearest-branch sector is
\[
\phi=\theta+b\pi+\sigma\arcsin\left(\frac{A\varepsilon q}{rs}\right)\pmod{2\pi},
\quad 0<\frac{A\varepsilon q}{rs}<1.
\]
The Jacobian in \(q\) is \(A\varepsilon/[rs\sqrt{1-(A\varepsilon q/(rs))^2}]\). The induced unnormalized density for each mark is therefore
\[
\frac{\varepsilon}{A\sqrt{1-(A\varepsilon q/(rs))^2}}
\mathbf1_{\{0<r<\rho(\theta),\,0<s<\rho(\phi),\,0<q<1,\,A\varepsilon q<rs\}}.
\]
For fixed \((\theta,b,\sigma,r,s,q)\) in the limiting interior, this density divided by \(\varepsilon\) tends to \(1/A\) times the two radial-interval indicators. Since \(\Pr(D<\varepsilon)/\varepsilon\to2H/A\) by step 2, the conditional joint density converges pointwise almost everywhere to \(1/(2H)\) on the stated support. The candidate limiting density integrates to one: summing the two signs gives \(2H/(2H)=1\). Scheffé's lemma applies to these probability densities on a common fixed measure space, proving **total-variation**, not merely weak, convergence. Integrating its product indicators proves the uniform, fair-sign and conditional radial statements.

## Verification
The standalone `verify.py` uses direct area-uniform polar rejection sampling for disks and the strictly convex radial oval \(\rho(\theta)=1+0.4\cos\theta\), using 1.7 million independent point pairs (3.4 million sampled points) for each body. The oval has area \(\pi(1+a^2/2)\), exact normalized slope \(8-4a^2/(1+a^2/2)\), and conditional parallel-branch probability \(1/2+a^2/4\). Numerical small-determinant slopes at successively smaller thresholds, conditional marks, and an independently integrated exact disk determinant density all passed. Execute `python verify.py` with NumPy and SciPy. No finite simulation is used in place of a proof.

## Relationship to prior work
Random determinant dispersion and moments are established subjects. Rademacher and Vempala (2006, publicly posted August 25) treat determinant dispersion for algorithms and high-dimensional geometric probabilities; Breiding, Bürgisser, Lerario and Mathis (2021) treat expected determinants via zonoids. Those inspected statements do not supply a sharp **planar near-zero anchored determinant slope** with an exact radial antipodal symmetry defect or its marked total-variation law. The work of Henze on random triangles in convex regions and Pivovarov on determinants of random convex-body samples is relevant but their complete articles were not accessible, so priority is provisional rather than certified. Earlier random-simplex volume results involving three random vertices do not automatically imply a two-random-vertex, one-fixed-anchor law.

## Limitations
The assertion concerns one interior anchor and two independent **area** samples; it is not a law for three random vertices, boundary sampling, a boundary anchor, or arbitrary spatial dimensions. The asymptotic is first order and no quantitative remainder or convergence rate is proved. Full historical priority verification, particularly against inaccessible older random-triangle literature, and independent mathematical validation have not been performed.

## References
- L. Rademacher and S. Vempala, *Dispersion of Mass and the Complexity of Randomized Geometric Algorithms*, ECCC TR06-102 (first public release August 25, 2006). https://eccc.weizmann.ac.il/report/2006/102/
- P. Breiding, P. Bürgisser, A. Lerario and L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996 (first posted September 30, 2021). https://arxiv.org/abs/2109.14996
- M. D. Perlman and J. A. Wellner, *Squaring the Circle and Cubing the Sphere: Circular and Spherical Copulas*, Symmetry 3 (2011). https://www.mdpi.com/2073-8994/3/3/574
- O. Reichenwallner, *Moments of volumes of lower-dimensional random simplices are not monotone*, 2017. https://link.springer.com/article/10.1007/s00605-017-1077-3
- N. Henze, *Random triangles in convex regions*, Journal of Applied Probability (abstract available). https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/random-triangles-in-convex-regions/45B3779718B7D8E2585F9E77EDFFE244
- P. Pivovarov, *On determinants and the volume of random polytopes in isotropic convex bodies* (2010, abstract available). https://doi.org/10.1007/s10711-010-9462-2
