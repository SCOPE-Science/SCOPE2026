# A geometric staircase of optimal high-receptivity visits under geometric pollen carryover

## Finding
Consider a single pollinator carrying initial compatible pollen load \(L>0\), and \(n\ge 2\) successive receptive flowers. The pollinator deposits the same fraction \(1-q\), \(0<q<1\), of its residual load on each flower, regardless of its identity. Exactly \(r\) flowers, \(1\le r<n\), have high fertilization sensitivity \(a>b>0\); the other \(n-r\) have sensitivity \(b\). A flower receiving compatible pollen amount \(x\) has expected normalized successful seed output \(1-e^{-\alpha x}\), where \(\alpha\) is its sensitivity. All flowers have equal maximum normalized output. The order of the two flower types can be chosen, but their counts are fixed.

Write \(h(t)=e^{-bt}-e^{-at}\). For each \(c\in(0,1)\), let \(\theta(c)>0\) be the unique positive solution of \(h(\theta)=h(c\theta)\). Define \(c=q^r\) and, for \(1\le s\le n-r\),
\[
\Lambda_s=\frac{\theta(q^r)}{(1-q)q^{s-1}}.
\]
These thresholds satisfy \(0<\Lambda_1<\cdots<\Lambda_{n-r}\), with universal ratios \(\Lambda_{s+1}/\Lambda_s=1/q\), independent of \(a,b,n\) (except through the first threshold). **Every optimal sequence places its \(r\) high-sensitivity flowers in one consecutive block.** If \(L\) is not a threshold, the block starts at the unique position
\[
s_*(L)=1+\#\{s\in\{1,\ldots,n-r\}:L>\Lambda_s\}.
\]
At \(L=\Lambda_s\), precisely two arrangements are optimal: high-sensitivity blocks starting at \(s\) and \(s+1\). Each possible block occurs as the unique optimum on a nonempty interval of initial load, and the optimum progresses one position later at each successive threshold. Consequently, highly receptive flowers should come first when pollen is scarce, but last when pollen is abundant, under the stated saturation model.

The threshold equation can have a closed form: if \(a=2b\) and \(q^r=1/2\), then \(\theta(q^r)=2\log((1+\sqrt5)/2)/b\). For \(n=6\), \(r=2\), \(a=2\), \(b=1\), \(q=2^{-1/2}\), thresholds are approximately \(3.285919879,4.646992458,6.571839758,9.293984915\). At \(L=8\), the optimal high-sensitivity positions are \(4,5\) (one-based); expected total normalized successes are approximately \(4.241880690637\), compared to \(3.990255637369\) with high-sensitivity flowers first.

## Assumptions and scope
The event is one prescribed finite sequence. Geometric pollen loss is deterministic in expectation, with no pollen replenishment, grooming, competing donors, pollen-size variation, pollinator selection feedback, or species-specific removal fractions. All \(n\) flowers receive one visit; choosing order does not alter travel time, visit count or the retention factor \(q\). Each flower's expected contribution is the saturating negative-exponential response above, with identical normalized capacity; no claim is made about joint success independence. The objective is the expected **sum** of normalized successes across all \(n\) flowers. Permutations of indistinguishable flowers of the same sensitivity are identified as the same arrangement. All inequalities and optimizer statements hold for every real \(L>0,a>b>0,0<q<1\) and integers \(n\ge2,1\le r<n\).

## Proof
The amount delivered to visit \(j\), indexed from \(1\), is \(x_j=(1-q)Lq^{j-1}\), regardless of flower order. Placing a high-sensitivity rather than low-sensitivity flower at visit \(j\) improves expected normalized seed output by
\[
h(x_j)=(1-e^{-ax_j})-(1-e^{-bx_j})=e^{-bx_j}-e^{-ax_j}>0.
\]
Thus every arrangement with high-sensitivity position set \(S\), \(|S|=r\), has total objective \(F(S)=\sum_{j=1}^{n}(1-e^{-bx_j})+\sum_{j\in S}h(x_j)\). Maximization is exactly the problem of choosing the \(r\) largest values among the ordered score sequence \(h(x_1),\ldots,h(x_n)\).

