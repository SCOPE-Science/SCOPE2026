# Positive connectivity correlations on every weighted cactus random-cluster graph

## Finding

**Theorem.** Let \(G=(V,E)\) be any finite connected simple cactus graph (every edge belongs to at most one simple cycle). Fix \(q>0\) and positive edge weights \(z_e>0\). Draw \(A\subseteq E\) with probability proportional to \(q^{k_G(A)}\prod_{e\in A}z_e\), where \(k_G(A)\) counts components of the spanning subgraph \((V,A)\). For every four vertices \(a,b,c,d\), let \(E_{ab}\) and \(E_{cd}\) be their respective connectivity events in \((V,A)\). Then

\[
\operatorname{Cov}(\mathbf1_{E_{ab}},\mathbf1_{E_{cd}})\ge0.
\]

If \(a\ne b\) and \(c\ne d\), the inequality is **strict** precisely when the unique block-cut-tree routes from \(a\) to \(b\) and from \(c\) to \(d\) traverse a common nontrivial block (bridge edge or cycle). If the routes have no common block, the two indicators are independent. When either pair consists of the same vertex, its indicator is identically one and the covariance is zero.

The same assertions hold for the weighted spanning-forest (*arboreal gas*) law \(\Pr(F)\propto\prod_{e\in F}\lambda_e\), with \(F\subseteq E\) acyclic and every \(\lambda_e>0\). In particular this proves the connectivity-correlation inequality on cacti throughout the full nonuniform-weight regime \(0<q<1\) and its forest limit.

## Assumptions and scope

Graphs are finite, connected, simple, and cactus. All edge weights are strictly positive and finite. Repeated marked vertices are permitted; the strictness statement concerns only two nontrivial vertex pairs. The finite cactus has a block-cut tree whose blocks are either individual bridges or chordless cycles, possibly sharing articulation vertices but not edges. The arboreal-gas law ranges over *all* spanning forests, not just spanning trees. No claim is made for general graphs with overlapping cycles.

## Proof

**1. Independent block laws.** Let \(\mathcal B\) be the set of nontrivial blocks. For every edge set \(A\), writing \(A_B=A\cap E(B)\), the articulation-block identity is

\[
k_G(A)=\sum_{B\in\mathcal B}k_B(A_B)-(|\mathcal B|-1).
\]

Indeed every block gluing identifies one common vertex and subtracts exactly one component from the sum, for all edge selections. Consequently the random-cluster measure factors as the product of its block measures. The demand \(a\leftrightarrow b\) is equivalent to requiring the two entry/exit vertices to connect inside *every* block of the unique route between \(a\) and \(b\) in the block-cut tree. Within a block that is absent from a demand's route, its local factor is identically one.

**2. Bridges.** A bridge block has its edge open with probability \(z_e/(q+z_e)\in(0,1)\). Its only nontrivial two-terminal connectivity event is the edge-open indicator, with strictly positive variance. Thus any two local demands within the same bridge have strictly positive covariance.

**3. Cycle reduction.** For a cycle with edge weights \(z_e\), consider independent Bernoulli edges with probabilities \(p_e=z_e/(q+z_e)\). Relative to this product law, the random-cluster law multiplies the *all-open* configuration by \(q\), leaving every other configuration's relative weight unchanged: the cycle rank is one exactly when every edge is open.

The endpoints of the two nontrivial terminal-pair demands divide the cycle into \(m\in\{2,3,4\}\) nonempty consecutive arcs (with shared endpoints reducing \(m\)). The \(i\)th arc is fully open with independent product-law probability \(P_i=\prod_{e\in\mathrm{arc}_i}p_e\); define its positive odds of being not fully open by

\[
r_i=\frac{1-P_i}{P_i}=\prod_{e\in\mathrm{arc}_i}(1+q/z_e)-1>0.
\]

For a set \(I\subseteq\{0,\ldots,m-1\}\) of arcs that are **not** fully open, remove the common positive normalization \(\prod_iP_i\). Its remaining weight is \(q\) if \(I=\varnothing\) and \(\prod_{i\in I}r_i\) otherwise. Every marked-terminal connection is determined by this set \(I\), since the marked vertices form a cycle whose arc-edges are open precisely outside \(I\).

Write \(Z_0=\sum_{I\ne\varnothing}\prod_{i\in I}r_i\), and write \(A_0,B_0,C_0\) for the same weighted sums restricted, respectively, to the first demand, the second demand, and their intersection. The covariance equals

\[
\frac{(q+C_0)(q+Z_0)-(q+A_0)(q+B_0)}{(q+Z_0)^2}
=\frac{R_0+qW_0}{(q+Z_0)^2},
\]

where \(R_0=C_0Z_0-A_0B_0\) and \(W_0=Z_0+C_0-A_0-B_0\ge0\); the latter is the total weight of nonempty configurations in which *neither* connection event holds.

