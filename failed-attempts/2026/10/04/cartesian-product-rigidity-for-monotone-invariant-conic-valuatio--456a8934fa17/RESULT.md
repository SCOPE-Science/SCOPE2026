# Cartesian-product rigidity for monotone invariant conic valuations
## Finding
For every family \( (\mu_d)_{d\ge 1} \) in which \(\mu_d\) is a real-valued monotone \(\mathrm O(d)\)-invariant valuation on the closed convex cones of \(\mathbb R^d\) and \(\mu_{d+e}(C\times D)=\mu_d(C)+\mu_e(D)\), there are unique \(\alpha\in\mathbb R\) and \(\gamma\ge0\) such that \(\mu_d(C)=\alpha d+\gamma\,\delta(C)\) for every \(d\) and \(C\), where \(\delta(C)=\sum_{k=0}^d k\,v_k(C)\) is statistical dimension. Conversely every such pair defines a family with these properties. In particular, the two one-dimensional normalizations \(\mu_1(\{0\})=0\) and \(\mu_1(\mathbb R)=1\) force \(\mu_d=\delta\) in every dimension.

This converts the dimension-by-dimension classification of monotone invariant conic valuations into a cross-dimensional rigidity theorem. The normalized conclusion characterizes statistical dimension using only valuation, monotonicity, orthogonal invariance, Cartesian-product additivity, and two one-dimensional anchor values; no continuity or calibration on all linear subspaces is assumed.

## Assumptions and scope
For each integer \(d\ge1\), let \(\mathcal C_d\) be the closed convex cones in \(\mathbb R^d\). A family \( (\mu_d)_{d\ge1} \) is assumed to satisfy all of the following.

1. Each \(\mu_d:\mathcal C_d\to\mathbb R\) is a valuation: whenever \(C,K,C\cup K\in\mathcal C_d\),
   \[\mu_d(C\cup K)+\mu_d(C\cap K)=\mu_d(C)+\mu_d(K).\]
2. Each \(\mu_d\) is monotone under inclusion and invariant under \(\mathrm O(d)\).
3. The family is additive under Cartesian products: for every \(d,e\ge1\), \(C\in\mathcal C_d\), and \(D\in\mathcal C_e\),
   \[\mu_{d+e}(C\times D)=\mu_d(C)+\mu_e(D).\]

Write \(v_0,\ldots,v_d\) for the conic intrinsic volumes and
\[\delta(C)=\sum_{k=0}^d k\,v_k(C).\]
The primary recent input is Lotz's classification of monotone rotation-invariant valuations on all closed convex cones. Its verified primary MSC is 52A55 and its first public version is dated 2026-09-08.

## Proof
Set
\[\alpha:=\mu_1(\{0\}),\qquad \beta:=\mu_1(\mathbb R).\]
In one dimension the closed convex cones are \(\{0\}\), the two rays, and \(\mathbb R\). Orthogonal invariance makes the two ray values equal. Applying the valuation identity to the union of the two opposite rays gives
\[\mu_1(\mathbb R)+\mu_1(\{0\})=2\mu_1(\mathbb R_+).\]
Thus \(\mu_1=\alpha v_0+\beta v_1\). Since \(\{0\}\subset\mathbb R\), monotonicity gives \(\alpha\le\beta\).

For every \(d\ge2\), Lotz's Theorem 1.1 gives unique coefficients \(a_{d,0}\le\cdots\le a_{d,d}\) such that
\[\mu_d(C)=\sum_{k=0}^d a_{d,k}v_k(C).\]
For a \(k\)-dimensional linear subspace \(L_k\subset\mathbb R^d\), the intrinsic volumes satisfy \(v_j(L_k)=1\) when \(j=k\) and vanish otherwise, so
\[a_{d,k}=\mu_d(L_k).\]
Any such subspace is orthogonally congruent to the Cartesian product of \(k\) copies of \(\mathbb R\) and \(d-k\) copies of \(\{0\}\). Repeated product additivity therefore gives
\[a_{d,k}=k\beta+(d-k)\alpha=\alpha d+(\beta-\alpha)k.\]
Using \(\sum_k v_k(C)=1\),
\[
\begin{aligned}
\mu_d(C)
&=\sum_{k=0}^d\bigl(\alpha d+(\beta-\alpha)k\bigr)v_k(C)\\
&=\alpha d+(\beta-\alpha)\sum_{k=0}^d k\,v_k(C)\\
&=\alpha d+(\beta-\alpha)\delta(C).
\end{aligned}
\]
Set \(\gamma=\beta-\alpha\ge0\). This proves necessity and uniqueness of \(\alpha,\gamma\), since they are recovered from the two one-dimensional values.

