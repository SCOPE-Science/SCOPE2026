# A logarithmic uniqueness threshold for sparse random networked public-goods games

## Finding

For fixed \(p_0>0\) and \(q>0\), every integer \(n\ge\max\{2,p_0\}\), and model parameters \(b,c_0>0\), let \(B\in\{0,1\}^{n\times n}\) have \(B_{ii}=1\) and independent \(B_{ij}\sim\mathrm{Bernoulli}(p_0/n)\) for \(i\ne j\). Define \(S_{ij}=\sum_{k\ne i}B_{ki}B_{kj}\), \(K_R=\exp\!\big(p_0[\exp(2+p_0(e-1))-1]\big)\), \(K_C=\exp\!\big(p_0(e-1)+p_0[\exp(1+p_0(e-1))-1]\big)\), and \(u_n=(q+1)\log n+\log(K_R+K_C)\). In the homogeneous quadratic-benefit, quadratic-cost networked public-goods model of Cheng, Deng, and Ma, if \(c_0/(2b)>u_n\), then the Nash equilibrium is unique with probability at least \(1-n^{-q}\).

The threshold is logarithmic in the number of players for fixed \(p_0\) and \(q\). The constants above are explicit and conservative; the statement is a sufficient condition, not a sharp threshold.

## Assumptions and scope

Let \(n\ge\max\{2,p_0\}\), so \(p=p_0/n\in(0,1]\). The interaction matrix is \(W=B\): its off-diagonal entries are independent Bernoulli variables with parameter \(p\), and every diagonal entry equals one. The curvature parameters satisfy \(b,c_0>0\). The matrix \(S\) is the nonnegative overlap matrix appearing in the near-potential uniqueness criterion for the homogeneous model in [1, Theorem 3.6]. In the quadratic case of [1, Section 4.2], the benefit derivative is \(2b\)-Lipschitz and the cost has strong-convexity constant \(c_0\), so the criterion is satisfied whenever \(c_0/(2b)>\|S\|_2\). Here \(\|\cdot\|_2\) is the induced Euclidean operator norm.

## Proof

Write \(D_k=\sum_{\ell\ne k}B_{k\ell}\). For a fixed row index \(i\), define \(Z_{ki}=\sum_{\ell\notin\{k,i\}}B_{k\ell}\) for \(k\ne i\). Then \(Z_{ki}\sim\mathrm{Bin}(n-2,p)\), it is independent of \(B_{ki}\), and the variables indexed by different \(k\) use different rows. The row sum \(R_i=\sum_jS_{ij}\) therefore satisfies
\[
R_i=\sum_{k\ne i}B_{ki}(2+Z_{ki}),
\qquad
\mathbb{E}e^{R_i}=
\big[1-p+pe^2(1-p+pe)^{n-2}\big]^{n-1}.
\]
Since \((1-p+pe)^{n-2}\le \exp(p_0(e-1))\), and \(1+x\le e^x\), this gives \(\mathbb{E}e^{R_i}\le K_R\).

For a fixed column index \(j\), write \(Z_{kj}=\sum_{\ell\notin\{k,j\}}B_{k\ell}\) for each \(k\ne j\), and the column sum is
\[
C_j=\sum_iS_{ij}=D_j+\sum_{k\ne j}B_{kj}(1+Z_{kj}),
\]
where \(D_j\sim\mathrm{Bin}(n-1,p)\), and the terms from rows \(k\ne j\) are independent of one another and of \(D_j\). Hence
\[
\mathbb{E}e^{C_j}=
(1-p+pe)^{n-1}
\big[1-p+pe(1-p+pe)^{n-2}\big]^{n-1}
\le K_C.
\]
Markov's inequality and a union bound now yield, for every \(u\ge0\),
\[
\Pr\!\left(\max_iR_i>u\ \text{or}\ \max_jC_j>u\right)
\le n(K_R+K_C)e^{-u}.
\]
Set \(u=u_n=(q+1)\log n+\log(K_R+K_C)\). The right-hand side is \(n^{-q}\). On the complementary event, both the maximum row sum and maximum column sum of \(S\) are at most \(u_n\). The standard induced-norm inequality gives
\[
\|S\|_2\le\sqrt{\|S\|_1\|S\|_\infty}\le u_n.
\]
Thus, if \(c_0/(2b)>u_n\), the uniqueness criterion of [1, Theorem 3.6] applies on this event, proving the claim.

## Verification

The row and column moment-generating functions above follow directly from independent Bernoulli entries; no independence between different row sums or column sums is required for the union bound. The operator-norm step uses both row and column sums, so it does not assume that \(S\) is symmetric. For fixed \(p_0\) and \(q\), \(u_n=(q+1)\log n+O_{p_0}(1)\). The primary paper states an \(O(\sqrt n)\) threshold with probability at least \(1/2\) in [1, Theorem 4.3]; the logarithmic bound here is independently established by controlling both induced norms. No numerical experiment is used as a proof.

## Relationship to prior work

Cheng, Deng, and Ma state a random-network threshold of order \(\sqrt n\) and explicitly identify polylogarithmic dependence as a direction for further study [1, Section 4.2.1]. The present result independently derives a logarithmic sufficient condition for the same sparse directed Bernoulli model by controlling both row and column sums of the overlap matrix; it does not assume symmetry or rely on a one-sided row-sum bound for the operator norm. Naghizadeh and Liu give a necessary-and-sufficient P-matrix condition for uniqueness in a different network public-goods model with linear costs and unbounded efforts [2, Theorem 1]; that result does not supply this random, convex-cost threshold. Lugosi, Mendelson, and Zhivotovskiy study spectral-norm concentration for the symmetric adjacency matrix of an undirected Erdős–Rényi graph, primarily in regimes with edge probability at least of order \(\log n/n\) [3]; their matrix and probability regime differ from the overlap matrix here.

## Limitations

The constants \(K_R\) and \(K_C\) are not optimized, and the sufficient threshold is not asserted to be necessary or sharp. The result fixes \(p_0\) and \(q\) as \(n\) varies; it does not cover arbitrary degree distributions, dependent edges, heterogeneous benefits or costs, or all directed network models. The conclusion is uniqueness with high probability under the stated curvature condition, not a claim about convergence of every learning dynamic.

## References

[1] Y. Cheng, X. Deng, and Y. Ma, “Networked Digital Public Goods Games with Heterogeneous Players and Convex Costs,” arXiv:2502.01001 (first public version 2025-02-03), *Proceedings of the ACM Web Conference 2025*, pp. 1416–1424. https://arxiv.org/abs/2502.01001 ; https://doi.org/10.1145/3696410.3714869

[2] P. Naghizadeh and M. Liu, “Provision of Public Goods on Networks: On Existence, Uniqueness, and Centralities,” arXiv:1604.08910 (2016). https://arxiv.org/abs/1604.08910

[3] G. Lugosi, S. Mendelson, and N. Zhivotovskiy, “Concentration of the spectral norm of Erdős–Rényi random graphs,” *Bernoulli* 26(3) (2020), 2253–2274. https://arxiv.org/abs/1801.02157 ; https://doi.org/10.3150/19-BEJ1192
