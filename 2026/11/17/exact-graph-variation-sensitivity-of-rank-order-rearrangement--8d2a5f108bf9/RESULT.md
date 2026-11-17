# Exact graph-variation sensitivity of rank-order rearrangement

## Finding

Let \(G=(V,E,w)\) be any finite connected simple undirected graph, with \(|V|=n\ge 2\), positive edge weights \(w_e\), and a fixed order \(v_1,\ldots,v_n\) of the vertices. For real vertex functions, write
\[
\operatorname{TV}_w(h)=\sum_{\{u,v\}\in E}w_{uv}|h(u)-h(v)|.
\]
Let \(R(f)(v_i)\) be the \(i\)-th smallest of the \(n\) values of \(f\), including multiplicities. Define the sharp *two-input variation sensitivity*
\[
\mathcal L(G,w)=\sup_{\operatorname{TV}_w(f-g)>0}
\frac{\operatorname{TV}_w(R(f)-R(g))}{\operatorname{TV}_w(f-g)}.
\]
For every nonempty proper vertex subset \(S\), set \(b_w(S)=\sum_{\{u,v\}\in E:\,|\{u,v\}\cap S|=1} w_{uv}\) and, for \(1\le k<n\), let
\[
I_k=\min_{|S|=k}b_w(S),\qquad J_k=\max_{|S|=k}b_w(S).
\]
Then \(I_k>0\) and the exact sharp formula is
\[
\boxed{\mathcal L(G,w)=\max_{1\le k<n}\frac{J_k}{I_k}.}
\]
Each cardinality-level ratio \(J_k/I_k\) is realized by a pair of signals with strict, unchanged rank ordering; no limiting perturbations are necessary. The answer does not depend on the prescribed output order \(v_1,\ldots,v_n\).

Moreover, \(\mathcal L(G,w)=1\) **if and only if** \(G\) is a complete graph with equal positive edge weights (including the two-vertex case). Thus every other finite connected weighted graph admits a perturbation whose variation increases under rank-order rearrangement.

For unweighted graphs the formula yields, for every admissible order,
\[
\mathcal L(P_n)=n-1\quad(n\ge2),\qquad
\mathcal L(C_n)=\lfloor n/2\rfloor\quad(n\ge3),\qquad
\mathcal L(K_n)=1,\qquad
\mathcal L(K_{1,m})=m.
\]
If \(B_q\) consists of two disjoint \(q\)-cliques joined by one bridge edge, \(q\ge2\), then
\[
\boxed{\mathcal L(B_q)=\left\lfloor\frac{q^2}{2}\right\rfloor+1.}
\]
Hence the sensitivity of a rearrangement map on a connected graph can grow quadratically in the vertex count, despite rank-order rearrangement being nonexpansive in every coordinatewise \(\ell_p\) norm of *differences* (for \(1\le p\le\infty\)). The one-input Pólya–Szegő energy inequality and the two-input stability problem are different assertions.

## Assumptions and scope

All vertex values and perturbations are real. Graphs are finite, connected, undirected and simple, with strictly positive edge weights, not necessarily equal. The operator \(R\) globally sorts the multiset of values and places the resulting list into one fixed vertex order; ties are harmless because order statistics have unambiguous values. The same graph and weights measure input and output variation. The seminorm vanishes exactly on constant vertex functions. No normalization of edge weights or vertex counting measure is used.

## Proof

**1. A precise coarea identity.** For every real function \(h:V\to\mathbb R\), the layer-cake identity on each edge and finite interchange of sums and integrals give
\[
\operatorname{TV}_w(h)=\int_{-\infty}^{\infty}
 b_w(\{v:h(v)>s\})\,ds.
\]
If \(P\) is any permutation of the vertex coordinates, \(\{Ph>s\}\) has the same cardinality as \(\{h>s\}\). Consequently
\[
 b_w(\{Ph>s\})\le J_k\le \mathcal L_* I_k
 \le \mathcal L_* b_w(\{h>s\}),
\qquad \mathcal L_*:=\max_{1\le k<n}J_k/I_k,
\]
where \(k=|\{h>s\}|\). For \(k=0,n\), both boundaries vanish. Integration proves \(\operatorname{TV}_w(Ph)\le\mathcal L_*\operatorname{TV}_w(h)\) for every coordinate permutation \(P\).

