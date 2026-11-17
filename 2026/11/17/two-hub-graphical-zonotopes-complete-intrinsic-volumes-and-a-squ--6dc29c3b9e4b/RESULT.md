# Two-hub graphical zonotopes: complete intrinsic volumes and a square-root forest-connectivity anomaly

## Finding

For each integer \(q\ge2\), let \(G_q=K_{2,q}\), with two hubs and \(q\) peripheral vertices, and define its canonical graphical zonotope in the inherited Euclidean metric by
\[
Z_q=\sum_{\{u,v\}\in E(G_q)}[e_u,e_v]\subset\mathbb R^{q+2}.
\]
It has intrinsic dimension \(d=q+1\). Write \(V_k(Z_q)\) for its \(k\)-th Euclidean Steiner intrinsic volume, normalized by
\[
\operatorname{Vol}_{d}(Z_q+t B_d)=\sum_{k=0}^d\kappa_{d-k}V_k(Z_q)t^{d-k},\qquad \kappa_j=\operatorname{Vol}_j(B_j).
\]
Then \(V_0(Z_q)=1\) and, simultaneously for every \(0\le k\le q+1\),
\[
\boxed{V_k(Z_q)=D_q(k)+C_q(k)},
\]
where the following completely explicit expressions use empty sums and out-of-range binomial coefficients as zero:
\[
D_q(k)=\sum_{\substack{a,b\ge0\\a+b=k\le q}}
\frac{q!}{a!b!(q-a-b)!}\sqrt{(a+1)(b+1)},
\]
\[
C_q(k)=\begin{cases}
q\binom{q-1}{k-2}2^{k-2}\sqrt{k+1},&2\le k\le q+1,\\
0,&\text{otherwise}.
\end{cases}
\]
These are respectively the contributions of forests whose hubs are disconnected and connected. In particular, the entire intrinsic-volume polynomial \(\sum_{k=0}^{q+1}V_k(Z_q)z^k\) is determined, rather than only its top or surface-area coefficients.

Let \(\mathcal F_q\) be the family of all spanning forests of \(G_q\) (isolated vertices are allowed), and give each forest the probability
\[
\mathbb P_q(F)=\frac{\prod_{T\in\operatorname{Comp}(F)}\sqrt{|V(T)|}}{\sum_{H\in\mathcal F_q}\prod_{T\in\operatorname{Comp}(H)}\sqrt{|V(T)|}}.
\]
Thus the denominator is exactly the sum of all Steiner intrinsic volumes; the measure is geometrically induced by wedge volumes, with the stated fixed unit-generator normalization. The probability that the two hubs are disconnected has the sharp two-term expansion
\[
\boxed{\mathbb P_q(h_1\not\leftrightarrow h_2)=
\sqrt{\frac{3}{2q}}-\frac{3}{2q}+O(q^{-3/2}).}
\]
Under uniform counting over the same forests the probability is exactly \(3/(q+3)\), so Euclidean-volume weighting delays hub connectivity by an unbounded square-root factor.

Finally, for the forest edge-count \(K_q=|E(F)|\) under \(\mathbb P_q\),
\[
\bigl\|\mathcal L(K_q)-\mathcal L(2+\operatorname{Bin}(q-1,2/3))\bigr\|_{\mathrm{TV}}=O(q^{-1/2}),
\]
and hence
\[
\frac{K_q-2q/3}{\sqrt{2q/9}}\xrightarrow{\mathrm d}N(0,1).
\]

## Assumptions and scope

The graph is the simple complete bipartite graph with precisely two distinguished hubs, \(q\ge2\) other vertices, and one unweighted segment \([e_u,e_v]\) for every edge. The Euclidean metric is inherited from \(\mathbb R^{q+2}\) on its affine \((q+1)\)-plane. The formula is exact for all ranks, not a lattice-volume normalization. The asymptotic assertions take \(q\to\infty\) with the two-hub part fixed. The Wills/Steiner coefficient sum and forest law depend on this specified length scale.

## Proof

**1. Euclidean forest expansion.** Translate each segment by one endpoint; translation preserves intrinsic volumes, leaving generators \(g_{uv}=e_u-e_v\). The standard zonotope intrinsic-volume identity gives
\[
V_k(Z_q)=\sum_{\substack{I\subseteq E(G_q)\\|I|=k}}\sqrt{\det(G_I^{\mathsf T}G_I)},
\]
with zero assigned to linearly dependent subsets (the empty determinant is one). One justification is Kubota's projection formula: the projected \(k\)-volume of a zonotope is the sum of absolute determinants over its \(k\)-generator subsets; the rotational average of each determinant is a common constant times its Euclidean wedge norm, with the constant canceled by Kubota's normalization on a \(k\)-dimensional parallelepiped.

A subcollection of graph incidence vectors is independent if and only if its graph edges form a forest. For a tree with \(s\) vertices the Gram determinant of its \(s-1\) oriented incidence vectors equals \(s\): the nonzero Laplacian eigenvalues multiply to \(s\) by the matrix-tree identity, since a tree has one spanning tree. Orthogonal supports of different components therefore give the forest weight \(\prod_T\sqrt{|V(T)|}\), including isolated components with factor one.

