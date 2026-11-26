# Sharp Gaussian Katznelson–Tzafriri decay for positive Cesàro-bounded binomial shifts

## Finding
For every real \(0<\alpha<1\) and \(0<\theta<1\), define on complex \(\ell^1(\mathbb N)\) the weighted backward shift \(We_1=0\) and \(We_j=(j/(j-1))^\alpha e_{j-1}\) for \(j\ge2\), and its binomial smoothing \(S=(1-\theta)I+\theta W\). Put \(\phi(x)=(2\pi)^{-1/2}\exp(-x^2/2)\) and
\[
F_\alpha(t)=\int_{-\infty}^{t}\frac{|x|\phi(x)}{(t-x)^\alpha}\,dx,\qquad M_\alpha=\max_{t\in\mathbb R}F_\alpha(t).
\]
Then \(0<M_\alpha<\infty\) and
\[
\boxed{\lim_{n\to\infty}n^{(1-\alpha)/2}\|S^{n+1}-S^n\|_{1\to1}=\left(\frac{\theta}{1-\theta}\right)^{(1+\alpha)/2}M_\alpha.}
\]
In particular, despite \(\sup_n\|S^n\|=\infty\), the power differences tend to zero at the exact (not merely upper-bound) polynomial rate. The spectrum is \(\{1-\theta+\theta z: |z|\le1\}\), whose only unit-circle point is \(1\).

There is also an exact central-window profile. If \(j_n\ge1\) are integers and
\[
\frac{j_n-n\theta}{\sqrt{n\theta(1-\theta)}}\longrightarrow t\in\mathbb R,
\]
then
\[
\lim_{n\to\infty} n^{(1-\alpha)/2}\|(S^{n+1}-S^n)e_{j_n}\|_1=\left(\frac{\theta}{1-\theta}\right)^{(1+\alpha)/2}F_\alpha(t).
\]
The maximizing constant is given by a one-variable absolutely convergent Gaussian integral; no claim about uniqueness of its maximizer is needed.

## Assumptions and scope
All spaces are over the complex scalars, \(\mathbb N=\{1,2,\dots\}\), and \(\|\cdot\|_{1\to1}\) is the bounded-operator norm. Parameters \(\alpha,\theta\) are fixed strictly inside \((0,1)\) before taking \(n\to\infty\). An operator is absolutely Cesàro-bounded when a constant \(C\) satisfies \(\sum_{k=0}^{N-1}\|T^kx\|\le CN\|x\|\) for every \(N\ge1\) and vector \(x\). No uniformity as either parameter approaches an endpoint is claimed.

## Proof
**1. Boundedness, Cesàro property, spectrum, and non-power boundedness.** The shift is positive, \(\|W^k\|=(k+1)^\alpha\), and for each basis vector \(e_j\) one has \(W^ke_j=(j/(j-k))^\alpha e_{j-k}\) for \(0\le k<j\), and zero otherwise. Its \(1\)-absolute Cesàro constant is \(1/(1-\alpha)\): the upper bound follows by averaging \(j^\alpha\sum_{r=1}^{j}r^{-\alpha}\), and the lower bound is the large-\(j\) integral limit. Arnold, Example 3.2, and Lemma 7.3 also establish directly that binomial smoothing preserves absolute Cesàro boundedness, so \(S\) is positive and \(1\)-absolutely Cesàro bounded. The vectors \((\lambda^{j-1}/j^\alpha)_{j\ge1}\) are \(\ell^1\) eigenvectors for \(W\) for every \(|\lambda|<1\), while \(\lim_{k\to\infty}\|W^k\|^{1/k}=1\). Therefore \(\sigma(W)=\{z:|z|\le1\}\), and spectral mapping gives the asserted \(\sigma(S)\).

To see the unbounded growth of the powers, put \(\mu=n\theta\), \(\sigma=\sqrt{n\theta(1-\theta)}\), and choose \(j=\lfloor\mu+\sigma\rfloor\). The binomial expansion below and the binomial local central limit theorem imply
\[
\lim_{n\to\infty}n^{-\alpha/2}\|S^ne_j\|_1=\left(\frac\theta{1-\theta}\right)^{\alpha/2}\int_{-\infty}^1\phi(x)(1-x)^{-\alpha}\,dx>0.
\]
Thus \(S\) is not power bounded; integrability here depends on \(\alpha<1\).

