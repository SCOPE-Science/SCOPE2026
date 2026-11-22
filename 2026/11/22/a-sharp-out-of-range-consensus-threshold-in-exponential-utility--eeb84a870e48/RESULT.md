# A sharp out-of-range consensus threshold in exponential-utility two-agent opinion dynamics

## Finding

Consider two individuals obeying the noise-free utility-weighted pair rule of Siebenmorgen and Restrepo, with exponential utility \(U(z)=e^{\kappa z}\), \(\kappa>0\), and learning rate \(0<\mu<1\). Despite exact geometric contraction of their disagreement, their eventual shared opinion can lie outside the interval of initial opinions. If their initial gap is \(d>0\), there is a **unique** critical learning rate \(\mu_c(\kappa d)\in(1/2,1)\): consensus belongs to the initial interval for \(\mu\le\mu_c\), and exceeds the initially larger opinion for \(\mu>\mu_c\). In particular, the consensus tends to positive infinity as \(\mu\uparrow1\) with all other data fixed. The threshold has sharp weak- and strong-utility asymptotics.

## Assumptions and scope

Fix \(\kappa>0\), \(0<\mu<1\), and two real initial opinions \(x_0<y_0\), with \(d=y_0-x_0>0\). Choose a confidence radius \(\varepsilon>d\), so that the pair remains receptive. Set \(m_0=(x_0+y_0)/2\), \(a=\kappa d/2\), and \(r=|1-2\mu|\). At integer times, both agents update synchronously according to
\[
 x_{t+1}=x_t+2\mu\frac{e^{\kappa y_t}}{e^{\kappa x_t}+e^{\kappa y_t}}(y_t-x_t),\qquad
 y_{t+1}=y_t+2\mu\frac{e^{\kappa x_t}}{e^{\kappa x_t}+e^{\kappa y_t}}(x_t-y_t).
\]
The factor two corresponds to the two-agent normalization \(\mu N/(N-1)\) of the originating model. Opinions are mathematically real-valued; no hard projection to a bounded opinion domain is imposed. Define \(L_\mu=\lim_{t\to\infty}x_t=\lim_{t\to\infty}y_t\). Then
\[
 L_\mu=m_0+\mu d\sum_{j=0}^{\infty}r^j\tanh(a r^j).
\tag{1}
\]
For \(\mu>1/2\) put \(r=2\mu-1\) and
\[
 H_a(r)=\frac{1+r}{2}\sum_{j=0}^\infty r^j\tanh(a r^j).
\tag{2}
\]
There exists exactly one \(r_c(a)\in(0,1)\) such that \(H_a(r_c)=1/2\), and \(\mu_c=(1+r_c)/2\). More precisely,
\[
 \mu_c(\kappa d)=1-\frac{\kappa d}{4}+O((\kappa d)^3) \quad(\kappa d\downarrow0),
\]
\[
 \mu_c(\kappa d)=\frac12+e^{-\kappa d}(1+o(1))\quad(\kappa d\to\infty).
\]
Finally,
\[
 L_\mu=m_0+\frac{\log\cosh(\kappa d/2)}{\kappa(1-\mu)}+O_{\kappa,d}(1),\qquad \mu\uparrow1.
\tag{3}
\]

## Proof

**Exact contraction and drift.** Subtract the two updates. Their utility fractions sum to one, so \(y_{t+1}-x_{t+1}=(1-2\mu)(y_t-x_t)\). Thus \(y_t-x_t=(1-2\mu)^td\), and the absolute gap never exceeds the initial gap. In particular the confidence test stays satisfied. Writing \(m_t=(x_t+y_t)/2\) and simplifying the difference between the two utility fractions gives
\[
 m_{t+1}-m_t=\mu(y_t-x_t)\tanh\!\left(\frac{\kappa(y_t-x_t)}2\right)
 =\mu d r^t\tanh(a r^t)>0.
\]
Since \(r<1\), these increments are summable, giving (1), geometric agreement, and a common finite limit for each fixed \(\mu<1\).

**Crossing of the initial convex hull.** For \(0<\mu\le1/2\), each update is a convex combination of the two existing opinions because its cross-weight is at most \(2\mu\le1\). Hence both remain within the initial interval, and the positive mean drift gives \(L_\mu>m_0\). For \(1/2<\mu<1\), (1) becomes \(L_\mu-m_0=dH_a(r)\). Every term of \(H_a(r)\) is continuous and increasing in \(r\in[0,1)\), and its zeroth term is strictly increasing, so \(H_a\) is continuous and strictly increasing. At \(r=0\), \(H_a(0)=\tanh(a)/2<1/2\). As \(r\uparrow1\), arbitrarily many initial summands stay bounded below by a fixed positive value, so \(H_a(r)\to\infty\). The intermediate value theorem gives a unique \(r_c\) and hence a unique \(\mu_c\). As \(L_\mu>m_0\), leaving \([x_0,y_0]\) can only occur above \(y_0=m_0+d/2\), precisely when \(H_a(r)>1/2\).