The function \(h\) is strictly increasing up to \(x_0=\log(a/b)/(a-b)\) and strictly decreasing thereafter, because \(h'(x)=ae^{-ax}-be^{-bx}\), whose unique zero is \(x_0\). Its strict upper level sets are intervals. Since \(x_1>x_2>\cdots>x_n\), the \(r\) highest sampled scores form a contiguous interval of indices; in a boundary tie, the only possible choices are two adjacent blocks. In particular, it suffices to compare block sums \(B_s=\sum_{j=s}^{s+r-1}h(x_j)\), \(1\le s\le n-r+1\).

To prove the needed crossing is unique, fix any \(c\in(0,1)\), set \(d=(a-b)/2>0\) and \(m=(a+b)/2>d\), and write \(h(x)=2e^{-mx}\sinh(dx)\). For \(R_c(x)=h(x)/h(cx)\), differentiating gives
\[
\frac{d}{dx}\log R_c(x)=-m(1-c)+d\bigl(\coth(dx)-c\coth(cdx)\bigr).
\]
For every \(y>0\), the function \(y/(e^{2y}-1)\) is strictly decreasing. Therefore \(\coth y-c\coth(cy)<1-c\), and hence
\[
\frac{d}{dx}\log R_c(x)<-(m-d)(1-c)=-b(1-c)<0.
\]
Also \(\lim_{x\downarrow0}R_c(x)=1/c>1\) and \(\lim_{x\to\infty}R_c(x)=0\), using \(h(x)\sim(a-b)x\) at zero and \(h(x)\sim e^{-bx}\) at infinity. Thus exactly one \(\theta(c)>0\) has \(R_c(\theta)=1\). More precisely, \(h(cx)-h(x)<0\) when \(0<x<\theta(c)\) and is positive when \(x>\theta(c)\).

Adjacent blocks differ by only their two endpoint scores:
\[
B_{s+1}-B_s=h(x_{s+r})-h(x_s)=h(q^rx_s)-h(x_s).
\]
With \(c=q^r\), this difference is negative for \(L<\Lambda_s\), zero at \(\Lambda_s\), and positive for \(L>\Lambda_s\). The thresholds are strictly increasing and obey the asserted exact geometric ratio. Consequently, for any \(L\) off the thresholds, the consecutive block scores first strictly increase, then strictly decrease, with their unique maximum at \(s_*(L)\). At each \(\Lambda_s\) exactly one adjacent pair of block sums ties for the maximum. Strict unimodality of the individual scores rules out an additional noncontiguous optimal choice, because scores between the tied endpoint indices strictly exceed the tied endpoint score while scores outside them are smaller. Every interval of loads between the successive thresholds is nonempty, which proves all regimes and all uniqueness/tie assertions.

For the closed-form subfamily, with \(a=2b\) and \(c=1/2\), set \(u=e^{-b\theta/2}\in(0,1)\). The equation \(h(\theta)=h(\theta/2)\) reduces to \(u(1+u)=1\); hence \(u=(\sqrt5-1)/2\) and \(\theta=2\log((1+\sqrt5)/2)/b\). Substitution proves the example without any numerical optimization assumption.

## Verification
The standalone `checker.py` uses deterministic randomized examples over \(2\le n\le9\), every \(1\le r<n\), multiple positive sensitivity pairs and loss factors. It independently enumerates all \(\binom nr\) high-sensitivity position sets away from transition points, compares their objective with the predicted unique block, and checks every adjacent-block equality at the numerically bisected transition. It also verifies the golden-ratio identity and sample values. A direct replay passed 6089 assertions. The executable calculations are diagnostics only; the preceding argument proves the infinite-parameter statements.

To reproduce with Python 3: run `python checker.py` in the directory containing the extracted files. No nonstandard packages are required.

## Relationship to prior work
Geometric attenuation of pollen transfer among successive flowers is a classical modelling assumption, and saturating flower-level seed-set responses are established ecological ideas. Iwasa, de Jong and Klinkhamer (1995) optimize the fraction of flowers visited under an exponential transfer model, not the permutation of two fixed classes of recipient sensitivity. Waites and Ågren (2004) report saturating seed set with compatible pollen receipts. Cresswell and Hoyle (2006) recover paternity shadows and describe field-based flower-to-flower dispersal; they do not optimize heterogeneous recipient ordering in their model. Aizen and Harder (2007) introduce a negative-exponential dose response to pollen receipt, but accessible abstract/metadata do not settle whether their full text contains the present sequencing result. Kortsch and colleagues (2023) model geometric transfer along observed visitation sequences and aggregate successful pollination, rather than optimize the order of two receptivity classes. The general combinatorial selection of the largest entries of a unimodal score profile is elementary; the contribution claimed here is the exact coupled ecological phase diagram, including all geometric switching loads, optimizer uniqueness, and a high-load reversal, not that selection principle.

## Limitations
This is an idealized arrangement theorem, not evidence that free-foraging pollinators follow the predicted optimal order or that real floral sensitivity is exactly dichotomous. If sensitive flowers differ in capacity, pollen removal depends on flower identity, multiple visits accumulate, or pollen limitation deviates substantially from a negative-exponential dose response, the objective may no longer separate and the block theorem need not hold. The polynomial/exponential sensitivity model is not calibrated to an empirical population. Historical priority is provisional: the full 2007 Aizen–Harder article and the full 1995 visitation-optimization article were not both accessible for statement-level comparison, and generic scheduling/assignment literature may contain equivalent consequences.

## References
- Iwasa, Y., de Jong, T. J., and Klinkhamer, P. G. L. (1995), "Why pollinators visit only a fraction of the open flowers on a plant: The plant's point of view," *Journal of Evolutionary Biology* 8, 439–453, https://academic.oup.com/jeb/article-abstract/8/4/439/7322536 (public issue date July 1, 1995).
- Waites, A. R., and Ågren, J. (2004), "Pollinator visitation, stigmatic pollen loads and among-population variation in seed set in Lythrum salicaria," *Journal of Ecology* 92, 512–526, https://doi.org/10.1111/j.0022-0477.2004.00893.x (first published May 13, 2004).
- Cresswell, J. E., and Hoyle, M. (2006), "A mathematical method for estimating patterns of flower-to-flower gene dispersal from a simple field experiment," *Functional Ecology* 20, 245–251, https://doi.org/10.1111/j.1365-2435.2006.01085.x (first published April 19, 2006).
- Aizen, M. A., and Harder, L. D. (2007), "Expanding the limits of the pollen-limitation concept: effects of pollen quantity and quality," *Ecology* 88, 271–281, https://doi.org/10.1890/06-1017 (first published February 1, 2007).
- Kortsch, S., et al. (2023), "Landscape composition and pollinator traits interact to influence pollination success in an individual-based model," *Functional Ecology* 37, 2056–2071, https://doi.org/10.1111/1365-2435.14353.
