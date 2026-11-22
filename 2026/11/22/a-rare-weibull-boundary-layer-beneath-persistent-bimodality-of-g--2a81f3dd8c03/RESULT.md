# A rare Weibull boundary layer beneath persistent bimodality of Gumbel block maxima

## Finding
For a fixed exponent \(p>1\), parameter \(\mu\in\mathbb R\), and \(\sigma>0\), let \(X_1,X_2,\ldots\) be independent with the invertible bimodal Gumbel distribution of Otiniano et al. (2023), written
\[
F(x)=\exp\left\{-\exp\left[-\frac{x|x|^{p-1}+\mu}{\sigma}\right]\right\},\qquad x\in\mathbb R.
\]
Let \(M_n=\max_{1\le j\le n}X_j\), \(c_n=n e^{-\mu/\sigma}\), and \(k=(p-1)/p\). Then the following single block-maximum structure holds.

1. **Exact closure and persistent two-mode density.** The maximum has the same family of distributions with \(\mu\) replaced by \(\mu-\sigma\log n\). For every integer \(n\ge1\), its continuous density has exactly two strict local maxima, one negative and one positive, with a strict intervening zero at the origin.
2. **Exponentially rare lower lobe.** Its entire negative branch has probability
   \[
   \Pr(M_n<0)=e^{-c_n}.
   \]
   Conditional on this event, the rescaled negative maximum
   \[
   W_n=\left(\frac{c_n}{\sigma}\right)^{1/p}(-M_n)
   \]
   has the exact survival function
   \[
   \Pr(W_n>t\mid M_n<0)=\exp\left[-c_n\bigl(e^{t^p/c_n}-1\bigr)\right],\quad t\ge0.
   \]
   It increases in stochastic order with \(n\) to a \(\operatorname{Weibull}(p)\) law with survival \(e^{-t^p}\), and admits the exact monotone coupling \(W_n=[c_n\log(1+E/c_n)]^{1/p}\), with a common \(E\sim\operatorname{Exp}(1)\).
3. **Sharp peak separation.** Let \(x_n^-<0<x_n^+\) be the two density modes and set \(b_n=\sigma\log c_n\). As \(n\to\infty\),
   \[
   x_n^-=-\left(\frac{\sigma k}{c_n}\right)^{1/p}\left[1+O(c_n^{-1})\right],\qquad
   (x_n^+)^p=b_n+\frac{\sigma^2 k}{b_n}+O(b_n^{-2}).
   \]
   Their density heights satisfy
   \[
   f_{M_n}(x_n^-)\sim\frac{p}{\sigma}(\sigma k)^k e^{-k} c_n^{1/p}e^{-c_n},\qquad
   f_{M_n}(x_n^+)\sim\frac{p}{e\sigma}b_n^k.
   \]
   Thus the negative local mode persists for *every* block size but has exponentially disappearing mass and height, while the positive local mode diverges at the powered-logarithmic scale. The right mode eventually becomes the unique global mode.

## Assumptions and scope
The claims hold for **every** real \(p>1\), \(\mu\in\mathbb R\), \(\sigma>0\), and integer \(n\ge1\), with all asymptotics taken as \(n\to\infty\) for fixed parameters. The original model's notation is \(p=1+\delta\) with \(\delta>0\). The distribution is continuous on the entire real line; \(M_n<0\) has positive probability at every finite sample size, so its conditional law is well-defined. \(\operatorname{Weibull}(p)\) means the distribution on \([0,\infty)\) whose survival is \(e^{-t^p}\). The little-oh / big-oh constants may depend on the fixed model parameters. We distinguish the existence of a *local density mode* from that mode's probability mass.

