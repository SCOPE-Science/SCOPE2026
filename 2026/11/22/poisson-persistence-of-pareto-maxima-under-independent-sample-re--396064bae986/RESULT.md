# Poisson persistence of Pareto maxima under independent sample refresh

## Finding

Consider a labelled cloud of \(n\) independent points with independent continuous coordinate marginals in dimension \(d\ge2\). Each label independently retains its original vector with probability \(q_n\), or otherwise replaces that **entire** vector by an independent new draw. A label is *persistent* if it is coordinatewise Pareto-maximal both before and after refresh. Let \(I_{n,d}\) count persistent labels, and let \(P_{n,d}\) count those persistent labels whose vector was actually retained.

The following joint set of conclusions describes the same two-sample persistence problem.

**Exact hypergeometric law.** Conditional on exactly \(K=k\) retained vectors, put \(N=2n-k\) and let \(M_{N,d}\) count Pareto maxima among \(N\) independent points in the original product distribution. Then
\[
P_{n,d}\mid (K=k,M_{N,d}=m)\ \sim\ \operatorname{Hypergeom}(N,m,k).
\]
The hypergeometric notation means the number of marked maxima in a uniformly chosen size-\(k\) subset of the \(N\) distinct vectors. In particular, writing \(\mu_{N,d}=\mathbb E M_{N,d}\),
\[
\mathbb E P_{n,d}=\mathbb E\left[\frac{K}{2n-K}\,\mu_{2n-K,d}\right],\qquad
\mu_{N,d}=\sum_{j=1}^{N}(-1)^{j-1}\binom Nj j^{1-d}.
\]
For \(d=2\), the full finite-size probability generating function is
\[
\mathbb E[z^{P_{n,2}}\mid K=k]
=\frac{[u^k]\displaystyle\prod_{j=1}^{N}\left(1+u\left[1+\frac{z-1}{j}\right]\right)}{\binom Nk},\qquad N=2n-k.
\]
Furthermore, if \(H_N=\sum_{j=1}^N1/j\) and \(H_N^{(2)}=\sum_{j=1}^N1/j^2\), then for \(N\ge2\), with \(a=k/N\),
\[
\operatorname{Var}(P_{n,2}\mid K=k)
=a^2(H_N-H_N^{(2)})
 +\frac{a(1-a)}{N-1}\{NH_N-H_N^2-H_N+H_N^{(2)}\}.
\]
For \(N=1\) (necessarily \(n=k=1\)), \(P_{1,2}=1\) conditional on \(K=1\), so the conditional variance is zero.

**Refresh does not create a macroscopic persistent maximum.** For each fixed \(d\ge2\), uniformly over all \(0\le q_n\le1\),
\[
0\le\mathbb E(I_{n,d}-P_{n,d})
=O_d\!\left(\frac{(1+\log n)^{2d-2}}{n}\right).
\]
Thus, if \(q_n=q\in(0,1]\) is fixed, a fraction \(q/(2-q)\) of the asymptotic expected skyline remains persistent:
\[
\mathbb E I_{n,d}\sim\frac{q}{2-q}\frac{(\log n)^{d-1}}{(d-1)!}.
\]

**Sharp rare-retention transition.** For fixed \(d\ge2\), if \(q_n(\log n)^{d-1}\to\theta\in[0,\infty)\), then
\[
I_{n,d}\ \Longrightarrow\ \operatorname{Poisson}\!\left(\frac{\theta}{2(d-1)!}\right).
\]
In the plane, this has an all-retention-level strengthening: with
\(\lambda_n(q)=\frac{q}{2-q}H_{\lfloor(2-q)n\rfloor}\),
\[
\sup_{0\le q\le1}
 d_{\mathrm{TV}}\!\left(\mathcal L(I_{n,2}),\operatorname{Poisson}(\lambda_n(q))\right)
=O\!\left(\frac1{\log n}+\frac{\log n}{\sqrt n}\right).
\]
All limits have \(n\to\infty\). The transition covers \(q_n\sim\theta/\log n\) in the plane; for example, the planar limiting Poisson mean is \(\theta/2\).

## Assumptions and scope

The vectors have dimension \(d\ge2\), fixed as \(n\to\infty\). The \(n\) original vectors are iid. Within each vector, coordinates are independent and their marginals are continuous; different coordinates need not share a distribution. Each label's retention indicator is independent of everything else. When a label refreshes, the new vector is drawn independently from the same product law. Dominance means coordinatewise greater than or equal to, with one strict coordinate; continuity makes ties negligible. The original and refreshed samples each have exactly \(n\) labelled observations, and retained labels count as *one distinct vector* in their union. The intersection statistic uses **labels**, not coincident numerical positions; a refreshed label may rarely be maximal in both. All results remain valid after coordinatewise probability-integral transforms to independent uniforms.

