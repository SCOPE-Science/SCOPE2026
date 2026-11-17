# Sharp binomial boundary layers and exact surface area of two-row Monge polytopes

## Finding

For each integer \(q\ge2\), let \(\mathcal M_q\) consist of nonnegative real \(2\times q\) arrays \(C=(a_1,\ldots,a_q;b_1,\ldots,b_q)\) satisfying \(\sum_i(a_i+b_i)=1\) and \(a_i-b_i\le a_{i+1}-b_{i+1}\) for \(1\le i<q\). All measures use the Euclidean metric inherited from \(\mathbb R^{2q}\). Put
\[
V_q=\operatorname{Vol}_{2q-1}(\mathcal M_q)=\frac{\sqrt{2q}}{q!(2q-1)!},\qquad
h_q=(2q-1)\sqrt{\frac{2q-1}{2q}},
\]
and let \(B_q\sim\operatorname{Binomial}(q,1/2)\). The volume identity is previously known and serves only as normalization.

**Exact coordinate-facet boundary layer.** For every \(1\le i\le q\), let \(A_i\) and \(B_i^{\mathrm{fac}}\) be the facets given by \(a_i=0\) and \(b_i=0\), respectively. Their individual \((2q-2)\)-dimensional Euclidean areas satisfy
\[
\frac{\operatorname{Area}(A_i)}{V_q}=2h_q\Pr(B_q\ge i),\qquad
\frac{\operatorname{Area}(B_i^{\mathrm{fac}})}{V_q}=2h_q\Pr(B_q<i).
\]
Consequently \(\operatorname{Area}(A_i)+\operatorname{Area}(B_i^{\mathrm{fac}})=2h_qV_q\) for every column, the complete coordinate-facet area sum is \(2qh_qV_q\), and the largest-to-smallest \(A_i\)-facet area ratio is exactly \(2^q-1\).

**Exact comparison-facet sum and total area.** Let \(W_i\), \(1\le i<q\), be the distinct facets \(a_i-b_i=a_{i+1}-b_{i+1}\). Then
\[
\sum_{i=1}^{q-1}\frac{\operatorname{Area}(W_i)}{V_q}
=\frac{q(q-1)(2q-1)}2,
\]
and therefore the *entire* Euclidean boundary has the closed surface-to-volume ratio
\[
\boxed{\quad\frac{\operatorname{Area}(\partial\mathcal M_q)}{V_q}
=\frac{q(q-1)(2q-1)}2+2q(2q-1)\sqrt{\frac{2q-1}{2q}}.\quad}
\]
The \(q-1\) comparison facets constitute only \((q-1)/(3q-1)\) of the facets but carry fraction \(1-4/q+O(q^{-2})\) of the total surface area.

**Triangular and Gaussian facet profiles.** If \(1\le i_q<q\) and \(i_q/q\to u\in(0,1)\), then
\[
\frac{\operatorname{Area}(W_{i_q})}{q^2 V_q}\longrightarrow4\min\{u,1-u\}.
\]
If \(1\le j_q\le q\) and \(2(j_q-q/2)/\sqrt q\to t\in\mathbb R\), with \(\Phi\) the standard normal distribution function, then
\[
\frac{\operatorname{Area}(A_{j_q})}{h_q V_q}\longrightarrow2[1-\Phi(t)],\qquad
\frac{\operatorname{Area}(B_{j_q}^{\mathrm{fac}})}{h_q V_q}\longrightarrow2\Phi(t).
\]
In particular, the two types of boundary facet exhibit distinct macroscopic scales and profiles.

## Assumptions and scope

The positive Monge inequalities are precisely the displayed adjacent inequalities; their joint closure also enforces the nonadjacent ones. Each of the \(2q\) nonnegativity faces and \(q-1\) adjacent-comparison faces is a genuine facet for \(q\ge2\). All areas are relative-dimensional Euclidean measures in the hyperplane \(\sum_i(a_i+b_i)=1\), not coordinate projections or lattice-normalized volumes. Endpoints in the Gaussian scaling are interpreted only for ranks remaining in \(1,\ldots,q\). No arbitrary higher-row claim is made.

