# Sharp reversal ceiling for staged logistic wildfire severity under competing fuel treatments

## Finding

Consider two fuel treatments, each represented by a chain of \(n\ge 1\) necessary stages of a severe-fire event. Suppose the conditional probability of stage \(i\) succeeding, given the success of earlier stages under treatment \(A\), is \(\sigma(\beta w-\theta_{A,i})\), where \(\sigma(z)=1/(1+e^{-z})\), weather index \(w\in\mathbb R\), common slope \(\beta>0\), and \(\theta_{A,i}\in\mathbb R\). The analogous definition holds for treatment \(B\), with the *same* number of stages and slope but freely differing thresholds. No independence across stages is assumed beyond these conditional probabilities.

**Theorem.** Unless the risks are identical at every weather index, the two severe-event probabilities are equal at **at most \(n-1\) different finite weather indices**, and hence can reverse their risk ranking at most \(n-1\) times. The bound is sharp in a stronger prescribed-location sense: for every \(n\ge2\), every \(\beta>0\), and every \(n-1\) distinct finite weather indices, there are positive finite stage-odds parameters for the two treatments such that their risk curves cross **simply at exactly those indices**, with a strict ranking change at each.

At three stages, define \(a_i=e^{\theta_{A,i}}>0\), \(b_i=e^{\theta_{B,i}}>0\), and \(e_j(a),e_j(b)\) as elementary symmetric polynomials. Writing \(u=e_1(a)-e_1(b)\), \(v=e_2(a)-e_2(b)\), and \(z=e_3(a)-e_3(b)\), two simple positive-weather-odds crossings occur **if and only if**
\[
uz>0,\qquad uv<0,\qquad v^2>4uz.
\]
The corresponding odds values are the two positive solutions to \(ut^2+vt+z=0\) and the weather indices are their logarithms divided by \(\beta\). Here a *crossing* means a simple zero of the risk difference, so a tangential tie does not count as a reversal.

**Exact three-stage example.** Take \(\beta=1\), \(b=(1,2,3)\), and let the three positive values of \(a\) be the negatives of the three distinct negative roots of
\[
Q_A(t)=t^3+\frac{301}{50}t^2+\frac{547}{50}t+\frac{151}{25}.
\]
These roots lie respectively in \((-16/5,-3)\), \((-2,-7/4)\), and \((-6/5,-1)\). Then
\[
Q_A(t)-Q_B(t)=\frac{(t-1)(t-2)}{50},\qquad Q_B(t)=(t+1)(t+2)(t+3).
\]
Consequently treatment \(A\) has lower modeled severe-event risk for weather \(w<0\) and for \(w>\log 2\), but strictly *higher* risk for \(0<w<\log 2\). The risks are equal only at \(w=0\) and \(w=\log2\). Both treatment-specific risk curves nevertheless increase strictly with weather.

## Assumptions and scope

The stages are abstract conditional requirements for a severe outcome; they are not fitted physical submodels in the cited wildfire studies. Every chain has exactly \(n\) stages, common positive weather slope \(\beta\), unrestricted real stage thresholds, and the same scalar weather covariate. Fuel treatments may change every threshold. All probabilities are conditional on the modeled exposure scenario; the comparison is not an assertion about particular observed fire incidents. The stated upper bound concerns distinct finite ties or sign reversals of exact risk curves, not finite-sample estimates.

## Proof

Set \(t=e^{\beta w}>0\). The chain rule for conditional probabilities, which does not require independent stages, gives
\[
R_A(w)=\prod_{i=1}^n\frac{t}{t+a_i}=\frac{t^n}{Q_A(t)},\qquad Q_A(t)=\prod_{i=1}^n(t+a_i),
\]
and the corresponding formula for \(B\). Both denominators are strictly positive for \(t>0\). Therefore
\[
R_A-R_B=\frac{t^n\bigl(Q_B(t)-Q_A(t)\bigr)}{Q_A(t)Q_B(t)}.
\]
The two polynomials \(Q_A,Q_B\) are monic of degree \(n\), so their difference is either zero identically or has degree at most \(n-1\). In the first case the multisets \(\{a_i\}\) and \(\{b_i\}\) are equal by uniqueness of polynomial roots; in the second case the difference has at most \(n-1\) distinct positive roots, and hence at most that many sign changes. The map \(w\mapsto t\) is strictly increasing and bijective from \(\mathbb R\) onto \((0,\infty)\).

