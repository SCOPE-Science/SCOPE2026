# A single reversal threshold for cost-optimal ecological survey duration under persistent Gamma detectability

## Finding

**Theorem (unique heterogeneity reversal).** Let \(0<q<1\), \(k>0\), \(\mu>0\), \(c>0\), and \(\Delta>0\). An ecological site is occupied with prior probability \(q\). Conditional on occupation, detections follow a Poisson process with a *single site-specific random intensity* \(\Lambda\), drawn once before searching and retained during the entire visit. Compare (G) \(\Lambda\sim\operatorname{Gamma}(k,\text{scale}=\mu/k)\) and (H) the mean-matched homogeneous rate \(\Lambda=\mu\). Under either model, search ends at the first detection or at a chosen deterministic cap \(t\ge0\); search costs \(c\) per unit time, while an occupied site missed before the cap incurs incremental management loss \(\Delta\) relative to an occupied site detected in time. There are no false positives or arrivals during searching.

Write \(M=\mu\Delta/c\) and \(\alpha=(1-q)/q\). The cost-minimizing caps \(t_G,t_H\) are unique. If \(M\le1/q\), both are zero. If \(M>1/q\), each is positive and finite and is given by

\[
\mu t_H=\log\!\left(\frac{M-1}{\alpha}\right),\qquad
w+\alpha w^{k+1}=M,\quad w>1,\qquad
\mu t_G=k(w-1).
\]

There is precisely one positive \(x_c=x_c(k,q)\) solving

\[
e^{x_c}=\left(1+\frac{x_c}{k}\right)^{k+1}+\frac{x_c}{k\alpha}.
\]

With \(M_c=1+\alpha e^{x_c}>1/q\), the *complete strict ordering* of optimal search caps is

\[
\begin{array}{c|ccc}
M& (1/q,M_c)&M_c&(M_c,\infty)\\\hline
\text{optimal caps}&t_G<t_H&t_G=t_H&t_G>t_H.
\end{array}
\]

Thus matching the mean detection intensity does not induce a uniform direction of error in the economically optimal search duration. There is exactly one reversal as the avoided late-management loss grows.

For \(q=1/2\), \(k=1\), and \(\mu=c=1\), the crossover solves \(e^x=1+3x+x^2\), with \(x_c\approx2.893116430925\) and \(M_c\approx19.049471975666\). At \(M=3\), \((t_G,t_H)\approx(0.302775638,0.693147181)\); at \(M=20\), \((t_G,t_H)\approx(3,2.944438979)\).

## Assumptions and scope

The Gamma distribution uses the shape/scale normalization specified above; hence \(\mathbb E\Lambda=\mu\) and \(\operatorname{Var}(\Lambda)=\mu^2/k\). The Gamma rate is *persistent*, not independently redrawn at each revisit. Conditional on \(\Lambda\), the time \(T\) until first detection is exponential of rate \(\Lambda\), and an empty site has \(T=\infty\). For a cap \(t\), the actual survey duration is \(\min(T,t)\). An occupied site is managed early when detected and otherwise suffers a fixed later extra loss \(\Delta\); adding any common baseline management cost does not affect the optimizer. The cost criterion is expected variable survey cost plus expected extra late-management loss. Optimization is over all deterministic nonnegative caps, including zero and arbitrarily large finite caps, under a single continuous visit.

## Proof

**1. Exact expected cost.** Let \(S(t)=\mathbb E(e^{-\Lambda t})\) conditional on occupation, with \(S_H(t)=e^{-\mu t}\) and \(S_G(t)=(1+\mu t/k)^{-k}\). By the survival-tail integral identity, the expected search time is

\[
(1-q)t+q\int_0^t S(u)\,du.
\]

The probability of occupied-but-undetected is \(qS(t)\). Therefore, up to a constant independent of \(t\),

\[
C(t)=c\left((1-q)t+q\int_0^t S(u)\,du\right)+q\Delta S(t).
\]

