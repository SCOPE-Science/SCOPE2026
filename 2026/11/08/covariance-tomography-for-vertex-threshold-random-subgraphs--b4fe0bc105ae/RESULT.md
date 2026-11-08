# Covariance tomography for vertex-threshold random subgraphs

## Finding

Let \(G\) be any finite simple graph on the labelled vertex set \(\{1,\ldots,n\}\), where \(n\ge 2\). Independently assign uniform \([0,1]\) variables \(U_v\) to its vertices. For a fixed known threshold \(0<\tau<2\), retain an edge \(uv\) exactly when \(U_u+U_v\ge\tau\), and observe only the resulting degree vector \(Y\). Write \(Q=D_G+A_G\) for the signless Laplacian of the unobserved host graph, and set
\[
 r=\min\{\tau,2-\tau\},\qquad
 a_\tau=\frac{r^2(3r^2-8r+6)}{12},\qquad
 c_\tau=\frac{r^3(4-3r)}{12}.
\]
Then the degree covariance matrix satisfies the **exact spectral identity**
\[
 \boxed{\ \Sigma_\tau:=\operatorname{Cov}(Y)=a_\tau Q+c_\tau Q^2.\ }
\]
Both coefficients are strictly positive for every \(0<\tau<2\). Consequently the full labelled host graph is uniquely determined from the degree covariance alone, by the principal positive-semidefinite square root:
\[
 \boxed{\ Q=\frac{(a_\tau^2 I+4c_\tau\Sigma_\tau)^{1/2}-a_\tau I}{2c_\tau}.\ }
\]
In particular, at the irregular-subgraph threshold \(\tau=1\), \(\Sigma_1=(Q+Q^2)/12\). The dimension of the covariance nullspace is exactly the number of bipartite connected components of \(G\), counting isolated vertices as bipartite components. At the degenerate thresholds \(\tau\le0\) and \(\tau\ge2\), the degree covariance is zero for every host, so covariance-only recovery is not universally possible.

There is also an explicit finite-sample guarantee. Let \(\Delta\ge1\) be a known upper bound on the host's maximum degree (\(\Delta=n-1\) is always permitted). From \(m\) independent copies of the labelled degree vector, construct the empirical covariance \(\widehat\Sigma\), apply the same matrix-square-root formula to obtain \(\widehat Q\), and declare \(uv\) an edge exactly when \(\widehat Q_{uv}>1/2\), for \(u\ne v\). For any \(0<\delta<1\), this recovers every edge simultaneously with probability at least \(1-\delta\) whenever
\[
 \boxed{\ m>\frac{18n^2\Delta^4}{a_\tau^2}\log\frac{4n^2}{\delta}.\ }
\]
This is a valid sufficient sample bound, not a claim of optimal sample complexity.

## Assumptions and scope

The host is an arbitrary labelled, finite, undirected simple graph; it need not be connected or regular. Each experiment resamples all independent uniform vertex variables, and the identities of the vertices are retained between experiments. Only degrees in the sampled graph are used for reconstruction, not its sampled edge set or its latent vertex variables. The threshold is fixed and known. The finite-sample statement assumes independent experiments and a known degree upper bound. Empty hosts are covered by the population identity; the stated finite-sample bound uses \(\Delta\ge1\) and also covers them.

## Proof

