# Sharp dispersion minimum and zero-deflation law for the semi-Poisson count family

## Finding

The 2023 semi-Poisson count distribution of Almuhayfith, Bapat, Bakouch and Alnaghmosh is **strictly underdispersed**, not overdispersed, at every permitted parameter. More sharply, its variance-to-mean ratio has **exactly one global minimum**, and its zero probability is **strictly deficient** relative to a Poisson law with the same mean. The results determine the full shape and sharp endpoints of these two natural calibration diagnostics.

Writing the rate parameter as \(t>0\), let \(X_t\) have mass function
\[
 p_n(t)=\frac{(n+1)t^{n+2}}{(n+2)n!S(t)},\qquad n=0,1,\ldots,\qquad S(t)=(t^2-t+1)e^t-1.
\]
Put \(\mu(t)=\mathbb E X_t\), \(v(t)=\operatorname{Var}(X_t)\), \(F(t)=v(t)/\mu(t)\) and \(R(t)=p_0(t)e^{\mu(t)}\). Then, for every \(t>0\),
\[
 0<F(t)<1,\qquad \frac12<R(t)<1.
\]
The function \(R\) decreases strictly from \(1\) to \(1/2\) as \(t\) increases from \(0\) to infinity. The function \(F\) decreases strictly to a unique minimum at \(t=t_*\) and then increases strictly toward \(1\), with the rigorously enclosed values
\[
1.40741241822510067986511<t_*<1.40741241822510067986512,
\]
\[
0.9099071739796848<F(t_*)<0.9099071739796851.
\]
The exact characterization of \(t_*\) is the unique positive zero of the exponential polynomial \(N\) specified in the proof below. The strict underdispersion conclusion follows already from the model's weighted-Poisson structure and an established general principle, so the original model-specific contribution here is the **unique sharp dispersion minimum together with the exact mean-matched zero-calibration profile**, not the general underdispersion principle by itself.

## Assumptions and scope

Only \(t>0\) and integer counts \(n\ge0\) are assumed. The stated distribution is the original, non-zero-modified semi-Poisson family, not the unrelated semi-Poisson level-spacing distribution in mathematical physics. All claims concern the population law, not the performance of numerical parameter estimators or a particular observed sample. The Poisson comparator for \(R\) has parameter \(\mu(t)\), so its zero probability is \(e^{-\mu(t)}\).

## Proof

