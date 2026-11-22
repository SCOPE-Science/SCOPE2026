# Two geometric boundary Poisson laws and exact conditional calibration for a zero-frequency goodness-of-fit test

## Finding

Let \(n\ge2\), \(0<p_n<1\), and let \(X_{n,1},\ldots,X_{n,n}\) be independent geometric random variables on \(\{0,1,2,\ldots\}\), with
\[
\Pr(X_{n,i}=j)=p_n(1-p_n)^j,\qquad j=0,1,\ldots.
\]
Put \(q_n=1-p_n\), \(S_n=\sum_i X_{n,i}\), \(K_n=\sum_i\mathbf1_{\{X_{n,i}=0\}}\), \(\widehat p_n=n/(n+S_n)\), and define the geometrically studentized zero-frequency statistic of Di Noia et al. by
\[
Z_n=\frac{\sqrt n(\widehat p_n-K_n/n)}{(1-\widehat p_n)\sqrt{\widehat p_n}}
\quad\text{if }S_n>0,\qquad Z_n=0\quad\text{if }S_n=0.
\]

**Theorem (sharp two-boundary phase diagram).** For *arbitrary* parameter sequences \((p_n)\subset(0,1)\):

1. \(Z_n\Rightarrow N(0,1)\) **if and only if** both \(np_n\to\infty\) and \(nq_n^2\to\infty\).
2. If \(np_n\to\lambda\in(0,\infty)\), then \(Z_n\Rightarrow (\lambda-P_\lambda)/\sqrt\lambda\), with \(P_\lambda\sim\mathrm{Poisson}(\lambda)\). If \(np_n\to0\), then \(Z_n\to0\) in probability.
3. If \(nq_n^2\to\lambda\in(0,\infty)\), the **same** centered Poisson limit holds; if \(nq_n^2\to0\), then \(Z_n\to0\) in probability. Thus the opposite endpoints have different critical scales but the same limit family.

**Exact finite-sample conditional calibration.** For every integer \(s\ge1\), conditioning on \(S_n=s\) eliminates the unknown parameter:
\[
\Pr(K_n=k\mid S_n=s)=
\frac{\binom nk\binom{s-1}{n-k-1}}{\binom{n+s-1}{n-1}}
\]
for feasible \(k\) (namely \(0\le k\le n-1\) and \(n-k\le s\)); all other conditional probabilities are zero. For observed \((s,k)\), define \(H(s)=n^2/(n+s)\) and sum these masses over feasible \(j\) satisfying \(|j-H(s)|\ge|k-H(s)|\). The resulting exact conditional two-sided \(p\)-value is superuniform under the geometric model, for every \(n\) and \(p_n\), with \(p\)-value one when \(s=0\). The conditional composition formula is elementary; the novel target is the coupled sharp phase diagram and its calibration implication for this published statistic.

For a conventional nominal two-sided \(5\%\) normal critical value \(c=\Phi^{-1}(0.975)\), put
\[
\lambda_*(c)=\left(\frac{\sqrt{c^2+4}-c}{2}\right)^2\approx0.176524554935.
\]
At either endpoint, whenever \(0<\lambda<\lambda_*(c)\), the limiting normal-calibrated rejection probability is \(1-e^{-\lambda}\), tending to \(0.161821802509\) as \(\lambda\uparrow\lambda_*(c)\). Thus the nominal \(5\%\) procedure can have limiting null rejection probability arbitrarily close to \(16.18\%\); no global supremum over all \(\lambda\) is claimed.

## Assumptions and scope

The observations are iid within each row, but their common geometric success probability \(p_n\) may change arbitrarily with sample size. The test is the specifically defined zero-frequency-versus-fitted-geometric-probability statistic, with the sample-mean fit and the plug-in variance used by Di Noia et al. The model has no truncation or covariates. The convention at \(S_n=0\) is part of the definition and is necessary near the degenerate endpoint. Normal convergence is weak convergence on the real line; the results do not assert uniform tail approximation in shrinking significance levels. The two Poisson cases apply to disjoint endpoint sequences, not a joint same-sequence limit.

## Proof

**1. Exact algebra and the two sparse mechanisms.** Temporarily write \(p=p_n\), \(q=1-p\), \(S=S_n\), and \(K=K_n\). Put \(J=n-K=\sum_i\mathbf1_{\{X_i\ge1\}}\) and \(D=S-J=\sum_i(X_i-1)_+\). The deterministic identities
\[
H:=n\widehat p=\frac{n^2}{n+S},\qquad
H-K=\frac{S^2}{n+S}-D,
\]
\[
Z_n=\frac{H-K}{q_{\rm fit}\sqrt H},\qquad
q_{\rm fit}\sqrt H=\frac{Sn}{(n+S)^{3/2}},\quad
q_{\rm fit}=\frac S{n+S},
\]
hold if \(S>0\). The identities expose two different rare-event counts: \(K\) for \(p\downarrow0\), and \(D\) for \(q\downarrow0\).

