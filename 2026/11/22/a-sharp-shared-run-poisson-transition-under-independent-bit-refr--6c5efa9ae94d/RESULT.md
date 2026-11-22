# A sharp shared-run Poisson transition under independent bit refresh

## Finding

Let \(X_1,\ldots,X_n\) be independent fair bits. Obtain \(Y_1,\ldots,Y_n\) by independently retaining each \(X_j\) with probability \(1-\varepsilon_n\), and otherwise replacing it with a fresh fair bit. Let \(k=k_n\to\infty\) be an integer such that \(n2^{-k-1}\to\lambda\in(0,\infty)\). For each interior starting site \(i\in\{2,\ldots,n-k+1\}\), let \(E_i^X\) mean that a zero at site \(i-1\) is followed by at least \(k\) consecutive ones, and define \(E_i^Y\) similarly.

Mark site \(i\) by \(S\) if both events occur, by \(X\) if only \(E_i^X\) occurs, by \(Y\) if only \(E_i^Y\) occurs, and otherwise leave it unmarked. If \(k_n\varepsilon_n\to c\in[0,\infty]\), with \(e^{-\infty/2}=0\), the three marked point processes of rescaled sites \(i/n\) converge jointly to **independent homogeneous Poisson point processes** on \([0,1]\) with respective intensities

\[
\lambda e^{-c/2}\,du,\qquad
\lambda(1-e^{-c/2})\,du,\qquad
\lambda(1-e^{-c/2})\,du.
\]

In particular, if \(L_n^X\) and \(L_n^Y\) are the longest runs of ones in the two length-\(n\) sequences, then

\[
\Pr(L_n^X<k_n,L_n^Y<k_n)\longrightarrow
\exp\{-\lambda(2-e^{-c/2})\}.
\]

The result also holds without an asymptotic limit for \(k_n\varepsilon_n\), along any subsequence for which \(\theta_n=(1-\varepsilon_n/2)^{k_n+1}\to\theta\in[0,1]\), after replacing \(e^{-c/2}\) by \(\theta\). Thus the *sharp refresh crossover* for extreme head runs is \(\varepsilon_n\asymp1/\log n\). At \(c=0\) the limiting extreme-run processes coincide, while at \(c=\infty\) they are independent.

## Assumptions and scope

The bits \(X_j\) are independent Bernoulli\((1/2)\), the refresh decisions and replacement bits are independent across coordinates and of \(X\), and \(0\le\varepsilon_n\le1\). The process concerns left endpoints of runs of length *at least* \(k_n\), so every physical long run is counted once. The interval is linear, not circular. A possible run beginning at the very first bit is omitted from the marked processes; its probability is at most \(2^{-k_n}\), which tends to zero. The theorem is about a two-copy coupling at one refresh step, not a functional-in-time convergence theorem. Convergence is vague convergence of finite point measures on the compact marked space \([0,1]\times\{S,X,Y\}\), or equivalently weak convergence of their finite counting measures.

For exact finite expectations, set \(m=n-k\), \(p=2^{-(k+1)}\), \(t=1-\varepsilon/2\), and \(q=pt^{k+1}\). If \(N_X\) and \(N_Y\) are interior long-run-start counts, then \(\mathbb E N_X=\mathbb E N_Y=mp\), and

\[
\operatorname{Cov}(N_X,N_Y)
=m(q-p^2)+2\sum_{d=1}^{\min(k,m-1)}(m-d)
\left[\frac{\varepsilon t^{k-d}}{2^{k+d+2}}-p^2\right].
\]

This is an explicit specialization of general finite bivariate-pattern methods, not claimed as an independent historical novelty.

## Proof

**1. Single-site intensities.** For each interior start \(i\), \(\Pr(E_i^X)=\Pr(E_i^Y)=p=2^{-k-1}\). The joint one-coordinate law has

\[
\Pr(X_j=Y_j=0)=\Pr(X_j=Y_j=1)=\tfrac12(1-\varepsilon/2)=\tfrac t2,
\quad \Pr(X_j\ne Y_j)=\varepsilon/2.
\]

Independence across coordinates gives \(\Pr(E_i^X\cap E_i^Y)=q=2^{-k-1}t^{k+1}\). The respective site probabilities of the three exclusive marks are \(q,p-q,p-q\). Since \(mp\to\lambda\), their total expected counts tend to \(\lambda\theta,\lambda(1-\theta),\lambda(1-\theta)\), and the corresponding site intensities are spatially uniform.

**2. Exact collisions between distinct sites.** A long-run start in one copy excludes another start in the same copy at every displacement \(1\le d\le k\). For \(i<j=i+d\), \(1\le d\le k\), the crossing event \(E_i^X\cap E_j^Y\) has exact probability

\[
 r_d=\frac{\varepsilon}{2^{k+d+2}}t^{k-d}.
\]

Indeed, the earlier run forces \(X_{j-1}=1\) while the later run forces \(Y_{j-1}=0\), a discordant coordinate of probability \(\varepsilon/4\). There are \(k-d\) coordinates forced to be one in both copies, \(d-1\) earlier coordinates forced only in \(X\), \(d\) later coordinates forced only in \(Y\), and a preceding zero forced only in \(X\). Multiplication gives \(r_d\). The reverse orientation \(E_i^Y\cap E_j^X\) has the same probability. For \(d>k\), the blocks of underlying paired coordinates are disjoint, so all associated site marks are independent.