## Proof

### 1. Exact persistent-core law

Condition on a set of \(k\) retained labels. Form the union of the first and second samples, counting a shared retained vector only once. The union consists of \(N=2n-k\) iid draws, with \(k\) draws identified as the retained core. Their core labels are exchangeable with the other union labels. A retained point is maximal in both samples if and only if no point in their union dominates it. Given the total \(m\) union maxima, the number in the uniformly marked size-\(k\) core is exactly hypergeometric. Averaging its conditional mean gives the expectation formula.

For a uniform product sample, a point with dominance-orthant volume \(u\) is maximal with probability \((1-u)^{N-1}\). The product of \(d\) independent uniforms has density \(({-\log u})^{d-1}/(d-1)!\). Hence
\[
\mu_{N,d}=\frac{N}{(d-1)!}\int_0^1(1-u)^{N-1}(-\log u)^{d-1}\,du
=\sum_{j=1}^{N}(-1)^{j-1}\binom Nj j^{1-d}.
\]

In the plane, sorting by decreasing first coordinate makes the second-coordinate sequence a uniform random permutation. Its upper-record indicators are independent Bernoulli variables with success probabilities \(1/j\), \(1\le j\le N\). A uniformly chosen size-\(k\) core corresponds to taking the coefficient of \(u^k\) in the displayed product. For \(N\ge2\), total variance applied to the hypergeometric law gives \(a^2\operatorname{Var}(M)+a(1-a)\mathbb E[M(N-M)]/(N-1)\), where \(M=M_{N,2}\). Using the record mean \(H_N\) and variance \(H_N-H_N^{(2)}\) gives the displayed expression. For \(N=1\), the sole point is retained and maximal under the stated conditioning.

### 2. Refreshed labels are negligible

Fix a refreshed label \(i\), and among its other \(n-1\) labels let \(m\) be retained and \(r=n-1-m\) refreshed. Write \(V_m\) for the fraction of the unit cube not dominated by \(m\) independent shared points. The two positions of label \(i\) are independent uniform probes. Dropping the restrictions imposed by the \(r\) independently refreshed competitors gives
\[
\Pr(i\text{ maximal twice}\mid m,r)\le\mathbb E V_m^2.
\]
Let \(A(x)=\prod_{h=1}^{d}(1-x_h)\) be a probe's dominating-orthant volume. Since the volume of the union of two dominating orthants is at least \(\max\{A(x),A(y)\}\),
\[
\mathbb E V_m^2
\le \mathbb E\exp[-m\max\{A(X),A(Y)\}].
\]
For a uniform probe, \(F_d(t)=\Pr(A(X)\le t)=t\sum_{\ell=0}^{d-1}(-\log t)^\ell/\ell!\). Integrating the Laplace transform by parts and using \(F_d(t)\le C_d t(1+|\log t|^{d-1})\) shows
\[
\mathbb E V_m^2=O_d\!\left(\frac{(1+\log m)^{2d-2}}{m^2}\right)
\quad(m\ge2).
\]
Alternatively, dropping the restrictions from all shared competitors instead gives two independent maximality events among \(r+1\) points, so
\[
\Pr(i\text{ maximal twice}\mid m,r)
\le\left(\frac{\mu_{r+1,d}}{r+1}\right)^2.
\]
At least one of \(m,r\) is at least \((n-1)/2\). The classical bound \(\mu_{s,d}=O_d((1+\log s)^{d-1})\) thus proves the uniform \(O_d((1+\log n)^{2d-2}/n^2)\) probability per refreshed label. Summing over at most \(n\) labels gives the bound for \(\mathbb E(I-P)\). This argument uses actual independence of full-vector replacements, not mere coordinatewise noise.

### 3. Poisson transition in fixed dimension

The classical hypercube-maxima estimates give
\[
\mu_{N,d}\sim\frac{(\log N)^{d-1}}{(d-1)!},\qquad
\operatorname{Var}(M_{N,d})=O_d((\log N)^{d-1}).
\]
When \(q_n(\log n)^{d-1}\to\theta>0\), the binomial law of \(K\) yields \(K/(2n-K)\sim q_n/2\) in probability, while \(M_{2n-K,d}/(\log n)^{d-1}\to1/(d-1)!\). Given \(M\) and \(K\), replacing the finite-population marks of the \(M\) maxima by independent Bernoulli marks of rate \(K/(2n-K)\) incurs total-variation error at most \(O(M^2/n)\), which vanishes by the moment bounds. Their binomial success probability tends to zero and mean tends to \(\theta/[2(d-1)!]\); the Poisson limit follows. If \(\theta=0\), the exact expectation and the refreshed-label error give \(\mathbb E I\to0\), so the zero-mean Poisson limit follows by Markov's inequality. For fixed positive \(q\), the same exact expectation and a binomial concentration argument yield the stated mean asymptotic.

