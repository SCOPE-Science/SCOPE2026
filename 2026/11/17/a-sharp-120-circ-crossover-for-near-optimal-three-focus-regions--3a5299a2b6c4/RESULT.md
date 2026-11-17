# A sharp \(120^\circ\) crossover for near-optimal three-focus regions

## Finding
Fix \(b,c>0\). For each angle \(\theta\) near \(2\pi/3\), put
\[
 A_\theta=(0,0),\quad B_\theta=b(\cos(\theta/2),\sin(\theta/2)),\quad
 C_\theta=c(\cos(\theta/2),-\sin(\theta/2)).
\]
Let \(T_\theta\) be this triangle, let \(Z_\theta\) be a point sampled uniformly with respect to its Euclidean area, and define the three-focus distance cost and its minimum by
\[
 F_\theta(z)=|z-A_\theta|+|z-B_\theta|+|z-C_\theta|,
 \qquad M_\theta=\min_{z\in T_\theta}F_\theta(z).
\]
For an arbitrary fixed \(\lambda\in\mathbb R\), take \(\theta_t=2\pi/3+\lambda\sqrt t\), with \(t\downarrow0\). Set
\[
 k=\frac38\left(\frac1b+\frac1c\right),\qquad
 \beta=\frac{\sqrt3}{2},\qquad
 \Delta_0=\frac{\sqrt3bc}{4},\qquad
 m_\lambda=-\frac{\beta^2}{4k}\max\{-\lambda,0\}^2.
\]
Define the finite-area planar domain
\[
 \Omega_\lambda=\left\{(x,y):x>0,\quad
 kx^2+\beta\lambda x+\frac{y^2}{2x}<1+m_\lambda\right\},
 \qquad \mathcal V_\lambda=\operatorname{area}(\Omega_\lambda).
\]
Then the **critical-window area law** is
\[
 \boxed{\Pr\{F_{\theta_t}(Z_{\theta_t})-M_{\theta_t}<t\}
 =\frac{\mathcal V_\lambda}{\Delta_0}t^{5/4}+o(t^{5/4}).}
\]
Here \(\mathcal V_\lambda\) is explicit as the absolutely convergent integral
\[
 \boxed{\mathcal V_\lambda=
 2\sqrt2\int_{\substack{x>0\\ 1+m_\lambda-kx^2-\beta\lambda x>0}}
 \sqrt{x(1+m_\lambda-kx^2-\beta\lambda x)}\,dx.}
\]
Writing a point in bisector coordinates \(z=u(1,0)+v(0,1)\), the conditional law of
\(\big(u/\sqrt t,\,v/t^{3/4}\big)\), given the event displayed above, converges **in total variation** to normalized uniform area measure on \(\Omega_\lambda\).
For each \(s\in(0,1]\), the conditional relative excess has the limiting CDF
\[
 \boxed{\lim_{t\downarrow0}\Pr\left\{
 \frac{F_{\theta_t}(Z_{\theta_t})-M_{\theta_t}}{t}\le s
 \ \middle|\ F_{\theta_t}(Z_{\theta_t})-M_{\theta_t}<t\right\}
 =s^{5/4}\frac{\mathcal V_{\lambda/\sqrt s}}{\mathcal V_\lambda}.}
\]
In the exactly critical case \(\lambda=0\),
\[
 \mathcal V_0=\sqrt2\,k^{-3/4}B(3/4,3/2),\quad
 \frac{F_{2\pi/3}(Z)-M_{2\pi/3}}t\ \Big|\ F_{2\pi/3}(Z)-M_{2\pi/3}<t
 \ \Longrightarrow\ \operatorname{Beta}(5/4,1).
\]
For the limiting uniform point \((X,Y)\) on \(\Omega_0\), the two marks
\[
 U=kX^2,\qquad V=\frac{Y}{\sqrt{2X(1-kX^2)}}
\]
are independent, with \(U\sim\operatorname{Beta}(3/4,3/2)\) and \(V\sim\operatorname{Uniform}[-1,1]\). The crossover-volume extremes are
\[
 \mathcal V_\lambda\sim\frac{\pi\sqrt2}{4(\beta\lambda)^{3/2}}
 \quad(\lambda\to+\infty),\qquad
 \mathcal V_\lambda\sim\frac{\pi\sqrt{\beta(-\lambda)}}{k}
 \quad(\lambda\to-\infty).
\]
They match the singular approach to the linear-vertex and quadratic-interior Fermat regimes, respectively. These large-parameter statements are asymptotics of the proved crossover profile, not assertions of uniformity in unbounded \(\lambda\) as \(t\to0\).

