# Sharp near-diameter geodesic tails and curvature recovery for constant-curvature disks

## Finding

Fix \(R>0\) and \(\kappa\ge0\). In the simply connected surface of constant Gaussian curvature \(-\kappa^2\), let \(B_{\kappa,R}\) denote a closed geodesic disk of intrinsic radius \(R\). Take independent area-uniform points \(X,Y\) of this disk and write \(D=d(X,Y)\) for their intrinsic minimizing geodesic distance. The disk is geodesically convex, so this is also the ambient distance. Its essential supremum equals \(2R\).

**Theorem.** As \(\varepsilon\downarrow0\),
\[
\Pr(D>2R-\varepsilon)=C_{\kappa,R}\varepsilon^{5/2}+O_{\kappa,R}(\varepsilon^{7/2}),
\]
where
\[
C_{\kappa,R}=\begin{cases}
\dfrac{8\kappa^{5/2}}{15\pi}\dfrac{\coth^2(\kappa R/2)}{\sqrt{\tanh(\kappa R)}},&\kappa>0,\\[5pt]
\dfrac{32}{15\pi R^{5/2}},&\kappa=0.
\end{cases}
\]
The dimensionless coefficient ratio is
\[
\frac{C_{\kappa,R}}{C_{0,R}}=
\left[\frac{z}{2}\coth\left(\frac z2\right)\right]^2
\sqrt{\frac z{\tanh z}},\qquad z=\kappa R,
\]
and strictly increases from one to infinity as \(z\) goes from zero to infinity. Therefore the entire pair-distance distribution, indeed just its diameter and its leading near-diameter probability constant, uniquely determines both disk radius and curvature parameter within this family. Close to zero curvature the ratio equals \(1+z^2/3+O(z^4)\).

There is a **joint marked rare-event limit**. In geodesic polar coordinates write radial positions \(r_1,r_2\), angular positions \(\theta_1,\theta_2\), and let \(w=\pi-\delta\), where \(\delta\in[0,\pi]\) is the smaller angular separation. Put
\[
a_{\kappa,R}=\begin{cases}\tanh(\kappa R)/(4\kappa),&\kappa>0,\\R/4,&\kappa=0.\end{cases}\]
Set
\[
U_\varepsilon=\frac{R-r_1}{\varepsilon},\quad
V_\varepsilon=\frac{R-r_2}{\varepsilon},\quad
W_\varepsilon=\frac{a_{\kappa,R}w^2}{\varepsilon},\quad
T_\varepsilon=1-U_\varepsilon-V_\varepsilon-W_\varepsilon.
\]
Conditioned on \(D>2R-\varepsilon\), these four coordinates converge in distribution to \(\operatorname{Dirichlet}(1,1,1/2,1)\). In particular the limiting means of the first three coordinates are \(2/7,2/7,1/7\). The first azimuth is exactly uniform, while the orientation sign of the near-antipodal angular displacement is a fair independent sign, jointly independent of the limiting Dirichlet vector.

## Assumptions and scope

The curvature parameter \(\kappa\) and radius \(R\) are fixed before taking \(\varepsilon\downarrow0\); the error estimate is not claimed uniform as \(R\to\infty\) or as both parameters vary. Area-uniform means normalized intrinsic Riemannian area, not uniform Euclidean coordinates of the Poincaré model. Boundary points have zero mass. The distance is intrinsic geodesic distance, not Euclidean chord separation or a random-graph distance. The theorem includes the flat disk as a continuous limiting case.

## Proof

**1. Polar measure.** By rotational symmetry, the two angular coordinates are independent uniform elements of \([0,2\pi)\). The radial coordinates are independent with probability density
\[
f_{\kappa,R}(r)=\begin{cases}
\kappa\sinh(\kappa r)/(\cosh(\kappa R)-1),&\kappa>0,\\
2r/R^2,&\kappa=0,
\end{cases}\qquad 0\le r\le R.
\]
The boundary density equals \(b_{\kappa,R}=\kappa\coth(\kappa R/2)\) for positive curvature scale and \(b_{0,R}=2/R\). The angular defect \(w\) from antipodality is uniform on \([0,\pi]\), independent of the radii. The first azimuth and the sign of the oriented angular difference are uniform independent marks.

