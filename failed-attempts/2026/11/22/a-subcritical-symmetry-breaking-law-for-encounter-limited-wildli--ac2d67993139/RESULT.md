# A subcritical symmetry-breaking law for encounter-limited wildlife crossings

## Finding

**Theorem (crowding-limited passage allocation).** Fix an integer \(n\ge2\), a dimensionless encounter-load parameter \(c>0\), and fractions \(x_1,\ldots,x_n\ge0\) with \(\sum_{i=1}^{n}x_i=1\). A crossing attempted at passage \(i\) succeeds with probability \(e^{-cx_i}\). Define the total expected successful fraction
\[
F_{n,c}(x)=\sum_{i=1}^{n}x_i e^{-cx_i}.
\]
All global maximizers exist, have strictly positive components, and are either equal or, up to permutation, of the form \((s,\ldots,s,1-(n-1)s)\) with \(0<s<1/n\). The following sharp distinction holds.

1. For \(n=2\), the equal allocation is the unique global optimum exactly when \(0<c\le4\). For \(c>4\), the only global maximizers are the two permutations of \(((1-t_c)/2,(1+t_c)/2)\), with the unique \(t_c\in(0,1)\) satisfying
   \[
   (c-2)\tanh(ct_c/2)=ct_c.
   \]
   Thus symmetry breaking is continuous at \(c=4\).
2. For every \(n\ge3\), there exists \(\delta_n>0\) such that at every \(2n-\delta_n<c<2n\), the equal allocation remains a strict local maximizer but is **not** globally optimal. In particular, at \(n=3,c=59/10\), the allocation \((9/40,9/40,11/20)\) strictly beats \((1/3,1/3,1/3)\). Three passages are the sharp minimum for this coexistence of locally optimal balance with a better asymmetric allocation.
3. For every fixed \(n\ge2\), as \(c\to\infty\),
   \[
   c\max_{x}F_{n,c}(x)\longrightarrow\frac{n-1}{e}.
   \]
   In every family of global maximizers one component tends to \(1\), while each of the other \(n-1\) components satisfies \(cx_i\to1\). Hence strong encounter loads favor \(n-1\) lightly used passages and one heavily used, low-success passage rather than equal routing.

## Assumptions and scope

An arbitrary positive number of attempted crossings is allocated fractionally among \(n\) initially identical passages. At passage \(i\), the number of independent adverse encounters for one attempt is Poisson with mean \(cx_i\); survival means zero encounters. Thus the success probability is \(e^{-cx_i}\). The calculation concerns an externally imposed routing allocation of a fixed demand, not behavioral equilibrium. There are no baseline mortality differences, capacity costs, displacement feedbacks, or dependence between attempts that changes the stated marginal probability. The parameter \(c\) is dimensionless; its empirical magnitude is not estimated here. The result is about an idealized success fraction, not a prediction for particular structures or species.

## Proof

