# Marked cusp-pair and midpoint laws for distant points in ideal hyperbolic polygons

## Finding

Let \(P\) be a fixed convex ideal hyperbolic \(n\)-gon in curvature \(-1\), with \(n\ge3\). Draw \(X,Y\) independently uniformly for hyperbolic area and put \(D=d_{\mathbb H^2}(X,Y)\). The leading scalar distance tail for this model is **prior work**, not the finding here. The new result is the limiting **marked geometry** under \(D>R\), including a total-variation statement, the behavior of the geodesic midpoint, and a labelled shape-recovery formula for ideal quadrilaterals.

Normalize by an isometry so the ideal vertices are \(a_1<\cdots<a_m<\infty\), followed by \(\infty\), where \(m=n-1\). Put \(w_\infty=a_m-a_1\), \(w_1=(a_2-a_1)^{-1}\), \(w_m=(a_m-a_{m-1})^{-1}\), and for \(1<i<m\),
\[
w_i=(a_i-a_{i-1})^{-1}+(a_{i+1}-a_i)^{-1}.
\]
Let \(g_{ij}=(a_i-a_j)^2\) for finite distinct vertices, and \(g_{i\infty}=g_{\infty i}=1\). Define
\[
S=\sum_{k\ne\ell}w_kw_\ell g_{k\ell},\qquad p_{ij}=\frac{w_iw_jg_{ij}}S\quad(i\ne j).
\]
Choose sufficiently high disjoint horoball cusp charts \(\gamma_i(z)=-1/(z-a_i)\) at finite vertices and \(\gamma_\infty(z)=z\), with chart heights \(H_i\), in which the polygon is exactly a vertical strip of width \(w_i\). Give each strip a normalized horizontal coordinate \(\Xi_i\in(0,1)\). On the event that \(X\) and \(Y\) belong to distinct such cusp strips, denote their ordered cusp labels by \(I,J\), their chart heights by \(Y_I,Y_J\), and set \(U_R=\log(Y_I/H_I)/R\), \(E_R=D-R\). Outside that event assign any fixed dummy values to the labels and marks.

**Theorem.** Conditional on \(D>R\), the event of two distinct cusp strips has probability tending to one, and
\[
\boxed{\mathcal L(I,J,\Xi_I,\Xi_J,U_R,E_R\mid D>R)\ \xrightarrow{\mathrm{TV}}\ \sum_{i\ne j}p_{ij}\,\delta_{(i,j)}\otimes\mathrm{Unif}(0,1)^{\otimes3}\otimes\mathrm{Exp}(1).}
\]
Here the three independent uniforms are the two transverse strip coordinates and the logarithmic depth split \(U\), while the exponential mark is the positive distance overshoot. In particular, the two logarithmic depths, divided by \(R\), converge *weakly* to \((U,1-U)\); no total-variation convergence is claimed for this two-coordinate singular limit.

Let \(M_R\) be the ambient hyperbolic midpoint of the geodesic from \(X\) to \(Y\). With conditional probability tending to one, it lies in one of the cusp neighborhoods and its label is the label of the endpoint having the larger logarithmic depth. Its cusp-chart log height, divided by \(R\), converges **weakly** to \(|U-1/2|\), hence has limiting density \(2\) on \((0,1/2)\). The midpoint's cusp label is determined by \(I\) when \(U>1/2\) and by \(J\) when \(U<1/2\), independently of the limiting overshoot and transverse coordinates.

For a labelled ideal quadrilateral with consecutive vertices \(0,1,t,\infty\), \(t>1\), the conditional **unordered** endpoint-cusp probabilities satisfy
\[
\begin{array}{c|c}
\text{cusp pair}&\text{limiting probability}\\ \hline
\{0,t\},\ \{1,\infty\}&1/4\ \text{each}\\
\{0,1\},\ \{t,\infty\}&1/(4t)\ \text{each}\\
\{1,t\},\ \{0,\infty\}&(t-1)/(4t)\ \text{each}.
\end{array}
\]
Thus exactly half of very long pairs terminate at opposite ideal vertices, **for every shape**, and the marked probabilities recover the labelled cross-ratio by \(t=1/[4\lim\Pr(\{I,J\}=\{0,1\}\mid D>R)]\). The limiting cusp occupied by the *midpoint* is uniformly distributed over all four vertices, regardless of \(t\). These shape-recovery and midpoint conclusions do not follow from knowing the scalar distance-tail coefficient alone.

## Assumptions and scope

The polygon is fixed and has all vertices ideal; it carries the ambient, geodesically convex hyperbolic metric, not a quotient-surface metric. Uniform distribution is normalized area, which is \(A=(n-2)\pi\) by Gauss--Bonnet. Cusp labels are attached to fixed, disjoint horoball neighborhoods whose complement is compact. The limiting marked law is independent of the cutoff heights and depends on polygon shape through the explicit categorical weights. The convention for the irrelevant complement event does not affect the limit.

## Proof