Conversely, fix \(\alpha\in\mathbb R\) and \(\gamma\ge0\), and define
\[\mu_d(C)=\alpha d+\gamma\delta(C).\]
For fixed \(d\), this is the intrinsic-volume combination with coefficients \(\alpha d+\gamma k\), which are nondecreasing in \(k\); Lotz's theorem therefore gives valuation, monotonicity, and orthogonal invariance. The conic intrinsic-volume product rule
\[v_m(C\times D)=\sum_{i+j=m}v_i(C)v_j(D)\]
and \(\sum_i v_i=1\) imply
\[
\delta(C\times D)
=\sum_{i,j}(i+j)v_i(C)v_j(D)
=\delta(C)+\delta(D),
\]
so the family is Cartesian-product additive.

Finally, if \(\mu_1(\{0\})=0\) and \(\mu_1(\mathbb R)=1\), then \(\alpha=0\), \(\beta=1\), hence \(\gamma=1\), and \(\mu_d=\delta\) for every \(d\).

## Verification
The proof has no finite-enumeration step. The nonstandard input was checked directly in the full text of Lotz's arXiv:2609.09335: Theorem 1.1 supplies the intrinsic-volume representation with nondecreasing coefficients, and the preliminaries state \(v_j(L_k)=\delta_{jk}\) and \(\sum_jv_j=1\). The direct-product convolution for conic intrinsic volumes and the identity \(\delta(C)=\sum k v_k(C)\) were checked in Amelunxen--Lotz--McCoy--Tropp, arXiv:1303.6672v2, Sections 5.2 and 5.5. The all-dimensional conclusion follows analytically from repeated product additivity on one-dimensional factors; no computation is extrapolated to an infinite statement.

Boundary cases are included: \(d=1\) is proved separately, \(k=0\) and \(k=d\) are covered by the same product argument, and \(\gamma=0\) gives the ambient-dimension family \(\mu_d(C)=\alpha d\).

## Relationship to prior work
Lotz classifies monotone invariant valuations separately in each fixed dimension: the coefficient vector may be any nondecreasing \( (d+1)\)-tuple. The present result imposes Cartesian-product compatibility across dimensions and shows that all those coefficient vectors must lie on one common affine line \(a_{d,k}=\alpha d+\gamma k\). The Lotz paper does not discuss Cartesian products or statistical dimension in the inspected full text.

Amelunxen--Lotz--McCoy--Tropp prove that statistical dimension is a canonical extension of linear dimension: under continuity, rotation invariance, localizability, and the calibration \(\delta(L)=\dim L\) on every linear subspace, it is unique. Their work also records the direct-product law for conic intrinsic volumes and hence for statistical dimension. The present normalized statement is not that characterization restated: it assumes only two values in dimension one and derives the values on every higher-dimensional subspace from Cartesian-product additivity. Oymak--Tropp later describe statistical dimension as the canonical additive, continuous extension of dimension and use its direct-product additivity, but do not classify all cross-dimensional product-additive invariant valuations.

Targeted semantic searches for Cartesian-product additive conic valuations, statistical-dimension characterizations by products, and product-additive monotone invariant valuations found no statement equivalent to the two-parameter classification above. The closest published finding located concerns automatic continuity and fixed-dimensional intrinsic-volume representation, not Cartesian-product compatibility across dimensions.

## Limitations
The theorem concerns real-valued valuations on all closed convex cones and assumes orthogonal invariance in every dimension. It does not classify valuations on pointed cones alone, valuations taking values in non-real semigroups, or families satisfying only an inequality under products. The originality search was targeted rather than exhaustive; older valuation literature could contain a differently phrased cross-dimensional monoidal characterization. The result is a structural corollary of the recent fixed-dimensional classification plus the classical intrinsic-volume product rule, not a new proof of either ingredient.

## References
1. Martin Lotz, *Monotone invariant valuations on convex cones*, arXiv:2609.09335v2, first public version 2026-09-08. Theorem 1.1 and Section 2.
2. Dennis Amelunxen, Martin Lotz, Michael B. McCoy, Joel A. Tropp, *Living on the edge: A geometric theory of phase transitions in convex optimization*, arXiv:1303.6672v2. Sections 5.2, 5.5, and 5.6.
3. Samet Oymak, Joel A. Tropp, *Universality laws for randomized dimension reduction, with applications*, Information and Inference 7 (2018), 337--446, DOI:10.1093/imaiai/iax011. Remark 3.6 and the direct-product discussion.
