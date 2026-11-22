# A Gumbel false-positive boundary for dense-grid gamma-Cox zero detection

## Finding

For the gamma-driven Cox detector and refining lattice specified below, the outermost false-positive location has a universal Poisson-edge and Gumbel limit. Let \(R_K\) be the greatest absolute coordinate at which any atom is detected. Then for every \(t\in\mathbb R\),
\[
\lim_{K\to\infty}\Pr\!\left(KR_K^2-\log K-\log A_K\le t\right)=\exp\!(-2e^{-t}).
\]
More precisely, the signs and centered energy coordinates of all nonzero detected sites form two independent limiting Poisson point processes with intensity \(e^{-y}\,dy\). In the concrete dense-grid choice \(h_K=1/(\sqrt K(\log K)^2)\), one has
\[
\log K+\log A_K=\log K+\tfrac32\log\log K-\log2.
\]
The detection radius is asymptotically \(\sqrt{\log K/K}\), while the probability that *every* candidate is classified correctly tends to zero. This is a spatial resolution law, not a proof that the process exactly identifies arbitrary function zeros.

## Assumptions and scope

Let \(K>e\) tend to infinity. Take a deterministic spacing \(h_K>0\), define \(A_K=(2h_K\sqrt{K\log K})^{-1}\), and assume \(A_K\to\infty\) and \(\log A_K=o(\log K)\). The fixed test function is \(g(x)=x\) on \(\mathbb R\), whose only true zero is the lattice site \(j=0\). Candidates are \(x_{j,K}=jh_K\) for \(j\in\mathbb Z\). Independently sample \(C_{j,K}\sim\operatorname{Gamma}(K,1)\) using the rate-one convention, and conditionally independent \(N_{j,K}\sim\operatorname{Pois}(C_{j,K}e^{-K(jh_K)^2})\). Write \(I_{j,K}=\mathbf1_{\{N_{j,K}\ge1\}}\). Let \(R_K=\sup\{|jh_K|:I_{j,K}=1\}\), with \(R_K=0\) if no sites are detected. Define \(T_K=\log K+\log A_K\) and the point process, omitting the true zero,
\[
\Xi_K=\sum_{j\ne0}I_{j,K}\,\delta_{(\operatorname{sgn}j,\,Kj^2h_K^2-T_K)}.
\]
Convergence of \(\Xi_K\) means vague convergence of locally finite counting measures on the disjoint union \(\{-1,+1\}\times\mathbb R\). No claim concerns other functions, non-independent atomic masses, or a fixed finite candidate set.

## Proof

**1. The infinite detector exists.** For every fixed \(K\),
\[
\mathbb E\sum_{j\in\mathbb Z}C_{j,K}e^{-K(jh_K)^2}
=K\sum_{j\in\mathbb Z}e^{-K(jh_K)^2}<\infty.
\]
Consequently the random total atomic intensity is finite almost surely, and the conditional Poisson counts have a finite total almost surely. Integrating the Gamma Laplace transform, the indicators at distinct sites are independent Bernoulli variables, with
\[
p_{j,K}=\Pr(I_{j,K}=1)
=1-\left(1+e^{-K(jh_K)^2}\right)^{-K}.
\]
The exact zero at \(j=0\) is missed with probability \(2^{-K}\).

**2. Mesh and rare-success asymptotics.** On the positive side write \(E_{j,K}=Kj^2h_K^2\) and \(y_{j,K}=E_{j,K}-T_K\). Since \(T_K/\log K\to1\), sites whose energies lie in \(T_K+[a,b]\) have consecutive energy spacings
\[
E_{j+1,K}-E_{j,K}=Kh_K^2(2j+1)
=\frac1{A_K}(1+o(1))
\]
uniformly for fixed real \(a<b\). Indeed \(Kh_K^2=1/(4A_K^2\log K)\) and \(j\sim2A_K\sqrt{T_K\log K}\). On the same bounded energy window,
\[
Ke^{-E_{j,K}}=A_K^{-1}e^{-y_{j,K}},\qquad
p_{j,K}=A_K^{-1}e^{-y_{j,K}}(1+o(1)),
\]
uniformly, by \(1-(1+u)^{-K}=Ku+O((Ku)^2)\) for \(u\ge0\) with \(Ku\to0\). Thus for every finite interval \([a,b]\),
\[
\sum_{j\ge1:y_{j,K}\in[a,b]}p_{j,K}\longrightarrow\int_a^b e^{-y}\,dy,
\quad\max_{j:y_{j,K}\in[a,b]}p_{j,K}\longrightarrow0.
\]
The same holds on the negative side. Since the indicators are independent, for disjoint compactly supported nonnegative test functions, their joint Laplace functional converges to the product of Poisson Laplace functionals. This proves the marked vague convergence.

