# A six-vertex Euclidean inball transition for complete-graph spanning-tree polytopes

## Finding
For each integer \(n\ge4\), write \(E=E(K_n)\), \(m=\binom n2\), and
\[
P_n=\operatorname{conv}\{\mathbf1_T:T\text{ is a spanning tree of }K_n\}\subset\mathbb R^E.
\]
All Euclidean distances and balls are intrinsic to the affine hyperplane \(H_n=\{x:x(E)=n-1\}\). Let \(r_n\) be the largest radius of a ball in \(P_n\). Then
\[
\boxed{r_n^2=\begin{cases}
\dfrac{n-2}{n(n-1)},&n=4,5,\\[3pt]
\dfrac{4(n-1)}{n(n-2)(n+1)},&n\ge6.
\end{cases}}
\]
The uniform edge vector \(c_e=2/n\) is an incenter in every dimension. The ball centered at \(c\) is tangent to precisely \(n\) facets when \(n=4,5\), namely the singleton-cut facets \(x(\delta(v))\ge1\); for \(n\ge6\), it is tangent to precisely \(m\) facets, namely the nonnegativity facets \(x_e\ge0\). There are no further tangent facets at \(c\).

For \(n\ge6\) the incenter is unique. For \(n=4,5\), the **entire** set \(\mathcal I_n\) of incenters is the following polytope, of affine dimension exactly \(m-n=n(n-3)/2\):
\[
\begin{split}
\mathcal I_n=\{z\in H_n:\;&z(\delta(v))=2(n-1)/n\quad(v\in[n]),\\
&z_e\ge r_n\sqrt{1-1/m}\quad(e\in E),\\
&z(E(S))\le |S|-1-r_n\sqrt{a_S(1-a_S/m)}\\
&\hspace{18mm}(S\subset[n],\ 2\le |S|\le n-2),\quad a_S=\tbinom{|S|}{2}\}.
\end{split}
\]
In particular, the maximal-ball center locus is two-dimensional for \(K_4\), five-dimensional for \(K_5\), and a singleton from \(K_6\) onward. This is an exact metric phase change, not an assertion about the Minkowski-asymmetry center locus.

## Assumptions and scope
The graphs are finite, simple, undirected, and complete. An edge subset \(F\subseteq E\) has \(x(F)=\sum_{e\in F}x_e\); \(E(S)\) consists of edges with both endpoints in \(S\); and \(\delta(v)\) consists of edges incident with \(v\). The dimension of \(P_n\) in \(H_n\) is \(m-1\). Euclidean means the metric inherited from the orthonormal edge coordinate basis; no weighting or affine normalization is allowed. The theorem excludes \(n=3\), whose nonnegativity constraints are not facets. The motivating public work (arXiv:2606.17017, first released 2026-06-15) concerns symmetric formulations, and the classical Edmonds/Chaourar descriptions furnish the facet inequalities used here.

## Proof
**1. Complete halfspace description and projection norms.** Edmonds' spanning-tree theorem gives
\[
P_n=\{x\in H_n:x_e\ge0\ (e\in E),\quad x(E(S))\le |S|-1\ (2\le |S|\le n-1)\}.
\]
For \(n\ge4\) the displayed inequalities are facet defining (in the indicated ranges): deletion of an edge leaves a connected graphic matroid; each complete induced subgraph on \(k\ge2\) vertices and its contraction have connected graphic matroids (for \(k=2\) this is the parallel-class facet). Alternatively only the completeness of this halfspace system, not irredundancy, is needed for the radius bound. For any edge subset of size \(a\) the normal \(\mathbf1_F\), projected orthogonally into the tangent space \(H_n-H_n\), has squared norm \(a(1-a/m)\). In particular, a coordinate normal has squared norm \(1-1/m\).

**2. Symmetry reduces the ball problem to one center.** At a candidate radius \(r\), the set of feasible centers is the intersection of the displayed halfspaces with each right-hand side shifted inward by \(r\) times the projected normal length. This set is convex and invariant under all relabelings of the vertices of \(K_n\). Averaging any feasible center over all permutations gives the only invariant point in \(H_n\), namely \(c_e=(n-1)/m=2/n\). Hence the optimal radius equals the minimum of the distances from \(c\) to the stated supporting hyperplanes, and \(c\) attains the optimum.

The coordinate halfspaces have squared distance
\[
d_0^2=\frac{(2/n)^2}{1-1/m}=\frac{4(n-1)}{n(n-2)(n+1)}.
\]
For \(k=|S|\in\{2,\ldots,n-1\}\), the slack at \(c\) is \((k-1)(n-k)/n\), and \(|E(S)|=k(k-1)/2\); consequently the corresponding squared distance is
\[
d_k^2=\frac{2(n-1)(k-1)(n-k)}{nk(n+k-1)}.
\]
The singleton-cut description \(x(\delta(v))\ge1\) of the \(k=n-1\) facet follows from \(x(E)=n-1\), and
\[
d_{n-1}^2=\frac{n-2}{n(n-1)}.
\]

