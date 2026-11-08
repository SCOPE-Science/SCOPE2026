# Fixed-size Good–Turing covariance can reverse the Poisson sign

## Finding

For a categorical law on a finite alphabet, take \(n\ge2\) independent draws, let \(N_i\) be the occupancy of category \(i\) of mass \(p_i\), and define missing mass \(M_n=\sum_i p_i\mathbf1_{\{N_i=0\}}\) and the Good–Turing singleton estimator \(G_n=n^{-1}\sum_i\mathbf1_{\{N_i=1\}}\). Their covariance is exactly
\[
\operatorname{Cov}(M_n,G_n)=
\sum_{i\ne j}p_ip_j(1-p_i-p_j)^{n-1}
-\left(\sum_i p_i(1-p_i)^n\right)
 \left(\sum_j p_j(1-p_j)^{n-1}\right).
\]

This covariance has **opposite possible signs at every fixed sample size** \(n\ge2\):

* Under the uniform law on \(a\ge2\) categories it is strictly negative, with exact value
\[
\frac{a-1}{a}\left[\left(1-\frac2a\right)^{n-1}
-\left(1-\frac1a\right)^{2n-2}\right]<0.
\]
* Fix any \(q\in(0,1)\). Under the core-and-diffuse-tail law on \(m+1\) categories with masses \(q\) and \((1-q)/m\), repeated \(m\) times, the covariance converges as \(m\to\infty\) to
\[
C_{n,q}=q^2(1-q)^n\left[1-(1-q)^{n-1}\right]>0.
\]
In fact the finite covariance differs from \(C_{n,q}\) in absolute value by at most
\[
\frac{2n(1-q)+n(n-1)(1-q)^2}{m}.
\]
Thus positivity holds for every integer \(m\) greater than that displayed numerator divided by \(C_{n,q}\).

By contrast, in the Poissonized model of expected sample size \(t>0\), define \(G_t=t^{-1}\sum_i\mathbf1_{\{N_i(t)=1\}}\) and \(M_t=\sum_i p_i\mathbf1_{\{N_i(t)=0\}}\). Then, for every finite categorical law,
\[
\operatorname{Cov}(M_t,G_t)=-\sum_i p_i^2e^{-2tp_i}<0.
\]
For the same core-and-diffuse-tail laws, the Poissonized covariance tends to \(-q^2e^{-2tq}<0\), even when \(t=n\). Thus Poissonization can reverse this estimator–target covariance sign at matched expected sample size.

For a concrete strictly positive fixed-size instance, \(n=3\), \(q=1/2\), and \(m=10\) give
\[
\operatorname{Cov}(M_3,G_3)=\frac{5801}{12800000}>0.
\]

## Assumptions and scope

All categories have fixed nonnegative probabilities summing to one; zero-mass categories may be removed. The finite-sample formula covers finite alphabets, \(n\ge2\). The uniform assertion assumes \(a\ge2\); the core-and-tail family assumes \(0<q<1\), integer \(m\ge1\), and fixed \(n\) in the limit. The Poissonized model uses independent category counts of means \(tp_i\), arising from a Poisson total sample size of mean \(t\). The assertions concern covariance, not Pearson correlation; no assertion of universal positivity under nonuniform laws is made.

## Proof

For distinct categories \(i,j\), independence of the original draws gives
\[
\Pr(N_i=0)= (1-p_i)^n,\qquad
\Pr(N_j=1)=np_j(1-p_j)^{n-1},
\]
\[
\Pr(N_i=0,N_j=1)=np_j(1-p_i-p_j)^{n-1}.
\]
The events \(N_i=0\) and \(N_i=1\) are disjoint. Multiplying by the masses and by the singleton normalization \(1/n\) yields the exact joint moment, and subtracting the product of expectations yields the first formula.

Under the uniform law \(p_i=1/a\), use \(a(1-1/a)=a-1\) to simplify that formula to the displayed result. For \(a\ge2\), \(0\le1-2/a<(1-1/a)^2\); raising to the positive integer \(n-1\) proves strict negativity.

