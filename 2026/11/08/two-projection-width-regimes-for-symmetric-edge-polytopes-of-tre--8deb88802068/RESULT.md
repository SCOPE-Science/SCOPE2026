# Two projection-width regimes for symmetric edge polytopes of trees

## Finding

For a finite connected simple graph \(G\) with \(n\ge2\) vertices and \(m\) edges, define its Euclidean symmetric edge polytope in the intrinsic \((n-1)\)-space \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\) by
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G)\}.
\]
Let \(W_G\) denote the length of its projection onto a Haar-uniform one-dimensional direction in \(H\). All edge vectors have length \(\sqrt2\); no graph-dependent rescaling is made. Let \(\Phi\) and \(\varphi\) denote the standard Gaussian distribution function and density.

**Sparse-dependence regime.** For any sequence of connected simple graphs with \(n\to\infty\), \(m=m_n\to\infty\), and maximum degree \(\Delta_n=o(m_n^{1/3})\), put
\[
q_m=\Phi^{-1}(1-1/(2m)),\qquad b_m=\sqrt2\,q_m.
\]
Then
\[
\boxed{\frac{b_m}{2}\left(\frac{\sqrt{n-1}}2W_G-b_m\right)\ \xrightarrow{d}\ \mathcal G,}
\]
where \(\Pr(\mathcal G\le t)=\exp(-e^{-t})\). If the graph degrees are uniformly bounded, convergence also holds for the first two moments of the variable displayed on the left, and
\[
\boxed{\frac{(n-1)b_m^2}{16}\operatorname{Var}(W_G)\longrightarrow\frac{\pi^2}{6}.}
\]
In particular, for path graphs on \(n\) vertices,
\[
\boxed{n\log n\,\operatorname{Var}(W_G)\longrightarrow\frac{2\pi^2}{3}.}
\]

**Fixed-hub regime.** Fix an integer \(k\ge1\) and a tree \(T\) on \(k\) labeled vertices. Attach \(\ell_{j,m}\) distinct new leaves to its vertex \(j\), where \(m=\sum_{j=1}^k\ell_{j,m}\to\infty\) and \(\ell_{j,m}/m\to\rho_j>0\) for every \(j\). The resulting tree has \(n=m+k\) vertices. Put \(a_m=\Phi^{-1}(1-1/m)\) and let \(Z_1,\ldots,Z_k\) be independent standard Gaussians. Then
\[
\boxed{\frac{\sqrt{n-1}}2W_G-a_m\xrightarrow{d}H_k:=\max_{1\le j\le k}|Z_j|.}
\]
The convergence holds for the first two moments. Its limit law is
\[
\Pr(H_k\le t)=\begin{cases}(2\Phi(t)-1)^k,&t\ge0,\\0,&t<0,\end{cases}
\]
and the exact asymptotic width variance is
\[
\boxed{\frac{n-1}{4}\operatorname{Var}(W_G)\longrightarrow v_k:=\operatorname{Var}(H_k)>0.}
\]
Here \(v_k=2\int_0^\infty t[1-(2\Phi(t)-1)^k]dt-\big(\int_0^\infty[1-(2\Phi(t)-1)^k]dt\big)^2\). In particular,
\[
\boxed{v_1=v_2=1-2/\pi,}
\]
although \(H_1\) and \(H_2\) have different distributions. Hence stars and balanced double stars have distinct non-Gaussian limiting laws but the same leading width-variance coefficient.

All tree symmetric edge polytopes on \(n\) vertices are combinatorially \((n-1)\)-crosspolytopes. The contrast between the Gumbel path law at fluctuation scale \((n\log n)^{-1/2}\) and the hub laws at scale \(n^{-1/2}\) therefore cannot be read from the face lattice.

**Exact finite-size moments in the hub family.** Let \(S_G=\max_{\{i,j\}\in E(G)}|X_i-X_j|\) for independent standard Gaussians \(X_i\). For a hub-core tree as above, its distribution function \(F_S(r)=\Pr(S_G\le r)\), for \(r\ge0\), is the \(k\)-dimensional integral
\[
F_S(r)=\int_{\mathbb R^k}\!\prod_{j=1}^k\varphi(z_j)
\prod_{\{i,j\}\in E(T)}\mathbf1_{\{|z_i-z_j|\le r\}}
\prod_{j=1}^k[\Phi(z_j+r)-\Phi(z_j-r)]^{\ell_{j,m}}\,dz.
\]
For every real \(p>0\), its exact Haar-width moment is
\[
\boxed{\mathbb EW_G^p=\frac{2^p\,p\int_0^\infty r^{p-1}(1-F_S(r))\,dr}
{2^{p/2}\Gamma((n-1+p)/2)/\Gamma((n-1)/2)}.}
\]
These bounded-width moments determine the finite-dimensional width law.

## Assumptions and scope