## Assumptions and scope
The parent triangles are nondegenerate, \(b,c>0\) are fixed, \(\lambda\) is fixed and finite, and \(t>0\) is sufficiently small that \(0<\theta_t<\pi\). Each sampled point is **area-uniform**, not side-uniform. All distances and areas are Euclidean. The cost is unweighted and has exactly three foci at the triangle vertices. The interior angle at \(A_\theta\) is \(\theta\). The use of the symbol \(\operatorname{Beta}(p,q)\) denotes the usual probability law with density proportional to \(u^{p-1}(1-u)^{q-1}\) on \((0,1)\). Total variation concerns the law of the rescaled planar point conditioned on the stated rare event, not the law of the unscaled point.

## Proof
**1. Exact distance decomposition and the critical scaling.** Put \(h=\theta/2\). In local bisector coordinates \(z=(u,v)\) with \(u>0\) inside the triangle near \(A_\theta\), direct calculation yields
\[
 F_\theta(u,v)=\sqrt{u^2+v^2}+
 \sqrt{b^2+u^2+v^2-2b(u\cos h+v\sin h)}+
 \sqrt{c^2+u^2+v^2-2c(u\cos h-v\sin h)}.
\]
Let \(e_B=(\cos h,\sin h)\), \(e_C=(\cos h,-\sin h)\), and \(r=\sqrt{u^2+v^2}\). Taylor expansion of the two smooth nonvertex distances gives, uniformly in \(\theta\) near \(2\pi/3\),
\[
 F_\theta(u,v)-(b+c)=r-2u\cos h+
 \frac{r^2-(e_B\cdot z)^2}{2b}+
 \frac{r^2-(e_C\cdot z)^2}{2c}+O(r^3).
\]
For \(\theta=2\pi/3+\lambda\sqrt t\), note
\[
 1-2\cos h=\beta\lambda\sqrt t+O(t),\qquad
 \frac{\sin^2h}{2}\left(\frac1b+\frac1c\right)=k+O(\sqrt t).
\]
At \(u=\sqrt t\,x\), \(v=t^{3/4}y\), for fixed \(x>0\) and \(y\in\mathbb R\),
\[
 \frac{r-u}{t}=\frac{v^2}{t(r+u)}\longrightarrow\frac{y^2}{2x},
\]
while the smooth quadratic contribution divided by \(t\) tends to \(kx^2\); its cross-terms are of smaller order. Hence, pointwise and uniformly on compact sets with \(x\) bounded away from zero,
\[
 \frac{F_{\theta_t}(\sqrt t\,x,t^{3/4}y)-(b+c)}t
 \longrightarrow G_\lambda(x,y):=kx^2+\beta\lambda x+\frac{y^2}{2x}.
\]

**2. Uniform localization, including the cusp.** The classical Fermat minimizer is unique for every noncollinear triangle and equals \(A_{2\pi/3}\) at the critical angle; this also follows directly from strict convexity of the sum of three noncollinear Euclidean distances and the subgradient condition. Compactness then ensures that all points with \(F_{\theta_t}(z)-(b+c)\le Ct\) converge to \(A_{2\pi/3}\), for any fixed finite \(C\). To obtain the *quantitative* localization, use the exact identity
\[
 |be_B-z|-b+e_B\cdot z
 =\frac{r^2-(e_B\cdot z)^2}{|be_B-z|+b-e_B\cdot z},
\]
and its counterpart for \(c,e_C\). In a small fixed neighborhood of the origin, denominators stay positive and comparable to \(b,c\). Since \(e_B,e_C\) are nonparallel near the critical angle, the sum of these two nonnegative remainders is at least \(c_0r^2\) for some \(c_0>0\). Moreover the triangle wedge has \(|v|\le C_0u\), and therefore \(r-u=v^2/(r+u)\ge c_1v^2/u\) when \(u>0\). Since \(1-2\cos(\theta_t/2)\ge-C_2\sqrt t\), the exact distance decomposition gives
\[
 F_{\theta_t}(u,v)-(b+c)\ge c_3u^2+c_1\frac{v^2}{u}-C_2\sqrt t\,u
 \ge\frac{c_3}2u^2+c_1\frac{v^2}{u}-C_4t.
\]
Consequently, every bounded-scaled-excess sublevel is contained in \(0\le u\le C_5\sqrt t\), \(|v|\le C_6t^{3/4}\), with constants independent of small \(t\). This bound also controls minimizers, because \(F_{\theta_t}(A_{\theta_t})=b+c\).

