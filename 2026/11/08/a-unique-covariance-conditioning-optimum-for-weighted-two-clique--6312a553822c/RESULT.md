# A unique covariance-conditioning optimum for weighted two-clique graphical zonotopes

## Finding

Fix integers \(a,b\ge2\), let \(n=a+b-1\), and form the graph \(G_{a,b}\) by identifying exactly one vertex of \(K_a\) with one vertex of \(K_b\), leaving all other vertices disjoint. Put weight \(t>0\) on every edge of the first clique and \(s>0\) on every edge of the second. Define its centered graphical zonotope by
\[
Z_{a,b}(t,s)=\sum_{\{i,j\}\in E(K_a)}[-\tfrac t2(e_i-e_j),\tfrac t2(e_i-e_j)]
+\sum_{\{i,j\}\in E(K_b)}[-\tfrac s2(e_i-e_j),\tfrac s2(e_i-e_j)]
\subset\mathbf1^\perp\subset\mathbb R^n.
\]
Choose \(X\) uniformly over the **distinct vertices** of this zonotope, not uniformly by volume and not by independent edge signs. Let \(C=\operatorname{Cov}(X)\) in the inherited Euclidean metric. Put \(U=a(a+1)t^2\), \(V=b(b+1)s^2\), and
\[
\Delta=\sqrt{(U+V)^2-4n(a+1)(b+1)t^2s^2}.
\]
Then the complete covariance spectrum, with multiplicities, is
\[
\boxed{\ 0\ (1),\quad U/12\ (a-2),\quad V/12\ (b-2),\quad
\lambda_\pm=(U+V\pm\Delta)/24\ (1\text{ each}).\ }
\]
An eigenvalue with zero multiplicity is omitted. For **every** \(a,b\ge2\) and \(t,s>0\), the two eigenvalues \(\lambda_-\) and \(\lambda_+\) are strictly positive, distinct, and respectively the smallest and largest positive eigenvalues. Hence the intrinsic covariance condition number is \(\kappa=\lambda_+/\lambda_-\).

The scale ratio \(t/s\) has **one and only one** optimal positive value:
\[
\boxed{\ \left(\frac ts\right)_{\!\mathrm{opt}}
=\sqrt{\frac{b(b+1)}{a(a+1)}}.\ }
\]
The sharp minimum is
\[
\boxed{\ \min_{t,s>0}\kappa
=\frac{\bigl(\sqrt{ab}+\sqrt{(a-1)(b-1)}\bigr)^2}{a+b-1}.\ }
\]
For the unweighted zonotope \(t=s=1\), the condition number is strictly larger than this bound unless \(a=b\). At fixed \(a\) and \(b\to\infty\), the unweighted condition number grows quadratically while optimal weighting leaves it bounded:
\[
\kappa(1,1)\sim\frac{b^2}{a+1},\qquad
\min_{t,s>0}\kappa\longrightarrow
\bigl(\sqrt a+\sqrt{a-1}\bigr)^2.
\]
These statements concern the single connected two-block family and allow clique size two. In the equal-size case \(a=b\), the optimum has \(t=s\) and \(\kappa=a+b-1\).

## Assumptions and scope

The graph is simple and has exactly two maximal clique blocks intersecting in precisely one articulation vertex. The first and second block each carry a constant positive **edge-length weight**; the two weights may differ. The ambient metric is the ordinary Euclidean metric on the zero-sum hyperplane, with no volume-normalization or change of inner product. Sampling is uniform over distinct vertices, which correspond to acyclic orientations. Common positive scaling of \(t\) and \(s\) multiplies \(C\) by the square of that scale and leaves \(\kappa\) unchanged.

The conclusion is not asserted for graphs with overlapping clique edge sets, for weights varying *within* a clique, for volume-uniform sampling, or for the covariance of independent edge signs. The classical unweighted Laplacian spectrum of a two-clique coalescence is not itself the new result; the weighted **vertex covariance**, its sharp global weight optimization, and the resulting anisotropy asymptotics are the subject.

## Proof

