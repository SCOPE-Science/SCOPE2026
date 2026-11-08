# The White Whale zonotope has a nondegenerate segment of Euclidean incenters in every dimension

## Finding

For every integer \(d\ge2\), let the White Whale zonotope be
\[
W_d=\sum_{\emptyset\ne S\subseteq[d]}[0,\mathbf1_S]\subset\mathbb R^d,
\qquad \sigma_d=2^{d-2}\mathbf1.
\]
All distances below are ordinary ambient Euclidean distances. Its largest inscribed-ball radius is exactly
\[
r_d=\frac{2^{d-2}}{\sqrt2}.
\]
The complete set of centers of largest inscribed balls is a **nondegenerate one-dimensional segment**
\[
\boxed{\ \operatorname{Inc}(W_d)=\{\sigma_d+t\mathbf1:|t|\le\theta_d\}\ },
\]
with the following fully finite, exact description of its positive half-length. Put
\[
B_d=\{0,1\}^d\setminus\{0\},\qquad
h_d(a)=\frac12\sum_{v\in B_d}|a\cdot v|.
\]
Let \(\mathcal R_d\) contain one choice of primitive integer normal from each unoriented line that is the common nullspace of \(d-1\) linearly independent members of \(B_d\). Then
\[
\boxed{\ \theta_d=
\min_{\substack{a\in\mathcal R_d\\ a\cdot\mathbf1\ne0}}
\frac{h_d(a)-r_d\|a\|_2}{|a\cdot\mathbf1|}>0.\ }
\]
This formula determines both endpoints using finitely many integer nullspace computations and radicals, without any enumeration of zonotope vertices. In low dimensions, exhaustive exact arithmetic yields
\[
\theta_2=1-\frac1{\sqrt2},\qquad
\theta_d=2^{d-3}(3-\sqrt6)\quad\text{for }d=3,4,5.
\]
The facets touched by the ball centered at \(\sigma_d\) have exactly the \(d(d-1)\) oriented unit normals
\[
\frac{e_i-e_j}{\sqrt2}\quad(i\ne j).
\]
No other facet touches this centrally placed maximal ball. At either endpoint of the incenter segment, exhaustive exact checks show **two additional facet contacts** when \(d=2\), and exactly \(3\binom d3\) additional contacts when \(d=3,4,5\), with endpoint-contact normals proportional to permutations of \((1,1,-1,0,\ldots,0)\).

## Assumptions and scope

The generator set contains exactly one segment \([0,\mathbf1_S]\) for each nonempty subset \(S\subseteq[d]\), with coefficient one and no multiplicities or additional weights. The metric is the ordinary Euclidean metric of \(\mathbb R^d\), not a lattice or affine-invariant metric. The finite radical expression for \(\theta_d\) applies in every integer dimension \(d\ge2\); the simple closed forms displayed for \(d\le5\) are not asserted for larger dimensions.

## Proof

**Center and support.** Each coordinate appears in \(2^{d-1}\) generators, so the symmetry center is \(\sigma_d=2^{d-2}\mathbf1\). After translation by \(-\sigma_d\), the body is
\[
Z_d=\sum_{v\in B_d}[-v/2,v/2],\qquad h_{Z_d}(u)=h_d(u).
\]
For a centrally symmetric convex body, averaging a contained ball and its reflected ball proves that the same radius is attained at the symmetry center. The optimal radius is therefore \(\min_{\|u\|_2=1}h_d(u)\).

**The sharp radius and equality.** Let \(\varepsilon_i\) be independent unbiased signs and \(s=\sum_i u_i\). Pairing the two signs of their sum yields
\[
h_d(u)=2^{d-2}\,\mathbb E\left|s+\sum_i\varepsilon_i u_i\right|
=2^{d-2}\,\mathbb E\max\left\{|s|,\left|\sum_i\varepsilon_i u_i\right|\right\}.
\]
Szarek's sharp scalar \(L^1\) Khinchin inequality gives \(\mathbb E|\sum_i\varepsilon_i u_i|\ge\|u\|_2/\sqrt2\). Equality in its nonzero case requires exactly two coefficients of equal absolute value; one route to this equality characterization is Haagerup's coefficient-wise lower bound with its strictly increasing special function for coefficients of size at most \(1/\sqrt2\), combined with the elementary maximum-coefficient case. Thus \(h_d(u)\ge r_d\|u\|_2\). Equality also requires the shift \(s\) not to increase the expectation. Equal-sign two-coefficient vectors have \(|s|>0\) and a positive probability of zero random-sign sum, so the inequality is then strict. Opposite equal coefficients give \(s=0\) and equality. The full set of unit minimizers is therefore precisely \(\{(e_i-e_j)/\sqrt2:i\ne j\}\).