## Proof

**1. Exact volume and probability representation.** Take \(2q\) independent unit-rate exponential random variables \(X_i,Y_i\), let \(S=\sum_i(X_i+Y_i)\), and set \(a_i=X_i/S\), \(b_i=Y_i/S\). The normalized vector is uniform on the full \((2q-1)\)-simplex. The contrasts \(D_i=X_i-Y_i\) are i.i.d. standard Laplace with density \(f(t)=e^{-|t|}/2\) and cumulative distribution \(F\). The Monge event is exactly \(D_1\le\cdots\le D_q\), with probability \(1/q!\). Conditioning on it gives intrinsic-uniform distribution on \(\mathcal M_q\). The ambient probability simplex has Euclidean volume \(\sqrt{2q}/(2q-1)!\); hence the stated known \(V_q\).

**2. Coordinate facet slicing.** A coordinate-zero facet of the full probability simplex has area divided by the full simplex volume equal to \(h_q\). A normalized area fraction of a coordinate face lying in a Monge chamber equals the probability that the independent remaining exponential entries satisfy the ordering condition. On \(a_i=0\), the unnormalized contrast is \(D_i=-Y_i\), where \(Y_i\) remains unit exponential, and so \(U=F(D_i)=e^{-Y_i}/2\) is *uniform on* \((0,1/2)\). For the other \(q-1\) independent Laplace contrasts, conditioned on \(U=u\), the probability of the prescribed order is
\[
\frac{u^{i-1}(1-u)^{q-i}}{(i-1)!(q-i)!}.
\]
Its average is \(2\int_0^{1/2}u^{i-1}(1-u)^{q-i}\,du/[(i-1)!(q-i)!]\). Dividing by the chamber-volume probability \(1/q!\) and using the regularized-beta/binomial identity gives \(2\Pr(B_q\ge i)\). Multiplication by \(h_q\) proves the first coordinate formula. The reflection \((a_i,b_i,i)\mapsto(b_{q+1-i},a_{q+1-i},q+1-i)\) proves the second, using complementarity of the binomial tails. All coordinate consequences follow by summing and taking \(i=1,q\).

**3. Exact comparison-wall coarea.** Write \(g_i=(a_{i+1}-b_{i+1})-(a_i-b_i)=(D_{i+1}-D_i)/S\). Its intrinsic Euclidean normal has length \(2\). If \(f_{g_i\mid\mathcal M_q}(0+)\) denotes the interior one-sided density of its slack under uniform volume, elementary coarea gives \(\operatorname{Area}(W_i)/V_q=2f_{g_i\mid\mathcal M_q}(0+)\). The change of variables from the unnormalized gap to \(g_i\) multiplies its delta density by \(S\). Given a complete set of contrasts \(D_j\), exponential splitting gives \(\mathbb E(S\mid D_1,\ldots,D_q)=q+\sum_j|D_j|\). At the equality \(D_i=D_{i+1}=t\), the two colliding contrasts contribute \(2|t|\). Count the orderings of the remaining contrasts to obtain the exact individual formula. If \(Z_{(1)}\le\cdots\le Z_{(q-1)}\) are the order statistics of \(q-1\) independent standard Laplace variables, then
\[
\boxed{\quad
\frac{\operatorname{Area}(W_i)}{V_q}
=2q\,\mathbb E\left[f(Z_{(i)})\left(q+\sum_{j=1}^{q-1}|Z_j|+|Z_{(i)}|\right)\right].\quad}
\]
This identity determines each comparison-facet area by a finite-dimensional elementary expectation (equivalently, a one-dimensional integral over the \(i\)-th order-statistic density with two truncated first moments). It is derived from the one-sided density of a genuine interior slack, so no factor of two from a two-sided tie convention is inserted.