**Small utility gradient.** At \(r_c\), use \(z-z^3/3\le\tanh z\le z\) for \(z\ge0\). Since \(\mu/(1-r^2)=1/[4(1-\mu)]\) on the branch \(r=2\mu-1\), the critical identity \((L_\mu-m_0)/d=1/2\) implies
\[
 \frac{a}{4(1-\mu_c)}\left(1-\frac{a^2}{3}\right)
 \le\frac12\le\frac{a}{4(1-\mu_c)}.
\]
Consequently \(a(1-a^2/3)/2\le1-\mu_c\le a/2\); substituting \(a=\kappa d/2\) proves the first expansion.

**Strong utility gradient.** Write \(\delta=\mu_c-1/2\), \(r_c=2\delta\). The crossing equation reads
\[
 (1/2+\delta)\left[\tanh a+\sum_{j\ge1}(2\delta)^j\tanh(a(2\delta)^j)\right]=1/2.
\]
The zeroth term gives \(\delta\le (\coth a-1)/2=1/(e^{2a}-1)\), so \(\delta=O(e^{-2a})\). The tail is at most \(a r_c^2/(1-r_c^2)=O(ae^{-4a})=o(e^{-2a})\), since \(\tanh z\le z\). Using \(\tanh a=1-2e^{-2a}+O(e^{-4a})\) in the crossing equation yields \(\delta=e^{-2a}(1+o(1))=e^{-\kappa d}(1+o(1))\).

**Divergent consensus near the maximal learning rate.** On \(\mu>1/2\), write \(s=-\log r\) and \(g(v)=e^{-v}\tanh(ae^{-v})\). The function \(g\) is nonnegative, decreasing and integrable. Integral comparison for a monotone Riemann sum gives
\[
 \sum_{j=0}^\infty g(js)=\frac1s\int_0^\infty g(v)\,dv+O(1)
 =\frac{\log\cosh a}{a s}+O(1).
\]
Since \(s=-\log(2\mu-1)=2(1-\mu)+O((1-\mu)^2)\), multiplying by \(\mu d\) proves (3), including the positive diverging coefficient.

## Verification

The standalone `check.py` compares direct synchronous iteration with the exact series over 50 parameter combinations (including both sides of the learning-rate transition), numerically solves for sample critical rates, and checks scaled high-learning behavior. Run `python check.py` with Python 3; no nonstandard packages are required. The general statements follow from the analytic proof, not from the finite numerical tests. For \(\kappa=d=1\), \(\mu_c\approx0.764874065819\). With \(x_0=0,y_0=1,\mu=0.9\), the limiting opinion is approximately \(1.69114933003\), exceeding both starting opinions.

## Relationship to prior work

The underlying two-agent update rule, including geometric decay of the pair difference, follows directly from Siebenmorgen and Restrepo (2026), Equation (1) and their two-agent observation. The originating work studies utility bias and noise-driven opinion dynamics, including a stationary collective-polarization distribution; it does not give this no-noise exponential-utility sharp convex-hull-exit threshold, its uniqueness or the divergence law. Published work on finite-population weak-noise Gibbs exponents for the same utility-weighted setting is related but analyzes stochastic aggregate behavior, not the pathwise deterministic threshold here. Known convex-combination invariance for conventional averaging is explicitly used for the low-rate regime; this result instead delineates its failure under the source's normalized high-rate update. The checked materials do not constitute an exhaustive historical-priority proof.

## Limitations

This is a deterministic two-individual result for unbounded real opinions with positive exponential utility and synchronous interaction; it does not establish overshoot in noisy finite populations, larger networks, or bounded-domain implementations that clip opinions. The sharp critical parameter depends on the product \(\kappa d\), not on an arbitrary initial configuration. Near \(\mu=1\), a formal limit of the infinite-time consensus diverges, but for each fixed \(\mu<1\) the consensus is finite. An independent scientific audit has not been performed.

## References

1. Siebenmorgen and Restrepo, *A Utility-Driven Bounded-Confidence Model for Opinion Dynamics*, arXiv:2605.21844 (first public 2026-05-21), https://arxiv.org/abs/2605.21844.
2. *The finite-population Gibbs exponent for noisy utility-weighted opinion averaging*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-finite-population-gibbs-exponent-for-noisy-utility-weighted--8f1089ea0c11 (related stochastic extension, not a source for the deterministic assertion).
