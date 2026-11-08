# Price-sorted activation and exact spectral rates for pinned complete networks

## Finding

Let \(K_n\) be the unit-conductance complete graph, with \(n\ge 2\) vertices. A nonnegative pinning gain \(u_i\) at vertex \(i\) costs \(p_i u_i\), where every price \(p_i>0\), and the available budget is \(B>0\). The optimization is
\[
\Lambda(B)=\max_{u_i\ge 0,\ \sum_i p_i u_i\le B}\lambda_{\min}\!\bigl(L_{K_n}+\operatorname{diag}(u)\bigr).
\]
There is exactly one globally optimal vector \(u\). After sorting vertices so that \(p_1\le\cdots\le p_n\), gains become positive in nondecreasing price order and never disappear as \(B\) increases. The complete phase diagram is explicit in one scalar root per phase, with no symmetry assumption on the gain vector.

Define, for \(1\le q\le n\),
\[
T_q=\sum_{i=1}^{q}\sqrt{p_i},\qquad P_q=\sum_{i=1}^{q}p_i,
\]
and for \(1\le q<n\) the rate thresholds
\[
\ell_q=q-\frac{T_q}{\sqrt{p_{q+1}}},\quad \ell_0=0,\quad\ell_n=+\infty.
\]
These thresholds are nonnegative and nondecreasing. The optimal rate \(\lambda=\Lambda(B)>0\) is uniquely determined by \(F(\lambda)=B\), where, for any \(q<n\) satisfying \(\ell_{q-1}\le\lambda\le\ell_q\),
\[
F(\lambda)=(n-\lambda)\left(\frac{T_q^2}{q-\lambda}-P_q\right),
\]
and for \(\lambda\ge\ell_{n-1}\),
\[
F(\lambda)=T_n^2+(\lambda-n)P_n.
\]
On the \(q<n\) phase, the unique optimal gains are
\[
u_i=\begin{cases}
(n-\lambda)\left(\dfrac{T_q}{(q-\lambda)\sqrt{p_i}}-1\right),&i\le q,\\
0,&i>q.
\end{cases}
\]
On the final phase they are \(u_i=\lambda-n+T_n/\sqrt{p_i}\), for all \(i\). Formulae on adjacent closed phases agree at each boundary. A newly eligible gain is zero at its entry threshold; equal prices may activate together.

The sharp budget thresholds are \(\beta_0=0\), \(\beta_n=+\infty\) and
\[
\beta_q=(n-\ell_q)\left(T_q\sqrt{p_{q+1}}-P_q\right),\qquad 1\le q<n.
\]
Thus for \(\beta_{q-1}<B<\beta_q\) precisely the \(q\) cheapest vertices are pinned (with empty intervals permitted for tied prices). On each proper phase,
\[
F'(\lambda)=P_q+\frac{(n-q)T_q^2}{(q-\lambda)^2},\qquad
F''(\lambda)=\frac{2(n-q)T_q^2}{(q-\lambda)^3}>0.
\]
The derivatives of adjacent formulae match at every phase boundary. Consequently \(\Lambda(B)\) is strictly increasing, concave and continuously differentiable for \(B>0\), strictly concave before the final activation when that interval is nonempty, and exactly affine thereafter:
\[
\Lambda(B)=n+\frac{B-T_n^2}{P_n}\quad(B\ge\beta_{n-1}).
\]
In the final phase, the gain differences \(u_i-u_j=T_n(1/\sqrt{p_i}-1/\sqrt{p_j})\) are independent of the budget.

## Assumptions and scope

All vertices and edges of the complete graph are present; the edge conductances are exactly one, no masses or nonlinear device costs are introduced, and every vertex may be given an arbitrary nonnegative finite pinning gain. The prices and budget are arbitrary strictly positive real numbers. The eigenvalue uses the ordinary Euclidean inner product, and \(L_{K_n}=nI-\mathbf1\mathbf1^{\mathsf T}\). For \(B=0\), the trivially optimal allocation is the zero vector with rate zero; the theorem above concerns \(B>0\). Relabeling vertices with equal prices does not change the unique labeled optimal gain vector.

## Proof

