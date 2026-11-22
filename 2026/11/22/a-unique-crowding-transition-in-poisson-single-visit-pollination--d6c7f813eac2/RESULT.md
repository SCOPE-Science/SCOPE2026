# A unique crowding transition in Poisson single-visit pollination

## Finding

For every integer \(n\geq2\) and real \(B>0\), distribute a fixed expected number \(B\) of independent pollinating seed-predator visits among \(n\) equivalent flowers. Flower \(i\) receives a Poisson number of visits of mean \(x_i\geq0\), and retains viable seed in the idealized single-success regime if and only if it receives **exactly one** visit. Thus expected viable flowers equal
\[
\Phi_n(x_1,\ldots,x_n)=\sum_{i=1}^n x_i e^{-x_i},\qquad \sum_{i=1}^n x_i=B.
\]

The following global classification holds.

1. Every maximizer uses strictly positive means. It is either uniform, with every \(x_i=B/n\), or has precisely one overloaded flower of mean \(x>2\) and \(n-1\) equally visited flowers of mean \(1<y<2\).
2. For two flowers, uniform allocation is the unique maximizer for \(0<B\leq4\). For \(B>4\), the only maximizers are the two permutations of \((B/2-t,B/2+t)\), where \(t>0\) is the unique solution of \(B=2+2t\coth t\). The imbalance begins continuously, with \(t\sim\sqrt{3(B-4)/2}\) as \(B\downarrow4\).
3. For every \(n\geq3\), there is exactly one switching budget \(B_c(n)\), with \(n+1<B_c(n)<2n\). Uniform allocation uniquely maximizes the expectation for \(B<B_c(n)\). At \(B=B_c(n)\), it ties at least one overloaded allocation, and for \(B>B_c(n)\) every maximizer is overloaded. The nonuniformity is discontinuous at the switch: the competing overloaded allocation stays a positive distance from uniformity as \(B\downarrow B_c(n)\) from above.
4. As \(B\to\infty\), each global optimizer (up to relabeling) has \(n-1\) means tending to \(1\), with the remaining mean equal to \(B-(n-1)+o(1)\); the maximum expectation tends to \((n-1)/e\).

In particular, two flowers have a continuous balance-breaking transition at total expected load \(4\), whereas every larger finite collection has a single discontinuous transition before the mean reaches \(2\) visits per flower. For \(n=3\), a numerical solution of the stationarity and equal-value equations gives \(B_c(3)\approx5.774313471725\) (illustrative, not a certified numerical interval).

## Assumptions and scope

The \(n\) flowers are exchangeable; each has the same one-visit viability rule; expected visit intensities are nonnegative real control variables with a fixed sum \(B\). Visit counts are modeled as independent Poisson variables; only their one-visit marginal probabilities are required for the expectation, so independence is not required for the algebraic expectation itself. No variable floral costs, behavioral constraints, traffic feedback, interacting visits, heterogeneous fitness or empirical calibration is assumed. The exact-one rule is a limiting representation of brood-pollinating seed-predator systems in which repeat oviposition destroys viability. It is *not* a general biological claim that two visits harm all flowers.

A 'global maximizer' means a point of the closed simplex \(\{x_i\geq0:\sum_i x_i=B\}\) attaining the displayed expectation. A 'transition' means a change in its global maximizing configuration, not a bifurcation of actual pollinator dynamics. We use only real-variable analysis, not simulations to establish global statements.

## Proof

**1. Interior and shape.** Write \(f(u)=ue^{-u}\) on \([0,\infty)\). Its first three derivatives are \(f'(u)=(1-u)e^{-u}\), \(f''(u)=(u-2)e^{-u}\), and \(f'''(u)=(3-u)e^{-u}\). A global maximum exists by compactness. No component may be zero: if \(x_i=0\) and \(x_j>0\), moving a sufficiently small amount from \(x_j\) to \(x_i\) strictly increases the objective because \(f'(0)=1>f'(x_j)\).

