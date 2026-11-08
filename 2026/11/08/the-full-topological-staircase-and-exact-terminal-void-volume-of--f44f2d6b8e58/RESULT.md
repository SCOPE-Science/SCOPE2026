# The full topological staircase and exact terminal void volume of simplex-skeleton convexification

## Finding

Let \(d\ge2\), let \(0\le r<d\), let \(\Delta\) be any nondegenerate \(d\)-simplex, and write \(A=\operatorname{skel}_{r}(\Delta)\) for the union of its closed faces of dimension at most \(r\). For each real \(\lambda\ge0\), put \(X_\lambda=A+\lambda\Delta\) and \(Y_\lambda=(1+\lambda)^{-1}X_\lambda\), using the same affine coordinates as the simplex. Write \(n=d+1\) and \(s=r+1\).

**Theorem (complete topological filtration and terminal volume).** If \(p=(p_1,\ldots,p_n)\) is the barycentric vector of a point of \(\Delta\), then
\[
Y_\lambda=\left\{p\in\Delta:\sum_{i=1}^{s}p_{(i)}\ge\frac1{1+\lambda}\right\},\qquad p_{(1)}\ge\cdots\ge p_{(n)}.
\]
For \(s\le k\le d\), throughout the half-open parameter interval
\[
\frac{k-s}{s}\le\lambda<\frac{k+1-s}{s},
\]
there is a **strong deformation retraction** \(Y_\lambda\searrow\operatorname{skel}_{k-1}(\Delta)\). In particular,
\[
Y_\lambda\simeq\bigvee^{\binom d k} S^{k-1}.
\]
At and above \(\lambda_*=(n-s)/s=(d-r)/(r+1)\), one has \(Y_\lambda=\Delta\). This is the exact convexification threshold: at every smaller parameter \(Y_\lambda\) is a proper nonconvex subset of \(\Delta\). In the displayed range, all homotopy groups are understood through the stated wedge equivalence; for \(k=1\), \(\bigvee^{d}S^0\) denotes \(d+1\) points.

Moreover, all reduced **integral persistent-homology bars** are given explicitly: for each \(k=s,\ldots,d\), precisely \(\binom d k\) bars of degree \(k-1\) occur, each on
\[
\left[\frac{k-s}{s},\frac{k+1-s}{s}\right).
\]
There are no other reduced bars or torsion. This describes every inclusion-induced map, not just isolated homotopy types.

In the **entire last preconvexification phase**
\[
\frac{d-s}{s}\le\lambda\le\frac{n-s}{s},
\]
the relative missing volume has the exact expression
\[
\frac{\operatorname{Vol}_d((1+\lambda)\Delta\setminus X_\lambda)}{\operatorname{Vol}_d((1+\lambda)\Delta)}
=C_{d,r}\left(\frac1{1+\lambda}-\frac{s}{n}\right)^d,
\quad C_{d,r}=\frac{d!\,n^d}{s!\,(n-s-1)!\,(n-s)^s\,s^{n-s-1}}.
\]
Thus the missing volume vanishes to exactly the \(d\)-th order at the sharp convexification threshold, for **every skeleton dimension**. This ratio, the filtration, and the threshold depend only on \(d,r\), not on the shape of \(\Delta\).

## Assumptions and scope

All simplices and faces are closed. \(\operatorname{skel}_r(\Delta)\) includes all faces spanned by at most \(s=r+1\) vertices, and includes the \(0\)-skeleton. Minkowski addition is by a single continuously dilated **convex full simplex**, not by repeated sums of the nonconvex skeleton. Intrinsic \(d\)-volume is taken within the affine hull of \(\Delta\), and the normalized copy of the sum means that a point \(a+\lambda z\) is divided by \(1+\lambda\). For a simplex not through the origin, translations and nonsingular affine changes of coordinates carry this normalized interpolation and the volume ratio to the standard barycentric model. The filtration is increasing in \(\lambda\). Reduced persistent homology uses integer coefficients, with standard half-open interval conventions and degree zero interpreted as reduced \(H_0\).

## Proof

**Step 1: exact barycentric membership.** Work in the standard \((n-1)\)-simplex \(\{p_i\ge0,\ \sum_i p_i=1\}\subset\mathbb R^n\). A point \(p\) is in \(Y_\lambda\) if and only if there are probability vectors \(a,z\) with \(|\operatorname{supp}(a)|\le s\) and \((1+\lambda)p=a+\lambda z\). This is equivalent to existence of an \(s\)-subset \(I\) with \(\sum_{i\in I}(1+\lambda)p_i\ge1\): necessity follows by summing the coordinates supporting \(a\); sufficiency follows by assigning the unit mass of \(a\) to that support within the capacities \((1+\lambda)p_i\), then normalizing the residual vector to obtain \(z\), with \(\lambda=0\) handled directly. Maximizing over \(I\) gives the displayed sum of the largest \(s\) coordinates. Denote that function by \(f_s(p)\).

