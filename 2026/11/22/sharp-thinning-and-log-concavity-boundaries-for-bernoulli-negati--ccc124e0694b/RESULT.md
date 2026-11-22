# Sharp thinning and log-concavity boundaries for Bernoulli–negative-binomial counts

## Finding
Let \(X=B+N\), with independent \(B\sim\operatorname{Bernoulli}(p)\) and \(N\sim\operatorname{NB}(\nu,\theta)\), parameterized by
\[\Pr(N=k)=(1-\theta)^\nu\frac{(\nu)_k}{k!}\theta^k,\qquad k=0,1,\ldots.\]
Assume \(\nu>0\), \(0<\theta<1\), and \(0<p<1\), and set \(r=p/(1-p)\). Then the following classifications are sharp, including equality at the boundaries:

The classical infinite-divisibility threshold for this Bernoulli--negative-binomial convolution is known in substance from Letac, Malouche and Maurer (2002), whose real-convolution-powers classification covers it: \(r\le\theta\) and \(r^2\le\nu\theta^2\), with logarithmic pgf coefficients \(\lambda_k=[\nu\theta^k+(-1)^{k-1}r^k]/k\). This known threshold is used below as context, **not asserted as a new discovery**. The new classifications are:

1. Discrete self-decomposability under independent Bernoulli thinning, defined by the requirement that \(G(z)/G(1-a+az)\) is a probability generating function for every \(0<a<1\), holds **if and only if**
\[\boxed{r\leq\theta\quad\text{and}\quad\nu(1-\theta)\theta^2\geq(1+r)r^2.}\]
2. Global log-concavity of the probability masses holds **if and only if**
\[\boxed{\nu\geq1.}\]
For \(0<\nu<1\), their logarithms are eventually strictly convex. The latter gives the exact domain in which the log-concavity argument in Ong--Sim--Liu--Srivastava (2023, Section 2.6) applies; without this shape restriction its unconditional conclusion is false.

These properties differ even among overdispersed members of the family: the regimes of infinite divisibility without thinning self-decomposability, thinning self-decomposability without log-concavity, and log-concavity without infinite divisibility are all nonempty.

## Assumptions and scope
The notation \(\operatorname{NB}(\nu,\theta)\) denotes the zero-based negative binomial count law with the above mass; it includes all **real** \(\nu>0\). The probability generating function (pgf), normalized at \(z=1\), is
\[G(z)=(1-p+pz)\left(\frac{1-\theta}{1-\theta z}\right)^\nu.\]
Additive infinite divisibility means that, for every positive integer \(m\), the law of \(X\) is the convolution of \(m\) identically distributed laws supported on \(\mathbb N_0\). Discrete self-decomposability is the binomial-thinning definition stated above, not self-decomposability for ordinary multiplication of real random variables. Log-concavity means \(f_k^2\ge f_{k-1}f_{k+1}\) for **every** \(k\ge1\), with \(f_k=\Pr(X=k)>0\).

## Proof
**Step 1: classical logarithmic coefficients, reproduced as a lemma.** Since \(G(0)=(1-p)(1-\theta)^\nu>0\), the formal Taylor expansion at zero is unique. Writing \(r=p/(1-p)\),
\[\log G(z)=\log G(0)+\log(1+rz)-\nu\log(1-\theta z)
=\log G(0)+\sum_{k\ge1}\frac{\nu\theta^k+(-1)^{k-1}r^k}{k}z^k.\]
The classical compound-Poisson characterization of nonnegative-integer infinitely divisible laws with positive atom at zero (Steutel--van Harn, 1979, Lemma 1.2) states that all such logarithmic coefficients must be nonnegative, and conversely nonnegative summable coefficients give a compound-Poisson law. Every odd coefficient is positive. Even coefficients are
\[\lambda_{2j}=\frac{\nu\theta^{2j}-r^{2j}}{2j},\qquad j\ge1.\]
If \(r>\theta\), the ratio \((r/\theta)^{2j}\) eventually exceeds \(\nu\), hence an even coefficient is negative. If \(r\le\theta\), all even coefficients are nonnegative precisely when the first, \(\lambda_2\), is nonnegative: \(r^2\le\nu\theta^2\). In that case \(r\le\theta<1\) ensures \(\sum_k\lambda_k<\infty\); normalization at \(z=1\) gives \(G(z)=\exp\{\sum_{k\ge1}\lambda_k(z^k-1)\}\). This reproduces the known infinite-divisibility boundary as a prerequisite, including equality cases; that boundary is not claimed to be original here.

