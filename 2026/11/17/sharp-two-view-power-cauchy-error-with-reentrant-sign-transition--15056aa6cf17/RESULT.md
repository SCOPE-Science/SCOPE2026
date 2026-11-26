# Sharp positive two-view minimax for superquadratic planar brightness

## Finding

For every real \(p>2\), write
\[
c_p=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma(1+p/2)}.
\]
Among all fixed normalized positive rules \(\mu\) on at most two unoriented planar directions, the minimum angular discrepancy is
\[
\inf_\mu\mathfrak D_p(\mu)=\max\{\tfrac12-c_p,\ c_p-2^{-p/2}\}.
\]
The unique minimizing rule, up to a common rotation, sign choices of direction representatives and relabeling, places weight \(1/2\) on each of two perpendicular directions. It simultaneously attains the universal bounds on the upper and lower potential extremes. The sharp perimeter-normalized convex-body error is half the angular discrepancy. The contribution is the superquadratic minimax value and equality classification. The convex-body norm reduction, exact quadratic endpoint, and the polarity comparison described below are not asserted as new.

## Assumptions and scope

Take \(K\subset\mathbb R^2\) compact, convex and full-dimensional, with surface-area measure \(S_K\) and perimeter \(P(K)=S_K(S^1)\). Put
\[
B_pK(u)=\tfrac12\int_{S^1}|u\cdot v|^p\,dS_K(v).
\]
The uniform circular mean is \(c_pP(K)/2\), where \(c_p=\pi^{-1}\int_0^\pi|\cos\theta|^p\,d\theta\) by the beta integral. Write a rule as \(\mu=\sum_{j=1}^m w_j\delta_{u_j}\) with \(1\le m\le2\), weights \(w_j>0\), \(\sum_jw_j=1\), and angles \(\phi_j\in\mathbb R/\pi\mathbb Z\) representing the \(u_j\). The potential and angular discrepancy are
\[
F_\mu(\theta)=\sum_jw_j|\cos(\theta-\phi_j)|^p,
\qquad \mathfrak D_p(\mu)=\|F_\mu-c_p\|_\infty.
\]
The geometric error is the supremum over \(K\) of \(\bigl|\sum_jw_j B_pK(u_j)-c_pP(K)/2\bigr|/P(K)\).

## Proof

**Norm reduction.** Interchanging integrations gives the geometric error bound \(\mathfrak D_p(\mu)/2\). Choose rectangles with long-side normals \(\pm v_0\), where \(v_0\) maximizes the absolute angular discrepancy. As the aspect ratio tends to infinity, their normalized surface-area measures tend to the even two-point measure on \(\pm v_0\). The potential is even, so this realizes the bound as a supremum. This is the planar instance of An's defect norm identity [1, Theorem 3.2].

**Universal bounds and sharpness.** At a heaviest node the potential is at least its weight, hence \(\max F_\mu\ge1/2\). If there are two distinct projective nodes, their larger separating gap on the circle of circumference \(\pi\) has length \(L\ge\pi/2\). At its midpoint the distance to both nodes is \(L/2\), so \(\min F_\mu\le\cos^p(L/2)\le2^{-p/2}\). A one-node rule has minimum zero and maximum one, and satisfies both bounds strictly. For the equal perpendicular rule,
\[
F_0(\theta)=\tfrac12\bigl(|\cos\theta|^p+|\sin\theta|^p\bigr)
=\tfrac12[x^q+(1-x)^q],\qquad x=\cos^2\theta,\quad q=p/2>1.
\]
Strict convexity gives its maximum \(1/2\) and minimum \(2^{-q}\). Its mean is \(c_p\), which lies strictly between the two endpoints. Thus the universal bounds imply the stated minimax error, and the perpendicular equal rule attains it.

**Uniqueness.** Nonperpendicular distinct nodes have \(L>\pi/2\), hence \(\min F_\mu<2^{-q}\). They also have \(\max F_\mu>1/2\): either the larger weight exceeds \(1/2\), or the weights are equal and there is a strictly positive contribution from the other node at a sampled node. For perpendicular nodes with unequal weights, the larger weight again exceeds \(1/2\). At the bisector the value is \(2^{-q}\) but the angular derivative is \(p2^{-q}(1-2w)\ne0\), where \(w\) weights the direction with angle zero. This gives \(\min F_\mu<2^{-q}\). In each nonoptimal case both extrema are strictly worse, which excludes equality regardless of which side of the error dominates.

## Polarity as a consequence of prior moment monotonicity

For the optimal rule the high and low deviations are \(1/2-c_p\) at the axes and \(c_p-2^{-q}\) at the bisectors. Their comparison follows directly from the balanced order-four character moment in [2]. With that source's phase variable,
\[
H_q(\phi)=\tfrac14\sum_{k=0}^3(1+\cos(\phi+k\pi/2))^q.
\]
Its axis value satisfies \(2^{-q}H_q(0)=1/4+2^{-q-1}\). Its circular mean is \(2^q c_p\), since \((1+\cos\phi)/2=\cos^2(\phi/2)\). In [2, Proof, balanced-coefficient argument], \(H_q\) is strictly decreasing on \((0,\pi/4)\) for \(1<q<2\) and \(q>3\), strictly increasing there for \(2<q<3\), and constant at \(q=2,3\). Phase periodicity and reflection then make \(H_q(0)\) a strict extremal value relative to its mean in the nonconstant cases. Thus the positive error is larger on \((2,4)\) and \((6,\infty)\), the negative error is larger on \((4,6)\), and the magnitudes tie at 4 and 6. This application of [2] compares the two deviations for the optimal rule; [2] does not optimize the planar two-direction problem over weights and nodes.

## Relation to prior work and limitations

An [1, Theorems 3.2, 4.3, 5.2] supplies the norm reduction and exactness framework, including the known unique exact equal orthogonal pair at \(p=2\). The subquadratic two-direction theorem [3] determines a different error for \(0<p<2\) with the same optimizer. Its obstruction uses test normals perpendicular to the samples to get \(\min F\le1/2\), useful when \(c_p>1/2\). For \(p>2\), the mean lies below \(1/2\), and the two obstructions and their strict cases above are needed. The sign corollary is credited to [2] through the moment identity. These comparisons do not establish exhaustive historical priority.

The theorem is for real \(p>2\), calibrated positive weights, fixed rules with at most two planar projective directions, and perimeter-normalized error over full-dimensional bodies. No determination for more nodes, signed weights, adaptive rules or other dimensions is asserted. The rectangle argument proves a supremum, not attainment by a full-dimensional convex body.

## Verification

The proof of the minimax value and uniqueness is analytic. The accompanying `verify.py` uses Python 3 and its standard library for finite numerical checks of the normalization, orthogonal extrema, the two geometric test directions and selected instances of the credited polarity comparison. It is a diagnostic, not the proof for all real exponents or all rules.

## References

1. C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, [arXiv:2609.05869v1](https://arxiv.org/abs/2609.05869), Theorems 3.2, 4.3 and 5.2.
2. [*Sharp Λ(p) constants for order-four character pairs*](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-lambda-p-constants-for-order-four-character-pairs--edfa311d2932/RESULT.md), Proof, balanced-coefficient phase analysis.
3. [*Sharp positive two-direction quadrature for subquadratic cosine brightness*](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-sharp-positive-two-direction-quadrature-for-subquadratic-cosine--35c0341352f2/RESULT.md), Finding and Proof §§2–3.
