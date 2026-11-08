# Independent Poisson omission counts in uniform subtrees of complete split graphs

## Finding

Let \(a\to\infty\) and let \(b=b(a)\) be positive integers with \(b/a\to c\in(0,\infty)\). Form the **complete split graph** \(G_{a,b}=K_a\vee\overline K_b\), the join of an \(a\)-vertex clique \(A\) and a \(b\)-vertex independent set \(B\). Choose uniformly from all nonempty subgraphs of \(G_{a,b}\) that are trees, without requiring them to be induced or spanning. Write \(K\) and \(L\) for the numbers of omitted vertices in \(A\) and \(B\), respectively.

**Theorem.** In total variation on \(\mathbb N_0^2\),
\[
(K,L)\ \xrightarrow{\mathrm{TV}}\
\operatorname{Pois}\!\left(\lambda_A(c)\right)
\otimes\operatorname{Pois}\!\left(\lambda_B(c)\right),
\]
where
\[
\lambda_A(c)=\frac{\exp\!\left(-c-\frac1{1+c}\right)}{1+c},
\qquad
\lambda_B(c)=c\exp\!\left(-\frac1{1+c}\right).
\]
Thus omissions from the two vertex classes become independent. In particular, the probability that the uniformly chosen subtree is spanning tends to
\[
q(c)=\exp\!\left[-\frac{e^{-c-1/(1+c)}}{1+c}
-c e^{-1/(1+c)}\right].
\]
This limiting spanning probability is strictly decreasing in \(c>0\). Its continuous limit at \(c\downarrow0\) is \(e^{-1/e}\), and \(q(c)\sim e^{1-c}\) as \(c\to\infty\). These endpoint statements concern the displayed function, not an extension of the probabilistic theorem to arbitrary non-proportional growth regimes.

## Assumptions and scope

All graphs are labeled, simple, unweighted and undirected; two subtrees are different if they differ in vertex or edge sets. Every one-vertex subgraph is counted as a tree. The vertex-class identities are retained. The statement assumes \(a\to\infty\), \(b\to\infty\), and a finite strictly positive ratio limit \(c\); it does not assert uniformity in \(c\), or a theorem when \(b/a\to0\) or \(\infty\).

## Proof

For \(i\ge1\) and \(j\ge0\), the number \(\tau(i,j)\) of spanning trees of the induced complete split graph with \(i\) clique and \(j\) independent vertices is
\[
\tau(i,j)=i^{j-1}(i+j)^{i-1}.
\tag{1}
\]
The expression is interpreted as \(i^{i-2}\) for \(j=0\), including the one-vertex convention. To verify (1) for \(j\ge1\), the Laplacian has nonzero eigenvalues \(i+j\) with multiplicity \(i\) and \(i\) with multiplicity \(j-1\), so the matrix-tree theorem gives (1); the case \(j=0\) is Cayley's formula. A tree on no clique vertices can only be a single independent vertex.

Let \(\tau_0=\tau(a,b)=a^{b-1}(a+b)^{a-1}\). For \(0\le k\le a-1\) and \(0\le\ell\le b\), the number of subtrees omitting exactly \(k\) clique vertices and \(\ell\) independent vertices, divided by \(\tau_0\), is exactly
\[
R_{a,b}(k,\ell)=
\binom ak\binom b\ell
\frac{(a-k)^{b-\ell-1}(a+b-k-\ell)^{a-k-1}}
{a^{b-1}(a+b)^{a-1}}.
\tag{2}
\]
There are also precisely \(b\) trees with no clique vertices, each a singleton. This accounts for every subtree without duplication.

For fixed \(k,\ell\), rewrite (2) as
\[
\binom ak\binom b\ell a^{-\ell}(a+b)^{-k}
\left(1-\frac{k}{a}\right)^{b-\ell-1}
\left(1-\frac{k+\ell}{a+b}\right)^{a-k-1}.
\tag{3}
\]
The first factor tends to \(c^{\ell}/[(1+c)^k k!\ell!]\), while the last two factors tend to \(e^{-ck}\) and \(e^{-(k+\ell)/(1+c)}\). Consequently,
\[
R_{a,b}(k,\ell)\longrightarrow
\frac{\lambda_A(c)^k\lambda_B(c)^\ell}{k!\ell!}.
\tag{4}
\]

The passage from fixed-coefficient limits to the whole distribution requires a tail bound. Whenever \(\ell\le b-1\), both exponents in (3) are nonnegative and
\[
0\le R_{a,b}(k,\ell)\le
\frac{1}{k!\ell!}\left(\frac{a}{a+b}\right)^k
\left(\frac ba\right)^\ell.
\tag{5}
\]
Since \(b/a\) remains bounded, the right side is dominated by a summable two-dimensional exponential-series envelope, independent of sufficiently large \(a\). The exceptional boundary \(\ell=b\), consisting of clique-only trees, has total relative mass at most
\[
\frac{2^a a^{a-2}}{a^{b-1}(a+b)^{a-1}}
=2^a a^{-b}\left(\frac a{a+b}\right)^{a-1}
\longrightarrow0.
\tag{6}
\]
Here \(i^{i-2}\le a^{a-2}\) for \(1\le i\le a\), with the singleton interpreted as one, and \(b/a\to c>0\). The further relative mass from singleton independent vertices, \(b/\tau_0\), also tends to zero.

