# Mortality-matched investment for serial habitat passage under arbitrary deadline rewards

## Finding

Consider an organism, propagule, or transported biological payload that must traverse two directed habitat connections in sequence, and can be lost while waiting at either one. With positive traversal rates \(u,v\), local loss hazards \(d_1,d_2\), and fixed investment \(u+v=C\), every optimal allocation assigns **strictly more traversal capacity to the stage having the larger loss hazard**, regardless of the nonnegative bounded function used to reward successful arrival times. Thus the ordering survives deterministic deadlines, random independent deadlines, exponential discounting, and even nonmonotone reward windows.

For a deterministic deadline \(T>0\), an optimal allocation is unique for all sufficiently short and all sufficiently long deadlines. Its first-stage rate satisfies

\[
u_T=\frac C2+\frac{C^2(d_1-d_2)}{96}T^2+O(T^3)\quad(T\downarrow0),
\]

and every finite-deadline optimum converges as \(T\to\infty\) to the unique eventual-success maximizer

\[
u_\infty=\frac{C}{1+\sqrt{d_2(C+d_1)/(d_1(C+d_2))}}.
\]

If the two loss hazards are equal, exactly balanced investment is the unique optimum for every nonnegative, nonincreasing, bounded reward that is nonzero on a set of positive measure; in particular for all deterministic deadlines.

## Assumptions and scope

There are states \(0\) (first connection), \(1\) (second connection), \(2\) (successful arrival), and a cemetery state \(\partial\) (irreversible loss). Start in \(0\). From \(0\), the independent exponential clocks \(u>0\) and \(d_1>0\) send the process to \(1\) and \(\partial\), respectively. From \(1\), independent exponential clocks \(v>0\) and \(d_2>0\) send it to \(2\) and \(\partial\). State \(2\) is absorbing. Rates are fixed throughout the traversal and satisfy \(u+v=C>0\); endpoints \(u=0\) or \(v=0\) are allowed as design alternatives with zero success.

For any bounded Borel \(w:[0,\infty)\to[0,\infty)\), positive on a set of positive Lebesgue measure, define

\[
J_w(u)=\mathbb E\big[w(\tau)\mathbf1_{\{\text{successful arrival}\}}\big],\qquad v=C-u,
\]

where \(\tau\) is the time of successful arrival and the indicator prevents evaluation of \(w\) after loss. For a deterministic deadline \(T\), set \(w(s)=\mathbf1_{\{s\le T\}}\), writing \(J_T(u)\). For an independent random deadline \(D\), \(w(s)=\Pr(D\ge s)\), assuming this is nonzero on a positive-measure set. No assumption of empirical calibration is made. The distinction between a passage rate and a per-stage extinction hazard is substantive: maximizing successful arrival probability is not maximizing mean lifetime of an extinction–recolonization system.

## Proof

**1. Exact successful-arrival density.** For passage durations \(x,y>0\), successful completion through both stages has joint (unconditional) density

\[
u v\,e^{-(u+d_1)x-(v+d_2)y}\,dx\,dy.
\]

Consequently

\[
J_w(u)=uv\int_0^\infty\!\int_0^\infty
w(x+y)e^{-(u+d_1)x-(v+d_2)y}\,dx\,dy.
\tag{1}
\]

Put \(K=C+d_1+d_2\), \(\delta=u-v+d_1-d_2\), and \(\operatorname{sinhc}(z)=\sinh(z)/z\) for \(z\ne0\), with value \(1\) at zero. The substitution \(s=x+y\) gives the exact reduction

\[
J_w(u)=uv\int_0^\infty s\,w(s)e^{-Ks/2}
\operatorname{sinhc}\!\left(\frac{\delta s}{2}\right)ds.
\tag{2}
\]

Since \(d_1,d_2>0\), the integral and all its rate derivatives converge absolutely, uniformly over the compact design interval. Formula (2) also holds at \(u=0,C\), where \(J_w=0\).

**2. Strict loss-hazard matching for every admissible reward.** The even function \(\operatorname{sinhc}\) strictly increases with \(|z|>0\): its power series is \(\sum_{n\ge0}z^{2n}/(2n+1)!\), and every nonconstant coefficient is positive. Let \(u>v\), and compare it with the swapped design \((v,u)\). Their products \(uv\) and \(K\) agree. If \(d_1>d_2\), then

\[
\big|u-v+d_1-d_2\big|>
\big|v-u+d_1-d_2\big|.
\]