**2. Exact threshold region.** Put \(u=R-r_1\), \(v=R-r_2\), and \(h=\varepsilon-u-v\). The triangle inequality gives \(D\le r_1+r_2=2R-u-v\); therefore \(D>2R-\varepsilon\) forces \(u,v\ge0\) and \(h>0\). For \(\kappa>0\), the hyperbolic cosine rule at angular separation \(\pi-w\) gives
\[
\cosh(\kappa D)=\cosh\bigl(\kappa(r_1+r_2)\bigr)
-\sinh(\kappa r_1)\sinh(\kappa r_2)(1-\cos w).
\]
Thus on the triangle \(u,v\ge0\), \(u+v<\varepsilon\), the condition is \(1-\cos w<q\), where
\[
q=\frac{\cosh(\kappa(2R-u-v))-\cosh(\kappa(2R-\varepsilon))}
{\sinh(\kappa(R-u))\sinh(\kappa(R-v))}.
\]
The \(\kappa=0\) cosine-rule counterpart is
\[
q=\frac{(2R-u-v)^2-(2R-\varepsilon)^2}{2(R-u)(R-v)}.
\]
For sufficiently small \(\varepsilon\) both expressions satisfy \(0\le q<2\); the conditional angular probability is therefore exactly \(\arccos(1-q)/\pi\).

**3. Uniform boundary expansion.** The numerator is proportional to \(h\). The mean-value theorem applied to the numerator and smoothness of the denominator, uniformly for \(0\le u+v\le\varepsilon\), yield
\[
q=\frac{h}{2a_{\kappa,R}}[1+O_{\kappa,R}(\varepsilon)],
\qquad
\frac{\arccos(1-q)}\pi
=\frac1{\pi\sqrt{a_{\kappa,R}}}\sqrt h\,[1+O_{\kappa,R}(\varepsilon)].
\]
The error is uniform even as \(h\downarrow0\); at \(h=0\) both sides vanish. In particular the rare event implies \(u,v=O(\varepsilon)\) and \(w=O(\sqrt\varepsilon)\). Also \(f_{\kappa,R}(R-u)f_{\kappa,R}(R-v)=b_{\kappa,R}^2[1+O_{\kappa,R}(\varepsilon)]\) uniformly on the triangle.

**4. Exact leading integral.** Integrating the conditional angular probability and the independent radial densities gives
\[
\Pr(D>2R-\varepsilon)=\frac{b_{\kappa,R}^2}{\pi\sqrt{a_{\kappa,R}}}
[1+O_{\kappa,R}(\varepsilon)]
\int_{\substack{u,v\ge0\\u+v<\varepsilon}}
(\varepsilon-u-v)^{1/2}\,du\,dv.
\]
The remaining integral is exactly
\[
\int_0^\varepsilon s\sqrt{\varepsilon-s}\,ds
=\frac4{15}\varepsilon^{5/2}.
\]
Consequently the leading constant is \(4b_{\kappa,R}^2/(15\pi\sqrt{a_{\kappa,R}})\), which simplifies to the stated formulas, including the flat limit. The same uniform estimates give the claimed absolute \(O_{\kappa,R}(\varepsilon^{7/2})\) remainder.

