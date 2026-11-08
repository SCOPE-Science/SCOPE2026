# Geometric-to-exponential transition for minimally filled types at coupon completion

## Finding

Consider an independent sequence of draws from \(n\ge2\) equally likely coupon types. For an integer \(m=m_n\ge1\), stop on the first draw at which every type has been seen at least \(m\) times. Denote by \(K_n\) the number of types whose count at this stopping instant is **exactly** \(m\). Thus \(K_n\ge1\), and this is a statistic of the stopped occupancy vector, not of the hitting time alone.

Define, for \(t>0\),
\[
Q_m(t)=e^{-t}\sum_{j=0}^{m-1}\frac{t^j}{j!},\quad
f_m(t)=e^{-t}\frac{t^{m-1}}{(m-1)!},\quad
p_m(t)=e^{-t}\frac{t^m}{m!}.
\]
Let \(b_n\) be the unique positive root of \(nQ_{m_n}(b_n)=1\), and let \(A_n=b_n/m_n-1\), which is strictly positive for all sufficiently large \(n\).

**Exact finite-sample law.** For every \(n\ge2\), \(m\ge1\), and \(1\le k\le n\),
\[
\Pr(K_n=k)=n\binom{n-1}{k-1}\int_0^\infty f_m(t)
 p_m(t)^{k-1}\bigl(1-Q_m(t)-p_m(t)\bigr)^{n-k}\,dt.
\]

**Asymptotic classification.** With no monotonicity requirement on \(m_n\), the following implications hold along every applicable subsequence:
\[
A_n\longrightarrow a\in[0,\infty)
\quad\Longrightarrow\quad K_n\Rightarrow \operatorname{Geom}\left(\frac1{1+a}\right),
\]
where \(\Pr(\operatorname{Geom}(p)=k)=p(1-p)^{k-1}\) for \(k\ge1\), including the point mass at one when \(a=0\); and
\[
A_n\longrightarrow\infty
\quad\Longrightarrow\quad\frac{K_n}{A_n}\Rightarrow\operatorname{Exp}(1).
\]
For the natural transition scale \(m_n/\log n\to\alpha\in(0,\infty)\), let \(r_\alpha>1\) be the unique solution of
\[
r_\alpha-1-\log r_\alpha=\frac1\alpha.
\]
Then \(K_n\Rightarrow\operatorname{Geom}(1/r_\alpha)\). For \(m_n/\log n\to\infty\), \(K_n\to1\) in probability. For \(m_n/\log n\to0\), \(A_n\to\infty\) and the exponential normalization applies. In particular, when \(m_n\sim\log n\), the limiting geometric success parameter is \(1/r_1\approx0.3178444\).

## Assumptions and scope

All coupon labels are independent and uniform on the same \(n\)-element set; sampling is with replacement. The multiplicity threshold is common to all labels and may grow at an arbitrary rate. These results concern the occupancy vector at its **own** first \(m\)-coverage time; they do not describe counts at a deterministic clock time, unequal coupon probabilities, or a separately delayed first-coverage time.

## Proof

**1. Exact stopped law by Poisson embedding.** Give each type an independent rate-one Poisson process. Their merged chronological marks are independent uniform coupon labels, so the joint count vector at the first all-types-\(m\) event is exactly that of the discrete draws. The \(m\)-th arrival times of the individual processes are independent \(\operatorname{Gamma}(m,1)\) variables. Their maximum \(\tau_n\) is attained uniquely almost surely. Its density is \(nf_m(t)F_m(t)^{n-1}\), where \(F_m=1-Q_m\). Conditional on the maximum being \(t\) and its attaining type, the other processes independently have \(m\)-th arrival time at most \(t\); each has count exactly \(m\) with conditional probability \(p_m(t)/F_m(t)\). Consequently
\[
K_n-1\mid\tau_n=t\sim\operatorname{Bin}\left(n-1,\frac{p_m(t)}{F_m(t)}\right),
\]
and multiplication of the binomial probability by the maximum density proves the finite-sample formula.

**2. Uniform tail and local mark asymptotics.** Write \(b=b_n\), \(m=m_n\), and \(w=Q_m(b)/f_m(b)\). We establish
\[
\frac{b-m}{\sqrt m}\to\infty,\quad
w\sim\frac b{b-m},\quad
\frac{w}{b-m}\to0.
\]
For bounded \(m\), the first statement follows from \(Q_m(b)=1/n\to0\) and \(b\to\infty\). If \(m\to\infty\), the central limit theorem for a sum of \(m\) exponential variables and \(Q_m(b)=1/n\) imply \((b-m)/\sqrt m\to\infty\). Subsequence reasoning covers arbitrary \(m_n\). For \(b>m\), use the exact identity
\[
\frac{Q_m(b)}{f_m(b)}=\int_0^\infty e^{-s}\left(1+\frac sb\right)^{m-1}ds.
\]
Set \(\delta=1-(m-1)/b\). The integrand is at most \(e^{-\delta s}\), proving the upper bound \(w\le1/\delta\). For a lower bound, truncate to \(0\le s\le(b\delta^2)^{1/4}/\delta\) and expand \((m-1)\log(1+s/b)\): the error is \(o(1)\) uniformly because \(b\delta^2\to\infty\). Thus \(w\delta\to1\). Since \(\delta\sim(b-m)/b\), this gives the stated tail ratio and \(w/(b-m)\sim b/(b-m)^2\to0\).

