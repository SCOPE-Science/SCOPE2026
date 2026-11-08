# Quenched Gaussian fluctuations of spanning-tree complexity in Pólya threshold graphs

## Finding

**Theorem (connected Pólya threshold graph).** Fix initial urn weights \(R,B>0\) and reinforcement \(\Delta>0\), and put \(a=R/\Delta\), \(b=B/\Delta\). For each integer \(n\ge2\), construct a threshold graph by a two-color Pólya urn: at birth \(i\), a red draw makes the new vertex adjacent to every older vertex, and a black draw makes it adjacent to none. Ignore self-loops when counting spanning trees. Condition the resulting graph on its final draw being red; denote its number of spanning trees by \(\tau_n\).

There is a coupling of these conditioned graphs, with a common latent variable \(P\sim\operatorname{Beta}(a+1,b)\), under which, conditional on \(P=p\), all nonterminal creation bits are independent \(\operatorname{Bernoulli}(p)\). In this coupling, almost surely,

\[
\frac{\log\tau_n-(n-2)\log n}{n}\longrightarrow
f(P),\qquad
f(p)=-1+\frac{1-2p}{1-p}\log p,\quad 0<p<1.
\]

For each fixed \(p\in(0,1)\), conditional on \(P=p\),

\[
\frac{\log\tau_n-(n-2)\log n-nf(p)}{\sqrt n}
\ \Longrightarrow\ \mathcal N(0,v(p)),
\]

where the **explicit, strictly positive** variance is

\[
v(p)=p(1-p)\int_0^1\left[
\frac{1}{1-p}\log\left(\frac{p+(1-p)y}{p}\right)
-\frac1p\log(1-y)
\right]^2\,dy.
\]

In particular \(v(1/2)=\pi^2/3\). The joint convergence with \(P\) is stable: conditional Gaussian fluctuations mix over the \(\operatorname{Beta}(a+1,b)\) latent law. Unconditionally, the first-order normalized statistic converges to the nondegenerate random variable \(f(P)\), while its second-order centered fluctuations are a non-Gaussian mixture of centered normal laws unless the variance mixing happens to degenerate. The function \(f\) is strictly increasing from \(-\infty\) to \(0\).

## Assumptions and scope

The graph has \(n\) distinct labeled vertices, with off-diagonal adjacency rule \(A_{ij}=Z_{\max(i,j)}\) for \(i\ne j\). The terminal bit \(Z_n=1\) ensures connectivity. Conditioning on this event in a classical Pólya urn changes its de Finetti distribution from \(\operatorname{Beta}(a,b)\) to \(\operatorname{Beta}(a+1,b)\); this posterior shift is essential. The construction may equivalently sample \(P\) from the latter distribution, sample independent \(Z_1,\ldots,Z_{n-1}\mid P\sim\operatorname{Bernoulli}(P)\), then set \(Z_n=1\). This coupling across \(n\) is used to formulate the almost-sure assertion; the original conditioned graph laws for individual \(n\) are exactly preserved. Parameters \(R,B,\Delta\) are fixed and positive. No uniformity as \(p\downarrow0\) or \(p\uparrow1\) is asserted.

The statistic is the logarithm of the number of ordinary unoriented spanning trees, not the weight of a minimum spanning tree and not the number of loop-rooted forests. Although the original construction may have a loop at each dominating vertex, loops do not affect its graph Laplacian or spanning-tree count.

## Proof

**Step 1: de Finetti conditioning and exact tree count.** The classical two-color Pólya urn has mixing law \(\operatorname{Beta}(a,b)\); conditional on the mixing parameter, all draw indicators are independent Bernoulli. Bayes' formula after observing \(Z_n=1\) gives the posterior density proportional to \(p\,p^{a-1}(1-p)^{b-1}\), hence \(P\mid Z_n=1\sim\operatorname{Beta}(a+1,b)\). Conditional on this parameter, \(Z_1,\ldots,Z_{n-1}\) remain independent Bernoulli.

Set \(S_{i+1,n}=\sum_{j=i+1}^n Z_j\) and \(\lambda_i=iZ_i+S_{i+1,n}\) for \(2\le i\le n\). In the loop-free Laplacian, the vectors \(u_i=\sum_{j<i}e_j-(i-1)e_i\) are eigenvectors with eigenvalues \(\lambda_i\), while the all-ones vector has eigenvalue zero. Direct multiplication using \(A_{ij}=Z_{\max(i,j)}\) proves these identities, and the \(n\) vectors are orthogonal. Since \(Z_n=1\), each \(\lambda_i\ge1\), and Kirchhoff's matrix-tree theorem gives the exact identity

\[
\tau_n=\frac1n\prod_{i=2}^n\left(iZ_i+\sum_{j=i+1}^nZ_j\right),\qquad
\lambda_n=n.
\]

Write \(L_n=\log\tau_n-(n-2)\log n=\sum_{i=2}^{n-1}\log(\lambda_i/n)\). Fix \(p\in(0,1)\) for the rest of the argument and work under the conditional iid law.

**Step 2: first-order centering.** For \(0\le x<1\), let

