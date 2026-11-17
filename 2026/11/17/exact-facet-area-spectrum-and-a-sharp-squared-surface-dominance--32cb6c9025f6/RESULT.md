# Exact facet-area spectrum and a sharp squared-surface dominance transition in biclique root polytopes

## Finding
For every integer \(q\ge2\), let \(P_q\) be the symmetric edge polytope of the complete bipartite graph \(K_{2,q}\), realized using actual coordinate roots \(\pm(e_i-e_j)\) in \(\mathbb R^{q+2}\). Its affine hull is the \((q+1)\)-dimensional coordinate-sum-zero subspace. **All distances and intrinsic volumes in this article use the ordinary Cartesian Euclidean metric on this subspace.**

All \(2^q+2\) facets have intrinsic dimension \(q\). Precisely \(2^q\) are signed-leaf prisms, indexed by sign vectors \(s\in\{\pm1\}^q\); the remaining two are congruent exceptional cross-polytopes. If \(r\) is the number of positive entries of \(s\), their intrinsic facet volumes are respectively
\[
 V_B(q,r)=\frac{\sqrt{2(q+2r(q-r))}}{(q-1)!},\qquad
 V_A(q)=\frac{2^q}{q!}\sqrt{1+\frac q2}.
\]
Consequently the complete intrinsic facet-area multiset consists of \(\binom qr\) copies of \(V_B(q,r)\) for each \(0\le r\le q\), plus two copies of \(V_A(q)\). Values can coincide; these are multiplicities of **facets**, not an assertion that every displayed value is distinct. The exact \(q\)-dimensional Euclidean surface area is
\[
 \mathcal S_q=\frac{2^{q+1}}{q!}\sqrt{1+\frac q2}
 +\frac{\sqrt2}{(q-1)!}\sum_{r=0}^q\binom qr\sqrt{q+2r(q-r)}.
\]

The two types contribute the following sums of **squared** facet volumes:
\[
 \sum_{A\text{-facets}}V^2=\frac{4^q(q+2)}{(q!)^2},\qquad
 \sum_{B\text{-facets}}V^2=\frac{2^q q(q+1)}{((q-1)!)^2}.
\]
Their ratio is
\[
 R_q=\frac{2^q(q+2)}{q^3(q+1)}.
\]
The two exceptional facets dominate the entire squared-area sum **if and only if \(q\ge10\)**. This is a threshold for squared Euclidean area mass, not for ordinary surface area and not for a facet's inclusion probability.

For a facet chosen uniformly from all \(2^q+2\) facets and \(A_q\) denoting its intrinsic volume,
\[
 q\left(\frac{(q-1)!}{q}A_q-1\right)\ \xrightarrow{\mathrm d}\ 1-\frac{Z^2}{2},\qquad Z\sim N(0,1).
\]
In particular, ordinary signed-leaf facets typically have normalized areas within order \(1/q\) of unity despite the rare cross-polytope area amplification. There is **no assertion of convergence of moments** of the scaled random variable; rare exceptional facets affect those moments.

## Assumptions and scope
The graph is the labeled complete bipartite graph \(K_{2,q}\), with \(q\ge2\). Its two hub vertices carry indices \(1,2\), and its \(q\) leaf-side vertices carry indices \(3,\ldots,q+2\). We work with
\[
 P_q=\operatorname{conv}\{\pm(e_i-e_j):i\in\{1,2\},\ j\in\{3,\ldots,q+2\}\}.
\]
The polytope has affine dimension \(q+1\), so its facets have intrinsic dimension \(q\). The \(q\)-dimensional Hausdorff measure of a facet is denoted \(\operatorname{vol}_q\), and \(\mathcal S_q\) is the sum of those measures. No alternate lattice or root-system metric renormalization is used. The facet count and facet-potential classification are previously known [1]; the metric-area formulas and the stated distributional/squared-area consequences are the claim tested here.

## Proof
**Step 1: Exhaustive facet classification (known premise).** Proposition 3.4 of [1] says that for \(K_{2,q}\), every facet-supporting integer potential, modulo an additive constant, is either zero on both hub vertices with an arbitrary sign \(\pm1\) on each other vertex, or zero on every leaf-side vertex with independent signs on the two hubs, excluding duplicate constant-potential cases. The first family has exactly \(2^q\) potentials. In the second family the two nonconstant hub-sign assignments give exactly two different facets. Thus the following two explicit constructions account for every facet, with no missing metric contributors.

**Step 2: Signed-leaf facets are orthogonal prisms.** Put \(h=(e_1+e_2)/2\) and let \(s=(s_1,\dots,s_q)\in\{\pm1\}^q\) be the leaf-side potential. The vertices of its supporting facet are
\[
 s_j(e_{j+2}-e_1),\quad s_j(e_{j+2}-e_2)\qquad(1\le j\le q).
\]
For each \(j\), these endpoints form the line segment from \(m_j-(e_1-e_2)/2\) to \(m_j+(e_1-e_2)/2\), where \(m_j=s_j(e_{j+2}-h)\); the unordered pair is unaffected by interchanging segment endpoints. Therefore the facet is exactly the Minkowski sum of \(\operatorname{conv}\{m_1,\ldots,m_q\}\) and the segment \([-(e_1-e_2)/2,(e_1-e_2)/2]\). They are orthogonal, as every \(m_j\) has equal first two coordinates. The segment length is \(\sqrt2\).