**1. Edge-pair moments.** For \(e=uv\), write \(Z_e={\bf1}\{U_u+U_v\ge\tau\}\). Let \(p_\tau=\mathbb E Z_e\), \(v_\tau=p_\tau(1-p_\tau)\), and \(g_\tau(x)=\mathbb P(U+x\ge\tau)\), where \(U\) is an independent uniform variable. For \(0<\tau\le1\), the function \(g_\tau(x)\) equals \(1-\tau+x\) on \([0,\tau]\) and \(1\) on \([\tau,1]\). Direct integration gives
\[
 p_\tau=1-\frac{\tau^2}{2},\qquad
 \mathbb E[g_\tau(U)^2]=1-\tau+\tau(1-\tau)^2+\tau^2(1-\tau)+\frac{\tau^3}{3}.
\]
For \(1\le\tau<2\), \(g_\tau(x)=0\) up to \(\tau-1\), then \(g_\tau(x)=x+1-\tau\); hence \(p_\tau=(2-\tau)^2/2\) and \(\mathbb E[g_\tau(U)^2]=(2-\tau)^3/3\). In either range,
\[
 c_\tau:=\operatorname{Var}(g_\tau(U))=\frac{r^3(4-3r)}{12},
 \quad v_\tau-2c_\tau=\frac{r^2(3r^2-8r+6)}{12}=a_\tau.
\]
Two distinct edges with no common vertex have independent indicators. Two distinct edges sharing exactly one endpoint are independent conditional on that endpoint's uniform label, so their unconditional covariance is exactly \(c_\tau\). A single indicator has variance \(v_\tau\). These observations exhaust all pairs because the host is simple.

**2. Matrix identity.** Let \(B\) be the unsigned vertex-edge incidence matrix of the host: each column has a one at each of its two endpoints. The sampled degree vector is \(Y=BZ\), and \(Q=BB^\mathsf T\). The previous paragraph gives the edge-indicator covariance matrix
\[
 \operatorname{Cov}(Z)=(v_\tau-2c_\tau)I+c_\tau B^\mathsf TB=a_\tau I+c_\tau B^\mathsf TB,
\]
because \(B^\mathsf TB\) has diagonal entries two and off-diagonal entries one precisely for edges sharing an endpoint. Therefore
\[
 \operatorname{Cov}(Y)=B\operatorname{Cov}(Z)B^\mathsf T
 =a_\tau BB^\mathsf T+c_\tau (BB^\mathsf T)^2=a_\tau Q+c_\tau Q^2.
\]

**3. Identifiability and nullspace.** Since \(0<r\le1\), we have \(c_\tau>0\) and
\[
 3r^2-8r+6=3(r-4/3)^2+2/3>0,
\]
so \(a_\tau>0\). The matrix \(Q=BB^\mathsf T\) is positive semidefinite, and \(x\mapsto a_\tau x+c_\tau x^2\) is strictly increasing on \([0,\infty)\). Applying its inverse by spectral calculus yields the stated principal-square-root formula. The off-diagonal entries of \(Q\) are exactly the binary adjacency indicators, proving recovery, including isolated vertices. Moreover \(\ker\Sigma_\tau=\ker Q=\ker B^\mathsf T\). The latter consists of vertex vectors satisfying \(z_u+z_v=0\) on every edge: on a bipartite connected component there is one degree of freedom, and an odd cycle forces this freedom to vanish. This proves the nullity assertion. Outside \((0,2)\), all sampled edges are deterministically present or deterministically absent, making every degree vector deterministic and its covariance zero.

**4. Stability and a finite-sample decoder.** Let \(\widehat\Sigma\) be the sample covariance with divisor \(m\), namely \(m^{-1}\sum_{j=1}^m Y^{(j)}Y^{(j)\mathsf T}-\bar Y\bar Y^\mathsf T\). It is positive semidefinite. Whenever \(S,T\) are positive semidefinite, the standard integral solution of the Sylvester equation for positive square roots shows
\[
 \|(a_\tau^2I+4c_\tau S)^{1/2}-(a_\tau^2I+4c_\tau T)^{1/2}\|_2
 \le \frac{2c_\tau}{a_\tau}\|S-T\|_2.
\]
After division by \(2c_\tau\), the inverse reconstruction map is consequently \(1/a_\tau\)-Lipschitz in operator norm.

