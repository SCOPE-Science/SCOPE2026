# Exact vertex-radius spectrum and a nonconcentrating chi-square law for clique-windmill graphical zonotopes

## Finding

Let \(k\ge3\) and \(m\ge2\) be integers. Let \(W_{m,k}\) be the graph obtained by identifying one distinguished vertex (the hub) of \(m\) copies of the complete graph \(K_k\), leaving all other vertices distinct. In standard incidence coordinates, consider the **centered graphical zonotope**
\[
 Z_{m,k}=\sum_{\{u,v\}\in E(W_{m,k})}
 \left[-\tfrac12(e_u-e_v),\tfrac12(e_u-e_v)\right]
 \subset\{x:\textstyle\sum_vx_v=0\}.
\]
Its \((k!)^m\) vertices are assigned **equal counting weight**; this is not uniform Euclidean volume and not normal-cone solid-angle weighting. For a uniformly chosen vertex \(V\), put \(Q=\|V\|_2^2\), \(C_k=k(k^2-1)/12\), and \(\sigma_k^2=(k^2-1)/12\).

**Full exact radial spectrum.** For \(0\le j\le k-1\) put \(b_j=2j-(k-1)\). The generating polynomial recording **four times** squared Euclidean radius is
\[
 \boxed{\displaystyle
 \sum_{v\in\operatorname{Vert}(Z_{m,k})}t^{4\|v\|_2^2}
 =((k-1)!)^m
 \sum_{\substack{a_0,\ldots,a_{k-1}\ge0\\\sum_j a_j=m}}
 \frac{m!}{\prod_ja_j!}\,
 t^{\,m k(k^2-1)/3+(\sum_j a_jb_j)^2-\sum_ja_jb_j^2}.}
\]
All exponents are nonnegative integers. If multiple compositions yield the same exponent, their multiplicities add; this formula consequently determines *every* squared-radius shell and its vertex count.

**Exact moments and limiting law.** For every \(m,k\) in the stated range,
\[
 \boxed{\mathbb EQ=mC_k,\qquad
 \operatorname{Var}(Q)=2m(m-1)\sigma_k^4.}
\]
For each fixed \(k\), as \(m\to\infty\),
\[
 \boxed{\displaystyle
 \frac{Q}{m}\ \xrightarrow{\mathrm d}\
 C_k-\sigma_k^2+\sigma_k^2\chi_1^2.}
\]
Here \(\chi_1^2\) is the square of a standard Gaussian. Thus the normalized squared radius has a **nondegenerate non-Gaussian limit**, with variance tending to \(2\sigma_k^4>0\); uniform vertices do not concentrate on a single Euclidean shell.

For comparison with the known outer-radius problem, the unique minimum enclosing ball is origin-centered and has squared radius
\[
 R^2=mC_k+m(m-1)(k-1)^2/4.
\]
Its exact set of contact points comprises \(2((k-1)!)^m\) vertices, a proportion \(2/k^m\) of all vertices. The radius/contact statement is supplementary; the *new claim* is the complete radial spectrum, its exact variance, and the non-Gaussian limiting vertex-radius law.

## Assumptions and scope

All edges have unit generator length; the norm is the ambient Euclidean norm of the canonical zero-sum incidence realization. The graph has \(1+m(k-1)\) vertices and no edges between distinct non-hub cliques. The parameter \(k\) is held fixed in the limit; the theorem makes no universal assertion for jointly growing \(k,m\). Uniform vertex sampling differs from uniform intrinsic-volume sampling and from sampling a vertex using a random Gaussian normal direction. For \(m=1\), every radius is constant and the stated two-class contact formula is not intended; hence \(m\ge2\).

## Proof

**1. The vertex model.** Every simple cycle of \(W_{m,k}\) lies inside one clique. Consequently an orientation is acyclic precisely when its restriction to each clique is a total-order (transitive) orientation. Conversely every independent choice of a total order in each clique is globally acyclic: a directed cycle would be a simple cycle inside one clique. By the graphical-zonotope/acyclic-orientation correspondence, these are all distinct zonotope vertices. There are \((k!)^m\) of them. Under the uniform counting measure, the clique orders are independent and uniform.

**2. Local Euclidean scores.** For a single clique of size \(k\), the centered signed-edge sum at the vertex in rank \(j+1\), with ranks indexed from \(j=0\) to \(k-1\), is \(j-(k-1)/2\). Indeed each of its \(k-1\) incident signed half-edge generators contributes \(\pm1/2\); their sum is the number below minus the number above, divided by two. The multiset of all local scores is \(\{j-(k-1)/2:0\le j<k\}\), with constant squared sum
\[
 \sum_{j=0}^{k-1}\bigl(j-(k-1)/2\bigr)^2=C_k.
\]
Let \(H_i\) be the local score at the shared hub in clique \(i\). Then \(H_1,\ldots,H_m\) are independent uniforms on that displayed set, each hub position occurring with exactly \((k-1)!\) local orders. Their mean is zero and their variance is \(\sigma_k^2\).