At an interior maximum all derivatives \(f'(x_i)\) coincide. Since \(f'\) is strictly decreasing on \((0,2)\) and strictly increasing on \((2,\infty)\), there are at most two coordinate values. Two coordinates both greater than \(2\) are impossible: their opposite-direction second variation is \(f''(x_i)+f''(x_j)>0\), contradicting local maximality. If no coordinate exceeds \(2\), injectivity of \(f'\) on \((0,2]\) forces equality of all coordinates (the endpoint \(2\) also has a unique derivative value on \((0,2]\)). Otherwise, exactly one coordinate is \(x>2\), and all others equal \(y<2\). Equal derivatives are negative, hence \(y>1\). This proves the structural classification. For such a nonuniform maximum, necessarily \(B=(n-1)y+x>n+1\).

**2. Two flowers.** Parameterize \(x_1=B/2-t\), \(x_2=B/2+t\) with \(0\leq t\leq B/2\). Direct calculation gives
\[
\Phi_2(t)=2e^{-B/2}\left[(B/2)\cosh t-t\sinh t\right],\qquad
\Phi_2'(t)=2e^{-B/2}\left[(B/2-1)\sinh t-t\cosh t\right].
\]
For \(t>0\), an interior critical point solves \(B=2+2t\coth t\). The function \(t\coth t\) increases strictly from \(1\) to infinity: its derivative has numerator \(\sinh t\cosh t-t>0\) because \(\sinh(2t)>2t\). Consequently, for \(B\leq4\) the objective strictly decreases with \(t>0\); for \(B>4\), it increases initially, then decreases across exactly one root. The root is feasible since \(t<B/2=1+t\coth t\). Symmetry yields the two unique permutations. The Taylor expansion \(t\coth t=1+t^2/3+O(t^4)\) gives \(t\sim\sqrt{3(B-4)/2}\).

**3. At most one global switch.** Write each allocation as \(x_i=Bp_i\), where \(p\) is in the unit simplex \(\Delta_n\). Relative to the uniform objective \(B e^{-B/n}\), the value at the share vector \(p\) is
\[
R_p(B)=\sum_{i=1}^n p_i\exp\left[B\left(\frac1n-p_i\right)\right].
\]
The function \(\log R_p(B)\) is convex in \(B\): it is the log moment-generating function of the finite probability distribution assigning mass \(p_i\) to \(1/n-p_i\). It is valid also when some \(p_i=0\), by deleting zero-weight terms. Therefore
\[
g_n(B)=\max_{p\in\Delta_n}\log R_p(B)
\]
is convex, continuous and nonnegative; the uniform allocation gives \(g_n(B)=0\) as a lower bound. The structural argument in step 1 shows \(g_n(B)=0\) for all \(0<B\leq n+1\), since an overloaded maximizer would force \(B>n+1\). For sufficiently large \(B\), the allocation \((1,\ldots,1,B-n+1)\) yields an objective tending to \((n-1)/e>0\), while the uniform value tends to \(0\). Thus the zero set of the nonnegative convex function \(g_n\) is precisely a closed interval \([0,B_c(n)]\) with finite right endpoint; moreover \(g_n(B)>0\) for every \(B>B_c(n)\).

Uniform allocation is the **only** maximizer for \(0<B<B_c(n)\). Indeed, if a nonuniform share vector \(p\) tied uniform at some such \(B\), then \(\log R_p(0)=\log R_p(B)=0\). When its positive shares differ, \(\log R_p\) is strictly convex and must become positive just beyond \(B\), contradicting \(g_n=0\) on a neighborhood to its right. When its positive shares are all equal on a proper subset of size \(m<n\), \(R_p(B)=\exp[B(1/n-1/m)]<1\), also excluding a tie.

**4. The transition for three or more flowers.** For \(n\geq3\), at \(B=2n\) compare the uniform vector \((2,\ldots,2)\) to the feasible perturbation with \(n-1\) coordinates \(2-\varepsilon\) and one coordinate \(2+(n-1)\varepsilon\). Since \(f''(2)=0\), \(f'''(2)=e^{-2}>0\), Taylor's theorem yields
\[
\Phi_n(2-\varepsilon,\ldots,2-\varepsilon,2+(n-1)\varepsilon)
-nf(2)
=\frac{e^{-2}}6(n-1)n(n-2)\varepsilon^3+O_n(\varepsilon^4)>0
\]
for sufficiently small positive \(\varepsilon\). Hence \(B_c(n)<2n\). Also \(B_c(n)>n+1\): otherwise, a sequence of nonuniform maximizers at budgets approaching \(n+1\) from above would satisfy \(x>2\), \(y>1\), \((n-1)y+x\to n+1\), so \(x\to2\), \(y\to1\), contradicting their stationary derivative equality \(f'(x)=f'(y)\), since \(f'(2)=-e^{-2}\neq0=f'(1)\).

At \(B=B_c(n)<2n\), the uniform allocation is a strict local maximizer because \(f''(B_c/n)<0\). Maximizers for budgets decreasing to \(B_c\) from above have convergent subsequences by compactness; their limits are maximizers at \(B_c\). They cannot approach the uniform point: near it the second variation remains strictly negative for all sufficiently close budgets, and it beats every unequal sufficiently nearby allocation. Thus a distinct overloaded maximizer ties uniform at \(B_c\), and the displacement is bounded away from zero along all maximizers just above \(B_c\). This is a discontinuous transition. The two extreme phases cannot alternate because the positive set of the convex \(g_n\) is the ray \((B_c,\infty)\).

**5. Large-visit limit.** For \(B>B_c(n)\), every maximizer has one \(x>2\) and \(n-1\) instances of \(y\in(1,2)\); since \(x=B-(n-1)y\to\infty\), stationarity implies \(f'(y)=f'(x)\to0^-\). The only zero of \(f'\) in \([1,2]\) is \(1\), hence \(y\to1\) and \(x=B-(n-1)+o(1)\). The objective tends to \((n-1)/e\). This completes the proof.

## Verification

The standalone `checker.py` performs deterministic numerical checks of the two-flower hyperbolic optimum on a parameter grid, stationarity and global-candidate consistency for several higher flower counts, random feasible competitors, and the strict cubic comparison at \(B=2n\). A replay produced 62,645 passed assertions. The checker is supplementary only: random simplex tests do not prove global optimality, and neither the transition uniqueness nor the infinite parameter ranges depend on it. The proof above supplies those results. The approximate value of \(B_c(3)\) comes from numerically solving \(f'(x)=f'(y)\), \(x+2y=B\), and \(f(x)+2f(y)=3f(B/3)\).

## Relationship to prior work

Després (2003) establishes the biological relevance of seed-eating brood pollinators, in which oviposition and pollination are coupled. Holland, Bronstein and DeAngelis (2004), and DeAngelis and Holland (2006), discuss floral visitation, flower-to-pollinator ratios, and seed consumption. Ezoe (online October 26, 2016; journal issue 2017) analyzes flower-production and fruit-abortion resource strategies under over-oviposition; the present theorem instead fixes the number of flowers and the total expected Poisson visits and optimizes their *heterogeneous intensity distribution*, establishing a global sharp two-versus-many transition.

Mathar and Žilinskas (1993) study fixed-traffic ALOHA with finite Bernoulli transmitters sharing a **single** collision channel, whose throughput is \(\sum_i p_i\prod_{j\ne i}(1-p_j)\), rather than the sum of singleton probabilities across **independent** channels considered here. The common expression \(u e^{-u}\) is classical (Poisson singleton probability and Poisson ALOHA throughput); neither that expression nor maximizing it separately implies the global fixed-sum phase classification. Mathematical priority is not certified: no exhaustive universal-literature search is possible, and some plausible older biological and optimization texts were only partially accessible.

## Limitations

The exact-one survival assumption is a sharp, deliberately idealized damage threshold; many ordinary pollinators improve seed set with repeated visits, and natural visitors cannot necessarily be steered to a prescribed vector of Poisson means. The theorem optimizes expected *number of viable flowers*, not population growth, net seeds under partial damage, evolutionary stability, or welfare. Its budget \(B\) is an expected visit count, not observed visits. For \(n\geq3\), the switch is proved unique and bounded, but no elementary closed-form expression for \(B_c(n)\) is asserted, and the numerical example is not an interval-certified root. Inaccessible relevant complete texts remain a historical-priority risk. No independent validation has been undertaken.

## References

- Després, L. (2003), *Sex and pollen: the role of males in stabilising a plant-seed eater pollinating mutualism*. Oecologia 135, 60–66. First online February 7, 2003. https://doi.org/10.1007/s00442-003-1181-z
- Holland, J. N., Bronstein, J. L., and DeAngelis, D. L. (2004), *Testing hypotheses for excess flower production and low fruit-to-flower ratios in a pollinating seed-consuming mutualism*. Oikos 105, 633–640. https://doi.org/10.1111/j.0030-1299.2004.13058.x
- DeAngelis, D. L., and Holland, J. N. (2006), *Emergence of ratio-dependent and predator-dependent functional responses for pollination mutualism and seed parasitism*. Ecological Modelling 191, 551–556. https://doi.org/10.1016/j.ecolmodel.2005.06.005
- Ezoe, H. (2017 issue; online 2016), *Optimal resource allocation model for excessive flower production in a pollinating seed-predator mutualism*. Theoretical Ecology 10, 105–115. https://doi.org/10.1007/s12080-016-0316-x
- Mathar, R., and Žilinskas, A. (1993), *Maximizing throughput of finite population slotted ALOHA*. Informatica 4, 163–171. https://doi.org/10.3233/INF-1993-41-211
