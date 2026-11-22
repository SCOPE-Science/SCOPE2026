# A sharp three-crop chronology switch under lagged seed predation

## Finding

Three recurring annual seed crops can be arranged in two inequivalent orientations. In the explicitly defined lagged-predator model below, the orientation producing less cumulative seed predation is rigid for a Holling-II intake law but reverses exactly once, at a sharp crop-dependent half-saturation threshold, for a Holling-III law.

Let \(A>B>C>0\), let the calendar repeat the three annual seed crops \((A,B,C)\) or \((A,C,B)\), and let predator abundance at the beginning of year \(t\) obey
\[
P_{t+1}=\rho P_t+b+\eta S_t,\qquad 0\le\rho<1,\quad b\ge0,\quad\eta>0.
\]
Take the unique periodic predator state and define its three-year predation total as \(H=\sum_{t=0}^{2}P_tg(S_t)\). For either of the two per-predator functional responses
\[
g_2(s)=\frac{s}{K+s},\qquad g_3(s)=\frac{s^2}{K^2+s^2},\qquad K>0,
\]
write \(\Delta_j=H_j(A,B,C)-H_j(A,C,B)\). Then
\[
\Delta_2=\frac{\eta K(A-B)(A-C)(B-C)}{(1+\rho+\rho^2)(K+A)(K+B)(K+C)}>0,
\]
whereas
\[
\Delta_3=\frac{\eta K^2(A-B)(A-C)(B-C)(AB+AC+BC-K^2)}{(1+\rho+\rho^2)(K^2+A^2)(K^2+B^2)(K^2+C^2)}.
\]
Consequently, the Holling-III ranking reverses exactly once as \(K\) increases through
\[
K_*=\sqrt{AB+AC+BC}.
\]
It favors \((A,C,B)\) for lower predation when \(0<K<K_*\), ties at \(K=K_*\), and favors \((A,B,C)\) for lower predation when \(K>K_*\). The background predator input \(b\) and interannual predator carryover \(\rho\) do not affect the ranking. The Holling-II ranking always favors \((A,C,B)\) for lower predation. These are comparisons of *cumulative predation proxies*, not claims about plant evolutionary fitness or a fitted field system.

The three-year horizon is minimal: reversing a one-year or two-year repeated calendar only shifts its phase, so its total periodic predation is identical. For three pairwise distinct positive crop levels the two orientations are not related by a phase shift and the strict rankings above apply.

## Assumptions and scope

The crops are prescribed exogenously and recur indefinitely in a deterministic period-three sequence; they do not respond to predation. Predator retention is nonnegative and strictly less than one, additive recruitment is proportional to the previous year's crop, and the positive intake function is evaluated at the current year's crop. This is a deliberately transparent linear numerical-response approximation, not the nonlinear Nicholson–Bailey dynamics of specialist seed predators and not a demographic density-feedback model. One year represents one recurrence step. The sign results compare two periodic steady regimes, not arbitrary finite-duration transients.

The dimensionless functional responses are saturating *per-predator loss proxies*; an overall consumption-rate multiplier can be absorbed into predator abundance units. Physical seed escape is \(\sum_t S_t-H\) only in parameter regimes where yearly consumption remains between zero and available seed. Such regimes exist for both signs and are exhibited below. The positive parameter \(K\) uses the same crop units as \(S_t\); \(\eta\) and \(b\) have abundance-per-crop and abundance units respectively.

The data and proof do not assume \(b>0\): the positive crops and \(\eta>0\) suffice for a positive periodic predator stock even when \(b=0\). If \(A\), \(B\), \(C\) coincide, orientation invariance is immediate; the strict claim assumes \(A>B>C\). The endpoint \(\rho=1\), where a bounded positive periodic predator cycle need not exist, is excluded.

## Proof

**1. Existence and uniqueness of the predator cycle.** For any three-periodic \(S_t\), three consecutive iterations of the affine recurrence have contraction factor \(\rho^3<1\), so there is a unique globally attracting three-periodic solution. Direct substitution gives
\[
P_t=\frac{b}{1-\rho}+\frac{\eta}{1-\rho^3}
\bigl(S_{t-1}+\rho S_{t-2}+\rho^2 S_t\bigr),
\]
where crop indices are read modulo three. Every term is nonnegative, and the crop-driven term is strictly positive.