**3. Moving minimum.** The preceding bounds make the rescaled minimizers precompact. The limit function \(G_\lambda\) has infimum
\[
 m_\lambda=\min_{x\ge0}\big(kx^2+\beta\lambda x\big)
 =-\frac{\beta^2\max\{-\lambda,0\}^2}{4k},
\]
obtained at \(y=0\). If \(\lambda<0\) the minimizing \(x\) is \(-\beta\lambda/(2k)>0\), so the compact convergence in Step 1 gives the matching upper and lower bounds. If \(\lambda\ge0\), the classical vertex optimality condition \(2\cos(\theta_t/2)\le1\) gives \(M_{\theta_t}=b+c\) exactly. Thus in every case
\[
 \frac{M_{\theta_t}-(b+c)}{t}\longrightarrow m_\lambda.
\]
At the boundary \(x=0\), the only possible finite-cost scaled limit has \(y=0\), so no minimizer or positive-volume contribution is lost there.

**4. Area and total variation.** The coordinate map \((x,y)\mapsto(u,v)=(\sqrt t\,x,t^{3/4}y)\) has Jacobian \(t^{5/4}\). Step 2 confines all relevant sublevel sets to a common compact rectangle in the scaled plane. Step 1 and Step 3 show almost-everywhere convergence of their indicators to \(\mathbf1_{\Omega_\lambda}\). The boundary of \(\Omega_\lambda\) has planar Lebesgue measure zero, since every positive-\(x\) section has at most two endpoints in \(y\). Dominated convergence gives both area convergence and convergence in \(L^1\) of the conditional densities. The triangle area tends to \(\Delta_0\), proving the probability and total-variation conclusions. Integrating the \(y\)-section of \(\Omega_\lambda\) gives exactly the asserted integral for \(\mathcal V_\lambda\).

**5. Relative-excess distribution and critical marks.** The anisotropic substitution \(x=\sqrt s\,\xi\), \(y=s^{3/4}\eta\) gives
\[
 G_\lambda(x,y)-m_\lambda
 =s\left[G_{\lambda/\sqrt s}(\xi,\eta)-m_{\lambda/\sqrt s}\right],
\]
because \(m_\lambda=s\,m_{\lambda/\sqrt s}\). Its Jacobian is \(s^{5/4}\). Taking the ratio of areas at excess \(s\) and \(1\) proves the conditional CDF. At \(\lambda=0\), setting \(z=kx^2\) in the cross-section integral gives a density proportional to \(z^{-1/4}(1-z)^{1/2}\), i.e. \(\operatorname{Beta}(3/4,3/2)\). Conditional on \(x\), the rescaled transverse mark \(y/\sqrt{2x(1-kx^2)}\) is uniform on \([-1,1]\), independently of \(z\). The critical Beta excess follows from the CDF formula.

**6. Opposite crossover ends.** For \(\lambda\to+\infty\), put \(x=z/(\beta\lambda)\) in the integral. Dominated convergence gives
\(\mathcal V_\lambda\sim 2\sqrt2(\beta\lambda)^{-3/2}\int_0^1\sqrt{z(1-z)}\,dz=\pi\sqrt2/[4(\beta\lambda)^{3/2}]\).
For \(\lambda\to-\infty\), complete the square and put \(x=x_0+z\), where \(x_0=-\beta\lambda/(2k)\). The integration range becomes \(|z|<k^{-1/2}\) for sufficiently negative \(\lambda\), and dominated convergence gives
\[\mathcal V_\lambda\sim2\sqrt2\sqrt{x_0}\int_{-1/\sqrt k}^{1/\sqrt k}\sqrt{1-kz^2}\,dz
 =\frac{\pi\sqrt{\beta(-\lambda)}}k.
\]
This completes the proof.