**2. High-mean endpoint \(np\to\lambda\).** Since \(\mu=q/p\) and \(\mathrm{Var}(p\overline X)=q/n\),
\[
\frac{\widehat p}{p}=\frac1{1+p(\overline X-\mu)}\longrightarrow1
\quad\text{in probability}.
\]
Thus \(H-np\to0\) in probability whenever \(np\) remains bounded, and \(q_{\rm fit}\to1\). Meanwhile \(K\sim\mathrm{Binomial}(n,p)\Rightarrow P_\lambda\) if \(\lambda>0\). Slutsky's theorem gives \(Z_n\Rightarrow(\lambda-P_\lambda)/\sqrt\lambda\). If \(\lambda=0\), then \(\Pr(K>0)\le np\to0\). On \(K=0\), \(Z_n=\sqrt H/q_{\rm fit}\to0\) in probability, proving the stated degeneration.

**3. Low-mean endpoint \(nq^2\to\lambda\).** Here \(q\to0\). Let \(B=\sum_i\mathbf1_{\{X_i\ge2\}}\). Since \(B\sim\mathrm{Binomial}(n,q^2)\), \(B\Rightarrow P_\lambda\) for \(\lambda>0\). The event \(D\ne B\) requires some \(X_i\ge3\), with probability at most \(nq^3=(nq^2)q\to0\). Thus \(D\Rightarrow P_\lambda\). For \(\lambda>0\), \(nq\to\infty\), and
\[
\frac S{nq}\longrightarrow1\quad\text{in probability},
\qquad\frac{S^2}{n+S}\longrightarrow\lambda,
\qquad\frac{Sn}{(n+S)^{3/2}}\longrightarrow\sqrt\lambda.
\]
The first convergence follows from \(\mathbb E S=nq/p\) and \(\operatorname{Var}(S)=nq/p^2\). The exact algebra in step 1 proves the second Poisson limit. If \(\lambda=0\), \(\Pr(D>0)\le nq^2\to0\); on \(D=0\), \(Z_n=S\sqrt{n+S}/n\) (or zero for \(S=0\)). Since \(\mathbb E(S/\sqrt n)=\sqrt n q/p\to0\) and \(S/n\to0\) in probability, \(Z_n\to0\).

**4. Gaussian regime: sufficiency.** Define the rowwise score
\[
Y_i=p^2(X_i-q/p)+(\mathbf1_{\{X_i=0\}}-p).
\]
Direct moments of the geometric distribution yield \(\mathbb EY_i=0\) and
\[
\operatorname{Var}(Y_i)=p q^2.
\]
For \(p\le1/2\), \(\mathbb E|Y_i|^3\le C p\): use \(\mathbb E X_i^3=O(p^{-3})\), \(p^2X_i\) of third absolute moment \(O(p^3)\), and the centered zero indicator with third absolute moment \(O(p)\). For \(p\ge1/2\), \(\mathbb E|Y_i|^3\le C q^2\): on \(X_i=0\) the score equals \(q^2\), on \(X_i=1\) it equals \(-2pq\), and the total \(\sum_{j\ge2}p q^j|Y_i(j)|^3\) is \(O(q^2)\). Consequently, Lyapunov's ratio is bounded by \(C/\sqrt{np}\) for \(p\le1/2\), and by \(C/\sqrt{nq^2}\) for \(p\ge1/2\). Both tend to zero under the two asserted conditions, so
\[
-\frac{\sum_iY_i}{\sqrt{npq^2}}\Rightarrow N(0,1).
\]
For \(\delta=\overline X-q/p\) the exact expansion
\[
\widehat p-p=-p^2\delta+\frac{p^3\delta^2}{1+p\delta}
\]
has standardized remainder \(o_P(1)\): \(\operatorname{Var}(p\delta)=q/n\), and on \(|p\delta|\le1/2\) its expected absolute value after multiplication by \(\sqrt n/(q\sqrt p)\) is at most \(2\sqrt p/\sqrt n\). Also \(\widehat p/p\to1\) and \((1-\widehat p)/q\to1\), since \(\operatorname{Var}(\overline X/(q/p))=1/(nq)\) and \(nq\to\infty\). Hence studentization preserves the normal limit.

