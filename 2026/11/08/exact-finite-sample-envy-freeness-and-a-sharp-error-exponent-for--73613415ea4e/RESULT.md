# Exact finite-sample envy-freeness and a sharp error exponent for welfare-maximizing allocations

## Finding

Consider two agents and \(m\ge 1\) labeled indivisible goods. For each good \(g\), their additive marginal values \(X_g,Y_g\) are mutually independent uniform random variables on \([0,1]\), independent across goods. Assign every good to the agent with the higher value (ties have probability zero). Let \(F_m\) be the probability that this uniquely welfare-maximizing complete allocation is envy-free (EF).

For all integers \(m\ge1\), put
\[
Q_m=\sum_{\substack{r,s,u\ge0\\r+s+u=m\\r>u}}
\frac{m!}{r!s!u!}\sum_{j=0}^{r}(-1)^{r-j}\binom rj
\frac{(r-u)^{2m-s-j}}{(2m-s-j)!}.
\]
Then the **exact rational probability** is
\[
\boxed{F_m=2Q_m-1.}
\]
In particular,
\[
F_1=0,\qquad F_2=\frac13,\qquad F_3=\frac{23}{60},\qquad
F_4=\frac{55}{126},\qquad F_5=\frac{4927}{10080}.
\]

A sharp asymptotic identifies the first-order constant, not just exponential convergence. Let
\[
M(t)=\begin{cases}\displaystyle\frac{(t-1)e^t+t+e^{-t}}{t^2},&t\ne0,\\1,&t=0,\end{cases}
\]
let \(\theta<0\) be the **unique** root of \(M'(\theta)=0\), and put \(\rho=M(\theta)\) and \(\sigma^2=M''(\theta)/M(\theta)\). Then
\[
\boxed{1-F_m=\frac{2\rho^m}{|\theta|\sigma\sqrt{2\pi m}}\bigl(1+o(1)\bigr),\qquad m\to\infty.}
\]
Numerically, \(\theta\approx-0.55313582658\), \(\rho\approx0.95530710097\), \(-\log\rho\approx0.04572241850\), \(\sigma^2\approx0.29113197755\), and \(2/(|\theta|\sigma\sqrt{2\pi})\approx2.67339615\).

## Assumptions and scope

The two agents have **nonnegative additive** utilities, no resource constraints other than allocating each good exactly once, and fully independent \(\operatorname{Uniform}(0,1)\) values. Envy-freeness means each agent values their own allocated bundle at least as much as the other bundle. The probability is over the \(2m\) independent draws; no randomization is required by the allocation mechanism itself. The finite identity holds for every integer \(m\ge1\); the asymptotic fixes two agents and lets \(m\to\infty\).

## Proof

**1. Reduce envy-freeness to a one-dimensional sum.** Define the first agent's own-minus-other utility contribution for good \(g\) by
\[
Z_g=X_g\mathbf1_{\{X_g>Y_g\}}-X_g\mathbf1_{\{X_g<Y_g\}}.
\]
Define the second agent's analogous contribution \(W_g=Y_g\mathbf1_{\{Y_g>X_g\}}-Y_g\mathbf1_{\{Y_g<X_g\}}\). Almost surely, \(Z_g+W_g=|X_g-Y_g|>0\). Therefore both agents cannot envy one another at the same time. Exchanging their labels preserves the joint law, so
\[
F_m=1-2\Pr\{Z_1+\cdots+Z_m<0\}=2\Pr\{Z_1+\cdots+Z_m>0\}-1.
\]
The zero-sum event has probability zero by absolute continuity.

**2. Find the exact summand distribution.** Conditioning on the first agent's value \(X_g=x\), the probability of winning is \(x\) and of losing is \(1-x\). Thus the \(Z_g\) are iid with probability density
\[
f(z)=\begin{cases}1+z,&-1<z<0,\\z,&0<z<1,\\0,&\text{otherwise}.\end{cases}
\]
Consequently \(M(t)=\mathbb E[e^{tZ_g}]=\int_0^1\bigl(xe^{tx}+(1-x)e^{-tx}\bigr)\,dx\), which evaluates to the displayed expression. In particular, \(M(0)=1\), \(M'(0)=\mathbb EZ_g=1/6\), and \(M''(t)>0\) for all real \(t\).

**3. Invert the finite bilateral transform.** For every \(t>0\), integer \(h\ge1\), and real \(a\), the bilateral Laplace transform of \((a-z)_+^{h-1}/(h-1)!\) is \(e^{at}/t^h\), because
\[
\int_{-\infty}^{a}e^{tz}\frac{(a-z)^{h-1}}{(h-1)!}\,dz=\frac{e^{at}}{t^h}.
\]
Expand the transform of the sum as
\[
M(t)^m=t^{-2m}\sum_{r+s+u=m}\frac{m!}{r!s!u!}e^{(r-u)t}(t-1)^r t^s,
\]
and expand \((t-1)^r\) binomially. Every resulting term has the form \(c\,e^{(r-u)t}/t^{2m-s-j}\) with a strictly positive integer denominator exponent. The finite signed combination of the inverse-transform functions equals the sum density almost everywhere: after replacing \(z\) by \(m-z\), uniqueness of the ordinary Laplace transform applies to these locally integrable functions of polynomial growth. Integrating this equality over \(z>0\) is legitimate term by term, because each inverse term vanishes for \(z>r-u\) and
\[
\int_0^\infty\frac{(a-z)_+^{h-1}}{(h-1)!}\,dz=\frac{(a_+)^h}{h!}.
\]
Only \(r>u\) contributes, giving \(\Pr\{\sum_gZ_g>0\}=Q_m\) and proving the finite formula.

**4. Prove the sharp large-deviation asymptotic.** Since \(M'(0)=1/6>0\), \(M''(t)>0\), and \(M'(t)\to-\infty\) as \(t\to-\infty\), there is a unique \(\theta<0\) with \(M'(\theta)=0\). Strict convexity gives \(0<\rho=M(\theta)<1\). Define the tilted density \(f_\theta(z)=e^{\theta z}f(z)/\rho\). It is a compactly supported, nonlattice, bounded density with mean zero and variance \(\sigma^2>0\). If \(h_m\) is the density of a sum of \(m\) independent variables with this tilted law, exponential change of measure gives
\[
\Pr\left\{\sum_gZ_g<0\right\}=\rho^m\int_{-\infty}^0e^{-\theta z}h_m(z)\,dz.
\]
The **local** central limit theorem yields \(\sqrt m\,h_m(z)\to1/(\sigma\sqrt{2\pi})\) for every fixed \(z\). For completeness, its Fourier proof applies here directly: the tilted density is piecewise smooth with bounded support, so its characteristic function is \(O(1/|t|)\); the square is integrable, it has modulus strictly below one away from zero, and its Taylor expansion at zero is \(1-\sigma^2t^2/2+o(t^2)\). Fourier inversion then yields both the local limit and \(\sup_z\sqrt m\,h_m(z)=O(1)\). Since \(\theta<0\), \(e^{-\theta z}\) is integrable over the negative half-line. Dominated convergence therefore gives
\[
\sqrt m\int_{-\infty}^0e^{-\theta z}h_m(z)\,dz
\longrightarrow\frac{1}{|\theta|\sigma\sqrt{2\pi}}.
\]
Finally multiply by \(\rho^m\) and use the factor of two from step 1. This proves the claimed asymptotic with its exact prefactor.

## Verification

Run `python3 verify.py`. The standalone program uses integer/rational arithmetic to evaluate the finite sum, independently derives the two-good probability using maximum/minimum order statistics, compares six probabilities with direct seeded simulations of the full two-agent mechanism, and computes \(\theta\), \(\rho\), \(\sigma\), and the prefactor using independently evaluated defining integrals. A separate numerical check of convolution with the exact piecewise-linear density agreed with the exact finite formula for \(m=1,\ldots,12\) to better than \(1.2\times10^{-7}\); it is numerical corroboration, not proof of the infinite assertion.

## Relationship to prior work

The welfare-maximizing allocation and its eventual envy-freeness under symmetric independent values were already established in Dickerson et al. (2014); related results on groups, online allocation, and asymmetric preferences appear in Manurangsi and Suksompong (2017), Zeng and Psomas (2019), and Bai and Gölz (2021). Bu and Tao (2026) study the complexity of jointly obtaining envy-free and welfare-optimal allocations. The contribution here is restricted to the **exact finite-\(m\) probability** and the **sharp exponential rate including its leading constant** for the canonical two-agent uniform model; mere eventual envy-freeness and the allocation mechanism are not claimed to be new.

## Limitations

The exact arithmetic does not automatically extend to other value distributions, correlations, more than two agents, or nonadditive valuations. The sharp asymptotic is an \(m\to\infty\) statement, with no claimed finite error bound. Published literature comparisons do not rule out unindexed or independently derived equivalent formulas. An independent scientific audit has not been performed.

## References

1. X. Bu and B. Tao, *Fair and Efficient Allocations: Decision Problems in the Gap of Polynomial Hierarchy*, arXiv:2609.31849, first posted 2026-09-25. https://arxiv.org/abs/2609.31849
2. J. P. Dickerson, J. Goldman, J. Karp, A. Procaccia, and T. Sandholm, *The Computational Rise and Fall of Fairness*, AAAI 2014, DOI:10.1609/aaai.v28i1.8884. https://jpdickerson.com/pubs/dickerson14computational.pdf
3. P. Manurangsi and W. Suksompong, *Asymptotic Existence of Fair Divisions for Groups*, Mathematical Social Sciences 89 (2017), 100–108. https://arxiv.org/abs/1706.08219
4. D. Zeng and A. Psomas, *Fairness-Efficiency Tradeoffs in Dynamic Fair Division*, arXiv:1907.11672. https://arxiv.org/abs/1907.11672
5. Y. Bai and P. Gölz, *Envy-Free and Pareto-Optimal Allocations for Agents with Asymmetric Random Valuations*, IJCAI 2022; arXiv:2109.08971. https://arxiv.org/abs/2109.08971