The same estimates hold uniformly for \(t=b+wx\), \(x\) in any compact set, since the shift is \(o(b-m)\). In particular, if \(h_m(t)=f_m(t)/Q_m(t)\), then \(w h_m(b+wx)\to1\). Integration of \(d\log Q_m/dt=-h_m\) therefore yields
\[
nQ_m(b+wx)\to e^{-x}.
\]
Further, the marked-count ratio satisfies
\[
\frac{p_m(b+wx)}{Q_m(b+wx)}
=\frac{b+wx}{m}\,h_m(b+wx)
\sim\frac{b-m}{m}=A_n.
\]
These asymptotics remain valid when \(A_n\to0\) or \(A_n\to\infty\): the relative error is controlled by \(b/(b-m)^2\to0\).

**3. Mixture and transition.** The maximum CDF is \(F_m(t)^n\). Hence \(X_n=(\tau_n-b)/w\Rightarrow G\), where \(\Pr(G\le x)=e^{-e^{-x}}\). Also \(e^{-G}\sim\operatorname{Exp}(1)\). On events with \(X_n\) in a fixed compact set, the conditional binomial success probability tends uniformly to zero and its mean is asymptotic to \(A_n e^{-X_n}\). Tightness of \(X_n\) extends this to the random maximum. If \(A_n\to a<\infty\), the conditional binomial law tends to a mixed Poisson law with mixing variable \(a e^{-G}\), and its probability generating function is
\[
\mathbb E\exp\bigl[-a(1-z)e^{-G}\bigr]
=\frac1{1+a(1-z)},\qquad0\le z\le1.
\]
Therefore \(K_n-1\) is asymptotically geometric on nonnegative integers with success probability \(1/(1+a)\). If \(A_n\to\infty\), the conditional binomial variance is bounded by its mean, which is \(O_{\Pr}(A_n)\); division by \(A_n\) makes the centered binomial fluctuation negligible. Thus \(K_n/A_n\Rightarrow e^{-G}\sim\operatorname{Exp}(1)\).

**4. Threshold identification.** For each fixed \(r>1\), the gamma upper-tail large-deviation rate is
\[
-\frac1m\log Q_m(mr)\to I(r)=r-1-\log r\quad(m\to\infty).
\]
It follows by monotonicity of \(Q_m\) and the quantile equation that \(b_n/m_n\to r_\alpha\) when \(m_n/\log n\to\alpha\in(0,\infty)\). The same comparison shows \(b_n/m_n\to1\) when \(m_n/\log n\to\infty\), and \(b_n/m_n\to\infty\) when \(m_n/\log n\to0\) (the last assertion follows also for bounded \(m_n\) from \(b_n\to\infty\)). This completes the classification.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to evaluate the displayed integral by finite polynomial expansion and independent absorption-state dynamic programming for the original coupon process. All \(143\) assertions pass for \(2\le n\le5\) and \(1\le m\le3\), including normalization and the historical harmonic-mean identity at \(m=1\). The finite checks do not establish the infinite-limit theorem; that conclusion follows from the analytic steps above. Run `python verify.py` using Python 3 standard library.

## Relationship to prior work

Castro and Marinho, arXiv:2610.33199v1, obtain Gumbel completion-time limits for growing collection multiplicity; this does not specify the number of exactly-minimal types *at completion*. Long, arXiv:2604.25108v2, establishes a uniform gamma-tail quantile lemma and moment laws for the stopping time; its tail normalization is consistent with, and independently supports, Step 2. Myers and Wilf, arXiv:math/0304229v1, give the full finite distribution and harmonic mean for singletons at first coverage (the special case \(m=1\)), which is prior work and not a novelty claim here. Ilienko, arXiv:2002.00650v1, studies numbers of unfilled later collections at first coverage or deterministically delayed times and fixed-level point-process limits; it also suggests extensions around higher completion times. The present new content is the marked stopped-law classification for **growing** \(m\), especially the geometric family at \(m\asymp\log n\), including its parameter and both neighboring regimes.

## Limitations

There are no finite-sample rate bounds or convergence of moments asserted for general \(m_n\). The exact integral is an identity, not a claim to computational complexity improvements. Earlier fixed-\(m\) consequences can be implicit in point-process results. The historical-priority assessment may change if a broader marked-extremes or stopped-occupancy theorem covering varying multiplicities is identified. Independent mathematical validation has not been performed.

## References

1. M. E. Castro and R. Marinho, *Cutoff profile for the coupon collector with many collections*, arXiv:2610.33199v1, first posted 2026-10-23. https://arxiv.org/abs/2610.33199
2. C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108v2, §3.1 and Appendix A. https://arxiv.org/html/2604.25108v2
3. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1, §4. https://arxiv.org/html/math/0304229v1
4. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650v1, published in *Modern Stochastics: Theory and Applications* (2026), §§1–2, 7–8. https://www.vmsta.org/journal/VMSTA/article/358/text
