# Asymmetric optimal founder effort in two identical quorum-limited habitats

## Finding

Consider two identical, independent habitat patches. A total expected founder-arrival intensity of ten can be assigned as nonnegative Poisson means \(x\) and \(10-x\). Each patch is independently suitable with probability \(q=799/800\); conditional on suitability, a patch passes a one-step establishment threshold if at least two founders arrive. The objective is to maximize the probability that **at least one patch** passes this threshold. The complete set of globally optimal allocations consists of **exactly two unequal interior splits**, \((x_*,10-x_*)\) and \((10-x_*,x_*)\), where
\[
x_*=5-u_*,\qquad 2<u_*<3,
\]
with \(u_*\) the unique solution in \((2,3)\) of
\[
e^5\left(5\frac{\sinh u}{u}-\cosh u\right)=799.
\]
Numerically \(x_*=2.9374809396609965\ldots\). Neither concentrating all effort in one habitat nor distributing it equally is globally optimal. The two strict asymmetric optima persist throughout an open neighborhood of the specified positive mean budget and suitability probability.

## Assumptions and scope

The decision variable is **expected founder intensity**, not a fixed realized number of founders. Conditional on allocation \((x,10-x)\), counts at the two patches are independent Poisson random variables with those means, including zero means at boundary allocations. Suitability is independent between patches, with common probability \(799/800\), and independent of counts. There is no dispersal between patches during the one-step bottleneck. The viability proxy is the event of at least two arrivals at a suitable patch; it does not imply reproduction or eventual ecological persistence.

For \(z\ge0\), the probability a patch fails this event is
\[
f(z)=1-q+q(1+z)e^{-z}
=\frac{1+799(1+z)e^{-z}}{800}.
\]
The probability of failure at **both** patches is \(F(x)=f(x)f(10-x)\), for \(0\le x\le10\). Global success is \(1-F(x)\). The conclusion is a global optimization over this entire continuous interval.

## Proof

