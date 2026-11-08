# Sharp simplex-John saturation for partial permutohedra

## Finding

For positive integers \(m,n\), let \(\mathcal P(m,n)\subset\mathbb R^m\) be the convex hull of vectors in \(\{0,1,\ldots,n\}^m\) having distinct positive entries. Define
\[
S_{m,n}=\sum_{j=0}^{\min(m,n)-1}(n-j),\qquad
T_{m,n}=\{x\in\mathbb R^m:x_i\ge0,\ \sum_{i=1}^m x_i\le S_{m,n}\}.
\]
The unique maximum-volume ellipsoid of \(\mathcal P(m,n)\) coincides with that of its containing simplex \(T_{m,n}\) **if and only if** \(m=1\) or \(m\ge n\). The transition is sharp: for every \(2\le m<n\), the simplex John ellipsoid fails the defining coordinate cap \(x_i\le n\), and \(\mathcal P(m,n)\) has strictly smaller maximal inscribed-ellipsoid volume.

In the saturation range \(m\ge n\), put \(S=n(n+1)/2\), \(\mathbf 1=(1,\ldots,1)^\mathsf T\), and \(J=\mathbf 1\mathbf 1^\mathsf T\). The John ellipsoid is exactly
\[
E_{m,n}=\left\{c+A^{1/2}u:\|u\|_2\le1\right\},\qquad
c=\frac{S}{m+1}\mathbf1,\qquad
A=\frac{S^2}{m(m+1)}\left(I-\frac{J}{m+1}\right).
\]
Its \(m\)-dimensional Euclidean volume is
\[
\operatorname{vol}_m(E_{m,n})=
\frac{\kappa_m S^m}{m^{m/2}(m+1)^{(m+1)/2}},
\qquad \kappa_m=\frac{\pi^{m/2}}{\Gamma(m/2+1)}.
\]
For \(m>n\), exactly the \(m\) nonnegativity facets and the total-sum facet are tangent, at \(m+1\) distinct points. On the sharp boundary \(m=n\ge2\), exactly the \(m\) additional singleton caps \(x_i=n\) become tangent, producing \(2m+1\) distinct contact points; other proper subset-sum facets remain strictly separated. At \(m=n=1\) there are two contacts, not three.

## Assumptions and scope

All dimensions and parameters are positive integers. The Euclidean metric on \(\mathbb R^m\) is the ordinary coordinate metric. The word *John ellipsoid* means the unique ellipsoid of maximum full-dimensional Euclidean volume contained in the given convex polytope. For \(m\ge n\), the total coordinate sum of a vertex of \(\mathcal P(m,n)\) is at most \(S=n(n+1)/2\). The formula is for the original coordinate realization of the partial permutohedron, not a translated parking-function realization. Facet-contact counts refer to supporting facets, with coincident facets counted once.

## Proof

**1. Facet description.** The established subset-sum description of partial permutohedra [1, Proposition 2.8] states that \(x_i\ge0\) and
\[
\sum_{i\in U}x_i\le B_{|U|},\qquad
B_s=\sum_{j=0}^{\min(s,n)-1}(n-j).
\]
The inequalities for \(|U|\ge n\) are implied by nonnegativity and the total-sum bound; the irredundant upper facets have \(1\le |U|\le n-1\) and \(|U|=m\) (with the obvious duplication removed). These inequalities show \(\mathcal P(m,n)\subseteq T_{m,n}\).

**2. Ellipsoid of the containing simplex.** Map \(T_{m,n}\) to the standard \(m\)-simplex with barycentric coordinates \(\lambda_0=1-\sum_i x_i/S_{m,n}\), \(\lambda_i=x_i/S_{m,n}\). In the hyperplane \(\sum_{i=0}^m\lambda_i=1\) its vertices are the coordinate vectors. Permutation invariance and uniqueness force the John ellipsoid to be the ball centered at \(\lambda_i=1/(m+1)\), whose radius is its distance to any facet, \(1/\sqrt{m(m+1)}\). Pulling back gives the above \(c\) and \(A\) with \(S\) replaced by \(S_{m,n}\). In particular, for an indicator vector \(\mathbf1_U\) of a set of cardinality \(s\), the support of the simplex ellipsoid is
\[
H_m(s)=\frac{S_{m,n}}{m+1}
\left(s+\sqrt{\frac{s(m+1-s)}{m}}\right).
\]
For every coordinate \(i\), this gives \(\max_E x_i=2S_{m,n}/(m+1)\).

