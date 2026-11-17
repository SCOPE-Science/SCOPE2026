# Exact Euclidean inballs and center ranks for mixed-arm spider free spaces

## Finding

Let \(p\ge 1\) and \(q\ge 2\) be integers. The mixed-arm spider \(T_{p,q}\) is a tree with root \(o\), \(p\) unit edges \(ox_j\), and \(q\) disjoint two-edge arms \(o v_i w_i\); every edge has length one. Its shortest-path metric has \(N=1+p+2q\) vertices. Let \(K_{p,q}\) be the real Lipschitz-free unit ball in the canonical coordinate realization
\[
 H=\{z\in\mathbb R^{V(T_{p,q})}:\sum_vz_v=0\},\quad
 K_{p,q}=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(T_{p,q})\}.
\]
All Euclidean norms and radii below use the Euclidean structure inherited by \(H\), not an arbitrary isometric Banach-space coordinate change.

Define
\[
 d_{p,q}=\begin{cases}
 2,&p=1\text{ and }q\text{ is odd},\\
 0,&p+q\text{ is even and not in the preceding case},\\
 1,&p+q\text{ is odd}.
 \end{cases}
\]
Then the globally maximal radius of an inscribed Euclidean ball is
\[
 \boxed{r_{p,q}=\left(p+5q-\frac{d_{p,q}^{2}}{1+p+2q}\right)^{-1/2}}.
\]
The origin is an optimal center. All facets of \(K_{p,q}\) have extreme polar normals given by independently signed edge increments. A facet contacts the origin-centered optimal ball **if and only if** each two-edge arm has the same sign on its two edges and its signed arm totals have absolute imbalance \(d_{p,q}\), as made precise below.

Put
\[
 \mathcal S_{p,q}=\bigl\{(a,b):a\in\{-q,-q+2,\ldots,q\},\ 
 b\in\{-p,-p+2,\ldots,p\},\ |3a+b|=d_{p,q}\bigr\}.
\]
The exact number of contacting facets is
\[
 \boxed{C_{p,q}=\sum_{(a,b)\in\mathcal S_{p,q}}
 \binom{q}{(q+a)/2}\binom{p}{(p+b)/2}}.
\]
To determine the **entire affine dimension of the maximum-ball center set** \(\mathcal I_{p,q}\), define \(\eta_q=1\) if some \((a,b)\in\mathcal S_{p,q}\) has \(|a|<q\), and zero otherwise; define \(\eta_p\) analogously by \(|b|<p\). Let
\[
 R_{p,q}=\dim_{\mathbb R}\operatorname{span}\{(a,b):(a,b)\in\mathcal S_{p,q}\}\in\{0,1,2\}.
\]
Then
\[
 \boxed{\dim\operatorname{aff}\mathcal I_{p,q}=
 p+2q-\bigl[(q-1)\eta_q+(p-1)\eta_p+R_{p,q}\bigr].}
\]
These are finite closed binomial and two-dimensional rank formulas, with no optimization over an exponential family required.

For the particularly transparent fixed size \(p=3\), the center-locus dimension and contact count have different parity laws:
\[
\begin{array}{c|c|c|c}
 &r_{3,q}^{-2}&C_{3,q}&\dim\operatorname{aff}\mathcal I_{3,q}\\\hline
q\text{ even}&5q+3-1/(2q+4)&6\binom{q}{q/2}&q+1\\
q\text{ odd}&5q+3&2\binom{q}{(q-1)/2}&q+3
\end{array}
\]
Here \(q\ge2\), so the odd case begins at \(q=3\). Thus changing the parity changes the center-locus dimension by two relative to the baseline in this natural infinite subfamily.

## Assumptions and scope

The domain is precisely the unweighted shortest-path metric on the finite tree described above, \(p\ge1\), \(q\ge2\), over the real field. No statements are asserted for arbitrary weighted trees, longer arms, or a different Euclidean embedding. The unit ball of a real Lipschitz-free space over a tree has the stated symmetric-edge presentation: every nonedge molecule is a convex combination of unit-edge molecules along its unique geodesic.

The center locus \(\mathcal I_{p,q}\) consists of all \(c\in H\) for which the translated Euclidean ball \(c+r_{p,q}B_2(H)\) lies in \(K_{p,q}\). The formula determines its affine dimension, not a volume or explicit vertex presentation of the center polytope.

## Proof

**1. All facet normals.** The polar ball is
\[
 K_{p,q}^{\circ}=\{f\in H:|f_u-f_v|\le1\text{ for every edge }uv\}.
\]
Set the root potential to zero before orthogonally projecting onto \(H\). Since the tree has \(p+2q\) edges and the rooted edge-increment map is an invertible linear map, \(K_{p,q}^{\circ}\) is an affine image of a cube. Every polar vertex is uniquely specified by choosing each edge increment independently in \(\{-1,1\}\). These \(2^{p+2q}\) vertices are precisely the outward facet normals of \(K_{p,q}\) with supporting value one.

**2. Centered squared norm.** Write the \(p\) short-leaf potentials as \(r_j\in\{-1,1\}\). On each long arm the internal and tip potentials are \((s_i,s_i+t_i)\) with \(s_i,t_i\in\{-1,1\}\). A *straight* arm has \(t_i=s_i\), giving values \((s_i,2s_i)\), sum \(3s_i\), and sum of squares \(5\). A *returning* arm has \(t_i=-s_i\), giving \((s_i,0)\), sum \(s_i\), and sum of squares \(1\). For any such rooted potential \(u\), the squared norm of the centered polar normal is exactly
\[
 \|u-\overline u\mathbf1\|_2^2
 =\sum_{v\ne o}u_v^2-\frac{1}{N}\left(\sum_{v\ne o}u_v\right)^2,
 \qquad \overline u=N^{-1}\sum_v u_v.
\]

