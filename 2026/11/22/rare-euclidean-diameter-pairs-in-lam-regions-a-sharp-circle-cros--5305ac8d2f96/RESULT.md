# Rare Euclidean diameter pairs in Lamé regions: a sharp circle crossover and angular support transition

## Finding

For \(p>0\), define the planar Lamé region \(K_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p\le1\}\), of area \(A_p=4\Gamma(1+1/p)^2/\Gamma(1+2/p)\). Let \(X_p,Y_p\) be independent and uniformly distributed by area in \(K_p\), and let \(D_p=\|X_p-Y_p\|_2\). For every **fixed** \(0<p<2\), the Euclidean diameter of \(K_p\) is \(2\), and

\[
\Pr(D_p>2-\varepsilon)\sim C_p\varepsilon^{2+2/p},\qquad
C_p=\frac{p^{2/p}\Gamma(1+2/p)}{(1+2/p)(2+2/p)\Gamma(1+1/p)^2}.
\]

For example, the astroid \(p=2/3\) has \(C_{2/3}=64/(405\pi)\) and exponent \(5\); the diamond \(p=1\) has \(C_1=1/6\) and exponent \(4\). The four ordered pairs of diametral axial tips each contribute exactly one quarter of the leading probability. Conditional on selecting a fixed tip pair, put \(X=(1-\varepsilon U,\varepsilon^{1/p}V)\), \(Y=(-1+\varepsilon W,\varepsilon^{1/p}Z)\) after an axial symmetry. The triple \((U,W,1-U-W)\) converges in distribution to \(\operatorname{Dirichlet}(1+1/p,1+1/p,1)\); given \((U,W)\), the limiting normalized transverse marks \(V/(pU)^{1/p}\) and \(Z/(pW)^{1/p}\) are independent uniform variables on \([-1,1]\), with the zero-deficit boundaries ignored as null events.

The circular limit has a **different** probability exponent. For each fixed \(\lambda\ge0\), set \(p_\varepsilon=2-\lambda\varepsilon\). Define the continuous \(\pi/2\)-periodic function

\[
H(\theta)=-\tfrac12\bigl(\cos^2\theta\log|\cos\theta|+\sin^2\theta\log|\sin\theta|\bigr),
\qquad 0\log0:=0.
\]

Then

\[
\Pr(D_{p_\varepsilon}>2-\varepsilon)
\sim\varepsilon^{5/2}F(\lambda),\quad
F(\lambda)=\frac{16}{15\pi^2}\int_0^{2\pi}
(1-2\lambda H(\theta))_+^{5/2}\,d\theta.
\]

The conditional polar angle of the first point converges to density \((16/(15\pi^2F(\lambda)))(1-2\lambda H(\theta))_+^{5/2}\). Conditional on this angle, the scaled inward excess radial deficits \((a,b)\ge0\) and angular gap coordinate \(z\in\mathbb R\) are *uniform in the three-dimensional region* \(a+b+z^2/4<1-2\lambda H(\theta)\). The angular density is positive for almost every direction when \(0\le\lambda\le2/\log2\); for \(\lambda>2/\log2\), its positive set consists of exactly four disjoint neighborhoods of coordinate axes. Moreover,

\[
F(0)=\frac{32}{15\pi},\qquad
F(\lambda)\sim\frac{4\sqrt2}{3\pi\sqrt{\lambda\log\lambda}}
\quad(\lambda\to\infty).
\]

## Assumptions and scope

All distances are **Euclidean**, and both points are independent with respect to **normalized planar Lebesgue area**. The region is convex only when \(p\ge1\), but all assertions also include the star-shaped, nonconvex range \(0<p<1\). The fixed-shape limit holds for each fixed \(p\in(0,2)\); the circle crossover is instead a different joint limit with a fixed \(\lambda\ge0\). The large-\(\lambda\) statement is a subsequent limit of the crossover function and is not an assertion of uniformity in both \(\lambda\) and \(\varepsilon\).

## Proof

**1. Diameter and isolated maximizers.** For \(0<p<2\) and \(x\in K_p\), \(\|x\|_2\le\|x\|_p\le1\), with equality in the first inequality only on the coordinate axes. Thus a pair is at Euclidean distance \(2\) exactly when it consists of opposite tips \((\pm1,0)\) or \((0,\pm1)\); there are four **ordered** such pairs. Compactness forces every pair of distance tending to \(2\) toward one of them. This applies to \(p<1\) as a direct inequality about coordinates, without invoking norm convexity.

