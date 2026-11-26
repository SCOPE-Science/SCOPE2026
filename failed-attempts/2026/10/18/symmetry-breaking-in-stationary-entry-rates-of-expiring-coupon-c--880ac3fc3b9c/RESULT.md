# Symmetry breaking in stationary entry rates of expiring coupon collectors

## Finding

For independent coupons drawn from an arbitrary positive probability vector, maximize the stationary rate of **new entrances** into simultaneous coverage of every coupon type after deterministic expiration. The optimization differs fundamentally from maximizing the fraction of time with complete coverage.

For two types, write the draw probabilities as \(p\) and \(q=1-p\), and retain only the last \(M\ge2\) draws. Let \(\mu_M(p)\) be the stationary probability that the old length-\(M\) window lacked a type and the new length-\(M\) window contains both. Then
\[
\mu_M(p)=p q^M+q p^M.
\]
For \(M=2,3\), the unique global maximizer is \(p=1/2\). For **every integer \(M\ge4\)**, the balanced law is instead a strict local minimum, and exactly two global maximizers exist. They are \(p_M\) and \(1-p_M\), where \(p_M=r_M/(1+r_M)<1/2\) and \(r_M\in(0,1)\) is the unique root in that interval of
\[
1-Mr+Mr^{M-1}-r^M=0.
\]
For \(M=4\), the maximizers are \(p=(1\pm1/\sqrt3)/2\) and the maximum flux equals \(1/12\), compared with \(1/16\) at balance. As \(M\to\infty\),
\[
p_M=\frac1{M+1}+O\bigl((2/M)^{M-1}\bigr),\qquad
\max_{p\in[0,1]}\mu_M(p)\sim\frac1{eM},\qquad
\mu_M(1/2)=2^{-M}.
\]
Thus the ratio of optimal to balanced entry rates is asymptotic to \(2^M/(eM)\).

This inversion is not restricted to two types. For each fixed number \(n\ge2\) of coupon types and \(M\to\infty\), the deliberately imbalanced vector
\[
p_1=1-\frac{n-1}{M},\qquad p_2=\cdots=p_n=\frac1M
\]
satisfies
\[
\mu_{n,M}(\boldsymbol p)\sim
\frac{(n-1)e^{-1}(1-e^{-1})^{n-2}}{M},
\]
whereas uniform draws give \(\mu_{n,M}(\boldsymbol u)\sim((n-1)/n)^M\). Therefore uniform draws fail to maximize the stationary new-entry rate for every fixed \(n\ge2\) once \(M\) is sufficiently large. No assertion is made that the displayed imbalanced vector is globally optimal for \(n\ge3\).

## Assumptions and scope

Let \(n\ge2\), \(M\ge n\) be integers. Let \((X_t)_{t\in\mathbb Z}\) be independent and identically distributed with \(\Pr(X_t=i)=p_i>0\) for \(1\le i\le n\), \(\sum_i p_i=1\). Define \(W_t=(X_{t-M+1},\ldots,X_t)\) and let \(A\) be the set of windows containing each of the \(n\) coupon types. The stationary entrance intensity is
\[
\mu_{n,M}(\boldsymbol p)=\Pr(W_{t-1}\notin A,\ W_t\in A).
\]
The two-type optimization uses all \(p\in[0,1]\) for compactness; both maximizers lie in \((0,1)\). Limits with \(M\to\infty\) hold with \(n\) fixed. The quantity optimized is **stationary entrance intensity**, not the expected first completion time from an empty collection.

## Proof

**Exact weighted entrance identity.** The departing symbol is \(X_{t-M}\), the entering symbol \(X_t\), and their common middle block consists of the \(M-1\) variables \(X_{t-M+1},\ldots,X_{t-1}\). An entrance occurs precisely when, for one unique missing type \(a\), the middle block contains all types except \(a\), the entering symbol is \(a\), and the departing symbol is not \(a\). The three components involve disjoint coordinates and are independent. Hence
\[
\mu_{n,M}(\boldsymbol p)=\sum_{a=1}^{n}p_a(1-p_a)\sum_{S\subseteq[n]\setminus\{a\}}(-1)^{n-1-|S|}\left(\sum_{i\in S}p_i\right)^{M-1}.
\tag{1}
\]
This identity is exact for every positive probability vector; the inner expression is the probability that the middle block uses every one of the other \(n-1\) types and no \(a\). The identity reduces for uniform probabilities to Long's previously established Stirling-number expression; that uniform specialization is not a new claim.

**Two-type classification.** With two types, the middle block is monochromatic, giving \(\mu_M(p)=p(1-p)^M+(1-p)p^M\). For \(M=2\) the expression is \(p(1-p)\), and for \(M=3\) it is \(p(1-p)(1-2p(1-p))\). Both have unique global maximum at \(p=1/2\), the second by monotonicity in \(p(1-p)\in[0,1/4]\).

