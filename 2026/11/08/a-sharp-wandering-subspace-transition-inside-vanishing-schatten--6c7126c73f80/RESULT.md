# A sharp wandering-subspace transition inside vanishing Schatten perturbations of a rootless-tree isometry

## Finding
For every real \(p>2\) and every \(\varepsilon>0\), one fixed isometry \(U\) on a separable Hilbert space admits *both* an analytic expansive weighted shift with the wandering-subspace property and an analytic expansive weighted shift without it, each within \(\varepsilon\) of \(U\) in Schatten \(\mathcal S_p\)-norm. These examples belong to an explicit continuous two-parameter family of positive weighted shifts on a rootless quasi-Brownian directed tree. Within the family, the property holds **exactly when** \(0<\beta\leq1\), and the critical value is sharp.

There is a quantitative refinement. For integers \(N\geq2\), the perturbation \(K_{N,\beta}=S_{N,\beta}-U\) is compact and satisfies \(K_{N,\beta}\in\mathcal S_p\) **if and only if** \(p>2\). For each fixed \(\beta>0\) and \(p>2\),
\[
\lim_{N\to\infty}N^{p/2-1}\|K_{N,\beta}\|_{\mathcal S_p}^{p}=\frac4{p-2},
\qquad
\|K_{N,\beta}\|\sim N^{-1/2}.
\]
Thus the two sides of the wandering-subspace transition accumulate at the **same** isometry, even in every Schatten norm above the sharp exponent two.

## Assumptions and scope
Work over the complex Hilbert space \(H=\ell^2(V)\), where
\[
V=\{(j,m):j\in\mathbb N_0,\ m\in\mathbb Z\}.
\]
The children of \((0,m)\) are \((0,m-1)\) and \((1,m)\); the sole child of \((j,m)\), for \(j\geq1\), is \((j+1,m)\). This directed tree is leafless, rootless and of quasi-Brownian valency two. Its reference shift is the isometry
\[
Ue_{0,m}=e_{0,m-1},\qquad Ue_{j,m}=e_{j+1,m}\quad(j\geq1).
\]
Fix an integer \(N\geq2\) and a real \(\beta>0\). Define a positive weighted shift \(S_{N,\beta}\) by
\[
S_{N,\beta}e_{0,m}=\lambda_{0,m-1}e_{0,m-1}+\lambda_{1,m}e_{1,m},\qquad
S_{N,\beta}e_{j,m}=\lambda_{j+1,m}e_{j+1,m}\quad(j\geq1),
\]
where the incoming-child weights are
\[
\lambda_{0,m}=\begin{cases}\sqrt{(N+m)/(N+m+1)},&m\geq0,\\1,&m\leq-1,\end{cases}
\]
\[
\lambda_{1,m}=\begin{cases}(N+m)^{-1/2},&m\geq1,\\(N+1+|m|)^{-1/2},&m\leq0,\end{cases}
\]
and, for \(j\geq2\),
\[
\lambda_{j,m}=\begin{cases}
(1+m/N)^{\beta/[2(m-1)]},&m\geq2\text{ and }2\leq j\leq m,\\
1,&\text{otherwise}.
\end{cases}
\]
Here the wandering-subspace property means \(H=\overline{\operatorname{span}}\{S_{N,\beta}^{k}h:k\geq0,\ h\in\ker S_{N,\beta}^{*}\}\). Analyticity means \(\bigcap_{k\geq0}S_{N,\beta}^kH=\{0\}\). A Wold-type decomposition is understood in the standard left-invertible sense; for analytic operators it is equivalent to the wandering-subspace property. The Schatten statement applies to finite exponents \(p>0\), including quasi-normed classes below one.

## Proof
**1. Boundedness and expansivity.** Distinct parent columns of a weighted shift on a directed tree have disjoint supports. For spine parents \((0,m)\) with \(m\geq1\), the outgoing squared weights sum to \((N+m-1)/(N+m)+1/(N+m)=1\). For \(m\leq0\), the sum is \(1+(N+1+|m|)^{-1}\geq1\). Every unary tooth-parent column has norm \(\lambda_{j+1,m}\geq1\). The unary weights are uniformly bounded (indeed their largest value occurs at \(m=2\)), hence \(S_{N,\beta}\) is bounded and satisfies \(S_{N,\beta}^{*}S_{N,\beta}\geq I\).

