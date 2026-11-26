# Two-tail covariance phases for Pearson chi-square and occupancy frequencies

## Finding

Let \(n,m\ge2\) be integers, and throw \(n\) independently labeled balls uniformly into \(m\) boxes. Write \(N_i\) for the occupancy of box \(i\), and for every \(0\le r\le n\) define the frequency-spectrum statistic \(M_r=\#\{i:N_i=r\}\). Consider Pearson's classical uniformity statistic
\[
X^2=\sum_{i=1}^m\frac{(N_i-n/m)^2}{n/m}.
\]
For \(p=1/m\), \(q=1-p\), and \(B\sim\operatorname{Bin}(n-2,p)\), every real function \(f\colon\{0,\ldots,n\}\to\mathbb R\) satisfies the exact **collision--curvature identity**
\[
\boxed{\operatorname{Cov}\!\left(X^2,\sum_{i=1}^mf(N_i)\right)
=(n-1)q\,\mathbb E\,[f(B+2)-2f(B+1)+f(B)].}\tag{1}
\]
In particular, put
\[
P_{n,p}(r)=r(r-1)-2r(n-1)p+n(n-1)p^2,
\qquad
\beta_{n,p}(r)=\binom nrp^rq^{n-r}.
\]
Then the entire Pearson--frequency covariance spectrum is explicit:
\[
\boxed{\operatorname{Cov}(X^2,M_r)
=\frac{\beta_{n,p}(r)}{np^2q}\,P_{n,p}(r).}\tag{2}
\]
Define two real roots
\[
r_\pm=(n-1)p+\frac12\pm\sqrt{npq+(\tfrac12-p)^2}.
\]
These satisfy \(0<r_-<r_+<n\). For every integer \(0\le r\le n\), the covariance in (2) is **positive on both tails** \(r<r_-\) and \(r>r_+\), **negative in the intervening band** \(r_-<r<r_+\), and is zero exactly when \(r=r_-\) or \(r=r_+\). In particular, the empty- and all-ball box counts have strictly positive covariance with \(X^2\), and at least one frequency count has strictly negative covariance.

Two natural fixed-frequency slices expose different transitions:

* **Singletons:** for \(M_1\), the covariance is strictly negative for \(n<2m\), vanishes precisely for \(n=2m\), and is strictly positive for \(n>2m\).
* **Doubletons:** for \(M_2\), define
\[
n_\pm(m)=\frac{4m+1\pm\sqrt{8m^2-8m+1}}2.
\]
For integer \(n\ge2\), its covariance is positive when \(n<n_-(m)\) or \(n>n_+(m)\), negative when \(n_-(m)<n<n_+(m)\), and zero at integer endpoints. The exact doubleton-decorrelation pairs are governed by the negative Pell equation
\[
k^2-2(2m-1)^2=-1.
\]
Every such \(m\ge2\) comes from \(k+(2m-1)\sqrt2=(1+\sqrt2)^{2j+1}\), \(j\ge1\), with the two integer sample sizes \(n=(4m+1\pm k)/2\). The first six pairs are \((m,n)=(3,3),(3,10),(15,10),(15,51),(85,51),(85,290)\). Thus exact zero dependence occurs along an infinite, sparse arithmetic family.

Finally, for any fixed \(r\ge0\) and a sequence \(n,m\to\infty\) with \(n/m\to\lambda>0\),
\[
\boxed{\frac1m\operatorname{Cov}(X^2,M_r)
\longrightarrow\frac{e^{-\lambda}\lambda^{r-1}}{r!}\left[r(r-1)-2r\lambda+\lambda^2\right].}\tag{3}
\]
The expression is well defined for \(r=0\) because \(\lambda>0\). Its bracket is the second Poisson--Charlier polynomial (in the monic normalization), giving a sharp loading transition for any fixed occupancy frequency.

## Assumptions and scope

The sample size \(n\), alphabet size \(m\), and frequency index \(r\) are as above; every allocation has probability \(m^{-n}\). Only the completely specified uniform null is considered. The statistic \(X^2\) uses expected count \(n/m\) in **each** box; its expectation is \(m-1\). The binary collision observable is \(\mathbf1_{\{X_a=X_b\}}\) for two sampled labels \(a<b\). All finite-sample assertions are exact and require no limiting approximation. Formula (3) assumes a fixed frequency index, not a frequency growing with \(m\).

## Proof

Let \(X_1,\ldots,X_n\) denote the independent uniform box labels, and put
\[
T=\sum_{1\le a<b\le n}\mathbf1_{\{X_a=X_b\}}.
\]
Since \(\sum_iN_i=n\) and \(\sum_iN_i^2=n+2T\), direct expansion gives
\[
X^2=m-n+\frac{2m}{n}T.\tag{4}
\]
Take an arbitrary \(F_f=\sum_i f(N_i)\). By exchangeability of observation pairs,
\[
\operatorname{Cov}(X^2,F_f)
=\frac{2m}{n}\binom n2\operatorname{Cov}(\mathbf1_{\{X_1=X_2\}},F_f)
=(n-1)\bigl(\mathbb E[F_f\mid X_1=X_2]-\mathbb EF_f\bigr),\tag{5}
\]
because \(\Pr(X_1=X_2)=1/m\). Conditional on that collision, the common box is uniformly chosen, and the other \(n-2\) labels remain independent and uniform. Thus, with \(B\sim\operatorname{Bin}(n-2,p)\),
\[
\mathbb E[F_f\mid X_1=X_2]=\mathbb Ef(B+2)+(m-1)\mathbb Ef(B).
\]
Without conditioning, a fixed box has occupancy distributed as \(B+V\), with independent \(V\sim\operatorname{Bin}(2,p)\); hence
\[
\mathbb EF_f=m\left[p^2\mathbb Ef(B+2)+2pq\mathbb Ef(B+1)+q^2\mathbb Ef(B)\right].
\]
Subtracting the last two displays, using \(mp=1\), yields \(q\,\mathbb E\Delta^2f(B)\), where \(\Delta^2f(b)=f(b+2)-2f(b+1)+f(b)\). Combined with (5), this proves (1) for **every** real \(f\) on the entire stated domain.

For the coordinate indicator \(f(k)=\mathbf1_{\{k=r\}}\), and with \(b_j=\Pr(B=j)\) extended as zero outside \(0\le j\le n-2\), equation (1) gives
\[
\operatorname{Cov}(X^2,M_r)=(n-1)q\,(b_{r-2}-2b_{r-1}+b_r).\tag{6}
\]
For all \(0\le r\le n\), the binomial coefficient ratios, with out-of-range terms interpreted as zero, give
\[
\frac{b_{r-2}}{\beta_{n,p}(r)}=\frac{r(r-1)}{n(n-1)p^2},\qquad
\frac{b_{r-1}}{\beta_{n,p}(r)}=\frac{r(n-r)}{n(n-1)pq},\qquad
\frac{b_r}{\beta_{n,p}(r)}=\frac{(n-r)(n-r-1)}{n(n-1)q^2}.
\]
Substitution in (6) and elementary simplification gives (2); an equivalent useful form is
\[
P_{n,p}(r)=(r-np)^2-(1-2p)(r-np)-npq.\tag{7}
\]
The positive factor in (2) makes the covariance sign exactly that of \(P_{n,p}(r)\). Equation (7) gives the stated roots. Its quadratic minimum is \(-npq-(\tfrac12-p)^2<0\), attained at \(r=(n-1)p+1/2\), strictly between \(0\) and \(n\). Moreover \(P_{n,p}(0)=n(n-1)p^2>0\) and \(P_{n,p}(n)=n(n-1)q^2>0\), proving the strict root placement and both-tail signs. Since \(\sum_{r=0}^nM_r=m\) deterministically, \(\sum_r\operatorname{Cov}(X^2,M_r)=0\), and strict positivity at \(r=0\) forces a negative value at some other integer \(r\).

For \(r=1\), direct substitution yields \(P_{n,p}(1)=(n-1)p(np-2)\), proving the singleton threshold. For \(r=2\), multiplication by \(m^2\) yields
\[
m^2P_{n,1/m}(2)=n^2-(4m+1)n+2m^2+4m.\tag{8}
\]
Its discriminant is \(8m^2-8m+1\) and both real roots exceed \(2\), giving the doubleton sign statement. For integer \(m,n\), a zero exists precisely when the discriminant is an odd square \(k^2\), equivalently \(k^2-2(2m-1)^2=-1\). Conversely every positive odd-exponent solution of this classical negative Pell equation provides odd \(k\), odd \(2m-1\), and the two integral roots \((4m+1\pm k)/2\) in the allowed sample-size range. The standard descent by multiplication with \(3-2\sqrt2\) reduces every positive solution beyond \((1,1)\) to a smaller positive solution, so the complete positive solution sequence is \((1+\sqrt2)^{2j+1}\). This proves the complete arithmetic classification.

For (3), \(B\) converges in law to \(\operatorname{Pois}(\lambda)\), while \((n-1)q/m\to\lambda\). Apply (6), noting that the three point probabilities converge, and use
\[
\pi_{r-2}-2\pi_{r-1}+\pi_r
=\frac{e^{-\lambda}\lambda^{r-2}}{r!}
[r(r-1)-2r\lambda+\lambda^2],
\]
where \(\pi_j=0\) for \(j<0\), to obtain the asserted limit. For \(r=0\), the algebraic form is interpreted by cancellation of the positive \(\lambda\) powers, not by a probability at negative index.

## Verification

The standalone `VERIFY.py` enumerates occupancy compositions with exact multinomial probabilities, computes \(X^2\), each \(M_r\), their means and covariance independently of (1)--(2), and compares the result with the closed formulas. It also tests the curvature identity for two non-indicator nonlinear functions and checks the first six doubleton Pell-zero examples. The verification uses only Python's standard library and exact rational arithmetic. The complete finite grid consists of \(m=2,\ldots,7\), \(n=2,\ldots,10\) whenever the number of compositions does not exceed \(25{,}000\). These finite tests support but do not replace the all-parameter proof above.

## Relationship to prior work

Pearson's chi-squared statistic and its collision-\(U\)-statistic representation are established methods; see Kim (2018), Section 2, especially Lemma 2.1. Gupta and Price (2022) discuss collision, singleton, empty-bin, and other separable occupancy statistics in uniformity-testing efficiency and large-deviation analyses; their Appendix A studies covariances between two cell-score statistics. Barbour and Gnedin (2008) study frequency-spectrum counts and their joint asymptotics in general occupancy schemes. These works motivate a joint comparison but the inspected relevant statements do not provide the exact finite null covariance of the Pearson statistic against **every** frequency count, its two real sign thresholds, the doubleton's reentrant sign law and complete Pell decorrelation family.

Two related public findings concern covariance between *occupied richness* \(K=\#\{i:N_i>0\}\) and frequency counts \(M_r\), and covariance between richness and *the total pair-collision count*. They are not equivalent to the coordinatewise collision--frequency spectrum in (2): they replace one observable by richness, or aggregate over the whole frequency spectrum. The new content is the curvature identity and its exact signed and arithmetic consequences, not the elementary collision representation itself.

## Limitations

Uniform box probabilities and Pearson normalization by \(n/m\) are essential to the compact scalar curvature formula. An arbitrary multinomial null generally introduces box-dependent weights. Positive covariance does not assert stochastic positive association or imply improved goodness-of-fit power; none is claimed. The two-tail classification is for covariance with a single \(M_r\), not a full covariance-matrix sign law. The Poisson limit requires fixed \(r\) and positive finite loading \(\lambda\). Classical occupancy texts could contain equivalent finite-moment identities under other nomenclature; targeted literature checks reduce but do not eliminate historical-priority risk.

## References

1. Ilmun Kim, *Multinomial Goodness-of-Fit Based on U-Statistics: High-Dimensional Asymptotic and Minimax Optimality*, arXiv:1812.08924, first publicly submitted 2018-12-21, Section 2 and Appendix.
2. Shivam Gupta and Eric Price, *Sharp Constants in Uniformity Testing via the Huber Statistic*, arXiv:2206.10722, first publicly submitted 2022-06-21, Introduction and Appendix A.
3. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, first publicly submitted 2008-09-25.
4. I. Diakonikolas et al., *Collision-based Testers are Optimal for Uniformity and Closeness*, arXiv:1611.03579, first publicly submitted 2016-11-11.