Because \(w>0\) on a positive-measure set of positive times, equation (2) shows \(J_w(u)>J_w(v)\). Thus no maximizing design can satisfy \(u<v\). At \(u=v=C/2\), differentiation of (2) gives

\[
J_w'(C/2)=\frac{C^2}{4}\int_0^\infty s^2w(s)e^{-Ks/2}
\operatorname{sinhc}'\!\left(\frac{(d_1-d_2)s}{2}\right)ds>0,
\]

when \(d_1>d_2\). Hence the balanced design is not maximal either. Continuity, positivity in \((0,C)\), and zero endpoint values guarantee an interior maximizer; every maximizer obeys \(u>v\). Reversing indices proves \(u<v\) when \(d_1<d_2\). No monotonicity of \(w\) was used.

**3. Equal-hazard rigidity for nonincreasing rewards.** Suppose \(d_1=d_2=d>0\) and \(w\) is nonincreasing. The probability of completing both passages before loss equals

\[
q(u)=\frac{u}{u+d}\frac{v}{v+d}
=\frac{uv}{uv+dC+d^2},
\]

strictly maximized at \(u=v=C/2\). Conditional on success, \(\tau=X+Y\) is the sum of independent exponentials with rates \(A=u+d\) and \(B=v+d\). Their sum \(A+B=C+2d=2m\) is fixed. With \(\eta=|A-B|/2\), its survival function is

\[
\Pr(X+Y>t)=e^{-mt}
\left[\cosh(\eta t)+\frac{m}{\eta}\sinh(\eta t)\right]
\]

(with the continuous limit at \(\eta=0\)). For every \(t>0\), this expression increases strictly as \(\eta\) increases: both \(\cosh(\eta t)\) and \(\sinh(\eta t)/\eta\) are increasing. Thus balance makes conditional arrival time stochastically smallest, so it maximizes \(\mathbb E[w(\tau)\mid\text{success}]\). Multiplication by the strictly maximized \(q(u)\) gives unique balance. The assertion is intentionally restricted to nonincreasing rewards; a reward confined to late arrival times need not favor balance.

**4. Short-horizon uniqueness and expansion.** For \(w(s)=\mathbf1_{\{s\le T\}}\), equation (2) has the uniform \(C^2\)-in-\(u\) Taylor expansion

\[
\frac{2J_T(u)}{T^2}=uv\left[1-\frac{KT}{3}
+\left(\frac{K^2}{16}+\frac{\delta^2}{48}\right)T^2
+O(T^3)\right].
\tag{3}
\]

All derivatives through order two of the remainder are uniform on \([0,C]\), because the integrand is analytic jointly in \(u,T\) near the compact design set. The right side approaches the strictly concave quadratic \(u(C-u)\) in \(C^2\); therefore it is strictly concave for all sufficiently small \(T>0\), ensuring a unique interior optimizer \(u_T\). Let \(u_T=C/2+h_T\). Differentiating the logarithm of (3), using \(K\) constant and \(\delta=d_1-d_2+2h_T\), yields

\[
0=-\frac{8h_T}{C^2}+\frac{d_1-d_2}{12}T^2+O(T^3),
\]

hence \(h_T=C^2(d_1-d_2)T^2/96+O(T^3)\).

**5. Long-horizon optimizer and uniqueness near infinity.** Monotone convergence in (1), or separate integration over the two successful passages, gives

\[
J_\infty(u)=\lim_{T\to\infty}J_T(u)
=\frac{u}{u+d_1}\frac{C-u}{C-u+d_2}.
\tag{4}
\]

The logarithm of (4) has strictly negative second derivative on \((0,C)\), since

\[
\frac{d^2}{du^2}\log J_\infty(u)
=-\frac1{u^2}+\frac1{(u+d_1)^2}
-\frac1{(C-u)^2}+\frac1{(C-u+d_2)^2}<0.
\]

Its derivative vanishes exactly when

\[
d_1(C-u)(C-u+d_2)=d_2u(u+d_1),
\]

and solving for the unique interior root gives the stated \(u_\infty\). Because both loss hazards are positive, \(J_T\to J_\infty\) uniformly together with the first two \(u\)-derivatives (dominate derivatives of the successful-passage density by a fixed integrable exponential polynomial). Every sequence of maximizers thus converges to \(u_\infty\). Since \(J_\infty''(u_\infty)<0\) and all maximizers eventually lie in a small neighborhood of that point, \(J_T''<0\) there for large \(T\), giving uniqueness for all sufficiently large deadlines.