## Proof
**Maximum closure and rare-event law.** Write \(h(x)=x|x|^{p-1}\), a strictly increasing bijection on \(\mathbb R\). Taking the \(n\)-th power of the given distribution yields
\[
F_{M_n}(x)=\exp\left[-c_n e^{-h(x)/\sigma}\right]
=\exp\left\{-\exp\left[-\frac{h(x)+\mu-\sigma\log n}{\sigma}\right]\right\}.
\]
At zero, \(h(0)=0\), so \(F_{M_n}(0)=e^{-c_n}\), proving the exact negative-branch mass. For \(r>0\), \(h(-r)=-r^p\), whence
\[
\Pr(M_n<-r)=\exp[-c_n e^{r^p/\sigma}].
\]
Divide by \(\Pr(M_n<0)\), take \(r=(\sigma/c_n)^{1/p}t\), and obtain the displayed exact conditional survival. Let \(E\) have a unit exponential law. The event
\[
[c_n\log(1+E/c_n)]^{1/p}>t
\]
is equivalent to \(E>c_n(e^{t^p/c_n}-1)\), proving the coupling identity. For every fixed \(E>0\), the function \(c\mapsto c\log(1+E/c)\) is strictly increasing (its derivative is \(\log(1+u)-u/(1+u)>0\), where \(u=E/c>0\)) and tends to \(E\). Since \(c_n\uparrow\infty\), the coupled \(W_n\) increase almost surely to \(E^{1/p}\); hence they increase in stochastic order to the stated Weibull law. An explicit first-order conditional-tail correction follows for every fixed \(t\ge0\):
\[
\Pr(W_n>t\mid M_n<0)=e^{-t^p}\left[1-\frac{t^{2p}}{2c_n}+O(c_n^{-2})\right].
\]

**Exactly two modes.** Differentiate the maximum CDF away from zero. For \(x>0\) and \(z=x^p\), the density is
\[
f_{M_n}(x)=\frac p\sigma z^k c_n e^{-z/\sigma}\exp[-c_n e^{-z/\sigma}],
\]
whereas for \(x<0\) and \(z=(-x)^p\) it is
\[
f_{M_n}(x)=\frac p\sigma z^k c_n e^{z/\sigma}\exp[-c_n e^{z/\sigma}].
\]
Both vanish as \(x\to0\) because \(k>0\), and vanish at the respective infinite ends. Logarithmic differentiation with respect to \(z>0\) gives two strictly decreasing functions,
\[
D_-(z)=\frac{k}{z}+\frac{1-c_n e^{z/\sigma}}\sigma,
\qquad D_+(z)=\frac{k}{z}+\frac{c_n e^{-z/\sigma}-1}\sigma,
\]
with derivatives
\[
D_-'(z)=-\frac{k}{z^2}-\frac{c_n e^{z/\sigma}}{\sigma^2}<0,
\qquad D_+'(z)=-\frac{k}{z^2}-\frac{c_n e^{-z/\sigma}}{\sigma^2}<0.
\]
Each derivative score decreases from positive infinity at zero to a strictly negative value at infinity, giving exactly one positive root in each branch. The density rises and falls once on each open half-line, proving exactly two strict modes.

**Sharp locations.** Let \(z_n^-=(-x_n^-)^p\). Its exact equation is
\[
c_n e^{z_n^-/\sigma}=1+\frac{\sigma k}{z_n^-}.
\]
Define \(t_n=c_n z_n^-/\sigma\). Then \(t_n e^{t_n/c_n}=k+t_n/c_n\). For \(c_n>1\), this implies \(0<t_n\le k/(1-1/c_n)\), and the implicit-function theorem at \((t,1/c)=(k,0)\) gives \(t_n=k+O(c_n^{-1})\). This yields the stated negative mode position for every fixed positive \(k\).

For \(z_n^+=(x_n^+)^p\), its equation is
\[
c_n e^{-z_n^+/\sigma}=1-\frac{\sigma k}{z_n^+}.
\]
For large \(n\), this forces \(z_n^+>b_n=\sigma\log c_n\to\infty\). Taking logarithms gives
\[
z_n^+-b_n=-\sigma\log\left(1-\frac{\sigma k}{z_n^+}\right)
=\frac{\sigma^2k}{z_n^+}+O((z_n^+)^{-2}).
\]
Consequently \(z_n^+=b_n+\sigma^2k/b_n+O(b_n^{-2})\), as claimed.

**Sharp heights and global mode.** Insert \(z_n^-=\sigma k/c_n[1+O(c_n^{-1})]\) into the negative density. Because \(c_n e^{z_n^-/\sigma}=c_n+k+O(c_n^{-1})\), one obtains
\[
f_{M_n}(x_n^-)=\frac p\sigma(\sigma k)^k c_n^{1-k}e^{-k-c_n}[1+O(c_n^{-1})].
\]
Since \(1-k=1/p\), this is the asserted negative-peak equivalent. At the positive root, \(c_n e^{-z_n^+/\sigma}=1+O(b_n^{-1})\) and \(z_n^+\sim b_n\), so its density is asymptotic to \((p/(e\sigma))b_n^k\). The ratio of the negative height to the positive height tends to zero. Since these are the only two local maxima and both tails vanish, the positive one is the unique global maximum for all sufficiently large \(n\).

