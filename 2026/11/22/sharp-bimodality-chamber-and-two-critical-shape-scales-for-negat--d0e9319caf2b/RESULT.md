# Sharp bimodality chamber and two critical shape scales for negative-binomial–logarithmic conflation

## Finding
For the conflation of a negative-binomial and a logarithmic-series count distribution (CNBLD), let the shape be \(r>0\), the probability-product parameter be \(0<\theta<1\), and let its positive-integer probability mass be
\[
p_k=\frac1{Z(r,\theta)}\frac{(r)_k\theta^k}{k!\,k},\qquad k=1,2,\dots,
\]
where \((r)_k=\Gamma(r+k)/\Gamma(r)\) and \(Z(r,\theta)=\sum_{k\ge1}(r)_k\theta^k/(k!k)\in(0,\infty)\). A *local modal component* is a maximal constant-mass block not smaller than its existing neighbors. Define for integers \(j\ge1\)
\[
h_j(r)=\frac{j(j+r)}{(j+1)^2},\qquad
\gamma_j=\frac{2j^2+4j+1}{j^2+j-1}
=2+\frac{2j+3}{j^2+j-1}.
\]
For \(2<r<7\), define \(m(r)=\min\{j\ge1:r\ge\gamma_j\}\) and \(H(r)=h_{m(r)}(r)=\max_{j\ge1}h_j(r)\). The mass function has **exactly two separated local modal components** if and only if
\[
\boxed{2<r<7,\qquad H(r)^{-1}<\theta<\min\left\{1,\frac4{r+1}\right\}.}
\]
These two components are the boundary singleton \(\{1\}\) and one later (possibly two-point) peak. At all other admissible parameters the mass function has only one local modal component. In the strict interior of the displayed chamber, except on the countable plateau curves \(\theta=h_j(r)^{-1}\), the two maxima and the intervening minimum are strict singletons.

For \(2<r<7\) the sharp *global-mode crossover* is
\[
\theta_*(r)=\min_{k\ge2}\left(\frac{k!\,k}{(r+1)_{k-1}}\right)^{1/(k-1)}
\in\left(H(r)^{-1},\min\{1,4/(r+1)\}\right).
\]
The minimum is attained at a finite integer. For \(\theta<\theta_*(r)\), count one is the unique global mode; at \(\theta=\theta_*(r)\) count one ties with a later global mode; and for \(\theta>\theta_*(r)\), every global mode is interior. This statement is in addition to, not a replacement for, the local-mode chamber.

The chamber has two sharply different edge laws. As \(r=2+\varepsilon\downarrow2\), its \(\theta\)-width is \(\varepsilon^2/4+O(\varepsilon^3)\). For any fixed \(0<c<1/4\), putting \(\theta=1-c\varepsilon^2\) gives a first interior local minimum and a later local maximum at count indices
\[
\frac{1-\sqrt{1-4c}}{2c\,\varepsilon}+O(1)
\quad\text{and}\quad
\frac{1+\sqrt{1-4c}}{2c\,\varepsilon}+O(1),
\]
respectively. Near the other endpoint, for \(17/5\le r<7\) the chamber width is exactly \((7-r)/[2(r+1)(r+2)]\sim(7-r)/144\).

A small exact witness is \(r=6\), \(\theta=17/30\), when the three consecutive likelihood ratios are \(119/120<1\), \(136/135>1\), and \(153/160<1\): count one and count three are distinct strict local modes, separated by a strict minimum at count two. At \(r=6\), \(\theta=3/(2\sqrt7)\), these two modes are **equal global maxima**.

## Assumptions and scope
The distribution has full support on positive integers, real shape \(r>0\), and \(0<\theta<1\). The factor \(Z\) makes it a genuine probability mass. The nonstandard notion of a modal *component* accounts for equal adjacent masses at isolated parameter curves; a singleton local mode is strict if both existing neighbors have strictly smaller masses. The modal chamber is stated for CNBLD; the left-shifted SCNBLD inherits it with every modal index reduced by one. No claim is made about the distinct CNBSLD variant or arbitrary mixtures.

