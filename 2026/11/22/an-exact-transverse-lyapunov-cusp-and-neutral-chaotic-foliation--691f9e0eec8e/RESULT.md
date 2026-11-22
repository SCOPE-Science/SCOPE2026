# An exact transverse Lyapunov cusp and neutral chaotic foliation in a three-species Lotka–Volterra map

## Finding

Consider the cyclic three-species quadratic map of Muni (2024), restricted to its symmetric competition slice and maximal logistic growth:
\[
F_a(x_1,x_2,x_3)_i=x_i+3x_i\left(1-x_i-a\sum_{j\ne i}x_j\right),\qquad a>0,\quad i=1,2,3.
\]
Put \(S_a=1+2a\). Its positive diagonal segment \(L_a=\{(t,t,t):0\le t\le 4/(3S_a)\}\) supports an ergodic invariant probability \(\mu_a\), the image of the logistic-map arcsine law under \(u\mapsto(4u/(3S_a),4u/(3S_a),4u/(3S_a))\). For \(\mu_a\)-almost every orbit the three ambient Lyapunov exponents, with multiplicity, are
\[
\boxed{\left(\log2,\ \Lambda(a),\ \Lambda(a)\right)},\qquad
\Lambda(a)=\begin{cases}
\displaystyle\log\!\frac{2+a}{1+2a},&0<a<1,\\[5pt]
0,&a=1,\\[5pt]
\displaystyle 2\log\!\left(1+\sqrt{\frac{a-1}{1+2a}}\right),&a>1.
\end{cases}
\]
Thus both transverse exponents are strictly positive for **every** \(a>0\) except the single neutral value \(a=1\). Their zero has different orders on the two sides:
\[
\lim_{a\uparrow1}\frac{\Lambda(a)}{1-a}=\frac13,
\qquad
\lim_{a\downarrow1}\frac{\Lambda(a)}{\sqrt{a-1}}=\frac2{\sqrt3}.
\]
Here \(a\uparrow1\) is from below and \(a\downarrow1\) is from above.

The neutral parameter has a stronger exact property. Let
\[
\Delta=\left\{x_i\ge0:\ 0\le s=x_1+x_2+x_3\le\frac43\right\}.
\]
At \(a=1\) this **entire three-dimensional tetrahedron** is forward invariant, and, whenever \(s>0\), every species proportion \(p_i=x_i/s\) remains fixed until the exceptional orbit reaches the origin. For each composition \(p_i>0\), \(\sum_i p_i=1\), the ray \(x=(4u/3)p\) carries an ergodic invariant probability \(\mu_p\) conjugate to the logistic map \(u\mapsto4u(1-u)\), with Lyapunov spectrum \((\log2,0,0)\). These probabilities are pairwise distinct. For three-dimensional Lebesgue-almost every \(x\in\Delta\), the empirical probabilities converge to \(\mu_{p(x)}\). Therefore **there is no invariant probability with a basin of positive three-dimensional Lebesgue measure in \(\Delta\)** at \(a=1\). The claim concerns this tetrahedron and this normalization of Lebesgue measure, not all of \(\mathbb R^3\).

## Assumptions and scope

The parameter \(a\) is any positive real number and the growth parameter of the source map is set exactly to \(R=3\), with its two directed competition coefficients set equal to \(a\). The diagonal measure \(\mu_a\) is the pushforward of \(du/[\pi\sqrt{u(1-u)}]\) on \((0,1)\). Lyapunov exponents refer to the full ambient derivative cocycle, rather than only the one-dimensional restriction to the diagonal. They are almost-everywhere exponents relative to this explicitly specified invariant probability; this does not imply that \(\mu_a\) is a physical or attracting measure when \(a\ne1\). At \(a=1\), statements about typical initial data and absence of positive-volume physical basins are restricted to \(\Delta\). Boundary points, preimages of critical points, and degenerate zero-multiplier orbits may have different pointwise exponents and are not in the almost-everywhere assertion.

## Proof

**1. Invariant logistic diagonal.** On \(x_1=x_2=x_3=t\), the equation gives \(t'=4t-3S_at^2\). With \(u=3S_at/4\), this becomes \(u'=4u(1-u)\), mapping \([0,1]\) to itself. Under \(u=\sin^2(\pi\theta)\), the logistic map is a factor of the doubling map \(\theta\mapsto2\theta\pmod1\); consequently its arcsine law \(\nu(du)=du/[\pi\sqrt{u(1-u)}]\) is invariant and ergodic. Its image on \(L_a\) is \(\mu_a\).

**2. Constant spectral splitting.** At the diagonal point \((t,t,t)\), the Jacobian has diagonal entries \(4-3(2+2a)t\) and off-diagonal entries \(-3at\). Its fixed orthogonal splitting into the line spanned by \((1,1,1)\) and the two-dimensional zero-sum plane has scalar multipliers respectively
\[
A(u)=4(1-2u),\qquad B_a(u)=4(1-k_au),
\qquad k_a=\frac{2+a}{1+2a}.
\]
These subspaces are invariant at every iterate; the derivative matrices commute and the products on them are the products of these scalar multipliers. The logarithms are integrable for \(\nu\), including when a multiplier has isolated zeros, because their singularities are logarithmic. The ergodic theorem yields the three exponents from their \(\nu\)-integrals for almost every initial \(u\), excluding the null set eventually hitting an exact zero.

