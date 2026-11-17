# Dyson circular shape laws at the maximal perimeter of random spherical triangles

## Finding
Take independent uniform points \(X_1,X_2,X_3\) on \(S^{d-1}\) for any integer \(d\ge3\). Write \(a=d(X_2,X_3)\), \(b=d(X_1,X_3)\), \(c=d(X_1,X_2)\), and \(P=a+b+c\), where each distance is the length of a minimizing great-circle arc. Put \(\alpha=(d-2)/2\). Then \(P<2\pi\) almost surely and
\[
\Pr(P>2\pi-\varepsilon)=C_d\varepsilon^\alpha+o(\varepsilon^\alpha),\quad
C_d=\frac{\sqrt\pi\,\Gamma(d/2)^2}{2(d-2)\Gamma((d-1)/2)\Gamma((d-2)/2)}4^{-\alpha}
\frac{\Gamma(1+3\alpha/2)}{\Gamma(1+\alpha/2)^3}.
\]
For instance \(C_3=\pi\Gamma(7/4)/(16\Gamma(5/4)^3)\), \(C_4=3/(4\pi)\), and \(C_6=1/4\).

Conditioned on \(P>2\pi-\varepsilon\), the joint law of \((b,c)\) converges **in total variation** to the density
\[
h_d(b,c)=\frac{\left[\sin b\sin c\sin(2\pi-b-c)\right]^\alpha}{I_\alpha}
\boldsymbol1_{\{0<b,c<\pi,\ b+c>\pi\}},\qquad
I_\alpha=\frac{\pi^2}{2\cdot8^\alpha}\frac{\Gamma(1+3\alpha/2)}{\Gamma(1+\alpha/2)^3}.
\]
The third side converges to \(a=2\pi-b-c\). Defining the three complementary limiting side gaps \(g_a=\pi-a\), \(g_b=\pi-b\), \(g_c=\pi-c\), we have \(g_a+g_b+g_c=\pi\). They are the cyclic half-gaps of three circular phases with the density of a **Dyson circular \(\beta\)-ensemble**, where \(\beta=\alpha=(d-2)/2\). Specifically dimensions \(d=4,6,10\) produce circular orthogonal, unitary and symplectic eigenphase-gap laws (Dyson indices 1, 2, 4).

There is an independent transverse mark. Let \(\gamma\) denote the intrinsic angle at \(X_1\), and on the event \(\pi<b+c<2\pi\) and \(a_0=2\pi-b-c>\varepsilon\), define
\[
T_\varepsilon=(\pi-\gamma)\sqrt{\frac{\sin b\sin c}{2\varepsilon\sin a_0}}.
\]
Set this mark to zero on the remaining (asymptotically negligible) part of \(P>2\pi-\varepsilon\). Then conditionally on that rare event, \((b,c,T_\varepsilon)\) converges **in total variation** to the product of \(h_d(b,c)\,db\,dc\) and an independent \(\mathrm{Beta}(d-2,1)\) variable, with density \((d-2)t^{d-3}\boldsymbol1_{0<t<1}\).

## Assumptions and scope
The three vertices are independent and uniformly distributed with respect to normalized surface measure on the unit sphere \(S^{d-1}\). The ambient Euclidean dimension \(d\) is any fixed integer at least three. Geodesic distances are shorter great-circle arcs, with values in \([0,\pi]\). The limit is as \(\varepsilon\downarrow0\) at fixed \(d\), not a joint dimension–threshold limit. The formula concerns the perimeter of this three-vertex shortest-geodesic cycle; no convex hull or oriented area convention is needed. Degeneracies have probability zero.

## Proof
**1. Independent spherical coordinates.** Fix \(X_1\) by rotational invariance. The distances \(b,c\) are independent, each with density
\[
f_d(s)=F_d\sin^{d-2}s,\quad F_d=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)},\quad 0<s<\pi.
\]
Conditional on \((b,c)\), the angle \(\gamma\) between the unit tangent directions of \(X_2\) and \(X_3\) is independent of them and has density
\[
g_d(\gamma)=G_d\sin^{d-3}\gamma,\quad G_d=\frac{\Gamma((d-1)/2)}{\sqrt\pi\Gamma((d-2)/2)}.
\]
The spherical cosine formula reads
\[
\cos a=\cos b\cos c+\sin b\sin c\cos\gamma.
\]
It implies \(a\le\arccos(\cos(b+c))\), and therefore \(P\le 2\pi\). Equality requires the measure-zero condition \(\gamma=\pi\) in the region \(b+c>\pi\), establishing the almost-sure strict inequality.

**2. Interior boundary layer.** On \(b+c>\pi\), put \(a_0=2\pi-b-c\in(0,\pi)\). With \(\delta=\pi-\gamma\), the cosine law becomes
\[
\cos a=\cos a_0+\sin b\sin c\,(1-\cos\delta).
\]
At each fixed interior pair \((b,c)\), expansion at \(\delta=0\) yields
\[
2\pi-P=a_0-a=\frac{\sin b\sin c}{2\sin a_0}\delta^2+o(\delta^2).
\]
Since \(\Pr(\pi-\gamma<r)\sim G_d r^{d-2}/(d-2)\), it follows for such fixed pairs that
\[
\varepsilon^{-\alpha}\Pr(P>2\pi-\varepsilon\mid b,c)
\longrightarrow \frac{G_d}{d-2}\left(\frac{2\sin a_0}{\sin b\sin c}\right)^\alpha.
\]

