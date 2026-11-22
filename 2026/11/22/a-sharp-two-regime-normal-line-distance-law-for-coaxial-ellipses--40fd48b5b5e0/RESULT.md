# A sharp two-regime normal-line distance law for coaxial ellipses

## Finding

The normal-line pseudometric of Akopyan and Glazyrin has a complete algebraic two-regime formula on the natural four-parameter family of concentric, co-axial Euclidean ellipses. In one regime the distance sees only the difference of their major-minus-minor semiaxis gaps. In the other, an interior reversal of the support-function difference introduces a strictly positive additional term, with an explicit square-root critical value. In particular, two different nested ellipses with exactly the same major-minus-minor gap can have positive normal-line distance.

Precisely, for real \(a\ge b>0\) and \(c\ge d>0\), define the centered solid ellipses
\[
E_{a,b}=\{(x,y)\in\mathbb R^2:x^2/a^2+y^2/b^2\le1\},\qquad E_{c,d}=\{(x,y)\in\mathbb R^2:x^2/c^2+y^2/d^2\le1\}.
\]
Put \(A=a^2-b^2\), \(C=c^2-d^2\), \(p=b-d\), \(q=a-c\), and \(\sigma_0=Ad-Cb\), \(\sigma_1=Ac-Ca\). Let \(\mathfrak d\) be Definition 2.1 of [1], namely half the angular integral of Euclidean distances between corresponding normal lines. Then
\[
\boxed{\mathfrak d(E_{a,b},E_{c,d})=2|q-p|\quad\text{if }\sigma_0\sigma_1\ge0.}
\]
If \(\sigma_0\sigma_1<0\), necessarily \(A,C>0\), \(A\ne C\), and
\[
\boxed{\begin{aligned}
u_*&=\frac{C^2b^2-A^2d^2}{AC(A-C)}\in(0,1),\\
z_*&=\operatorname{sgn}(A-C)\sqrt{\frac{(A-C)(Cb^2-Ad^2)}{AC}},\\
\mathfrak d(E_{a,b},E_{c,d})&=2\bigl(|z_*-p|+|q-z_*|\bigr)>2|q-p|.
\end{aligned}}
\]
Equality \(\sigma_0\sigma_1=0\) belongs to the first regime: no strict extra term occurs. The formulas cover circles without exceptions: two concentric disks have distance zero, and the distance between a centered ellipse and any concentric disk is \(2(a-b)\).

For example, \(E_{3,2}\supset E_{2,1}\) have equal semiaxis gaps \(3-2=2-1\) but
\[
\mathfrak d(E_{3,2},E_{2,1})=4\left(1-\sqrt{\frac{14}{15}}\right)>0.
\]

The general normalization identity underlying this result, also valid for arbitrary planar compact convex bodies, is
\[
\mathfrak d(K,L)=\frac12\operatorname{TV}_{[0,2\pi]}(h_K-h_L),
\]
where \(h_K,h_L\) are their support functions on the unit circle. Hence \(\mathfrak d(K,L)=0\) exactly when one body is an outer Euclidean parallel body of the other (allowing parallel offset zero). This kernel fact explains why the ellipse formula detects changes in shape but ignores uniform disk offsets.

## Assumptions and scope

All distances, areas, normals and support functions use the standard Euclidean plane. The normal-line pseudometric is not a Hausdorff or shortest-point distance. Supporting normal lines are associated with the *same* oriented unit-normal angle; at a.e. angle they are unique. The two ellipses must share both center and principal-axis directions. The major semiaxes are placed on the common horizontal axis and obey \(a\ge b\), \(c\ge d\); circles are allowed. No claim is made for ellipses with different centers or rotated axes.

The quantity \(\operatorname{TV}\) is ordinary total variation around a full angular period; since support functions of compact convex bodies are Lipschitz, this equals the integral of the absolute a.e. angular derivative. For arbitrary convex bodies the kernel statement is considered for their full compact convex sets, not for parametrized curves with an unrelated direction pairing.

## Proof