**3. Radial identity and all multiplicities.** All non-hub coordinates belong to a unique clique. Their sum of squares is \(mC_k-\sum_iH_i^2\). The single global hub coordinate is \(S=\sum_iH_i\). Hence
\[
 \boxed{Q=mC_k+S^2-\sum_{i=1}^mH_i^2
 =mC_k+2\sum_{1\le i<j\le m}H_iH_j.}
\]
Writing \(H_i=b_{j_i}/2\) gives the claimed integer formula for \(4Q\). For any tuple of hub-position frequencies \((a_0,\ldots,a_{k-1})\), its \(m\) positions can be arranged in \(m!/\prod a_j!\) ways and the leaf ranks independently in \(((k-1)!)^m\) ways. Summing proves the full generating polynomial. All exponents are nonnegative since they equal four times actual squared norms.

**4. Exact moments.** Centered independence gives \(\mathbb E(H_iH_j)=0\) for distinct indices, so \(\mathbb EQ=mC_k\). In the variance of \(2\sum_{i<j}H_iH_j\), two distinct unordered index pairs have zero covariance: disjoint pairs factor, while pairs sharing one index leave a factor of a mean-zero third variable. Each pair has second moment \(\sigma_k^4\). Therefore \(\operatorname{Var}(Q)=4\binom m2\sigma_k^4=2m(m-1)\sigma_k^4\), with no assumption on a Gaussian approximation.

**5. Limit and nonconcentration.** The classical central limit theorem gives \(S/\sqrt m\Rightarrow N(0,\sigma_k^2)\), while the strong law gives \(m^{-1}\sum_iH_i^2\to\sigma_k^2\) almost surely. The radial identity, continuous mapping and Slutsky's lemma yield the displayed shifted-and-scaled \(\chi_1^2\) limit. Its positive variance \(2\sigma_k^4\) rules out convergence in probability of \(Q/m\) to a constant. The exact variance formula independently supplies the same limiting variance.

**6. Outer contacts.** From the radial identity,
\[
 Q\le mC_k+2\binom m2\bigl((k-1)/2\bigr)^2.
\]
Equality for \(m\ge2\) requires every \(H_i\) to have largest possible modulus and all hub scores to share the same sign; conversely these choices attain equality. There are two sign choices and \(((k-1)!)^m\) independent leaf orders each. The zonotope is centrally symmetric around the origin. A compact centrally symmetric convex body has an origin-centered smallest enclosing ball; its Euclidean center is unique. Strict convexity of squared distance to that center excludes any nonvertex contact. The fraction of contacts follows by dividing by \((k!)^m\).

## Verification

The standalone script `verification/check_windmill.py` reconstructs vertices directly from all oriented edge contributions, with no use of the spectrum formula in the direct reconstruction. It compares the resulting exact integer shell counts to the independent multinomial/rank formula, checks the exact mean, variance, maximal radius and contact count, and confirms there are no duplicate orientation vertices. Tested pairs \((k,m)\) are \((3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(6,2)\): 548,748 total vertices across seven finite cases. Its output is `CLIQUE_WINDMILL_RADII_PASS cases=7 enumerated=548748`. This is a finite consistency check; the proof above is valid for all integers in the assumptions. The limiting distribution follows analytically from the central limit theorem, not from finite simulation.

## Relationship to prior work

Sanchez and Kolesnik (2020) characterize general graph tournament score polytopes, recovering their zonotopal realization, but not Euclidean radial distributions. Padrol, Pilaud and Poullot (2021) establish the general graphical-zonotope deformation framework and recall the classical correspondence between vertices and acyclic orientations. Pešović and Stojadinović (2022) place graphical zonotopes in a family interpolating to graph associahedra and study combinatorial enumerators. Neither inspected complete manuscript treats Euclidean vertex-radius shell counting or a vertex-radius probability law.

The published *Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes* gives a stronger graph-general theorem for the **outer** Euclidean diameter and contact set; the outer-radius formula above is accordingly not presented as an original invariant. Its statement and full mathematical proof do not give the distribution among *all* non-extreme vertices, their quadratic radial variance, or the shifted chi-square limit. The published *Universal inertia and covariance laws for cactus graphical zonotopes* studies **uniform intrinsic Euclidean volume** rather than the discrete uniform-vertex measure considered here, and its inertia value does not imply the displayed vertex-radius law. A search for equivalent squared-length, orientation-score and hub-rank formulations found no stronger direct coverage, but historical priority remains provisional.

## Limitations

The formula relies on unit-weight complete cliques sharing exactly one hub, and on uniform sampling of all zonotope vertices; weighted petals, multi-hub joins and other sampling measures may behave differently. The limiting law fixes clique size. No claim is made that the circumradius or its equality classification is new, that finite enumeration proves an infinite theorem, or that the comparison exhausts differently indexed prior literature. Independent mathematical audit has not been performed.

## References

1. M. Sanchez, B. Kolesnik, *The geometry of random tournaments*, first public arXiv posting 2020-09-19, arXiv:2009.09322, Sections 1–3. https://arxiv.org/abs/2009.09322
2. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, first public arXiv posting 2021-11-24, arXiv:2111.12422, Sections 1.3 and 2. https://arxiv.org/abs/2111.12422
3. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053, first public posting 2022-09-24, Section 2. https://arxiv.org/abs/2209.12053
4. *Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes*, publicly indexed mathematical result (2026-10-11), identifier `19096c28cee4`; its full `RESULT.md` covers outer radius and contact sets, not radial vertex distributions.
5. *Universal inertia and covariance laws for cactus graphical zonotopes*, publicly indexed mathematical result (2026-11-08), identifier `4688476ceb85`; its full `RESULT.md` addresses uniform-volume rather than uniform-vertex moments.
