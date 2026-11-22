# A sharp module-count transition in fixed-budget Steele photoinhibition

## Finding

Consider \(n\geq2\) identical independent photosynthetic modules with nonnegative dimensionless irradiances \(x_1,\ldots,x_n\), constrained by \(\sum_{i=1}^n x_i=S>0\). Suppose each module has the Steele photoinhibited response \(f(x)=x\exp(-x)\). The aggregate response is \(F_n=\sum_{i=1}^n f(x_i)\).

**Theorem.** For two modules, the equal allocation uniquely maximizes \(F_2\) when \(0<S\leq4\). When \(S>4\), precisely two permutations of one unequal pair maximize it; the pair converges to equality as \(S\downarrow4\). For every \(n\geq3\) there is exactly one threshold \(S_c(n)\) strictly between \(n\) and \(2n\), such that equality uniquely maximizes \(F_n\) for \(S<S_c(n)\), equality and exactly \(n\) one-high allocations tie at \(S=S_c(n)\), and exactly those \(n\) unequal permutations maximize \(F_n\) for \(S>S_c(n)\). The unequal allocations contain \(n-1\) identical lower irradiances between \(1\) and \(2\), and one greater irradiance above \(2\). Their appearance at the global threshold is discontinuous for every \(n\geq3\). Thus **three modules are the sharp onset of a discontinuous optimum**.

