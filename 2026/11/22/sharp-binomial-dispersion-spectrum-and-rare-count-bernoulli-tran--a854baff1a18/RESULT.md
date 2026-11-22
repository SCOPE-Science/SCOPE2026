# Sharp binomial-dispersion spectrum and rare-count Bernoulli transition in the bimodal beta-binomial family

## Finding

For every fixed integer \(n\ge 2\), the bimodal beta-binomial family of Reyes et al. (2024) has **the entire sharp feasible equimean-binomial variance-ratio range**
\[
\left\{\frac{\operatorname{Var}(Y)}{\mathbb E Y\,[1-\mathbb E Y/n]}:\ Y\sim\mathrm{BBB}(n,\alpha,\beta,q),\ \alpha,\beta>0,\ q\in\mathbb R\right\}=(0,n).
\]
Neither endpoint is attained at finite admissible parameters. In particular, this weighted family admits strictly underdispersed, equidispersed, and overdispersed laws relative to the binomial with the same mean; the unweighted \(q=0\) beta-binomial subfamily is always overdispersed.

A separate, model-specific structural limit explains the lower extreme. Fix \(n\ge2\), \(\alpha>0\), and \(q\ne0\). As \(\beta\to\infty\),
\[
Y\ \xrightarrow{\mathrm{TV}}\ \operatorname{Bernoulli}(\pi_q),\qquad
\pi_q=\frac{q^2}{2+q^2},
\]
with the **sharp total-variation asymptotic**
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y),\operatorname{Bernoulli}(\pi_q)\bigr)
=\frac{2|q|\sqrt{n\alpha}}{2+q^2}\,\beta^{-1/2}+O(\beta^{-1}).
\]
The resulting binomial-dispersion limit is
\[
\lim_{\beta\to\infty}\frac{\operatorname{Var}(Y)}{\mathbb E Y\,[1-\mathbb E Y/n]}
=\frac{2n}{2n+(n-1)q^2}<1.
\]
Every fixed \(q\ne0\), however small, therefore yields underdispersion for sufficiently large \(\beta\). Here and throughout, all limits hold with the other displayed parameters fixed, except for the explicitly indicated endpoint constructions.

## Assumptions and scope

Let \(B\sim\operatorname{BetaBinomial}(n,\alpha,\beta)\) have mass function
\[
b_k=\binom nk\frac{(\alpha)_k(\beta)_{n-k}}{(\alpha+\beta)_n},\qquad k=0,1,\ldots,n,
\]
where \((z)_j=z(z+1)\cdots(z+j-1)\) and \((z)_0=1\). Write
\[
\mu=\frac{n\alpha}{\alpha+\beta},\qquad
\sigma^2=\frac{n\alpha\beta(\alpha+\beta+n)}{(\alpha+\beta)^2(\alpha+\beta+1)}.
\]
The weighted law \(Y\sim\mathrm{BBB}(n,\alpha,\beta,q)\) is defined exactly by
\[
\Pr(Y=k)=b_k\,\frac{1+[1-q(k-\mu)/\sigma]^2}{2+q^2},\qquad k=0,\ldots,n,
\]
with \(\alpha,\beta>0\), \(q\in\mathbb R\), and fixed integer \(n\ge2\). Normalization follows from \(\mathbb E[(B-\mu)/\sigma]=0\) and \(\mathbb E[((B-\mu)/\sigma)^2]=1\). All masses are strictly positive. Define \(m=\mathbb EY\), \(v=\operatorname{Var}(Y)\) and \(R_n=v/[m(1-m/n)]\). Thus \(R_n=1\) means exactly the variance of \(\operatorname{Binomial}(n,m/n)\); this is not the Poisson Fano factor \(v/m\). The case \(n=1\), for which \(R_1=1\) identically, is excluded.

## Proof

**1. Universal strict bounds.** Because \(Y\in\{0,\ldots,n\}\),
\[
\operatorname{Var}(Y)=m(n-m)-\mathbb E[Y(n-Y)].
\]
The mass at \(Y=1\) is strictly positive, so for \(n\ge2\) the last expectation is positive; also \(v>0\) and \(0<m<n\) by full support. Consequently \(0<R_n<n\) for every finite parameter triple.

**2. The rare-count boundary, including the rate.** Fix \(n,\alpha>0\) and fixed \(q\ne0\); let \(\beta\to\infty\). Set \(c=n\alpha\). The ordinary beta-binomial has
\[
\mu=c\beta^{-1}+O(\beta^{-2}),\quad
\sigma^2=c\beta^{-1}+O(\beta^{-2}),\quad
\mathbb E[B(B-1)]=\frac{n(n-1)\alpha(\alpha+1)}{(\alpha+\beta)(\alpha+\beta+1)}=O(\beta^{-2}).
\]
Therefore \(b_1=c\beta^{-1}+O(\beta^{-2})\), \(b_0=1-c\beta^{-1}+O(\beta^{-2})\), and \(\sum_{k\ge2}b_k=O(\beta^{-2})\). Since the quadratic weight is at most \(O(\beta)\) on the fixed finite support, \(\Pr(Y\ge2)=O(\beta^{-1})\). At zero its weight is
\[
\frac{1+[1+q\mu/\sigma]^2}{2+q^2}=
\frac{2+2q\sqrt c\,\beta^{-1/2}+O(\beta^{-1})}{2+q^2}.
\]
Hence, writing \(p_k=\Pr(Y=k)\),
\[
\begin{aligned}
p_0&=\frac2{2+q^2}+\frac{2q\sqrt c}{2+q^2}\beta^{-1/2}+O(\beta^{-1}),\\
p_1&=\frac{q^2}{2+q^2}-\frac{2q\sqrt c}{2+q^2}\beta^{-1/2}+O(\beta^{-1}),\\
\sum_{k=2}^n p_k&=O(\beta^{-1}).
\end{aligned}
\]
The second line uses total probability one. This proves the Bernoulli limit and, because \(q\ne0\), gives the sharp TV constant from the two opposite leading deviations. Bounded support gives convergence of means and variances, so
\[
R_n\to\frac{\pi_q(1-\pi_q)}{\pi_q(1-\pi_q/n)}
=\frac{2n}{2n+(n-1)q^2}.
\]
The \(O(\cdot)\) constants may depend on fixed \(n,\alpha,q\); no uniformity in growing \(q\) is claimed.