To compute the \((q-1)\)-simplex volume, use the edges \(m_i-m_q\) for \(1\le i<q\). If \(r\) signs are positive and \(q-r\) negative, the determinant of their Gram matrix is
\[
 \det\bigl[\langle m_i-m_q,m_j-m_q\rangle\bigr]_{1\le i,j<q}=q+2r(q-r).
\]
For verification of this identity without hidden normalization, choose the last sign \(s_q=+1\) by global sign reversal; the \((q-1)\)-by-\((q-1)\) Gram matrix then equals the diagonal matrix with entries one, plus a rank-one term from the last leaf, plus the rank-one hub contribution \(\tfrac12(s_i-1)(s_j-1)\). The matrix determinant lemma, or the split into equal-sign and opposite-sign spans, gives \(q+2r(q-r)\). Direct calculation also handles the endpoint cases \(r=0,q\). Thus the prism area is \(\sqrt2\) times the simplex area, giving \(V_B(q,r)\) as stated.

**Step 3: Two exceptional facets are cross-polytopes.** The exceptional potential with hub values \(1,-1\) and leaf values zero has supporting vertices \(e_1-e_{j+2}\) and \(e_{j+2}-e_2\), for \(1\le j\le q\). Write \(c=(e_1-e_2)/2\) and \(g_j=h-e_{j+2}\). Its facet is the translate \(c+\operatorname{conv}\{\pm g_1,\ldots,\pm g_q\}\). The vectors \(g_j\) have Gram matrix \(I_q+\tfrac12\mathbf1\mathbf1^{\mathsf T}\), whose determinant is \(1+q/2\). A standard \(q\)-cross-polytope has Euclidean volume \(2^q/q!\); applying the Gram-determinant factor yields \(V_A(q)\). The potential with reversed hub signs gives the antipodal facet of the same area.

**Step 4: Summing areas and squared areas.** There are \(\binom qr\) B facets with \(r\) positive signs. Summing their formulas and adding two A facets proves \(\mathcal S_q\). The binomial identity \(\sum_r\binom qr r(q-r)=2^{q-2}q(q-1)\) gives the B squared-area sum; doubling \(V_A(q)^2\) gives the A sum. Their quotient is exactly \(R_q\).

For the sharp threshold, direct exact rational substitution verifies \(R_q<1\) for \(2\le q\le9\) and \(R_{10}>1\). For every integer \(q\ge5\),
\[
 \frac{R_{q+1}}{R_q}=\frac{2q^3(q+3)}{(q+1)^2(q+2)^2}>1,
\]
since the numerator minus denominator is \(q^4-13q^2-12q-4>0\) for all \(q\ge5\). The last inequality follows because its polynomial is positive at \(q=5\) and strictly increasing thereafter. Hence the threshold is exactly \(q=10\).

**Step 5: Random-facet limit.** Conditional on being a B facet, the signs are independent fair Rademacher variables and \(S_q=\sum_js_j=2r-q\) satisfies \(S_q/\sqrt q\Rightarrow Z\sim N(0,1)\). From Step 2,
\[
 \frac{(q-1)!}{q}V_B(q,r)=\sqrt{1+\frac2q-\frac{S_q^2}{q^2}}.
\]
The continuous mapping theorem and the identity \(\sqrt{1+t}-1=t/(\sqrt{1+t}+1)\) imply
\[
 q\left(\frac{(q-1)!}{q}V_B(q,r)-1\right)
 =\frac{2-S_q^2/q}{\sqrt{1+2/q-S_q^2/q^2}+1}\ \Rightarrow\ 1-\frac{Z^2}{2}.
\]
The probability of selecting either exceptional A facet is \(2/(2^q+2)\to0\), so the unconditional law has the same weak limit. All quantifiers are \(q\to\infty\) through integers \(q\ge2\); no moment convergence is invoked.

## Verification
The included standalone program `verify_surface.py` executes exact SymPy Gram-determinant checks for every sign pattern for \(2\le q\le6\), and separately reconstructs every facet directly from the root vertices using SciPy convex-hull hyperplane equations in an orthonormal affine chart. It then computes their Euclidean \(q\)-volumes by a second, independently projected convex-hull calculation. It checks the total area, both squared-area sums, and exact integer threshold conditions. The recorded successful output is:

```
K2Q_SURFACE_PASS q=2..6 exact_gram and independent_hull; squared_area_threshold=10
```

These finite checks are corroborating evidence, not substitutes for the all-dimensional Gram-matrix and binomial proofs. Routines need Python, NumPy, SciPy and SymPy. Reproduce using `python verify_surface.py` from a folder containing the included program.

## Relationship to prior work
The complete bipartite facet classification is Proposition 3.4 and the geometric facet presentation is Example 3.6 of Higashitani--Jochemko--Michałek [1]. Their results supply the *known supporting-potential types* used here; their facet count, combinatorial types, and Ehrhart results should not be interpreted as newly established. Chen--Davis--Korchevskaia [2] investigate facets and facet subgraphs, and D'Alì--Juhnke-Kubitzke--Koch [3] study generalization to regular matroids. The metric Gram determinants, exact Euclidean surface area, squared-area threshold, and uniform-facet fluctuation law are distinct from those primarily combinatorial statements. No claim of priority beyond the checked sources is made.

## Limitations
This statement is specific to the standard Euclidean root-coordinate realization of \(K_{2,q}\); arbitrary affine transformations change facet areas. The squared-area threshold does not compare the corresponding contributions to ordinary unsquared surface area. The weak limit is for a *uniformly chosen facet*, not for area-weighted facet sampling, and does not establish convergence of second moments of the normalized variable. Previous literature using alternate surface-area conventions or an equivalent closed formula could still affect historical priority. Independent scientific audit has not been performed.

## References
[1] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (20 July 2018), Theorem 3.1, Proposition 3.4, Example 3.6. https://arxiv.org/abs/1807.07678.

[2] T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public July 2021). https://arxiv.org/abs/2107.12315.

[3] A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (10 July 2023). https://arxiv.org/abs/2307.04933.
