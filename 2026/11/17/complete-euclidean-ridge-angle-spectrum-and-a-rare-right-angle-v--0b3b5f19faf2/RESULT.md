# Complete Euclidean ridge-angle spectrum and a rare-right-angle variance law for biclique symmetric edge polytopes

## Finding
For every integer \(q\ge2\), let \(P_q\) be the symmetric edge polytope of the complete bipartite graph \(K_{2,q}\), in its **standard Euclidean root embedding**:
\[
P_q=\operatorname{conv}\{\pm(e_i-e_j):i\in\{1,2\},\ 3\le j\le q+2\}\subseteq H_q,\qquad H_q=\{x\in\mathbb R^{q+2}:\sum_i x_i=0\}.
\]
A ridge means a face of dimension \(q-1\) (codimension two in \(P_q\)), and its interior dihedral angle is the angle inside \(P_q\) between the two incident supporting hyperplanes, in the intrinsic Euclidean metric of \(H_q\).

There are exactly \(2^{q-1}(q+4)\) ridges. Of these, \(2^{q+1}\) have angle \(\pi/2\). The other \(q2^{q-1}\) ridges are partitioned into classes indexed by \(1\le r\le q\), with \(r\binom qr\) ridge incidences in class \(r\). Define
\[
h_{q,r}=2r-q-1,\qquad C_{q,r}=\frac{q^2-3-h_{q,r}^2}{\sqrt{\bigl(q(q+2)-(h_{q,r}+1)^2\bigr)\bigl(q(q+2)-(h_{q,r}-1)^2\bigr)}}.
\]
Each class-\(r\) ridge has the exact angle \(\theta_{q,r}=\pi-\arccos(C_{q,r})\). The classes \(r\) and \(q+1-r\) have the same angle and multiplicity, and for \(q\ge3\) these are the **only** equalities between distinct class labels. Thus \(P_q\) has exactly \(1+\lceil q/2\rceil\) distinct dihedral-angle values for \(q\ge3\): one right angle and \(\lceil q/2\rceil\) strictly obtuse angles. For \(q=2\), all twelve ridge angles are right angles.

For a ridge chosen uniformly from all ridges, let \(\Theta_q\) be its angle. If \(Z\sim N(0,1)\), then, as \(q\to\infty\),
\[
\sqrt q\,(\pi-\Theta_q)\xrightarrow{\mathsf P}2,\qquad
q^{3/2}\left(\pi-\Theta_q-\frac{2}{\sqrt q}\right)\xrightarrow{\mathrm d}Z^2-\frac23,\qquad
q\operatorname{Var}(\Theta_q)\longrightarrow\pi^2.
\]
The last relation is a **rare-ridge effect**: only a proportion \(4/(q+4)\) of ridges are right-angled, yet they determine the leading angle variance. The first two limits are weak/probabilistic statements and do not imply convergence of the corresponding unbounded rescaled moments.

## Assumptions and scope
The parameter is every integer \(q\ge2\). Root coordinates are unscaled unit-coordinate differences in \(\mathbb R^{q+2}\); no affine normalization is imposed. The two hub labels are \(1,2\), and the other \(q\) labels are leaves. Ridges are counted as **unoriented faces**, not ordered pairs of incident facets. The facet classification used below is the previously proved result of Higashitani--Jochemko--Michałek [1, Proposition 3.4]; all angle, multiplicity and limiting-distribution claims are derived anew.

## Proof
**1. All facets and their supporting vertices.** By [1, Proposition 3.4], every facet of \(P_q\) is of one of the following two sorts. For each leaf-sign vector \(s\in\{\pm1\}^q\), let \(B_s\) have potential \((0,0,s_1,\ldots,s_q)\). Its supporting vertex set is
\[
\{s_j(e_{j+2}-e_1),\ s_j(e_{j+2}-e_2):1\le j\le q\}.
\]
The only other facets are \(A_+\) and \(A_-\), with respective potentials \((1,-1,0,\ldots,0)\) and \((-1,1,0,\ldots,0)\). The \(A_+\) facet contains \(e_1-e_{j+2}\) and \(e_{j+2}-e_2\) for every \(j\); \(A_-=-A_+\). All listed potentials attain maximum one on \(P_q\). There are \(2^q+2\) facets. Equality of an inequality at a convex combination of vertices requires equality at every positively weighted constituent vertex; therefore intersections of listed facets are the convex hulls of their **shared** supporting vertices.

