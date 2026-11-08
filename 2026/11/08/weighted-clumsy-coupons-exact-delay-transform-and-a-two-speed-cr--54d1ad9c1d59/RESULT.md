# Weighted clumsy coupons: exact delay transform and a two-speed critical law

## Finding

A coupon refresh process with unequal sampling frequencies admits an exact finite first-completion transform and a sharp critical-regime limit. The same transform proves that dispersion in the sampling probabilities strictly increases the mean time to completion.

**Finite theorem.** Fix an integer \(m\ge2\), positive selection probabilities \(q_1,\ldots,q_m\) summing to one, and a common erasure probability \(p\in(0,1)\). At each discrete step one type \(i\) is drawn with probability \(q_i\); that type is set to *present* with probability \(1-p\), or *absent* with probability \(p\), leaving the other types unchanged. Begin with all types absent. Let \(T\) be the first all-present time, let \(C\) be the first time every type has been drawn (ignoring refresh marks), and set \(D=T-C\). Put \(r=p/(1-p)\), \(q(S)=\sum_{i\in S}q_i\), and \(q(\varnothing)=0\).

The variables \(C\) and \(D\) are independent and, for \(0\le z<1\),

\[
\mathbb E z^D=\left[(1-z)\sum_{S\subseteq[m]}\frac{r^{|S|}}{1-z(1-q(S))}\right]^{-1},\qquad
\mathbb ED=\sum_{\varnothing\ne S\subseteq[m]}\frac{r^{|S|}}{q(S)}.
\]

Moreover, for fixed \(m,p\), **both** \(\mathbb E D\) and \(\mathbb E T\) are strictly Schur-convex in the positive vector \((q_1,\ldots,q_m)\): if \(\mathbf q\) majorizes \(\mathbf q'\), then the corresponding means for \(\mathbf q\) are at least those for \(\mathbf q'\), with strict inequality unless the vectors are permutations. Uniform sampling is therefore the unique minimizer of the mean clumsy completion time, up to permutation.

**Two-speed critical theorem.** Fix \(0<\theta<1\), \(c>0\), and positive \(a<b\) with \(\theta a+(1-\theta)b=1\). For each sufficiently large \(m\), divide the types into groups of sizes \(m_1=\lfloor\theta m\rfloor\) and \(m_2=m-m_1\), sample them with probabilities \(a/(m\bar w_m)\) and \(b/(m\bar w_m)\), respectively, where \(\bar w_m=(m_1a+m_2b)/m\), and use \(p_m=c/m\). Write \(T_m,C_m,D_m\) for the corresponding times. Let \(G\) be standard Gumbel and independent of \(\tau\), defined below. Then

\[
\left(\frac{C_m}{m}-\frac{\log m}{a},\frac{D_m}{m}\right)
\Longrightarrow\left(\frac{G+\log\theta}{a},\tau\right),
\qquad
\frac{T_m}{m}-\frac{\log m}{a}\Longrightarrow\frac{G+\log\theta}{a}+\tau.
\]

Here \(\tau\) is the first time that **both** coordinates of a stationary two-class immigration–death process are zero. The independent coordinates start as Poisson variables of means \(C_1=\theta c\) and \(C_2=(1-\theta)c\); their immigration rates are \(\theta ac\) and \((1-\theta)bc\), and the respective death rates at population \(j\) are \(aj\) and \(bj\). For every \(s>0\),

\[
\mathbb E e^{-s\tau}=
\left[s\sum_{j,k\ge0}\frac{C_1^j C_2^k}{j!\,k!\,(s+aj+bk)}\right]^{-1},
\quad
\mathbb E\tau=\sum_{j+k\ge1}\frac{C_1^jC_2^k}{j!\,k!\,(aj+bk)},
\quad
\frac{\mathbb E D_m}{m}\longrightarrow\mathbb E\tau.
\]

There is an atom \(\Pr(\tau=0)=e^{-c}\). With the normalization above, unequal rates incur the **strict critical-delay penalty**

\[
\mathbb E\tau>
\sum_{h\ge1}\frac{c^h}{h!\,h},
\]

where the right side is the mean delay for the equal-rate model at the same parameter \(c\).

## Assumptions and scope

All selection probabilities are fixed, strictly positive and sum to one in the finite theorem. The erasure mark is independent from draw to draw, has the same probability \(p\) for every type, and replaces rather than adds to the chosen type's state. Completion is checked after each update. The two-speed theorem keeps \(a,b,c,\theta\) fixed as \(m\to\infty\), with \(a<b\); it does not cover rates tending together, vanishing type masses, or a growing number of speed classes. The conditional-independent components of the limiting queue start in their **stationary** distributions, not from an empty queue.

A vector \(\mathbf q\) *majorizes* \(\mathbf q'\) when the sums of its \(j\) largest entries exceed those of \(\mathbf q'\) for each \(j<m\), and both vectors have total sum one. The strictness assertion concerns pairs not related by permutation.