**5. Conditional rare shape.** In the joint radial-angular measure, make the change of variables
\[
(u,v,w)=\left(\varepsilon U,\varepsilon V,\sqrt{\varepsilon/a_{\kappa,R}}\,\sqrt W\right).
\]
The Jacobian is \(\varepsilon^{5/2}W^{-1/2}/(2\sqrt{a_{\kappa,R}})\). The rare-event region tends to \(U,V,W\ge0\), \(U+V+W<1\). After division by its probability, the density converges in \(L^1\), by dominated convergence and the preceding uniform local bounds, to
\[
\frac{15}{8}W^{-1/2}\mathbf1_{\{U,V,W>0,\ U+V+W<1\}}.
\]
Writing \(T=1-U-V-W\), this is exactly the \(\operatorname{Dirichlet}(1,1,1/2,1)\) law. The angular sign and initial azimuth are independent uniform marks before and after conditioning. This proves joint convergence.

**6. Inverse curvature.** From the support endpoint one reads \(R=\tfrac12\operatorname{ess\,sup}D\). For \(z>0\), the logarithmic derivative of the normalized coefficient is
\[
\frac{5}{2z}-\frac2{\sinh z}-\frac1{\sinh(2z)}>0,
\]
since \(\sinh z>z\) and \(\sinh(2z)>2z\). This ratio tends to one at zero and is unbounded for large \(z\). Thus it has a unique inverse, recovering \(z\), then \(\kappa=z/R\). Its Taylor expansion \(1+z^2/3+O(z^4)\) follows from the expansions of \(\coth\) and \(\tanh\). This proves the theorem.

## Verification

The standalone `check_hyperbolic_disk.py` computes the exact rare-event probability by a two-dimensional radial quadrature after analytically integrating the angular variable. It checks six fixed radius/curvature pairs, four small thresholds per pair, the conditional rescaled-shape means against their \(\operatorname{Dirichlet}\) limits, and strict numerical curvature ordering across three radii. It prints `HYPERBOLIC_DISK_DIAMETER_RIGIDITY_OK` on success. Numerical integration is corroborative; all limit and uniqueness claims above follow from the analytic argument, not from finite calculations.

## Relationship to prior work

Gugelmann, Panagiotou, and Peter (2012) formulate a rigorous random hyperbolic graph model and state the hyperbolic polar area density and cosine rule. Their principal statistics concern degree sequences and clustering, rather than the fixed-radius \(2R\) endpoint of the intrinsic *ambient* two-point distance law. Kiwi and Mitsche (2014) study the diameter measured in random-graph edges, which is a different metric observable. Tu and Fischbach (2002) discuss distance laws in Euclidean balls, furnishing relevant background for the flat endpoint; the Euclidean exponent alone is not claimed as an independently new fact. Related research on Euclidean disk-to-annulus long-distance transitions, hyperbolic cusp distances, and growing hyperbolic-ball deficits concerns different domains or limiting regimes. The claim here is the fixed-radius curvature-dependent sharp coefficient, conditional Dirichlet rare-shape law, and inverse curvature recovery.

## Limitations

No statistical stability or optimal estimator under finite/noisy samples is proved. The result is only for geodesic disks in complete simply connected two-dimensional nonpositively curved *space forms*, not variable-curvature surfaces or general convex domains. The \(O_{\kappa,R}\) constants can deteriorate when parameters vary. Historical priority is provisional: published general Riemannian endpoint-asymptotic frameworks might cover portions of the law, and no independent audit has been performed.

## References

1. L. Gugelmann, K. Panagiotou, U. Peter, “Random Hyperbolic Graphs: Degree Sequence and Clustering,” first posted 2012-05-07, arXiv:1205.1470, Sections 2–3. https://arxiv.org/abs/1205.1470
2. M. Kiwi, D. Mitsche, “A Bound for the Diameter of Random Hyperbolic Graphs,” first posted 2014-08-13, arXiv:1408.2947, Sections 1–2. https://arxiv.org/abs/1408.2947
3. S.-J. Tu, E. Fischbach, “Random distance distribution for spherical objects: general theory and applications to physics,” *J. Phys. A* 35 (2002), 6557; DOI:10.1088/0305-4470/35/31/303 (bibliographic abstract consulted; full text not inspected).
