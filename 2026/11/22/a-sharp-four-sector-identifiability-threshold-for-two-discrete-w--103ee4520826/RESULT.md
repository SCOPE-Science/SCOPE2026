# A sharp four-sector identifiability threshold for two discrete wrapped Cauchy constructions

## Finding
Fix an integer \(m\geq2\), let \(\theta_j=2\pi j/m\) and \(h=\pi/m\), and discretize a circular wrapped Cauchy density either by integrating over arcs centered at the lattice sites or by normalizing its values at the sites. The following is a sharp population-identifiability theorem.

**Theorem.** In the centered-bin, origin-registered model defined below:

1. For \(m=2\) and \(m=3\), the sets of marginalized and origin-registered conditionalized probability vectors coincide *exactly*. Every positive-concentration marginalized law has a unique positive-concentration conditionalized representation, with a generally different concentration; both families contain the uniform vector. Consequently, observation of arbitrarily many independent sector labels cannot distinguish these construction mechanisms without additional information.
2. For every \(m\geq4\) and every marginalized concentration \(0<\rho<1\), the resulting probability vector differs from **every** conditionalized wrapped Cauchy vector, even if the latter may choose both its concentration and an arbitrary angular location. The uniform distribution, obtained at zero concentration, belongs to both families.
3. For \(m\geq4\), an explicit three-probability reciprocal curvature contrast \(K_m\) is strictly positive under every nonuniform centered-bin marginalized law, and is exactly zero under every origin-registered conditionalized law. The empirical plug-in contrast consequently gives a consistent test for the two registered mechanisms at each fixed positive concentration.

This is a distinction between *families after free refitting of concentration*, rather than a comparison using equal numerical parameter values.

## Assumptions and scope
Take \(m\in\{2,3,\ldots\}\) and \(0\le\rho,\eta<1\). Let
\[
f_\rho(\theta)=\frac{1-\rho^2}{2\pi\{1+\rho^2-2\rho\cos\theta\}},\qquad\theta\pmod{2\pi}.
\]
The marginalized, bin-centered masses are
\[
P_{\rho,m}(j)=\int_{\theta_j-h}^{\theta_j+h} f_\rho(\theta)\,d\theta,
\quad j=0,\ldots,m-1,
\]
where integration is on the periodic circle. The conditionalized probability vector, allowing arbitrary angular location \(\nu\), is
\[
Q_{\eta,\nu,m}(j)=
\frac{\{1+\eta^2-2\eta\cos(\theta_j-\nu)\}^{-1}}
{\sum_{k=0}^{m-1}\{1+\eta^2-2\eta\cos(\theta_k-\nu)\}^{-1}}.
\]
For an origin-registered conditionalized vector put \(\nu=0\). The bin-centered convention corresponds to the conventional consecutive bins with parent location at a bin midpoint. That registration is essential: the theorem does not characterize every possible off-center marginalized parent location.

## Proof
**Step 1 (an exact closed form with the correct branch).** Put
\[
a=(1+\rho^2)\cos h,\qquad b=2\rho,\qquad c=(1-\rho^2)\sin h>0.
\]
Using the wrapped Cauchy antiderivative with a tangent-half-angle substitution and taking the continuous argument branch in \((0,\pi)\) gives, for every \(j\),
\[
P_{\rho,m}(j)=\frac1\pi\operatorname{Arg}\{a-b\cos\theta_j+ic\}
=\frac1\pi\operatorname{arccot}\!\left(\frac{a-b\cos\theta_j}{c}\right),
\tag{1}
\]
where \(\operatorname{Arg}(u+ic)\in(0,\pi)\) and \(\operatorname{arccot}:\mathbb R\to(0,\pi)\). The normalization and positivity follow directly from the defining integrals. Formula (1) is valid even if the arc crosses the circular origin and does not rely on a principal-value arctangent that would lose a multiple of \(\pi\).