For sharpness, choose any distinct prescribed positive roots \(r_1,\ldots,r_{n-1}\), and any distinct positive values \(b_1,\ldots,b_n\). Let \(Q_B(t)=\prod_i(t+b_i)\) and
\[
Q_A(t)=Q_B(t)+\varepsilon\prod_{j=1}^{n-1}(t-r_j).
\]
All roots of \(Q_B\) are negative and simple. By the intermediate value theorem on disjoint small neighborhoods of those negative roots (or continuous dependence of simple real polynomial roots), for every sufficiently small nonzero real \(\varepsilon\), the perturbed monic polynomial \(Q_A\) still has \(n\) distinct real negative roots. Their negatives define admissible positive \(a_i\). Then \(Q_A-Q_B\) vanishes **only** at the prescribed \(r_j\), where each root is simple, and its sign alternates between consecutive roots. Taking \(r_j=e^{\beta w_j}\) realizes any prescribed distinct weather indices \(w_j\).

For \(n=3\), subtraction yields precisely \(ut^2+vt+z\). A real quadratic has two distinct positive roots if and only if its leading and constant coefficients have the same nonzero sign, its middle coefficient has the opposite sign to the leading coefficient, and its discriminant is strictly positive. These are the displayed three inequalities. If the leading coefficient vanishes, no two distinct roots are possible.

For the example, evaluate \(Q_A\) at consecutive pairs: \(Q_A(-16/5)=-57/625<0<Q_A(-3)=2/5\), \(Q_A(-2)=6/25>0>Q_A(-7/4)=-9/320\), and \(Q_A(-6/5)=-92/625<0<Q_A(-1)=3/25\). Thus the three distinct disjoint intervals contain three negative roots, exhausting this cubic's roots. The displayed exact polynomial subtraction gives crossings at \(t=1,2\), and the sign follows from the denominator identity. Finally \(\frac{d}{dw}\log R_A=\beta\sum_i a_i/(t+a_i)>0\), and similarly for \(B\), establishing individual monotonicity even though the ranking reverses twice.

## Verification

The included `checker.py` uses exact rational arithmetic to verify the witness polynomials, all six signed root-bracket evaluations, both crossover points, and three risk differences: at weather odds \(t=1/2\) the difference is \(-1/91980\), at \(t=3/2\) it is \(3/275590\), and at \(t=3\) it is \(-9/120040\). It also runs 30,000 supplementary exact rational comparisons in one through eight stages and checks two-stage crossing algebra. Run `python3 checker.py` with a standard Python 3 installation; no external packages or datasets are required. Finite checks support, but do not substitute for, the universal proof above.

## Relationship to prior work

Brodie and collaborators (2024) empirically compare fuel treatments and weather-dependent wildfire severity, motivating comparisons across weather without establishing this conditional-stage theorem. Perrakis and collaborators (2023) fit logistic crown-fire occurrence models; their published models do not claim identical stage slopes or prove the exact crossing count. The heterogeneous proportional-odds reliability literature, notably Panja, Kundu and Pradhan (2020/2021), compares parallel and series system laws under parameter-majorization and generator assumptions. The product of independent logistic CDFs is algebraically equivalent to this conditional-chain product, but those inspected stochastic-order results do not give the prescribed \(n-1\)-crossing attainability or the three-stage exact criterion. These are mathematical comparisons on the explicit model; not a claim that the underlying logistic distribution, polynomial-root bound or majorization techniques are themselves new.

## Limitations

The theorem assumes a common log-odds weather slope across *all* stages and treatments; varying slopes, interactions, threshold drift, competing failure pathways, or an unequal number of stages can invalidate the ceiling. The construction is a mathematical witness, not a fire-management recommendation. It establishes neither ecological fit nor empirical parameter identifiability, and it provides no uncertainty or robustness guarantee for noisy estimated crossovers. The accessible literature comparison does not establish comprehensive historical priority; one relevant earlier maximum-order-statistic paper was accessible only by abstract.

## References

1. Brodie, E. G., Knapp, E. E., Brooks, W. R., Drury, S. A., and Ritchie, M. W. (2024), *Forest thinning and prescribed burning treatments reduce wildfire severity and buffer the impacts of severe fire weather*, Fire Ecology 20, 17, published 2024-02-07. https://doi.org/10.1186/s42408-023-00241-z
2. Perrakis, D. D. B., Cruz, M. G., Alexander, M. E., and collaborators (2023), *Improved logistic models of crown fire probability in Canadian conifer forests*, International Journal of Wildland Fire, publicly online 2023-08-25. https://doi.org/10.1071/WF23074
3. Panja, A., Kundu, D., and Pradhan, B. (2020 preprint, revised 2021), *Stochastic comparisons of lifetimes of series and parallel systems with dependent and heterogeneous components*, https://arxiv.org/abs/2002.04271
4. Hazra, N. K., et al. (2017), *On stochastic comparisons of maximum order statistics from the location-scale family of distributions*, Journal of Multivariate Analysis; abstract inspected, full text not obtained. https://doi.org/10.1016/j.jmva.2017.06.001