**Normalization and moment formulas.** By termwise summation of the entire series,
\[
\sum_{n\ge0}\frac{n+1}{n+2}\frac{t^{n+2}}{n!}=S(t).
\]
Consequently \(S(t)>0\), every \(p_n(t)>0\), and exponential-family differentiation gives
\[
\mu(t)=t\frac{S'(t)}{S(t)}-2,\qquad v(t)=t\mu'(t).
\]
Define
\[
 A(t)=e^t(t^3-t^2+2t-2)+2=\mu(t)S(t),
\]
\[
 T(t)=t^2e^t\{e^t(t^3-2t^2+2t+2)-(t^2+4t+2)\}.
\]
Direct differentiation simplifies the dispersion index to \(F(t)=T(t)/[S(t)A(t)]\); its denominator is positive for \(t>0\).

**Uniform strict underdispersion.** The consecutive birth ratio is
\[
r_n(t)=\frac{(n+1)p_{n+1}(t)}{p_n(t)}
=t\left(1+\frac1{(n+1)(n+3)}\right).
\]
It is strictly decreasing in \(n\). The shift identities
\[
\mathbb E r_{X_t}(t)=\mu(t),\qquad
\mathbb E[X_t r_{X_t}(t)]=\mathbb E[X_t(X_t-1)]
\]
yield
\[
 v(t)-\mu(t)=\operatorname{Cov}(X_t,r_{X_t}(t))<0.
\]
Strictness follows because the law has at least two distinct positive-probability counts. This also proves strict ultra-log-concavity. Positivity of the variance and mean yields \(0<F(t)<1\).

**Unique worst dispersion.** A formal derivative calculation gives
\[
F'(t)=\frac{N(t)}{S(t)^2 A(t)^2},\qquad
N(t)=\sum_{k=1}^4 P_k(t)e^{kt},
\]
where
\[
\begin{aligned}
P_1(t)&=2t^4+16t^3+28t^2+8t,\\
P_2(t)&=t^6-10t^5-4t^4+24t^3-60t^2-24t,\\
P_3(t)&=t^9+2t^8+9t^7-18t^5+62t^4-72t^3+36t^2+24t,\\
P_4(t)&=4t^7-25t^6+44t^5-52t^4+32t^3-4t^2-8t.
\end{aligned}
\]
Write \(c_n=n![t^n]N(t)\), using the ordinary Maclaurin coefficient notation. Exact integer algebra gives \(c_n=0\) for \(0\le n\le9\), \(c_n<0\) for \(10\le n\le14\), and \(c_n>0\) for \(15\le n\le25\). To verify *all* remaining coefficients, define the polynomial
\[
Q_k(n)=\sum_{j\ge0}[t^j]P_k(t)\frac{n(n-1)\cdots(n-j+1)}{k^j}.
\]
Then \(c_n=\sum_{k=1}^4 k^nQ_k(n)\). For each \(k=1,2,3,4\), expansion of \(Q_k(26+u)\) as a polynomial in \(u\) has strictly positive rational coefficients; hence \(c_n>0\) for every integer \(n\ge26\). The accompanying checker reconstructs the derivative identity, all finite coefficient signs, and every shifted-polynomial coefficient with exact arithmetic.

Therefore \(N(t)/t^{14}\) is strictly increasing for \(t>0\): differentiating its convergent series gives only positive terms, since each negative coefficient occurs at a negative power and every positive coefficient at a positive power. This ratio tends to \(-\infty\) as \(t\downarrow0\) and to \(+\infty\) as \(t\to\infty\) (the positive \(n=15\) term alone suffices). It consequently has exactly one positive zero \(t_*\). As \(S^2A^2>0\), \(F'\) changes sign only once, from negative to positive. The sharp minimum follows. Exact rational Taylor enclosures for \(e^{kt}\) certify the displayed interval for \(t_*\); interval arithmetic applied to \(T/(SA)\) certifies the displayed bound for \(F(t_*)\).

**Sharp zero-mass deficit.** Since \(p_0(t)=t^2/[2S(t)]\), differentiation gives
\[
\frac{d}{dt}\log R(t)
=\frac2t-\frac{S'(t)}{S(t)}+\mu'(t)
=\frac{v(t)-\mu(t)}{t}<0.
\]
At the left endpoint the distribution concentrates at zero, so \(R(t)\to1\). At infinity, \(S(t)=e^t t^2(1-t^{-1}+t^{-2})-1\) and \(\mu(t)=t+O(t^{-1})\), whence \(R(t)\to1/2\). Thus the zero-mass ratio decreases bijectively from \(1\) to \(1/2\).

The dispersion endpoint expansions, obtained from the same normalization, are
\[
F(t)=1-\frac5{24}t+O(t^2)\quad(t\downarrow0),\qquad
F(t)=1-\frac2{t^2}+O(t^{-3})\quad(t\to\infty).
\]
They independently confirm that the sharp minimum lies strictly inside the parameter domain.

## Verification

Run \(\texttt{python3 checker.py}\) from the directory containing the standalone checker. It requires only Python 3 standard-library modules. Its exact-integer and rational operations verify the exponential-polynomial derivative numerator, the finite signs through degree 25, positive shifted-polynomial coefficients (covering every higher degree), and interval bounds for the unique minimizer and minimum. The exponential upper bounds use a positive Taylor remainder bounded by a geometric tail, never a floating-point assumption. The printed numerical intervals are certified rational bounds. The checker does not replace the analytical proof of strict underdispersion or the zero-mass monotonicity; those arguments are given above.

## Relationship to prior work

Almuhayfith, Bapat, Bakouch and Alnaghmosh (2023) introduced the family and supplied its probability mass function, normalizer, mean, variance, and index of dispersion. Their paper describes the family as overdispersed and says that its dispersion index exceeds one, with a reported maximum near parameter \(1.4\). Here the same printed mass function instead implies a ratio below one and a *unique minimum* near \(1.4074\). This comparison is about the mathematically defined population law; it does not assert that the source's empirical fit computations were independently re-evaluated.

The broader weighted-Poisson principle that log-concave weights generate underdispersion is explicitly acknowledged (e.g. Puig, Valero and Fernández-Fontelo, first published 2023, Proposition 5, citing earlier work). It accounts for the sign of dispersion but supplies neither the model-specific global uniqueness certificate nor the sharp numerical dispersion minimum and zero-calibration range established here. Cahoy, Di Nardo and Polito (2021) likewise give general weighted-Poisson factorial-moment criteria; these do not specialize to this exact global optimization. Searches for the semi-Poisson model, equivalent weight, Fano-factor extremum, and corrected dispersion characterizations did not identify an earlier theorem with this complete claim. Absence from search results is not a guarantee of historical novelty.

## Limitations

The theorem is specific to the exact one-parameter distribution above. It does not characterize arbitrary zero-inflated modifications or rate mixtures, which may have different dispersion. The results are population identities; they neither invalidate the empirical datasets nor establish a definitive ranking against alternative fitted models. Related research outside the inspected materials may exist. Independent mathematical validation has not been performed.

## References

1. F. E. Almuhayfith, S. R. Bapat, H. S. Bakouch and A. M. Alnaghmosh, “A Flexible Semi-Poisson Distribution with Applications to Insurance Claims and Biological Data,” *Mathematics* 11 (2023), article 1122, published 23 February 2023. https://doi.org/10.3390/math11051122 . Accessible primary full text: https://www.researchgate.net/publication/368739367_A_Flexible_Semi-Poisson_Distribution_with_Applications_to_Insurance_Claims_and_Biological_Data .
2. P. Puig, J. Valero and A. Fernández-Fontelo, “Some mechanisms leading to underdispersion: Old and new proposals,” *Scandinavian Journal of Statistics* 51 (2024), 245–267; first published 7 August 2023, especially Section 3.2 and Proposition 5. https://doi.org/10.1111/sjos.12677 .
3. D. Cahoy, E. Di Nardo and F. Polito, “Flexible models for overdispersed and underdispersed count data,” *Statistical Papers* 62 (2021), 2969–2990; published 4 February 2021, especially Section 3. https://doi.org/10.1007/s00362-021-01222-7 .
4. “Poisson XRani Distribution: An Alternative Discrete Distribution for Overdispersed Count Data,” 2024, https://doi.org/10.1155/2024/5554949 . Considered for its discussion of the semi-Poisson model among count-data alternatives, not as a covering theorem.