**2. Cancellation of orientation-invariant terms.** Define
\[
U=A g(B)+B g(C)+C g(A),\qquad
V=A g(C)+C g(B)+B g(A).
\]
For the sequence \((A,B,C)\), the sum \(\sum_t S_{t-1}g(S_t)\) equals \(U\), while \(\sum_t S_{t-2}g(S_t)\) equals \(V\). For the reversed sequence \((A,C,B)\), they exchange. The sums \(\sum_t g(S_t)\) and \(\sum_t S_tg(S_t)\) are invariant under reordering. Consequently the difference in cumulative predator losses is exactly
\[
H(A,B,C)-H(A,C,B)
=\frac{\eta(1-\rho)}{1-\rho^3}(U-V)
=\frac{\eta}{1+\rho+\rho^2}(U-V).
\]
This derivation also establishes independence from the background recruitment \(b\) and the ranking's independence from the retention parameter \(\rho\).

**3. General three-point curvature identity.** Let \(g[A,B,C]\) be the second divided difference, equal when the crops are distinct to
\[
\frac{g(A)}{(A-B)(A-C)}
+\frac{g(B)}{(B-A)(B-C)}
+\frac{g(C)}{(C-A)(C-B)}.
\]
A common-denominator expansion establishes
\[
U-V=-(A-B)(A-C)(B-C)\,g[A,B,C].
\]
For \(A>B>C\), the sign of the orientation difference is opposite to the sign of the second divided difference. It is therefore controlled by a finite three-crop curvature comparison, not merely by the response's second derivative at the mean crop.

**4. Holling-II evaluation.** Substituting \(g_2(s)=s/(K+s)\), or writing it as \(1-K/(K+s)\), yields
\[
U-V=\frac{K(A-B)(A-C)(B-C)}{(K+A)(K+B)(K+C)}>0.
\]
Multiplying by the strictly positive factor found in step 2 proves the first formula and its strict sign.

**5. Holling-III evaluation and unique switch.** Direct reduction of the three-point divided difference for \(g_3(s)=s^2/(K^2+s^2)\) yields
\[
U-V=\frac{K^2(A-B)(A-C)(B-C)(AB+AC+BC-K^2)}{(K^2+A^2)(K^2+B^2)(K^2+C^2)}.
\]
Every factor outside the final parenthesis is strictly positive. Since \(AB+AC+BC>0\), the parenthesis is strictly positive for \(0<K<K_*\), zero at \(K_*\), and strictly negative for \(K>K_*\). This gives a single crossing, all equality cases, and the stated ranking. No numerical root search or finite enumeration is needed for this conclusion.

**6. Sharpness of three seasons.** A one-year calendar has only one orientation. Every reversal of a two-year calendar \((A,B)\) is the one-year phase shift \((B,A)\). The unique periodic predator orbit and its cycle sum shift with it, so the two totals are equal. Three pairwise distinct crops have two inequivalent cyclic orientation classes, and the explicit strict signs in steps 4–5 separate them. Thus the minimal period assertion is sharp.

## Verification

The standalone script `check.py` uses exact rational arithmetic to reconstruct the periodic predator cycle directly, evaluate both calendars independently, and compare their difference against the two factored formulas. It reports 6,066 passed assertions, including 6,000 randomized exact-rational comparisons for positive (not necessarily ordered) crop triples, variable background input and retention, plus structured rational examples and period-two phase checks. This finite test suite supplements, but does not replace, the six analytic proof steps above.

For a physically admissible example take \((A,B,C)=(3,2,1)\), \(\rho=1/2\), \(b=0\) and \(\eta=1/20\). All yearly predation quantities are smaller than the corresponding available seed crop, for both calendar orientations and for \(K=2,4\). The sharp threshold is \(K_*=\sqrt{11}\). Exact evaluation gives
\[
\Delta_3(K=2)=\frac1{325}>0,
\qquad
\Delta_3(K=4)=-\frac8{14875}<0.
\]
Thus the seed-escape-favoring orientation changes from \((A,C,B)\) to \((A,B,C)\) as \(K\) passes the threshold. Direct stationary predator abundances for \((3,2,1)\) are \((11/70,8/35,3/14)\); for \((3,1,2)\) they are \((13/70,17/70,6/35)\). These fractions permit independent hand recomputation of both displayed differences.