### 4. Uniform planar total-variation approximation

Conditional on \(K\), write \(a=K/(2n-K)\) and \(N=2n-K\). The \(M_{N,2}\) record positions can be coupled from size-\(K\) sampling without replacement to independent Bernoulli marks with rate \(a\) at error \(O(\mathbb E M_{N,2}^2/N)=O((\log n)^2/n)\). Independent record indicators then make the marked count a sum of independent Bernoulli variables with probabilities \(a/j\), \(1\le j\le N\). A Poisson–Stein bound gives
\[
d_{\mathrm{TV}}\!\left(\mathcal L\left(\sum_{j=1}^N\operatorname{Bern}(a/j)\right),\operatorname{Poisson}(aH_N)\right)
\le\frac{1-e^{-aH_N}}{aH_N}\sum_{j=1}^N\frac{a^2}{j^2}
\le\frac{C}{H_N}
\]
for \(a>0\), and both variables vanish when \(a=0\). The binomial fluctuations of \(K\) give
\[
\mathbb E\left|\frac{K}{2n-K}H_{2n-K}-\lambda_n(q)\right|=O\!\left(\frac{\log n}{\sqrt n}\right)
\]
uniformly in \(q\); this follows from the bounded derivative of \(k\mapsto k/(2n-k)\), harmonic-number increments, and \(\mathbb E|K-nq|\le\sqrt n/2\). Coupling Poisson variables by their means, and adding the refreshed-label error from Step 2, proves the claimed uniform bound.

## Verification

The accompanying `checker.py` uses only the Python standard library. Run `python checker.py`. It exhausts planar coordinate-rank permutations and retained-core subsets through union size seven, compares the exact coefficient generating function with the full enumeration, checks the finite conditional mean and variance, and checks the joint two-sample common-core identity for small labelled systems. It additionally tests exact small dimension-two and dimension-three hypergeometric consequences. The observed outputs were:

```
PASS 194 exact finite assertions (all ranks and core subsets to N=7)
PASS 172 extra dimension-2/3 exact hypergeometric and mean assertions
PASS 12 independent full-union two-sample identity assertions
```

The enumeration checks finite identities only; the uniform asymptotic error and Poisson limits rely on the analytic arguments above together with the cited classical maxima moment bounds.

## Relationship to prior work

Classical research established the distribution and expectation of *single-sample* planar maxima and asymptotic expectations/variances for maxima in a fixed-dimensional hypercube. These facts supply the record-indicator and variance inputs used here. The result here instead addresses *label persistence across two dependent samples*, where a fraction of points is shared, and gives the exact conditional overlap law and the rare-retention Poisson threshold. The distinction is important: the joint overlap law is not itself a single-sample maximal-point count. Research on \(k\)-dominant skylines studies weakening the dominance order in one sample, rather than preserving ordinary maxima after random replacement. Algorithmic dynamic-skyline work motivates the question but does not by itself provide a stochastic persistence law.

## Limitations

The stated dimension remains fixed; coordinates are independent and continuous; replacement refreshes the *whole* vector independently. No claim is made for correlated coordinates, partial-coordinate refresh, adversarial updates, growing dimension, or convergence of the full joint two-sample skyline point process. For fixed \(q=0\) the persistent count is small but need not vanish identically at finite size: refreshed labels can coincidentally remain maximal twice. The bound on that contribution is order-based, not an optimal constant. The proof and literature comparison are mathematical analysis, not independent external validation. Undetected earlier results on overlapping record processes or general thinning of random partial-order antichains could imply some or all of the claim; a negative catalogue search cannot establish priority.

## References

1. O. Barndorff-Nielsen and M. Sobel (1966), “On the distribution of the number of admissible points in a vector random sample,” *Theory of Probability and Its Applications* **11**, 249–269. Law and moments of maxima in a single random sample. Available text: https://m.mathnet.ru/links/c4da4be81939f1b3092c1f57d18d3494/tvp624.pdf
2. Z.-D. Bai, L. Devroye, H.-K. Hwang and T.-H. Tsai (2005), “Maxima in Hypercubes,” *Random Structures & Algorithms*. DOI: https://doi.org/10.1002/rsa.20053 . Author-hosted full text: https://luc.devroye.org/max-d-cube.pdf . Fixed-dimensional mean/variance estimates and normal approximations.
3. H.-K. Hwang, T.-H. Tsai and W.-M. Chen (2011 preprint), “Threshold phenomena in \(k\)-dominant skylines of random samples,” https://arxiv.org/abs/1111.6224 . A different one-sample weakening-of-dominance problem.