**2. Passage to the nonlinear sorting map.** For fixed \(f,g\), the segment \(h_t=(1-t)f+tg\), \(0\le t\le1\), has only finitely many crossover times of coordinate values. On each intervening open subinterval, a single coordinate permutation \(P_j\) gives \(R(h_t)=P_j h_t\). Persistent ties cause no problem: any fixed tie-resolving permutation works throughout that interval. Continuity of order statistics allows the endpoint identity
\[
 R(g)-R(f)=\sum_j (t_{j+1}-t_j)P_j(g-f).
\]
Applying the triangle inequality for \(\operatorname{TV}_w\) and the bound in step 1 gives \(\operatorname{TV}_w(R(g)-R(f))\le\mathcal L_*\operatorname{TV}_w(g-f)\).

**3. Exact witnesses.** Choose \(k\) and sets \(S,T\) with \(|S|=|T|=k\), \(b_w(S)=I_k\), and \(b_w(T)=J_k\). Choose any bijection \(\pi:V\to V\) that maps the output rank positions in \(T\) to input positions in \(S\). Assign strictly increasing values \(4,8,\ldots,4n\) in that output-rank order to a baseline input \(f\). With \(g=f+\mathbf 1_S\), all ranks remain unchanged and \(R(g)-R(f)=\mathbf 1_T\), while \(g-f=\mathbf 1_S\). Hence the ratio is \(J_k/I_k\). Taking the maximum over \(k\) proves the boxed formula with exact attainment.

**4. Rigidity at one.** Every \(J_k/I_k\ge1\). If \(\mathcal L=1\), all singleton cuts have the same total weight \(d\). For \(n\ge3\), all two-vertex cuts likewise have a common weight \(c\). Declare \(w_{uv}=0\) for missing edges. Then \(b_w(\{u,v\})=2d-2w_{uv}=c\) for every distinct pair, so all possible \(w_{uv}\) are equal. Connectivity makes their common value positive; therefore the graph is complete with equal edge weights. The converse follows from \(b_w(S)=w|S|(n-|S|)\). The case \(n=2\) is immediate.

**5. Named families.** On a path, each nontrivial cut has at least one boundary edge, while the alternating cut has all \(n-1\) edges crossing; hence \(\mathcal L(P_n)=n-1\). On a cycle, the minimum boundary at every size is two, and the largest boundary at size \(k\) is \(2\min(k,n-k)\), attained by separated vertices or their complement; hence \(\mathcal L(C_n)=\lfloor n/2\rfloor\). On a star with \(m\) leaves, singletons have cut sizes one and \(m\), and the general formula gives \(m\). On a uniform clique, the cut boundary depends only on size.

For \(B_q\), let \(a\) and \(b\) be the selected counts in its two \(q\)-cliques. The boundary equals \(a(q-a)+b(q-b)+\varepsilon\), where \(\varepsilon\in\{0,1\}\) indicates whether the bridge crosses. Every boundary is at most \(2\lfloor q^2/4\rfloor+1=\lfloor q^2/2\rfloor+1\). For \(k=q\), selecting one whole clique gives minimum one, while balanced selections in the two cliques with opposite bridge-endpoint status realize that upper bound. For any \(k\ne q\), at least one clique is split, forcing boundary at least \(q-1\); thus such ratios do not exceed the ratio at \(k=q\). The barbell formula follows.

## Verification