**2. An exact finite column formula.** For \(p_n(k)=\binom nk\theta^k(1-\theta)^{n-k}\), interpreted as zero off \(0\le k\le n\), the binomial expansion gives
\[
S^ne_j=\sum_{0\le k<j}p_n(k)\left(\frac{j}{j-k}\right)^\alpha e_{j-k}.
\]
Since \(S^{n+1}-S^n=\theta(W-I)S^n\), the coefficient of \(e_{j-k}\) in the difference is \(\theta j^\alpha[p_n(k-1)-p_n(k)]/(j-k)^\alpha\). Hence, with \(d_n(k)=|p_n(k-1)-p_n(k)|\),
\[
\|(S^{n+1}-S^n)e_j\|_1=\theta j^\alpha\sum_{k=0}^{j-1}\frac{d_n(k)}{(j-k)^\alpha}.\tag{1}
\]
As \(\ell^1\) has its canonical unconditional basis, the norm of any bounded matrix operator is the supremum of absolute column sums, so the norm sought is the supremum of (1) over all \(j\ge1\).

**3. Gaussian gradient local limit and domination.** Write \(\mu=n\theta\), \(\sigma=\sqrt{n\theta(1-\theta)}\), and \(x_k=(k-\mu)/\sigma\). The binomial local central limit theorem together with the *exact* ratio
\[
\frac{p_n(k-1)-p_n(k)}{p_n(k)}=\frac{k-n\theta-\theta}{\theta(n-k+1)}\quad(0\le k\le n)
\]
(with the endpoint interpreted separately) yields, uniformly for \(x_k\) in any fixed compact interval,
\[
\sigma^2 d_n(k)\longrightarrow |x_k|\phi(x_k)
\]
in the lattice local-limit sense: the difference between the two sides tends uniformly to zero. A uniform envelope, with \(C,c>0\) depending only on \(\theta\), is
\[
\sigma^2 d_n(k)\le C(1+|x_k|)e^{-c x_k^2}\qquad(0\le k\le n+1,\ n\ge n_0).\tag{2}
\]
For completeness, on \(k\le n(1+\theta)/2\) apply the displayed ratio and the standard binomial bound \(p_n(k)\le C\sigma^{-1}e^{-c x_k^2}\); the denominator is comparable to \(n\), and the ratio's numerator is bounded by \(C\sigma(1+|x_k|)\). On its complementary upper tail, a Chernoff bound combined with the same binomial point-mass estimate gives exponentially small quantities; powers of \(n\) from the small denominator are absorbed by a weaker Gaussian factor. The indices \(0\) and \(n+1\) obey the same envelope directly. This proves (2) without assuming uniform Stirling expansions at the endpoints.

**4. The central profile.** Suppose \(t_n=(j_n-\mu)/\sigma\to t\in\mathbb R\). Then \(j_n/\mu\to1\) and, writing \(t_n-x_k=(j_n-k)/\sigma\), formula (1) becomes
\[
\frac{\sigma^{1+\alpha}}{\theta j_n^\alpha}\|(S^{n+1}-S^n)e_{j_n}\|_1
=\frac1\sigma\sum_{k<j_n}\frac{\sigma^2d_n(k)}{(t_n-x_k)^\alpha}.\tag{3}
\]
On fixed compact subsets of \(( -\infty,t)\), (3) is a Riemann sum converging to \(F_\alpha(t)\). By (2), the near-edge contribution \(0<t_n-x_k\le\varepsilon\) is bounded by \(C\varepsilon^{1-\alpha}+O(\sigma^{\alpha-1})\), uniformly for bounded \(t_n\): indeed \(\sigma^{-1}\sum_{1\le r\le\varepsilon\sigma}(r/\sigma)^{-\alpha}\le C\varepsilon^{1-\alpha}+C\sigma^{\alpha-1}\). The far Gaussian tails are uniformly negligible by (2). Thus (3) converges to \(F_\alpha(t)\). Finally,
\[
 n^{(1-\alpha)/2}\frac{\theta\mu^\alpha}{\sigma^{1+\alpha}}
=\left(\frac{\theta}{1-\theta}\right)^{(1+\alpha)/2},
\]
proving the stated column-wise profile.