**4. Sum exactly.** Sum the preceding identity over \(i=1,\ldots,q-1\). Sorting preserves the multiset of Laplace observations. For independent standard Laplace \(Z,Z'\), use
\[
\mathbb E f(Z)=\frac14,\quad
\mathbb E[|Z|f(Z)]=\frac18,\quad
\mathbb E|Z|=1.
\]
With \(n=q-1\), the expectation of the summed terms is
\[
qn/4+n/8+n(n-1)/4+n/8=n(2q-1)/4.
\]
Multiplying by \(2q\) gives \(q(q-1)(2q-1)/2\), as claimed. The facets already enumerated exhaust all codimension-one faces; this also proves the full surface formula.

**5. Two different limits.** Fix \(0<u<1\), and let \(i_q/q\to u\). The Laplace order statistic \(Z_{(i_q)}\) converges in probability to \(F^{-1}(u)\). Thus \(f(Z_{(i_q)})\to\min(u,1-u)\). Also \(q^{-1}\sum_{j=1}^{q-1}|Z_j|\to1\) in \(L^1\), and \(q^{-1}|Z_{(i_q)}|\to0\) in \(L^1\). Boundedness of \(f\), integrability of \(|Z|\), and the standard logarithmic bound for Laplace order-statistic magnitudes justify passage through expectations. Divide the formula of step 3 by \(q^2\) to get \(4\min(u,1-u)\). The coordinate profile follows directly from the classical central limit theorem for \(\operatorname{Binomial}(q,1/2)\). Finally, comparison-facet area has order \(q^3V_q\) in aggregate, whereas coordinate facets have total area \(4q^2V_q(1+O(q^{-1}))\). Their ratio is \(4/q+O(q^{-2})\), giving the area-condensation statement.

## Verification

The reproducibility file `verify_monge_boundary.py` reconstructs the complete known list of vertices of \(\mathcal M_q\) and computes the intrinsic Euclidean volume of each facet with singular-value orthonormalization and independent convex-hull triangulation. Its run checked all \(24\) coordinate/comparison facets for \(q=2,3,4,5\) and their exact global normalization. It additionally checked rational binomial complementarity, extreme-facet ratios, and aggregate formulas for every \(2\le q\le100\), reporting `MONGE_BOUNDARY_PASS direct_facets=38 exact_dimensions=2..100`. The attached `requirements.txt` specifies the numerical dependencies. Finite calculations corroborate the analytic proof but are not substitutes for its general or limit arguments.

## Relationship to prior work

Erickson and Kretschmann's *The structure and normalized volume of Monge polytopes* (first public version November 13, 2023) gives the original Monge-polytope model, vertices/facets and normalized volume; these are used here and are **not** new results. Published work on uniform two-row Monge polytopes also supplies the sorted-Laplace/exponential representation and studies volume-uniform limit shapes and Gumbel extremes. Other related work gives exact centroids and logarithmic entry profiles. The present claim is instead the *Euclidean boundary area measure*, with all coordinate-facet areas, an exact comparison-facet sum and complete surface area, and distinct Gaussian-versus-triangular facet profiles. Neither the known volume nor the probability sampler by itself states the coarea and size-biased boundary formulas. Relevant full texts were checked for claim-level implication, not only titles; historical priority is nevertheless provisional, particularly for independently derived facet-area specializations.

## Limitations

The all-dimensional formulas apply only to two-row normalized Monge polytopes with the displayed metric and orientation. The individual comparison-facet areas are given by an exact expectation, not a simplified elementary closed form, although their total and bulk limit are explicit. The Gaussian statement is a weak limit for the coordinate index in a \(\sqrt q\)-window; it is not a uniform error estimate for all ranks. Unindexed or inaccessible mathematically equivalent literature remains a historical-priority risk. No independent validation has been carried out.

## References

1. William Q. Erickson and Jan Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first public version November 13, 2023. https://arxiv.org/abs/2311.07522 .
2. *Uniform two-row Monge polytopes have a Laplace limit shape and independent Gumbel edges*, published October 18, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-uniform-two-row-monge-polytopes-have-a-laplace-limit-shape-and-i--7c7e590d3b3c/RESULT.md .
3. *Exact centroids and logarithmic edge profiles of two-row Monge polytopes*, published November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-centroids-and-logarithmic-edge-profiles-of-two-row-monge-p--20e8b8de7493/RESULT.md .
4. William Q. Erickson and Nicholas B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, first public version September 8, 2026. https://arxiv.org/abs/2609.09508 .
