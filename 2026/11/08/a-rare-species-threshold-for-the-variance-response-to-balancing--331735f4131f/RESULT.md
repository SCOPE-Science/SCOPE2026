# A rare-species threshold for the variance response to balancing common species

## Finding
Let \(T_{\boldsymbol p}\) be the number of independent with-replacement observations required to detect every species in a three-species community with positive probabilities \(\boldsymbol p\). Fix the rare species probability \(0<a<1/3\) and redistribute the remaining probability between two more common species:
\[
\boldsymbol p(a,\delta)=\left(a,\frac{1-a}{2}+\delta,\frac{1-a}{2}-\delta\right),\quad |\delta|<\frac{1-3a}{2}.
\]
Write \(V_a(\delta)=\operatorname{Var}(T_{\boldsymbol p(a,\delta)})\). Define
\[
Q(a)=3a^5-12a^4+56a^3-38a^2+45a-6.
\]
There is a **unique** \(a_*\in(0,1/3)\) satisfying \(Q(a_*)=0\), with \(0.147<a_*<0.148\) and \(a_*\approx0.147902267275574\). Then the configuration with equal common-species probabilities, \(\delta=0\), is a strict local **maximum** of completion-time variance for \(a<a_*\), and a strict local **minimum** for \(a>a_*\). At \(a=a_*\), it remains a strict local minimum, but its quadratic response vanishes and the first nonzero variation is positive and quartic. More precisely,
\[
V_a(\delta)-V_a(0)=\frac{32Q(a)}{(1-a^2)^4}\,\delta^2+O_a(\delta^4).
\]
For every fixed \(a\in(0,1/3)\), balancing the two common species strictly improves the entire completion-time tail: for \(0\le |\delta_1|<|\delta_2|<(1-3a)/2\),
\[
\Pr\{T_{\boldsymbol p(a,\delta_1)}>n\}<\Pr\{T_{\boldsymbol p(a,\delta_2)}>n\}\qquad(n\ge3),
\]
with equality for \(n=0,1,2\). Thus, below \(a_*\), improving *every* nontrivial completion probability can locally **increase** the variance. Three species are the smallest possible number for this behavior.

For an exact illustration, the balanced-common-species community \(\boldsymbol q=(1/12,11/24,11/24)\) is strictly faster than \(\boldsymbol p=(1/12,5/12,1/2)\) in the above tail order, but
\[
\mathbb E[T_{\boldsymbol p}]-\mathbb E[T_{\boldsymbol q}]=\frac{72}{5005}>0,\qquad
\operatorname{Var}(T_{\boldsymbol q})-\operatorname{Var}(T_{\boldsymbol p})=\frac{3564216}{25050025}>0.
\]

## Assumptions and scope
A closed community contains exactly three detectable species; each observation independently returns one species with constant positive probability. Detection is perfect, sampling is with replacement, and observations continue until all species have been seen at least once. The strict local assertions concern perturbations of the *two common-species probabilities* at fixed rare-species probability \(a\), not arbitrary perturbations of all coordinates. The local statements hold for every real \(a\) in the specified open interval and sufficiently small nonzero real \(\delta\) satisfying the displayed positivity and rarity constraint. The tail comparison holds over its entire displayed range.

## Proof
**Moment identities.** For any positive species probability vector \(\boldsymbol p=(p_1,\ldots,p_m)\), put \(q_S=\sum_{i\in S}p_i\). Inclusion-exclusion for the event that at least one species remains unobserved after \(n\) draws gives
\[
\Pr(T_{\boldsymbol p}>n)=\sum_{\varnothing\ne S\subseteq[m]}(-1)^{|S|+1}(1-q_S)^n\qquad(n\ge0),
\]
with the standard convention \(0^0=1\) at \(n=0\). The nonnegative-integer tail identities \(\mathbb E T=\sum_{n\ge0}\Pr(T>n)\) and \(\mathbb E T^2=\sum_{n\ge0}(2n+1)\Pr(T>n)\) yield, by convergent geometric sums,
\[
M_1(\boldsymbol p)=\sum_{S\ne\varnothing}(-1)^{|S|+1}\frac1{q_S},\qquad
M_2(\boldsymbol p)=\sum_{S\ne\varnothing}(-1)^{|S|+1}\frac{2-q_S}{q_S^2},\qquad
V=M_2-M_1^2.
\]
These are exact rational functions of positive \(p_i\).

**Local curvature and critical threshold.** Fix \(a\in(0,1/3)\), let \(b+c=1-a\), and set \(t=bc\), \(t_0=(1-a)^2/4\). Because the preceding rational expression is symmetric in \(b,c\), it is a rational function \(W(a,t)\); at the balanced point \(t=t_0\), direct differentiation of those displayed finite sums and simplification give
\[
\left.\frac{\partial W}{\partial t}\right|_{t=t_0}=-\frac{32Q(a)}{(1-a^2)^4}.
\]
As \(t=t_0-\delta^2\), Taylor's theorem gives the claimed coefficient. The polynomial derivative is
\[
Q'(a)=15a^4-48a^3+168a^2-76a+45
\ge45-\frac{48}{27}-\frac{76}{3}>0
\]
for \(0<a<1/3\), while \(Q(0)=-6\) and \(Q(1/3)=544/81\). Hence exactly one root exists and the curvature changes sign there. The explicit rational evaluations \(Q(147/1000)<0<Q(148/1000)\) isolate it.