For \(M\ge4\), put \(r=p/(1-p)\) and \(F_M(r)=(r+r^M)/(1+r)^{M+1}\). A direct differentiation gives
\[
F_M'(r)=\frac{g_M(r)}{(1+r)^{M+2}},\qquad
g_M(r)=1-Mr+Mr^{M-1}-r^M.
\tag{2}
\]
We have \(g_M(0)=1\), \(g_M(1)=0\), and \(g_M'(1)=M(M-3)>0\), so \(g_M\) is negative immediately to the left of \(1\). Thus there exists at least one root in \((0,1)\). The reciprocity \(g_M(r)=-r^Mg_M(1/r)\) gives a corresponding root above \(1\). The coefficient signs of \(g_M\), ordered by descending powers, are \(-,+,-,+\). Descartes' rule of signs permits at most three positive roots counted with multiplicity. Since \(1\) is a simple root and there are roots on either side, those three exhaust all positive roots, and the root \(r_M\in(0,1)\) is unique and simple. The sign pattern is therefore \(+, -, +, -\) on the intervals separated by \(r_M,1,1/r_M\). Consequently \(F_M\) has exactly two global peaks, at \(r_M\) and \(1/r_M\), and a strict local minimum at \(r=1\). There are no positive boundary maximizers because \(F_M(0)=\lim_{r\to\infty}F_M(r)=0\). For \(M=4\), the reduction \(\mu_4=p(1-p)(1-3p(1-p))\) gives the specified maximizers and \(1/12\).

**Large-window optimizer.** The unique root lies in \((1/M,2/M)\): \(g_M(1/M)=(1/M)^{M-1}(M-1/M)>0\), and \(g_M(2/M)<0\) for all \(M\ge4\), since \(g_M(2/M)\le -1+M(2/M)^{M-1}<0\). From \(g_M(r_M)=0\),
\[
r_M-\frac1M=r_M^{M-1}\left(1-\frac{r_M}{M}\right),
\]
so \(r_M=1/M+O((2/M)^{M-1})\), whence the estimate for \(p_M\). Substitution gives \(M\mu_M(p_M)\to e^{-1}\), since the second summand is negligible and \((1-p_M)^M\to e^{-1}\). At balance the exact flux is \(2^{-M}\).

**Fixed-alphabet contrast.** Take \(p_1=1-(n-1)/M\) and \(p_i=1/M\) for \(i\ge2\). For each rare symbol \(a\ge2\), the \(M-1\) middle draws have asymptotically independent counts of the remaining \(n-2\) rare types, each converging to a Poisson law of mean one. The count of type \(a\) tends to an independent Poisson law of mean one; type \(1\) occurs with probability tending to one. Thus the probability of no \(a\) and all other types present tends to \(e^{-1}(1-e^{-1})^{n-2}\). Each corresponding factor \(p_a(1-p_a)\) is asymptotic to \(1/M\). The contribution of the dominant type is bounded by \(p_1(1-p_1)^M\) and is negligible compared with \(1/M\). Summing yields the imbalanced asymptotic. Under uniform draws, Long's finite formula and the standard finite-alphabet onto-word asymptotic give \(\mu_{n,M}(\boldsymbol u)\sim((n-1)/n)^M\), exponentially smaller than \(1/M\). This completes the comparison.

**Stationary occupancy contrast.** For two types the coverage fraction is \(\pi_M(p)=1-p^M-(1-p)^M\), uniquely maximized by \(p=1/2\) for every \(M\ge2\), despite the opposite entrance-rate behavior for \(M\ge4\). The ergodic mean duration of a complete-coverage episode per entrance is \(\pi_M(p)/\mu_M(p)\). In particular, at the flux-optimizing bias this duration is asymptotic to \((e-1)M\), whereas at balance it equals \(2^M-2\). The stationary mean interval between consecutive entrances is \(1/\mu_M(p)\) (Kac/ergodic frequency identity). These are stationary assertions, not first-completion-time comparisons.

## Verification

The accompanying standalone `checker.py` uses only Python's standard library. It enumerates finite length-\(M+1\) words at exact rational probabilities for two-, three- and four-type examples; checks equation (1) against a direct event count; checks the derivative identity in (2) at rational points; verifies the rational root bracketing inequalities over a finite parameter range; and performs supplementary numerical asymptotic sanity checks. Run using `python checker.py`. The checker does not replace the proof by finite enumeration, does not certify Descartes' root argument, and does not establish the asymptotic assertions by testing.

## Relationship to prior work

Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws* (arXiv:2604.26298v1, first publicly posted April 29, 2026), establishes the exact flux and a rare-entry hitting law under uniform draws. Its Theorem 3.1 provides the middle-block decomposition used as the starting point of (1), but it does not analyze biased sampling or optimize entrance intensity. In the present result the reduction of (1) to Long's uniform formula is background, not a new result.

Shank and Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20(2), #P33 (2013), derive expected collection-time formulas under unequal probabilities and accumulation quotas without deterministic expiration. The present stationary entrance optimization is a different functional and is not implied by their classical-time identities. The general literature on word-pattern and run counts supplies known methods for evaluating pattern frequencies; this work claims no novelty for evaluating a fixed binary word probability, only the strict global phase transition in the optimized entrance rate and its fixed-alphabet implications.

## Limitations

The result assumes independent identical draws, deterministic lifetime of exactly \(M\) draws, and stationary two-sided sampling. The full optimizer is classified only for two coupon types. For \(n\ge3\), the displayed sparse distribution is an asymptotically effective competitor, not a proven global optimizer. No statement about optimal one-sided first hitting times is established. Earlier run-frequency or pattern-optimization formulations may encode the two-type polynomial after a change of variables; no universal literature-exhaustion or independent priority certification is claimed.

## References

1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1 (2026), https://arxiv.org/abs/2604.26298.
2. N. B. Shank and H. Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20(2), #P33 (2013), https://doi.org/10.37236/3348.
3. B. C. Johnson and J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1, article 5 (2014), https://doi.org/10.1186/2195-5832-1-5.