\[
h_1(x)=\log\bigl(p+(1-p)x\bigr),\quad
h_0(x)=\log\bigl(p(1-x)\bigr),\quad
h_z(x)=h_0(x)+zA(x),
\]

\[
A(x)=\log\left(\frac{p+(1-p)x}{p(1-x)}\right),\qquad
b_p(x)=\frac{p}{p+(1-p)x}+\frac{1-p}{p(1-x)}.
\]

The integral of \(p h_1+(1-p)h_0\) is

\[
\int_0^1\bigl[p h_1(x)+(1-p)h_0(x)\bigr]dx
=-1+\frac{1-2p}{1-p}\log p=f(p).
\]

For \(i<n\), put \(x_i=i/n\), \(k_i=n-i\), and \(\epsilon_i=Z_i-p\). The exact decomposition is

\[
\lambda_i=n\bigl[p(1-x_i)+x_i Z_i\bigr]+\delta_i,
\qquad \delta_i=(1-p)+\sum_{j=i+1}^{n-1}\epsilon_j.
\]

**Step 3: uniform Taylor control.** Set \(m_n=\lceil n^{1/3}\rceil\), and retain indices \(2\le i\le n-m_n\). Hoeffding's inequality and a union bound imply, with probability at least \(1-O(n^{-3})\), that simultaneously for these indices

\[
|\delta_i|\le C_p\sqrt{k_i\log n}+1.
\]

The positive baseline in the previous display is at least \(p k_i\). As \(k_i\ge m_n\), the relative correction is uniformly \(o(1)\). Taylor's formula, summed over all retained indices on the preceding high-probability event, therefore yields

\[
\sum_{i=2}^{n-m_n}\log(\lambda_i/n)
=\sum_{i=2}^{n-m_n}h_{Z_i}(x_i)
+\sum_{i=2}^{n-m_n}\frac{\delta_i}{n[p(1-x_i)+x_i Z_i]}
+O((\log n)^2).
\]

Indeed on this high-probability event the quadratic remainder is bounded by \(C_p\sum_{k=m_n}^{n}\log n/k=O((\log n)^2)\). For the omitted \(m_n-1\) indices, \(1\le\lambda_i\le n\) and thus their total log contribution in absolute value is at most \(m_n\log n=o(\sqrt n)\). The analogous tail of the deterministic integral also has magnitude \(O(m_n\log n)\). Riemann-sum error for the regular part and integrable logarithmic singularity is \(O(\log n)\).

**Step 4: reverse-martingale decomposition.** Replace the reciprocal in the linear term by its conditional mean \(b_p(x_i)\). Define

\[
D_n=\sum_{i=2}^{n-m_n}\frac{\delta_i}{n}
\left(\frac1{p(1-x_i)+x_iZ_i}-b_p(x_i)\right).
\]

Because \(\delta_i\) depends only on the later bits, the summands form reverse martingale differences and are pairwise orthogonal. Their variances sum to at most

\[
\mathbb E_p D_n^2\le C_p\sum_{k=m_n}^n\frac{k+1}{k^2}
=O(\log n),
\]

where the implied constant depends on the fixed parameter. Consequently \(D_n=o_{\mathbb P_p}(\sqrt n)\). Also \((1-p)n^{-1}\sum b_p(x_i)=O(\log n)\) deterministically. Interchanging the sums gives the remaining random contribution

\[
\sum_{j=3}^{n-1}\epsilon_j H_{n,j},\quad
H_{n,j}=\frac1n\sum_{i=2}^{\min(j-1,n-m_n)}b_p(x_i).
\]

For \(y<1\), its continuum primitive is

\[
H_p(y)=\int_0^y b_p(x)\,dx
=\frac{p}{1-p}\log\frac{p+(1-p)y}{p}
-\frac{1-p}{p}\log(1-y).
\]

The direct Bernoulli part of \(\sum h_{Z_i}\) is \(\sum_{i=2}^{n-m_n}\epsilon_i A(x_i)\). The Riemann approximation \(H_{n,j}=H_p(j/n)+O(1/m_n)\) holds uniformly for \(j\le n-m_n\) (again with a deterministic constant depending on the fixed parameter). The last \(m_n\) coefficients, and corresponding missing terms, have magnitudes at most \(C_p\log n\). Because the bits are independent and centered, the mean square of all coefficient-replacement errors is \(O(n/m_n^2+m_n\log^2n)=o(n)\). Therefore

\[
L_n-nf(p)=\sum_{j=2}^{n-1}\epsilon_j g_p(j/n)
+o_{\mathbb P_p}(\sqrt n),
\]

where

\[
g_p(y)=A(y)+H_p(y)
=\frac1{1-p}\log\frac{p+(1-p)y}{p}
-\frac1p\log(1-y).
\]

The square of this weight is integrable on \((0,1)\), and \(\max_{j<n}|g_p(j/n)|=O(\log n)=o(\sqrt n)\). Hence the Lindeberg triangular-array theorem gives the stated conditional central limit theorem with variance \(p(1-p)\int_0^1g_p(y)^2dy\).

