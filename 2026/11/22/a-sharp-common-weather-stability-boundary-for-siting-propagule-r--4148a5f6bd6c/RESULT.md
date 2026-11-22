# A sharp common-weather stability boundary for siting propagule release between two habitats

## Finding
Consider one release source on a transect, two identical receiving habitats at normalized positions \(\pm d\), and common random environmental intensity \(Z\sim\mathrm{Exp}(1)\). Conditional on \(Z\), successful arrivals are independent Poisson counts with respective means \(\lambda Z/[1+(x-d)^2]\) and \(\lambda Z/[1+(x+d)^2]\). The objective \(J(x)\) is the probability that **both** habitats receive at least one arrival.

Write \(q=d^2\) and
\[
B(q,\lambda)=2(q+1)^2(q-1)-\lambda(q+1)(q+5)-\lambda^2(7q+3).
\]
If \(0<q\le1\), the central release point \(x=0\) is a strict local maximum for every \(\lambda>0\). If \(q>1\), there is exactly one critical positive intensity
\[
\lambda_c(q)=\frac{4(q+1)^2(q-1)}{(q+1)(q+5)+\sqrt{(q+1)^2(q+5)^2+8(7q+3)(q+1)^2(q-1)}}.
\]
For \(0<\lambda<\lambda_c(q)\) the midpoint is a strict local **minimum** and at least two symmetric off-centre global maximizers exist; for \(\lambda>\lambda_c(q)\) the midpoint is a strict local maximum. At equality it is a degenerate strict local maximum with a strictly negative quartic leading departure. No global uniqueness or midpoint global optimality is claimed for \(\lambda\ge\lambda_c(q)\).

This common-environment transition precedes the independent-environment counterpart: \(0<\lambda_c(q)<q-1\) whenever \(q>1\). Its limits are
\[
\lambda_c(q)\sim\tfrac23(q-1)\quad(q\downarrow1),\qquad
\lambda_c(q)/q\longrightarrow(\sqrt{57}-1)/14\quad(q\to\infty).
\]
Consequently, the dependence structure of environmental forcing changes the local release-site stability boundary even with the same single-habitat mean founding law.

## Assumptions and scope
The source is restricted to the entire one-dimensional transect, with location \(x\in\mathbb R\), and receiving points fixed at \(\pm d\), \(d>0\). The attenuation \(1/(1+r^2)\) is a **dimensionless relative Cauchy-shaped recruitment response**, not a claim about an unbounded-dimensional normalized dispersal density. Intensity \(\lambda>0\); one **shared** exponential environmental multiplier \(Z\) affects both habitats, while conditional counts are independent. Establishment means at least one arrival, with no mate limitation, competition, or downstream survival model.

## Proof
Let \(u=1+(x-d)^2\), \(v=1+(x+d)^2\). By exponential Laplace transforms and conditional independence,
\[
J(x)=1-\frac{u}{u+\lambda}-\frac{v}{v+\lambda}
+\frac{uv}{uv+\lambda(u+v)}
=\frac{\lambda^2[\lambda(u+v)+2uv]}
{(u+\lambda)(v+\lambda)[uv+\lambda(u+v)]}.
\]
Set \(z=x^2\ge0\), \(q=d^2\), \(p(z)=(1+q+z)^2-4qz\), \(s(z)=2(1+q+z)\), \(w(z)=p(z)+\lambda s(z)\). Then
\[
J(z)=\frac{\lambda^2[w(z)+p(z)]}{w(z)[w(z)+\lambda^2]}.
\]
All denominator factors are strictly positive. Differentiation gives
\[
\frac{dJ}{dz}=\frac{\lambda^2H(z)}{w(z)^2[w(z)+\lambda^2]^2},\quad
H=(w'+p')w(w+\lambda^2)-(w+p)w'(2w+\lambda^2).
\]
A direct polynomial identity yields
\[
H(0)=2(q+1)(\lambda+q+1)B(q,\lambda),
\]
\[
H'(0)=-4(q+1)(\lambda+q+1)C(q,\lambda),\quad
C=3\lambda^2+(9-7q)\lambda+5q^2-6q+5.
\]
For \(q\le1\), each term of the displayed expression for \(B\) is nonpositive and the intensity terms are strictly negative: hence \(H(0)<0\). For \(q>1\), \(B(q,0)>0\) and \(\partial_\lambda B=-(q+1)(q+5)-2\lambda(7q+3)<0\); hence exactly one positive zero \(\lambda_c(q)\), given by the stable quadratic-root expression above. Since \(z=x^2\), the sign of \(H(0)\) establishes strict local minima or maxima in \(x\) away from equality.

