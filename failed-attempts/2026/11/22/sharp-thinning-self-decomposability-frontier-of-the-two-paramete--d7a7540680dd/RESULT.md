# Sharp thinning self-decomposability frontier of the two-parameter Poisson generalized Lindley law

## Finding

Let \(Y\) have the two-parameter Poisson generalized Lindley (PGL, also TPPGL) law with probability generating function
\[
G_{\alpha,\theta}(z)=\frac{\theta^\alpha(\theta+2-z)}{(\theta+1)(\theta+1-z)^\alpha},\qquad \alpha>1,\quad\theta>0.
\]
The law is **self-decomposable under independent Bernoulli thinning at every rate** if and only if
\[
\boxed{\alpha\ge A(\theta):=\frac{(\theta+1)^3}{\theta(\theta+2)^2}.}
\]
This is an inclusive sharp boundary. Equivalently, all admissible shapes \(\alpha>1\) work when \(\theta\ge (\sqrt5-1)/2\); below that rate, exactly \(\alpha\ge A(\theta)>1\) work. The law remains ordinarily compound Poisson even in the non-self-decomposable region.

In the allowed region the *unique* independent innovation at any thinning rate \(t\in(0,1)\) is explicitly compound Poisson: put \(q=(1+\theta)^{-1}\), \(r=(2+\theta)^{-1}\), and \(q_t=qt/(1-q+qt)\), \(r_t=rt/(1-r+rt)\). Its jump intensities are
\[
\boxed{\nu_k(t)=\frac{\alpha(q^k-q_t^k)-(r^k-r_t^k)}{k}>0,\qquad k=1,2,\ldots.}
\]
In the excluded region some thinning rate has **no nonnegative integer-valued innovation distribution**, and its prospective probability of one is negative. A rational witness is \(\theta=2/49\), \(\alpha=17/10\), \(t=1/2\), for which the logarithmic coefficient is \(\nu_1(1/2)=-249361/2400900<0\).

## Assumptions and scope

The parameters range over \(\theta>0\) and real \(\alpha>1\), the domain of the original gamma-mixture PGL law. The variable \(Y\) is nonnegative integer-valued. For \(t\in(0,1)\), the thinning \(t\circ Y'\) is the sum of \(Y'\) independent Bernoulli\((t)\) variables, where \(Y'\) has the same law as \(Y\) and is independent of the innovations. By definition, self-decomposability here means that for *every* \(t\in(0,1)\) there is an independent \(E_t\) such that \(Y\overset d=t\circ Y'+E_t\), or equivalently that \(H_t(z):=G(z)/G(1-t+tz)\) is a probability generating function. This does **not** mean ordinary additive self-decomposability on the real line and does not claim that the innovations themselves have PGL laws.

## Proof

**Step 1: compound-Poisson canonical coefficients.** Since \(0<r<q<1\), direct factorization gives
\[
G_{\alpha,\theta}(z)=G_{\alpha,\theta}(0)\frac{1-rz}{(1-qz)^\alpha},\quad G_{\alpha,\theta}(0)=\frac{(1-q)^\alpha}{1-r}.
\]
Taking the power-series logarithm at zero and using \(G(1)=1\) yields the absolutely convergent expansion on \(|z|\le1\)
\[
\log G(z)=\sum_{k\ge1}\lambda_k(z^k-1),\quad\lambda_k=\frac{\alpha q^k-r^k}{k}>0.
\]
Summability follows from \(q<1\), and positivity follows from \(\alpha>1\) and \(q>r\). Thus every law in the original parameter domain is compound Poisson, regardless of the new boundary.