Differentiation yields \(C'(t)=c[(1-q)+qS(t)]-q\Delta[-S'(t)]\). Define \(R(t)=[-S'(t)]/[\alpha+S(t)]\). The sign of \(C'(t)\) is the sign of \(c-\Delta R(t)\).

**2. Unique optimal cap and exact equations.** Write \(x=\mu t\) and \(w=1+x/k\). Direct differentiation gives

\[
R_H(t)=\frac{\mu}{1+\alpha e^x},\qquad
R_G(t)=\frac{\mu}{w+\alpha w^{k+1}}.
\]

Both are strictly decreasing from the common initial value \(q\mu\) to zero. Consequently \(C'(0)\ge0\) exactly when \(M\le1/q\), giving unique optimum zero, with a strict positive derivative for every positive \(t\) even at equality. When \(M>1/q\), the derivative changes from negative to positive exactly once, establishing a unique finite global minimizer. Solving \(\Delta R=c\) produces the displayed explicit homogeneous cap and unique positive Gamma root.

**3. A single rate-comparison crossing.** Since both rate formulas have positive denominators, for every \(x>0\),

\[
R_G(t)>R_H(t)\quad\Longleftrightarrow\quad
F(x):=e^x-\left(1+\frac{x}{k}\right)^{k+1}-\frac{x}{k\alpha}>0.
\]

Here \(F(0)=0\), \(F'(0)=-(1+1/\alpha)/k<0\), and \(F''(0)=-1/k<0\). Its third derivative is

\[
F'''(x)=e^x-\left(1-\frac1{k^2}\right)\left(1+\frac{x}{k}\right)^{k-2}>0\qquad(x\ge0).
\]

For \(k\le1\), the subtracted coefficient is nonpositive. For \(1<k\le2\), the coefficient lies below one and the power is at most one. For \(k>2\), \(\log(1+x/k)\le x/k\) implies \((1+x/k)^{k-2}\le e^x\), and again the coefficient is below one. Also \(F,F',F''\) eventually become positive because exponentials dominate powers. Therefore \(F''\) crosses zero exactly once, then \(F'\) does, and finally \(F\) does at exactly one strictly positive \(x_c\). It follows that \(R_G<R_H\) before \(x_c/\mu\), and \(R_G>R_H\) afterward.

**4. A single optimal-cap reversal.** Let \(M>1/q\) vary. The homogeneous optimum \(x_H=\mu t_H=\log((M-1)/\alpha)\) is strictly increasing from zero to infinity. At \(t_H\), \(R_H=c/\Delta\). Since \(R_G\) is strictly decreasing, \(t_G<t_H\) exactly when \(R_G(t_H)<R_H(t_H)\); similarly, greater corresponds to greater. The unique crossing in step 3 translates to the unique loss threshold \(M_c=1+\alpha e^{x_c}\), with the three strict/equality regimes in the theorem.

## Verification

The standalone file `verify.py` uses only the Python standard library and can be executed using `python3 verify.py`. It checks exact rational identities for Gamma integer shapes and rational durations, derivative sign changes on specified finite grids, ordering reversals for a range of real shapes and occupancies, and the documented benchmark values. On the supplied package its output is `PASS 1274 arithmetic/finite-grid diagnostic checks`. These checks support the formulas and catch implementation or normalization errors; they do **not** prove uniqueness on a continuum. The proof of that statement is the strict third-derivative argument in step 3.

## Relationship to prior work

Hauser and McCarthy (2009) formulate risk- and cost-weighted invasive-surveillance allocation; Guillera-Arroita, Hauser and McCarthy (2014) specifically optimize removal surveys that terminate on first detection, with constant site-specific detection intensities. Moore et al. (2014) analyze random rates over repeated visits, including temporal correlations; Moore and McCarthy (2016) give Gamma detection-rate calculations and spatial/temporal allocations, primarily for visit-to-visit random rates and fixed survey budgets. The presently proved statement is narrower but different: a single *persistent* Gamma latent intensity within a removal survey, expected executed search cost plus missed-management penalty, and an all-parameter **unique crossing** between optimal caps under mean matching. The general usefulness of rate heterogeneity in search design and broad nonmonotonic changes in effort are prior knowledge; the claimed contribution is the exact one-crossing theorem for this specific model. Historical priority beyond the inspected material is not established.

## Limitations

The finding is an exact mathematical comparison conditional on a correctly specified Gamma frailty distribution, not a calibrated field recommendation. It assumes a fixed occupation state, one survey, known parameters, no false detections, no additional travel/set-up cost depending on the cap, and a constant extra loss per missed occupied site. The parameter endpoints \(q=0\) and \(q=1\) are excluded; for \(q=1\), the homogeneous model can favor an infinite cap and the stated finite comparison does not apply. No general result is claimed for arbitrary frailty laws, replenished detectability across visits, or multiple interacting sites.

## References

1. C. E. Hauser and M. A. McCarthy (2009), *Streamlining ‘search and destroy’: cost-effective surveillance for invasive species management*, Ecology Letters 12, 683–692. DOI: https://doi.org/10.1111/j.1461-0248.2009.01323.x (online version publicly recorded 11 May 2009).
2. G. Guillera-Arroita, C. E. Hauser, and M. A. McCarthy (2014), *Optimal surveillance strategy for invasive species management when surveys stop after detection*, Ecology and Evolution 4, 1751–1760. DOI: https://doi.org/10.1002/ece3.1056 (first published 11 April 2014).
3. A. L. Moore, M. A. McCarthy, K. M. Parris, and J. L. Moore (2014), *The Optimal Number of Surveys when Detectability Varies*, PLOS ONE 9, e115345. DOI: https://doi.org/10.1371/journal.pone.0115345 (published 19 December 2014).
4. A. L. Moore and M. A. McCarthy (2016), *Optimizing ecological survey effort over space and time*, Methods in Ecology and Evolution 7, 891–899. DOI: https://doi.org/10.1111/2041-210X.12564 (first published 25 March 2016).
