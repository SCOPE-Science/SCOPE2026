# Two unequal visits identify false-positive occupancy and obey a universal short-budget allocation law

## Finding

Consider a closed ecological site observed in two nonoverlapping visits of positive durations \(u,v\), with \(u+v=T\). Its occupancy indicator is Bernoulli with unknown probability \(0<\psi<1\). When unoccupied, independent false alarms follow a homogeneous Poisson process of unknown rate \(\alpha>0\); when occupied, independent genuine detections add rate \(\lambda>0\) to this false-alarm process. Each visit retains only whether **any** alarm occurred, yielding one of the four ordered binary histories. For every \(T>0\):

1. The three parameters \((\psi,\alpha,\lambda)\) are **globally identifiable** from the distribution of the two binary histories if and only if \(u\ne v\). For \(u=v\) they are not locally identifiable, and the three-parameter Fisher determinant is zero. For every unequal positive split the Fisher information is positive definite.
2. For the exact local Fisher D criterion, as the total duration \(T\downarrow0\) with parameters fixed in the stated interior domain, the two mirrored optimal short/long splits approach
\[
\frac{\min(u,v)}T\longrightarrow x_0=\frac{1-1/\sqrt3}{2}=0.211324865405187\ldots.
\]
Indeed, for sufficiently small \(T\), there are exactly two global maximizing splits, interchanged by \(u\leftrightarrow v\). Uniformly for \(0\le x\le1\), with \(u=Tx\), the determinant obeys
\[
\det I_T(x)=\frac{\psi^2(1-\psi)^2\lambda^8}{144\mu_1^2\mu_2}\,T^8 x^2(1-x)^2(1-2x)^2+O(T^9),
\quad \mu_1=\alpha+\psi\lambda,\quad\mu_2=\alpha^2+\psi(2\alpha\lambda+\lambda^2).
\]
In particular, the optimized leading shape factor is exactly \(1/108\); the equal-duration design has zero determinant at **every** budget, not merely asymptotically.

This is a local information design result, not a statement about the distribution of finite-sample estimators.

## Assumptions and scope

Sites are mutually independent and identically distributed. Occupancy is constant across visits. The two conditional encounter processes are Poisson with fixed rates during both visits, and disjoint intervals have independent increments conditional on occupancy. False alarms occur in occupied as well as unoccupied sites. A genuine encounter and a false alarm are not distinguished by the binary recording mechanism. Both rates and prevalence are unknown, strictly interior, and shared across sites. No encounter timestamps, within-visit counts, confirmatory observations, per-visit setup costs, or adaptive stopping are retained or modeled. Fisher information is evaluated per site at a fixed nominal parameter triple; the number of independent sites only scales its determinant.

## Proof

**1. The four-history likelihood.** Write
\[
m(t)=(1-\psi)e^{-\alpha t}+\psi e^{-(\alpha+\lambda)t}.
\]
This is the probability of no alarm for duration \(t\). Conditional independence of the disjoint visits gives, in the order \((00,10,01,11)\),
\[
(p_{00},p_{10},p_{01},p_{11})=
\big(m(T),\;m(v)-m(T),\;m(u)-m(T),\;1-m(u)-m(v)+m(T)\big).
\]
All four entries are strictly positive. This distribution determines precisely the three numbers \(m(u),m(v),m(T)\). For \(u=v\), two of those are the same and \(p_{10}=p_{01}\), leaving only two degrees of freedom for three parameters.

**2. Global injectivity with unequal durations.** The functions \(1,e^{-ct}\) form part of an exponential Chebyshev system: any nonzero real linear combination of \(n\) exponentials with distinct real exponents has at most \(n-1\) distinct real zeros. To prove this elementary fact, divide by one exponential, differentiate, use Rolle's theorem and induct on \(n\). If two different parameter triples produced the same three observed values, the difference of their survival functions would be a linear combination of at most four distinct exponentials vanishing at the four distinct times \(0,u,v,T\) (both survival functions equal one at zero). The Chebyshev zero bound forces the difference to vanish identically. Linear independence of exponentials, positive mixture weights and the ordering \(\alpha<\alpha+\lambda\) then make the two parameter triples identical.

**3. Exact Fisher determinant and its strict positivity.** Let \(G\) be the \(3\times3\) matrix with rows \(\nabla m(u),\nabla m(v),\nabla m(T)\), derivatives in the parameter order \((\psi,\alpha,\lambda)\). The three independent probabilities are an invertible determinant-one linear transform of those three survival values. By the multinomial Fisher formula and a rank-one determinant identity,
\[
\det I_T=\frac{(\det G)^2}{p_{00}p_{10}p_{01}p_{11}}.
\]
For \(t>0\), divide the row \(\nabla m(t)\) by \(t e^{-\alpha t}\), put \(z=e^{-\lambda t}\), and obtain
\[
\left(-\lambda L(z),\;-(1-\psi)-\psi z,\;-\psi z\right),
\qquad L(z)=\int_0^1 z^s\,ds.
\]
The final two columns span \(1\) and \(z\) since \(0<\psi<1\). Moreover \(L''(z)=\int_0^1s(s-1)z^{s-2}\,ds<0\) for \(0<z<1\). Thus three distinct points on the strictly concave curve \(L\) cannot be collinear. Since \(u,v,T\) are distinct exactly when \(u\ne v\), the determinant of \(G\), and therefore the Fisher determinant, is nonzero exactly for unequal positive visit durations.