**1. Exact derivative and reduction.** For \(q=799/800\), put \(c=(1-q)/q=1/799\). Then
\[
\frac{-f'(z)}{f(z)}=\frac{z}{1+z+c e^z}=:H(z).
\]
For \(0<x<5\), put \(y=10-x\) and
\[
Q(x)=\frac{x e^y-y e^x}{y-x}.
\]
As the denominator in the following fraction is strictly positive, direct algebra gives
\[
\frac{F'(x)}{F(x)}=H(y)-H(x)
=\frac{(y-x)(1-Q(x)/799)}{(1+x+c e^x)(1+y+c e^y)}.
\]
In particular, \(\operatorname{sign}F'(x)=\operatorname{sign}(799-Q(x))\). Set \(u=5-x\), so \(0<u<5\). Then
\[
Q(x)=G(u):=e^5\left(5\frac{\sinh u}{u}-\cosh u\right).
\]
The continuous value at zero is \(G(0)=4e^5\).

**2. A strict one-peak lemma.** Differentiating and cancelling positive factors shows the sign of \(G'(u)\) equals the sign of
\[
J(u)=5u\cosh u-(5+u^2)\sinh u.
\]
Its entire power series is
\[
J(u)=\frac23u^3-
\sum_{n=3}^{\infty}\frac{4n(n-2)}{(2n+1)!}u^{2n+1}.
\]
Consequently \(J(u)/u^3\) is strictly decreasing for all \(u>0\), starts at \(2/3\), and tends to a negative value without bound as \(u\to\infty\) (also immediately from the exponential representation of \(J\)). Therefore \(G\) strictly increases to a single global maximum and then strictly decreases. No other extrema or level-set crossings are possible.

**3. Exact location of the crossings.** The following strict inequalities hold:
\[
G(0)<799,\quad G(2)<799<G(3),\quad 799<G(4),\quad G(5)=-1<799.
\]
They are *exact rationally certified inequalities*, not merely floating-point observations: use \(E_{20}=\sum_{j=0}^{20}1/j!\), bound \(E_{20}<e<E_{20}+2/21!\), and evaluate all expressions using rational interval arithmetic. The complete certificate is implemented in `check.py`. As \(G\) has only one peak, the equation \(G(u)=799\) has exactly two roots, \(u_-\in(2,3)\) and \(u_+\in(4,5)\). The signs of \(F'\) in \((0,5)\) are respectively positive, negative, positive as \(u=5-x\) crosses these two roots in decreasing order. Thus \(x=5-u_+\) is a strict local maximum of \(F\), \(x_*=5-u_-\) is its only strict interior local minimum on \((0,5)\), and the equal allocation \(x=5\) is a strict local maximum of \(F\).

**4. Global comparison.** The same rational interval certificate proves
\[
F(3)<F(0),\qquad F(3)<F(5).
\]
The monotonicity diagram from step 3 implies \(F(x_*)\le F(3)<F(0)\); since \(x_*\) is the only interior minimum of \(F\) on \([0,5]\), it is the unique minimum there. By exact reflection symmetry \(F(x)=F(10-x)\), \(10-x_*\) is the only further global minimizer on \([0,10]\). This proves the complete two-optimum classification. Nondegenerate derivative crossings and a strict global gap to every point outside neighborhoods of the two minima imply, by continuity and the implicit-function theorem, that a pair of unequal interior global optima persists for all sufficiently nearby positive budgets and suitability probabilities. Their exact locations need not remain the values computed here.

## Verification

`check.py` uses only the Python standard library. Run `python check.py` in the same directory as this file. It constructs strict rational bounds for \(e\), certifies the strict comparisons of \(G\) and \(F\), and independently checks the analytic logarithmic derivative against centered finite differences at 249 locations. The printed numerical optimum is diagnostic, whereas global uniqueness is proved by the one-peak lemma and derivative sign analysis. The checker is standalone and requires no external data or software packages.

The illustrative values are \(F(x_*)\approx0.001708378230066\), compared with \(F(0)\approx0.001748774978353\) and \(F(5)\approx0.001732819399997\). All success probabilities are their complements.

## Relationship to prior work

Grevstad (1999) distinguished Allee-related aggregation from environmental-risk diversification and reported an intermediate optimal introduction size in a simulation model; the accessible abstract does not assert this exact two-Poisson-mean, two-quorum, continuous-allocation optimization. Shea and Possingham (2001), in accessible full text, optimized a multi-year stochastic control model with a different sigmoid release-success relationship and discrete release-size actions. Duncan and colleagues (2014), in accessible full text, analyzed the establishment probability as a function of founding population size with environmental heterogeneity, rather than two simultaneous controllable Poisson-mean allocations. Goodsman and Lewis (2016) analyzed a spatial dynamical minimum-founder threshold, rather than the independent one-step two-site optimization.

A relevant published mathematical result for **fixed counts of known male and female founders** at two habitats proves that all globally best allocations concentrate or divide nearly equally. The present claim is not a corollary: here the arrivals are Poisson random variables constrained only in expectation, a local viable event is a single-type count of at least two, and the exact global best solutions are strictly asymmetric. Derman, Lieberman and Ross (1974) studied the broader allocation of reliability budgets to independent components, including the one-of-two system form of the current objective with an arbitrary component success function. That establishes the general formulation; the accessible abstract supplies conditions for equal allocation, but no exact all-global optimizer classification for the present nonconcave two-arrival Poisson success curve. Their complete text was not accessible, making this a material historical-coverage risk. Other published two-patch allocation models were compared by their hypotheses and objective, not by title or superficial parameter resemblance.

## Limitations

The conclusion is for a stylized one-step quorum proxy and does not claim long-term persistence, field applicability, or optimality under fixed realized founder numbers. The independent site-suitability model omits correlated disturbances, inter-patch migration, demographic reproduction and heterogeneous sites. The explicit theorem gives one robust parameter neighborhood, not a complete phase diagram over every founder budget and suitability probability. A general reliability-allocation theory already includes the same abstract one-of-two optimization structure, and this claim does not assert originality for that framework. Search coverage cannot establish global historical priority; an older highly relevant simulation paper was accessible only in abstract form and could not be obtained through the available institutional route.

## References

1. C. Derman, G. J. Lieberman and S. M. Ross (1974), *Optimal allocations in the construction of k-out-of-n reliability systems*, Management Science 21:241–250. DOI `10.1287/mnsc.21.3.241`. First published online 1974-11-01; complete text unavailable, abstract read.
2. F. S. Grevstad (1999), *Factors influencing the chance of population establishment: implications for release strategies in biocontrol*, Ecological Applications 9:1439–1447. DOI `10.1890/1051-0761(1999)009[1439:FITCOP]2.0.CO;2`. First public date verified from publisher: 1999-11-01.
3. K. Shea and H. P. Possingham (2001 online), *Optimal release strategies for biological control agents: an application of stochastic dynamic programming to population management*, Journal of Applied Ecology 37:77–86. DOI `10.1046/j.1365-2664.2000.00467.x`. Publisher gives first publication 2001-12-25.
4. R. P. Duncan, T. M. Blackburn, S. Rossinelli and S. Bacher (2014), *Quantifying invasion risk: the relationship between establishment probability and founding population size*, Methods in Ecology and Evolution 5:1255–1263. DOI `10.1111/2041-210X.12288`. First public date 2014-10-23.
5. D. W. Goodsman and M. A. Lewis (2016), *The minimum founding population in dispersing organisms subject to strong Allee effects*, Methods in Ecology and Evolution 7:1100–1109. DOI `10.1111/2041-210X.12573`. First public date 2016-04-05.
6. *An all-or-nearly-even release theorem for two-site mate-limited establishment*, 2026, public mathematics record: `https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-an-all-or-nearly-even-release-theorem-for-two-site-mate-limited--16a69419a1f0`.