**3. Boundary uniformity and integration.** The exact condition for \(b+c>\pi\) and \(a_0>\varepsilon\) is
\[
1-\cos\delta < \frac{\cos(a_0-\varepsilon)-\cos a_0}{\sin b\sin c}.
\]
The cap probability is bounded by a constant depending on \(d\) times the right-hand side to power \(\alpha\). The numerator is at most \(\varepsilon(\sin a_0+\varepsilon)\), so after multiplication by \(f_d(b)f_d(c)\) and division by \(\varepsilon^\alpha\), the integrand is dominated by an integrable multiple of \([\sin b\sin c]^\alpha\). The sliver \(a_0\le\varepsilon\) has probability \(O(\varepsilon^{2d-2})\). In the other region \(b+c\le\pi\), the maximum perimeter is \(2(b+c)\), so a near-maximal event forces \(\pi-b-c<\varepsilon/2\); the cosine law and the angular-cap estimate bound its integrated probability by \(O(\varepsilon^{d-1})\). Both remainders are \(o(\varepsilon^\alpha)\). Dominated convergence therefore gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-\alpha}\Pr(P>2\pi-\varepsilon)
=F_d^2\frac{G_d}{d-2}2^\alpha
\!\int_{b+c>\pi}[\sin b\sin c\sin(2\pi-b-c)]^\alpha\,db\,dc.
\]

**4. Circular integral and constant.** Use \(x=\pi-b\), \(y=\pi-c\), \(z=\pi-x-y=\pi-a_0\), so \(x,y,z>0\), \(x+y+z=\pi\). The three circular angles \(0,2x,2(x+y)\) have pairwise chord product \(8\sin x\sin y\sin z\). The circular Dyson normalization identity for three particles,
\[
\int_{[0,2\pi]^3}\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^\alpha d\theta_1d\theta_2d\theta_3
=(2\pi)^3\frac{\Gamma(1+3\alpha/2)}{\Gamma(1+\alpha/2)^3},
\]
implies, by fixing one phase and ordering the other two,
\[
\int_{x,y>0,x+y<\pi}[\sin x\sin y\sin(x+y)]^\alpha\,dx\,dy
=\frac{\pi^2}{2\cdot8^\alpha}\frac{\Gamma(1+3\alpha/2)}{\Gamma(1+\alpha/2)^3}=I_\alpha.
\]
Substitution into Step 3 simplifies exactly to the stated \(C_d\). Because the normalized \((b,c)\)-densities converge pointwise on the interior to \(h_d\) and their total integrals converge to one, Scheffé's lemma yields convergence in total variation. The explicit circular-phase mapping proves the Dyson gap characterization.

**5. Transverse mark.** In the interior, the cap scale is \(r_\varepsilon=\sqrt{2\varepsilon\sin a_0/(\sin b\sin c)}\). The substitution \(\delta=r_\varepsilon t\), together with \(\sin^{d-3}(\delta)\sim\delta^{d-3}\), gives the limiting conditional mark density \((d-2)t^{d-3}\boldsymbol1_{0<t<1}\), with a factor independent of \((b,c)\). The same integrable bound from Step 3 controls the joint transformed densities, and the excluded slivers have vanishing conditional mass. Scheffé's lemma on the extended marked state space proves the asserted joint total-variation convergence.

## Verification
The standalone script `check_perimeter.py` computes the finite-\(\varepsilon\) event probability by independent two-dimensional Gaussian quadrature of the exact angular beta probability, not by sampling the asymptotic expression. For \(d=3,4,5,6,8\), the computed ratios \(\Pr(P>2\pi-\varepsilon)/(C_d\varepsilon^\alpha)\) approach 1 as \(\varepsilon\downarrow0\); at \(\varepsilon=0.002\) they lie between 0.99999 and 1.00137. The script also checks the exact cases \(C_4=3/(4\pi)\), \(C_6=1/4\), and numerically checks the circular integral normalization for two values of \(\alpha\). These are numerical consistency checks rather than a computer-assisted proof of the continuum limit.

## Relationship to prior work
Finch and Jones, *Random Spherical Triangles*, arXiv:1009.5329 (first available 2010-09-27), discuss the classical three-dimensional random spherical triangle and reproduce the earlier Jones–Benyon-Tinker complete integral for its perimeter density. Their full text observes divergence at \(2\pi\). Thus the **three-dimensional marginal** perimeter tail, obtainable in principle by expanding that known density, is **not** treated as separately original. R. E. Miles' 1971 paper supplies a classical trivariate side-density treatment on the ordinary two-sphere; its full text was not accessible for comparison. The present specific claim is the all-dimensional sharp endpoint coefficient plus the independent Beta transverse mark and the identification of the conditioned complementary gaps with Dyson circular \(\beta\) ensembles, including the orthogonal, unitary, and symplectic cases. The circular Selberg/Dyson normalization formula itself is classical and is used, not claimed new.

## Limitations
The proof fixes dimension and assumes independent uniform spherical vertices. It gives no quantitative error term or uniform-in-dimension bound, and no analogue for curved nonround manifolds, nonuniform samples, or geodesic cycles of more than three vertices. The conditional law is for the specified shortest-geodesic perimeter event; phase rotations and labels are handled only through circular gap distributions. Historical priority remains provisional because a highly relevant 1971 full text and an unpublished 1994 manuscript were not available. The mathematical argument is internally checked but has not undergone independent validation.

## References
1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, submitted 2010-09-27; full text https://arxiv.org/html/1009.5329v3.
2. R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, Sankhyā A **33** (1971), 145–174, https://www.jstor.org/stable/25049720.
3. Dyson circular-ensemble/Selberg normalization, standard formula documented at https://en.wikipedia.org/wiki/Circular_ensemble (the normalization identity is used as classical background).