## Proof
**1. Exact successive-ratio structure.** Direct cancellation of the Pochhammer and factorial factors gives
\[
\frac{p_{j+1}}{p_j}=\theta h_j(r)
=\theta\frac{j(j+r)}{(j+1)^2}.
\]
The normalization cancels. For every integer \(j\ge1\), exact polynomial simplification gives
\[
h_{j+1}(r)-h_j(r)
=\frac{(2-r)j^2+(4-r)j+(r+1)}{(j+1)^2(j+2)^2}
=\frac{(j^2+j-1)(\gamma_j-r)}{(j+1)^2(j+2)^2}.
\]
Moreover, \(\gamma_1=7\), \(\gamma_j\downarrow2\) strictly, since
\[
\gamma_j-\gamma_{j+1}=\frac{2(j+2)^2}{(j^2+j-1)(j^2+3j+1)}>0.
\]
Also \(h_j(r)-1=((r-2)j-1)/(j+1)^2\). For \(r\le2\), all \(h_j(r)<1\), so every successive mass ratio is below one. For \(r\ge7\), the sequence \((h_j(r))_{j\ge1}\) is nonincreasing, making \((p_j)\) log-concave and hence unimodal. For \(2<r<7\), the sequence \(h_j\) increases up to the finite maximum at \(m(r)\) (possibly tied with \(m(r)+1\) at \(r=\gamma_{m(r)}\)), then decreases to its limit one, strictly from above. In particular \(H(r)>\max\{h_1(r),1\}\), and the superlevel set \(\{j\ge1:\theta h_j(r)>1\}\) is empty or a finite contiguous interval. This exhausts all possible arrangements of upward and downward steps of the mass sequence.

**2. Number of modes, including boundary equalities.** In the middle shape interval the superlevel set is nonempty exactly when \(\theta>1/H(r)\). Since \(h_1(r)=(r+1)/4\), the left endpoint is strictly locally maximal exactly when \(\theta<4/(r+1)\). Together with \(\theta<1\), these inequalities are necessary and sufficient for the mass sequence first to decrease, then to increase, and finally to decrease. The contiguous nature of the ratio superlevel set shows that this gives precisely two separated local modal components. Equalities \(\theta h_j(r)=1\) produce only constant-mass plateaus and never introduce another modal component. If either strict inequality fails, or if \(r\notin(2,7)\), the ratios have no down–up–down pattern, so precisely one local modal component exists. The chamber is nonempty for every \(2<r<7\) because \(H(r)>\max\{1,(r+1)/4\}\).

The exact maximizer is constructive: \(m(r)=\lceil a(r)\rceil\), where
\[
a(r)=\frac{4-r+\sqrt{5r^2-12r+8}}{2(r-2)};
\]
if \(a(r)\) is integer, both indices \(a(r)\) and \(a(r)+1\) maximize \(h_j\). This follows by solving \(r=\gamma_j\) and using strict decrease of \(\gamma_j\).

**3. Global-mode crossover.** The exact ratio to the boundary mass is
\[
\frac{p_k}{p_1}=\theta^{k-1}\frac{(r+1)_{k-1}}{k!\,k},\quad k\ge2.
\]
Consequently, each \(k\ge2\) overtakes count one precisely when \(\theta\) exceeds \(b_k(r)=(k!k/(r+1)_{k-1})^{1/(k-1)}\). Stirling's ratio estimate gives \(b_k(r)\to1\) as \(k\to\infty\). At \(\theta=1/H(r)<1\), the mass sequence strictly drops from count one and never increases, hence every \(b_k(r)>1/H(r)\); since \(b_k\to1>1/H\), their infimum is a minimum, achieved at a finite index, and strictly greater than \(1/H\). To see that it lies below the upper chamber boundary, if \(3<r<7\), at \(\theta=4/(r+1)\), the first mass ratio equals one and the second exceeds one, so \(p_3>p_1\). For \(2<r\le3\), as \(k\to\infty\), the formal \(\theta=1\) ratio \(p_k/p_1=(r+1)_{k-1}/(k!k)\sim k^{r-2}/\Gamma(r+1)\to\infty\); therefore some \(b_k(r)<1\). This establishes the strict position of \(\theta_*(r)\). Comparing all \(p_k/p_1\) to one proves each of the three global-mode regimes without any finite cutoff assumption. At a crossover, the ratio topology above ensures that any later equal-global mode belongs to the unique interior peak component.

