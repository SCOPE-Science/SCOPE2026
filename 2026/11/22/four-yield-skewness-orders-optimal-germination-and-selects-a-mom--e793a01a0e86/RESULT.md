# Four-yield skewness orders optimal germination and selects a moment-robust seed strategy

## Finding

For a density-independent annual seed bank facing **four fixed positive seed-yield levels**, fixing the environmental mean and variance still leaves an exact one-dimensional ambiguity in the germination-optimal policy. This ambiguity is completely ordered by the yield's third moment. More precisely, for two probability laws with the same first two moments, the increase in the derivative of long-run log growth when the third raw moment increases by \(\Delta m_3>0\) is **exactly**
\[
\frac{\Delta m_3\,s g^2}{\prod_{i=1}^4 [s+g(r_i-s)]}>0,\qquad 0<g\le1.
\]
Thus increasing skewness at fixed mean and variance never decreases the uniquely optimal germination fraction, and strictly increases it whenever the lower-skewness optimizer is less than one. The growth itself increases strictly at *every* positive germination fraction. The optimal policy switches from a positive partial-germination strategy to complete germination precisely at the third-moment threshold in the theorem below.

Moreover, over the entire set of probability laws on these four yield levels with prescribed mean and second moment, the law with **minimum third moment** is the unique least-favorable law for every \(g>0\). Consequently the unique distributionally robust maximin policy is exactly that law's ordinary log-growth optimizer. A four-level yield alphabet is minimal for two different probability laws on the same known support to agree in their first two moments and disagree in their optimal policy.

## Assumptions and scope

Consider independent identically distributed annual environments, an annual seed population with no density dependence, and a constant germination fraction \(g\in[0,1]\). A dormant seed survives from one year to the next with a fixed probability \(s\in(0,1]\). A germinated seed produces \(r_i>0\) viable replacement seeds in environment \(i\), where \(0<r_1<r_2<r_3<r_4\) are fixed and the environmental probabilities are \(p_i\ge0\), \(\sum_i p_i=1\). The annual seed multiplication factor is \(s(1-g)+g r_i\), and the almost-sure asymptotic logarithmic growth exponent is
\[
L_p(g)=\sum_{i=1}^{4}p_i\log\bigl(s+g(r_i-s)\bigr).
\]
This equals the expectation by the strong law of large numbers; all logarithms are finite because yields are positive. Define the first three raw moments \(\mu=\sum_i p_i r_i\), \(\nu=\sum_i p_i r_i^2\), and \(m_3=\sum_i p_i r_i^3\). Assume \(\mu>s\), ensuring that the unique optimal germination fraction is positive. Let \(e_1,e_2,e_3,e_4\) denote the elementary symmetric polynomials in the four fixed yield levels.

**Theorem.** For any two probability laws \(p^-\) and \(p^+\) on the same four yield levels, with identical \(\mu,\nu\), and \(\Delta m_3=m_3(p^+)-m_3(p^-)>0\):

1. For all \(0<g\le1\), the derivative difference is the boxed formula in the Finding and \(L_{p^+}(g)>L_{p^-}(g)\). Their unique optimizers satisfy \(g^*_{p^+}\ge g^*_{p^-}\), with strict inequality exactly when \(g^*_{p^-}<1\).
2. For every such law, the complete-germination criterion is
\[
g^*_p=1\quad\Longleftrightarrow\quad m_3\ge m_{3,c}:=e_3-e_2\mu+e_1\nu-\frac{e_4}{s}.
\]
If this fails, the unique optimizer satisfies \(0<g_p^*<1\). At equality \(g_p^*=1\), with zero left derivative there.
3. For a nonempty probability set \(\mathcal P(\mu,\nu)\) consisting of all laws on these four yield levels with fixed normalization, mean, and second moment, the unique law \(p_{\min}\) of least third moment minimizes \(L_p(g)\) over \(\mathcal P\) simultaneously for every \(g>0\). Thus
\[
\max_{0\le g\le1}\min_{p\in\mathcal P(\mu,\nu)}L_p(g)
=\max_{0\le g\le1}L_{p_{\min}}(g),
\]
with the unique maximizing fraction \(g^*_{p_{\min}}\). If the feasible probability set has more than one law, its least-favorable endpoint has at least one zero probability.
4. On any common alphabet of at most three distinct yield levels, normalization plus the first two raw moments uniquely determine the probabilities. Four is therefore the sharp minimum for this moment-matched policy ambiguity.