**3. No intermediate subset is closer.** Set \(f(t)=(t-1)(n-t)/[t(n+t-1)]\) for real \(t\in[2,n-1]\). Direct differentiation gives
\[
f'(t)=\frac{n(-2t^2+2t+n-1)}{t^2(n+t-1)^2}.
\]
The numerator decreases strictly after \(t\ge2\), so \(f\) first increases and then decreases (either branch may be empty); its minimum is at an endpoint. Moreover
\[
\frac{d_2^2}{d_{n-1}^2}=\frac{(n-1)^2}{n+1}>1\qquad(n\ge4),
\]
and the inequality is strict for all \(2\le k<n-1\). Thus \(\min_k d_k=d_{n-1}\). Comparing the two candidate distances gives
\[
d_{n-1}^2-d_0^2=\frac{n^2-7n+8}{(n-2)(n-1)(n+1)}.
\]
It is negative for integers \(n=4,5\) and positive for every integer \(n\ge6\). This proves the radius formula and exactly the claimed tangent-facet counts at the uniform center.

**4. Complete incenter classification.** When \(n\ge6\), each of the \(m\) coordinate inequalities is active at \(c\). Any feasible center \(z\) for radius \(r_n\) therefore satisfies \(z_e\ge r_n\sqrt{1-1/m}=2/n\) for every \(e\). Since \(z(E)=n-1=m(2/n)\), all these inequalities are equalities, hence \(z=c\).

When \(n=4,5\), all \(n\) singleton-cut inequalities are active at \(c\). The shifted version is \(z(\delta(v))\ge1+r_n\sqrt{(n-1)(1-(n-1)/m)}=2(n-1)/n\). Summing over \(v\) gives the fixed sum \(2z(E)=2(n-1)\); hence all \(n\) shifted inequalities must be equalities. The shifted coordinate and remaining subset inequalities are exactly the further conditions displayed in the formula for \(\mathcal I_n\), so that formula is necessary and sufficient. At \(c\), every remaining shifted inequality is strict, by Step 3. Hence a relatively open neighborhood of \(c\) inside the affine degree-constraint subspace consists of incenters.

To determine its dimension, the unsigned vertex-edge incidence matrix \(B\) of \(K_n\), with rows indexed by vertices, has row rank \(n\): if \(\lambda_u+\lambda_v=0\) for every edge, a triangle forces three coefficients to vanish and completeness forces all the rest. Thus the \(n\) degree equations \(Bz=2(n-1)\mathbf1/n\) have affine dimension \(m-n\); the equation \(z(E)=n-1\) is already their sum divided by two. The relative strictness at \(c\) shows that \(\mathcal I_n\) has this **exact** dimension.

## Verification
The source `verify.py` uses only the Python standard library. It checks the exact rational squared distances and the sharp transition for each integer \(4\le n\le500\), verifies projected-normal and incidence ranks for \(4\le n\le10\), enumerates every spanning tree of \(K_4,K_5,K_6\) by Prüfer words and tests every Edmonds subset inequality, and constructs explicit nonuniform feasible centers for \(n=4,5\) by a four-cycle perturbation of \(c\). It reported `VERIFICATION_OK 451620`. These finite checks are not proof of the unrestricted statement; Steps 1–4 supply the proof.

## Relationship to prior work
Edmonds' spanning-tree inequalities and Chaourar's full facet theory are essential established inputs, not new results. Pokutta's 2026 theorem on symmetric extension complexity uses the same incidence-vector polytope and its symmetry but proves a bound on extended formulations, not on Euclidean inscribed balls. A separate published result on **Minkowski centers** of complete-graph spanning-tree polytopes determines an affine-invariant asymmetry and weighted-degree center locus. It does **not** imply the present Euclidean phase transition: its center locus has dimension \(m-n\) for every \(n\), whereas the present Euclidean center is unique for every \(n\ge6\). The original statement claimed here is solely the Euclidean squared radius, complete incenter set, and facet-contact transition at six graph vertices.

## Limitations
This result does not address noncomplete graphs, other embeddings of the graphic-matroid base polytope, weighted Euclidean norms, arbitrary John ellipsoids, or the asymmetry center locus. The motivating study's first public preprint date is distinct from later document revision dates. Historical novelty is supported by inspected primary material and indexed-record comparison, not independently certified; differently named prior Chebyshev-center calculations remain possible. Numerical verification is finite. Independent mathematical audit is not performed.

## References
1. S. Pokutta, *Symmetric Extension Complexity of the Spanning Tree Polytope*, arXiv:2606.17017, first submitted 2026-06-15. https://arxiv.org/abs/2606.17017
2. B. Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292, first submitted 2019-03-18; particularly Theorems 2.1 and 2.3, Corollary 2.4. https://arxiv.org/html/1903.07292v4
3. J. Edmonds, *Submodular functions, matroids, and certain polyhedra*, 1969; classical graphic-matroid polytope inequalities, as quoted in reference 1.
4. Published mathematical record *Minkowski centers of complete-graph spanning-tree polytopes and the exceptional six-vertex cut*, published-finding corpus record dd8588f15b8f (2026-10-11), mathematical comparison only.
