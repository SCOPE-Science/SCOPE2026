# Exact Crofton complexity and two-scale asymptotics for cross-polytope sections

## Finding

Let \(d\ge3\) and let \(C_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d\) be the regular cross-polytope. Sample an unoriented affine hyperplane using Euclidean-motion-invariant hyperplane measure, conditioned on meeting \(C_d\). Almost surely its intersection is a \((d-1)\)-polytope; write \(V_d\) for the number of vertices of this intersection. Let \(H_1,\ldots,H_d\) be independent absolute standard normal random variables, with increasing order statistics \(H_{(1)}<\cdots<H_{(d)}\), and set \(H_{(0)}=0\), \(m_d=\mathbb E H_{(d)}\), and \(v_d(k)=k(2d-k-1)\).

**Exact law.** For every \(k=1,\ldots,d\), the contribution of the interval indexed by \(k\) has probability
\[
\Pr\{K_d=k\}=\frac{\mathbb E[H_{(d-k+1)}-H_{(d-k)}]}{m_d},\qquad V_d=v_d(K_d).
\]
In particular, \(v_d(d-1)=v_d(d)=d(d-1)\), so these two probabilities must be added for the maximum vertex count. For any threshold \(h\) with \(v_d(1)\le h<v_d(d)\), put \(k_*(h)=\min\{k:v_d(k)>h\}\). Then
\[
\Pr\{V_d>h\}=\frac{\mathbb E H_{(d-k_*(h)+1)}}{m_d}.
\]
The mean has the exact form
\[
\boxed{\mathbb E V_d=\frac{2d(d-1)}{\sqrt\pi\,m_d}.}
\]

**Two distinct asymptotic scales.** As \(d\to\infty\),
\[
\boxed{\frac{\log V_d}{\log d}-1\ \Longrightarrow\ \operatorname{Beta}(1,\tfrac12).}
\]
Its limiting CDF is \(1-\sqrt{1-x}\) for \(0\le x\le1\). Yet for each fixed \(0<x<1\), the probability of genuinely quadratic-scale complexity is only of logarithmically small order:
\[
\boxed{\sqrt{2\log d}\,\Pr\!\left\{\frac{V_d}{d^2}>x\right\}\longrightarrow
\sqrt2\,\operatorname{erf}^{-1}(\sqrt{1-x}).}
\]
For every fixed real \(s>0\), the complete positive-moment asymptotic is
\[
\boxed{\sqrt{2\log d}\;\mathbb E\left(\frac{V_d}{d^2}\right)^s\longrightarrow
\int_0^\infty\!\left[1-\operatorname{erf}(t/\sqrt2)^2\right]^s\,dt.}
\]
At \(s=1\), the integral is \(2/\sqrt\pi\); hence
\[
\mathbb E V_d\sim\sqrt{\frac2\pi}\,\frac{d^2}{\sqrt{\log d}}.
\]
The sharp distinction between the beta-typical polynomial exponent and rare quadratic-scale contributions explains why this mean cannot be inferred by treating the limiting beta law as an ordinary integrable limit.

**Three-dimensional exact check.** For the regular octahedron, sections are almost surely quadrilaterals or hexagons and
\[
\Pr\{V_3=6\}=\frac{\pi}{2\arctan(1/\sqrt2)}-2=0.552149656\ldots,\qquad
\Pr\{V_3=4\}=1-\Pr\{V_3=6\}.
\]

## Assumptions and scope

The isometry-invariant measure on unoriented hyperplanes is the quotient of \(d\sigma(u)\,dt\), where \(u\) ranges over the Euclidean unit sphere and \(t\in\mathbb R\); the irrelevant overall multiplicative normalization cancels after conditioning on intersection. **Uniform orientation followed by uniform translation conditional on intersection is *not* this law:** under the invariant conditional law, orientation is weighted by the directional width. The polytope has unit vertex radius. The section is not required to pass through the origin. Hyperplanes incident to any original vertex or containing an original edge form a null set; all assertions about vertex counts are almost-sure assertions. The limit is in ambient dimension \(d\) with section codimension one, and moment limits hold for each fixed \(s>0\), not uniformly in \(s\).

## Proof

