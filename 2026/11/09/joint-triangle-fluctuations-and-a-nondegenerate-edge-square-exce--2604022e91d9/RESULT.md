# Joint triangle fluctuations and a nondegenerate edge-square excess in finite-memory Pólya threshold graphs

## Finding

Consider a simple threshold graph grown from a binary Pólya creation sequence, with a universal vertex attached to every preceding vertex when its bit is one and an isolated vertex when its bit is zero. For fixed finite memory, the edge and triangle densities have a joint Gaussian limit with an explicit covariance matrix, and their difference from the deterministic graphon relation has its own strictly positive Gaussian fluctuation.

For each integer \(n\ge3\), write \(E_n\) for the number of *non-loop* edges and \(T_n\) for the number of unordered triples spanning a triangle, and define
\[
e_n=\frac{E_n}{\binom n2},\qquad t_n=\frac{T_n}{\binom n3}.
\]
Set
\[
D_M=1+2M\delta+\frac{M(M-1)\delta^2}{1+\delta},
\qquad v=\rho(1-\rho)D_M.
\]
Then, almost surely, \(e_n\to\rho\) and \(t_n\to\rho^2\), and
\[
\sqrt n\begin{pmatrix}e_n-\rho\\ t_n-\rho^2\end{pmatrix}
\Longrightarrow\mathcal N_2\!\left(0,\,
v\begin{pmatrix}\frac43&\frac52\rho\\\frac52\rho&\frac{24}{5}\rho^2\end{pmatrix}\right).
\]
The covariance matrix is positive definite, with determinant \(3v^2\rho^2/20\). Consequently the centered triangle–edge-square excess satisfies the nondegenerate law
\[
\boxed{\sqrt n\,(t_n-e_n^2)\Longrightarrow
\mathcal N\!\left(0,\,\frac{2}{15}\rho^3(1-\rho)D_M\right).}
\]
In particular, the triangle fluctuations cannot be obtained just by squaring the edge-density fluctuation: a nonzero extra Gaussian component survives. The factor \(D_M\) gives the exact dependence on memory and reinforcement.

## Assumptions and scope

Fix an integer \(M\ge1\), a baseline \(0<\rho<1\), and a reinforcement ratio \(\delta>0\), all constant as \(n\to\infty\). Let \((X_j)_{j\ge1}\) be binary draws. The first \(M\) draws follow an ordinary two-color Pólya urn with initial red fraction \(\rho\) and reinforcement ratio \(\delta\). For \(j>M\), the finite-memory rule is
\[
\Pr(X_j=1\mid X_1,\ldots,X_{j-1})
=\frac{\rho+\delta\sum_{h=1}^M X_{j-h}}{1+M\delta}.
\]
The graph has labeled vertices \(1,\ldots,n\), with an ordinary edge \(\{i,j\}\) for \(i<j\) precisely when \(X_j=1\). Self-loops present in some descriptions of the generating adjacency matrix are *excluded* from \(E_n,T_n\). We use the unconditioned creation process; the final bit is not forced to one.

## Proof

**1. Exact motif identities.** By the universal/isolated rule,
\[
E_m=\sum_{j=1}^m(j-1)X_j,\qquad
T_m=\sum_{1\le j<k\le m}(j-1)X_jX_k
=\sum_{k=1}^m X_k E_{k-1}.
\]
Put \(Y_j=X_j-\rho\), \(S_m=\sum_{j=1}^mY_j\) and \(S_0=0\). Expansion gives the *exact* formula
\[
T_m=\rho^2\binom m3
+\rho\sum_{j=1}^m\left[(j-1)(m-j)+\frac{(j-1)(j-2)}2\right]Y_j
+R_m,
\]
where \(R_m=\sum_{j<k}(j-1)Y_jY_k\). With \(A_m=\sum_{j<m}(j-1)Y_j\), summation by parts yields
\[
R_m=S_mA_m-\frac12\left[(m-2)S_{m-1}^2-\sum_{j=1}^{m-2}S_j^2
+\sum_{j=1}^{m-1}(j-1)Y_j^2\right].
\]
Thus \(\max_{m\le n}|R_m|=O_{\Pr}(n^2)\) whenever \(\max_{m\le n}|S_m|=O_{\Pr}(\sqrt n)\); also \(R_n=o(n^3)\) almost surely if \(S_n=o(n)\) almost surely.

**2. Stationary finite-memory invariance and innovation variance.** The moving length-\(M\) bit word is a finite-state irreducible aperiodic Markov chain. Its invariant law is the exchangeable length-\(M\) Pólya sample law: consistency and exchangeability of the ordinary Pólya process show that shifting one position and appending a new draw leaves this law unchanged. The initialization above already has that invariant law. Accordingly,
\[
\mathbb EY_j=0,\quad \mathbb EY_j^2=\rho(1-\rho),\quad
\operatorname{Cov}(Y_i,Y_j)=\frac{\rho(1-\rho)\delta}{1+\delta}
\quad(0<|i-j|<M).
\]
With \(\alpha=\delta/(1+M\delta)\), define the bounded martingale differences
\[
\varepsilon_j=Y_j-\alpha\sum_{h=1}^M Y_{j-h},\qquad j>M.
\]
Because the conditional mean is \(\alpha\sum_{h=1}^M Y_{j-h}\), orthogonality gives the stationary innovation variance
\[
q=\rho(1-\rho)\left[1-\alpha^2\left(M+\frac{M(M-1)\delta}{1+\delta}\right)\right],
\]
and direct algebra gives \((1+M\delta)^2q=v\). Summing the recurrence, the boundary error is bounded by a constant depending only on \(M,\rho,\delta\):
\[
S_n=(1+M\delta)\sum_{j=M+1}^n\varepsilon_j+O(1).
\]
The ergodic theorem for the predictable innovation variances and the bounded-increment martingale functional central limit theorem imply
\[
\left(n^{-1/2}S_{\lfloor ns\rfloor}\right)_{0\le s\le1}
\Longrightarrow\left(\sqrt v\,W(s)\right)_{0\le s\le1}
\]
in the Skorokhod space, where \(W\) is standard Brownian motion. Its tightness implies \(\max_{m\le n}|S_m|=O_{\Pr}(\sqrt n)\). The ergodic theorem also implies \(S_n=o(n)\) almost surely.