**2. Exact two-class enumeration.** If the two hubs are disconnected, every peripheral vertex chooses one of three states: attached only to the first hub, only to the second hub, or isolated. With \(a,b\) in the first two states there are \(q!/[a!b!(q-a-b)!]\) forests of rank \(k=a+b\); their component-size product is \((a+1)(b+1)\). This proves the expression for \(D_q(k)\).

If the hubs are connected, exactly one peripheral vertex carries both incident edges: zero would disconnect the hubs, while two would form a four-cycle. Choose this bridging vertex in \(q\) ways; of the remaining \(q-1\) peripherals, choose \(k-2\) to attach, each independently to either hub. The single nontrivial component then has \(k+1\) vertices. This proves \(C_q(k)\), with no excluded forest types.

**3. Weighted connectivity asymptotics.** Let \((A,B,R)\) have the multinomial distribution with \(q\) trials and equal category probabilities \(1/3\). Let \(T\) have the binomial distribution \(\operatorname{Bin}(q-1,2/3)\). Summing the exact branches over all ranks gives
\[
\sum_k D_q(k)=3^q\mathbb E\sqrt{(A+1)(B+1)},\qquad
\sum_k C_q(k)=q3^{q-1}\mathbb E\sqrt{T+3}.
\]
By concentration and second-order Taylor expansion on \(A,B\in[q/6,q/2]\) (the complement has exponentially small probability), the first expectation is \(q/3+O(1)\): first-order centered terms average to zero and the Hessian on that region is \(O(1/q)\), while the covariance trace is \(O(q)\). The same argument gives \(\mathbb E\sqrt{T+3}=\sqrt{2q/3}\,[1+O(q^{-1})]\). Consequently
\[
\frac{\sum D_q(k)}{\sum C_q(k)}=\sqrt{\frac3{2q}}+O(q^{-3/2}).
\]
Expanding \(R/(1+R)\) for this ratio \(R\) yields the stated two-term weighted-disconnection probability. Ordinary unweighted forest enumeration has exactly \(3^q\) disconnected forests and \(q3^{q-1}\) connected forests, giving \(3/(q+3)\).

**4. The intrinsic-index limit.** Conditionally on a connected-hub forest, \(K_q=2+T\) under the binomial law tilted by \(\sqrt{T+3}\). The tilt has total-variation distance \(O(q^{-1/2})\) from the untilted law: its normalized weight differs from one in expected absolute value by \(O(q^{-1/2})\), using binomial concentration and the Lipschitz bound for the square root on the central range. The total mass of disconnected-hub forests is itself \(O(q^{-1/2})\). The triangle inequality proves the claimed total-variation bound for the unconditional rank. The binomial central limit theorem, together with a bounded centering difference, proves the displayed normal limit.

## Verification

The standalone `check_k2q_intrinsic.py` reconstructs **every edge subset** of \(K_{2,q}\) for \(1\le q\le7\), rejects cyclic subsets, computes forest components, and independently checks both intrinsic-volume branches by rank and connectivity. For \(1\le q\le6\) it additionally computes the integer Gram determinant by Bareiss elimination and compares it to the component-size product for every forest. The executable output ends with `K2Q_INTRINSIC_PASS q=1..7`. This finite check is not used as a proof of the unrestricted formula. Separate numerical evaluation of the exact sums gives disconnection probabilities \(0.29289254\), \(0.22031037\), \(0.14912576\), \(0.10967314\), \(0.07990951\) at \(q=10,20,50,100,200\), consistent with the proved limit.

## Relationship to prior work

Graphical zonotopes, their generators, and their deformation cones are well established; the complete-bipartite case also arises naturally in shuffle constructions. The general projection/forest determinant formula is a standard geometric input, not claimed as new. Previously determined complete-bipartite total volume and facet-area information already covers the top two intrinsic-volume ranks and is not re-claimed as original here. What is new in the present statement, subject to historical priority verification, is the **joint exact expression of every intrinsic-volume coefficient** for this two-hub family together with the **geometrically weighted forest connectivity law**, its sharp square-root anomaly relative to uniform forests, and the normalized intrinsic-index law. The 2022 work on spanning-tree completions of bipartite forests counts completions rather than Euclidean forest wedge weights and does not imply these asserted statistical constants without new metric enumeration.

## Limitations

This is a result only for \(K_{2,q}\), not arbitrary bipartitions. The Gaussian approximation is given at the stated total-variation order, not as a local limit with explicit uniform errors. The probabilistic forest measure comes from the fixed unit Euclidean generators; changing all generator lengths changes the relative weights of intrinsic ranks. The priority comparison cannot exclude unpublished or unindexed equivalent formulas. No independent mathematical audit has been performed.

## References

- A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first public 2021-11-24; https://arxiv.org/html/2111.12422v2.
- M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053, first public 2022-09-24; https://arxiv.org/html/2209.12053v1.
- F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first public 2022-01-18; https://arxiv.org/abs/2201.06896.
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Journal of Graph Theory 101 (2022), 79–94; https://doi.org/10.1002/jgt.22812.
- E. Gover and N. Krikorian, *Determinants and the Volumes of Parallelotopes and Zonotopes*, Linear Algebra and its Applications 433 (2010), 28–40; https://doi.org/10.1016/j.laa.2010.01.033.
