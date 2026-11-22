# A universal one-crossing law for variable retention in planar seed dispersal

## Finding
Consider an animal or other carrier moving by homogeneous isotropic planar diffusion until a positive random seed-retention time. Relative to retaining every seed for exactly the **same mean time**, arbitrary nondegenerate retention-time variability (not necessarily Gamma, bounded, or possessing an inverse moment) produces **exactly one positive radial-distance threshold**: the random-retention law has less mass beyond every shorter radius and more beyond every longer radius. Moreover, the signed difference between the two beyond-radius probabilities has exactly one strict negative minimum and one strict positive maximum. This is an exact result for radial cumulative probabilities, not a claim about the number of crossings of spatial densities.

Write the diffusion coefficient as \(\kappa>0\), the retention time as \(T\), its finite positive mean as \(m=\mathbb E T\), and the final radial displacement as \(R=|B_T|\), with independent standard planar Brownian motion scaled so that each coordinate of \(B_t\) has variance \(2\kappa t\). Define the matched-mean comparator \(R_0=|B_m|\). For \(s=r^2/(4\kappa)\) and \(r>0\),
\[
\Delta(s)=\Pr(R>r)-\Pr(R_0>r)=\mathbb E\exp(-s/T)-\exp(-s/m).
\]
For every nonconstant positive \(T\) of finite mean, unique numbers \(0<s_-<s_*<s_+<\infty\) exist such that \(\Delta(s)<0\) for \(0<s<s_*\), \(\Delta(s)>0\) for \(s>s_*\), and \(s_-\) and \(s_+\) are respectively the **only** positive stationary points, a strict global negative minimum and strict global positive maximum. Thus the physical crossover distance is \(r_*=\sqrt{4\kappa s_*}\).

When \(0<a\le T\le b<\infty\) almost surely and \(T\) is nonconstant, the strictly valid support bracket is
\[
2a<s_*<2b,\qquad \sqrt{8\kappa a}<r_*<\sqrt{8\kappa b}.
\]
For a weakly heterogeneous family \(T_\varepsilon=m+\varepsilon Z>0\), where \(Z\) is bounded, nonconstant and centered, and \(\varepsilon\downarrow0\), the *three* event-scale locations have distribution-independent limits:
\[
\frac{s_-(\varepsilon)}m\to2-\sqrt2,\qquad
\frac{s_*(\varepsilon)}m\to2,\qquad
\frac{s_+(\varepsilon)}m\to2+\sqrt2.
\]

## Assumptions and scope
The carrier starts at the origin of the entire plane; its position follows \(B_t=\sqrt{2\kappa}\,W_t\) for standard two-dimensional Brownian motion \(W\). Seed release occurs at a random time \(T\in(0,\infty)\), independent of the Brownian path, with \(0<\mathbb E T=m<\infty\) and \(\Pr(T=m)<1\). No density, variance, Gamma parametrization, lower retention bound or finite \(\mathbb E(T^{-1})\) is required. The comparison uses the deterministic duration \(m\), which matches mean squared displacement \(\mathbb E R^2=4\kappa m\). If support bounds or weak-heterogeneity limits are used, their additional assumptions are those stated above.

## Proof
**1. Exact radial tail.** Conditionally on \(T=t\), \(B_t\) is centered bivariate Gaussian with coordinate variance \(2\kappa t\). Hence \(|B_t|^2/(4\kappa t)\) has the unit exponential distribution, giving \(\Pr(R>r\mid T=t)=\exp[-r^2/(4\kappa t)]\). Average in \(T\); the same expression with \(t=m\) gives the comparator.