**1. Exact eigenvalue feasibility.** Put \(\lambda>0\), \(s=n-\lambda\) and \(d_i=n+u_i-\lambda\). Then
\[
L_{K_n}+\operatorname{diag}(u)-\lambda I
=\operatorname{diag}(d_i)-\mathbf1\mathbf1^{\mathsf T}.
\]
For a positive-semidefinite matrix of this form, every \(d_i>0\): testing the \(i\)-th basis vector gives \(d_i\ge1\). Conversely, when \(d_i>0\), the congruence by \(\operatorname{diag}(d_i)^{-1/2}\) reduces positive semidefiniteness to
\[
\sum_{i=1}^{n}\frac1{d_i}\le1.
\]
Thus \(\lambda_{\min}\ge\lambda\) is equivalent to positive \(d_i\), \(d_i\ge s\), and the displayed reciprocal-sum inequality.

**2. Minimum cost for a target rate.** For fixed \(\lambda>0\), minimize \(\sum_i p_i(d_i-s)\) under those constraints. At a minimum the reciprocal-sum constraint is an equality. Indeed, if it were strict, one of the gains could be decreased, since all zero gains would give \(\sum_i1/(n-\lambda)>1\) when \(\lambda<n\); and if \(\lambda\ge n\), a positive gain can always be decreased while preserving strict feasibility. The Lagrange conditions give, for a single \(\eta>0\),
\[
d_i=\max\left\{s,\sqrt{\frac{\eta}{p_i}}\right\}\quad (s>0),
\]
and \(d_i=\sqrt{\eta/p_i}\) when \(s\le0\). Equivalently, if \(d_i>s\), then \(p_i=\eta/d_i^2\), while for \(d_i=s\), \(p_i\ge\eta/s^2\). Hence every positively pinned vertex has a price no larger than that of any unpinned vertex.

These conditions are globally sufficient and imply uniqueness. For any feasible competitor \(e_i\), strict convexity of the reciprocal function gives
\[
\sum_i\frac1{e_i}\ge\sum_i\left(\frac1{d_i}-\frac{e_i-d_i}{d_i^2}\right).
\]
Because both reciprocal sums are at most one and the optimal one equals one, \(\sum_i(e_i-d_i)/d_i^2\ge0\), strictly if \(e\ne d\). At inactive coordinates, \(e_i-d_i\ge0\), so the price inequalities imply
\[
\sum_i p_i(e_i-d_i)\ge\eta\sum_i\frac{e_i-d_i}{d_i^2}\ge0,
\]
with strict inequality whenever \(e\ne d\). Thus the optimum at every target rate is unique and globally least costly.

**3. Active-set solution.** Sort the prices. If the \(q<n\) cheapest indices are active, the other \(n-q\) denominators equal \(s=n-\lambda\). The equality constraint becomes
\[
\frac{T_q}{\sqrt\eta}+\frac{n-q}{s}=1,
\qquad
\sqrt\eta=\frac{sT_q}{q-\lambda}.
\]
Substitution gives precisely the gains and budget function in the finding. The inequalities for having the first \(q\) prices active and the remainder inactive reduce to \(\ell_{q-1}\le\lambda\le\ell_q\). The thresholds are ordered because
\[
\ell_{q+1}-\ell_q
=1-\frac{\sqrt{p_{q+1}}}{\sqrt{p_{q+2}}}
+T_q\left(\frac1{\sqrt{p_{q+1}}}-\frac1{\sqrt{p_{q+2}}}\right)\ge0.
\]
When all indices are active, the reciprocal constraint gives \(\sqrt\eta=T_n\), and hence the final affine formula. Its feasibility starts precisely at \(\ell_{n-1}=n-T_n/\sqrt{p_n}\).