## Proof

**1. Exact independence at ordinary cover.** Conditional on the entire type-selection history up to \(C\), the last refresh mark for each distinct type is an independent Bernoulli mark with failure probability \(p\). These marks are attached to distinct draw indices, so their joint law is the product law and is independent of the selection history. Future type draws and refresh marks are independent of the history at the stopping time \(C\). Thus the law of the residual time \(D\), conditional on \(C\) or its selection history, is the hitting time of the all-present state for a chain begun from its stationary product Bernoulli\((1-p)\) law. This law does not depend on \(C\), proving independence.

**2. Exact resolvent.** Start the refresh chain instead from all present, and denote by \(P_{00}(n)\) its probability of being all present at time \(n\). After \(n\) draws, let \(U\) be the set of types never selected. Conditional on the selected types, their last marks are independent, so the all-present probability equals \((1-p)^{m-|U|}\). Expanding

\[
(1-p)^{m-|U|}=(1-p)^m\sum_{S\subseteq U}r^{|S|}
\]

and using \(\Pr(S\subseteq U)=(1-q(S))^n\) gives

\[
P_{00}(n)=(1-p)^m\sum_{S\subseteq[m]}r^{|S|}(1-q(S))^n.
\]

The same chain started in equilibrium has all-present probability \((1-p)^m\) at every time. By the strong Markov property at the first all-present hitting time \(D\),

\[
\frac{(1-p)^m}{1-z}=
\mathbb E z^D\sum_{n\ge0}z^nP_{00}(n).
\]

Summing the geometric series and canceling the stationary mass proves the probability-generating function. Its first derivative at \(z\uparrow1\) gives the displayed mean: the empty-set contribution is \(1/(1-z)\), while every other subset has positive \(q(S)\).

**3. Strict mean comparison.** Write \(w_i=mq_i\), so the positive weights have mean one. Using \(1/x=\int_0^\infty e^{-xt}\,dt\), the last formula and the classical Poissonized cover-time identity give exactly

\[
\begin{aligned}
\mathbb ED&=m\int_0^\infty\left[\prod_{i=1}^m(1+r e^{-w_i t})-1\right]dt,\\
\mathbb EC&=m\int_0^\infty\left[1-\prod_{i=1}^m(1-e^{-w_i t})\right]dt.
\end{aligned}
\]

For every \(t>0\), the map \(w\mapsto\log(1+r e^{-wt})\) has strictly positive second derivative, while \(w\mapsto\log(1-e^{-wt})\) has strictly negative second derivative. Karamata's inequality therefore makes the first product strictly increase and the second strictly decrease under a strict majorization of the weight vector. Integrating yields the stated strict Schur-convexity of each expected time, and hence of their sum.

**4. The weighted ordinary-cover limit.** In a unit-rate Poissonization, the type counts are independent Poisson processes of rates \(a/(m\bar w_m)\) and \(b/(m\bar w_m)\). The probability that all types are seen by time \(t\) is therefore

\[
\bigl(1-e^{-a t/(m\bar w_m)}\bigr)^{m_1}
\bigl(1-e^{-b t/(m\bar w_m)}\bigr)^{m_2}.
\]

At \(t=(m/a)(\log m+x)\), the first factor tends to \(\exp(-\theta e^{-x})\), and the second tends to one because \(b/a>1\). This is the law of \((G+\log\theta)/a\). Uniformly positive rescaled sampling rates imply \(C_m=O_{\mathbb P}(m\log m)\). The centered sum of the first \(C_m\) independent mean-one exponential interarrival times is \(o_{\mathbb P}(m)\); hence de-Poissonization transfers the weak limit to the discrete ordinary cover time.

**5. Delay transform and mean limit.** The exact finite resolvent for the two classes compresses to

\[
\mathbb E z^{D_m}=
\left[(1-z)\sum_{j=0}^{m_1}\sum_{k=0}^{m_2}
\frac{\binom{m_1}{j}\binom{m_2}{k}r_m^{j+k}}
{1-z[1-(aj+bk)/(m\bar w_m)]}\right]^{-1},
\qquad r_m=\frac{c}{m-c}.
\]

For \(z=e^{-s/m}\), the empty term contributes one after multiplication by \(1-z\); every fixed nonempty \((j,k)\) contributes in the limit

\[
\frac{C_1^jC_2^k}{j!k!}\frac{s}{s+aj+bk}.
\]

For all sufficiently large \(m\), the binomial coefficients times \(r_m\)-powers are bounded by \((2c)^{j+k}/(j!k!)\), and the fraction is at most one. Dominated convergence for the absolutely summable double series proves the stated limiting Laplace transform. Likewise,

\[
\frac{\mathbb E D_m}{m}
=\bar w_m\sum_{j+k\ge1}
\frac{\binom{m_1}{j}\binom{m_2}{k}r_m^{j+k}}{aj+bk}
\longrightarrow
\sum_{j+k\ge1}\frac{C_1^jC_2^k}{j!k!(aj+bk)},
\]