**3. Transfer to motifs.** Weighted summation by parts and step-function Riemann approximation transfer the preceding functional limit and the remainder bound into
\[
\left(\frac{E_{\lfloor nt\rfloor}-\rho\binom{\lfloor nt\rfloor}2}{n^{3/2}},
\frac{T_{\lfloor nt\rfloor}-\rho^2\binom{\lfloor nt\rfloor}3}{n^{5/2}}\right)
\Longrightarrow
\sqrt v\left(\int_0^t s\,dW_s,\,
\rho\int_0^t(ts-s^2/2)\,dW_s\right)
\]
in the product Skorokhod space, with a continuous limiting process. In particular, at \(t=1\), multiplying by the asymptotic denominator factors \(2\) and \(6\) respectively gives
\[
\sqrt n(e_n-\rho)\Longrightarrow2\sqrt v\int_0^1s\,dW_s,
\quad
\sqrt n(t_n-\rho^2)\Longrightarrow6\rho\sqrt v\int_0^1(s-s^2/2)\,dW_s
\]
*jointly*. Integrating the three polynomial products yields the displayed covariance matrix. Since \(e_n-\rho=O_{\Pr}(n^{-1/2})\), the quadratic delta-method remainder vanishes:
\[
\sqrt n\,(t_n-e_n^2)
\Longrightarrow\rho\sqrt v\int_0^1(2s-3s^2)\,dW_s.
\]
The exact integral \(\int_0^1(2s-3s^2)^2ds=2/15\) proves the boxed law. Finally, the almost-sure conclusions follow by the ergodic law, the weighted linear identities, and \(R_n=o(n^3)\) almost surely.

## Verification

The standalone standard-library Python file `check_motif.py` exhaustively checks the edge and triangle identities, the quadratic remainder identity, stationary finite-memory word distributions and innovation variances for small memory sizes and rational parameters, plus the Gaussian covariance integrals. It passed **8,615 exact rational assertions**. The standalone `simulate_motif.py` reproduces a seeded simulation with \(M=3\), \(\rho=0.4\), \(\delta=0.7\), \(n=2500\) and 2,300 independent replications; its sample variance was \(0.03473495\), compared with the asymptotic value \(0.03547859\). The simulation is a diagnostic, not the infinite-limit proof; no independence or external certification is claimed.

## Relationship to prior work

Yu, Alajaji and Gharesifard introduce the Pólya threshold graph and its finite-memory variant, and study degree statistics, spectral structure and consensus; their published treatment does not state this finite-memory motif covariance or the edge-square excess fluctuation. Prior finite-memory Pólya-urn work establishes the order-\(M\) draw process, which is used here rather than claimed new. Earlier analysis of finite-memory *edge* fluctuations yields the same innovation multiplier \(D_M\), but the triangle component and the nondegenerate residual are not implied by an edge-only limit.

Konno, Masuda, Roy and Sarkar establish central limit results for triangle counts in static threshold networks built from *independent* vertex weights. Diaconis, Holmes and Janson explain connections among threshold-graph representations. These precedents cover much of the independent-input context and motivate the present comparison, but do not provide the dependent finite-memory joint covariance above. Bhattacharya, Chatterjee and Janson establish general subgraph-count fluctuation results for graphon-sampled graphs with independent vertex sampling, a distinct dependence regime. Standard martingale invariance principles supply the probabilistic machinery and are not asserted as new. Published mathematical-record searches found no statement directly implying the new finite-memory coefficient and joint fluctuation; this is not a proof of priority.

## Limitations

The theorem assumes fixed finite \(M\), fixed positive \(\delta\), and \(0<\rho<1\), with the original unconditioned creation process. It does not treat memory growing with graph size, forced connectedness, local clustering coefficients, or a quantitative central-limit convergence rate. The model is a threshold graph, not the Erdős–Rényi graph. The exact novelty comparison remains subject to independent verification against broader Markov-dependent motif limit theory. Finite enumerations and simulations cannot certify an asymptotic result.

## References

1. J. Yu, F. Alajaji and B. Gharesifard, *Pólya Threshold Graphs*, arXiv:2603.18452 (first posted 2026-03-19), https://arxiv.org/abs/2603.18452.
2. F. Alajaji and T. Fuja, *A Communication Channel Modeled on Contagion*, IEEE Transactions on Information Theory 40 (1994), 2035–2041.
3. N. Konno, N. Masuda, R. Roy and A. Sarkar, *Rigorous results on the threshold network model*, arXiv:math/0505681 (2005), https://arxiv.org/abs/math/0505681.
4. P. Diaconis, S. Holmes and S. Janson, *Threshold graph limits and random threshold graphs*, arXiv:0908.2448 (2009), https://arxiv.org/abs/0908.2448.
5. B. B. Bhattacharya, A. Chatterjee and S. Janson, *Fluctuations of Subgraph Counts in Graphon Based Random Graphs*, arXiv:2104.07259 (2021), https://arxiv.org/abs/2104.07259.