**Step 2 (strict reciprocal convexity).** With \(x=\cos\theta\in[-1,1]\), set
\[
G(x)=\frac{\pi}{\operatorname{arccot}\bigl((a-bx)/c\bigr)},\quad
y=\frac{a-bx}{c},\quad t=\operatorname{arccot}y.
\]
Twice differentiating (using \(dt/dy=-1/(1+y^2)\)) yields the exact identity
\[
G''(x)=\frac{2\pi b^2}{c^2}
\frac{1-y\,t}{(1+y^2)^2t^3}.
\tag{2}
\]
For \(y\le0\), \(1-yt>0\). For \(y>0\), \(t=\arctan(1/y)<1/y\), again giving \(1-yt>0\). Thus \(G\) is strictly convex throughout \([-1,1]\) whenever \(\rho>0\). Moreover \(G(\cos\theta_j)=1/P_{\rho,m}(j)\).

**Step 3 (the positive contrast).** For \(m\ge4\), the three distinct cosine values
\[
x_0=1>x_1=\cos(2\pi/m)>x_2=\cos(4\pi/m)
\]
exist. Define, for positive probability vectors \(p=(p_0,\ldots,p_{m-1})\),
\[
K_m(p)=\frac{p_0^{-1}-p_1^{-1}}{x_0-x_1}
-\frac{p_1^{-1}-p_2^{-1}}{x_1-x_2}.
\tag{3}
\]
Strict convexity (2), equivalently strict increase of adjacent divided differences, gives \(K_m(P_{\rho,m})>0\) for \(\rho>0\). For every origin-registered conditionalized model,
\[
Q_{\eta,0,m}(j)^{-1}=Z\{1+\eta^2-2\eta\cos\theta_j\},
\quad Z=\sum_k(1+\eta^2-2\eta\cos\theta_k)^{-1},
\]
which is an affine function of \(\cos\theta_j\); hence \(K_m(Q_{\eta,0,m})=0\), including at \(\eta=0\).

**Step 4 (conditionalized angular location does not restore equality).** Suppose \(m\ge4\), \(\rho>0\), and \(P_{\rho,m}=Q_{\eta,\nu,m}\). From (1) and the strict decrease of the original wrapped density away from zero, \(P_{\rho,m}\) is nonuniform. Therefore \(\eta>0\). Also \(P_{\rho,m}(1)=P_{\rho,m}(m-1)\). Equality of the two conditionalized denominators for the sites \(\pm 2\pi/m\) then forces
\[
\cos(2\pi/m-\nu)=\cos(2\pi/m+\nu),
\quad 2\sin(2\pi/m)\sin\nu=0.
\]
Since \(m\ge4\), \(\sin(2\pi/m)\ne0\). Thus \(\nu=0\) or \(\pi\) modulo \(2\pi\), and \(Q_{\eta,\nu,m}(j)^{-1}\) is affine in \(\cos\theta_j\) in either case. Its contrast is therefore zero, contradicting Step 3. This proves disjointness for every nonuniform centered-bin marginalized law, even against a free-location conditionalized family.

**Step 5 (sharpness at two and three sectors).** At \(m=2,3\), reflection symmetry \(P(j)=P(m-j)\) implies the whole probability vector is fixed by its central-sector mass \(P(0)\). The same holds for \(Q_{\eta,0,m}\). Direct integration yields
\[
P_{\rho,m}(0)=\frac2\pi\arctan\!\left[
\frac{1+\rho}{1-\rho}\tan\frac{\pi}{2m}\right],
\tag{4}
\]
which increases strictly and continuously from \(1/m\) to \(1\) as \(\rho\) increases from zero to one. For the conditionalized construction, put \(d_m=\cos(2\pi/m)<1\). The equal off-center cosines for \(m=2,3\) imply
\[
Q_{\eta,0,m}(0)=
\left[1+(m-1)\frac{(1-\eta)^2}{1+\eta^2-2\eta d_m}\right]^{-1}.
\tag{5}
\]
Since \(\eta/(1-\eta)^2\) strictly increases on \([0,1)\), (5) is strictly increasing and continuous from \(1/m\) to \(1\). Equations (4)–(5) provide the unique reparameterization between the two full families. Identical probability vectors yield identical likelihoods for every sample size, so no label-based statistical test can identify which construction generated the law in these resolutions.