using \(aj+bk\ge\min(a,b)(j+k)\) for domination. Terms with binomial indices beyond group sizes are understood as zero.

**6. Identification as an immigration–death hitting time.** The independent equilibrium immigration–death coordinates have the stationary Poisson laws stated above. From the all-zero state, the chance of returning to that state at time \(t\) is

\[
P_{00}(t)=\exp\{-c+C_1e^{-at}+C_2e^{-bt}\}.
\]

Stationarity and the strong Markov property at the first time \(\tau\) of reaching zero give, for \(s>0\),

\[
\frac{e^{-c}}s
=\mathbb E e^{-s\tau}\int_0^\infty e^{-st}P_{00}(t)\,dt.
\]

Expanding the exponential in the integral yields the same Laplace transform as in step 5. Thus \(D_m/m\Rightarrow\tau\) by uniqueness of Laplace transforms for nonnegative random variables. Exact finite independence from step 1 gives the claimed independent joint limit and hence the sum law. The stationary all-zero probability yields \(\Pr(\tau=0)=e^{-c}\).

**7. Strict limiting heterogeneity penalty.** Tonelli's theorem converts the mean series into

\[
\mathbb E\tau=\int_0^\infty
\left[\exp\{c(\theta e^{-at}+(1-\theta)e^{-bt})\}-1\right]dt.
\]

Since \(\theta a+(1-\theta)b=1\) and \(a\ne b\), strict convexity of the exponential implies \(\theta e^{-at}+(1-\theta)e^{-bt}>e^{-t}\) for every \(t>0\). Integrating the strict inequality proves \(\mathbb E\tau>\int_0^\infty(e^{ce^{-t}}-1)dt=\sum_{h\ge1}c^h/(h!h)\).

## Verification

The accompanying `verify.py` is a standalone Python 3 script using only the standard library. It performs exact-rational transition normalization and detailed-balance checks, independently solves small absorbing Markov systems for both the finite delay generating function and its mean, checks the all-present return-kernel spectral expression against brute-force state evolution, compares exact cover-time expectations under increasingly unequal rates, and cross-checks the limiting mean and Laplace transform via independently evaluated integral/series expressions. It also evaluates Poissonized cover CDFs on increasing finite sizes. Running `python3 verify.py` gave **1,168 passed deterministic checks**. These computations are finite consistency tests only; the infinite claims are supported by the preceding analytic proof.

## Relationship to prior work

Attrill and Garoni (2026), Theorem 4.10 and Lemma 4.2, derive the critical Gumbel-plus-single-rate immigration–death law and the independent cover/delay decomposition for **uniform** coupon sampling. The result above generalizes the sampling probabilities, determines an exact arbitrary-weight delay resolvent, identifies strict selection-rate dispersion costs, and derives the distinct two-speed critical law with its stationary two-dimensional queue.

Long (2026) treats the uniform clumsy refresh model with fixed erasure probability. His unequal-probability Section 3.6 instead concerns the **global reset-button collector**, a different transition mechanism. Anceaume, Busnel and Sericola (2014) prove uniform optimality for the **monotone** unequal-probability coupon collector; that case supplies the ordinary-cover component but has no post-cover erasure delay. Makowski (2001) establishes classical infinite-server busy-period formulas and convex-order comparisons, relevant to interpreting the limiting queue but not a weighted-coupon critical limit. The queue return-resolvent idea and the usual ordinary coupon Gumbel theory are not claimed as independently new.

## Limitations

The new limit is for exactly two fixed positive speed classes and common per-update erasure probability \(p_m=c/m\). It asserts weak convergence and convergence of the **post-cover delay's mean**, but does not assert convergence of centered full completion-time moments or a rate of weak convergence. The strict finite Schur-convexity concerns **expected** completion times, not stochastic domination of full laws. No claim is made about heterogeneous erasure probabilities, global reset dynamics, a growing range of rates, or historical uniqueness: a more general existing heat-bath or infinite-server result could subsume some individual identities. The comparison with published work remains subject to independent historical verification.

## References

1. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem* (2026), arXiv:2605.14206v1, first public 2026-05-14. https://arxiv.org/abs/2605.14206
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors* (2026), arXiv:2605.14511v1. https://arxiv.org/abs/2605.14511
3. E. Anceaume, Y. Busnel and B. Sericola, *New results on a generalized coupon collector problem using Markov chains* (2014), arXiv:1402.5245. https://arxiv.org/abs/1402.5245
4. A. M. Makowski, *On a Random Sum Formula for the Busy Period of the M/G/Infinity Queue with Applications* (2001), University of Maryland technical report TR 2001-9. https://drum.lib.umd.edu/items/4970634d-7eae-44b1-ae43-175f19c6ce6d
