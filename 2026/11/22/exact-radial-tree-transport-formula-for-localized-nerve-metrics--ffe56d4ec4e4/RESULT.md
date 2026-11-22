# Exact radial-tree transport formula for localized nerve metrics on finite ultrametrics

## Finding

Let \((M,d)\) be a finite ultrametric space with at least two points, let \(0<r\leq\operatorname{diam}(M)\), and let \(\mu,\nu\) be arbitrary probability measures on \(M\). The scale-localized nerve-map transport metric introduced by McCabe and Perea is
\[
d_{\mathrm L}^{\,r}(\mu,\nu)=\max_{m\in M}\inf_{\pi\in\Pi(\mu,\nu)}\sum_{x,y\in M}\left[\min\{k_m(x),k_m(y)\}\,d(x,y)+2r|k_m(x)-k_m(y)|\right]\pi(x,y),
\qquad k_m(x)=\max\{r-d(m,x),0\}.
\]
For every center \(m\), a **canonical radial tree**, described below, realizes the bracketed cost exactly as its tree-path pseudometric. Writing \(\ell(e)\) for its edge lengths and \(A_e\subseteq M\) for the sites represented below an oriented edge, one obtains the exact formula
\[
\boxed{\displaystyle d_{\mathrm L}^{\,r}(\mu,\nu)=\max_{m\in M}\sum_{e\in E(T_m)}\ell(e)\,|\mu(A_e)-\nu(A_e)|.}
\]
Thus the localized metric on every finite ultrametric admits a finite maximum of explicit weighted absolute mass-imbalance sums, with **no transport linear program**. All centers and all probability weights are covered; this is a metric evaluation theorem, not an additional stability estimate for the nerve map itself.

## Assumptions and scope

