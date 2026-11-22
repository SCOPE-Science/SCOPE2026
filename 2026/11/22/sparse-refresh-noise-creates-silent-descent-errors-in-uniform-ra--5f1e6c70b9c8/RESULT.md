# Sparse refresh noise creates silent descent errors in uniform random rankings

## Finding

Independently refresh each of the continuous scores underlying a uniform random ranking with probability \(p\). Let \(D\) and \(D'\) be the descent counts before and after the refresh, \(\Delta=D'-D\), and let \(H\) count positions where the descent indicator changes. For every \(n\ge2\) and \(0\le p\le1\),

\[
\operatorname{Cov}(D,D')=\frac{(1-p)((n+1)-(n-1)p)}{12},\qquad
\operatorname{Var}(\Delta)=\frac{p(2n-(n-1)p)}6,
\]

\[
\mathbb E H=(n-1)\left(\frac{2p}{3}-\frac{p^2}{6}\right).
\]

At the critical sparse-refresh scale \(np_n\to\lambda\in[0,\infty)\), let \(N_+,N_-,N_2\) be independent Poisson variables of mean \(\lambda/6\). Then the **joint**, integer-valued law obeys

\[
d_{\rm TV}\left(\mathcal L(\Delta,H),\mathcal L(N_+-N_-,N_++N_-+2N_2)\right)\longrightarrow0.
\]

More quantitatively, for each \(n\ge2\), \(p\in[0,1]\), and \(\lambda\ge0\), this total-variation distance is at most

\[
2p+\frac52 np^2+\frac12|np-\lambda|.
\]

Thus \(\Delta\) has the symmetric Skellam limit, while \(H\) is a sum of independent \(\operatorname{Poisson}(\lambda/3)\) and twice \(\operatorname{Poisson}(\lambda/6)\) variables. For \(\lambda>0\) the two summaries are not independent. In particular,

\[
\Pr(\Delta=0,H>0)\longrightarrow
 e^{-\lambda/3}I_0(\lambda/3)-e^{-\lambda/2}>0\quad(\lambda>0),
\]

where \(I_0(z)=\sum_{j\ge0}(z^2/4)^j/(j!)^2\). This quantifies **silent local errors**: at least one adjacent ranking comparison changes, yet the total number of descents remains unchanged. If \(np_n\to0\), then \(H\to0\) in probability; if \(np_n\to\infty\), then \(\Delta/\sqrt{\operatorname{Var}(\Delta)}\) converges to a standard Gaussian. The sparse marked-Poisson law, the Gaussian regime, and the exact covariance constitute one noise-scale description of the same statistic.

## Assumptions and scope

Let \(X_1,\ldots,X_n\) and \(U_1,\ldots,U_n\) be independent and identically distributed continuous random variables with the **same** atomless distribution. Let \(B_1,\ldots,B_n\) be independent \(\operatorname{Bernoulli}(p)\) variables, independent of all scores, and put \(Y_i=X_i\) if \(B_i=0\), and \(Y_i=U_i\) if \(B_i=1\). Distribution-free statements follow from the probability integral transform. Set

\[
I_i=\boldsymbol 1\{X_i>X_{i+1}\},\quad
I'_i=\boldsymbol 1\{Y_i>Y_{i+1}\},\quad
D=\sum_{i=1}^{n-1}I_i,\quad D'=\sum_{i=1}^{n-1}I'_i,
\]

\[
\Delta=D'-D,\qquad H=\sum_{i=1}^{n-1}|I'_i-I_i|.
\]

All assertions are unconditional on the original ranking. The coupling is **independent score replacement before re-ranking**, not an adjacent-transposition chain, a Mallows deformation, or an independent second ranking except at \(p=1\).

## Proof

**Exact cross moments.** Each \(I_i\) has mean \(1/2\), variance \(1/4\), and adjacent within-sample covariance \(-1/12\), with zero covariance at greater separation. At the same position across samples, conditioning on whether neither, one, or both scores were replaced gives

\[
\operatorname{Cov}(I_i,I'_i)=\frac{(1-p)^2}{4}+\frac{2p(1-p)}{12}.
\]

Across adjacent positions, the only common score occurs at the middle index if it was not replaced, so

\[
\operatorname{Cov}(I_i,I'_{i+1})=\operatorname{Cov}(I_{i+1},I'_i)=-\frac{1-p}{12}.
\]

Every other cross covariance is zero. Summing gives the claimed covariance; subtracting twice from \(2\operatorname{Var}(D)=(n+1)/6\) gives \(\operatorname{Var}(\Delta)\). A comparison with one refreshed endpoint changes with probability \(1/3\); with both refreshed endpoints it changes with probability \(1/2\). Consequently \(\Pr(I_i\ne I'_i)=2p(1-p)/3+p^2/2\), giving the expectation of \(H\).

**One refreshed interior score.** Condition on exactly one refreshed interior site and let its old and new scores be \(x,u\). Put \(a=|x-u|\). Each of its two neighboring comparisons flips independently with conditional probability \(a\), because their other scores are independent. Since \(\mathbb E a=1/3\) and \(\mathbb E a^2=1/6\), the four possible marks \((\Delta,H)\) have exact probabilities

\[
\Pr((0,0))=\tfrac12,\quad
\Pr((1,1))=\Pr((-1,1))=\Pr((0,2))=\tfrac16.
\]

When both comparisons flip, one newly gained descent cancels one lost descent; it never contributes \(\Delta=\pm2\).

**Poisson coupling and its finite bound.** Couple actual refreshed sites to an ideal independent sequence of marked Bernoulli trials at each of the \(n\) coordinates, having marks \((1,1),(-1,1),(0,2)\) with probability \(p/6\) each, and zero otherwise. If neither endpoint is refreshed and all refreshed interior indices are separated by at least three, the relevant three-score neighborhoods are disjoint. Conditional on the refresh indicators, the actual nonzero marks are then independent and have precisely the ideal single-site law. The probability of failure of these spacing conditions is at most \(2p+2np^2\). The ideal triple of nonzero mark counts is multinomial, with three cell probabilities \(p/6\); the standard Bernoulli-to-Poisson coupling, applied sitewise to the categorical trials, has total-variation error at most \(np^2/2\) from three independent Poisson counts of mean \(np/6\). Adjusting the three Poisson means to \(\lambda/6\) costs at most \(|np-\lambda|/2\). Pushing the count triple through \((a,b,c)\mapsto(a-b,a+b+2c)\) cannot increase total variation. Adding the bounds proves the quantitative inequality and the joint sparse limit.

The displayed Skellam zero probability follows by summing \(\Pr(N_+=k,N_-=k)\) over \(k\ge0\); \(H=0\) requires all three Poisson counts to vanish and has probability \(e^{-\lambda/2}\). Their difference is strictly positive for \(\lambda>0\), since \(N_2>0\) with positive probability while \(N_+=N_-=0\).

**Beyond the critical scale.** If \(np_n\to0\), Markov's inequality and the exact mean of \(H\) yield \(H\to0\) in probability. If \(np_n\to\infty\), write \(\Delta=\sum_{i=1}^{n-1}(I'_i-I_i)\). These bounded, centered summands form a one-dependent triangular array. For every fixed cumulant order \(r\ge3\), only connected ordered \(r\)-tuples of comparison positions contribute, and there are \(O_r(n)\) of them; each joint cumulant is \(O_r(p_n)\) because all its variables vanish when the union of their finitely many relevant refresh indicators is zero. Therefore \(\kappa_r(\Delta)=O_r(np_n)\). The exact variance is bounded between \(np_n/6\) and \(np_n/3\). All standardized cumulants of order at least three vanish, while the second equals one. The method of moments (normal moments determine their law) proves the Gaussian conclusion.

## Verification

Run the self-contained Python 3 checker with `python CHECK.py`. It enumerates all relative score orders of \(2n\) independent original/replacement scores for \(2\le n\le4\) and every refresh mask, for \(p\in\{0,1/3,1/2,1\}\). Across 12 exact finite cases, it verifies the cross covariance, variance of descent-count change, and expected number of changed comparisons using rational arithmetic. It additionally enumerates all 24 orders of the four scores relevant to a single-site refresh and verifies the four-point mark law. The completed run passed 49 exact assertions. These finite checks are not substitutes for the general proof.

## Relationship to prior work

Borodin, Diaconis and Fulman describe the **single-ranking** one-dependent descent process and its normal limit. Their formulas supply established background for local descent dependence, but do not contain the coupled independent-score-refresh model, its exact two-ranking covariance, or the critical marked-Poisson law. Chatterjee and Diaconis establish local permutation-statistic central limit theorems and joint descent/inverse-descent results; those concern different couplings and do not imply this sparse-refresh marked limit without new local mark and coupling calculations. The ordinary Skellam distribution and local-dependence Poisson approximation are classical mechanisms, not claimed as new. The asserted finding is their explicit rank-refresh specialization, finite noise covariance, quantitative joint error bound, and silent-error probability.

## Limitations

The model assumes independent refreshed coordinates and an atomless common score distribution. Correlated replacements, adaptive refresh locations, ties, and alternative Markov chains on rankings need separate analysis. The finite Poisson error bound is most useful when \(np^2\) is small; it does not imply a Poisson limit at fixed positive \(p\). The Gaussian statement establishes weak convergence, not a Berry–Esseen rate. Priority against unindexed or differently named general results remains open to independent literature review. No independent validation has been performed.

## References

1. A. Borodin, P. Diaconis, and J. Fulman, *On adding a list of numbers (and other one-dependent determinantal processes)*, first public arXiv posting 2009-04-23, [arXiv:0904.3740](https://arxiv.org/abs/0904.3740). Especially sections 2 and 5 on the one-dependent descent process.
2. S. Chatterjee and P. Diaconis, *A central limit theorem for a new statistic on permutations*, first public arXiv posting 2016-08-04, [arXiv:1608.01666](https://arxiv.org/abs/1608.01666). Especially Theorems 1.1 and 1.2 on permutation descent-related Gaussian limits.