**Step 5: almost-sure first-order law and mixtures.** The Hoeffding event in Step 3 fails with summable probability. On its eventual occurrence the Taylor correction is \(O(\sqrt{n\log n}+\log^2n)=o(n)\). The centered triangular sum \(\sum_{i=2}^{n-m_n}\epsilon_i A(i/n)\) is \(o(n)\) almost surely: bounded weighted Hoeffding gives summable tails for deviations of order \(n\), since the weights are \(O(\log n)\) and the sum of their squares is \(O(n)\). The terminal tail and Riemann errors are \(o(n)\) as well. This proves the almost-sure first-order law conditional on each \(p\in(0,1)\), hence under the common beta-mixture coupling. Conditional characteristic-function convergence combined with bounded convergence over the beta distribution yields joint (stable) Gaussian-mixture convergence.

For \(p=1/2\), \(g_p(y)=2\log((1+y)/(1-y))\) and thus

\[
v(1/2)=\int_0^1\log^2\!\left(\frac{1+y}{1-y}\right)dy
=4\int_0^\infty\frac{u^2}{\cosh^2u}\,du
=\frac{\pi^2}{3},
\]

using \(y=\tanh u\) and \(\int_0^\infty u^2/\cosh^2u\,du=\pi^2/12\), which follows by expanding \(\operatorname{sech}^2 u=4\sum_{k\ge1}(-1)^{k-1}k e^{-2ku}\) for \(u>0\), integrating termwise after a positive cutoff, and sending the cutoff to zero. Finally, direct differentiation and \(-\log p\ge1-p\) show \(f'(p)\ge1/p>0\); endpoint limits give its asserted range.

## Verification

The standalone `verify.py` reconstructs the Laplacian and Kirchhoff cofactor independently of the product formula, exhaustively tests connected binary creation strings for orders \(2\) through \(9\), evaluates the analytic limit and variance integrals, tests the special value \(\pi^2/3\), and performs seeded conditional Bernoulli simulations for selected finite orders and parameters. The tests are finite checks, not proofs of the asymptotic statements; the uniform Taylor and reverse-martingale estimates in the proof are the critical infinite arguments.

Run with `python verify.py`. Requires Python 3 and the standard library only. It uses integer Bareiss elimination for exact determinants, so no external symbolic or numerical libraries are necessary.

## Relationship to prior work

Yu, Alajaji and Gharesifard (2026) introduce Pólya threshold graphs, establish the de Finetti/Beta-binomial structure, and calculate individual degree laws and the Laplacian spectrum. Their connected-graph consensus construction also fixes the last creation bit at one; their text does not state a spanning-tree fluctuation theorem. The determinant factorization used here is an elementary consequence of their eigenvalue calculation and previously known threshold-graph spanning-tree formulas, including the explicit formula surveyed by Go, Khwa, Luo and Stamps (2021). **This finite factorization is not presented as original.**

Diaconis, Holmes and Janson (2008/2010) analyze independent-creation threshold graphs, their graphon limits and normalized Laplacian spectra. Those first-order results are relevant to the quenched law but do not explicitly provide the second-order logarithmic determinant Gaussian limit or the influence kernel \(g_p\) in their accessible full text. Hammer and Kelmans (1996) give general exact spanning-tree formulas for deterministic threshold graphs. The presently asserted contribution is the explicit second-order conditional fluctuation law and its beta mixture, not the underlying exchangeability or determinant identity.

## Limitations

This is a fixed-positive-parameter theorem, not uniform at the extremes of the beta support. Conditioning on connectedness at each order does not make the original unconditioned sequence nested; the almost-sure statement uses the explicit common latent-parameter coupling, which has the correct marginal conditioned law at every order. The proof is not a theorem about all random threshold graph mechanisms or arbitrary multi-color urns. Some older general probabilistic delta-method or spanning-tree results could subsume the claim after nontrivial specialization; full historical-priority certainty is not asserted. Numerical checks cannot establish originality, and no independent mathematical audit has been carried out.

## References

1. Jinghan Yu, Fady Alajaji, Bahman Gharesifard, *Pólya Threshold Graphs*, arXiv:2603.18452v1, first posted 2026-03-19. https://arxiv.org/html/2603.18452v1
2. Persi Diaconis, Susan Holmes, Svante Janson, *Threshold Graph Limits and Random Threshold Graphs*, Internet Mathematics 5 (2008), 267–320. https://pmc.ncbi.nlm.nih.gov/articles/PMC2930250/
3. Christian Go, Zhong Xuan Khwa, Xinyu Luo, Matthew T. Stamps, *Spanning tree enumeration via triangular rank-one perturbations of graph Laplacians*, arXiv:2103.13596v1, first posted 2021-03-25. https://arxiv.org/html/2103.13596v1
4. Peter L. Hammer and Alexander K. Kelmans, *Laplacian Spectra and Spanning Trees of Threshold Graphs*, Discrete Applied Mathematics 65 (1996), 255–273. https://doi.org/10.1016/0166-218X(94)00049-J
5. Kirchhoff's matrix-tree theorem (classical).