**4. Complete cycle inequalities.** Up to reversing or rotating the cycle and exchanging demands, precisely four endpoint-interlacement types remain. In each formula below the arcs are indexed consecutively and \(r_i>0\). Direct enumeration of the nonempty subsets \(I\) gives:

- **Two distinct endpoints, identical pair:** \(R_0=r_0r_1(r_0+r_1)>0\).
- **Three endpoints, with demands \((0,1)\) and \((1,2)\):**
  \[
  R_0=r_0r_1\big[(r_0+r_1)(1+r_2)+r_2\big]>0.
  \]
- **Four endpoints, nonalternating demands \((0,1)\) and \((2,3)\):**
  \[
  R_0=r_0r_2\big[(1+r_0+r_2)(1+r_1)(1+r_3)-1\big]>0.
  \]
- **Four endpoints, alternating demands \((0,2)\) and \((1,3)\):** putting \(S=r_0+r_1+r_2+r_3\),
  \[
  R_0=(r_0r_2+r_1r_3)\big[S+(r_0+r_2)(r_1+r_3)\big]
       +r_0r_1r_2r_3(4+S)>0.
  \]

Thus every pair of nontrivial connectivity demands within one cycle block has *strictly* positive covariance, for arbitrary \(q>0\) and positive heterogeneous edge weights.

**5. Assembling the cactus and equality.** For each block \(B\), let \(X_B,Y_B\in\{0,1\}\) represent the connection needed by the respective global demands, taking an absent local requirement to be the constant one. Block independence gives

\[
\Pr(E_{ab}\cap E_{cd})=\prod_B\mathbb E[X_BY_B],\qquad
\Pr(E_{ab})\Pr(E_{cd})=\prod_B\mathbb E[X_B]\mathbb E[Y_B].
\]

Each block term on the left is at least its right counterpart. Every factor is strictly positive under positive weights; a factor inequality is strict exactly when both demands traverse the same block. This proves both the correlation inequality and the sharp independence criterion.

**6. Weighted forest law and strictness.** Put \(z_e=q\lambda_e\) and send \(q\downarrow0\). For each edge set \(A\),

\[
q^{k_G(A)}\prod_{e\in A}q\lambda_e
=q^{|V|+\beta_1(A)}\prod_{e\in A}\lambda_e,
\]

where \(\beta_1(A)=|A|-|V|+k_G(A)\) is the cycle rank. Only forests survive after dividing by \(q^{|V|}\). In every bridge block, the limiting open probability is \(\lambda_e/(1+\lambda_e)\in(0,1)\). On cycles, \(r_i\to\prod_{e\in\mathrm{arc}_i}(1+1/\lambda_e)-1>0\), while the all-open weight \(q\to0\). The displayed strictly positive \(R_0\) polynomials therefore persist in the forest limit, proving strictness rather than merely nonnegativity.

## Verification

The two attached standard-library Python programs `verify_polynomials.py` and `verify_cactus_finite.py` are diagnostic checks. Run `python verify_polynomials.py` to independently expand and compare the four multivariate polynomial identities and establish coefficientwise nonnegativity of the residual; the script reports 20 passed symbolic assertions. Run `python verify_cactus_finite.py` to enumerate finite edge subsets with exact rational weights for cycles of orders 3–6 and two multicycle cactus test graphs; it reports 9,452 passed covariance assertions. Both programs use no external packages. The infinite family of graphs, all positive real weights, and the strictness classification are proved by the preceding algebra, not established by finite testing.

## Relationship to prior work

Çiçeksiz and Ravichandran (2026, arXiv:2610.00549v1) explicitly study positive correlations between two connectivity events and conjecture the unrestricted arboreal-gas and \(0<q<1\) inequalities. Their proven high-fugacity results do not imply the uniform all-weight cactus conclusion; their graph-wide conjecture would imply its nonnegative component, but does not provide the strict equality criterion. The present argument uses cactus block factorization and an explicit four-case cycle polynomial classification. Classical FKG positive association already treats \(q\ge1\); the scientifically new regime addressed here is \(0<q<1\) and forests.

Grimmett and Winkler's uniform-forest work concerns negative correlation between *edge* indicators rather than covariance of arbitrary vertex-pair connectivity events. Recent wired-tree results concern branch negative dependence, again a different event geometry. The general random-cluster measure and its tree specializations are not new here.

## Limitations

This is a pairwise covariance theorem for two vertex-connectivity events, not joint association for an arbitrary family of events or edge-indicator positive association. A cactus condition excludes any graph where an edge lies in more than one cycle. The strictness statement needs positive finite weights, connectedness, and nontrivial terminal pairs. Historical priority beyond the identified works is provisional; a general published implication for all cactus connection events, if located, would supersede this classification. No independent audit has been performed.

## References

- Recep Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549v1 (first public date 2026-09-30), https://arxiv.org/abs/2610.00549.
- Geoffrey R. Grimmett and Stan N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185, https://arxiv.org/abs/math/0302185.
- Heehyun Park, *The \(q<1\) Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence*, arXiv:2608.08565, https://arxiv.org/abs/2608.08565.