No claim of uniqueness at every intermediate deadline is made.

## Verification

The self-contained `check.py` numerically compares equation (2) against an independently integrated two-stage success density for randomized positive parameters, tests allocation swapping for constant, discounted and nonmonotone arrival windows, tests equal-hazard balance on deterministic deadlines, and examines both horizon limits. Run from the directory containing this file: `python check.py` (Python with SciPy). The resulting finite tests supplement, but cannot replace, the all-parameter proof above.

For \(C=3\), \(d_1=3\), \(d_2=0.2\) and \(T=2\), numerical maximization yields \(u_T\approx1.89630477\), compared with equal allocation \(u=1.5\). The successful-arrival probabilities are about \(0.29493954\) and \(0.27836450\), a relative improvement of approximately \(5.95\%\); the eventual-success optimizer is \(u_\infty\approx2.21638838\). The computation is illustrative, not an exact uniqueness certificate for this intermediate \(T\).

## Relationship to prior work

Oehri and coauthors' habitat-connectivity paper (preprint first posted 2023-11-24; journal 2024-09-24) motivates the ecological importance of serial and stepping-stone connectivity, but its publicly available full journal text develops multispecies landscape connectivity indicators and dispersal kernels, not competing stage-mortality clocks with optimally budgeted serial traversal or arbitrary arrival-time rewards. Saura, Bodin and Fortin (2014) already motivate and model networks of stepping-stone passages for long-distance dispersal, without this continuous-time rate-budget problem. Gholamialam and coauthors (2023) consider landscape vulnerability and least-cost paths, not this stochastic rate-budget theorem. Classical comparisons of sums of exponential random variables, including Bon and Păltănea (1999), already establish related hypoexponential stochastic orders; the equal-hazard conditional-arrival argument is an application of that established idea, not a claimed invention. The novel claim assessed here is the hazard-matched **universal success-allocation ordering** in the presence of competing death, together with sharp deadline-limit biases.

Published metapopulation rescue-budget results address reversible recolonization and mean extinction times rather than a single particle's absorbing two-step passage, and tandem queue scheduling results address distinct multi-customer objectives. Similar words such as 'two-stage' or 'budget' do not imply coverage; nevertheless priority over all historical stochastic-network control work is not proven.

## Limitations

This is an exact theorem for memoryless, independent, unidirectional transition and mortality clocks, a fixed sum of traversal *rates*, and one individual or propagule. Environmental variation, capacity constraints, feedback, alternate paths, correlated movement and mortality, and intervention costs nonlinear in rate are not represented. The universal ordering does not say the complete optimum is unique for every intermediate deadline or arbitrary nonmonotone weight. The early- and late-horizon uniqueness statements are asymptotic, not explicit finite cutoffs. This model has not been field-calibrated or independently externally validated.

## References

1. Oehri, J., Wood, S. L. R., Touratier, E., Leung, B., Gonzalez, A. *Rapid evaluation of habitat connectivity change to safeguard multispecies persistence in human-transformed landscapes.* bioRxiv preprint DOI: [10.1101/2023.11.23.568419](https://doi.org/10.1101/2023.11.23.568419), first posted 2023-11-24; final open-access article in *Biodiversity and Conservation* (2024), DOI: [10.1007/s10531-024-02938-2](https://doi.org/10.1007/s10531-024-02938-2).
2. Saura, S., Bodin, Ö., Fortin, M.-J. *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks.* *Journal of Applied Ecology* **51** (2014), 171–182; first available 2013-10-01. [10.1111/1365-2664.12179](https://doi.org/10.1111/1365-2664.12179).
3. Gholamialam, A., Matisziw, T. C., Trauth, K. M. *Contextualizing vulnerability of ecological systems to landscape alteration.* *Landscape Ecology* (2023), [10.1007/s10980-023-01656-4](https://doi.org/10.1007/s10980-023-01656-4).
4. Bon, J.-L., Păltănea, E. *Ordering properties of convolutions of exponential random variables.* *Lifetime Data Analysis* **5** (1999), 185–192, [10.1023/A:1009605613222](https://doi.org/10.1023/A:1009605613222).
5. *Scheduling servers in a two-stage queue with abandonments and costs.* *Probability in the Engineering and Informational Sciences*, [Cambridge Core article](https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/scheduling-servers-in-a-twostage-queue-with-abandonments-and-costs/07872168CE73AAAD817DD1D255268844).