To settle the *degenerate* point \(a=a_*\), define
\[
R(a)=3a^7-20a^6+149a^5-170a^4+405a^3-152a^2+115a-10.
\]
A further derivative of the same rational moment expression gives
\[
\left.\frac{\partial^2W}{\partial t^2}\right|_{t=t_0}=\frac{256R(a)}{(1-a^2)^6}.
\]
For \(147/1000\le a\le148/1000\), discarding positive terms and bounding the negative ones implies
\[
R(a)\ge115\frac{147}{1000}-10-152\left(\frac{148}{1000}\right)^2-170\left(\frac{148}{1000}\right)^4-20\left(\frac{148}{1000}\right)^6>3.
\]
Therefore, at \(a=a_*\), the quadratic coefficient vanishes and
\[
V_{a_*}(\delta)-V_{a_*}(0)=\frac{128R(a_*)}{(1-a_*^2)^6}\,\delta^4+O(\delta^6)>0
\]
for all sufficiently small nonzero \(\delta\). This completes all three strict local cases.

**Stochastic order and the sharp species threshold.** Fix the rare probability \(a\). For each observation, first distinguish a rare-species draw (probability \(a\)) from a common-group draw (probability \(1-a\)); conditional on a common-group draw, its two species have conditional probabilities \(r=1/2+\delta/(1-a)\) and \(1-r\). Given \(k\ge2\) common-group draws, the probability that *both* common species have appeared equals \(1-r^k-(1-r)^k\), strictly increasing as \(|\delta|\) decreases. Conditional on the rare/common-group indicators for \(n\ge3\) draws, this yields the claimed strict completion-time tail comparison, because the event that at least one rare draw and at least two common-group draws occur has positive probability. Completion before the third draw is impossible, proving the equality cases. The exact witness follows by substituting its rational probability vectors into \(M_1\) and \(V\).

For one species the completion time is constant. For two species write \(z=p_1p_2\), \(0<z\le1/4\). The moment formula simplifies to
\[
\operatorname{Var}(T)=z^{-2}-3z^{-1}-2,
\quad\frac{d}{dz}\operatorname{Var}(T)=\frac{-2+3z}{z^3}<0.
\]
Balancing two probabilities increases \(z\), so no variance-increasing balancing is possible with two species. The three-species effect is therefore minimal.

## Verification
The accompanying `verify.py` recomputes the moment formulas independently by inclusion-exclusion and a finite-state geometric-waiting recursion, reproduces the displayed rational mean and variance gaps, symbolically verifies the quadratic polynomial identity, and proves the quartic identity modulo the critical polynomial. It also checks exact rational endpoint signs and the positivity bound for the degenerate quartic coefficient. Run `python verify.py` with Python 3.10+ and SymPy 1.12+; the expected terminal marker is `VERIFICATION_PASS`. The code checks identities, not a statistical simulation, and the mathematical inequalities in the proof establish all continuum claims.

## Relationship to prior work
Anceaume, Busnel and Sericola (2014 preprint) derive completion-time distributions, moments and uniform minimization. Zoroa and collaborators (2016 preprint) develop the unequal-probability ecological occupancy model and its majorization-based speed comparison; its fixed-sample richness variance differs from the variance of the stopping time studied here. Yu (2017) proves the uniform distribution minimizes completion-time variance. Long (2026), §7.5, extends minimum-variance results radially, and §7.6 *explicitly notes that pairwise variance smoothing can fail*; this qualitative non-Schur-convexity fact is **not** claimed as new. The present contribution is the exact unique rare-species threshold, its quadratic-to-quartic transition and sharp three-species interpretation in a fixed-rare-frequency ecological comparison. Neither the global minimum at uniform probabilities nor failure of pairwise smoothing in general implies the stated quintic transition.

## Limitations
The result is local in the imbalance parameter, except for the stochastic tail order and displayed rational witness. It does not classify all global extrema for arbitrary three-species probabilities, cover imperfect detection, or establish a new general coupon-collector variance minimization theorem. Historical priority for the precise threshold requires independent literature review; Yu's brief 2017 note was not available in full text through the inspected sources, although its global-minimum theorem is independently discussed and reproved in the fully inspected relevant parts of Long (2026). No independent mathematical audit is asserted.

## References
- E. Anceaume, Y. Busnel and B. Sericola, “New results on a generalized coupon collector problem using Markov chains,” first public preprint 2014-02-21, [arXiv:1402.5245v1](https://arxiv.org/html/1402.5245v1).
- N. Zoroa, E. Lesigne, M.-J. Fernández-Sáez, P. Zoroa and J. Casas, “The coupon collector urn model with unequal probabilities in ecology and evolution,” first public preprint 2016-07-30, [arXiv:1608.00155](https://arxiv.org/abs/1608.00155).
- Y. Yu, “Minimum variance in the coupon collector's problem,” *Journal of Applied Probability* 54 (2017), 655–656, [doi:10.1017/jpr.2017.23](https://doi.org/10.1017/jpr.2017.23).
- C. D. Long, “Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem,” first public 2026-04-28, [arXiv:2604.25108v2](https://arxiv.org/html/2604.25108v2), particularly §§7.5–7.6.