**1. Exact normalized cusp area.** In the upper-half-plane, each sufficiently deep cusp becomes the strip \(\xi\in(l_i,l_i+w_i)\), \(y>H_i\), in the chart \(\gamma_i\). Write \(y=H_i e^u\), \(u>0\), and \(\xi=l_i+w_ix\), \(0<x<1\). Since \(dA=d\xi\,dy/y^2\), the normalized area element is exactly \((w_i/(AH_i))e^{-u}\,du\,dx\). For two points in distinct cusps, the four coordinates \((u,v,x,z)\) therefore have a product density proportional to \(e^{-(u+v)}\).

**2. Exact pairwise distance asymptotics and differentiability.** The half-plane identity \(\cosh D=1+|z_1-z_2|^2/(2\operatorname{Im}z_1\operatorname{Im}z_2)\), together with \(z_i=a_i-1/(l_i+w_ix+iH_i e^u)\) at finite cusps and \(z_\infty=l_\infty+w_\infty x+iH_\infty e^u\), gives, uniformly in both transverse coordinates,
\[
D=u+v+\kappa_{ij}+O_P(e^{-u}+e^{-v}),\qquad\kappa_{ij}=\log(g_{ij}H_iH_j).
\]
On regions where \(u,v\to\infty\), direct differentiation of this explicit expression also gives \(\partial_vD=1+O_P(e^{-u}+e^{-v})\). Both statements hold uniformly on \(u,v\ge\delta R\) for any fixed \(\delta>0\), with errors vanishing exponentially in \(R\).

**3. Leading mass and localization.** For independent exponential logarithmic cusp depths, exactly
\[
\int_{u,v\ge0}e^{-u-v}\mathbf1_{\{u+v>s\}}\,du\,dv=(s+1)e^{-s}.
\]
The already established scalar cusp-pair distance theorem (see References) therefore supplies
\[
\Pr(D>R)=\frac{S}{A^2}R e^{-R}+O_P(e^{-R}),
\]
The scalar formula is also verified here directly, rather than treated as an unexamined premise. If two points occupy the same cusp, a path consisting of two vertical legs and a horizontal segment gives \(D\le |u-v|+w_i/H_i\); integrating \(e^{-u-v}\) over \(|u-v|>R-O_P(1)\) gives \(O_P(e^{-R})\). If one point is in the compact complement of the cusps, its distance to cusp depth \(u\) is at most \(u+O_P(1)\), again contributing \(O_P(e^{-R})\). For a distinct pair, the difference between the true-distance indicator and the indicator of \(u+v+\kappa_{ij}>R\) is confined to \(|u+v-(R-\kappa_{ij})|\le C_P(e^{-u}+e^{-v})\). At a fixed sum \(s=u+v\) near \(R-\kappa_{ij}\), the permitted sum width is \(O_P(e^{-u}+e^{-s+u})\); its integral over \(0<u<s\) is bounded independently of \(R\). As \(e^{-s}=O_P(e^{-R})\) there, the total indicator replacement error is \(O_P(e^{-R})\). The exponential convolution identity therefore yields the stated scalar coefficient independently. For each ordered distinct cusp pair, the leading contribution is \((w_iw_jg_{ij}/A^2)R e^{-R}\). For any fixed \(\delta\in(0,1/2)\), omitting the region \(u/R\in[\delta,1-\delta]\) removes asymptotically at most a fraction \(2\delta\) of the distinct-cusp rare-event mass. Similarly the conditional overshoot is tight: for \(s\ge0\), the scalar ratio \(\Pr(D>R+s)/\Pr(D>R)\to e^{-s}\).

**4. A joint density and total-variation limit.** On \(\delta\le u/R\le1-\delta\) put \(q=u/R\) and \(e=D-R\). With \(u=Rq\), the inverse relation in Step 2 satisfies \(v=R+e-Rq-\kappa_{ij}+o(1)\) and \(\partial v/\partial e=1+o(1)\), uniformly for \(q\) in this compact interval, \(e\) in compact subsets of \((0,\infty)\), and transverse coordinates in \((0,1)^2\). Hence the transformed unnormalized density is
\[
\frac{w_iw_j}{A^2H_iH_j}\, R e^{-u-v}\frac{\partial v}{\partial e}
=\frac{w_iw_jg_{ij}}{A^2}R e^{-R}e^{-e}(1+o(1)).
\]
Divide by the preceding survival probability. The limiting joint density in \((q,e,x,z)\) for a fixed pair \((i,j)\) is exactly \(p_{ij}\mathbf1_{0<q<1,e>0,0<x,z<1}e^{-e}\). Step 3 supplies tightness for \(q\) and \(e\); in addition, the complement of distinct-cusp pairs vanishes. The density convergence plus tightness yields \(L^1\) convergence by truncation and Scheffé's lemma. Summing finitely many labels establishes the claimed total variation convergence.