## Proof

**1. Concavity and boundary optimizers.** Differentiation gives
\[
L_p'(g)=\sum_i\frac{p_i(r_i-s)}{s+g(r_i-s)},\qquad
L_p''(g)=-\sum_i\frac{p_i(r_i-s)^2}{[s+g(r_i-s)]^2}.
\]
Because \(\mu>s\), not all positive-mass yields equal \(s\), and the second derivative is strictly negative. Also \(L'_p(0)=(\mu-s)/s>0\), so the unique maximum lies in \((0,1]\); it is at one exactly when \(L'_p(1)\ge0\).

**2. The exact four-support identity.** Put
\[
w_i=\left(\prod_{j\ne i}(r_i-r_j)\right)^{-1}.
\]
Lagrange interpolation for polynomials through degree three gives \(\sum_iw_i r_i^k=0\) for \(k=0,1,2\), and \(\sum_iw_i r_i^3=1\). The null space of the \(3\)-by-\(4\) matrix with rows \((1)\), \((r_i)\), and \((r_i^2)\) is one-dimensional, hence the common-moment probability difference satisfies \(p_i^+-p_i^-=\Delta m_3 w_i\). For any \(g>0\), partial fractions yield
\[
\sum_iw_i\frac{r_i-s}{s+g(r_i-s)}
=\frac{s g^2}{\prod_i[s+g(r_i-s)]}.
\]
For example, writing \(z=s(1-1/g)\), use \((r_i-s)/[s+g(r_i-s)]=(1/g)(1-s/[g(r_i-z)])\), \(\sum_iw_i=0\), and \(\sum_i w_i/(z-r_i)=1/\prod_i(z-r_i)\). As there are four factors, \(\prod_i(z-r_i)=g^{-4}\prod_i[s+g(r_i-s)]\). Multiplying by \(\Delta m_3\) proves the exact positive derivative difference. Integration from zero, where the two growth functions equal \(\log s\), gives
\[
L_{p^+}(g)-L_{p^-}(g)=\Delta m_3\int_0^g
\frac{s t^2\,dt}{\prod_i[s+t(r_i-s)]}>0
\]
for every \(g>0\). Since both derivatives strictly decrease, the positive pointwise difference between derivatives implies the claimed optimizer ordering. If the lower-law optimizer is interior, the upper-law derivative is positive there, forcing a strictly larger optimizer; if it is one, both must have optimum one. This also establishes the complete equality cases.