**Step 2: a nested strong deformation retraction.** Triangulate \(\Delta\) by its barycentric subdivision. For each nonempty vertex subset \(I\subset[n]\), the corresponding barycentric-subdivision vertex \(b_I\) is the indicator of \(I\) divided by \(|I|\). Its value is \(f_s(b_I)=\min\{1,s/|I|\}\). The vertices of each subdivided simplex are indexed by a chain of nested subsets, and on such a simplex the order of barycentric coordinates is fixed. Hence \(f_s\) is affine there. For \(\alpha=1/(1+\lambda)\), the vertex condition \(f_s(b_I)\ge\alpha\) is exactly \(|I|\le k=\min\{n,\lfloor s(1+\lambda)\rfloor\}\). For a point \(p\) of the superlevel region in one subdivided simplex, write it as a convex combination of its barycentric vertices; at least one vertex has value at least \(\alpha\). Delete the coefficients of lower-valued vertices and renormalize the remaining coefficients. The straight-line homotopy to this point stays in the same subdivided simplex and remains in \(f_s\ge\alpha\) by affinity. These formulae agree on common faces and fix the induced good-vertex subcomplex pointwise; hence they give a global strong deformation retraction. That subcomplex is the barycentric subdivision of \(\operatorname{skel}_{k-1}(\Delta)\), and for \(k=n\) is all of \(\Delta\).

**Step 3: homotopy and maps, including endpoints.** The \((k-1)\)-skeleton of a \(d\)-simplex, with \(1\le k\le d\), is homotopy equivalent to a wedge of \(\binom d k\) spheres of dimension \(k-1\). This follows by inductively attaching a last vertex's star to the skeleton on the remaining vertices; the augmented simplicial chain complex of the full simplex is exact, proving concentrated, free reduced homology of rank \(\binom d k\). For \(k\ge2\), the skeleton is \((k-2)\)-connected, and the standard cellular induction yields the corresponding wedge homotopy type; \(k=1\) gives discrete points. The retractions at successive scales restrict compatibly to the included lower skeletons, because the high-threshold retraction fixes its entire retained complex. Thus the persistence system identifies with the simplex-skeleton inclusion system. Since each skeleton has reduced homology in a single degree and the next skeleton has none in the old degree, precisely the asserted bars appear and die. At each critical scale the *new* skeleton is present, as the superlevel inequality is weak.

**Step 4: the exact final-phase hole.** Put \(u=\tfrac1n\mathbf1\), \(\alpha=1/(1+\lambda)\), and \(\varepsilon=\alpha-s/n\). The minimum of \(f_s\) over \(\Delta\) is \(s/n\), uniquely at \(u\), so convexification occurs precisely when \(\varepsilon\le0\). For \(\varepsilon>0\), the missing region has the form \(u+\varepsilon W\), clipped to \(\Delta\), where
\[
W=\{v\in\mathbb R^n:\sum_i v_i=0,\ \max_{|I|=s}\sum_{i\in I}v_i<1\}.
\]
The boundary (where equality holds) has zero \(d\)-volume, so we may replace \(<\) by \(\le\) for all volume computations. Sort coordinates within a braid chamber. Let \(b_j=\mathbf1_{\{1,\ldots,j\}}-(j/n)\mathbf1\) for \(1\le j\le d\). Each ordered zero-sum vector is uniquely \(\sum_jt_jb_j\), \(t_j\ge0\), and on that chamber
\[
\max_{|I|=s}\sum_{i\in I}v_i=\sum_{j=1}^{d}q_jt_j,
\qquad q_j=\min(s,j)-sj/n>0.
\]
Thus the ordered portion of \(\overline W\) is the simplex with vertices \(0\) and \(b_j/q_j\). The Gram determinant of \(b_1,\ldots,b_d\) is \(1/n\), so its intrinsic volume is \(1/(\sqrt n\,d!\prod_jq_j)\). The \(n!\) coordinate-order chambers have disjoint interiors. Since \(\operatorname{Vol}_d(\Delta)=\sqrt n/d!\),
\[
\frac{\operatorname{Vol}_d(W)}{\operatorname{Vol}_d(\Delta)}
=\frac{d!}{\prod_{j=1}^{d}q_j}
=\frac{d!\,n^d}{s!\,(n-s-1)!\,(n-s)^s\,s^{n-s-1}}=C_{d,r}.
\]
Every coordinate of \(\overline W\) is at least \(-(n-1)/s\), with equality at a ray vertex; this follows by averaging the \(s\) largest entries subject to zero sum, or by inspecting the explicit ray vertices. Hence \(u+\varepsilon\overline W\subset\Delta\) whenever \(0\le\varepsilon\le s/[n(n-1)]\). This condition is equivalent to \(\lambda\ge(d-s)/s\). Throughout that final parameter interval there is no clipping, so the normalized volume deficit is exactly \(C_{d,r}\varepsilon^d\). The coefficient is strictly positive, proving the exact order \(d\). \(\square\)

