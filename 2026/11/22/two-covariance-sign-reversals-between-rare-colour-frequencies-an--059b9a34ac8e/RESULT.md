# Two covariance sign reversals between rare-colour frequencies and run changes in symmetric Pólya sampling

## Finding

Let \(q\ge2\) be an integer, \(a>0\) a real number, and \(X_1,\ldots,X_n\) the first \(n\ge2\) colours in the symmetric \(q\)-colour Pólya scheme with common initial mass \(a\) and unit reinforcement. Write \(N_j=\#\{i:X_i=j\}\). For an integer \(1\le r\le n\), define the frequency-of-frequencies count and colour-switch count
\[
C_{n,r}=\sum_{j=1}^q\mathbf1\{N_j=r\},\qquad
R_n=\sum_{i=1}^{n-1}\mathbf1\{X_i\ne X_{i+1}\}.
\]
The number of runs is \(R_n+1\), so adding that constant does not change covariance. Put
\[
d_q=\frac{(q-1)a}{qa+1},\qquad
b_{q,a}=\frac{(q-2)a}{(q-1)a+1},\qquad
p_{n,r}=\binom nr\frac{(a)^{\overline r}((q-1)a)^{\overline{n-r}}}{(qa)^{\overline n}},
\]
where the rising factorial \((z)^{\overline k}=\prod_{j=0}^{k-1}(z+j)\) equals one for \(k=0\). Then \(p_{n,r}>0\) and the *exact* covariance is
\[
\boxed{\operatorname{Cov}(R_n,C_{n,r})=\frac{q\,p_{n,r}}{n}F_{q,a,r}(n)},
\qquad
F_{q,a,r}(x)=2r(x-r)+(x-r)(x-r-1)b_{q,a}-x(x-1)d_q.
\tag{1}
\]
For every fixed integer \(q\ge2\), every real \(a>0\), and every fixed integer \(r\ge2\), the quadratic \(F_{q,a,r}\) has exactly two distinct real roots \(\nu_-\) and \(\nu_+\), satisfying
\[
\boxed{r<\nu_-<qr<\nu_+}.
\]
For *every integer* \(n\ge r\), the covariance is negative when \(n<\nu_-\) or \(n>\nu_+\), zero exactly when \(n\) equals a root, and positive precisely when \(\nu_-<n<\nu_+\). In particular, the covariance has a nonempty positive integer interval around \(n=qr\), but is strictly negative at \(n=r\) and for sufficiently large \(n\). Thus it has a universal **negative–positive–negative** sample-size dependence pattern, with possible exact zero endpoints, for every occurrence frequency \(r\ge2\).

For singletons, \(r=1\), there is instead exactly one nontrivial threshold:
\[
\boxed{\operatorname{sgn}\operatorname{Cov}(R_n,C_{n,1})
=\operatorname{sgn}\left(2q+\frac2a-n\right),\qquad n\ge2.}
\tag{2}
\]
Equality occurs only if the threshold is an integer and \(n\) equals it. At \(n=1\), \(R_1=0\) deterministically.

For fixed \(q,a\), as the frequency \(r\to\infty\), the two real sample-size thresholds obey \(\nu_\pm=t_\pm r+O_{q,a}(1)\), with
\[
t_\pm=q+\frac1a\pm\frac{\sqrt{a^2q^2-a^2q+2aq-a+1}}{a\sqrt{a+1}},
\qquad 1<t_-<q<t_+.
\tag{3}
\]

## Assumptions and scope

The predictive distribution of the scheme is
\[
\Pr(X_{k+1}=j\mid X_1,\ldots,X_k)=\frac{a+N_j(k)}{qa+k},
\]
where \(N_j(k)\) counts earlier appearances of colour \(j\). The parameter \(a\) is any positive real concentration, not necessarily an integer initial ball count. The case \(q=2\) is included (then \(b_{q,a}=0\)). All covariance statements concern the first \(n\) draws. The roots are roots of a continuous real quadratic, but the sign classification concerns only admissible integer sample sizes. There is no claim of stochastic ordering, independence at zero covariance, or the same signs for asymmetric initial masses.

## Proof

**Exchangeability and one-colour occupancy.** Multiplying the predictive probabilities shows that a specified sequence with count vector \((N_1,\ldots,N_q)\) has probability
\[
\Pr(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_{j=1}^q(a)^{\overline{N_j}}}{(qa)^{\overline n}}.
\tag{4}
\]
Consequently all orderings of a given count vector are equally likely, and the number of positions with colour \(1\) has the beta-binomial probability \(\Pr(N_1=r)=p_{n,r}\) in (1). Exchangeability of colour labels gives
\[
\operatorname{Cov}(R_n,C_{n,r})=q\,p_{n,r}
\bigl(\mathbb E[R_n\mid N_1=r]-\mathbb E R_n\bigr).
\tag{5}
\]

**Conditional run expectation.** Because the \(r\) positions of colour \(1\) are a uniformly chosen subset of positions, the mean number of adjacent colour changes involving colour \(1\) is \(2r(n-r)/n\). Conditional on \(N_1=r\), the other \(n-r\) observations retain the symmetric \((q-1)\)-colour Pólya law with concentration \(a\); two of those observations have unequal colours with probability \(b_{q,a}\). There are on average \((n-r)(n-r-1)/n\) adjacent pairs of two non-\(1\) colours. Thus
\[
\mathbb E[R_n\mid N_1=r]
=\frac{2r(n-r)+(n-r)(n-r-1)b_{q,a}}{n}.
\tag{6}
\]
The unconditional probability of two successive colours differing is \(d_q\), hence \(\mathbb E R_n=(n-1)d_q\). Substituting into (5) proves (1).

**Strict two-root classification for \(r\ge2\).** Direct algebra gives
\[
b_{q,a}-d_q=-\frac{a(a+1)}{(qa+1)((q-1)a+1)}<0.
\]
Therefore \(F_{q,a,r}\) is a strictly concave quadratic of \(x\), and
\[
F_{q,a,r}(r)=-r(r-1)d_q<0,
\]
\[
F_{q,a,r}(qr)=
\frac{r(a+r)(q-1)(qa+2)}{(qa+1)((q-1)a+1)}>0.
\tag{7}
\]
As \(x\to\infty\), \(F_{q,a,r}(x)\to-\infty\). The intermediate value theorem and strict concavity show that there are exactly two real roots, with one in \((r,qr)\) and the other in \((qr,\infty)\). The quadratic sign pattern and positivity of \(q p_{n,r}/n\) establish the exact sign classification; \(n=qr\) is always a positive-covariance integer, so the positive interval cannot be empty.

**Singleton boundary.** At \(r=1\), exact factorization yields
\[
F_{q,a,1}(n)=\frac{(n-1)(a+1)}{(q-1)a+1}
\left(2-\frac{na}{qa+1}\right).
\tag{8}
\]
Since \(n\ge2\), all prefactors are positive and (2) follows.

**Large-frequency locations.** For fixed \(q,a\), replacing \(x\) by \(tr\) and dividing by \(r^2\) gives the limiting quadratic
\[
2(t-1)+(t-1)^2 b_{q,a}-t^2d_q.
\]
Its two simple roots are exactly the values \(t_\pm\) in (3), obtained by the quadratic formula. Their ordering follows from evaluating the limit at \(t=1\) (negative), at \(t=q\) (positive), and at arbitrarily large \(t\) (negative). Since the two limiting roots are simple and the coefficient functions have corrections of order \(r^{-1}\), the finite roots satisfy \(\nu_\pm=t_\pm r+O_{q,a}(1)\).

## Verification

The accompanying standalone `check.py` uses exact rational probabilities to exhaustively enumerate Pólya colour sequences for \(q\in\{2,3\}\), \(a\in\{1/2,1,2\}\) and \(2\le n\le8\) for two colours or \(2\le n\le7\) for three. It compares 186 nontrivial parameter/frequency cases with (1), checks the singleton factorization and positive interior signs, and separately verifies the critical symbolic identities and limiting roots with SymPy. All checks passed. Finite enumeration corroborates the calculation; the preceding reasoning proves the classification for all admissible parameters.

## Relationship to prior work

The classical exchangeability and Dirichlet-mixture law for Pólya sampling are established prerequisites, not new assertions. Eryilmaz (2008, Theorem 1 and its subsequent specializations) derives **general joint laws of colour-specific runs and their lengths** under multicolour Pólya sampling. This is materially stronger coverage of the underlying finite joint sampling distributions, and in principle those sums determine the covariance studied here; no novelty is asserted for access to that joint law. In the inspected definitions, theorems and corollaries, the exact occurrence-frequency/total-switch covariance and especially the all-parameter two-root *sign classification* are not evaluated. The new proposition is an explicit structural sign classification requiring additional conditional-moment and polynomial reasoning, rather than a new joint run distribution. Hutter's 2013 treatment of the Dirichlet-multinomial predictive rule concerns modelling and redundancy.

Published research on iid *uniform* categorical sampling derives an exact covariance of an occupancy-frequency count with the total number of equal-colour **pairs**, including a two-root frequency-sign law and a reentrant sample-size phase. Conditioning on an iid colour-probability vector is not the same as the finite-concentration Pólya law: averaging covariance over a Dirichlet-distributed vector introduces an additional covariance between conditional expectations. The iid theorem therefore does not supply the all-concentration classification (1)–(3). Other research on symmetric Pólya urns classifies correlations between *two specified singleton-colour events*, not correlation of a sample-wide singleton/frequency count with the number of temporal colour switches. A published iid coverage-versus-run theorem concerns richness instead of any fixed positive frequency \(r\), and does not establish the two-switch phenomenon.

The new content here is the exact simultaneous dependence on reinforcement strength, alphabet size, frequency and sample length, the universal reentrant classification, the singleton boundary and large-frequency threshold constants—not the underlying beta-binomial or exchangeability identities.

## Limitations

This result does not cover unequal Dirichlet parameters, replacement rules with different reinforcement per colour, or non-exchangeable Markov inputs. The positive or negative covariance does not imply monotone association of the entire joint law. The two-real-root statement does not mean that an exact integer zero occurs for every choice of parameters. A sufficiently general earlier conditional-moment identity may implicitly imply (1); absence of a matching theorem in the inspected comparisons is not a guarantee of historical priority. The paper-sized independent validation of novelty has not occurred.

## References

1. S. Eryilmaz, *Run Statistics Defined on the Multicolor URN Model*, Journal of Applied Probability 45 (2008), 1007–1023, https://doi.org/10.1239/jap/1231340230.
2. M. Hutter, *Sparse Adaptive Dirichlet-Multinomial-like Processes*, arXiv:1305.3671, submitted 2013-05-16. https://arxiv.org/abs/1305.3671
3. *Reentrant covariance phases of occupancy-frequency counts and sample collisions*, public research record, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-reentrant-covariance-phases-of-occupancy-frequency-counts-and-sa--748ea0d89a26/RESULT.md
4. *Convex collision association and two-threshold frequency dependence in multinomial occupancy*, public research record, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-convex-collision-association-and-two-threshold-frequency-depende--9485777d7c83/RESULT.md
5. *The two-reversal singleton-correlation window in a symmetric reinforced urn*, public research record, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-the-two-reversal-singleton-correlation-window-in-a-symmetric-rei--0111d981dd23/RESULT.md
6. *Categorical coverage and run count have universal positive covariance*, public research record, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-categorical-coverage-and-run-count-have-universal-positive-covar--a8532889aa0a/RESULT.md
