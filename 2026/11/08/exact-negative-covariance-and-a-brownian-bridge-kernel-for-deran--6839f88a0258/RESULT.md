# Exact negative covariance and a Brownian-bridge kernel for derangement excedances

## Finding
Let \(\pi\) be a uniformly random fixed-point-free permutation of \(\{1,\ldots,n\}\), where \(n\ge4\), and set \(X_i=\mathbf1\{\pi(i)>i\}\). Write \(d_m\) for the subfactorial \(!m\), with \(d_0=1\) and \(d_1=0\), and define
\[
Q_n=d_{n-2}+2d_{n-3}+d_{n-4},\qquad
c_n=\frac{Q_n}{d_n}-\frac{1}{(n-1)^2}
=\frac{(n-1)d_{n-2}/(n-3)+d_{n-3}}{(n-1)d_n}>0.
\]
Then for every \(1\le i<j\le n\),
\[
\boxed{\operatorname{Cov}(X_i,X_j)=-c_n(i-1)(n-j).}
\]
The means and variances are
\[
\mathbb E[X_i]=\frac{n-i}{n-1},\qquad
\operatorname{Var}(X_i)=\frac{(i-1)(n-i)}{(n-1)^2}.
\]
Thus all pairs with \(2\le i<j\le n-1\) have strictly negative covariance; the first and last coordinates are deterministic. In the strictly off-diagonal sector the covariance is a negative scalar multiple of the discrete Brownian-bridge covariance kernel. Moreover, for fixed \(0<x<y<1\),
\[
\lim_{n\to\infty}n\operatorname{Cov}(X_{\lfloor xn\rfloor},X_{\lfloor yn\rfloor})=-x(1-y).
\]
This is a pairwise covariance result, not a statement of negative association or higher-order independence.

## Assumptions and scope
The law is uniform over all \(d_n\) permutations of \(\{1,\ldots,n\}\) with no fixed points. A positional excedance is the event \(\pi(i)>i\). All probabilities are exact for integers \(n\ge4\). The endpoints satisfy \(X_1=1\) and \(X_n=0\) almost surely. The asymptotic limit is for fixed distinct interior fractions \(x,y\); it does not assert a uniform approximation near the diagonal or endpoints.

## Proof
**1. One-point probabilities.** The law of a uniform derangement is invariant under simultaneous relabeling (conjugation). For any fixed \(i\), each nonfixed image \(j\ne i\) consequently has probability \(1/(n-1)\). There are \(n-i\) choices greater than \(i\); this gives the stated mean and Bernoulli variance.

**2. Counts with two prescribed images.** Suppose \(i\ne j\), \(a\ne b\), \(a\ne i\), and \(b\ne j\) are prescribed by \(\pi(i)=a\) and \(\pi(j)=b\). The remaining \(n-2\) domain and codomain labels have exactly \(m=n-|\{i,j,a,b\}|\) common labels whose fixed points are forbidden. Inclusion-exclusion gives the number of completions
\[
H(n,m)=\sum_{k=0}^{m}(-1)^k\binom{m}{k}(n-2-k)!.
\]
In particular, \(H(n,n-3)=B_n=d_{n-2}+d_{n-3}\) and \(H(n,n-4)=Q_n=d_{n-2}+2d_{n-3}+d_{n-4}\). These identities follow either by adjoining the missing fixed-point constraints one at a time or by the subfactorial inclusion-exclusion formula.

**3. Two excedances.** For \(i<j\), the available images for the pair of events \(\pi(i)>i\) and \(\pi(j)>j\) are \(n-j\) choices for \(\pi(j)\), and for each of those \(n-i-1\) distinct choices for \(\pi(i)\). Exactly \(n-j\) choices have \(\pi(i)=j\), leaving exactly one of the two prescribed images in \(\{i,j\}\); they contribute \(B_n\) completions each. The other \((n-j)(n-i-2)\) choices contribute \(Q_n\) completions each. (If \(j=n\), both counts vanish and the formula remains correct.) Hence
\[
\mathbb E[X_iX_j]=\frac{(n-j)\big(B_n+(n-i-2)Q_n\big)}{d_n}.
\]
The elementary identity \(B_n+(n-3)Q_n=d_n/(n-1)\) follows by substituting \(B_n=d_{n-2}+d_{n-3}\), \(Q_n=d_{n-2}+2d_{n-3}+d_{n-4}\), and the subfactorial recurrence. Thus
\[
\mathbb E[X_iX_j]=(n-j)\left(\frac1{n-1}-(i-1)\frac{Q_n}{d_n}\right).
\]
Subtracting \((n-i)(n-j)/(n-1)^2\) yields the boxed covariance identity.