**Step 2: exact thinning innovations.** For \(0<t<1\), define \(q_t=qt/(1-q+qt)\), \(r_t=rt/(1-r+rt)\). Replacing \(z\) in \(G\) by \(1-t+tz\) and expanding the same logarithms gives
\[
\log H_t(z)=\sum_{k\ge1}\nu_k(t)(z^k-1),\qquad
\nu_k(t)=\frac{\alpha(q^k-q_t^k)-(r^k-r_t^k)}{k}.
\]
The series is absolutely summable because \(0<q_t<q<1\) and \(0<r_t<r<1\). If all \(\nu_k(t)\ge0\), this is exactly a compound-Poisson PGF and hence a valid independent innovation law; conversely, a negative first coefficient implies \(H_t'(0)<0\), forbidding any PGF.

**Step 3: uniform positivity at the proposed boundary.** For \(0<s\le1\), write \(q_s=qs/(1-q+qs)\), \(r_s=rs/(1-r+rs)\). Their derivatives are
\[
q_s'=\frac{q(1-q)}{(1-q+qs)^2},\qquad r_s'=\frac{r(1-r)}{(1-r+rs)^2}.
\]
Since \(0<r_s<q_s\) and \(1-q+qs<1-r+rs\) for \(0<s<1\),
\[
\frac{r_s^{k-1}r_s'}{q_s^{k-1}q_s'}
=\left(\frac{r_s}{q_s}\right)^{k-1}
\frac{r(1-r)}{q(1-q)}
\left(\frac{1-q+qs}{1-r+rs}\right)^2
<\frac{r(1-r)}{q(1-q)}=A(\theta)
\]
for every integer \(k\ge1\) and \(0<s<1\). Moreover,
\[
\nu_k(t)=\int_t^1\bigl(\alpha q_s^{k-1}q_s'-r_s^{k-1}r_s'\bigr)\,ds.
\]
Thus \(\alpha\ge A(\theta)\) makes *every* \(\nu_k(t)\) strictly positive for every \(k\ge1\), \(0<t<1\), including equality \(\alpha=A(\theta)\). The compound-Poisson representation gives sufficiency with no finite-truncation assumption.

**Step 4: necessity and the sharp phase line.** If \(\alpha<A(\theta)\), then \(\alpha q(1-q)-r(1-r)<0\). For \(k=1\), the continuous integrand in Step 3 is therefore negative at \(s=1\), and remains negative on some left neighborhood of one. Choosing \(t\) in that neighborhood gives \(\nu_1(t)<0\), hence \(H_t'(0)=H_t(0)\nu_1(t)<0\); \(H_t\) cannot be a PGF. Finally,
\[
A(\theta)-1=\frac{1-\theta-\theta^2}{\theta(\theta+2)^2},
\]
so \(A(\theta)\le1\) exactly when \(\theta\ge(\sqrt5-1)/2\). This proves all assertions and includes both boundary regimes.

**Step 5: exact overlap with a previously studied count model.** The weighted negative-binomial Lindley (WNBL) PGF of Bakouch (2018) is
\[
B_{p,\beta}(z)=\frac{(1-p)^{\beta+1}\{1+p(\beta^2-1)z\}}{\{1+p(\beta^2-1)\}(1-pz)^{\beta+1}},\qquad0<p<1,\ \beta>0.
\]
At \(p=49/51\), \(\beta=7/10\), this is exactly \(G_{17/10,\,2/49}(z)\): the denominator exponent is \(17/10\), \(p=q=49/51\), and \(p(1-\beta^2)=49/100=r\). The rational witness above proves that this specific WNBL parameter pair is *not* thinning self-decomposable; it supplies a counterexample to the blanket self-decomposability assertion in the 2018 article without asserting that its other properties or every subfamily member fail.

## Verification

The accompanying standalone \(\texttt{check.py}\) uses exact Python fractions, with no numerical tolerance, to verify the canonical-coefficient identity, the inclusive equality case at \(\theta=1/4\), and a negative first innovation logarithmic coefficient at the rational exclusion witness. It also samples many positive coefficients on the allowed side. These finite checks support transcription and arithmetic; the infinite statements follow from the inequalities in Steps 3 and 4, not from enumeration. Reproduce with \(\texttt{python3 check.py}\).

## Relationship to prior work

The PGL/TPPGL law and its PGF were introduced by Irshad et al. (published online 20 January 2023) and independently developed by Atikankul (2023). Their count-time-series applications, and Rasheed et al.'s 2024 extension, employ the PGL count law *as the independent INAR innovation*. That construction does not require or determine when PGL is itself an invariant stationary marginal of an INAR process; the present theorem solves the latter all-thinning marginal feasibility question. The 1979 Steutel–van Harn canonical-sequence theorem gives a general criterion (nonincreasing coefficients of \(G'/G\)); the explicit family-specific sharp phase diagram and compound-Poisson innovations are not asserted by that general theorem alone. Bakouch (2018) has a WNBL family overlapping a one-dimensional subset of the PGL model and asserts general self-decomposability; Step 5 proves a direct rational counterexample on that overlap. Vardaki–Papageorgiou (REVSTAT, accepted/in press by 2025) discuss PGL convolution identities and bivariate extensions but not the marginal thinning threshold. Altun's identically named 2021 Poisson-generalized Lindley distribution has a different PGF and is not silently identified with this model.

## Limitations

This theorem concerns binomial-thinning self-decomposability on nonnegative integer counts, not continuous self-decomposability, general multivariate autoregressions, or uniqueness of stationary processes under all possible dynamics. An all-thinning invariant marginal permits independent innovations that depend on the chosen thinning rate; these innovations need not remain within the original PGL parametric family. The historical-originality comparison cannot rule out an unindexed older calculation or unpublished result. One closely related 2023 article was available only through metadata/abstract and the 2024 full-text synopsis, so no claim is made about its unseen full text. The 2018 overlap witness only disproves the blanket claim for the explicitly specified parameter pair.

## References

1. M. R. Irshad, V. D'Cruz, R. Maya and N. Mamode Khan, *Inferential properties with a novel two parameter Poisson generalized Lindley distribution with regression and application to INAR(1) process*, Journal of Biopharmaceutical Statistics 33 (2023), 335–356; online 20 January 2023. https://doi.org/10.1080/10543406.2022.2152832
2. W. Atikankul, *A New Poisson Generalized Lindley Regression Model*, Austrian Journal of Statistics 52 (2023). https://www.ajs.or.at/index.php/ajs/article/download/1344/775
3. F. W. Steutel and K. van Harn, *Discrete analogues of self-decomposability and stability*, Annals of Probability 7 (1979), 893–899. https://doi.org/10.1214/aop/1176994950
4. H. S. Bakouch, *A weighted negative binomial Lindley distribution with applications to dispersed data*, Anais da Academia Brasileira de Ciências 90 (2018), 2617–2642. https://doi.org/10.1590/0001-3765201820170733
5. I. M. Rasheed, V. D'Cruz, M. Radhakumari, S. A. Devi and N. M. Khan, *Bivariate Poisson Generalized Lindley Distributions and the Associated BINAR(1) Processes*, Austrian Journal of Statistics 53 (2024), 1–28. https://doi.org/10.17713/ajs.v53i1.1551
6. M. Vardaki and H. Papageorgiou, *On a Poisson Generalized Lindley Distribution: Related Models, Bivariate Extensions and Insurance Applications*, REVSTAT (in-press manuscript, no verified issue date). https://revstat.ine.pt/index.php/REVSTAT/article/download/798/771/4242