**3. Every maximizer is straight.** Fix all other arms and write \(X\in\mathbb Z\) for their total potential sum. Replacing one returning arm by either straight orientation changes the sum of squares by \(+4\). The smallest possible squared total sum after replacement is \((|X|-3)^2\), whereas the smallest squared total sum among the two possible returning orientations is \((|X|-1)^2\). Consequently the replacement admits a gain in centered squared norm of at least
\[
 4-\frac{(|X|-3)^2-(|X|-1)^2}{N}
 =4-\frac{8-4|X|}{N}\ge4-\frac8N>0,
\]
since \(N\ge6\). Replacing every returning arm increases the centered norm strictly. Therefore every maximal polar norm is attained **only** by straight long arms.

**4. Exact imbalance.** For straight arms put \(a=\sum_i s_i\) and \(b=\sum_jr_j\). The squared centered polar norm becomes
\[
 \|f\|_2^2=p+5q-\frac{(3a+b)^2}{N}.
\]
The allowed integer sums have the parities of \(q\) and \(p\), respectively. For even \(q\), taking \(a=0\) and taking \(b=0\) or \(\pm1\) achieves the smallest permitted parity. For odd \(q\) with \(p\ge2\), take \(a=\pm1\) and \(b=\mp3\) when \(p\) is odd (necessarily at least three), or \(b=\mp2\) when \(p\) is even. For \(p=1\) and odd \(q\), the smallest attainable absolute value is two. Thus the minimum is exactly \(d_{p,q}\); substituting proves the radius formula. A centrally symmetric convex body has an origin-centered maximal inball: translating an inball of radius \(r\) to its negative and taking the midpoint yields an origin-centered inball of the same radius.

**5. Contacts and centers.** A facet with normal \(f\) is at distance \(1/\|f\|_2\) from the origin, so steps 3–4 identify all contacts. For a given pair \((a,b)\), the number of choices of signs is the indicated binomial product; summing yields \(C_{p,q}\).

If \(c\) is any center of a radius-\(r_{p,q}\) inball, every maximal normal \(f\) and its antipode \(-f\) require \(\langle f,c\rangle=0\). Conversely, all other finitely many facet inequalities have strict slack at \(c=0\), so sufficiently small vectors perpendicular to the contact-normal span are also optimal centers. Hence the affine dimension is \(p+2q\) minus the rank of the contact normals.

On straight arms, each contact normal is the centered image of an arm-sign vector \((s_1,\ldots,s_q,r_1,\ldots,r_p)\) via an injective linear map. Its span is invariant under independent permutations of the long and short arms. Under these permutation groups, the coordinate space decomposes as the two within-group zero-sum subspaces plus the two-dimensional space of groupwise-constant vectors. A group contributes its whole zero-sum subspace if and only if some contact has mixed signs there, yielding \((q-1)\eta_q\) and \((p-1)\eta_p\). Averaging contact sign vectors within each group shows that the remaining span has rank precisely \(R_{p,q}\). This proves the dimension formula. Substituting the two explicit contact-sum classes for \(p=3\) gives the parity table.

## Verification

`CHECKER.py` uses Python 3 and SymPy (exact integer and rational arithmetic); run `python CHECKER.py` after installing SymPy. It independently enumerates **every** signed edge potential for 30 mixed-arm spiders with \(2\le q\le6\), \(1\le p\le11\), and \(p+2q\le14\), totaling 152,928 potentials. It computes centered norms, maximizing counts, and direct exact contact-normal ranks, and compares all results with the three formulas above. It also prints representative boundary and parity profiles. Finite checks corroborate but do not prove the infinite formulas; the proof above is independent of this enumeration.

## Relationship to prior work

Godard, *Tree metrics and their Lipschitz-free spaces* (2009), identifies the Banach-space connection between tree metrics and \(L_1\). Higashitani, Jochemko, and Michałek, *Arithmetic aspects of symmetric edge polytopes* (first public version July 20, 2018), give the connected tight-edge criterion for facets of symmetric edge polytopes. Alexander, Fradelizi, García-Lirola, and Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces* (first public version November 24, 2019), prove, among other things, the tree/affine-crosspolytope characterization. These general structural results do not specify the canonical Euclidean inradius or the center-locus rank for mixed-arm spiders.

The all-long-arm subdivided-star case and the diameter-three bistar case are separate special families. The present domain requires **both** short arms and at least two length-two arms, so it is neither of those families. The new content is the strict straight-arm screening principle in this heterogeneous family and the exact parity-sensitive norm, contact, and optimal-center-rank classification.

## Limitations

The proof concerns the intrinsic inherited Euclidean metric, not the Banach–Mazur distance to Hilbert space or the volume product; these are different invariants. It does not classify all faces of the optimal-center polytope, only its affine dimension. An equivalent prior result under a different optimization or finite-metric terminology cannot be excluded absolutely; nearby research on spiders and bistars makes this a relevant priority risk. No independent audit or external mathematical certification is claimed.

## References

- A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178 (2009), https://arxiv.org/abs/0904.3178.
- A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018), Theorem 3.1, https://arxiv.org/abs/1807.07678.
- M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), Proposition 2.6 and Section 3, https://arxiv.org/abs/1911.10642.