Let \(f_c(u)=ue^{-cu}\). Direct differentiation gives
\[
f'_c(u)=(1-cu)e^{-cu},\quad f''_c(u)=c(cu-2)e^{-cu},\quad f'''_c(u)=c^2(3-cu)e^{-cu}.
\]
The simplex is compact, so a global maximizer exists. Every maximizer is interior: if \(x_i=0\) and \(x_j>0\), transferring a sufficiently small amount from \(j\) to \(i\) changes the objective to first order by \(f'_c(0)-f'_c(x_j)=1-(1-cx_j)e^{-cx_j}>0\). At an interior maximizer, the first derivatives agree. The function \(f'_c\) decreases strictly below \(2/c\) and increases strictly above \(2/c\), so its level sets contain at most two points. Moreover, two coordinates strictly above \(2/c\) cannot coexist at a local maximum: transferring mass between them produces positive second variation \(f''_c(x_i)+f''_c(x_j)>0\). Thus all but at most one component equal a common smaller value, proving the structural classification. Strict concavity gives the equal allocation as the unique global maximum when \(c\le2\), an optional low-load boundary.

For \(n=2\), write \(x_1=(1-t)/2\), \(x_2=(1+t)/2\), \(0\le t\le1\). Then
\[
F_{2,c}=e^{-c/2}\{\cosh(ct/2)-t\sinh(ct/2)\}.
\]
For \(t>0\), the sign of its derivative is the sign of \((c-2)\tanh(ct/2)-ct\). Put \(z=ct/2\). The stationarity equation becomes \(c-2=2z\coth z\), and \(z\coth z\) strictly increases from \(1\) to infinity: its derivative has numerator \(\sinh z\cosh z-z>0\). At \(t=1\), \(2z\coth z>c>c-2\). For \(c\le4\) the derivative is negative for every \(t>0\), so balance uniquely wins; for \(c>4\) it changes from positive to negative exactly once, yielding the asserted reflected pair. As \(c\downarrow4\), the unique root tends to zero by continuity and strict monotonicity.

For general \(n\), the Hessian restricted to the tangent hyperplane \(\sum_i h_i=0\) at the equal point \(u=(1/n,\ldots,1/n)\) is \(f''_c(1/n)\sum_i h_i^2\). Hence \(u\) is a strict local maximum for \(c<2n\) and a strict local minimum for \(c>2n\). At \(c=2n\) set \(h=(n-1,-1,\ldots,-1)\). The first-order variation vanishes, the quadratic variation vanishes, but
\[
\sum_i h_i^3=(n-1)n(n-2)>0,\qquad f'''_{2n}(1/n)=(2n)^2e^{-2}>0.
\]
Consequently \(F_{n,2n}(u+\varepsilon h)>F_{n,2n}(u)\) for all sufficiently small positive \(\varepsilon\), provided \(n\ge3\). Fix one such feasible \(\varepsilon\). Continuity in \(c\) preserves this strict inequality throughout some interval immediately below \(2n\), while negative tangent Hessian makes \(u\) a strict local maximum there. Therefore that balanced local maximum is not global. The preceding two-passage classification proves the asserted minimality.

A completely rational strict certificate at \(n=3,c=59/10\) uses \(x=(9/40,9/40,11/20)\). Let \(P_m(y)=\sum_{j=0}^{m}(-y)^j/j!\). Taylor's integral remainder implies \(P_{27}(y)\le e^{-y}\le P_{26}(y)\) for every \(y\ge0\). Direct exact rational evaluation gives
\[
2\frac9{40}P_{27}\left(\frac{531}{400}\right)+\frac{11}{20}P_{27}\left(\frac{649}{200}\right)-P_{26}\left(\frac{59}{30}\right)>0.
\]
This strictly lower-bounds the advantage over the equal allocation. The included standalone checker evaluates this rational expression without floating-point assumptions. Numerical values of the two success fractions are approximately \(0.14074538713167\) and \(0.13992248802431\), respectively.

Finally, let \(y_i=cx_i\), so \(\sum_i y_i=c\) and \(cF=\sum_i y_ie^{-y_i}\). Since \(ye^{-y}\le1/e\) and some \(y_j\ge c/n\), for \(c\ge n\),
\[
 c\max F\le \frac{n-1}{e}+\frac cn e^{-c/n}.
\]
For \(c\ge n\), the feasible choice \(y_1=\cdots=y_{n-1}=1\), \(y_n=c-n+1\) yields \(cF\ge(n-1)/e+(c-n+1)e^{-(c-n+1)}\). The two bounds imply the stated limit. For any maximizing sequence, the largest \(y_i\) diverges and contributes zero. Every other term must tend to its individually maximal value \(1/e\); uniqueness of the maximizer of \(ye^{-y}\) forces \(y_i\to1\). This proves the optimizer profile without assuming uniqueness of the finite-\(c\) optimum.

## Verification

Reproduce with standard Python 3 using `python check_crossings.py`, which tests exact rational Taylor bounds, analytically derived derivatives and the two-passage stationarity equation, and supplementary numerical simplex comparisons. The rational inequality is a finite exact certificate. Randomized and grid comparisons are illustrations, not an exhaustive proof of global claims; the infinite and global statements are proved above. The checker requires no external packages.

## Relationship to prior work

Soanes and colleagues (2024) synthesize evidence on real wildlife crossings and emphasize that evidence of actual improvements in cross-road movement is limited. Mata, Herranz and Malo (2020) document predator–prey spatial and temporal associations at crossing structures, motivating density-dependent encounter hazards. Helldin (2022) discusses the tradeoff between concentrated and distributed crossing opportunities using ecological and policy arguments and cites Karlson, Seiler and Mörtberg (2017), whose theoretical GIS/circuit-model analysis concerns spatial connectivity rather than an exogenously allocated Poisson encounter load. Neither establishes the present continuous routing-optimization theorem in the inspected material. General nonconcave resource-allocation work (Andersson and Ygge, 2001) provides a broader algorithmic setting, especially for discrete allocations, not the exact continuous two-versus-many bifurcation and high-load optimizer profile established here. Those bodies of work are prior, not new claims. No empirical paper is asserted to calibrate the exponential risk kernel.

## Limitations

The mathematical conclusions are conditional on the specified Poisson encounter-load law and optimization of aggregate successful attempts. The model does not establish how wildlife choose routes, whether high-use passages actually have linear encounter intensity, or effects of predator avoidance, traffic, seasonality, heterogeneity, infrastructure cost or habitat connectivity. The existence of an asymmetric-better regime for \(n\ge3\) does **not** determine its sharp left endpoint or prove uniqueness of a global transition. Historical originality beyond the inspected published material remains provisional. This is not a management recommendation; independent validation has not been performed.

## References

1. Soanes, K. et al. (2024), *Do wildlife crossing structures mitigate the barrier effect of roads on animal movement? A global assessment*, Journal of Applied Ecology 61, 417–430. First published 2024-01-29. https://doi.org/10.1111/1365-2664.14582
2. Mata, C., Herranz, J. & Malo, J. E. (2020), *Attraction and Avoidance between Predators and Prey at Wildlife Crossings on Roads*, Diversity 12, 166. https://doi.org/10.3390/d12040166
3. Helldin, J. O. (2022), *Are several small wildlife crossing structures better than a single large?*, Nature Conservation 47, 197–213. https://doi.org/10.3897/natureconservation.47.67979
4. Andersson, A. & Ygge, F. (2001), *Efficient Resource Allocation with Non-Concave Objective Functions*, Computational Optimization and Applications 20, 281–298. https://doi.org/10.1023/A:1011263102622
5. Wagner, D. H. & Stone, L. D. (1974), *Optimization of Allocations Under a Coverability Condition*, SIAM Journal on Control 12, 373–379. https://doi.org/10.1137/0312029
6. Karlson, M., Seiler, A. & Mörtberg, U. (2017), *The effect of fauna passages and landscape characteristics on barrier mitigation success*, Ecological Engineering 105, 211–220. https://doi.org/10.1016/j.ecoleng.2017.04.059