**4. Sharp endpoint laws.** For \(r=2+\varepsilon\), treat \(h_x(r)=1+(\varepsilon x-1)/(x+1)^2\) for real \(x\ge1\). Its continuous maximizer is \(x=(2+\varepsilon)/\varepsilon\), with value \(1+\varepsilon^2/[4(1+\varepsilon)]\). The integer maximizer differs by at most one and the second derivative there is \(O(\varepsilon^4)\), hence
\[
H(2+\varepsilon)=1+\varepsilon^2/4+O(\varepsilon^3),
\qquad1-H(2+\varepsilon)^{-1}=\varepsilon^2/4+O(\varepsilon^3).
\]
Since \(r\le3\) near the lower endpoint, the upper \(\theta\) boundary is one, proving the quadratic chamber-width law. For \(\theta=1-c\varepsilon^2\), the equality \(\theta h_x(r)=1\) reduces exactly to
\[
(1-\theta)x^2+(2-r\theta)x+1=0.
\]
Substitute \(x=z/\varepsilon\) and pass to the leading quadratic \(cz^2-z+1=0\), whose two distinct positive roots are \((1\mp\sqrt{1-4c})/(2c)\). Smooth simple-root perturbation gives the two continuous crossing indices \(z_\pm/\varepsilon+O(1)\); rounding to integer local-extremum indices changes them by at most a bounded amount. For \(17/5\le r<7\), the maximum discrete ratio occurs at index two, so \(H(r)=2(r+2)/9\) and the upper bound is \(4/(r+1)\); subtracting gives \((7-r)/[2(r+1)(r+2)]\).

**5. Exact two-peak witness.** At \(r=6\), \(\theta=17/30\), the ratios \(p_2/p_1=119/120\), \(p_3/p_2=136/135\), and \(p_4/p_3=153/160\) are respectively below, above and below one. All later ratios decrease, proving the two strict local maxima at counts one and three. At \(\theta=3/(2\sqrt7)\), the product of the first two ratios is exactly one; both counts therefore share the global maximum. The third and all subsequent ratios are below one, while the first ratio is below one, so no other count ties.

## Verification
Run \(\texttt{python verify.py}\) with the open-source SymPy package installed. The checker verifies the polynomial difference and shape-threshold identities, the end-chamber width, the strict two-peak rational example, and the equal global-peak example in exact arithmetic. Additional exact-rational finite parameter probes check the single-interval structure of positive successive ratios. The infinite assertions—including modal exhaustiveness, finite attainment of the global crossover and both asymptotic laws—are proved above; finite probes are not claimed as exhaustive certificates.

## Relationship to prior work
Alqefari, Alzaid and Qarmalah (2024) defined the CNBLD and its shifted modification, derived the same successive-mass ratio and the \(p_{j+1}^2/(p_jp_{j+2})\) expression, and established log-concavity for \(r\ge7\), log-convexity for \(r\le2\), and a partial tail curvature threshold \(r\ge17/5\) from index two (Theorem 2, Remarks 3–4). These ingredients are prior work and are not claimed to be new. The contribution here is the *complete, sharp two-mode phase chamber* with exceptional plateau handling, an exact boundary-to-interior global-modal crossover, and the distinct critical endpoint scalings; a low shape can create a second count peak that is absent in the Poisson–logarithmic analogue. The 2025 paper by Alzaid, Alqefari and Qarmalah treats the different Poisson–logarithmic conflation, whose Section 3.3 establishes unimodality, not the two-parameter negative-binomial family or its second-mode chamber. General discrete log-concavity and likelihood-ratio concepts alone do not specify the newly exhibited non-log-concave parameter region. The priority comparison is best-knowledge only, not a claim of global uniqueness.

## Limitations
All conclusions concern the exact two-parameter CNBLD probability law on positive integers and its left-shifted version. They do not cover the separate CNBSLD law, other conflations, or observed-data inferential performance and power. The explicit global crossover is an attained minimum over positive integers rather than a uniform elementary closed form; its finite attainment is proved. For certain isolated parameter curves a modal peak consists of two adjacent equal mass values. Neither a Monte Carlo calculation nor a self-review substitutes for independent mathematical validation; no independent audit has been performed. Historical-priority risk remains for publications not found in the stated searches.

## References
1. A. A. Alqefari, A. A. Alzaid, N. Qarmalah, “On the Conflation of Negative Binomial and Logarithmic Distributions,” *Axioms* **13** (2024), 707, first publicly available 2024-10-13, https://doi.org/10.3390/axioms13100707; in particular Section 2 and Theorem 2 and Remarks 3–4 of Section 3.3.
2. A. A. Alzaid, A. A. Alqefari, N. Qarmalah, “On the Conflation of Poisson and Logarithmic Distributions with Applications,” *Axioms* **14** (2025), 518, https://doi.org/10.3390/axioms14070518, in particular Section 3.3 (unimodality of the distinct Poisson conflation).
