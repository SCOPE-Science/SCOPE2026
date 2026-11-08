# Exact two-map approximation of componentwise-weighted disconnected covering averages

## Finding
Let \(q:Y\to X\) be a finite covering of a finite connected topological graph \(X\). Suppose \(Y=\bigsqcup_{i=1}^{s}Y_i\), where every \(Y_i\) is connected and its restricted covering has degree \(d_i\ge 1\). Choose nonnegative weights \(\lambda_i\) with \(\sum_i\lambda_i=1\). Define the Markov operator
\[
(A_\lambda f)(x)=\sum_{i=1}^{s}\frac{\lambda_i}{d_i}\sum_{y\in q^{-1}(x)\cap Y_i}f(y).
\]
Write \(t_1\ge t_2\ge0\) for the two largest weights belonging to degree-one components (padding with zeros), and write \(u=\max_{d_i\ge2}\lambda_i/d_i\) (zero if the index set is empty). Let \(\mathcal E_2\) consist of convex combinations of at most two extreme Markov operators, and let \(\mathcal E_2^{\mathrm{eq}}\) consist of averages of two, with repeated operators permitted. Then both following exact distances are attained:
\[
\operatorname{dist}(A_\lambda,\mathcal E_2)=2\bigl(1-\max\{t_1+t_2,u\}\bigr),
\]
\[
\operatorname{dist}(A_\lambda,\mathcal E_2^{\mathrm{eq}})
=2\bigl(1-\max\{t_1,\min(t_1,1/2)+\min(t_2,1/2),u\}\bigr).
\]
These distances use the ordinary operator norm from the real \(C(Y)\) to \(C(X)\), both with supremum norms.

## Assumptions and scope
A finite graph is the compact one-dimensional CW complex obtained from finitely many closed edges, including possible loops. The covering is a genuine finite-sheeted topological covering; each component \(Y_i\) is connected. The weights \(\lambda_i\) are constant as \(x\) varies, may be zero, and sum to one. The base graph \(X\) is connected. The extreme Markov operators are the composition maps \(C_hf=f\circ h\), with \(h:X\to Y\) continuous; this characterization is Lemma 2.1 of Duru--Ilter--Bilgin [1]. The sets of approximants permit repeated maps, and \(\mathcal E_2\) permits a zero coefficient. None of the maps \(h\) is required to respect the covering.

## Proof
**1. Atomic norm and missing-fiber overlap.** For each \(x\in X\), the measure representing \(A_\lambda\) places mass \(\lambda_i/d_i\) at every point of the fiber in \(Y_i\). For another Markov kernel \(\nu_x\), the pointwise total-variation distance is \(2(1-O_x)\), where
\[
 O_x=\sum_{y\in q^{-1}(x)}\min\bigl\{\mu_x(\{y\}),\nu_x(\{y\})\bigr\}.
\]
Mass of \(\nu_x\) off the fiber contributes no overlap. Hence the operator distance is \(2(1-\inf_{x\in X}O_x)\). This follows from the Riesz representation theorem and the total-variation norm identity, with no finite-dimensional approximation.

**2. A section dichotomy.** Each continuous \(h:X\to Y\) has connected image and therefore lies in one component \(Y_i\). If \(d_i=1\), the inverse of \(q_i:Y_i\to X\) is a continuous section. If \(d_i\ge2\), no continuous section exists: a section of a finite covering is an open embedding, and its image, being compact and closed, would be a nonempty proper clopen subset of connected \(Y_i\). Thus, for any map \(h:X\to Y_i\) with \(d_i\ge2\), some \(x\) has \(h(x)\notin q_i^{-1}(x)\).

**3. Upper bounds on attainable uniform overlap.** If both approximating maps land in degree-one components, the total overlap at any point is at most \(t_1+t_2\); for equal coefficients it is at most \(t_1\) when the maps lie in the same component, and at most \(\min(t_1,1/2)+\min(t_2,1/2)\) when they lie in different components. These bounds remain true when the maps fail to be sections. If either map lands in a degree-at-least-two component, choose \(x\) where that map misses its fiber. At that \(x\), the other map can cover at most one atom, whose target mass is at most \(\max\{t_1,u\}\). Hence in all cases \(\inf_xO_x\) is at most \(\max\{t_1+t_2,u\}\) for unrestricted convex coefficients, and at most \(\max\{t_1,\min(t_1,1/2)+\min(t_2,1/2),u\}\) for equal coefficients. This proves both distance lower bounds.