**2. Fixed-\(p\) endpoint geometry.** Work near \(((1,0),(-1,0))\). Write

\[
X=(1-\varepsilon u,\varepsilon^{1/p}v),\qquad
Y=(-1+\varepsilon w,\varepsilon^{1/p}z).
\]

The two containment constraints converge on bounded sets to \(u,w\ge0\), \(|v|^p\le pu\), \(|z|^p\le pw\), because \((1-\varepsilon u)^p=1-p\varepsilon u+O(\varepsilon^2)\). Since \(2/p>1\),

\[
\|X-Y\|_2=\sqrt{(2-\varepsilon(u+w))^2+\varepsilon^{2/p}(v-z)^2}
=2-\varepsilon(u+w)+o(\varepsilon).
\]

For a rigorous localization, uniformly in small neighborhoods of the four tips, the strict coordinate-axis inequality gives \(1-\|x\|_2\ge c_p(1-|x_1|)\) when \(|x_1|\) is the large coordinate; indeed the constraint forces \(|x_2|^p\le1-|x_1|^p\), and \(|x_2|^2=o(1-|x_1|)\) as \(|x_1|\uparrow1\) for fixed \(p<2\). As \(2-\|X-Y\|_2\ge(1-\|X\|_2)+(1-\|Y\|_2)\), every near-diameter pair has \(u,w=O_p(1)\), and the containment constraint bounds its rescaled transverse coordinates. This supplies compact support for dominated convergence up to a slightly enlarged fixed box.

At one ordered tip pair, the probability divided by \(\varepsilon^{2+2/p}\) tends to

\[
\frac1{A_p^2}\int_{\substack{u,w\ge0\\u+w<1}}
\bigl(2(pu)^{1/p}\bigr)\bigl(2(pw)^{1/p}\bigr)\,du\,dw
=\frac{4p^{2/p}\Gamma(1+1/p)^2}{A_p^2\Gamma(3+2/p)}.
\]

Multiplying by four ordered tip pairs and using \(\Gamma(3+2/p)=(2+2/p)(1+2/p)\Gamma(1+2/p)\) yields \(C_p\). The same normalized limiting four-dimensional volume disintegrates into the claimed Dirichlet law for \((u,w,1-u-w)\) and the conditional independent uniform transverse marks.

**3. Nearly circular radial expansion.** For \(p=2-\lambda\varepsilon\), the polar boundary radius is \(r_p(\theta)=(|\cos\theta|^p+|\sin\theta|^p)^{-1/p}\), and Taylor expansion uniformly in \(\theta\) gives

\[
r_{2-\lambda\varepsilon}(\theta)=1-\lambda\varepsilon H(\theta)+O_\lambda(\varepsilon^2).
\]

Uniformity follows because \(a^q|\log a|^k\) is bounded for \(0\le a\le1\) and \(q\) in a compact positive interval. To obtain a distance exceeding \(2-\varepsilon\), both radial coordinates must equal \(1-O(\varepsilon)\), and the two polar angles differ by \(\pi+O(\sqrt\varepsilon)\). Put

\[
r_1=1-\varepsilon u,\quad r_2=1-\varepsilon w,\quad
\theta_2=\theta_1+\pi+\sqrt\varepsilon z.
\]

Then \(D=2-\varepsilon(u+w+z^2/4)+o_\lambda(\varepsilon)\), and the membership constraints become \(u,w\ge\lambda H(\theta)\). Define \(a=u-\lambda H(\theta)\), \(b=w-\lambda H(\theta)\); the limiting event is \(a,b\ge0\), \(a+b+z^2/4< c(\theta)\), with \(c(\theta)=(1-2\lambda H(\theta))_+\). Its three-dimensional volume equals

\[
\int_{-2\sqrt c}^{2\sqrt c}\frac12(c-z^2/4)^2\,dz=\frac{16}{15}c^{5/2}.
\]

The polar Jacobian is \(r_1r_2\varepsilon^{5/2}\,du\,dw\,d\theta\,dz\to\varepsilon^{5/2}\,du\,dw\,d\theta\,dz\), and \(A_p\to\pi\). The same compact near-diameter localization and dominated convergence prove the formula for \(F\) and the stated marked conditional limit.