## Verification

Run `python verify.py` using the standard Python library. It checks the braid-chamber Gram determinant, the volume coefficient, the extremal negative coordinate, the barycentric membership witness, the linearity on barycentric simplices, and mod-two homology of all proper simplex skeleta through dimension seven. On the packaged source it reports `PASS: 12615 exact assertions; n=3..10, all skeleton ranks and barycentric tests`. An independent optional check, `python verify_volume_hulls.py`, uses NumPy/SciPy to enumerate all permuted ray vertices and recompute convex-hull volumes for \(3\le n\le5\); it reports nine successful \((n,s)\) comparisons. These computations corroborate, but do not replace, the general proof. For example, with \(d=3\), \(r=1\), the filtration goes from a wedge of three circles to a two-sphere at \(\lambda=1/2\), then fills at \(\lambda=1\). On \([1/2,1]\), the exact relative void fraction is \(24(1/(1+\lambda)-1/2)^3\).

## Relationship to prior work

Meyer's 2026 general finite-convexification theorem provides necessary and sufficient covering conditions for pairs of compact sets and convex convexifiers; its inspected full text contains no exact simplex-skeleton topological filtration, simplex-skeleton volume polynomial, or all-degree persistence calculation. A separate published theorem titled *Sharp finite convexification thresholds for every skeleton of a simplex* treats **repeated equal-weight Minkowski averages of the skeleton itself**, obtaining a threshold \(\lceil d/r\rceil\) for \(1\le r<d\). The present deformation is \(\operatorname{skel}_r(\Delta)+\lambda\Delta\), with a continuously varying *convex simplex* as the second summand, and is not implied by the equal-weight result: its sharp threshold is \((d-r)/(r+1)\), and its topological and volume invariants are absent from that theorem. General work on Minkowski averages by Fradelizi, Madiman, Marsiglietti, and Zvavitch studies convergence and measures of nonconvexity, without this explicit superlevel filtration. An earlier complete treatment of **cubical** skeleta with anisotropic box offsets has fundamentally different coordinate barriers and preserves the original homology degree instead of generating the consecutive-dimensional staircase found here. The barycentric-order and polar-hypersimplex structure is specific to simplices. Deza, Hiriart-Urruty and Pournin analyzed volumes of related full-dimensional centrally symmetric polyhedral norm balls obtained by interpolating cubes and cross-polytopes; their polytopes and deformation operator differ from the present sum-zero polar hypersimplex and simplex-skeleton offset. Their norm-ball volume results do not determine the integral filtration described here.

## Limitations

The theorem concerns a simplex with the same simplex as convexifier, in arbitrary nondegenerate affine realization; it does not address arbitrary convexifiers, arbitrary polytopal complexes, or Euclidean-ball offsets. The explicit volume formula holds throughout the *last* preconvexification phase, not necessarily at all earlier parameters. The topology is exact for all parameters. Finite scripts verify examples only. The claim of historical originality is provisional; a related equivalent formulation in the literature on cardinality-constrained simplex filtrations or hypersimplex polars cannot be categorically excluded.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (publicly submitted 2026-10-19), https://arxiv.org/abs/2610.26744 . Full HTML text read.
2. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486, https://arxiv.org/abs/1704.05486 . Background on convexification and nonconvexity measures.
3. *Sharp finite convexification thresholds for every skeleton of a simplex*, publicly accessible 2026 mathematical record. Full statement and proof read; concerns equal-weight repeated skeleton sums, not the present convexifier.
4. Antoine Deza, Jean-Baptiste Hiriart-Urruty, Lionel Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607v2 (2021), https://arxiv.org/abs/2011.05607 . Definitions and volume sections inspected; distinct norm-ball family.