At the equality \(\lambda=\lambda_c(q)\), the quadratic \(C(q,\lambda)\) is strictly positive for \(q>1\): its discriminant in \(\lambda\) is \(21-54q-11q^2<0\) and its leading coefficient is positive. Thus \(H'(0)<0\), so \(J(x)-J(0)=-c x^4+O(x^6)\) for some \(c>0\), proving the stated degenerate strict local maximum. For \(\lambda<\lambda_c(q)\), \(J\) is even, continuous, positive at the midpoint and tends to zero at both infinities. The midpoint is strictly locally inferior to nearby points, so compactness gives at least one nonzero global maximizer and, by evenness, its distinct reflected counterpart.

The independent-environment comparison uses independent \(Z_+\) and \(Z_-\) rather than shared \(Z\); then \(J_{\mathrm{ind}}(x)=\lambda^2/[(1+\lambda+(x-d)^2)(1+\lambda+(x+d)^2)]\). Completing the square in \(x^2\) shows the midpoint ceases to be optimal exactly when \(q>1+\lambda\), so its exact transition is \(\lambda_{\mathrm{ind}}=q-1\). Substituting \(\lambda=q-1\) into \(B\) gives \(-2q(q-1)(3q-1)<0\), proving \(\lambda_c(q)<q-1\). Finally, substitute \(q=1+\varepsilon\), \(\lambda=\alpha\varepsilon\) into \(B=0\) to obtain \(8-12\alpha=0\) to leading order; substitute \(\lambda=\alpha q\) and divide by \(q^3\) for \(2-\alpha-7\alpha^2=0\). This proves both asymptotics.

## Verification
Run the included standard-library script `check.py` using `python3 check.py`. It verifies the exact rational response against inclusion-exclusion, polynomial derivative identities, critical threshold, quartic sign, and multiple near-threshold noncentral improvements over finite parameter tests. These diagnostics do not replace the algebraic proof or establish global uniqueness of any maximizer.

## Relationship to prior work
Clark et al. (1999) study alternative distance-dispersal kernels including fat tails; Greene et al. (2004) discuss alternative tree dispersal functions; Lindén and Mäntyniemi (2011) develop negative-binomial ecological counts; Seri et al. (2012) use Cauchy dispersal in forest clustering. They motivate the separate model ingredients, but their inspected text does not establish this specific common-environment local stability threshold. The independent-environment product-of-Cauchy transition is related to the classical modality of Cauchy products and **is not asserted to be new**; the claimed distinction is the nonfactorizing common-environment objective and its different threshold. A complete priority search remains open.

## Limitations
This is a local-stability classification of the midpoint, **not** a complete global optimizer classification above or at the threshold. Below threshold existence (not uniqueness) of off-centre global maximizers is proved. It assumes point habitats, identical Cauchy-shaped attenuation, exact Poisson conditional count laws and one exponential shared multiplier. It does not estimate dispersal, establishment or correlated weather parameters from field data. The local stability and the global consequences are for a one-dimensional feasible source transect; they must not be extrapolated to unconstrained planar siting.

## References
- Clark, J. S., et al. (1999). *Seed Dispersal Near and Far: Patterns Across Temperate and Tropical Forests*. Ecology. DOI: 10.1890/0012-9658(1999)080[1475:SDNAFP]2.0.CO;2. https://research.fs.usda.gov/download/treesearch/2094.pdf
- Greene, D. F., et al. (2004). *An evaluation of alternative dispersal functions for trees*. Journal of Ecology. DOI: 10.1111/j.0022-0477.2004.00921.x. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.0022-0477.2004.00921.x
- Lindén, A. and Mäntyniemi, S. (2011). *Using the negative binomial distribution to model overdispersion in ecological count data*. Ecology. DOI: 10.1890/10-1831.1. https://esajournals.onlinelibrary.wiley.com/doi/full/10.1890%2F10-1831.1
- Seri, E., Maruvka, Y. E., and Shnerb, N. M. (2012). *Neutral Dynamics and Cluster Statistics in a Tropical Forest*. American Naturalist. DOI: 10.1086/668125. https://www.journals.uchicago.edu/doi/full/10.1086/668125