The accompanying standard-library script `checker.py` independently computes weighted cut profiles, induced permutation-operator norms via binary level sets, and explicit strict-ranking witnesses using exact rational arithmetic. It checks all 43 connected labeled simple graphs with two through four vertices, 24 additional connected rationally weighted graphs, path/star/cycle identities for lengths two through twelve, and barbell identities for clique sizes two through six. Execute `python checker.py` from the directory containing the file.

The checker is finite corroboration, not a proof for arbitrary graphs or weights. Universal validity follows from the coarea, piecewise-permutation, and exact-witness arguments above.

## Relationship to prior work

Classical Pólya–Szegő and Hardy–Littlewood rearrangement theory studies how sorting one signal changes its energy. Hajaiej's 2010 Theorem 4.1 proves such a single-input discrete inequality. Chen et al. (public manuscript from 2014) motivate graph variation as a signal regularity measure but do not study the nonlinear two-input difference operator considered here. Steinerberger (2022), Gupta–Steinerberger (2022), and Hajaiej–Han–Hua (2022 manuscript; later journal publication) derive single-input discrete graph rearrangement inequalities and edge-isoperimetric comparisons; their assertions control \(\operatorname{TV}(R f)\) in terms of \(\operatorname{TV}(f)\), not \(\operatorname{TV}(R f-R g)\) in terms of \(\operatorname{TV}(f-g)\). These are mathematically distinct: even a rearrangement that always decreases single-input variation may have a large two-input sensitivity.

The coarea formula, the idea of ranking coordinate permutations on chambers, and graph edge-isoperimetry are established tools. The assessed statement is their combination into the sharp *two-input* graph-variation constant for arbitrary positive weights, its nonexpansivity rigidity, and the quadratic barbell family; it does not claim novelty for these constituent tools. A historically implicit equivalent result in the older variation-rearrangement literature is a residual priority risk.

## Limitations

The formula is an exact finite combinatorial characterization; optimizing the maximum and minimum cut boundary at each cardinality can be computationally hard for arbitrary large graphs. No polynomial-time algorithm for arbitrary graphs is claimed. The result covers global rank-order rearrangement on finite weighted simple graphs, not local filters, continuous domains, directed graphs, higher-order differences, or variations with different input and output weights. Complete classification of every maximizing pair is not claimed; explicit maximizing pairs are given. Numerical checks do not replace the proof, and independent external validation has not been performed.

## References

1. H. Hajaiej, *Rearrangement inequalities in the discrete setting and some applications*, Nonlinear Analysis **72** (2010), 1140–1148. DOI: 10.1016/j.na.2009.07.054. Author-hosted full text: https://hichem-hajaiej.com/wp-content/uploads/2014/12/Discrete.pdf.
2. S. Chen, A. Sandryhaila, J. M. F. Moura, and J. Kovačević, *Signal Recovery on Graphs: Variation Minimization*, arXiv:1411.7414, originally submitted November 26, 2014. https://arxiv.org/abs/1411.7414.
3. S. Steinerberger, *Discrete Rearrangements and the Pólya–Szegő Inequality on Graphs*, arXiv:2209.06765, September 14, 2022. https://arxiv.org/abs/2209.06765.
4. S. Gupta and S. Steinerberger, *Rearrangement Inequalities on the Lattice Graph*, arXiv:2212.07590, December 15, 2022; Bull. Lond. Math. Soc. **56** (2024), 3145–3163. https://arxiv.org/abs/2212.07590.
5. H. Hajaiej, F. Han, and B. Hua, *Discrete Schwarz rearrangement in lattice graphs*, arXiv:2209.01003, September 2, 2022, with later journal version. https://arxiv.org/abs/2209.01003.
6. *Variation Reducing Properties of Decreasing Rearrangements*, Canadian Journal of Mathematics **27** (1975), 330–336. DOI: 10.4153/CJM-1975-040-2 (historical priority-risk reference; only abstract-level access was obtained).