All graphs are finite, simple and connected, without weights or repeated edges. Projection directions are uniform in the intrinsic zero-sum Euclidean space, and the edge vectors are exactly \(e_i-e_j\). In the first regime the maximum-degree condition is applied to edge counts \(m_n\), not to vertex counts. Moment convergence in that regime is asserted only when maximum degree is bounded by one constant; distributional convergence allows the stated growing-degree range. In the second regime \(k\) and the core tree are fixed, and every leaf proportion has a strictly positive limit. The finite-size formulas concern these fixed-core trees, not arbitrary graphs with a growing core.

## Proof

**1. Exact Gaussian representation.** Let \(X=(X_1,\ldots,X_n)\) have independent standard-normal entries, and write \(R=\|X-\bar X\mathbf1\|_2\). Its centered direction \(U=(X-\bar X\mathbf1)/R\) is uniform in \(H\), independent of \(R\), and \(R^2\) has the \(\chi^2_{n-1}\) distribution. Symmetry of \(P_G\) and its vertex support imply the samplewise identity
\[
W_G=\frac{2S_G}{R},\qquad S_G=\max_{\{i,j\}\in E(G)}|X_i-X_j|.
\]
The independent radial factor also gives \(\mathbb E S_G^p=\mathbb ER^p\,\mathbb EW_G^p/2^p\), with
\[
\mathbb ER^p=2^{p/2}\frac{\Gamma((n-1+p)/2)}{\Gamma((n-1)/2)}.
\]
Conditioning on the \(k\) core Gaussian entries makes the attached-leaf events independent and gives the displayed \(F_S\) integral. Integrating \(p r^{p-1}\Pr(S_G>r)\) proves the exact moments.

**2. Rare exceedances on a sparse graph.** Orient the edges arbitrarily and put \(Y_e=(X_i-X_j)/\sqrt2\). Every \(Y_e\) is standard normal. Disjoint edges yield independent variables, and distinct edges with one shared endpoint have correlation \(\pm1/2\). For fixed \(t\in\mathbb R\), let \(u_m=q_m+t/q_m\) and let \(N_m=\sum_e\mathbf1_{\{|Y_e|>u_m\}}\). Normal-tail ratios imply \(\mathbb EN_m=2m\overline\Phi(u_m)\to e^{-t}\).

For any adjacent pair of edges, choose signs for their two Gaussian variables. The signed pair has correlation \(\rho\in\{-1/2,1/2\}\). Integrating its bivariate normal density over \([u_m,\infty)^2\), by translating both coordinates and dropping the nonnegative remainder of the exponent, gives uniformly for \(u_m\ge1\)
\[
\Pr(|Y_e|>u_m,|Y_f|>u_m)\le C u_m^{-2}\exp(-2u_m^2/3).
\]
Indeed the exponent at the corner is \(u_m^2/(1+\rho)\ge2u_m^2/3\), and its two positive linear terms each have coefficient at least \(2u_m/3\). There are at most \(2m(\Delta_n-1)\) ordered adjacent edge pairs. In the dependency-neighborhood Poisson approximation of Arratia, Goldstein and Gordon (1989, Theorem 1), the independent-outside-neighborhood term vanishes. The other two error sums obey
\[
B_1=O(\Delta_n/m),\qquad
B_2=O\big(\Delta_n m^{-1/3}(\log m)^{-1/3}\big),
\]
using \(q_m^2=2\log m-\log\log m+O(1)\). Both vanish under \(\Delta_n=o(m^{1/3})\). Consequently \(\Pr(N_m=0)\to\exp(-e^{-t})\), equivalent to
\[
\frac{b_m}{2}(S_G-b_m)\xrightarrow{d}\mathcal G.
\]
The event indicators for edges separated by a vertex are not independent; only vertex-disjoint edge sets are used as independent dependency blocks.

**3. Intrinsic radial normalization.** Since \(m\le\binom n2\), \(b_m^2=O(\log n)\). The normal maximum satisfies \(S_G=O_{\Pr}(b_m)\), while \(\sqrt{n-1}/R-1=O_{\Pr}(n^{-1/2})\). Therefore
\[
\frac{b_m}{2}\left(\frac{\sqrt{n-1}}2W_G-S_G\right)
=O_{\Pr}((\log n)/\sqrt n)=o_{\Pr}(1),
\]
which proves the first distributional limit.

**4. Second moments for bounded degrees.** Suppose \(\Delta_n\le D\). A greedy matching contains at least \(m/(2D-1)\) pairwise vertex-disjoint edges. If \(V_m=\frac{b_m}{2}(S_G-b_m)\), the union bound and the Gaussian hazard bound give \(\Pr(V_m>t)\le e^{-t}\) for \(t\ge0\). For \(0\le t\le q_m^2/2\), the independent matching and the same normal hazard bound give \(\Pr(V_m<-t)\le\exp(-c_D e^{t/2})\). For \(q_m^2/2<t\le q_m^2\), the lower-tail probability is at most \(\exp(-c_Dm^{2/3})\) for sufficiently large \(m\); it is zero beyond \(q_m^2\). These estimates provide uniform integrability of \(V_m^2\). Hence \(\mathbb EV_m\to\gamma\) and \(\operatorname{Var}(V_m)\to\pi^2/6\).