**3. Uniform local-dependence bound.** Index all three mark indicators at each interior site. Give every indicator the neighborhood of all three indicators at sites displaced by at most \(k\); outside this neighborhood it is independent of the entire sigma-field, so the \(b_3\) term of the Arratia–Goldstein–Gordon process bound is zero. Since every mark has probability at most \(p\), the first bound satisfies

\[
 b_1\le9m(2k+1)p^2=O(k/n)=o(1).
\]

Two distinct neighboring sites can both be marked only through one of the two crossing orientations, hence their total joint probability is at most \(2r_d\). Therefore

\[
 b_2\le4m\sum_{d=1}^{k}r_d
\le m\varepsilon2^{-k}\sum_{d=1}^{k}2^{-d}t^{k-d}.
\]

Splitting the last sum at \(k/2\) gives the uniform bound

\[
 \sum_{d=1}^{k}2^{-d}t^{k-d}
 \le e^{-\varepsilon k/4}+2^{1-k/2}.
\]

As \(\sup_{0\le\varepsilon\le1}\varepsilon e^{-\varepsilon k/4}\le4/(ek)\), and \(m2^{-k}=O(1)\), this implies \(b_2=O(1/k+2^{-k/2})=o(1)\) uniformly for all refresh probabilities. In particular, the potentially dangerous shifted cross-copy long runs have negligible intensity, even though same-site jointly present long runs may persist.

**4. Poisson limit and endpoints.** The marked-process version of the Arratia–Goldstein–Gordon local-dependence theorem approximates the complete finite array of marked indicators by independent Poisson counts with their exact site-specific means in total variation; the error is bounded by a constant multiple of \(b_1+b_2+b_3\). Their deterministic rescaling \(i\mapsto i/n\) yields independent Poisson point processes with the asserted intensity measures. If \(k\varepsilon\to c<\infty\), then \(\varepsilon\to0\) and \(t^{k+1}\to e^{-c/2}\); if \(k\varepsilon\to\infty\), then \(t^{k+1}\le e^{-k\varepsilon/2}\to0\). Finally, a long run starting at site 1 has probability \(2^{-k}\), while every other long run has exactly one counted left endpoint. The two boundaries therefore change the event of no long runs in either sequence with probability at most \(2^{1-k}=o(1)\). Taking zero-count probabilities gives the asserted joint longest-run limit.

**5. Exact covariance.** For interior sites at displacement \(d\le k\), the cross-copy start probability is \(r_d\), and for larger displacement it is \(p^2\). Summing diagonal and off-diagonal covariances yields the finite displayed identity. The collision bound also shows \(\operatorname{Cov}(N_X,N_Y)\to\lambda\theta\). This matches the common Poisson component of the limiting vector.

## Verification

The standalone `verify.py` uses exact rational arithmetic to enumerate joint binary-pair configurations for \(3\le n\le7\), permitted \(1\le k\le3\), and refresh probabilities \(0,1/2,1\). It checks both marginal means, same-site joint probabilities, the finite covariance identity, and exact cross-offset probabilities, including boundary-limited cases. Running `python verify.py` produces `PASS 181 exact rational formula assertions`. These finite tests do not prove the infinite point-process theorem; the local-dependence estimates and the cited Poisson-process theorem supply that proof.

## Relationship to prior work

Arratia, Goldstein and Gordon established the marked Poisson-process approximation theorem and analyzed the static longest-head-run process; their theorem is used as a tool here, not presented as new. Benjamini, Häggström, Peres and Steif studied dynamical sensitivity of run tests and exceptional-time sets, including qualitative noise sensitivity, but the inspected run-test statements do not identify this two-copy, critical-scale three-type spatial Poisson law. Kamalja and Shinde developed exact joint probability-generating-function methods for bivariate trials, which provide broader finite-distribution machinery; the present explicit finite covariance is not claimed to evade their coverage. Johnson and Fu reviewed static run-pattern approximations. The added target is the explicit noise-dependent *coupling of two long-run extremal location processes*, including their sharp \(1/\log n\) transition and simultaneous failure probability.

## Limitations

The result concerns fair bits, independent per-coordinate resampling, and the sparse window \(n2^{-k_n-1}\to\lambda\in(0,\infty)\), which ordinarily requires subsequences because \(k_n\) is integral. It does not address biased bits, general dependence between coordinates, arbitrary patterns, or sample paths over a continuum of refresh times. The claimed original contribution is the explicit marked critical crossover, not the static Poisson law, generic Chen–Stein theory, or general finite bivariate generating functions. A broad, as-yet-unlocated correlated-pattern limit theorem could imply the asserted explicit law; historical priority remains subject to independent full-literature review.

## References

1. R. Arratia, L. Goldstein, L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science 5 (1990), 403–434. https://doi.org/10.1214/ss/1177012015 (full text: https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/pacs-1.pdf).
2. I. Benjamini, O. Häggström, Y. Peres, J. E. Steif, *Which properties of a random sequence are dynamically sensitive?*, Annals of Probability 31 (2003), 1–34. https://doi.org/10.1214/aop/1046294302.
3. K. K. Kamalja, R. L. Shinde, *Runs and Patterns in a Sequence of Markov Dependent Bivariate Trials*, Open Journal of Statistics 1 (2011), 115–127. https://doi.org/10.4236/ojs.2011.12014.
4. B. C. Johnson, J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1 (2014), article 5. https://doi.org/10.1186/2195-5832-1-5.
5. I. Benjamini, G. Kalai, O. Schramm, *Noise Sensitivity of Boolean Functions and Applications to Percolation*, first public arXiv submission 1998-11-26, https://arxiv.org/abs/math/9811157.