**2. The two exact analytic-series tests.** Apply the rootless-tree criterion of Chavan and Trivedi, Theorem 1.3 and its analyticity criterion, to \(v=(0,0)\). Its ancestor at depth \(m\geq1\) is \((0,m)\). At that level a new tooth descendant \((m,m)\) joins the spine descendant \((0,0)\). The product of edge weights along the spine path is
\[
a_m=\sqrt{N/(N+m)}.
\]
For the new tooth path the product is \(b_m=\sqrt{g_m/(N+m)}\), where \(g_1=1\) and \(g_m=(1+m/N)^\beta\) for \(m\geq2\). Consequently the newly appearing squared relative path ratio is exactly \(g_m/N\), and the analyticity series of the source theorem is
\[
\alpha_{S_{N,\beta}}((0,0))=1+\frac1N\sum_{m\geq1}g_m=\infty.
\]
Thus \(S_{N,\beta}\) is analytic, for every positive \(\beta\).

The Cauchy dual is \(S_{N,\beta}'=S_{N,\beta}(S_{N,\beta}^{*}S_{N,\beta})^{-1}\). Every spine parent at a strictly positive level has column norm one; the entire spine path and the first tooth edge are unchanged in the dual. Each unary tooth edge is replaced by its reciprocal (because a one-child parent has squared column norm equal to that edge weight squared). The dual tooth-path product is therefore \(b'_m=1/\sqrt{(N+m)g_m}\), while its spine-path product is still \(a_m\). The dual series is
\[
\alpha_{S_{N,\beta}'}((0,0))=1+\frac1N\sum_{m\geq1}\frac1{g_m}.
\]
By comparison with \(\sum_{m\geq1}m^{-\beta}\), it diverges precisely when \(\beta\leq1\). The cited rootless-tree characterization gives the Wold-type decomposition, and hence wandering-subspace generation, precisely for \(0<\beta\leq1\). For \(\beta>1\), the first series diverges but the dual series converges, so the operator remains analytic and loses that generation property. These conclusions are infinite-dimensional and are not based on truncation.

**3. Exact singular-value formula for the perturbation.** Since the vectors \((S_{N,\beta}-U)e_v\) have disjoint supports for distinct parents \(v\), the positive operator \(K_{N,\beta}^{*}K_{N,\beta}\) is diagonal. The squared norms of its nonzero columns are: on spine parents \(m\geq1\), \(2(1-\sqrt{(N+m-1)/(N+m)})\); on spine parents \(m\leq0\), \((N+1+|m|)^{-1}\); and, at each \(m\geq2\), exactly \(m-1\) unary-parent columns have norm
\[
d_{m,N,\beta}=(1+m/N)^{\beta/[2(m-1)]}-1.
\]
Thus the complete (unordered) nonzero singular-value multiset is those column norms, with their stated multiplicities. In particular, for every \(p>0\),
\[
\begin{aligned}
\|K_{N,\beta}\|_{\mathcal S_p}^{p}={}&
\sum_{m=1}^{\infty}\left[2\left(1-\sqrt{\frac{N+m-1}{N+m}}\right)\right]^{p/2}\\
&+\sum_{k=0}^{\infty}(N+1+k)^{-p/2}\\
&+\sum_{m=2}^{\infty}(m-1)\left[(1+m/N)^{\beta/[2(m-1)]}-1\right]^p.
\end{aligned}
\]
The first two series each converge exactly for \(p>2\). The third converges exactly for \(p>2\), since its summand is asymptotic, for fixed \(N,\beta\), to a positive multiple of \(m^{1-p}(\log m)^p\). The column norms tend to zero away from a finite set, hence \(K_{N,\beta}\) is compact. The first term is maximal at \(m=1\), and the unary term decreases with \(m\geq2\) because \(m\mapsto\log(1+m/N)/(m-1)\) decreases. The largest nonpositive-spine column is smaller than the first positive-spine column. Therefore
\[
\|K_{N,\beta}\|=\max\left\{\sqrt{2\left(1-\sqrt{\frac N{N+1}}\right)},\ (1+2/N)^{\beta/2}-1\right\}.
\]
In particular, \(\|K_{N,\beta}\|\sim N^{-1/2}\) for fixed \(\beta\).

**4. Sharp Schatten asymptotics.** Fix \(p>2\) and \(\beta>0\). Both spine series are asymptotic to \(N^{1-p/2}/(p/2-1)\), by comparison with the corresponding Riemann integral. For the tooth term, use
\[
0\leq d_{m,N,\beta}\leq C_\beta\frac{\log(1+m/N)}{m-1},
\]
valid uniformly in \(N\geq2,m\geq2\), and split at \(m=N\). The range \(2\leq m\leq N\) is \(O(N^{2-p})\), by \(\log(1+m/N)\leq m/N\). The range \(m>N\) is also \(O(N^{2-p})\), by comparison with the integrable function \(t^{1-p}\log(1+t)^p\) on \([1,\infty)\). Since \(2-p<1-p/2\), the tooth term is lower order. Hence
\[
\|K_{N,\beta}\|_{\mathcal S_p}^{p}\sim\frac4{p-2}N^{1-p/2}.
\]
For any prescribed \(p>2\) and \(\varepsilon>0\), choose \(N\) sufficiently large for \(\beta=1/2\) and \(\beta=2\) simultaneously. Both perturbations then have Schatten \(p\)-norm less than \(\varepsilon\), while their Wold behaviors differ. The dependence on \(\beta\) is continuous in Schatten \(\mathcal S_p\) at each fixed \(N\), by dominated convergence on compact intervals of positive \(\beta\).

## Verification
A standalone standard-library Python script, `checker.py`, evaluates the edge weights, the Cauchy-dual weights, the two independent path-ratio identities, expansive column norms, the exact perturbation operator-norm formula, and truncated singular-value sums. Executing `python3 checker.py` produced 17,129 successful finite checks. These are diagnostics only: the full series convergence, Wold criterion, threshold, and limiting constant are proved above.

## Relationship to prior work
Chavan and Trivedi (arXiv:2501.01296) prove the rootless-tree Wold criterion used in Step 2 and construct analytic expansive non-Wold shifts. Their criterion and their existence construction are not claimed as new. Kujur (arXiv:2609.14662) studies higher-order concavity and explicit non-Wold quasi-Brownian shifts, including strict \(4\)-isometries, but does not identify the simultaneous arbitrarily small Schatten perturbation, sharp exponent, and parameter-switching phenomenon here. Bala and Golla (arXiv:2607.15222) give general spectral criteria for Schatten perturbations of partial isometries; those criteria concern membership in perturbation ideals, not the loss or recovery of wandering-subspace generation in this specific class. The present theorem adds the explicit compact/Schatten-local instability and its sharp quantitative law.

## Limitations
The model uses a particular rootless quasi-Brownian tree, positive weights, and the explicit parameters above. It does not assert instability near every isometry, nor a universal perturbation threshold for all rooted/rootless trees. The stated Schatten convergence requires \(p>2\); for \(p\leq2\) the displayed perturbations are not in \(\mathcal S_p\). The argument uses an established infinite-dimensional Wold criterion rather than proving that criterion again. Publication-priority risk remains from possibly broader perturbation results phrased without this construction, despite comparison to directly related papers.

## References
- Sameer Chavan and Shailesh Trivedi, *Wold-type decomposition for left-invertible weighted shifts on a rootless directed tree*, arXiv:2501.01296 (first public version 2025-01-02), Theorem 1.3 and §5; *Studia Mathematica* 287 (2026), 205–226, DOI 10.4064/sm250201-5-12.
- Ashish Kujur, *Wold-type decompositions for norm-increasing \(m\)-concave weighted shifts on directed trees*, arXiv:2609.14662 (2026), §§1, 5–6.
- Neeru Bala and Ramesh Golla, *Spectral Characterizations of Compact and Schatten-Class Perturbations of Partial Isometries*, arXiv:2607.15222 (2026), §§1–3.
- A. Anand, S. Chavan and S. Trivedi, *Analytic \(m\)-isometries without the wandering subspace property*, arXiv:1811.12080, Example 3.1 (earlier non-Wold constructions on one-circuit graphs).