**4. Angular transition and large parameter.** Writing \(q=\cos^2\theta\), one finds \(4H=-q\log q-(1-q)\log(1-q)\), the binary entropy, hence \(0\le H\le(\log2)/4\). In each quadrant it increases strictly from an axis to a diagonal, and then decreases strictly. The positive angular set therefore changes connectivity precisely at \(\lambda_*=2/\log2\). At \(\lambda=0\), direct integration gives \(F(0)=32/(15\pi)\). For \(\lambda\to\infty\), the four axial peaks dominate. At each axis \(H(\theta)=\frac12\theta^2\log(1/|\theta|)+O(\theta^2)\), so the rescaling \(\theta=\sqrt{2/(\lambda\log\lambda)}\,s\) makes \(2\lambda H\to s^2\). Dominated convergence on the four shrinking axial arcs, together with \(\int_{-1}^1(1-s^2)^{5/2}\,ds=5\pi/16\), yields the stated coefficient \(4\sqrt2/(3\pi)\).

## Verification

The standalone script `CHECK.py` recomputes the area, exact \(p=1\), \(p=2/3\), and circular constants, evaluates the critical integral, and independently uses deterministic Sobol quadrature on the exact finite-\(\varepsilon\) geometry. `CHECK_OUTPUT.txt` records six comparison ratios and a successful assertion exit. These finite checks illustrate convergence and do not replace the compactness argument, scaling convergence, or limiting angular analysis.

## Relationship to prior work

The classical disk pair-distance distribution is covered by Tu and Fischbach (2000), but a circle has an entire continuum of diametral directions, unlike \(K_p\) for fixed \(p<2\). Wong and Chu (1977) study average distances in \(\ell_p\) disks, not a stated sharp Euclidean **upper distance tail** or critical circle crossover. Alonso-Gutiérrez, Martín Goñi and Prochno (2025) establish \(n\to\infty\) central limits and large deviations in \(\ell_p^n\) balls; those conclusions do not determine a fixed two-dimensional rare-event tail. Closest indexed geometric-probability results concern invariantly sampled **lines** through \(\ell_p\) bodies, interior points of regular **polygons**, and interior points of **disk-clipped squares**. Their underlying measures and body families differ, and they do not imply the critical angular localization formula. This comparison is a best-knowledge historical assessment rather than a claim of independently established priority.

## Limitations

For fixed \(p<2\), the remainder is only \(o(\varepsilon^{2+2/p})\). The critical formula is pointwise for each fixed nonnegative \(\lambda\); no two-parameter uniform error estimate, sample-maxima theorem, or result for \(p>2\) is claimed. The source on mean distances by Wong and Chu was accessible at the abstract level but not as full text, and specialized historical priority remains a residual risk. The numerical checker is not an infinite proof. The range \(p<1\) is nonconvex, so convex-geometric corollaries must not be asserted there.

## References

1. S.-J. Tu and E. Fischbach, "A New Geometric Probability Technique for an N-dimensional Sphere and Its Applications to Physics," arXiv:math-ph/0004021, first made public 2000-04-17, https://arxiv.org/abs/math-ph/0004021 (full preprint, geometric probability for spherical regions).
2. C. K. Wong and K.-C. Chu, "Average Distances in \(\ell_p\) Disks," *SIAM Review* 19(2), 320–324 (1977), https://doi.org/10.1137/1019043 (abstract and bibliographic data inspected; complete text inaccessible).
3. D. Alonso-Gutiérrez, J. Martín Goñi and J. Prochno, "Limit theorems for the distance between two random points in \(\ell_p^n\)-balls," arXiv:2512.24367, https://arxiv.org/abs/2512.24367 (full preprint inspected, fixed \(p\) and dimension increasing).
4. M. Mayer and I. Molchanov, "A limit theorem for the maximal interpoint distance of a random sample in the unit ball," arXiv:math/0605289 (2006), https://arxiv.org/abs/math/0605289 (ball diameter sampling background).
5. J. Lellouche and M. Souris, "Distribution of Distances between Elements in a Compact Set," *Stats* 3(1) (2019), https://www.mdpi.com/2571-905X/3/1/1 (open-access literature overview of compact-set distance distributions).