Reproduce with Python 3 using `python check.py` in the directory containing this result. The checker is self-contained and requires only the standard library.

## Relationship to prior work

Satake and Bjørnstad (2004) provide a spatial resource–consumer explanation for masting and seed-predator persistence, with a nonlinear Nicholson–Bailey predator process and a lagged-seed correlation mechanism. Their author-posted text was inspected through the model, predator-dynamics and results sections. That analysis does not state the three-fixed-crop, type-II/type-III orientation distinction or the exact \(\sqrt{AB+AC+BC}\) threshold derived here.

Fletcher et al. (2010) explicitly distinguish type-II and type-III seed-predator functional responses using observations of hoarding red squirrels. Their methods, empirical results and discussion concern the response curve and predator satiation, not an exact time-reversal comparison of prescribed three-year crop calendars under linear predator memory. Tachiki and Iwasa (2010) analyze the evolution of masting with seedling banks and specialist predators, using different demographic dynamics and evolutionary outcomes. Linhart et al. (2014) report empirical responses of seed predators to cone availability. Zwolak et al. (2021) consider masting and scatter-hoarding evolution in a different demographic model; that later work is used as context only.

The standard three-point divided-difference identity is classical mathematics and is not claimed as new. Previous related calendar-orientation results for reciprocal-density Beverton–Holt models, seasonal population projections and prey-management scheduling are also not claimed here. The claim is specifically the complete comparative law for a periodically forced *lagged seed-predator stock* under the two stated per-capita intake curves, including the single exact half-saturation crossing and its independence from predator carryover.

## Limitations

This is a self-contained theoretical result, without a field calibration, spatial dispersal, stochasticity, nonlinear predator recruitment or mechanistic plant fitness. Predator consumption is modeled as a proxy linear in predator abundance, rather than a constrained coupled seed-budget update; only the supplied example explicitly verifies that consumption does not exceed the yearly crop. The exact uniqueness result holds only for the stated three-crop periodic stationary model and response shapes. It does not establish a universal direction of evolutionary selection on crop order or distinguish models from real data.

The literature comparison includes author-posted and openly accessible research text and available summaries, not an exhaustive human priority review. In particular, exact priority cannot be certified against inaccessible or unindexed work on periodically lagged predator models, nor against full text of every related mathematical calendar-order result.

## References

1. Satake, A. and Bjørnstad, O. N. (2004). *Spatial Dynamics of Specialist Seed Predators on Synchronized and Intermittent Seed Production of Host Plants.* American Naturalist 163, 591–605. Electronically published 2004-04-19. https://doi.org/10.1086/382661
2. Fletcher, Q. E., Boutin, S., Lane, J. E., LaMontagne, J. M., McAdam, A. G., Krebs, C. J. and Humphries, M. M. (2010). *The functional response of a hoarding seed predator to mast seeding.* Ecology 91, 2673–2683. https://doi.org/10.1890/09-1816.1
3. Tachiki, Y. and Iwasa, Y. (2010). *Both seedling banks and specialist seed predators promote the evolution of synchronized and intermittent reproduction (masting) in trees.* Journal of Ecology 98, 1398–1408. https://doi.org/10.1111/j.1365-2745.2010.01729.x
4. Linhart, Y. B. et al. (2014). *Variability in seed cone production and functional response of seed predators to seed cone availability: support for the predator satiation hypothesis.* Journal of Ecology. https://doi.org/10.1111/1365-2745.12231
5. Zwolak, R., Clement, D., Sih, A. and Schreiber, S. J. (2021). *Mast seeding promotes evolution of scatter-hoarding.* Philosophical Transactions of the Royal Society B 376, 20200375. https://doi.org/10.1098/rstb.2020.0375
