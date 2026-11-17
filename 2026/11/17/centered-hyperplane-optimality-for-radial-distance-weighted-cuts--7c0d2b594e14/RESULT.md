# Centered hyperplane optimality for radial distance-weighted cuts

## Finding
Let \(d\ge 2\), and let \(\mu,\nu\) be compactly supported, rotation-invariant Borel probability measures on \(\mathbb R^d\) assigning zero mass to every affine hyperplane. Let \(g:[0,\infty)\to[0,\infty)\) be continuous and nondecreasing, and set \(W(x,y)=g(\|x-y\|_2)\). For independent \(X\sim\mu\), \(Y\sim\nu\), define the distance-weighted cut
\[
C(u,t)=\mathbb E\big[W(X,Y)\,\mathbf1\{(u\cdot X-t)(u\cdot Y-t)<0\}\big],\qquad \|u\|_2=1.
\]
**Centered-cut principle.** For every \(u\) and real \(t\),
\[
C(u,t)\le C(u,0).
\]
More precisely, \(C(u,t)\) is even and nonincreasing in \(|t|\). If \(\mu=\nu\) is uniform surface probability on the unit sphere and \(g(r)=r\), then the decrease is strict on \(0<|t|<1\), and all maximizing affine hyperplanes pass through the origin.

For the sphere law and Euclidean weight, let \(R_d\) denote the optimal cut weight divided by \(\mathbb E\|X-Y\|_2\). It has the exact one-variable representation
\[
R_d=\frac{\int_0^\pi\theta\sin(\theta/2)\sin^{d-2}\theta\,d\theta}{\pi\int_0^\pi\sin(\theta/2)\sin^{d-2}\theta\,d\theta}
=\frac12+\frac{\mathbb E[q\sin(q/2)]}{\pi\mathbb E[\cos(q/2)]},
\]
where \(q\) has normalized density proportional to \(\cos^{d-2}q\) on \((-\pi/2,\pi/2)\). In particular,
\[
R_2=\frac2\pi,\qquad R_3=1-\frac4{3\pi},\qquad
R_d=\frac12+\frac1{2\pi d}+\frac1{2\pi d^2}+O(d^{-3}).
\]
For uniform points on the unit circle, the **entire affine-cut profile** is explicit: with \(C(t)=C(e_1,t)\) and \(L=\mathbb E\|X-Y\|_2\),
\[
\frac{C(t)}L=\begin{cases}\displaystyle\frac2\pi\sqrt{1-t^2},&|t|\le1,\\[2mm]0,&|t|\ge1.\end{cases}
\]
Thus the circle's optimal cut is uniquely a diameter, and moving its line by offset \(t\) gives an exact semicircular loss profile.

## Assumptions and scope
The radial measures need not coincide and may be supported on different spheres, shells, or concentric radial mixtures. The common center is the origin. Their compact support and hyperplane-null conditions ensure the cut expectation is finite, and remove boundary conventions. Weights are nonnegative, continuous, and nondecreasing functions of Euclidean separation; no convexity or differentiability of \(g\) is assumed. The universal theorem asserts optimality, not uniqueness for arbitrary measures or weights. The uniqueness, explicit profile, and asymptotics are asserted only for independent uniform spherical points with Euclidean weight. No claim is made for non-radial measures or nonmonotone weights.