**Step 6 (consistent registered-model separation).** For \(m\ge4\), let \(\widehat p_j\) be the sector sample frequencies from \(n\) independent labels. Define \(\widehat K_m\) by (3) whenever its three entries are positive, and define the test arbitrarily otherwise. At fixed interior parameters each true cell probability is positive and the probability of a zero empirical cell tends to zero exponentially. By the multinomial central limit theorem and the delta method, under any fixed registered conditionalized law \(\widehat K_m=O_p(n^{-1/2})\); under any fixed nonuniform centered-bin marginalized law \(\widehat K_m\to K_m(P)>0\) in probability. Therefore the test \(\widehat K_m>n^{-1/3}\) has asymptotic false-positive probability zero and asymptotic power one. This statement concerns registered conditionalized laws; for an unrestricted conditionalized angular location the population disjointness result remains valid but the same scalar contrast is not generally centered at zero.

## Verification
Run \(\texttt{python3 check.py}\) using the Python standard library. The program verifies (1) against independently evaluated composite Simpson integrals over bin arcs, normalized and symmetric probability vectors, the exact two- and three-sector reparameterization, the strict sign of (3) for multiple resolutions and concentrations, the zero conditionalized contrast, and (2) against finite differences. In the recorded run **2,814 assertions passed**. This is a numerical reproducibility check, *not* a substitute for the analytical proofs in Steps 1–6. In the illustrative four-sector case \(\rho=1/2\), the bin masses are approximately
\[
(0.5686116674,\ 0.1720208696,\ 0.0873465934,\ 0.1720208696)
\]
and \(K_4\approx1.5808166313>0\).

## Relationship to prior work
Mardia and Sriram (2020, revised 2022; journal publication 2022) introduced the marginalized and conditionalized discrete circular families, including their wrapped Cauchy specializations, and studied model misspecification. Their Theorem 2 characterizes equality when the **same parent** is required to agree for **all angular spacings and origins**. That does not imply either the equality of the refitted two- and three-sector families or their disjointness after concentration and conditionalized angular location are freely changed at a **fixed** sector count. The theorem here determines this resolution threshold and gives the explicit strictly signed contrast. The conditionalized wrapped Cauchy models in Girija–Srihari–Srinivas (2019) and Imoto–Shieh–Shimizu (2020) are related constructions rather than this fixed-resolution two-family classification.

## Limitations
The origin for the marginalized parent is fixed at the center of one of the equal sectors; no theorem is asserted for off-center marginalized parents. The separation is a population-law statement for every fixed \(\rho>0\), with uniformity as a shared boundary; it does not give uniform finite-sample power as concentration approaches zero. The plug-in contrast is an elementary consistent test only against the registered conditionalized subclass, while population disjointness holds against all conditionalized angular locations.

## References
1. K. V. Mardia and K. Sriram, *Families of Discrete Circular Distributions with Some Novel Applications*, arXiv:2009.05437, first submitted 11 September 2020, https://arxiv.org/abs/2009.05437; *Sankhya A*, published online 22 November 2022, https://doi.org/10.1007/s13171-022-00298-z. See Definitions 1–2, 5–6, Theorem 2, and Section 5.
2. S. V. S. Girija, G. V. L. N. Srihari and R. Srinivas, *On Discrete Wrapped Cauchy Model*, *Mathematical Theory and Modeling* 9 (2019), 15–23, https://pdfs.semanticscholar.org/4504/44a711d1ae3b936c6118149af1d9737b3726.pdf.
3. T. Imoto, G. S. Shieh and K. Shimizu, *Discrete Circular Distributions with Applications to Shared Orthologs of Paired Circular Genomes*, *Computer Modeling in Engineering & Sciences* 123 (2020), 1131–1149, https://staff.stat.sinica.edu.tw/gshieh/CMES/Discrete_Circular_Distributions_with_Applications_to_Shared_Orthologs_of_Paired_Circular_Genomes.pdf.