**Step 2: the sharp thinning condition.** In the above notation the canonical measure is the coefficient sequence of \(G'(z)/G(z)\):
\[b_k=k\lambda_k=\nu\theta^k+(-1)^{k-1}r^k,\qquad k\ge1.\]
The discrete self-decomposability characterization of Steutel--van Harn (1979, Theorem 2.2) is exactly that this nonnegative canonical sequence is nonincreasing. Its consecutive differences are
\[b_k-b_{k+1}=\begin{cases}
\nu(1-\theta)\theta^k+(1+r)r^k,&k\text{ odd},\\
\nu(1-\theta)\theta^k-(1+r)r^k,&k\text{ even}.
\end{cases}\]
All odd-index differences are positive. If \(r>\theta\), even-index differences are negative for all sufficiently large even \(k\). If \(r\le\theta\), the even-index differences are nonnegative for every even \(k\ge2\) precisely when they are nonnegative at \(k=2\), namely \(\nu(1-\theta)\theta^2\ge(1+r)r^2\). This condition also implies the classical infinite-divisibility condition, since \((1+r)/(1-\theta)>1\), so the canonical coefficients are nonnegative. The thinning characterization therefore yields the first new boundary on the entire stated region, with no unproved extension from finite coefficients.

**Step 3: complete log-concavity classification.** Put \(a_k=(1-\theta)^\nu(\nu)_k\theta^k/k!\), with \(a_{-1}=0\). For \(\nu\ge1\), the ratios \(a_{k+1}/a_k=\theta(k+\nu)/(k+1)\) are nonincreasing in \(k\). Thus the negative-binomial masses are log-concave. Bernoulli masses are log-concave, and convolution preserves log-concavity of positive sequences with interval supports; hence \(f_k=(1-p)a_k+pa_{k-1}\) is log-concave.

For \(0<\nu<1\), express the positive masses, for \(k\ge1\), as
\[f_k=(1-\theta)^\nu\frac{\Gamma(k+\nu)}{\Gamma(\nu)\Gamma(k+1)}\theta^k
\left(1-p+\frac{pk}{\theta(k+\nu-1)}\right).\]
Stirling's full inverse-power expansion for the Gamma ratio, together with the rational last factor, gives a positive constant \(C\) and constants \(c_1,c_2\) such that
\[\log f_k=k\log\theta+(\nu-1)\log k+C+\frac{c_1}{k}+\frac{c_2}{k^2}+O(k^{-3}).\]
The expansion continues to arbitrarily high inverse powers, so taking symmetric second differences preserves the remainder order. In particular,
\[\log f_{k+1}-2\log f_k+\log f_{k-1}=\frac{1-\nu}{k^2}+O(k^{-3})>0\]
for every sufficiently large integer \(k\). Thus \(f_k^2<f_{k-1}f_{k+1}\) eventually, and global log-concavity is impossible. This includes all interior \(p\), irrespective of how close to one it is.

**Step 4: independence of the boundaries.** With \(\theta=1/2\), the parameter triples \((\nu,p)=(2,1/4),(1,1/4),(1,2/5),(1/4,1/10)\) give, respectively, (i) all three properties, (ii) infinitely divisible but not thinning self-decomposable, (iii) log-concave but not infinitely divisible, and (iv) thinning self-decomposable but not log-concave. For each, \(\operatorname{Var}(X)-\mathbb E X=\nu\theta^2/(1-\theta)^2-p^2>0\), verifying that these examples can all be overdispersed. Every comparison above is a strict rational inequality except the positive membership classifications; no simulation is involved.

## Verification
A standalone Python 3 checker (`verify.py`) uses only standard-library exact fractions to reconstruct the pgf recursion through degree 22, verify nonnegative compound-Poisson coefficients and nonincreasing canonical measures on specified parameter grids, and confirm four rational regime-separating examples. Running `python3 verify.py` produced **9,791 exact-rational diagnostic assertions** with no failures. These finite diagnostics do not prove the all-degree or eventual-asymptotic results; Steps 1--3 are the proofs.

## Relationship to prior work
Ong, Sim, Liu and Srivastava (2023, their Sections 2.1--2.6) introduce the same pgf, study dispersion, estimation and mass-shape claims, but do not state the additive-divisibility or binomial-thinning phase boundaries. Their Section 2.6 argues global log-concavity using a convolution theorem without restricting the negative-binomial shape to \(\nu\ge1\). The present eventual-curvature argument supplies the missing sharp restriction.

Letac, Malouche and Maurer (2002) explicitly study real convolution powers of the **same Bernoulli--negative-binomial law**, so the corresponding infinite-divisibility cutoff is historical prior art, not part of the new contribution. Ben Salah (2021) develops more general real-power convolution theory; its abstract explicitly includes the negative-binomial case, and its full text was not accessible for a decisive comparison with the thinning boundary. Aoyama, Shimizu and Ong (2008, Section 4.2) discuss a generalized shifted inverse trinomial law including binomial--negative-binomial convolutions for integer shape; their formulas overlap the underlying family, not the classifications here. Steutel and van Harn (1979) supply the **general** canonical criteria for infinite divisibility and discrete self-decomposability; these criteria are not claimed to be new. The contribution claimed here is the explicit **thinning-self-decomposability** cutoff and the corrected **global log-concavity** cutoff, along with exact strict separation examples; the additive-infinite-divisibility cutoff is acknowledged as known from 2002. Relevant recent work on zero-inflated negative-binomial laws and folded discrete Laplace laws treats different pgfs and does not imply these boundaries.

## Limitations
The theorem is for independent Bernoulli and zero-based negative-binomial summands with strictly interior Bernoulli and negative-binomial probabilities and arbitrary positive real shape. It does not classify other finite mixtures, multivariate laws, ordinary real-line self-decomposability, or estimation performance. Numerical examples do not establish the infinite statements. The 2002 real-power result covers the classical additive-divisibility boundary. The 2021 real-power article remains a relevant inaccessible historical comparison; no novelty is claimed for generic power criteria, and earlier specialized thinning results remain a residual risk. No independent audit is asserted.

## References
- S. H. Ong, S. Z. Sim, S. Liu and H. M. Srivastava, “A Family of Finite Mixture Distributions for Modelling Dispersion in Count Data,” *Stats* **6** (2023), 942--955, first publicly posted 18 September 2023, https://doi.org/10.3390/stats6030059.
- G. Letac, D. Malouche and S. Maurer, “The Real Powers of the Convolution of a Negative Binomial Distribution and a Bernoulli Distribution,” *Proc. Amer. Math. Soc.* **130** (2002), 2107--2114, electronically published 8 February 2002, https://doi.org/10.1090/S0002-9939-02-05352-2.
- N. Ben Salah, “Generalized Convolution Product of an Infinitely Divisible Distribution and a Bernoulli Distribution,” *Communications in Statistics - Theory and Methods* **51** (2022), 7297--7304, first online 1 February 2021, https://doi.org/10.1080/03610926.2021.1879863 (abstract consulted; full text inaccessible).
- F. W. Steutel and K. van Harn, “Discrete Analogues of Self-Decomposability and Stability,” *Annals of Probability* **7** (1979), 893--899, Lemma 1.2 and Theorem 2.2, https://pure.tue.nl/ws/files/1956807/Metis199408.pdf.
- T. Aoyama, R. Shimizu and S. H. Ong, “A First-Passage Time Random Walk Distribution with Five Transition Probabilities: A Generalization of the Shifted Inverse Trinomial,” *Annals of the Institute of Statistical Mathematics* **60** (2008), 1--20, Section 4.2, https://www.ism.ac.jp/editsec/aism/pdf/060_1_0001.pdf.
- “Flexible Bivariate Generalized Shifted Inverse Trinomial Distributions,” *Stats* **9** (2026), Article 79, https://www.mdpi.com/2571-905X/9/4/79 (related bivariate extension, not a source for the new conclusions).