**3. Control all sites beyond a moving edge.** Fix \(t\in\mathbb R\). For the positive-side sites with \(E_{j,K}>T_K+t\), the upper bound \(p_{j,K}\le Ke^{-E_{j,K}}\) yields the Gaussian-tail comparison
\[
\sum_{j:E_{j,K}>T_K+t}Ke^{-E_{j,K}}
\le Ke^{-(T_K+t)}
+\frac K{h_K}\int_{\sqrt{(T_K+t)/K}}^\infty e^{-Kx^2}\,dx
\le\frac{e^{-t}}{A_K}+e^{-t}\sqrt{\frac{\log K}{T_K+t}}.
\]
(In the first inequality a boundary cell is accounted for explicitly.) The complementary lower bound follows by counting a finite energy interval \((t,M]\) and then letting \(M\to\infty\). Consequently
\[
\sum_{j\ge1:y_{j,K}>t}p_{j,K}\to e^{-t},
\quad\max_{j:y_{j,K}>t}p_{j,K}\le e^{-t}/A_K\to0.
\]
For both signs the total expected exceedance count tends to \(2e^{-t}\); the sum of squared probabilities vanishes. Hence
\[
\Pr\bigl(\text{no detected nonzero site with }y_{j,K}>t\bigr)
=\prod_{j\ne0:y_{j,K}>t}(1-p_{j,K})
\to\exp(-2e^{-t}).
\]
Since \(T_K+t>0\) eventually, the event on the left is exactly \(\{KR_K^2-T_K\le t\}\), including the possible all-zero-count case. This proves the distributional limit.

**4. Consequences.** Tightness of the centered maximum and \(T_K/\log K\to1\) give \(R_K/\sqrt{\log K/K}\to1\) in probability. At \(j=1\), \(K h_K^2=1/(4A_K^2\log K)\to0\), whence \(p_{1,K}\to1\): with probability tending to one the nonzero nearest neighbor is incorrectly declared a zero. Thus global exact classification fails even though \(\Pr(I_{0,K}=1)=1-2^{-K}\to1\) and each *fixed nonzero spatial location* is correctly excluded in the fixed-candidate regime. The explicit spacing choice follows by substituting \(A_K=(\log K)^{3/2}/2\).

## Verification

The included `verify_edge.py` checks the finite-\(K\) Gamma-Poisson marginal identity and directly evaluates truncated exact products for the outermost detected point, with Gaussian-tail truncation far beyond the edge. It passes 72 deterministic assertions. Numerical convergence is slow, as expected for the logarithmic boundary; no finite computation is used to establish the infinite-array limit. The proof establishes the analytic limit with its own mesh and tail arguments.

## Relationship to prior work

Micheas (arXiv:2611.16011v1, first posted 2026-11-11) introduces the gamma-driven Cox zero detector, its exact one-site detection formula, and fixed-finite-candidate consistency (Lemma 8, Theorem 9). Its discussion notes a need to treat continuous domains, but does not formulate the growing-lattice Poisson edge, its sharp \(\log A_K\) shift, or the Gumbel radius distribution. General rare-event point-process limit results, such as Hüsler–Schmidt (2016) and de Monte–Papastathopoulos (2026), provide background tools but do not state the model-specific energy centering or its grid-resolution consequence. The proof above verifies the limiting intensity directly rather than assuming a generic theorem supplies the application.

## Limitations

The theorem uses one simple root and a linearly varying deterministic test function, independent gamma masses, and a lattice shrinking fast enough that \(A_K\to\infty\) but with \(\log A_K=o(\log K)\). It does not address other root multiplicities, off-grid roots, imperfect evaluations, fully continuous candidate sets, or arbitrary dependence. The Poisson convergence is in the standard vague topology; mass diverges toward energy \(-\infty\), so global finite-point-process convergence on the whole real energy axis is not claimed. Historical priority beyond the inspected sources remains uncertain; independent verification has not been performed.

## References

1. A. C. Micheas, *Zero detection via Cox random measures*, arXiv:2611.16011v1 (2026-11-11), https://arxiv.org/abs/2611.16011.
2. J. Hüsler and M. Schmidt, *A note on the point processes of rare events*, Journal of Applied Probability (2016), https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/note-on-the-point-processes-of-rare-events/71026A8318DFBF6AC19D692E9AF3E5E1.
3. L. de Monte and I. Papastathopoulos, *A directional Poisson point process for univariate extremes*, Statistics and Probability Letters 235 (2026), 110722, https://doi.org/10.1016/j.spl.2026.110722.