**4. Strict sign.** The recurrence \(d_m=(m-1)(d_{m-1}+d_{m-2})\) implies
\[
Q_n=\frac{n-2}{n-3}d_{n-2}+d_{n-3},\qquad
d_n=(n-1)\big((n-1)d_{n-2}+(n-2)d_{n-3}\big).
\]
Subtracting gives
\[
(n-1)^2Q_n-d_n=(n-1)\left(\frac{n-1}{n-3}d_{n-2}+d_{n-3}\right)>0,
\]
because \(n\ge4\), \(d_{n-2}>0\), and \(d_{n-3}\ge0\). Therefore \(c_n>0\), proving exactly the stated strict/zero cases.

**5. Limiting kernel.** Since \(d_m/m!\to e^{-1}\), the formula in Step 4 gives \(n^3c_n\to1\). Inserting \(i=\lfloor xn\rfloor\) and \(j=\lfloor yn\rfloor\) into the exact covariance, and multiplying by \(n\), gives the stated limit. For \(i<j\), the Brownian-bridge kernel at \(t=(i-1)/(n-1)\), \(s=(j-1)/(n-1)\) is \(t(1-s)=(i-1)(n-j)/(n-1)^2\), confirming the exact off-diagonal interpretation.

## Verification
The accompanying `verify_derangement_covariance.py` independently enumerates every derangement of orders \(4\) through \(9\), calculates means and joint probabilities directly from permutation arrays, and compares them with the formulas using exact rational arithmetic. It also checks both double-image inclusion-exclusion identities and strict positivity for orders \(4\) through \(80\). The executable prints 579 exact assertions passed. Enumeration is a finite consistency test, not the basis of the infinite theorem, which follows from the explicit proof above. Run `python3 verify_derangement_covariance.py` with Python's standard library.

## Relationship to prior work
Ehrenborg and Steingrímsson enumerate prescribed excedance sets for unrestricted permutations, without conditioning on absence of fixed points. Kim and Zeng's *A New Decomposition of Derangements* develops generating functions for the **total** number of excedances; it does not present two-position covariance kernels. Eriksen, Freij and Wästlund enumerate **descent** constraints in derangements, a different positional statistic. Shin and Zeng extend aggregate excedance-enumerator identities in derangements and colored permutations; their inspected results are not stated for prescribed positional pairs. The present formula instead resolves all pairs of individual excedance indicators and the resulting strict negative-dependence pattern. The classical unrestricted-permutation exceedance problem is related, but conditioning away all fixed points changes both the endpoint factors and the finite coefficient.

## Limitations
The result concerns second moments only: neither negative association, a determinantal representation, nor a joint process limit is proved. No independent external audit has been performed. Although three relevant full texts were inspected for their statements and methods, an equivalent older positional-excedance formula may exist in specialized literature not located by the searches; historical priority therefore retains a residual risk. The asymptotic limit does not imply an empirical-process functional limit.

## References
- R. Ehrenborg and E. Steingrímsson, *The Excedance Set of a Permutation*, Advances in Applied Mathematics **24** (2000), 284–299; https://www.ms.uky.edu/~jrge/papers/Excedance.pdf.
- D. Kim and J. Zeng, *A New Decomposition of Derangements*, Journal of Combinatorial Theory, Series A **96** (2001), 192–198; author manuscript: https://mathsci.kaist.ac.kr/~dskim/papers/Derang.pdf.
- N. Eriksen, R. Freij and J. Wästlund, *Enumeration of derangements with descents in prescribed positions*, arXiv:0811.1925 (first submitted 2008-11-12), https://arxiv.org/abs/0811.1925.
- H. Shin and J. Zeng, *Symmetric unimodal expansions of excedances in colored permutations*, arXiv:1411.6184 (first submitted 2014-11-23), https://arxiv.org/abs/1411.6184.