**1. Combinatorial cut count.** The edge graph of \(C_d\) has vertices \(\pm e_i\) and all edges between non-antipodal vertices; it is the complete graph on \(2d\) vertices with its \(d\) antipodal pairs removed. Orient a generic hyperplane, write \(G\) for a standard Gaussian normal, and consider the unnormalized equation \(G\cdot x=t\). For \(t>0\), let \(R_d(t)=\#\{i:|G_i|>t\}\). Exactly \(R_d(t)\) polytope vertices lie in its positive open halfspace, and the remaining \(2d-R_d(t)\) in the negative halfspace. Every positive-side vertex has precisely one excluded antipodal connection to the opposite side. Thus the number of crossed graph edges is
\[
R_d(t)[2d-R_d(t)]-R_d(t)=v_d(R_d(t)).
\]
Each crossing of an original edge supplies exactly one section vertex, and every generic section vertex is obtained this way. Reflection through the origin treats \(t<0\) identically. This proves the deterministic count. On \(H_{(d-k)}<t<H_{(d-k+1)}\), \(R_d(t)=k\), with the convention \(H_{(0)}=0\).

**2. Exact Crofton probability.** Let \(U\) be Haar-uniform on the sphere, with width support value \(h(U)=\max_i|U_i|\). Under invariant hyperplane measure conditioned on meeting \(C_d\), the joint density of \((U,t)\) is proportional to \(\mathbf1_{\{|t|<h(U)\}}\). For any even-in-\(t\) event \(\mathcal E\), its probability is therefore
\[
\frac{\mathbb E_U\int_0^{h(U)}\mathbf1_{\mathcal E(U,t)}\,dt}{\mathbb E_U h(U)}.
\]
Write \(G=\rho U\), where radius \(\rho=\|G\|_2\) and direction \(U\) are independent. In the ratio, multiplication of the upper limit and integration variable by \(\rho\) cancels the common factor \(\mathbb E\rho\). Consequently the same probability equals
\[
\frac{\mathbb E_G\int_0^{H_{(d)}}\mathbf1_{\mathcal E(G,t)}\,dt}{\mathbb E H_{(d)}}.
\]
Using the intervals from Step 1 gives the asserted probability masses, and summing intervals from \(k_*(h)\) up through \(d\) telescopes to the stated tail formula. Since \(v_d(k+1)-v_d(k)=2(d-k-1)\ge0\), the threshold indexing is monotone. In particular, the final two counts coincide and combine.

**3. Exact mean.** Integrate the number of crossing edges against the unnormalized offset over \((-H_{(d)},H_{(d)})\). For any original edge with endpoints \(a,b\), the length of offsets whose separating hyperplane crosses this edge is precisely \(|G\cdot(a-b)|\). There are \(2d(d-1)\) original edges. Each joins distinct coordinate axes and thus \(G\cdot(a-b)\) is centered normal with variance \(2\), so its expected absolute value is \(2/\sqrt\pi\). Dividing the sum of expected offset lengths by \(2m_d\) proves
\[
\mathbb E V_d=\frac{2d(d-1)}{\sqrt\pi m_d}.
\]

**4. Logarithmic exponent.** Put \(b_d=\sqrt{2\log d}\). Elementary Gaussian upper-tail bounds and binomial concentration imply \(H_{(d)}/b_d\to1\) in \(L^1\). More generally, if \(0<y<1\) and \(k_d=d^{y+o(1)}\), then
\[
H_{(d-k_d+1)}/b_d\to\sqrt{1-y}\quad\text{in }L^1.
\]
Here is a direct justification: for any fixed \(a>0\), the number of absolute Gaussian observations exceeding \(a b_d\) is binomial with expectation \(d^{1-a^2+o(1)}\), by the elementary Mills bounds; upper and lower concentration bound its comparison to \(k_d\) whenever \(a\) lies strictly to either side of \(\sqrt{1-y}\). This yields convergence in probability, while domination by \(H_{(d)}\) and the uniform bound \(\sup_d\mathbb E[H_{(d)}^2/b_d^2]<\infty\) give uniform integrability. The case of the maximum follows similarly.

Fix \(0<y<1\). Since the increasing polynomial \(v_d(k)\) first exceeds \(d^{1+y}\) at \(k_d=\tfrac12d^{y+o(1)}\), the exact tail formula gives
\[
\Pr\!\left\{\frac{\log V_d}{\log d}-1>y\right\}
=\frac{\mathbb E H_{(d-k_d+1)}}{m_d}\longrightarrow\sqrt{1-y}.
\]
That is the survival function of \(\operatorname{Beta}(1,\tfrac12)\) and proves weak convergence, including endpoints by tightness on the deterministic bounded support.

**5. Quadratic rare tail.** For fixed \(0<x<1\), the smallest index satisfying \(v_d(k)>xd^2\) obeys
\[
\frac{k_d}{d}\longrightarrow q_x=1-\sqrt{1-x}\in(0,1).
\]
The empirical-distribution law for independent half normals implies that the upper order statistic \(H_{(d-k_d+1)}\) converges in probability to the finite quantile
\[
t_x=\sqrt2\operatorname{erf}^{-1}(\sqrt{1-x}).
\]
This convergence is in \(L^1\): for any fixed \(q<q_x\), the order statistic is eventually bounded above by \((qd)^{-1}\sum_i H_i\), whose second moments are bounded uniformly. Therefore the exact tail identity and \(m_d/b_d\to1\) give the claimed sharp quadratic-scale tail.

**6. All positive moments.** Set \(Q(t)=\Pr\{|G_1|>t\}=1-\operatorname{erf}(t/\sqrt2)\). For each fixed \(t\ge0\), \(R_d(t)\) is binomial \((d,Q(t))\), and hence
\[
\frac{v_d(R_d(t))}{d^2}\longrightarrow Q(t)(2-Q(t))=1-\operatorname{erf}(t/\sqrt2)^2
\]
in probability. Step 2 applied to the nonnegative moment function yields
\[
m_d\,\mathbb E(V_d/d^2)^s=\int_0^\infty\mathbb E\bigl[v_d(R_d(t))/d^2\bigr]^s\,dt.
\]
Since \(v_d(r)/d^2\le2r/d\) for \(0\le r\le d\), the integrand is bounded by \(2^s Q(t)^{\min\{s,1\}}\), using Jensen's inequality for \(0<s<1\) and \((R_d/d)^s\le R_d/d\) for \(s\ge1\). The bound is integrable on \([0,\infty)\) for every fixed \(s>0\). Dominated convergence and \(m_d/b_d\to1\) prove the moment limit. For \(s=1\), the limiting integral is
\[
\int_0^\infty[1-(1-Q(t))^2]dt
=\mathbb E\max\{|G_1|,|G_2|\}=\frac2{\sqrt\pi},
\]
where the last equality follows from polar integration of a two-dimensional standard Gaussian (or from its exact half-normal maximum). This agrees with the exact mean from Step 3.

**7. Three-dimensional constant.** For \(d=3\), \(v_3(1)=4\) and \(v_3(2)=v_3(3)=6\). Thus \(\Pr(V_3=6)=\mathbb E H_{(2)}/\mathbb E H_{(3)}\). Integration by parts in the half-normal order-statistic densities gives, with \(\theta=\arctan(1/\sqrt2)\),
\[
\mathbb E H_{(3)}=\frac{12\theta}{\pi\sqrt\pi},\qquad
\mathbb E H_{(2)}=\frac6{\sqrt\pi}-\frac{24\theta}{\pi\sqrt\pi}.
\]
The ratio simplifies as displayed. Every step uses absolutely convergent integrals.

## Verification

The supplied standalone script `check.py` uses only the Python standard library. It numerically integrates independent Gaussian-order-statistic tail formulas and, separately, counts the crossings of *every original edge* for uniformly oriented Gaussian normals with importance weights corresponding to Crofton sampling. It verifies complete finite laws in dimensions three, four and six, the exact mean from a separate edge integral, and the closed octahedral probability. Execution from the actual packaged file completes with `CROSSPOLYTOPE_CROFTON_FINITE_LAW_OK`. These checks are finite consistency tests; the almost-sure combinatorics and infinite-dimensional limits follow from the written proof rather than from simulation.

## Relationship to prior work

Donoho and Tanner (2006; earliest public posting 15 July 2006) study face numbers of *random orthogonal projections* of high-dimensional regular polytopes. Their projection model and proportional-dimension thresholds do not yield the distribution of vertex counts for *translated codimension-one affine sections*. Donoho and Tanner (2008) likewise study random projections of hypercubes and orthants, not conditional Crofton sections. Kabluchko, Litvak and Zaporozhets (first posted 26 November 2015) establish Gaussian-maximum expressions and precise asymptotics for the **mean width and random projection width** of regular polytopes. The half-normal maximum asymptotics used here are known; the claim is not that Gaussian extremes are new. The crossed-edge section count, its Gaussian-gap probability law, the beta exponent and its distinct rare-tail asymptotic are the assertions compared for novelty.

De Loera, Lopez-Campos and Torres (2024/2025) study the maximum and attainable numbers of vertices in polytope hyperplane sections. The edge-crossing characterization they recall is standard background here. Their main classes are cyclic polytopes and hypercubes, and their deterministic extremal and slice-sequence results do not imply the conditioned Crofton distribution for regular cross-polytopes.

Closely related archived research on Haar **central** cross-polytope hyperplane sections treats the Euclidean diameter of a section, not the vertex count of a **translated** random section. A separate exact affine-simplex result already gives the same beta exponent for simplex sections; that coincidence is acknowledged rather than claimed as a newly discovered beta distribution. Neither central-diameter results nor the affine-simplex law gives the stated cross-polytope probabilities or the distinct sharp upper-tail scale directly. No searched result was found that implies the entire stated theorem; that absence is not proof of absolute priority.

## Limitations

The theorem concerns regular cross-polytopes only, with invariantly sampled **affine** hyperplanes conditioned to intersect. It does not assert the same finite law for triaxial cross-polytopes, higher-codimension sections, or Haar-central sections. The asymptotic equivalents do not provide finite-dimensional error bounds. Numerical experiments alone do not establish any asymptotic theorem. Historical-priority uncertainty persists for geometric-probability treatments that could be unindexed or not accessible for full-text comparison; independent mathematical audit is not claimed.

## References

1. D. L. Donoho and J. Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension*, arXiv:math/0607364, first public posting 2006-07-15; https://arxiv.org/abs/math/0607364.
2. D. L. Donoho and J. Tanner, *Counting the Faces of Randomly-Projected Hypercubes and Orthants, with Applications*, arXiv:0807.3590, first public posting 2008-07-23; https://arxiv.org/abs/0807.3590.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first public posting 2015-11-26; https://arxiv.org/abs/1511.08479.
4. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first publicly posted 2024-12-17; https://arxiv.org/abs/2412.12419.