**1. Enumerating distinct zonotope vertices.** Every directed cycle in \(G_{a,b}\) is confined to one clique, because a simple cycle cannot traverse an articulation vertex twice. An orientation is therefore acyclic precisely when its restrictions to both cliques are acyclic. The latter are transitive tournaments, hence independently described by a permutation of each clique. Conversely each pair of permutations produces exactly one acyclic orientation, so there are \(a!b!\) distinct vertices. In the centered segment convention, a clique of order \(r\) and edge weight \(w\) contributes the coordinate vector \(w(\pi(i)-(r+1)/2)\) on its vertices, zero elsewhere, where \(\pi\) is the corresponding permutation. The shared coordinate is the sum of the two contributions.

**2. Exact covariance.** For a uniform permutation of \(\{1,\ldots,r\}\), each centered rank has variance \((r^2-1)/12\). By exchangeability and the zero sum of ranks, distinct centered ranks have covariance \(-(r+1)/12\). Thus the whole clique covariance is \((r+1)L_{K_r}/12\), where \(L_{K_r}=rI-J\) on that clique and vanishes off it. The two block permutations are independent. With \(u=(a+1)t^2/12\) and \(v=(b+1)s^2/12\), this yields the exact matrix identity
\[
\boxed{\ C=uL_{K_a}+vL_{K_b}.\ }
\]
Both Laplacians are extended by zero to the union's remaining vertices. Connectivity implies that the kernel of \(C\) is exactly the span of \(\mathbf1\).

**3. Complete spectrum.** On vectors supported in the \(a-1\) nonshared vertices of the first clique with coordinate sum zero, \(C\) acts by \(au=U/12\); this space has dimension \(a-2\). Analogously the other clique gives \(bv=V/12\) of multiplicity \(b-2\). On the remaining three-dimensional invariant space, represented by the values \((z,x,y)\) at the shared vertex, all first-clique nonshared vertices, and all second-clique nonshared vertices, the matrix is
\[
\begin{pmatrix}
(a-1)u+(b-1)v&-(a-1)u&-(b-1)v\\
-u&u&0\\
-v&0&v
\end{pmatrix}.
\]
Its characteristic polynomial is exactly
\[
\lambda\bigl(\lambda^2-(au+bv)\lambda+nuv\bigr).
\]
The resulting roots are \(0\) and \(\lambda_\pm\) as displayed. The discriminant is positive: the quadratic is positive at zero, while its value at each of \(au\) and \(bv\) is
\[
(au)^2-(au+bv)au+nuv
=-(a-1)(b-1)uv<0,
\]
and likewise for \(bv\). This proves
\[
0<\lambda_-<\min\{au,bv\}\le\max\{au,bv\}<\lambda_+.
\]
It establishes both extremal eigenvalues even when an internal contrast space has dimension zero.

**4. Sharp optimal weights and strictness.** Set \(y=u/v>0\). Since \(\lambda_++\lambda_-=au+bv\) and \(\lambda_+\lambda_-=nuv\), the exact identity
\[
\boxed{\ \kappa+2+\kappa^{-1}
=\frac{(ay+b)^2}{ny}
=\frac{4ab}{n}+\frac{(ay-b)^2}{ny}.\ }
\]
holds for every positive \(y\). On \(\kappa>1\), the function \(\kappa\mapsto\kappa+2+\kappa^{-1}\) is strictly increasing. Consequently the unique minimum occurs at \(ay=b\), equivalently at the asserted \(t/s\). With \(ay=b\), the roots of the quadratic yield
\[
\kappa_{\min}
=\frac{\sqrt{ab}+\sqrt{(a-1)(b-1)}}{\sqrt{ab}-\sqrt{(a-1)(b-1)}}
=\frac{(\sqrt{ab}+\sqrt{(a-1)(b-1)})^2}{n},
\]
using \(ab-(a-1)(b-1)=n\). This proves the bound, attainment, and the fact that no other positive ratio attains it. If \(t=s\), optimality requires \(a(a+1)=b(b+1)\), equivalent to \(a=b\) for positive integers.