**Step 1: Normal lines and support variation.** Write \(n_\theta=(\cos\theta,\sin\theta)\) and \(t_\theta=(-\sin\theta,\cos\theta)\). At a differentiability angle of the support function \(h_K(\theta)=\sup_{x\in K}x\cdot n_\theta\), the unique support point is
\[
x_K(\theta)=h_K(\theta)n_\theta+h_K'(\theta)t_\theta.
\]
The line through this point in direction \(n_\theta\) therefore has signed tangential offset \(h_K'(\theta)\). Distances between the corresponding parallel normal lines of \(K\) and \(L\) equal \(|h_K'(\theta)-h_L'(\theta)|\). In Definition 2.1 of [1], reversing all normal orientations merely shifts the integral by \(\pi\), so using outward normals gives the same result. Integrating yields
\[
\mathfrak d(K,L)=\frac12\int_0^{2\pi}|h_K'(\theta)-h_L'(\theta)|\,d\theta
=\frac12\operatorname{TV}(h_K-h_L).
\]
If this integral is zero, the absolutely continuous difference of support functions is constant, say \(r\). If \(r\ge0\), \(h_K=h_L+r h_B\), and uniqueness of support functions gives \(K=L+rB\), where \(B\) is the unit disk. If \(r<0\), likewise \(L=K+(-r)B\). The converse follows by additivity of support functions. This proves the general kernel assertion.

**Step 2: Reduce the ellipse distance to one-dimensional variation.** For the specified ellipse,
\[
h_{a,b}(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}.
\]
Writing \(u=\cos^2\theta\), set
\[
H(u)=\sqrt{b^2+Au}-\sqrt{d^2+Cu},\qquad 0\le u\le1.
\]
Four congruent quadrants contribute to the full angular total variation. Thus
\[
\mathfrak d(E_{a,b},E_{c,d})=2\operatorname{TV}_{[0,1]}H.
\]
Its endpoint values are \(H(0)=p\) and \(H(1)=q\).

**Step 3: Exactly classify stationary values.** For \(u\in[0,1]\),
\[
2H'(u)=\frac A{\sqrt{b^2+Au}}-\frac C{\sqrt{d^2+Cu}}.
\]
Both denominators are strictly positive, and the sign of this derivative equals the sign of the *affine* function
\[
S(u)=A^2(d^2+Cu)-C^2(b^2+Au)
=A^2d^2-C^2b^2+AC(A-C)u.
\]
Indeed squaring preserves order for the two nonnegative terms. Its endpoint signs are those of \(\sigma_0\) and \(\sigma_1\) because
\[
S(0)=(Ad-Cb)(Ad+Cb),\qquad S(1)=(Ac-Ca)(Ac+Ca).
\]
If the product of the endpoint signs is nonnegative, \(H'\) cannot change sign in the open interval (zeros at endpoints cause no reversal); hence \(H\) is monotone or constant and \(\operatorname{TV}H=|q-p|\). This includes \(A=C=0\) and all degeneracies.

If \(\sigma_0\sigma_1<0\), the affine function \(S\) has exactly one zero \(u_*\) strictly inside \((0,1)\); in particular \(A,C>0\) and \(A\ne C\). Solving gives the stated \(u_*\). At that point \(A/\sqrt{b^2+Au_*}=C/\sqrt{d^2+Cu_*}\), so \(H(u_*)\) has sign \(\operatorname{sgn}(A-C)\), and elimination of \(u_*\) gives
\[
H(u_*)^2=\frac{(A-C)(Cb^2-Ad^2)}{AC}.
\]
Thus \(H(u_*)=z_*\). Since the derivative changes sign across this point, \(z_*\) is strictly outside the interval with endpoints \(p,q\). Therefore
\[
\operatorname{TV}H=|z_*-p|+|q-z_*|>|q-p|.
\]
This proves both branches and their strictness.

**Step 4: Explicit boundary and rigidity.** For \((a,b,c,d)=(3,2,2,1)\), \((A,C)=(5,3)\), \((\sigma_0,\sigma_1)=(-1,1)\), \(u_*=11/30\) and \(z_*=\sqrt{14/15}\), while \(p=q=1\). Substitution proves the displayed positive exact value. If both ellipses are disks, \(H\) is constant. If an ellipse is compared with a disk, \(H\) is monotone, so the formula is \(2(a-b)\). More generally, the kernel characterization from Step 1 applies; two centered co-axial noncircular ellipses at zero distance must in fact coincide, since adding a nonzero disk to an ellipse cannot preserve an elliptic support function (alternatively, the derivative identity in Step 3 forces identical squared semiaxes).

## Verification

Run the accompanying standalone Python 3 file `checker.py`. It uses only standard-library arithmetic. It first proves the exact rational identities \(u_*=11/30\), \(z_*^2=14/15\), and checks the claimed exact distance. It then compares the algebraic branch formulas with a direct midpoint-rule integration of the original normal-line-distance integral on 252 fixed and seeded parameter configurations, including 40 interior-switch instances, circle cases, homothetic pairs and endpoint cases. The checker requires numerical differences below \(8\times10^{-6}\) for the randomized integration comparisons. This is *corroboration only*: the universally quantified result follows from Steps 1–4, not from the finite sample.

## Relationship to prior work

Akopyan and Glazyrin [1] introduce \(\mathfrak d\) (their `pdist`), prove its pseudometric and Minkowski convexity properties, and note concentric circles as an example of distinct curves at zero distance. Their Lemma 2.6 already supplies the underlying normal-offset integration identity; neither this identity nor the definition of the pseudometric is claimed as new here. The new assertion is the complete, explicit two-regime *pairwise ellipse* formula, its sharp interior-switch criterion, and the positive equal-semiaxis-gap example. Examination of [1] found no ellipse analysis or four-parameter formula. Classical support-function theory explains the preliminary variation identity; [2] treats normal chords of individual ellipses rather than this pairwise normal-line integral. Prior work on Minkowski-sum areas of rotated ellipses concerns a different functional and does not determine \(\mathfrak d\).

## Limitations

The theorem does not cover translated or independently rotated ellipses. The normal-line pseudometric is intentionally degenerate on Euclidean outer parallel bodies; it must not be described as a genuine metric on all convex bodies. The calculations do not resolve the original disjoint-body perimeter bound anew. The support-variation and parallel-body kernel observations are preliminary consequences of classical support theory rather than independent major contributions. No exhaustive historical novelty claim is made: an equivalent ellipse evaluation under an alternate name for the integral could exist outside the inspected literature. Independent mathematical audit has not been performed.

## References

1. A. Akopyan and A. Glazyrin, *On the total perimeter of disjoint convex bodies*, arXiv:2308.16340v1, first submitted 30 August 2023; Definition 2.1, Proposition 2.3 and Lemma 2.6. https://arxiv.org/abs/2308.16340
2. W. Cieślak, H. Martini and W. Mozgawa, *On Holditch's theorem*, *Journal of Geometry* 111, article 24 (2020), DOI:10.1007/s00022-020-00536-5, section on normal chords of ellipses. https://doi.org/10.1007/s00022-020-00536-5