**Actual facets and center rigidity.** For a normal \(e_i-e_j\), the generators lying in its kernel are those with identical entries in coordinates \(i,j\). They span the \((d-1)\)-dimensional hyperplane: the independent vectors \(e_k\) for \(k\ne i,j\), together with \(e_i+e_j\), are among them. Consequently the associated support face is a facet, and the above directions give all facets at distance \(r_d\) from \(\sigma_d\). If \(B(c,r_d)\subseteq Z_d\), the two support inequalities for each opposite pair of these normals imply \(c_i=c_j\) for all indices. Hence \(c=t\mathbf1\) for some real \(t\).

**Exact endpoints.** Such a ball is contained in \(Z_d\) if and only if
\[
r_d\|u\|_2+|t|\,|u\cdot\mathbf1|\le h_d(u)\qquad\text{for every }u\in\mathbb R^d.
\]
The hyperplanes \(\{v\cdot u=0:v\in B_d\}\) form a central, pointed polyhedral fan, because every coordinate vector belongs to \(B_d\). On each cone its support function is linear. Refine the fan by the additional hyperplane \(u\cdot\mathbf1=0\), so the absolute-value term is also linear. Every ray of the refinement with nonzero coordinate sum is already an extremal ray of the original arrangement, hence belongs, up to sign and positive multiple, to \(\mathcal R_d\); rays introduced by the refinement have zero coordinate sum. If the displayed inequality holds for these rays, it holds throughout every cone: the left support terms are linear there, while \(\|\sum_j\alpha_j u_j\|_2\le\sum_j\alpha_j\|u_j\|_2\) for nonnegative conic coefficients. This proves the exact finite minimum formula for \(\theta_d\). The minimum is over a nonempty finite set and is strictly positive, since all radius-equality rays have zero coordinate sum. Necessity follows by testing each original ray.

**Low-dimensional endpoints.** To specialize the finite formula, enumerate all independent \((d-1)\)-tuples of binary generators and reduce their cofactor normals to primitive integers. All such rays are checked in the standalone exact checker for \(d=2,3,4,5\). The minimizers occur at a coordinate vector for \(d=2\) and at permutations and negations of \((1,1,-1,0,\ldots,0)\) for \(d=3,4,5\). Substitution gives the stated exact radicals. For these dimensions the cofactor check also establishes that the only rays attaining the endpoint bound are the two coordinate normals when \(d=2\), and the \(3\binom d3\) unoriented signed-three-coordinate normals when \(d=3,4,5\). Each is a facet normal because the zero generators span its orthogonal hyperplane; the specific orientation tangent to a positive endpoint has positive coordinate sum.

## Verification

Run `python3 white_whale_checker.py`. It enumerates all \((d-1)\)-row selections among the \(2^d-1\) nonzero binary generators for each \(d=2,3,4,5\), reduces integer cofactor normals to unoriented primitive rays, and proves the candidate endpoint inequalities using rational integer-square-root enclosures. True equality cases are separately resolved by symbolic integer identities. The number of unique unoriented ray lines is respectively \(3,9,45,625\). It also verifies the sharp centered facet directions and, for each low dimension, proves strict endpoint slack on every ray other than the explicitly identified extra tangent facets. The general all-dimensions radius, center segment, and finite-ray formula are analytic and do not depend on these finite tests.

## Relationship to prior work

Deza, Hao, and Pournin define this White Whale zonotope and study its vertex and edge enumeration and the resonance arrangement; those results provide the exact generator family and polyhedral context. The sharp Szarek Khinchin inequality, discussed with proof ingredients and stability extensions by Eskenazis, Nayar, and Tkocz, supplies the known probability inequality from which the centered radius follows. The radius alone is therefore not proposed as a standalone novelty. The claimed additional geometric information is the *complete positive-dimensional incenter locus*, its explicit finite resonance-ray endpoint formula, and the exhaustive centered tangent-facet characterization. The examined White Whale source does not state these metric results; the examined sharp-inequality source does not classify centers of this zonotope.

## Limitations

No simple closed form for \(\theta_d\) is established here for \(d\ge6\); the exact finite radical optimization formula, not an extrapolation from the first four dimensions, is the general conclusion. This is a self-review, not an independently audited or certified research result. Historical originality remains provisional: an equivalent geometric formulation could exist outside the inspected sources.

## References

- A. Deza, M. Hao, and L. Pournin, *Sizing the White Whale*, arXiv:2205.13309v1 (public 2022-05-26), https://arxiv.org/html/2205.13309v1.
- A. Eskenazis, P. Nayar, and T. Tkocz, *Distributional stability of the Szarek and Ball inequalities*, published 2023-07-15, https://doi.org/10.1007/s00208-023-02669-9.
- S. Szarek, *On the best constant in the Khintchine inequality*, Studia Mathematica 58 (1976), 197–208; used as classical input rather than a claimed new inequality.