**3. Approaching both sharp endpoints.** Fix \(\alpha=1\). For each positive integer \(j\) choose \(q_j=j\). From the fixed-\(q_j\) limit just proved, select a finite \(\beta_j>0\) large enough that
\[
\left|R_n(1,\beta_j,q_j)-\frac{2n}{2n+(n-1)j^2}\right|<1/j.
\]
Then \(R_n(1,\beta_j,q_j)\to0\), proving sharpness at the lower end by a diagonal argument (without assuming a uniform asymptotic in \(q\)). At the upper end set \(q=0\) and \(\alpha=\beta=\varepsilon>0\). The ordinary beta-binomial has the exact identity
\[
R_n(\varepsilon,\varepsilon,0)=\frac{n+2\varepsilon}{1+2\varepsilon}\longrightarrow n\quad(\varepsilon\downarrow0).
\]
Equivalently, these laws converge to the equal mixture of point masses at \(0\) and \(n\).

**4. Every intermediate dispersion is realized.** The parameter domain \((0,\infty)^2\times\mathbb R\) is path connected. The finite-support probability formula makes \(R_n\) continuous throughout it, as its denominator is strictly positive. For any given \(r\in(0,n)\), Steps 2–3 provide finite parameter triples with \(R_n<r\) and \(R_n>r\). Any continuous line segment joining them remains admissible; the intermediate value theorem yields a finite triple with \(R_n=r\). Combined with Step 1 this proves the exact open interval.

Finally, the unweighted line \(q=0\) has
\[
R_n(\alpha,\beta,0)=\frac{n+\alpha+\beta}{1+\alpha+\beta}>1
\]
for every \(n\ge2\). This comparison is the structural distinction between the baseline and its quadratic weighting.

## Verification

The supplied standalone `check_dispersion.py` uses only the Python standard library. It reconstructs exact beta-binomial probabilities as rational rising factorials, uses \(q=t\sigma\) to keep the weighted probabilities rational for integer \(t\), and checks normalization, full-support dispersion bounds, and the unweighted variance factor across 428 test groups. One exactly rational underdispersed witness is
\[
n=2,\quad\alpha=1,\quad\beta=100,\quad q=50\sigma,\qquad
R_2=\frac{2329513809177953}{9120943935192402}<\frac13.
\]
The code also compares the leading total-variation asymptotic in several distinct signed-\(q\) cases and reports passing numerical checks. These computations check implementations and examples only; the infinite-parameter and asymptotic conclusions are supplied by the proof above.

Reproduce with `python check_dispersion.py` from the directory containing the two files. No external data or packages are needed.

## Relationship to prior work

Reyes et al. (2024) introduced exactly this weighted beta-binomial family, proved normalization and moment identities, and numerically illustrated changes in coefficient of variation and skewness. Their published results do not give the sharp complete equimean-binomial dispersion interval or the rare-count Bernoulli / sharp TV transition derived here. Their general moment formulas and basic weighting construction are acknowledged and reused rather than claimed as new. The 2020 bimodal shifted-Poisson paper of Gómez-Déniz et al. discusses underdispersion against a Poisson benchmark for a different infinite-support law; it does not imply the exact beta-binomial result. The 2022 discretized-Beta-mixture study of Simone treats another bounded-support family that may be underdispersed, not this quadratic beta-binomial tilt. The universal support inequality in Step 1 is classical; novelty is not attributed to it alone.

## Limitations

This theorem concerns the equimean-binomial variance ratio over **all** admissible shape and tilt parameters, not the dispersion range at a fixed mean, fixed shapes, or fixed tilt. The endpoints require limiting parameters and cannot be achieved by finite admissible triples. It makes no claim that the dispersion value uniquely identifies the parameters, or that any particular data set is underdispersed. The literature comparison is best-knowledge rather than a guarantee of historical priority. No independent validation is claimed.

## References

1. J. Reyes, J. Najera-Zuloaga, D.-J. Lee, J. Arrué, and Y. A. Iriarte, *A Bimodal Extension of the Beta-Binomial Distribution with Applications*, Axioms **13** (2024), 662, first publicly published 2024-09-25, https://doi.org/10.3390/axioms13100662.
2. E. Gómez-Déniz, J. V. Pérez-Rodríguez, J. Reyes, and H. W. Gómez, *A Bimodal Discrete Shifted Poisson Distribution. A Case Study of Tourists' Length of Stay*, Symmetry **12** (2020), 442, https://doi.org/10.3390/sym12030442.
3. R. Simone, *On finite mixtures of Discretized Beta model for ordered responses*, TEST **31** (2022), 828–855, https://doi.org/10.1007/s11749-022-00800-7.