**4. Uniform short-budget expansion.** Let \(\mu_j=(1-\psi)\alpha^j+\psi(\alpha+\lambda)^j\) for \(j=1,2,3\). Taylor's theorem gives \(m(t)=1-\mu_1t+\mu_2t^2/2-\mu_3t^3/6+O(t^4)\), with parameter derivatives and their time derivatives on compact parameter neighborhoods. Direct differentiation gives
\[
\det\frac{\partial(\mu_1,\mu_2,\mu_3)}{\partial(\psi,\alpha,\lambda)}=\lambda^4\psi(\psi-1).
\]
Every row of \(G\) has a factor of its observation time. After removing those factors, the remaining analytic alternant has the exact Vandermonde factor \((v-u)(T-u)(T-v)\). Consequently, with a jointly analytic factor \(H\),
\[
\det G=u^2v^2T(v-u)H(u,v,T),\qquad H(0,0,0)=\frac{\lambda^4\psi(\psi-1)}{12}.
\]
The probability factors can likewise be written \(p_{10}=u A(u,v)\), \(p_{01}=v B(u,v)\), and \(p_{11}=uv C(u,v)\), where \(A,B,C\) extend continuously and positively to zero, with limits \(\mu_1,\mu_1,\mu_2\). For instance, \(C=\int_0^1\int_0^1 m''(su+tv)\,ds\,dt\). Substitution into the exact Fisher formula yields
\[
\frac{\det I_T(x)}{T^8}=
 x^2(1-x)^2(1-2x)^2\,
 \frac{H(Tx,T(1-x),T)^2}{m(T)A B C},
\]
where the second factor converges uniformly, with two derivatives in \(x\), to \(\psi^2(1-\psi)^2\lambda^8/(144\mu_1^2\mu_2)>0\). This proves the displayed uniform expansion.

Set \(y=x(1-x)\in[0,1/4]\). The leading shape equals \(y^2(1-4y)\), whose sole positive maximizer is \(y=1/6\), with height \(1/108\). It has two symmetric, nondegenerate maximizers \(x_0\) and \(1-x_0\). Uniform convergence and nondegenerate local-maximizer stability imply that every exact maximizer converges to that two-point set. The exact Fisher objective is symmetric under exchanging visit lengths and has a nonzero determinant away from the endpoints and midpoint. Its analytic factorization and the strict curvature of the two limiting maxima ensure precisely one maximizer in each of their neighborhoods for all sufficiently small budgets. They are exchanged by the exact symmetry, proving the asserted two globally maximizing splits.

## Verification

Run `python verify.py` with Python 3.10 or later, SymPy and mpmath. It checks the moment Jacobian identity symbolically and compares the exact Jacobian-of-probabilities Fisher calculation to an independent direct score-sum computation over 375 seeded parameter sets. It also checks history normalization, strictly positive determinants away from balance, symmetry, the zero at balance, and three distinct parameter settings approaching the short-budget law. The diagnostic contains 2,269 assertions. The continuum, global identifiability and exact optimization statements are proved above and are not inferred from numerical sampling.

## Relationship to prior work

Royle and Link (2006) established the two-component occupancy observation mixture with false positives; this theorem specializes that likelihood to **two unequal-duration Poisson alarm windows** and obtains a global identifiability criterion and a sharp local D-optimal short-budget fraction. Miller et al. (2011) analyze ways to resolve false-positive ambiguity by introducing more informative detection types or methods, whereas this exact experiment uses only two unverified binary visit records. Clement (2016) optimizes the number and types of surveys to minimize occupancy-estimation error with fixed per-visit detection probabilities, not the within-site division of a vanishing continuous-time Poisson observation budget for three simultaneous unknowns. A related published two-visit result without false positives optimizes information for just prevalence and one detection rate and actually favors equal visit lengths for small budgets; its objective and rank are different. The global two-exponential identification step is an application of classical exponential Chebyshev theory and is not claimed as a new general theorem about exponential sums. The claimed new component is the joint three-parameter ecological identification/design law and its universal \(21.13\%\) short-budget fraction, subject to the historical-overlap limitation below.

## Limitations

The statistical interpretation of the mixture components as occupancy versus persistent heterogeneity still depends on the *model assumption*: mathematically identifying two mixture rates does not prove which ecological process generated them. The model assumes strict Poisson stationarity, independent visits conditional on occupancy, known common effort-time scale, equal rate parameters across sites, and no within-visit count or timing data. The fraction is an asymptotic D-optimal local-design law; it is not a parameter-robust finite-budget optimum or a minimum finite-sample mean-squared-error design. We do not assert uniqueness of optimal asymmetric splits for every positive finite duration. The full text of the 2006 foundational source was not accessed, and unlocated classical duration-design work remains a residual historical priority risk. No independent scientific audit has been performed.

## References

1. Royle, J. A., and Link, W. A. (2006). *Generalized site occupancy models allowing for false positive and false negative errors*. Ecology 87, 835–841. First online 2006-04-01. https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2
2. Miller, D. A., Nichols, J. D., McClintock, B. T., Grant, E. H. C., Bailey, L. L., and Weir, L. A. (2011). *Improving occupancy estimation when two types of observational error occur: non-detection and species misidentification*. Ecology 92, 1422–1428. First online 2011-07-01. https://doi.org/10.1890/10-1396.1
3. Clement, M. J. (2016). *Designing occupancy studies when false-positive detections occur*. Methods in Ecology and Evolution 7, 1538–1547. First online 2016-07-18. https://doi.org/10.1111/2041-210X.12617
4. *A two-visit occupancy experiment breaks equal-effort optimality* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-two-visit-occupancy-experiment-breaks-equal-effort-optimality--b8f26f454426. Related comparison only: no false alarms and two unknown parameters.