**2. Exact ridge-incidence classification.** The pair \(A_+,A_-\) has no common supporting vertices. For each \(s\), the intersection \(A_+\cap B_s\) consists of exactly one supporting vertex per leaf and is an affinely independent \((q-1)\)-simplex; the same is true of \(A_-\cap B_s\). These are \(2^{q+1}\) distinct ridges. For \(s\ne t\), let \(m\) be their number of agreeing leaf signs. The common vertices of \(B_s\) and \(B_t\), when \(m\ge1\), form an orthogonal line-segment prism over a simplex on \(m\) points, so the common face has dimension \(m\); for \(m=0\), the faces are disjoint. Thus \(B_s\cap B_t\) is a ridge exactly when \(s,t\) differ at one coordinate. There are \(q2^{q-1}\) such unordered sign-cube edges. Every ridge of a polytope has exactly two incident facets, so these exhaust all ridges. Orient a sign-cube edge from its endpoint with \(r\) positive signs toward the endpoint with \(r-1\) positives. There are \(r\binom qr\) such edges, giving the asserted classification and the total \(2^{q-1}(q+4)\).

**3. Angles from intrinsic normal Gram matrices.** If \(p\in\mathbb R^{q+2}\) is any potential, its Euclidean outward normal **in \(H_q\)** is \(\bar p=p-(\sum_i p_i)/(q+2)\mathbf1\). The two exceptional normals are opposites of \(a=(1,-1,0,\ldots,0)\), and each is orthogonal to every centered signed-leaf normal. Hence all \(A\)--\(B\) angles are right. For a \(B_s\)--\(B_t\) ridge as in step 2, put \(m=2r-q\). Their leaf-sign sums are \(m\) and \(m-2\); their leaf-vector dot product is \(q-2\). Consequently
\[
\begin{aligned}
(q+2)\|\bar p_s\|^2&=q(q+2)-m^2,\\
(q+2)\|\bar p_t\|^2&=q(q+2)-(m-2)^2,\\
(q+2)\langle\bar p_s,\bar p_t\rangle&=(q-2)(q+2)-m(m-2).
\end{aligned}
\]
The last displayed relation uses the same factor \(q+2\) as the two norm equations because each centered dot product equals \(q-2-m(m-2)/(q+2)\). Dividing gives the announced \(C_{q,r}\) after the substitution \(h=m-1\). For two outward unit normals of a convex polytope, the **interior** dihedral angle is \(\pi\) minus their angle, which proves the formula for \(\theta_{q,r}\).

**4. No hidden angular coincidences.** Set \(h=h_{q,r}\). The numerator of \(C_{q,r}\) equals \(q^2-3-h^2\), which is positive for \(q\ge3\), since \(|h|\le q-1\). Thus every \(B\)--\(B\) angle is strictly obtuse when \(q\ge3\). Write \(\delta=\pi-\theta_{q,r}\). Directly expanding the Gram determinant yields
\[
\tan\delta=\frac{2\sqrt{(q+2)(q^2-1-h^2)}}{q^2-3-h^2}.
\]
The right-hand side, as a function of \(u=h^2\) on \(0\le u\le(q-1)^2\), is strictly increasing: it is a positive constant times \(\sqrt X/(X-2)\) with \(X=q^2-1-u>2\), and the latter decreases strictly with \(X\). Therefore two angles coincide if and only if their squared \(h\)-values coincide, equivalently \(r'=r\) or \(r'=q+1-r\). This gives exactly \(\lceil q/2\rceil\) distinct obtuse angles. For \(q=2\), the numerator \(q^2-3-h^2\) vanishes for both admissible \(h\), so all ridge angles are right.