An ultrametric is a metric with \(d(x,z)\leq\max\{d(x,y),d(y,z)\}\). Fix \(m\in M\). For every distinct \(t\) with \(0<t<r\) attained among \(d(m,x)\), define its shell
\[
S_t=\{x\in M:d(m,x)=t\},\quad S_{\geq r}=\{x\in M:d(m,x)\geq r\}.
\]
Sites in \(S_{\geq r}\) will share one terminal tree vertex; this is necessary because the localized cost vanishes between them. A shell may contain one or more sites. Define three nonnegative scalar functions on \([0,r]\):
\[
H(t)=\frac{5rt-t^2}{2},\qquad L(t)=\frac{t(r-t)}2,\qquad F(t)=3rt-t^2=H(t)+L(t).
\]
The derivative \(H'(t)=(5r-2t)/2>0\) on \([0,r]\). Set the radial trunk from \(m\) (at height zero) to a terminal node (at height \(H(r)=2r^2\)), with branch points at heights \(H(t)\) for all occurring shells.

At the branch point at height \(H(t)\), graft a rooted, equidistant tree for the ultrametric restricted to \(S_t\), arranged so that its leaves representing the shell sites lie at distance exactly \(L(t)\) from that branch point and such that its leaf-to-leaf distances are \((r-t)d(x,y)\). To construct such a tree, take the standard dendrogram of the finite ultrametric \(d|_{S_t}\) of upper height \(t\), scale all vertical heights by \((r-t)/2\), and include an initial stem if the shell diameter is smaller than \(t\). As \(d(x,y)\leq t\) on the shell, all resulting edge lengths are nonnegative. Attach the entire outside set \(S_{\ge r}\) to the terminal node; zero-weight leaf edges or the identification of their site locations are equivalent. Denote this tree by \(T_m\), and for an edge directed away from the root define \(A_e\) as the preimage in \(M\) of sites in the descendant component. It has linearly many vertices and edges in \(|M|\) (after optional zero-length edge contractions).

## Proof

**Step 1: the localized cost equals tree distance.** Put
\[
c_m(x,y)=\min\{k_m(x),k_m(y)\}\,d(x,y)+2r|k_m(x)-k_m(y)|.
\]
For distinct shell radii \(0<t<s<r\), the ultrametric inequality gives \(d(x,y)=s\) whenever \(x\in S_t\) and \(y\in S_s\). It also gives \(d(x,y)\leq t\) within \(S_t\). Therefore all point pairs are covered by the following exhaustive cases:

- For \(y\in S_t\), \(c_m(m,y)=(r-t)t+2rt=F(t)=H(t)+L(t)\), the root-to-leaf tree length.
- For \(x\in S_t\) and \(y\in S_s\), with \(0<t<s<r\), \(c_m(x,y)=(r-s)s+2r(s-t)=F(s)-2rt\). Their lowest common ancestor lies at trunk height \(H(t)\), and the tree distance is \(F(t)+F(s)-2H(t)=F(s)-2rt\).
- For \(x,y\in S_t\), the two kernel weights coincide, so \(c_m(x,y)=(r-t)d(x,y)\), exactly the grafted dendrogram's leaf distance.
- For \(x\in S_t\) and \(y\in S_{\ge r}\), the cost is \(2r(r-t)\), exactly the tree length \(H(r)-H(t)+L(t)\).
- The cost between \(m\) and an outside site is \(2r^2=H(r)\); between two outside sites it is zero. Diagonal costs are zero.

The cases remain valid when the outside set is empty; in that case the terminal node is simply an unused trunk endpoint. Thus for every \(x,y\in M\),
\[
\boxed{c_m(x,y)=d_{T_m}(\iota_m(x),\iota_m(y))},
\]
where \(\iota_m\) maps each site to its assigned tree location. In particular, \(c_m\) is a tree *pseudometric*, not necessarily a tree metric on the original distinct sites, and not necessarily an ultrametric.

**Step 2: exact optimal transport for a tree pseudometric.** Push \(\mu,\nu\) forward by \(\iota_m\) to the vertices of \(T_m\). Let \(b(v)\) be their signed difference at a vertex. For each directed edge \(e\), every transport plan must move at least \(|\sum_{v\text{ below }e}b(v)|\) units across that edge, with edge cost \(\ell(e)\). Summing the edge lower bounds gives
\[
T_{c_m}(\mu,\nu)\geq\sum_e\ell(e)|\mu(A_e)-\nu(A_e)|.
\]
Conversely, on a tree the unique necessary net flow across each edge is exactly the signed mass imbalance of the descendant subtree. Sending that flow along each edge, then matching residual supplies and demands at the vertices, yields a feasible transport of exactly the displayed cost (equivalently, decompose a divergence-balanced finite tree flow into source-to-sink paths). Hence equality holds. This also justifies pooling distinct original sites that \(c_m\) identifies at zero distance.

**Step 3: maximize over all centers.** By the original definition of \(d_{\mathrm L}^{\,r}\), finite \(M\) makes its outer supremum a maximum, and substituting Step 2 for each center proves the boxed identity. Each tree requires only ultrametric clustering and a single subtree-imbalance pass per pair of measures, so the formula removes the nested transport optimization. No interchange of supremum and infimum has been asserted.

**Boundary demonstrating the ultrametric hypothesis.** On the ordinary four-point line \(\{0,1,2,3\}\), with \(m=1\), \(r=2\), the localized cost matrix is
\[
\begin{pmatrix}0&5&2&4\\5&0&5&8\\2&5&0&4\\4&8&4&0\end{pmatrix}.
\]
Its three four-point pair sums are \(9,10,9\). The two largest are unequal, violating the necessary four-point condition for a tree pseudometric, so the radial-tree assertion does not extend to arbitrary finite metric spaces.

## Verification

The accompanying standalone `check_tree.py` (Python 3, NumPy and SciPy) implements the kernel-defined cost independently of the radial-tree construction. It builds random ultrametric dendrograms for all sizes from two through nine points, with thirty seeds per size, at three radii and every possible center. For each of the **3,960** resulting center-and-radius instances, it checks all pair distances, the four-point tree condition, and two nontrivial transport cost comparisons against an independently formulated transportation linear program. It additionally checks the explicit four-point non-ultrametric obstruction. All checks passed in the packaged execution.

The unbounded theorem is established by Steps 1–3, not inferred from the finite tests. The code uses floating-point tolerances solely for numerical verification; its output is not a formal proof certificate.

## Relationship to prior work

McCabe and Perea [1] introduce the localized pseudometric \(c_m\) and the corresponding scale-dependent metric \(d_{\mathrm L}^{\,r}\) for stability of weighted nerve maps. Their Lemma 3.2 identifies \(c_m\) as a pullback of an auxiliary Wasserstein metric and their Proposition 3.3 proves metric properties and comparison with ordinary Wasserstein distance. Their Theorem 3.4 applies this quantity to nerve-map stability. The new assertion here is **the exact radial-tree realization of every \(c_m\) on finite ultrametrics and the resulting tree-cut closed formula for the complete localized metric**. The source's §3 and experimental discussion do not assert this realization.

The exact edge-imbalance formula for \(1\)-Wasserstein transport on trees is established background; see [2] and [3]. These results alone do not imply the finding, because identifying the original localized cost as a tree distance requires the new shell-wise identity and explicit grafting construction. General results on ultrametric dendrograms are also background, not a claim of novelty for dendrogram existence. No claim is made to originality of the individual ingredients or to exclusivity of the formula against all unindexed literature.

## Limitations

The formula assumes a **finite ultrametric** and a common radius \(0<r\leq\operatorname{diam}(M)\). It does not address general metric spaces, infinite ultrametrics, the distinct pointwise cost \(\widetilde c_m\) with a support-dependent coefficient, or the sharpness of a particular nerve-map stability constant. It gives an exact distance formula, not a new bound on nerve-map homotopy type. Publication-priority search cannot exclude unindexed equivalent expressions. Independent mathematical audit has not been performed.

## References

[1] Kenneth McCabe and Jose A. Perea, *Wasserstein Stability of the Nerve Map*, arXiv:2611.15938v1, first public 2026-11-11, https://arxiv.org/html/2611.15938v1 ; see §3, Lemma 3.2, Proposition 3.3, Theorem 3.4.

[2] Georges Skandalis and Alain Valette, *On the transportation cost norm on finite metric graphs*, arXiv:2601.16859v1 (2026), https://arxiv.org/abs/2601.16859 ; tree-flow cost properties and their relationship with transportation norms.

[3] Samantha Chen, Puoya Tabaghi, and Yusu Wang, *Learning Ultrametric Trees for Optimal Transport Regression*, arXiv:2210.12288 (2022), https://arxiv.org/abs/2210.12288 ; dendrogram representations and tree transport distances.