**3. Exact third-moment switch.** The monic quartic \(\prod_i(x-r_i)=x^4-e_1x^3+e_2x^2-e_3x+e_4\) vanishes at each \(r_i>0\), so
\[
\frac1{r_i}=\frac{e_3-e_2r_i+e_1r_i^2-r_i^3}{e_4}.
\]
Therefore \(L'_p(1)=1-s\sum_i p_i/r_i=1-(s/e_4)(e_3-e_2\mu+e_1\nu-m_3)\). Strict concavity from step 1 gives exactly the displayed threshold, including equality and endpoint cases.

**4. Worst-case moment law and support minimality.** For fixed feasible \(\mu,\nu\), every law lies on the affine line obtained by adding a multiple of \((w_i)\). This line's intersection with the probability simplex is a closed interval (possibly a singleton), and \(m_3\) is a strictly increasing affine coordinate along it. The positive comparison in step 2 shows that its smallest-\(m_3\) endpoint minimizes \(L_p(g)\) for *every* \(g>0\). At \(g=0\), all laws give \(\log s\), and the maximizer is positive by step 1, so the maximin identity and uniqueness follow. A nonsingleton feasible line terminates at the simplex boundary, forcing one or more vanishing probabilities. On an alphabet of size at most three, the corresponding square or tall Vandermonde moment matrix has full column rank, so no two distinct moment-matched laws exist. The example below attains the four-level boundary.

**Exact witness.** Choose \((r_1,r_2,r_3,r_4)=(1/2,1,3/2,2)\), \(s=24/25\), and
\[
p^-=(7,3,9,5)/24,\qquad p^+=(5,9,3,7)/24.
\]
Both have \(\mu=5/4\), \(\nu=15/8\), variance \(5/16\), but \(m_3(p^-)=99/32\), \(m_3(p^+)=101/32\), while \(m_{3,c}=25/8=100/32\). Direct exact arithmetic gives \(L'_{p^-}(1)=-1/50\) and \(L'_{p^+}(1)=+1/50\). Thus \(9/10<g^*_{p^-}<19/20\) but \(g^*_{p^+}=1\). With this same support, \(s,\mu,\nu\), the complete moment ambiguity set is
\[
p(t)=(1/4-t,1/4+3t,1/4-3t,1/4+t),\quad -1/12\le t\le1/12.
\]
Its unique worst law is \(p(-1/12)=(1/3,0,1/2,1/6)\), and its unique robust germination fraction is the positive root of
\[
2691g^2+718g-2784=0,
\quad g=\frac{-359+25\sqrt{12193}}{2691}\approx0.8924369947.
\]
The second root is negative; strict concavity shows the positive root is the global optimizer.

## Verification

The accompanying `check.py` is self-contained Python 3 code using only the standard library. Running `python3 check.py` gives `PASS 5615 exact rational assertions`. It checks the four-level formula on 400 deterministic rational support and probability samples, the harmonic interpolation identity, strict positivity, the complete rational witness, and derivative brackets for the robust optimizer. All infinite or universal quantifiers are established by the written proof, not by sampling. Exact source file bytes and checksums accompany this result.

## Relationship to prior work

Cohen (1966) established the underlying density-independent annual seed-bank log-growth criterion, its concavity, and the ordinary optimizer's connection to the inverse-yield (harmonic mean) boundary. Those classical results are not new here. The present mathematical contribution is the exact *within-fixed-first-two-moments* four-support derivative identity, its strict all-policy ordering, its sharp third-moment threshold, the support-minimal opposite-policy witness, and the resulting same-worst-law-for-every-policy maximin classification. Siegmund et al. (first public preprint, 2022) use seed-bank demographic models to motivate the ecological need to assess germination strategies; they do not present this fixed-moment four-support theorem. Sun and Boyd (2018) give general convex formulations for distributionally robust Kelly gambling with moment-constrained probabilities; that framework permits numerical solutions of such problems but does not state the special skewness ordering, fixed least-favorable law for all positive policies, or the rational germination threshold here. General divided-difference and stochastic-dominance theory may provide alternative derivations of parts of the comparison; historical novelty beyond the inspected sources remains provisional.

## Limitations

The environmental yield alphabet is assumed fixed, known, and exactly four-level; probabilities rather than yield values vary. Independent years, constant germination, no density dependence, and common dormant survival are modeling idealizations. Mean and variance alone do not establish the *true* ecological law or which policy is best without additional assumptions; the robust policy is only robust over the stated four-outcome moment ambiguity set. Larger or continuous support distributions need not have this one-parameter ordering. The analysis predicts mathematical growth and decision thresholds, not field outcomes. No independent external audit has been performed.

## References

- Dan Cohen, *Optimizing reproduction in a randomly varying environment*, Journal of Theoretical Biology **12** (1966), 119–129. https://doi.org/10.1016/0022-5193(66)90188-3 . Full text consulted via https://www.academia.edu/5917847/Optimizing_reproduction_in_a_randomly_varying_environment .
- Gregor-Fausto Siegmund, David A. Moeller, Vincent M. Eckhart, Monica A. Geber, *Bet hedging is not sufficient to explain intraspecific variation in germination patterns of a winter annual plant*, bioRxiv preprint first publicly posted **2022-09-17**, https://doi.org/10.1101/2022.09.15.508102 . Lawful full preprint text consulted via https://www.academia.edu/112508312/Bet_hedging_is_not_sufficient_to_explain_germination_patterns_of_a_winter_annual_plant . Later journal version https://doi.org/10.1086/726785 (2023).
- Qingyun Sun and Stephen Boyd, *Distributional Robust Kelly Gambling* (2018), https://web.stanford.edu/~boyd/papers/pdf/robust_kelly.pdf . Sections 1 and 2.1 consulted.
- D. ten Brink, J. R. Gremer, H. Kokko, *Optimal germination timing in unpredictable environments: the importance of dormancy for both among- and within-season variation*, Ecology Letters (2020), https://doi.org/10.1111/ele.13461 , lawful full text https://www.kokkonuts.org/wp-content/uploads/ele.13461.pdf .