**5. Probabilistic law and its variance anomaly.** Conditional on drawing a \(B\)--\(B\) ridge, the class weight satisfies
\[
\Pr\{r=j\mid B\text{--}B\}=\frac{j\binom qj}{q2^{q-1}}=\frac{\binom{q-1}{j-1}}{2^{q-1}}.
\]
Thus \(h=2r-q-1\) has exactly the law of a sum of \(q-1\) independent fair signs and \(h/\sqrt q\Rightarrow Z\). With \(h=\sqrt q\,z\) for bounded \(z\), the tangent formula and \(\arctan x=x-x^3/3+O(x^5)\) give, uniformly for bounded \(z\),
\[
\delta=\frac2{\sqrt q}+\frac{z^2-2/3}{q^{3/2}}+O_{|z|\le R}(q^{-5/2}).
\]
This establishes the two limits for a random \(B\)--\(B\) ridge, by the central limit theorem and tightness. The probability of drawing an \(A\)--\(B\) ridge is exactly \(p_q=4/(q+4)\to0\), so the same distributional conclusions hold for an **unconditioned** random ridge.

For the variance, let \(D_q\) be the exterior angle of a uniformly selected \(B\)--\(B\) ridge. A Hoeffding bound for the fair-sign sum shows \(\Pr\{|h|>q^{2/3}\}\le2e^{-c q^{1/3}}\) for a universal \(c>0\). On its complement the displayed exact tangent formula implies \(D_q=2q^{-1/2}+o(q^{-1/2})\) uniformly; on the rare complement \(0\le D_q\le\pi/2\). It follows that \(q\operatorname{Var}(D_q)\to0\) and \(\mathbb E D_q\sim2/\sqrt q\). Since the exterior angle of an \(A\)--\(B\) ridge is \(\pi/2\), the variance decomposition for a two-component mixture yields
\[
q\operatorname{Var}(\pi-\Theta_q)
=q(1-p_q)\operatorname{Var}(D_q)+qp_q(1-p_q)\bigl(\pi/2-\mathbb E D_q\bigr)^2\longrightarrow\pi^2.
\]
Variance is unchanged by subtracting the angle from \(\pi\), proving the final assertion.

## Verification
A standalone checker (`verify_ridges.py`) directly enumerates all predicted supporting faces, their shared vertices and affine intersection ranks for \(2\le q\le6\). In independently chosen orthonormal coordinates for \(H_q\), it also reconstructs the convex hull using SciPy Qhull and confirms that every computed hull facet hyperplane agrees with one of the displayed facet potentials. It verifies every incident-pair cosine and multiplicity, then checks the exact integer Gram-discriminant identity and binomial ridge totals for \(2\le q\le300\). Successful execution prints `K2Q_RIDGE_SPECTRUM_PASS q_hull=2..6 q_algebra=2..300`. These tests are finite checks, not proofs of the all-dimensional assertions or probabilistic limits.

## Relationship to prior work
The exhaustive facet-potential classification is due to Higashitani, Jochemko and Michałek [1, Theorem 3.1 and Proposition 3.4]; the present proof starts from that classification and does not claim it. Chen, Davis and Korchevskaia [2] describe facet/face subgraphs and their graph-theoretic geometry, while D'Alì, Delucchi and Michałek [3] relate symmetric edge polytopes, Kantorovich--Rubinstein geometry and arithmetic/combinatorial invariants. The inspected relevant material does not state the all-ridge **intrinsic Euclidean dihedral-angle multiset**, its exact binomial multiplicities, or the rare-ridge variance law. A facet-area calculation and angle calculations address different metric data: knowledge of all facet areas alone does not supply the normal inner products and ridge incidences required here.

## Limitations
The angle formulas depend on the standard Euclidean root embedding; they need not hold after a nonorthogonal affine transformation. The limiting law is for a **uniformly sampled ridge**, not a ridge sampled with intrinsic \((q-1)\)-volume weights. The distributional fluctuation limit does not imply convergence of its moments, and the variance anomaly specifically exhibits nonuniform integrability. The proof does not claim that angle classification extends to \(K_{p,q}\) with \(p>2\). Bibliographic priority remains provisional pending independent inspection of other potentially equivalent treatments. No independent mathematical audit has been performed.

## References
[1] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public 20 July 2018), Section 3.1, Proposition 3.4, Example 3.6. https://arxiv.org/abs/1807.07678.

[2] T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 26 July 2021; inspected version 2 dated 1 December 2022), especially Sections 1 and 4. https://arxiv.org/abs/2107.12315.

[3] A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (11 October 2019); *Electronic Journal of Combinatorics* 29(3) (2022), P3.24, especially Sections 2 and 4. https://doi.org/10.37236/10387.