**4. Budget inversion, smoothness, and rigidity.** The least-cost function \(F\) is continuous across activation thresholds, with \(F(0)=0\). Differentiation on every proper phase gives the positive derivative and second derivative stated above. At \(\ell_q\), both one-sided first derivatives equal \(P_q+(n-q)p_{q+1}\). On the final phase \(F'=P_n>0\). Therefore \(F\) is strictly increasing from zero to infinity, so \(F(\lambda)=B\) has exactly one solution. Its least-cost gains are feasible with budget exactly \(B\); any larger rate requires strictly more budget. The strict cost certificate in step 2 rules out every alternative optimal allocation, even one that breaks graph symmetries. Inverting the differentiable increasing convex function \(F\) gives the asserted regularity and strict concavity wherever \(q<n\).

**5. A concrete three-price transition.** For \(n=3\) and \((p_1,p_2,p_3)=(1,4,9)\), the entry rates are \(\ell_1=1/2\), \(\ell_2=1\), and the budget thresholds are \(\beta_1=5/2\), \(\beta_2=8\). One vertex is pinned below \(B=5/2\), two between \(5/2\) and \(8\), and all three above \(8\). In the final regime the optimal rate is \(\Lambda(B)=(B+6)/14\); at \(B=8\) the optimal gains are \((4,1,0)\), and at \(B=10\) they are \((29/7,8/7,1/7)\). These exact identities also provide simple checks for the endpoint conventions.

## Verification

The accompanying standard-library script `verify.py` constructs exact-rational active-set and rank-one certificates, checks both sides of phase boundaries and derivative matching exactly, and compares the derived optimum against independent random feasible gain allocations whose smallest eigenvalues are evaluated by the secular equation. Executing `python3 verify.py` reproduced 266 exact active-set certificates, 280 exact derivative/boundary checks, and 15,600 independent feasible-budget comparisons. These finite calculations corroborate the explicit formulas and certificates; they do not replace the all-parameter global proof.

## Relationship to prior work

The minimum eigenvalue of a pinned Laplacian as a convergence metric, and its semidefinite-optimization formulation, are established in earlier literature. Zhou and collaborators (2015) already formulate a linearly weighted gain constraint of the form \(\sum_i d_i w_i^\alpha=C\), with graph-importance-derived coefficients. Their paper gives an analytic solution for the uniform-coefficient case \(\alpha=0\) and numerical semidefinite solutions otherwise; on a complete graph intrinsic degree and betweenness do not generate arbitrary independent vertex prices. Jafarizadeh (2022) establishes analytical and algorithmic formulas for uniform total gain cost and several network families, including complete graphs; in particular, the all-vertices-pinned, equal-price optimum is already covered there. Liu and collaborators (2018) study selection of grounded vertices (infinite-gain pinning), which is a different optimization domain. The specific result established here is the finite-gain, **arbitrary independently priced** complete-graph classification: unique gain vector without an assumed support, ordered exact entry budgets, explicit piecewise algebraic rates, smooth transitions and final affine phase. It does not claim the general SDP formulation, uniform-price allocation or an arbitrary-graph optimizer as new.

## Limitations

The result concerns only unit-edge complete graphs, linear gain prices and continuous nonnegative gains. The theorem does not extend without further argument to heterogeneous edge weights, graph constraints other than completeness, bounded individual actuators, nonlinear costs, non-normal generators, discrete-time transient norms or infinite pinning. The numerical experiments cannot establish publication priority; specialist work on diagonal matrix loading or heterogeneous-cost pinning may overlap even if it was not located in the inspected sources.

## References

1. M.-Y. Zhou, Z. Zhuo, H. Liao, Z.-Q. Fu and S.-M. Cai, *Enhancing speed of pinning synchronizability: low-degree nodes with high feedback gains*, arXiv:1511.02012, first submitted 2015-11-06; published in *Scientific Reports* **5**, 17459 (2015). https://arxiv.org/abs/1511.02012 ; https://doi.org/10.1038/srep17459
2. S. Jafarizadeh, *Pinning Control of Dynamical Networks With Optimal Convergence Rate*, *IEEE Transactions on Systems, Man, and Cybernetics: Systems* **52** (2022), 7160–7172. https://doi.org/10.1109/TSMC.2022.3151222
3. H. Liu, X. Xu, J.-A. Lu, G. Chen and Z. Zeng, *Optimizing Pinning Control of Complex Dynamical Networks Based on Spectral Properties of Grounded Laplacian Matrices*, arXiv:1804.10818 (2018). https://arxiv.org/abs/1804.10818