For the core-and-tail law, couple all samples by first deciding independently whether each draw chooses the core (probability \(q\)) or the rare group (probability \(1-q\)), then choosing a uniform rare index among \(m\). Let \(K\sim\mathrm{Binomial}(n,q)\) count core draws. The probability that two of the \(n\) draws choose the same rare index is at most \(\binom n2(1-q)^2/m\), by the union bound. Define comparison variables
\[
M_*=(1-q)+q\mathbf1_{\{K=0\}},\quad
G_*=(n-K+\mathbf1_{\{K=1\}})/n.
\]
There are at most \(n\) distinct observed rare categories, so \(|M_n-M_*|\le n(1-q)/m\) deterministically; outside the rare-collision event \(G_n=G_*\). Both actual and comparison variables lie in \([0,1]\). The elementary inequality
\[
|\operatorname{Cov}(X,Y)-\operatorname{Cov}(X',Y')|
\le2\mathbb E|X-X'|+2\mathbb E|Y-Y'|
\]
for \([0,1]\)-valued variables gives the stated finite error bound.

Moreover, \(\mathbb EG_*=1-q+q(1-q)^{n-1}\) and \(\Pr(K=0)=(1-q)^n\). On \(K=0\) one has \(G_*=1\), so
\[
\operatorname{Cov}(M_*,G_*)
=q(1-q)^n\bigl(1-\mathbb EG_*\bigr)
=q^2(1-q)^n[1-(1-q)^{n-1}].
\]
This is positive exactly as claimed for every \(n\ge2\) and \(0<q<1\).

After Poissonization, each \(N_i(t)\) is an independent Poisson variable with mean \(tp_i\). For distinct categories the corresponding indicator terms are independent; within each category the singleton and empty indicators are mutually exclusive. Hence their covariance contribution is
\[
-\frac{p_i}{t}\Pr(N_i(t)=0)\Pr(N_i(t)=1)
=-p_i^2e^{-2tp_i}.
\]
Summation proves strict negativity and taking \(m\to\infty\) in the core-and-tail family yields \(-q^2e^{-2tq}\), since the rare terms have total magnitude at most \((1-q)^2/m\). Finally the finite example follows by direct rational substitution into the first formula.

## Verification

Run `python3 VERIFY.py` using Python's standard library only. It independently enumerates complete ordered samples for small alphabets, checks the derived uniform and two-level identities in exact rational arithmetic, checks the positive concrete example and finite error bound, and performs numerical sign checks of the Poisson formula. Its checks do not replace the exact derivation for arbitrary sample size.

## Relationship to prior work

The Good–Turing singleton estimator and missing mass, together with binomial and Poissonized occupancy models, are standard objects. Ben-Hamou, Boucheron, and Ohannessian (2014) give concentration and variance results for these objects and a Poissonized covariance-matrix calculation. Barbour and Gnedin (2008) study joint occupancy-count fluctuations and de-Poissonization. The negative Poissonized covariance is an immediate consequence of independent category counts, and the uniform fixed-size sign is also implied by previously published richness–singleton covariance results; **neither constituent fact is claimed as independently novel**. The specific contribution here is the all-sample-size nonuniform positive-covariance construction, with quantitative error, and its opposite sign under Poissonization at the same expected sample size. The cited inspected literature does not explicitly state that contrast, but implicit earlier coverage remains a priority risk.

## Limitations

The \(m\to\infty\) convergence holds with \(n,q\) fixed, not uniformly in growing sample size. The sufficient finite-\(m\) bound is conservative and does not identify optimal thresholds. The general exact covariance identity is a direct occupancy moment calculation, not a claim to a new general method. No complete classification of all category-weight profiles is asserted. Historical originality requires independent assessment; no independent audit has been performed.

## References

- A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme* (first public preprint 2008-09-25), https://arxiv.org/abs/0809.4387.
- A. Ben-Hamou, S. Boucheron, and M. I. Ohannessian, *Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications* (first public preprint 2014-12-30), https://arxiv.org/abs/1412.8652.
- D. Berend and A. Kontorovich, *On the Concentration of the Missing Mass* (first public preprint 2012-10-11), https://arxiv.org/abs/1210.3248.