**4. Two-map coverage lemma.** For every connected finite graph covering \(q_i:Y_i\to X\) of degree at least two, there are continuous maps \(h_1,h_2:X\to Y_i\) such that at each \(x\in X\) at least one map lies in \(q_i^{-1}(x)\). Here is a direct construction. At each vertex \(v\) choose two (not necessarily distinct) points \(a_v,b_v\) above \(v\). For each oriented edge identify its restricted covering with finitely many continuous sheet lifts \(\rho_j:[0,1]\to Y_i\). On the initial third of the edge, let both maps track sheets starting at \(a_v,b_v\). On the interval \([1/3,1/2]\), keep the second map on its sheet and move the first through an arbitrary path in connected \(Y_i\) to any point on a sheet whose terminal value is \(a_w\). On \([1/2,2/3]\), keep the first map on that sheet while moving the second through a path in \(Y_i\) onto a sheet ending at \(b_w\). On the final third, track both terminal sheets. Connected finite graphs are path connected, so both transitions exist. At every point of this edge at least one map tracks an actual fiber point, and the endpoints have the prescribed vertex values. Thus the edgewise maps glue continuously across all vertices, including loop edges. This two-map construction is a direct specialization of the single-atom transport mechanism in [1, Lemma 4.2]; it is included here so the mixed-component argument is self-contained. It does not assume either map is a section.

**5. Matching constructions.** If the two largest degree-one component masses exist, their inverse-cover sections, with convex coefficients \(1-t_2\) and \(t_2\), have overlap \(t_1+t_2\) at every \(x\). (If only one such component exists, use its section alone, with overlap \(t_1\).) Equal-weight copies of the largest section give overlap \(t_1\); equal-weight sections of two different degree-one components give overlap \(\min(t_1,1/2)+\min(t_2,1/2)\). If \(u>0\), choose a component attaining \(u\), apply the two-map coverage lemma, and take their equal average. At least one of its atoms lies in the corresponding fiber for every \(x\), contributing overlap at least \(u\): indeed \(u=\lambda_i/d_i\le1/2\). This construction also lies in unrestricted \(\mathcal E_2\). If \(u=0\) there is no need for it. Taking the best construction proves equality and attainment for both displayed distances. \(\square\)

**Corollary (unbounded cost of equal coefficients).** Let the covering have three connected components of degrees \(1,1,2\), with \(\lambda=(3/4,1/4-\varepsilon,\varepsilon)\) and \(0<\varepsilon<1/8\). Both coverings and sections exist (for example, a circle, its identity covers, and its connected double cover). The formulas give
\[
\operatorname{dist}(A_\lambda,\mathcal E_2)=2\varepsilon,
\qquad
\operatorname{dist}(A_\lambda,\mathcal E_2^{\mathrm{eq}})=1/2.
\]
Their ratio is \(1/(4\varepsilon)\), and is arbitrarily large. In contrast, for one connected cover and two terms the equal and unrestricted errors coincide [1].

## Verification
The standalone script `verify_examples.py` checks 4,265 exact-rational arithmetic assertions for all three-component degree triples from \(\{1,2,3,5\}\) and tenth-grid component masses, the connected-cover two-term specialization for degrees 2 through 13, and the unbounded-ratio family. Its observed output was `COMPONENTWISE_MARKOV_RATIONAL_CHECK_OK 4265`. These finite checks test scalar consequences only. The full theorem, especially the two-map coverage lemma, is proved analytically above.

## Relationship to prior work
Duru, İlter, and Bilgin [1, Theorems 1.1 and 1.2] calculate exact arbitrary/equal-weight \(m\)-term distances for a **single connected** uniform-degree covering; [1, Remark 6.7] identifies the connectedness restriction. The present formulas address **disconnected** finite coverings with heterogeneous, componentwise fiber masses and exactly two terms. In particular, the section masses compete with a nontrivial connected sheet and can cause an unbounded equal-weight penalty already for two terms. Brown [2] develops Markov approximation in weaker topologies on other function spaces, so its inspected method does not provide these operator-norm componentwise formulas. Kim [3] is a plausible older related source whose full text was unavailable during preparation, and publication priority remains provisional.

## Limitations
Only two extreme operators are budgeted; the theorem does not cover three or more terms, base-dependent weights, infinite coverings, arbitrary compact base spaces, or disconnected bases. No claim of independent verification or priority certification is made. The analytic result is self-contained; the finite checker is supplementary. Full-text comparison with some older Markov-approximation literature remains a residual originality risk.

## References
[1] H. Duru, S. İlter, and A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1 (publicly submitted 2026-10-26), https://arxiv.org/html/2610.35575v1.

[2] J. R. Brown, *Approximation theorems for Markov operators*, Pacific Journal of Mathematics (1966); https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-16/issue-1/Approximation-theorems-for-Markov-operators/pjm/1102994822.full.

[3] K. C. Kim, *Approximation theorems for Markov operators* (1972), https://doi.org/10.1007/BF00538394 (bibliographic record consulted; full text not inspected).