Put \(h=\sqrt{\log(4n^2/\delta)/(2m)}\). Each observed degree lies in \([0,\Delta]\). Applying Hoeffding's inequality to all \(n^2\) raw second-moment entries and all \(n\) first-moment entries and taking a union bound, with probability at least \(1-\delta\) we have simultaneously
\[
 |\widehat{\mathbb E}(Y_uY_v)-\mathbb E(Y_uY_v)|\le\Delta^2 h,
 \qquad |\bar Y_u-\mathbb E Y_u|\le\Delta h.
\]
The product-of-means error is at most \(2\Delta^2h\), hence every entry of \(\widehat\Sigma-\Sigma_\tau\) has absolute value at most \(3\Delta^2h\), and
\[
 \|\widehat\Sigma-\Sigma_\tau\|_2\le 3n\Delta^2h.
\]
The prescribed strict sample bound makes this less than \(a_\tau/2\), so \(\|\widehat Q-Q\|_2<1/2\). Each off-diagonal \(Q_{uv}\) is zero or one, thus thresholding \(\widehat Q_{uv}\) at \(1/2\) recovers the entire host adjacency matrix on the same high-probability event. This completes the proof.

## Verification

The accompanying `verify.py` uses standard-library exact rational arithmetic to independently assemble covariance from edge pairs and compare it with the polynomial formula for **every labelled graph on at most five vertices**, across nine rational thresholds in \((0,2)\). It also checks nullity against the number of bipartite components, computes analytic one- and two-edge moments by piecewise integration, and runs principal-matrix-square-root numerical reconstructions for selected graphs plus seeded direct vertex-label simulations. Run `python3 verify.py` from the directory containing the file. Its recorded result is `VERIFY_OK 11215 exact and numerical assertions`. These finite checks do not replace the all-graph derivation, the spectral argument, or the finite-sample probability bound.

## Relationship to prior work

The vertex-sum edge-selection mechanism is the irregular random-subgraph construction studied by Frieze, Gould, Karoński and Pfender and subsequently by Alon and Wei and by Fox, Luo and Pham. The latter two works analyze degree multiplicities and concentration for regular hosts, and the existing uniform marginal degree law at threshold one is not new. The present finding concerns a different observable and inverse question: the **entire covariance matrix of the labelled sampled degree vector**, its exact signless-Laplacian transformation for all interior thresholds, and reconstruction of the unknown host from degree-only repeated observations. McGregor and Sengupta investigate reconstruction from randomly vertex-deleted adjacency submatrices, rather than the degree-only threshold channel here. The standard linear-algebraic signless-Laplacian nullity theorem and the underlying probabilistic concentration inequality are used, not claimed as new. Existing results for independent bond percolation also allow recovery from degree covariance in that different sampling model; the distinctive claim here is the quadratic transform and its inverse in the dependent vertex-threshold model.

## Limitations

The result assumes known threshold and aligned vertex identities across independent observations; it does not recover anonymous unlabelled hosts from unordered degree multisets. The explicit sample bound is conservative and need not be minimax optimal. It degrades near the deterministic endpoint thresholds, where covariance identifiability fails. No claim is made that the individual covariance ingredients, matrix-square-root inequalities, or the signless-Laplacian kernel characterization were previously unknown. The literature comparison cannot rule out a prior equivalent covariance-transform calculation outside the sources inspected. Independent verification of the claimed historical priority has not been performed.

## References

1. J. Fox, S. Luo and H. T. Pham, *On random irregular subgraphs*, arXiv:2207.13651, first publicly posted 2022-07-27; later published in *Random Structures & Algorithms* 64 (2024), 899–917. https://arxiv.org/abs/2207.13651
2. N. Alon and F. Wei, *Irregular subgraphs*, arXiv:2108.02685 (2021). https://arxiv.org/abs/2108.02685
3. A. Frieze, R. J. Gould, M. Karoński and F. Pfender, *On graph irregularity strength*, *Journal of Graph Theory* 41 (2002), 120–137. https://doi.org/10.1002/jgt.10056
4. A. McGregor and R. Sengupta, *Graph Reconstruction from Random Subgraphs*, ICALP 2022, Article 96. https://doi.org/10.4230/LIPIcs.ICALP.2022.96
5. D. Cvetković, P. Rowlinson and S. Simić, *Signless Laplacians of finite graphs*, *Linear Algebra and its Applications* 423 (2007), 155–171. https://doi.org/10.1016/j.laa.2007.01.009
6. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, *Journal of the American Statistical Association* 58 (1963), 13–30.