Here are explicit one-dimensional definitions of every parameter; no multidimensional optimization remains. For \(d>0\), set
\[
u(d)=\frac{d}{e^d-1},\quad T_n(d)=n+d+n\nu(d),\quad a(d)=1+\nu(d),\quad b(d)=a(d)+d.
\]
For \(n\geq3\), let \(d_f(n)>0\) be the unique solution of \(1+n\nu'(d_f)=0\), and set \(S_f(n)=T_n(d_f)\). Define \(d_c(n)>d_f(n)\) as the unique solution on the increasing branch \(T_n(d)\in(S_f(n),2n)\) of
\[
(n-1)f(a(d))+f(b(d))=n f(T_n(d)/n).
\]
Then \(S_c(n)=T_n(d_c(n))\). For \(n\geq3\) and \(S>S_c(n)\), solve \(T_n(d)=S\) on \(d>d_f(n)\); the optimal vector is any permutation of \((a(d),\ldots,a(d),b(d))\). At equality use that vector and the balanced vector. For \(n=2\) and \(S>4\), the same formula applies with the unique \(d>0\) solving \(T_2(d)=S\).

For \(n=3\), numerical evaluation gives \(S_f\approx5.745643576733\), \(S_c\approx5.774313471725\), and a nonzero optimal jump \(d_c\approx1.397499519594\). At \(S=7\), the optimal allocation is approximately \((1.092139462245,1.092139462245,4.815721075509)\), attaining \(F_3\approx0.771835057925\), compared with the equal-allocation value \(0.678803775051\), an improvement of about \(13.7052\%\).

## Assumptions and scope

The modules are identical, their responses are additive and independent, and irradiance is freely divisible among them. The entire incoming dimensionless load \(S\) **must** be allocated: unused light cannot be dumped or reflected away. There are no other per-module irradiance caps, self-shading, mixing, photoacclimation, or dynamic controls. The result characterizes an idealized instantaneous response, not biomass production integrated over an experiment. Irradiance is scaled by the maximizing intensity of Steele's response; a positive common productivity factor cancels from the allocation problem. The theorem holds for every real \(S>0\) and every integer \(n\geq2\), including all threshold equalities and the boundary \(x_i=0\).

## Proof

**1. Boundary exclusion and stationary values.** The simplex is compact, so a maximizer exists. Since \(f'(0)=1\) and \(f'(y)=(1-y)e^{-y}<1\) for every \(y>0\), transferring a sufficiently small positive amount from any occupied module to a zero-irradiance module increases \(F_n\). Thus all maximizers are interior. At such a point, the Lagrange multiplier equation gives \(f'(x_i)=\lambda\) for all \(i\). The derivatives are
\[
f'(x)=(1-x)e^{-x},\quad f''(x)=(x-2)e^{-x},\quad f'''(x)=(3-x)e^{-x}.
\]
For \(\lambda\geq0\), \(f'\) is one-to-one over the only possible domain \(0<x\leq1\); therefore every coordinate is equal. For \(\lambda<0\), all coordinates exceed \(1\), and there are at most two possible values: \(a\in(1,2)\) and \(b>2\). Two coordinates equal to \(b\) are impossible at a local maximum: perturbing them by equal and opposite increments has strictly positive second derivative \(2f''(b)>0\). Hence every nonbalanced candidate maximizer consists of \(n-1\) copies of \(a\) and one copy of \(b\).

**2. Parametrization of all unequal candidates.** Set \(d=b-a>0\) and \(u=a-1>0\). The common-derivative relation \(u e^{-a}=(u+d)e^{-b}\) is equivalent to \(u=d/(e^d-1)\). Therefore \(a=a(d)\), \(b=b(d)\), and conservation is precisely \(S=T_n(d)\). Note that \(0<\nu(d)<1\) and that \(\nu(d)\) decreases from \(1\) to \(0\) as \(d\) increases. For \(d>0\),
\[
\nu''(d)=\frac{e^d\big((d-2)e^d+d+2\big)}{(e^d-1)^3}>0.
\]
For the numerator's bracket \(g(d)=(d-2)e^d+d+2\), we have \(g(0)=g'(0)=0\) and \(g''(d)=d e^d>0\), establishing strict positivity. Moreover \(\nu'(0+)=-1/2\) and \(\nu'(d)\to0\) as \(d\to\infty\). Hence \(T_2'(d)=1+2\nu'(d)>0\) for all \(d>0\), with \(T_2(0+)=4\). For every \(n\geq3\), \(T_n'\) increases strictly from \(1-n/2<0\) to \(1\), so it vanishes exactly at \(d_f>0\). The function \(T_n\) decreases from \(2n\) to \(S_f=T_n(d_f)\), then increases without bound. In particular \(n<S_f<2n\).

**3. Reject the lower branch and the fold.** Restrict to the subspace of candidate configurations by writing
\[
H_S(a)=(n-1)f(a)+f\big(S-(n-1)a\big).
\]
Its stationary condition is \(h(a,S)=f'(a)-f'(S-(n-1)a)=0\). At a nonbalanced stationary point parameterized by \(d\), differentiation of \(f'(a(d))=f'(b(d))\) gives \(f''(a)\nu'=f''(b)(1+\nu')\). Therefore
\[
H_S''(a)=(n-1)\big(f''(a)+(n-1)f''(b)\big)=(n-1)f''(b)\frac{T_n'(d)}{\nu'(d)}.
\]
Because \(f''(b)>0\) and \(\nu'<0\), this is positive on the decreasing \(T_n\)-branch, excluding it as a maximum, and negative on the increasing branch. At \(d=d_f\), it vanishes, but this stationary point is not a maximum either. In fact \(h_a=0\), \(h_S=-f''(b)\), and along the stationary family \(h(a(d),T_n(d))=0\). Differentiating twice at the fold \(T_n'(d_f)=0\) yields
\[
h_{aa}\big(\nu'(d_f)\big)^2=f''(b(d_f))T_n''(d_f)>0.
\]
Thus \(H_S'''=(n-1)h_{aa}>0\) at the fold, so this point is a stationary inflection, not a local maximum. The only possible maximizers are therefore the equal vector and an increasing-branch unequal vector (when it exists).

**4. The two-module case.** For \(n=2\), an unequal stationary point exists exactly when \(S>4\), and the unique positive \(d\) solving \(T_2(d)=S\) is on the strict-local-maximum branch. For \(S\leq4\) the equal allocation is the only possible maximizer; for \(S>4\), equality has \(f''(S/2)>0\), so it is a local minimum along the fixed-sum line and cannot maximize. Consequently only the two permutations of the unequal pair are global maximizers. Since \(T_2(d)\to4\) as \(d\downarrow0\), the unequal optimum merges continuously with equality at \(S=4\).

**5. The discontinuous global threshold for three or more modules.** Fix \(n\geq3\). At \(S=S_f\), the fold is not a local maximum and no other unequal stationary point exists; since a global maximizer exists and boundaries were excluded, the equal configuration is the sole maximizer. Hence the increasing-branch unequal candidate has a strictly smaller objective at the fold. At \(S=2n\), equality has \(f''(2)=0\) and \(f'''(2)=e^{-2}>0\); the fixed-sum perturbation proportional to \((n-1,-1,\ldots,-1)\) has zero quadratic term and positive cubic term proportional to \(n(n-1)(n-2)>0\). Thus equality is not a local maximum. The increasing-branch unequal candidate must have strictly greater value at \(S=2n\).

For \(S\in(S_f,2n)\), let \(d=d(S)>d_f\) solve \(T_n(d)=S\), and denote the unequal-minus-equal objective difference by \(G_n(S)\). The envelope derivative and the equality of derivatives at the two unequal irradiances give
\[
G_n'(S)=f'(a(d(S)))-f'(S/n)>0.
\]
Indeed, \(1<a(d)<S/n<2\) on this interval, and \(f'\) decreases strictly on \((1,2)\). Hence \(G_n\) rises strictly from a negative value at \(S_f\) to a positive one at \(2n\), and has exactly one zero \(S_c\) strictly in between. Below that zero the equal vector is the unique global maximizer, at the zero the equal and all \(n\) permutations of the distinct unequal vector tie, and above it the unequal permutations are the only maxima. For \(S>2n\), equality has \(f''(S/n)>0\) and is not a local maximum; the increasing-branch candidate remains the only possibility. At \(S=2n\) the cubic perturbation already excludes equality. The crossover occurs at \(d_c>d_f>0\), and hence has a nonzero finite jump for all \(n\geq3\).

**6. High-load limit.** Along the increasing branch \(S=T_n(d)\to\infty\) implies \(d\to\infty\) and \(\nu(d)\to0\). Thus \(n-1\) optimal module irradiances approach \(1\), the last approaches \(S-n+1\) up to an error vanishing at infinity, and \(F_n\to(n-1)/e\). The equal-allocation response \(n(S/n)e^{-S/n}\to0\). This limit depends critically on prohibiting disposal of excess incoming light.

## Verification

A bundled standard-library Python file, `verify.py`, evaluates the branch formulas by bisection, checks the defining equations and curvature for module counts \(2\leq n\leq35\), and samples deterministic random allocations on many fixed-budget simplexes, including around both thresholds. Its recorded execution passed **139,189 numerical assertions**; it also reconstructs the three-module threshold and illustrative values above. Those finite checks are corroboration and do not prove the global statements, which follow from Steps 1–6.

Run with `python verify.py` in the directory containing this file. All numbers are dimensionless and comparisons allow the floating-point tolerances explicitly present in the checker. No external data or Python dependencies are required.

## Relationship to prior work

Steele (1962) introduced a bell-shaped irradiance response incorporating photoinhibition; this theorem adopts its dimensionless functional form but addresses a different question, a fixed-sum division among any number of independent modules. Bonente and colleagues (2012) experimentally measured acclimation across low, control and high irradiances; their results motivate the relevance of unequal light efficiency but do not assert this static resource-partition theorem. The optical-depth optimization of Bernard and Lu (2021), inspected through its accessible full text, optimizes internal attenuation, biomass and depth within a single photobioreactor using a different growth function, not the fixed-sum irradiance allocation studied here. Other illumination-distribution optimization and generic separable resource-allocation results may be relevant to historical priority. No claim of absolute priority or applicability to realistic reactor control is made.

## Limitations

The response model is phenomenological and fixed in time. Photosynthetic acclimation, light/dark cycles, self-shading, maintenance respiration, unequal module areas, irradiance caps, and the option to reject excess illumination are not represented. In particular, allowing light to be discarded changes the high-load optimum and can invalidate the forced-allocation threshold as a design recommendation. The numerical verification samples only finitely many allocations. The self-review is not an independent proof review; literature coverage cannot establish historical uniqueness, particularly against general resource-allocation theorems.

## References

- J. H. Steele (1962). *Environmental control of photosynthesis in the sea*. Limnology and Oceanography 7(2), 137–150. https://doi.org/10.4319/lo.1962.7.2.0137 . The publisher verifies April 1962, without a precise public calendar day in the consulted record.
- G. Bonente et al. (2012). *Acclimation of Chlamydomonas reinhardtii to different growth irradiances*. Journal of Biological Chemistry 287(8), 5833–5847. https://doi.org/10.1074/jbc.M111.304279 . Electronically published 2011-12-28 per PubMed; the full open-access article was inspected.
- C. Brindley, F. G. Acién Fernández and J. M. Fernández-Sevilla (2011). *Analysis of light regime in continuous light distributions in photobioreactors*. Bioresource Technology 102, 3138–3148. https://doi.org/10.1016/j.biortech.2010.10.088 . Publisher abstract inspected; complete text not accessed.
- F. García-Camacho et al. (2012). *A mechanistic model of photosynthesis in microalgae including photoacclimation dynamics*. Journal of Theoretical Biology 304, 1–15. https://doi.org/10.1016/j.jtbi.2012.03.021 . Abstract and publication metadata inspected.
- O. Bernard and L.-D. Lu (2021). *Optimal optical conditions for microalgal production in photobioreactors*. https://arxiv.org/abs/2108.10009 . Open full text, including model and optimization section, inspected.