**2. Exactly one crossover without inverse-moment assumptions.** Put \(Y=m^{-1}-T^{-1}\), which is bounded above by \(m^{-1}\), and
\[
F(s)=\exp(s/m)\Delta(s)=\mathbb E\exp(sY)-1.
\]
For each \(s>0\), differentiation under the expectation is legitimate: the factors \(|Y|^k\exp(sY)\) are bounded for \(k=1,2\), because the negative tail is exponentially damped. Since \(T\) is nonconstant,
\[
F''(s)=\mathbb E[Y^2e^{sY}]>0.
\]
Further, \(F(0)=0\) and \(F'(0+)=m^{-1}-\mathbb E(T^{-1})<0\), including the value \(-\infty\) if the inverse moment diverges. The strict inequality is Jensen's inequality for \(t\mapsto t^{-1}\). A nonconstant finite-mean positive variable has positive probability above \(m+\delta\) for some \(\delta>0\); on that event \(Y>0\) is bounded below by a positive constant, so \(F(s)\to\infty\) as \(s\to\infty\). Strict convexity, the negative initial right slope and the positive divergence imply exactly one positive zero \(s_*\), negative before and positive after. Multiplying by \(\exp(-s/m)>0\) preserves these signs.

**3. Exactly two extrema.** Set
\[
J(s)=\mathbb E\big[T^{-1}e^{sY}\big]-m^{-1},\qquad
\Delta'(s)=-e^{-s/m}J(s).
\]
For every \(s>0\), the needed derivatives exist and
\[
J''(s)=\mathbb E\big[T^{-1}Y^2e^{sY}\big]>0.
\]
Strict Jensen gives \(J(0+)=\mathbb E(T^{-1})-m^{-1}>0\), with \(+\infty\) allowed. At the crossover, \(F(s_*)=0\) and strict convexity implies \(F'(s_*)>0\); therefore \(J(s_*)=-F'(s_*)<0\). Since \(\Pr(m+\delta<T<M)>0\) for suitable finite \(M\), the contribution of those durations implies \(J(s)\to\infty\) at large \(s\). Strict convexity of \(J\) gives exactly two positive zeros, one in \((0,s_*)\), one in \((s_*,\infty)\). Its sign is positive, negative, positive on the three resulting intervals. Consequently \(\Delta'\) has signs negative, positive, negative, proving the asserted unique strict global minimum and maximum; \(\Delta(s)\to0\) as \(s\to\infty\) by dominated convergence.

**4. Bound when retention times are bounded.** For fixed \(s>0\), put \(h_s(t)=\exp(-s/t)\). Direct differentiation gives
\[
h_s''(t)=\frac{s(s-2t)}{t^4}e^{-s/t}.
\]
At \(s\le2a\), this function is strictly concave on the nondegenerate support interval \([a,b]\) (apart from a possible endpoint equality), so strict Jensen yields \(\Delta(s)<0\). At \(s\ge2b\), strict convexity instead yields \(\Delta(s)>0\). The unique zero consequently obeys \(2a<s_*<2b\).

**5. Universal weak-heterogeneity limit.** For bounded centered nonconstant \(Z\) and \(T_\varepsilon=m+\varepsilon Z>0\), Taylor expansion uniformly over compact positive \(s\)-intervals, including one \(s\)-derivative, gives
\[
\Delta_\varepsilon(s)=\frac{\varepsilon^2\mathbb E Z^2}{2m^4}
 e^{-s/m}s(s-2m)+O(\varepsilon^3).
\]
The leading factor changes sign once at \(s=2m\), and its derivative has exactly two distinct positive zeros \(s=m(2\pm\sqrt2)\), since the dimensionless derivative is proportional to \(e^{-x}(-x^2+4x-2)\), \(x=s/m\). Uniform convergence and the already proved unique root and unique pair of extrema force the three stated limits.

## Verification
Run `python3 check_single_crossing.py` using only the Python standard library. The checker tests strict support bracketing, the one-crossover and two-extrema sign patterns across a seeded family of finite discrete retention laws, a near-zero retention component, the explicit two-duration example, and the weak-variation limits. It passes 6,800 diagnostic assertions. These finite diagnostics do not certify the infinite-law statements, which follow from the proof.

For an exact illustrating case, choose \(T=m/2\) or \(T=3m/2\), each with probability \(1/2\). Substituting into the crossover equation and writing \(z=\exp[s/(3m)]\) produces \((z-1)(z^3-z^2-z-1)=0\). The unique positive nontrivial solution is \(s_*=3m\log\tau\), where \(\tau\approx1.839286755214161\) solves \(\tau^3-\tau^2-\tau-1=0\). Thus \(s_*/m\approx1.828133590308019\).

## Relationship to prior work
Cousens et al. (2010) review animal seed-dispersal models combining movement and variable release time, motivating the observable radial probability comparison. Guttal et al. (2011) derive diffusion-plus-retention kernels and examine Gamma-retention variability, including a numerically investigated critical distance for **spatial kernel density** and a study of absolute long-distance dispersal. The present claim deliberately does not reassert that variability can enhance distant seed deposition. Its distinct content is the **arbitrary positive stopping-time distribution** theorem for the *radial cumulative tail*, with exact uniqueness of its single crossover, exact two-extrema morphology, support bounds and weak-heterogeneity constants. Gordillo and Greenwood (2025) analyze radial densities and heavy tails in randomized settling and diffusion models without the fixed-mean radial-tail one-crossing and extrema classification in their full text.

Related indexed Brownian first-passage results give one-crossing comparisons for hitting-time probabilities under variable diffusivity, which is not the law of the endpoint radius at an independent stopping time. Earlier local diffusion-source observation designs and wind-driven seed deposition results concern different optimization variables and do not imply the present mixture-tail ordering. The main 2011 article was read; its separately hosted supplementary Text S9 was not independently accessible, leaving a residual priority risk regarding its detailed numerical tail calculations.

## Limitations
The theorem assumes planar Gaussian motion, independence of stopping and movement, no drift or habitat boundaries, and a matched *mean* retention duration. It is not a classification for arbitrary non-Brownian paths, first-passage absorption, spatial kernel densities, or retention correlated with behavior. The location of the crossover generally depends on the full retention distribution, not just its variance. Weak-variability asymptotics assume bounded centered perturbations. The theorem is a mathematical benchmark, not an empirical predictor of any species' real dispersal range. The literature comparison supports a provisional originality assessment, not a claim of exhaustive historical priority.

## References
1. Cousens, R. D., Hill, J., French, K., and Bishop, I. D. (2010). *Towards better prediction of seed dispersal by animals*. Functional Ecology 24, 1163–1170. First published 2010-11-24. https://doi.org/10.1111/j.1365-2435.2010.01747.x
2. Guttal, V., Bartumeus, F., Hartvigsen, G., and Nevai, A. L. (2011). *Retention Time Variability as a Mechanism for Animal Mediated Long-Distance Dispersal*. PLOS ONE 6, e28447. First published 2011-12-14. https://doi.org/10.1371/journal.pone.0028447 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3237446/
3. Gordillo, L. F., and Greenwood, P. E. (2025). *Parameter variability can produce heavy tails in a model for the spatial distribution of settling organisms*. arXiv:2509.16385, first posted 2025-09-19. https://arxiv.org/abs/2509.16385