**5. Midpoint geometry.** For two upper-half-plane points \(z_k=x_k+iy_k\), their hyperbolic midpoint \(m=x_m+iy_m\) obeys the *exact* formulas
\[
x_m=\frac{x_1/y_1+x_2/y_2}{1/y_1+1/y_2},\qquad
y_m=\frac{2\cosh(D/2)}{1/y_1+1/y_2}.
\]
They follow by summing the unit timelike hyperboloid vectors and renormalizing. Substituting the cusp expressions from Step 2 shows that, uniformly when \(u/R\) stays a positive distance from both \(0,1\) and \(1/2\), \(m\) lies in the endpoint cusp with greater \(u\) or \(v\) and its logarithmic chart height equals \(|u-v|/2+O_P(1)\). The exceptional strips around these three values have vanishing conditional probability as their widths shrink, by Step 4. Thus the midpoint cusp label tends to the stated selection rule and its normalized logarithmic height tends to \(|U-1/2|\) in distribution. The pushforward of a uniform \(U\) has density \(2\) on \((0,1/2)\).

**6. Quadrilateral calculation.** For vertices \(0,1,t,\infty\), \(t>1\), the widths in cyclic order are \(1,\,t/(t-1),\,1/(t-1),\,t\). The sum of the six unordered pair weights is \(4t^2/(t-1)\). Their respective weights are \(t^2/(t-1)\) for each opposite pair, \(t/(t-1)\) for each pair in the second row of the table, and \(t\) for each pair in the third row. Dividing gives the table. The weighted row sums for the four vertices are all equal to \(2t^2/(t-1)\), so the midpoint's asymptotic cusp label is exactly uniform. The formula for the labelled cross-ratio follows by inversion.

## Verification

The accompanying independent numerical checker samples hyperbolic-area-uniform points using an exact ideal-triangle decomposition, computes distances from their defining half-plane formula, and compares two direct-simulation survival frequencies to the published leading coefficient. It separately reconstructs every cusp-pair weight, checks the quadrilateral identities for two distinct cross ratios, and tests the uniform pairwise distance expansion in each of six cusp pairs. A targeted independent computation uses the exact sum-of-exponentials conditional distribution as an importance proposal to check the marked geometry and the exact hyperbolic-midpoint identity. That proposal is deliberately described as approximate for the **true** rare-event condition; no simulation is presented as a proof of total variation. Install `requirements.txt` and run `python verify_marked_cusps.py` from the package directory. The successful output ends with `CUSP_MARKED_CONDITIONAL_GEOMETRY_OK`.

## Relationship to prior work

The published finding *Cusp-pair tails for random distances in ideal hyperbolic polygons* (published-finding corpus, November 8, 2026) already proves the scalar tail \(\Pr(D>R)=C(P)R e^{-R}+O_P(e^{-R})\) and the explicit weights' **sum**. That scalar asymptotic and the cusp-strip construction are prior contributions; neither is asserted to be new here. Its full text was examined, including the proof and limitations. It does **not** state a joint conditional total-variation limit, the midpoint's cusp-depth law, or the quadrilateral marked inverse formula. Knowing one summed coefficient cannot in itself determine six separate label frequencies or a conditional spatial distribution. The present theorem supplies that missing marked law, and the proved quadrilateral rigidity shows why retaining the marks matters.

Earlier literature on ideal hyperbolic polygons, notably Castle–Peyerimhoff–Siburg (2011) and Parker–Peyerimhoff–Siburg (arXiv:1607.07383, submitted July 25, 2016), studies deterministic billiard/geodesic length extrema, not independent uniform-area point pairs. The full accessible text of the latter was examined. Searches for conditional cuspidal depth splitting, rare hyperbolic distance midpoints and equivalent large-distance marks did not identify a covering theorem. The conditional exponential-convolution mechanism is elementary once the uniform cusp geometry is established; no priority claim is made for that probability mechanism in isolation.

## Limitations

The theorem is for fixed convex all-ideal polygons. There is no uniformity under degeneration of the ideal vertices and no claim for finite-vertex polygons, random polygon shapes, quotient-surface intrinsic distances, or nonsmooth cusp completions. The full two-depth vector has only weak convergence to its singular limit; the **charted** mark has total variation convergence. The midpoint statement is weak convergence. Historical priority remains provisional, especially for older general conditional cusp-excursion or marked regular-variation theorems. Numerical corroboration is not independent mathematical validation.

## References

- J. R. Parker, N. Peyerimhoff and K. F. Siburg, *Minimizing length of billiard trajectories in hyperbolic polygons*, arXiv:1607.07383, first submitted July 25, 2016, https://arxiv.org/abs/1607.07383.
- S. Castle, N. Peyerimhoff and K. F. Siburg, *Billiards in ideal hyperbolic polygons*, Discrete and Continuous Dynamical Systems 29 (2011), 893–908, https://doi.org/10.3934/dcds.2011.29.893 (first available online November 2010; primary MSC includes 53A35).
- *Cusp-pair tails for random distances in ideal hyperbolic polygons*, published-finding corpus public record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cusp-pair-tails-for-random-distances-in-ideal-hyperbolic-polygon--102d92c50bd6 (full `RESULT.md` inspected; scalar leading-order theorem credited).