**5. Gaussian regime: necessity.** If \(np_n\not\to\infty\), a subsequence satisfies \(np_n\to\lambda\in[0,\infty)\), and therefore \(p_n\to0\). Step 2 gives a nonnormal (lattice or degenerate) subsequential limit. If \(nq_n^2\not\to\infty\), some subsequence has \(nq_n^2\to\lambda\in[0,\infty)\) and hence \(q_n\to0\), and step 3 likewise gives a nonnormal limit. A sequence converging to a standard normal cannot have such a subsequence. This proves the equivalence without an assumed limit for \(p_n\).

**6. Exact calibration and size calculation.** For \(s\ge1\) and a feasible zero count \(k\), exactly \(n-k\) coordinates are positive. There are \(\binom nk\binom{s-1}{n-k-1}\) nonnegative integer \(n\)-vectors of total \(s\) with \(k\) zeros. Every such vector has the same geometric null mass \(p^nq^s\). Dividing by the \(\binom{n+s-1}{n-1}\) weak compositions of \(s\) proves the conditional law and its parameter independence. Since the conditional test tail is computed under its true finite null distribution, its p-value is superuniform conditional on every \(S=s\), and hence unconditionally.

For \(0<\lambda<\lambda_*(c)\), the centered Poisson limit has \(\sqrt\lambda<c\) when \(P_\lambda=0\), and \((k-\lambda)/\sqrt\lambda>c\) for every integer \(k\ge1\). No limiting atom lies on the critical boundary. Thus the rejection probability converges to \(\Pr(P_\lambda\ge1)=1-e^{-\lambda}\) in either endpoint regime. Solving \((1-\lambda)/\sqrt\lambda=c\) gives the displayed \(\lambda_*(c)\). The numerical value is evaluated from the standard normal quantile and the exponential function.

## Verification

The standalone \`check.py\` reconstructs exact algebra for every tuple of length \(2\) through \(5\) with entries from \(\{0,1,2,3,4\}\), checks the score variance at rational parameter values, verifies the composition normalizer and conditional p-value superuniformity by exact fractions over finite ranges, and independently simulates both rare-boundary regimes using the exact conditional positive-geometric law. It reports **13,626 passed assertions**. Simulations corroborate but do not prove infinite-sequence statements; the analytic proof above does. A critical computational precaution is to calculate \(H-K\) as \(S^2/(n+S)-D\) near \(p=1\), avoiding catastrophic subtraction of two large nearly equal quantities.

## Relationship to prior work

Di Noia, Barabesi, Marcheselli, Pisani, and Pratelli introduced the count-distribution test in arXiv:2112.11861 (first posted December 22, 2021). Its Proposition 3.1 gives fixed-parameter asymptotic normality, and its geometric-family subsection gives exactly the studentizing variance used here. The paper's simulation study evaluates fixed moderate sample sizes and parameter values; its published statement does not include a triangular-parameter phase diagram, the sparse-doubleton endpoint mechanism, the necessary-and-sufficient two-threshold normality criterion, or the resulting null-level inflation. The conditional composition identity itself follows from standard occupancy counting and is not asserted to be a new combinatorial identity. General triangular-array central limit and Poisson convergence results are used as known ingredients; the new claim concerns their **specific sharp interaction** in this fitted statistic. The 2026 paper on p.g.f.-based binomial-count tests concerns a different bounded family and distinct statistics. Literature and mathematical-record searches found no directly implying published claim, but the possibility of implicit coverage by broader older general asymptotic theory remains.

## Limitations

No uniform-in-parameter numerical error bound, convergence rate for critical laws, corrected joint-estimation power theorem, global maximal type-I inflation, or new estimator is claimed. At exactly the Poisson atom-equals-critical-value parameter, weak convergence alone does not determine an asymptotic strict-inequality rejection probability; the stated size formula uses strictly subcritical intensities. A conventional conditional p-value may be conservative because the null law is discrete. Literature search cannot certify historical uniqueness.

## References

1. A. Di Noia, L. Barabesi, M. Marcheselli, C. Pisani, L. Pratelli, *Goodness-of-fit test for count distributions with finite second moment*, arXiv:2112.11861 (first public posting 2021-12-22; later revisions): https://arxiv.org/abs/2112.11861 and full text https://arxiv.org/html/2112.11861.
2. Same authors, *Journal of Nonparametric Statistics* 35 (2023), 19–37, first published online October 27, 2022, https://doi.org/10.1080/10485252.2022.2137728.
3. *Pgf-based goodness-of-fit tests for binomial counts* (2026), https://doi.org/10.1007/s00184-025-01009-y (context for other count-data p.g.f. procedures, not a source of the theorem).