Dominated convergence applied to (4)–(6) therefore yields
\[
\frac{\#\{\text{all nonempty subtrees of }G_{a,b}\}}{\tau_0}
\longrightarrow
\sum_{k,\ell\ge0}\frac{\lambda_A^k\lambda_B^\ell}{k!\ell!}
=e^{\lambda_A+\lambda_B}.
\]
After normalization, the joint point probabilities converge to the product-Poisson probabilities. Because these probabilities have total mass one, convergence is also in total variation (equivalently, apply the discrete Scheffé lemma). The event \((K,L)=(0,0)\) is exactly the spanning event, giving \(q(c)\).

To establish strict monotonicity, write \(t=1+c\), \(h=e^{-c}/t\), and \(\beta(c)=\lambda_A(c)+\lambda_B(c)=e^{-1/t}(c+h)\). Differentiation gives
\[
\frac{\beta'(c)}{e^{-1/t}}
=1+\frac c{t^2}-h\left(1+\frac1t-\frac1{t^2}\right)
>\frac{(t-1)(t^2+t-1)}{t^3}>0.
\]
The first strict inequality uses \(h<1/t\) for \(c>0\). Hence \(q(c)=e^{-\beta(c)}\) is strictly decreasing. Direct expansion shows \(\beta(c)\to e^{-1}\) as \(c\downarrow0\) and \(\beta(c)=c-1+o(1)\) as \(c\to\infty\), proving the endpoint statements.

## Verification

The accompanying standalone Python checker uses no nonstandard packages. It independently computes exact Kirchhoff cofactors for induced graphs with up to six vertices, independently enumerates edge subsets forming trees, and matches every possible omitted-class count in several small labeled split graphs to (1)–(2). It also evaluates normalized finite-size coefficients and their analytic limits for multiple proportional growth ratios. Run `python check.py`. Successful execution prints `VERIFY_OK 868 exact/analytic-limit assertions`.

These finite checks are consistency evidence; the all-parameter and convergence claims rest on the determinant, combinatorial counting, dominated convergence and derivative arguments above.

## Relationship to prior work

Chin, Gordon, MacPhee and Vincent (2018) studied the distribution of sizes of subtrees and the complete-graph and complete-bipartite cases. Wagner (2019 preprint; 2021 journal article) proved broad spanning-subtree probability statements and a Poisson law for omitted vertices of dense Erdős–Rényi graphs. Cambie, Chen, Hao and Tokar (2023 preprint; 2024 journal article) studied mean subtree order on exactly these split graphs, principally in the regime with the clique order fixed and the independent side much larger. Wagner and Wang (2026) prove a *scalar* omitted-vertex Poisson law for arbitrary dense graph sequences. The new assertion here resolves the **joint vertex-class composition** of the omissions and its two explicit, asymptotically independent intensities when both classes grow proportionally. The scalar total \(K+L\) follows the general law, and is not claimed as a separate novelty.

## Limitations

There is no assertion of independent external validation. The proof does not give a convergence rate, does not treat ratio limits zero or infinity for the sampling law, and does not extend to general split graphs where some clique–independent edges are absent. Relevant older results may exist outside the inspected literature, and the full text of Chin et al. (2018) was not obtained in this examination; this is a residual priority risk. No conclusion of uniqueness follows from the literature searches alone.

## References

- A. J. Chin, G. Gordon, K. J. MacPhee, and C. Vincent, *Subtrees of graphs*, Journal of Graph Theory 89 (2018), 413–438. First published 2018-05-02. https://doi.org/10.1002/jgt.22359
- S. Wagner, *On the probability that a random subtree is spanning*, Journal of Graph Theory 98 (2021), 195–215; preprint https://arxiv.org/abs/1910.07349. https://doi.org/10.1002/jgt.22688
- S. Cambie, G. Chen, Y. Hao, and N. Tokar, *Decreasing the mean subtree order by adding k edges*, 2023 preprint and Journal of Graph Theory 105 (2024), 357–366. https://arxiv.org/abs/2308.12808
- S. Wagner and R. Wang, *The Distribution Of Subtrees In Dense Graphs And The Roots Of The Subtree Polynomial*, 2026 preprint. https://arxiv.org/abs/2605.03583
- Kirchhoff's matrix-tree theorem and Cayley's labeled-tree formula (standard enumeration tools).