## Verification
The standalone Python checker evaluates \(\mathcal V_\lambda\) by one-dimensional quadrature and compares the result with independent direct cross-sectional integration of the *exact three-distance cost* in the physical triangle. It tests five fixed crossover parameters and two decreasing excess thresholds. The analytic critical normalization is checked independently using the Beta function. Results include, for \(b=c=1\): \(k=0.75\), \(\mathcal V_0=1.6819639752622\), \(\mathcal V_0/\Delta_0=3.8843294155395\). At critical \(\lambda=0\), the direct-to-predicted probability ratios are approximately \(0.995526\) for \(t=0.004\) and \(0.999331\) for \(t=0.001\). For \(\lambda=2\), the corresponding ratios are approximately \(1.094876\) and \(1.049516\), consistent with a larger finite-threshold correction. The checker is diagnostic; the asymptotic and total-variation claims follow from the argument above, not from finite quadrature.

## Relationship to prior work
The Fermat–Torricelli problem, including the sharp \(120^\circ\) criterion for an interior versus vertex minimizer, is classical. Sekino (1999) gives the nondegenerate Hessian at a smooth three-focus critical point and general convexity/structure of multifocal level sets; those facts alone do not establish the singular near-critical area law. Shen and Tolosa (2008) solve the weighted Fermat problem and discuss minimizer location, but do not give the critical small-excess area crossover or its marked limiting distribution. Petrović, Banjac, and Malešević (first arXiv version 2013) calculate general trifocal level-set areas numerically for application, but do not evaluate an asymptotic critical window. A separately published equilateral three-focus radial-envelope theorem determines angular extrema of the sum at fixed distance from the centroid; its equilateral fixed-geometry statement neither contains the moving \(120^\circ\) family nor implies the \(5/4\) crossover volume or total-variation law. The present claim is the joint critical-window law, its complete limiting region, and its explicit crossover profile—not the classical Fermat minimizer or the generic smooth Hessian approximation.

## Limitations
The theorem is for exactly three equal-weight foci, and the two adjacent lengths are held fixed while the included angle varies at scale \(\sqrt t\). Only fixed finite \(\lambda\) is covered in the small-\(t\) assertion; the large-\(|\lambda|\) limits concern the independent crossover-volume function. The sampling density must be uniform with respect to Euclidean area on the parent triangle. Historical priority is provisional: some generalized-conic literature (notably Groß and Strempel, 1998) was accessible only through metadata/abstract, and an unlocated equivalent asymptotic under polyellipse or multifocal-level terminology cannot be excluded. Independent mathematical validation has not been performed.

## References
1. J. Sekino, “n-Ellipses and the Minimum Distance Sum Problem,” *American Mathematical Monthly* **106** (1999), 193–202. DOI: 10.1080/00029890.1999.12005030. Accessible full text: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/nellipse.pdf.
2. Y. Shen and J. Tolosa, “The Weighted Fermat Triangle Problem,” *International Journal of Mathematics and Mathematical Sciences* (2008), Article 283846; first published March 17, 2008. DOI: 10.1155/2008/283846. https://onlinelibrary.wiley.com/doi/10.1155/2008/283846.
3. M. Petrović, B. Banjac, and B. Malešević, “The Geometry of Trifocal Curves with Applications in Architecture, Urban and Spatial Planning,” arXiv:1312.1640 (first submitted December 5, 2013); *Spatium* **32** (2014), 28–33. https://arxiv.org/abs/1312.1640.
4. C. Groß and T.-K. Strempel, “On Generalizations of Conics and on a Generalization of the Fermat-Torricelli Problem,” *American Mathematical Monthly* **105** (1998), 732–743. DOI: 10.1080/00029890.1998.12004955. Abstract inspected; full material not obtained.
5. “Exact radial envelope for the equilateral three-focus distance sum,” published-finding corpus, published October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-radial-envelope-for-the-equilateral-three-focus-distance-s--094825f3a288.