**5. Global supremum and maximum.** For \(j<\mu/2\), every index in (1) is in an exponentially unlikely lower binomial tail, so its column contribution is bounded by \(\operatorname{poly}(n)e^{-c n}\), uniformly over those \(j\). For \(j>2\mu\), split (1) into \(k\le3\mu/2\) and \(k>3\mu/2\). On the first part \((j/(j-k))^\alpha\le4^\alpha\), and \(\sum_k d_n(k)=O(1/\sigma)\) by (2). On the second part the binomial gradient is exponentially small, while the weight ratio is at most \((2n)^\alpha\) for \(j\le2n\), and at most \(2^\alpha\) for \(j>2n\). Hence these outer-right columns contribute \(O(\sigma^{-1})+\operatorname{poly}(n)e^{-c n}\), which vanishes after the required normalization because \(\alpha>0\).

In the remaining range \(\mu/2\le j\le2\mu\), the prefactor in (3) is uniformly comparable to its central limit. The envelope (2) yields the discrete convolution \(\sigma^{-1}\sum_{x_k<t_n}(1+|x_k|)e^{-cx_k^2}(t_n-x_k)^{-\alpha}\). It tends uniformly to zero along any sequence for which \(|t_n|\to\infty\): for large positive \(t_n\), split at \(|x_k|\le t_n/2\), where the denominator yields \(O(t_n^{-\alpha})\), and its Gaussian complement; for large negative \(t_n\), all admissible \(x_k<t_n\) have a Gaussian tail factor. In the complement, split off \(0<t_n-x_k<1\); the lattice singular sum is uniformly bounded because \(\alpha<1\), and the remaining Gaussian tail controls it. Consequently every asymptotic maximizing column lies in a bounded central window. Subsequential central profiles then show \(\limsup\) is at most the maximum of \(F_\alpha\); choosing \(j_n=\lfloor\mu+t_*\sigma\rfloor\) for a maximizing \(t_*\) supplies the matching lower bound.

Finally, \(F_\alpha(t)\) is continuous by local integrability and Gaussian domination; it vanishes as \(t\to-\infty\) by a Gaussian tail and as \(t\to+\infty\) like \(t^{-\alpha}\int_{\mathbb R}|x|\phi(x)dx\). It is positive for finite \(t\). Therefore its finite positive maximum exists, completing the proof.

## Verification
The self-contained companion `check.py` evaluates finite binomial columns by two independent expansions and checks the exact identity (1) and the spectral/weight formulas at sample parameters. It also compares finite normalized norms with the Gaussian integral profile. These are supplementary tests, not an infinite-dimensional proof. Steps 1–5 above give the analytical justification for all quantifiers.

## Relationship to prior work
Arnold [1, Example 3.2 and Lemma 7.3] supplied the positive weighted backward shift and showed its binomial smoothing preserves absolute Cesàro boundedness. Arnold [1, Section 7] quantified power *growth* on central columns and then introduced complex rotations and direct sums to violate the Katznelson–Tzafriri conclusion. The present result asks a different question: for an unrotated, single positive binomially smoothed shift, what is the exact rate (including coefficient) of the **operator-norm power difference**? This requires a Gaussian local limit for the *signed gradient* of binomial probabilities and maximization over all input columns, neither furnished by Arnold's bound. Seifert's general resolvent-rate theorems [2] explicitly assume power boundedness, which fails here. Abadias [3] studies a Cesàro-mean analogue, not this raw power-difference asymptotic. Related finite-horizon power-amplification and weak-endpoint weighted-shift results concern other invariants and do not imply the claimed constant.

## Limitations
The theorem holds for one explicit positive family on \(\ell^1\); it is not a universal Katznelson–Tzafriri theorem for all positive absolutely Cesàro-bounded operators. In particular, it does not resolve positive-operator questions on \(L^p\) for \(p>1\). The parameters are strictly interior and the precise Gaussian maximum is left in explicit variational integral form. Possible equivalent asymptotic results in earlier probability-weighted-shift literature under different terminology remain a publication-priority risk. Independent mathematical validation has not been performed.

## References
[1] L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, publicly submitted 2026-09-24; https://arxiv.org/html/2610.00271v1; especially Example 3.2, Lemma 7.3 and Proposition 7.1.

[2] D. Seifert, *Rates of decay in the classical Katznelson–Tzafriri theorem*, arXiv:1410.1297, 2014; https://arxiv.org/abs/1410.1297, Sections 1–3.

[3] L. Abadias, *A Katznelson–Tzafriri type theorem for Cesàro bounded operators*, 2016, relevant abstract at https://arxiv.org/search/?query=Abadias+Katznelson+Tzafriri+Cesaro&searchtype=all (exact bibliographic locator subject to further verification).