**3. Exact saturation when \(m\ge n\).** In this range \(S_{m,n}=S\) is independent of \(m\). Fix \(1\le s\le n\). The function \(H_m(s)\) decreases strictly with real \(m\ge s\). Indeed, putting \(q(m)=\sqrt{s(1-(s-1)/m)}\) gives \(q(m)\ge1\) and
\[
q'(m)=\frac{s(s-1)}{2m^2q(m)},\qquad
(m+1)q'(m)\le\frac{s(m^2-1)}{2m^2}<s<s+q(m).
\]
Differentiating \((s+q(m))/(m+1)\) therefore gives a strictly negative derivative. It is enough to check the strongest case \(m=n\): there \(S=n(n+1)/2\) and
\[
H_n(s)=\frac n2\left(s+\sqrt{\frac{s(n+1-s)}n}\right)
\le\frac{s(2n-s+1)}2=B_s.
\]
The inequality is equivalent, after squaring positive sides, to \(n\le s(n+1-s)\), true for integers \(1\le s\le n\) because \((s-1)(n-s)\ge0\). Equality occurs only at \(s=1\) or \(s=n\). Thus for \(m\ge n\), every upper subset-sum inequality of cardinality \(s\le n\) contains the entire simplex ellipsoid. For \(n<s<m\), the upper bound is \(S\), while \(H_m(s)<S\) because \(\sqrt{s(m+1-s)/m}<m+1-s\); at \(s=m\) equality holds. Consequently the simplex John ellipsoid lies in \(\mathcal P(m,n)\). Since \(\mathcal P(m,n)\subseteq T_{m,n}\), maximum-volume uniqueness for the simplex proves it is also the unique John ellipsoid of \(\mathcal P(m,n)\).

**4. Sharp failure below the threshold.** When \(2\le m<n\), the total-sum bound is \(S_{m,n}=m(2n-m+1)/2\). The simplex John ellipsoid has support in the direction of coordinate \(i\) equal to
\[
\frac{2S_{m,n}}{m+1}=n+\frac{(m-1)(n-m)}{m+1}>n,
\]
violating the valid facet inequality \(x_i\le n\). It therefore cannot be the John ellipsoid of \(\mathcal P(m,n)\). Strict inequality of optimal ellipsoid volumes follows from uniqueness for \(T_{m,n}\), compactness of the inscribed-ellipsoid maximization problem, and the strict violation. For \(m=1\), \(\mathcal P(1,n)=[0,n]=T_{1,n}\), giving the claimed exception.

**5. Contact and volume assertions.** The simplex ellipsoid touches the \(m\) coordinate lower facets and the total-sum facet, each at one distinct point. The strictness calculations above show that at \(m>n\) no additional upper facet touches. At \(m=n\ge2\), the \(m\) singleton upper facets additionally touch because \(H_n(1)=n\), and all higher proper subset upper facets have strict inequality. The singleton upper point in direction \(i\) is \(x_i=n\) and \(x_j=(n-1)/2\) for \(j\ne i\), distinct from the original facet tangencies. The eigenvalues of \(A\) are \(S^2/[m(m+1)^2]\) once, along \(\mathbf1\), and \(S^2/[m(m+1)]\) with multiplicity \(m-1\); their product gives the displayed volume formula.

## Verification

Run `python3 verify.py` using Python's standard library. The standalone script performs 110526 exact integer/rational assertions: across \(1\le m,n\le45\), it checks the support inequalities using squared rational comparisons, all asserted equality cases and strict failures; separately for \(m,n\le4\), it reconstructs every vertex of \(\mathcal P(m,n)\) and tests the subset-sum bounds and maximizing directions. The final marker is `VERIFY_OK exact_assertions=110526`. Finite tests are corroborating checks only; the proof above establishes the result for all positive integer parameters.

## Relationship to prior work

The existence, vertex, and subset-sum facet descriptions of \(\mathcal P(m,n)\) are established in [1], and the classical John ellipsoid of a simplex is not new [3,4]. The 2026 study [2] proves Ehrhart magic positivity for a substantial parameter range, motivating exact geometry in the complementary regimes, but its reviewed results do not give a John-ellipsoid classification. Earlier computations of Euclidean inballs and enclosing ellipsoids concern different extremal optimization problems and do not imply that a non-spherical maximum-volume ellipsoid survives every subset-sum truncation. The original assertion here is the sharp two-parameter simplex-John saturation and the additional facet-contact transition at equality.

## Limitations

The theorem does not determine the John ellipsoid within the nonsaturation regime \(2\le m<n\); it proves that its volume is strictly smaller than that of the associated simplex. It does not address affine or metric deformations of partial permutohedra. This mathematical comparison is not an independent historical-priority or formal proof audit; less accessible prior work could contain equivalent facts.

## References

[1] R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253v3, Proposition 2.8, Sections 2–3 and 5. https://arxiv.org/abs/2207.14253

[2] F. Liu and Z. Zhang, *Magic Positivity for the Ehrhart Polynomials of Partial Permutohedra*, arXiv:2607.03854v1 (first public July 4, 2026), Theorems 1.3 and 1.6. https://arxiv.org/abs/2607.03854

[3] S. Lin, X. Ge, and G. Leng, *The John Theorem for Simplex*, arXiv:1001.4223. https://arxiv.org/abs/1001.4223

[4] A. Eydelzon, *From the Steiner Inellipse to the John Ellipsoid of a Simplex: A Corner-Volume Characterization*, arXiv:2609.08045v1. https://arxiv.org/abs/2609.08045