**3. Exact integrals.** The standard logarithmic cosine integral, verified directly by Jensen's formula or by factoring its trigonometric polynomial, is
\[
\frac1{2\pi}\int_0^{2\pi}\log|A+B\cos\theta|\,d\theta
=\begin{cases}
\log(|B|/2),& |A|\le|B|,\quad B\ne0,\\
\log\bigl((|A|+\sqrt{A^2-B^2})/2\bigr),& |A|>|B|.
\end{cases}
\]
Substituting \(u=(1-\cos\theta)/2\) gives
\[
\int\log|B_a(u)|\,d\nu(u)=\log4+
\frac1{2\pi}\int_0^{2\pi}
\log\left|1-\frac{k_a}{2}+\frac{k_a}{2}\cos\theta\right|d\theta.
\]
For \(a<1\), \(k_a>1\), so this equals \(\log k_a\). For \(a>1\), \(0<k_a<1\), so it equals
\(\log[2-k_a+2\sqrt{1-k_a}]=2\log(1+\sqrt{1-k_a})\).
At \(a=1\), the formulas meet at zero. The analogous integral of \(\log|A(u)|\), with \(k=2\), is \(\log2\). Finally \(k_a-1=(1-a)/(1+2a)\); Taylor expansion and \(1-k_a=(a-1)/(1+2a)\) give the two stated exact one-sided constants.

**4. Neutral foliation and lack of physical selection.** At \(a=1\) all three components share one factor:
\[
F_1(x)=(4-3s)x,
\qquad s=\sum_i x_i,
\qquad s'=4s-3s^2.
\]
For \(0\le s\le4/3\), the factor is nonnegative and \(0\le s'\le4/3\); hence \(\Delta\) is invariant. Whenever \(s'\ne0\), proportions are conserved. For fixed positive \(p\), writing \(x=(4u/3)p\) again gives the logistic map. The logistic arcsine law therefore yields a distinct ergodic measure \(\mu_p\) on every such ray. Its radial multiplier is \(4-8u\), and its two zero-sum transverse multipliers are \(4(1-u)\), giving \((\log2,0,0)\) by the integrals above.

Lebesgue-almost every \(x\in\Delta\) has positive components, a well-defined \(p\), and \(u=3s/4\) generic for the logistic arcsine measure: the latter is equivalent to Lebesgue measure on \((0,1)\), and the smooth change of variables between \((p_1,p_2,u)\) and interior \(x\) has nonzero Jacobian for \(u>0\). Thus the empirical measures of almost every such point converge weakly to \(\mu_p\). Because \(\int x_i\,d\mu_p=(2/3)p_i\), the map \(p\mapsto\mu_p\) is injective. For any fixed probability \(\eta\), the set of such typical \(x\) with empirical limit \(\eta\) lies in at most one composition ray, which has three-dimensional Lebesgue measure zero. The complement of the typical set is also null. Therefore no probability, invariant or otherwise, can have a positive-volume basin of empirical convergence inside \(\Delta\).

## Verification

The included standalone `verify.py` checks the exact reduced recurrence, Jacobian eigenmultipliers, their integral formulas via deterministic Chebyshev quadrature away from null-set singularities, the left and right asymptotic constants, and raywise conservation for the neutral parameter. It uses only the Python standard library. Execute `python3 verify.py` from the extracted package. The finite quadrature checks do not replace the analytic integral and ergodic proof.

## Relationship to prior work

Muni's 2024 article introduces precisely the cyclic three-dimensional polynomial map and studies quasiperiodic bifurcations, periodic orbits and numerical Lyapunov charts, particularly in asymmetric slices near \(R=1.4\). The present theorem selects the analytically distinguished maximal-logistic value \(R=3\) and the symmetric interaction line, and gives a complete **ambient** almost-everywhere Lyapunov formula with a unique neutral cusp and an exact continuum of chaotic invariant ray measures. Standard logistic ergodicity and Jensen's cosine integral are classical tools, not new assertions. Earlier three-dimensional Lotka–Volterra papers study bifurcations and chaos, and a related result treats the \(R=1\) Euler–May–Leonard critical simplex; its pointwise fixed face at symmetric interaction is distinct from the fully chaotic \(R=3\) foliation established here. The available prior information does not establish the present combined sharp spectrum and physical-basin exclusion; publication priority is not guaranteed.

## Limitations

The invariant diagonal is typically transversely unstable when \(a\ne1\); three positive exponents **for its invariant probability** do not prove the existence of a three-dimensional physical hyperchaotic attractor. The nonsmooth square-root parameter cusp is an exponent crossover, not a claim of a local bifurcation of attracting sets. The invariant-ray foliation and absence of a positive-volume physical basin are proved only at the exact critical competition \(a=1\), inside \(\Delta\). The full text of the 1987 Gardini et al. predecessor was not accessible; its abstract is relevant but insufficient to exclude every possible related theorem. Equivalent unindexed work and stronger inaccessible literature remain priority risks. Independent validation is not claimed.

## References

1. S. S. Muni, *Torus and hyperchaos in 3D Lotka–Volterra map*, arXiv:2408.15054v1, first public submission 2024-08-27, https://arxiv.org/html/2408.15054v1.
2. L. Gardini, R. Lupini, C. Mammana and M. G. Messia, *Bifurcations and Transitions to Chaos in the Three-Dimensional Lotka–Volterra Map*, SIAM J. Appl. Math. 47 (1987), 455–482, https://doi.org/10.1137/0147031 (abstract and publication metadata inspected; full text not read).
3. R. M. May, *Simple mathematical models with very complicated dynamics*, Nature 261 (1976), 459–467, https://doi.org/10.1038/261459a0 (logistic-map background).