## Proof
**1. Surface-crossing variation.** Fix a unit normal \(u=e_1\) by rotational invariance, and write \(A_t=\{x:x_1>t\}\). For smooth compactly supported radial densities \(\rho_\mu,\rho_\nu\), write
\[
C(t)=\iint W(x,y)[\mathbf1_{A_t}(x)\mathbf1_{A_t^c}(y)+\mathbf1_{A_t^c}(x)\mathbf1_{A_t}(y)]\,d\mu(x)d\nu(y).
\]
For a boundary point \(x=(t,x')\), put
\[
D_\nu(x,t)=\int_{y_1<t}W(x,y)\,d\nu(y)-\int_{y_1>t}W(x,y)\,d\nu(y).
\]
Differentiation through the moving hyperplane yields
\[
C'(t)=-\int_{x_1=t}D_\nu(x,t)\rho_\mu(x)\,dx'
-\int_{y_1=t}D_\mu(y,t)\rho_\nu(y)\,dy'.
\]
It remains to prove \(D_\nu(x,t)\ge0\) whenever \(t\ge0\).

**2. Antipodal pairing with a transverse reflection.** Let \(t\ge0\). Antipodal symmetry pairs every point \(y\in A_t\) with \(-y\in A_t^c\). The remaining part \(\{-t\le y_1<t\}\) of \(A_t^c\) contributes nonnegatively. For \(y=(s,z)\) with \(s>t\), the conditional distribution of \(z\) given \(s\) is invariant under \(z\mapsto-z\). After this change of variable, the average paired contribution compares
\[
g\left(\sqrt{(t+s)^2+\|x'-z\|_2^2}\right)
\quad\text{with}\quad
g\left(\sqrt{(t-s)^2+\|x'-z\|_2^2}\right).
\]
The first is no smaller because \((t+s)^2\ge(t-s)^2\) and \(g\) is nondecreasing. Hence \(D_\nu(x,t)\ge0\), and symmetrically \(D_\mu(y,t)\ge0\). Therefore \(C'(t)\le0\) for \(t\ge0\). Central symmetry gives \(C(-t)=C(t)\).

**3. Extension and strictness.** Approximate compactly supported rotation-invariant hyperplane-null Borel measures by smooth compactly supported radial densities, using radial approximate identities. The inequality passes to the limit since the weight is uniformly bounded on a common compact set, is continuous, and the delimiting hyperplanes have zero mass. Uniform surface laws on spheres satisfy the same derivative argument directly using coarea for spherical slices. When both laws are the uniform sphere and \(g(r)=r\), for every \(0<t<1\) the boundary slice and upper cap have positive surface measures. In the paired comparison, \((t+s)^2>(t-s)^2\), and strict monotonicity of \(g\) makes the boundary derivative strictly negative. Hence the center is the only optimal offset.

**4. Complete circle profile.** Parametrize \(S^1\) by polar angle. A cap cut by \(x_1>t\) is an angular arc of length \(2\alpha\), where \(\alpha=\arccos t\) for \(|t|<1\). The chord kernel on the circle is \(k(s)=2|\sin(s/2)|\), and its integral over one complete turn is \(8\). The unnormalized kernel integral over ordered pairs within the arc is
\[
I(\alpha)=4\int_0^{2\alpha}(2\alpha-s)\sin(s/2)\,ds=16(\alpha-\sin\alpha).
\]
The ordered-pair integral across the arc and its complement is \(2[(2\alpha)8-I(\alpha)]=32\sin\alpha\). The full ordered-pair integral is \(16\pi\). Dividing gives \(C(t)/L=2\sin\alpha/\pi=2\sqrt{1-t^2}/\pi\), with zero beyond the circle.

**5. Higher spherical dimensions.** For independent uniform \(X,Y\in S^{d-1}\), their mutual angle \(\theta\in[0,\pi]\) has density proportional to \(\sin^{d-2}\theta\) and chord length \(2\sin(\theta/2)\). For fixed \(X,Y\) at angle \(\theta\), a uniformly oriented central hyperplane separates them with probability \(\theta/\pi\), by projecting its random normal onto the span of the two directions. Rotational invariance makes every central normal optimal with equal value, giving the stated integral. For \(d=2\), its evaluation is \(2/\pi\). For \(d=3\), direct integration gives \(1-4/(3\pi)\).

For the high-dimensional expansion, set \(m=d-2\), \(q=\theta-\pi/2\), and normalize \(\cos^m q\) on \((-\pi/2,\pi/2)\). Laplace expansion of \(m\log\cos(z/\sqrt m)=-z^2/2-z^4/(12m)+O((z^6+z^8)/m^2)\), with exponentially small tails outside a shrinking central neighborhood, yields
\[
\mathbb E[q^2]=m^{-1}-m^{-2}+O(m^{-3})=d^{-1}+d^{-2}+O(d^{-3}),\quad
\mathbb E[q^4]=3d^{-2}+O(d^{-3}),\quad \mathbb E|q|^6=O(d^{-3}).
\]
Using \(\sin(q/2)=q/2-q^3/48+O(q^5)\) and \(\cos(q/2)=1-q^2/8+O(q^4)\),
\[
\frac{\mathbb E[q\sin(q/2)]}{\mathbb E[\cos(q/2)]}
=\frac12\mathbb E[q^2]+\frac1{16}(\mathbb E[q^2])^2-\frac1{48}\mathbb E[q^4]+O(d^{-3})
=\frac1{2d}+\frac1{2d^2}+O(d^{-3}),
\]
which proves the two correction terms.

## Verification
Run `python checker.py` with NumPy and SciPy. The verifier checks the exact dimension-two and dimension-three ratios by independent numerical quadrature, checks the sphere integral for additional dimensions, compares three higher-dimensional values against the displayed remainder bound, and reconstructs seven circle cut fractions directly from a discrete all-pairs chord matrix using an independent FFT convolution calculation. The analytical proof, not finite numerical checks, establishes the universal quantifiers, the monotonicity, and the asymptotic remainder.

## Relationship to prior work
Correa, Griesbach, Harb, Hommelsheim, Jlibene, Livanos, and Solan (2026) formulate distance-weighted hyperplane cuts and prove general dimension-dependent cut guarantees, including for Euclidean distance. Their inequality uses the standard random-central-hyperplane angular-separation identity, but their results do not determine the optimal affine hyperplane for the radial subfamily, the exact circle offset law, or the two-term spherical model asymptotic. The angular separation identity and elementary one-dimensional integration are recognized ingredients, not claimed as new. Plan and Vershynin (2014) develop random-hyperplane tessellation and angular separation machinery, but it is a distinct random embedding objective. Classical rearrangement and halfspace-depth theory may offer alternative formulations of the centering principle; no implication that settles the complete stated weighted radial cut theorem was established from the inspected material.

## Limitations
The centering theorem requires common rotational symmetry, compact support, and a continuous nonnegative nondecreasing distance weight. Arbitrary nonradial distributions, nonmonotone kernels, and hyperplane-charged distributions are not covered. The sphere formula does not determine the worst-case cut constant for arbitrary measures and supplies no improvement to the general lower bound. Research searches cannot certify historical priority: a comparable centering result could exist in rearrangement, integral geometry, or statistics literature. No independent mathematical audit has been performed.

## References
- J. Correa, S. M. Griesbach, E. Harb, F. Hommelsheim, R. Jlibene, V. Livanos, and E. Solan, *Separating Measures by Hyperplanes*, arXiv:2611.09166v1, first publicly available 2026-11-06. https://arxiv.org/html/2611.09166v1
- Y. Plan and R. Vershynin, *Dimension Reduction by Random Hyperplane Tessellations*, arXiv:1111.4452 (2011 preprint), *Discrete & Computational Geometry* 51 (2014). https://arxiv.org/abs/1111.4452
- G. Bonnet, A. Gusakova, C. Thäle, and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, *Advances in Mathematics* 386 (2021), 107813. https://doi.org/10.1016/j.aim.2021.107813