**5. Imbalanced limit.** For fixed \(a\), put \(b\to\infty\). With unit weights, \(au\) is bounded and \(bv\sim b^2/12\). The quadratic's larger root is therefore asymptotic to \(b^2/12\), while the product relation shows that the smaller root tends to \((a+1)/12\). Hence \(\kappa(1,1)\sim b^2/(a+1)\). In the exact optimized formula, divide the numerator and denominator by \(b\) and take the limit to obtain \((\sqrt a+\sqrt{a-1})^2\). All asymptotics are along positive integers \(b\).

## Verification

A standalone standard-library program is provided at `artifacts/verify.py`. Execute `python3 artifacts/verify.py` from the extracted finding folder. It independently generates vertices as signed edge-incidence vectors from **all global vertex orders**, removes duplicates, computes their centered covariance with exact fractions, and compares every matrix entry with the stated block-Laplacian formula. It also checks contrast eigenspaces, pseudodeterminants via exact elimination, and rational instances of the sharp weight-penalty identity. The observed successful result is `TWO_CLIQUE_WEIGHTED_COVARIANCE_CHECKS_PASSED profiles=6 vertices=2068 covariance_entries=217 tuning_profiles=1014`.

The code tests finitely many small graphs and positive integer edge weights. The all-size spectral formula, uniqueness, and asymptotics are established by the preceding algebraic proof rather than by these finite tests. In particular, no numerical optimization is used as a proof of the unique global minimizer.

## Relationship to prior work

Padrol–Pilaud–Poullot's *Deformed graphical zonotopes* (first public arXiv version November 24, 2021) supplies the graphical-zonotope and permutohedron setting and studies deformation cones; it does not give the weighted vertex-covariance conditioning optimization. Pilaud's *Acyclic reorientation lattices and their lattice quotients* (first arXiv version November 24, 2021) gives acyclic-orientation/vertex correspondences and the block-graph simpliciality setting; its main results concern lattice structures, fans, and quotientopes, not covariance conditioning.

Kling's *On the uniqueness of the Laplacian spectra of coalescence of complete graphs* (2023), Theorem 4, gives the **unweighted** Laplacian spectrum \(\{0,1,a^{(a-2)},b^{(b-2)},n\}\) for the same underlying graph. In particular, the equal-clique and equal-weight covariance spectrum is covered once the classical permutation covariance formula is supplied. This is explicitly **not** claimed as a new special case. For unequal clique edge lengths, the covariance Laplacian carries *distinct, weight-dependent* block coefficients; Kling's eigenvalues do not imply the sharp ratio-dependent conditioning minimum, its uniqueness, or the imbalanced bounded-anisotropy limit without a new weighted calculation. Generic Laplacian spectral methods are an available route to derive the weighted calculation; the novelty claim is limited to the combined exact covariance and its sharp optimization, not to equitable-quotient methodology.

## Limitations

No historical-priority or independent-review certification is asserted. Equivalent weighted coalescence spectral-optimization results might exist in network design or matrix preconditioning literature under different terminology. The results are exact mathematical identities for this two-block family but do not extend to arbitrary block-graph weight assignments by the same two-variable optimization. The measured random object is a uniformly chosen vertex, so its covariance must not be identified with the covariance of a volume-uniform point. The smallest positive covariance eigenvalue tends to zero if one weight tends to zero at fixed other weight; such a boundary is excluded by the strict positivity assumptions.

## References

1. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first public version November 24, 2021. https://arxiv.org/abs/2111.12422
2. Vincent Pilaud, *Acyclic reorientation lattices and their lattice quotients*, arXiv:2111.12387, first public version November 24, 2021; *Annals of Combinatorics* 28 (2024), 1035–1092. https://arxiv.org/abs/2111.12387
3. Gerhard Kling, *On the uniqueness of the Laplacian spectra of coalescence of complete graphs*, *Open Journal of Discrete Applied Mathematics* 6 (2023), 25–39, especially Theorem 4. https://pisrt.org/psr-press/journals/odam/04-vol-6-2023-issue-1/on-the-uniqueness-of-the-laplacian-spectra-of-coalescence-of-complete-graphs/