Put \(d=n-1\) and \(T_G=\sqrt d\,W_G/2\). Radial independence gives exactly
\[
\mathbb ET_G=\frac{\sqrt d}{\mathbb ER}\,\mathbb ES_G,
\qquad \mathbb ET_G^2=\mathbb ES_G^2.
\]
Since \(\sqrt d/\mathbb ER=1+O(d^{-1})\) and \(\mathbb ES_G^2=O(\log m)\), the discrepancy between the variances of the corresponding normalized Gaussian and Haar variables is \(O((\log m)^2/n)\). This proves moment convergence and the bounded-degree variance formula. On paths, \(m=n-1\) and \(b_m^2\sim4\log n\), giving the stated constant.

**5. The fixed-hub law and moments.** Let \(M_j^+\) and \(M_j^-\) be the largest and negative-smallest Gaussian among the leaves at hub \(j\). For every fixed \(j\), the positive leaf fraction implies \(M_j^+-a_m\to0\) and \(M_j^--a_m\to0\) in \(L^2\) (standard Gaussian extreme-value moment bounds and \(a_{\ell_{j,m}}-a_m\to0\)). Consequently the largest leaf-edge difference is
\[
\max_{1\le j\le k}\max(M_j^+-X_j,\,M_j^-+X_j)
=a_m+\max_{1\le j\le k}|X_j|+o_{L^2}(1).
\]
The finitely many core-edge differences have bounded second moments, so their contribution to this maximum tends to zero in \(L^2\). Hence \(S_G-a_m\to H_k\) in \(L^2\). The radial identity in step 1, \(\sqrt d/\mathbb ER=1+O(d^{-1})\), and \(a_m^2=O(\log n)\) give the asserted Haar distribution and first-two-moment limits and their variance formula.

**6. Equal first and second hub variances.** For \(k=1\), \(H_1=|Z_1|\), so \(\operatorname{Var}(H_1)=1-2/\pi\). For \(k=2\), apply polar coordinates to two independent Gaussians: the independent radius has first and second moments \(\sqrt{\pi/2}\) and \(2\), while the angular factor \(\max(|\cos\Theta|,|\sin\Theta|)\) has moments \(2\sqrt2/\pi\) and \(1/2+1/\pi\). Thus \(\mathbb EH_2=2/\sqrt\pi\), \(\mathbb EH_2^2=1+2/\pi\), and \(\operatorname{Var}(H_2)=1-2/\pi\). Their cumulative distribution functions are different. A tree's \(n-1\) edge-root columns are linearly independent (delete a leaf inductively), so the convex hull of their positive and negative copies is a linear image of the standard \((n-1)\)-crosspolytope. This establishes the combinatorial comparison.

## Verification

Run `python verify_width_regimes.py` with NumPy and SciPy. It checks the exact root support and full-rank incidence descriptions for small path and star trees; verifies the fixed-core maximum reduction, the finite Gaussian star CDF integral, and the exact \(k=2\) moment identities; then tests the predicted Gaussian hub coupling and the Gumbel CDF on seeded larger samples. The expected final output line is `ROOT_POLYTOPE_WIDTH_REGIME_CHECKS_PASSED`. These are finite corroborative checks; the asymptotic assertions follow from the analytical bounds above.

## Relationship to prior work

Braun and Bruegge (2022) study facet counts of symmetric edge polytopes and explicitly note that all tree instances are combinatorial crosspolytopes. D'Alì, Juhnke-Kubitzke and Koch (2023) show that their lattice classes are controlled by graphical matroids, which does not preserve the inherited Euclidean metric. Kabluchko, Litvak and Zaporozhets (2015) establish projection-width laws for *regular* Euclidean simplices and crosspolytopes, whose Gaussian support coordinates have a different dependence structure. Arratia, Goldstein and Gordon (1989) provide the general Poisson approximation theorem used here; the graph-dependent covariance bound and the fixed-hub geometry are separately established in this proof. The published study of width variance for *graphical zonotopes* addresses Minkowski sums, whose support functions add edge contributions rather than take their maximum. No covering formula or pair of regimes for these root-polytope widths was identified in the inspected sources; that priority assessment is provisional.

## Limitations

The lower-degree threshold \(\Delta_n=o(m^{1/3})\) is a sufficient condition, not asserted optimal. Under this growth condition the theorem proves weak convergence only, not moment convergence. Second-moment convergence in the first regime is proved for uniformly bounded degrees. The fixed-hub law assumes a fixed core and positive limiting leaf fractions, and does not describe intermediate numbers of hubs or vanishing leaf proportions. The exact finite-size integral is not claimed for growing cores. The construction is Euclidean and unweighted, and the results do not extend automatically to lattice-equivalent but non-isometric realizations. Literature priority is not independently certified.

## References

1. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, first public arXiv version 2022-01-31, arXiv:2201.13303, https://arxiv.org/abs/2201.13303.
2. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a Generalization of Symmetric Edge Polytopes to Regular Matroids*, arXiv:2307.04933 (2023-07-10), https://arxiv.org/abs/2307.04933.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479 (2015-11-26), https://arxiv.org/abs/1511.08479.
4. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25, https://doi.org/10.1214/aop/1176991491.