**Usual, unconditioned extreme law (context).** The increasing transform \(h(M_n)\) has, for every \(n\), the exact distribution \(b_n+\sigma G\), where \(G\) is standard Gumbel with CDF \(e^{-e^{-t}}\). For \(b_n>0\), a one-variable Taylor expansion therefore gives
\[
\frac{M_n-b_n^{1/p}}{(\sigma/p)b_n^{1/p-1}}\ \Rightarrow\ G.
\]
The Weibull limit above is explicitly *conditional on an exponentially rare event*, not a claim that the unconditional block maximum has a Weibull limit. The distinction is essential.

## Verification
The included `verify.py` is a standalone Python 3 checker requiring SymPy. It performs symbolic differentiations of the two log-density profiles, verifies the exact exponential coupling and its expansion, and checks the semigroup identity and the sharp-mode approximations for twelve specified parameter/sample-size combinations, including large sample sizes. All universality and asymptotic assertions are established by the analytic argument in the Proof section; finite numerical tests alone do not certify them. Reproduction: `python verify.py`.

## Relationship to prior work
Otiniano, Silva, Matsushita and Silva (2023) introduced precisely this CDF and density (their equations (4)–(5)), showed graphically that the density is bimodal when the power exponent exceeds one, and gave an implicit equation for its modes (their equation (6)). Those ingredients and the elementary CDF power operation are **prior work**, not claimed as novel. The assessed finding is the *sharp rare-branch law for block maxima*: an exact conditional exponential coupling, monotone Weibull boundary layer, explicit exponential extinction probability, and simultaneous modal location and height asymptotics. These statements are not supplied by the original implicit single-sample mode equation alone without the sample-maximum conditioning and asymptotic analysis.

The revised bimodal GEV of Otiniano et al. (2025) and the BGEV regression work of Otiniano et al. (2026) study different transformed GEV parameterizations; their general transformations and block-maxima discussion overlap in motivation but do not provide the indicated rare-negative-lobe conditional law or sharp modal asymptotics for the **fixed original 2023 CDF**. The earlier 2023 bimodal Gumbel model of Otiniano et al. has a different noninvertible CDF construction and does not furnish these same formulas. Standard extreme-value theory explains the ordinary Gumbel limit and is explicitly acknowledged; it does not itself state the specific exponentially rare conditional Weibull boundary layer and the persistent-but-vanishing second local mode.

## Limitations
This result applies to independent observations from the *original* 2023 invertible bimodal Gumbel CDF with fixed \(p>1\); it does not claim to apply to a broader generalized extreme-value family, dependent observations, or changing parameters. The strictly two-mode statement uses \(p>1\) essentially; at \(p=1\) the zero-density valley disappears. The right positive mode's global dominance is asymptotic, not asserted for each finite sample size. There is no assertion of independent mathematical certification or exhaustive historical-priority certainty. Conditional Weibull behavior concerns increasingly rare negative block maxima; it must not be misinterpreted as a typical sample maximum.

## References
1. C. G. Otiniano, E. B. Silva, R. Y. Matsushita, A. Silva, “Bridging Extremes: The Invertible Bimodal Gumbel Distribution,” *Entropy* **25** (2023), article 1598. Publicly published 29 November 2023. DOI: https://doi.org/10.3390/e25121598. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10742741/.
2. C. E. G. Otiniano, M. N. S. Lisboa, T. K. A. Ribeiro, “A Revised Bimodal Generalized Extreme Value Distribution: Theory and Climate Data Application,” *Entropy* **27** (2025), article 749. DOI: https://doi.org/10.3390/e27070749.
3. C. E. G. Otiniano, M. N. S. Lisboa, T. K. A. Ribeiro, J. B. Fachini-Gomes, “A regression-type model for bimodal extreme-valued data,” *TEST* **35** (2026), pp. 498–534. DOI: https://doi.org/10.1007/s11749-026-01005-y.
4. C. Otiniano, R. Vila, P. Brom, M. Bourguignon, “On the Bimodal Gumbel Model with Application to Environmental Data,” *Austrian Journal of Statistics* **52** (2023), pp. 45–65. DOI: https://doi.org/10.17713/ajs.v52i2.1392.
5. L. de Haan, A. Ferreira, *Extreme Value Theory: An Introduction*, Springer, 2006 (background on the ordinary Gumbel domain).
