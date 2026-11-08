# Exact cross-polytope skeleton convexification and its \(\ell_1\) Hausdorff phase transition

## Finding

Let \(n\ge2\) and \(0\le k<n\) be integers. Put \(s=k+1\), let
\[
 C_n=\{x\in\mathbb R^n:\|x\|_1\le1\},\qquad
 S_k=\{x\in\mathbb R^n:\|x\|_1=1,\ |\operatorname{supp}(x)|\le s\},
\]
so that \(S_k\) is the **closed \(k\)-skeleton** of the standard \(n\)-dimensional cross-polytope. For real \(\lambda\ge0\), define \(E_{n,k}(\lambda)=S_k+\lambda C_n\). Its convex hull equals \((1+\lambda)C_n\). Distances below use the \(\ell_1\) norm in the fixed standard coordinates.

**Theorem (all-parameter, exact metric profile).** For every choice of \(n,k,\lambda\) above,
\[
\boxed{\quad
 d_{H,\ell_1}\bigl(E_{n,k}(\lambda),(1+\lambda)C_n\bigr)
 =\max\left\{0,\ 1-\lambda,\ 2\left(1-\frac{k+1}{n}(1+\lambda)\right)\right\}.\quad}
\]
Consequently, the **sharp finite convexification threshold** in this natural convexifier is
\[
\boxed{\quad S_k+\lambda C_n=(1+\lambda)C_n
\quad\Longleftrightarrow\quad
\lambda\ge\max\left\{1,\frac{n}{k+1}-1\right\}.\quad}
\]
The threshold is also the Schneider nonconvexity index \(\inf\{\lambda\ge0:S_k+\lambda\operatorname{conv}(S_k)\text{ is convex}\}\).

The metric obstruction undergoes a sharp change at \(2(k+1)=n\). In the strict positive-defect regime: if \(2(k+1)<n\), every maximizer of the distance to \(E_{n,k}(\lambda)\) is an outer-boundary point whose \(n\) coordinate moduli all equal \((1+\lambda)/n\); if \(2(k+1)>n\), the origin is the unique maximizer; and if \(2(k+1)=n\), the maximizers are exactly the points with equal coordinate moduli and \(\ell_1\)-norm at most \(1+\lambda\) (including the origin). Thus the formula identifies both the exact magnitude and location of the deepest holes.

## Assumptions and scope

The skeleton is the **union** of all closed faces of dimension at most \(k\), including vertices. Although it is generally nonconvex, it is compact. The convexifier is exactly the standard cross-polytope \(C_n\), with no Euclidean-ball substitution; using the \(\ell_1\) Hausdorff metric is essential to the displayed elementary formula. The claim quantifies over all \(n\ge2\), all \(0\le k\le n-1\), and all finite real \(\lambda\ge0\). The equality at the threshold is included.

## Proof

**Step 1: distance to the sparse unit sphere.** Fix \(y\in\mathbb R^n\), let \(t=\|y\|_1\), and write the coordinate moduli in nonincreasing order \(b_1\ge\cdots\ge b_n\ge0\). Put \(T=\sum_{j=1}^s b_j\). We claim
\[
\boxed{\operatorname{dist}_1(y,S_k)=t-T+|T-1|.}\tag{1}
\]
Indeed, for a prescribed support \(I\) of size at most \(s\), with \(T_I=\sum_{i\in I}|y_i|\), every \(a\in S_k\) supported in \(I\) satisfies
\[
\|y-a\|_1\ge \sum_{i\notin I}|y_i|
 +\left|\sum_{i\in I}|y_i|-\sum_{i\in I}|a_i|\right|
 =t-T_I+|T_I-1|.
\]
Equality is attainable: match coordinate signs and choose nonnegative magnitudes summing to one, either decreasing the available total \(T_I\) to one or adding the missing mass \(1-T_I\) to one coordinate. This also works when \(T_I=0\). The function \(u\mapsto t-u+|u-1|\) is nonincreasing for \(u\ge0\). Therefore a support attaining the largest possible \(T_I\), the indices of the \(s\) largest coordinate moduli, minimizes the distance. This proves (1).

**Step 2: reduction to two endpoints.** Since \(E_{n,k}(\lambda)\) is the union of closed \(\ell_1\) balls of radius \(\lambda\) about points of \(S_k\),
\[
\operatorname{dist}_1(y,E_{n,k}(\lambda))
 =\max\{0,\operatorname{dist}_1(y,S_k)-\lambda\}.\tag{2}
\]
Also \(E_{n,k}(\lambda)\subseteq(1+\lambda)C_n\), so the Hausdorff distance equals the supremum of (2) over \(\|y\|_1\le1+\lambda\).

Let \(r=s/n\). Averaging the largest \(s\) coordinate moduli gives \(T\ge rt\), with equality for equal moduli. Since the expression in (1) decreases in \(T\), its maximum at any fixed \(t\in[0,1+\lambda]\) is realized by points with coordinate moduli \(t/n\), and equals
\[
 f_r(t)=t-rt+|rt-1|
 =\max\{t-1,\ 1+(1-2r)t\}.\tag{3}
\]
This is convex and piecewise affine, so its maximum on the interval occurs at an endpoint. Evaluating (3) at \(t=0\) gives \(1\); evaluating at \(t=1+\lambda\) gives
\[
\max\{\lambda,\ 1+(1-2r)(1+\lambda)\}.
\]
Subtracting \(\lambda\) and taking the positive part in (2) yields the exact displayed Hausdorff formula.

**Step 3: threshold and equality.** Formula (2) is identically zero on the convex hull precisely when both \(1-\lambda\le0\) and \(2(1-r(1+\lambda))\le0\). These conditions mean respectively \(\lambda\ge1\) and \(\lambda\ge1/r-1=n/s-1\). Both sets are compact, so vanishing Hausdorff distance is equivalent to equality of the sets. This proves the sharp threshold with equality included. Because \(\operatorname{conv}(S_k)=C_n\), this is exactly Schneider's index of this skeleton.

**Step 4: complete extremizer classification.** When the defect is strictly positive and \(2r<1\), both affine branches in (3) increase strictly, so \(t=1+\lambda\) is necessary; here \(rt<1\) throughout the defective regime. Equality in the largest-coordinate average \(T\ge rt\) then forces all \(b_i\) equal. When \(2r>1\) and the defect is positive, \(\lambda<1\); the decreasing branch of (3) dominates at its maximum, so only \(t=0\) attains it. When \(2r=1\), the defective range is \(\lambda<1\), and the constant branch \(f_r(t)=1\) prevails for all \(t\in[0,1+\lambda]\). Equality for \(t>0\) again requires equal coordinate moduli. These cases give exactly the stated maximizers. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and exact rational arithmetic. It independently minimizes distances to finite signed rational grids of sparse \(\ell_1\) unit vectors and compares them with (1), then checks the endpoint expression, witness extremizers, and sharp threshold for rational parameters. To reproduce, run `python3 verify.py` from the extracted directory. It reports `VERIFY_OK 980 exhaustive-grid point-distance tests; 140 profile/threshold tests`. The finite grid checks are corroboration only: the proof above establishes the theorem over all real parameters and dimensions.

## Relationship to prior work

Mark Meyer's *Finite convexification by Minkowski summation* (arXiv:2610.26744v1, first public 2026-10-19) gives general exposed-face and covering-radius criteria for determining whether \(A+\lambda K\) is convex, and studies several convexifiers. The present theorem evaluates the **entire quantitative Hausdorff profile** and its exact threshold for every skeleton of the standard cross-polytope with the matching \(\ell_1\) convexifier. The general criteria themselves do not state the displayed family-specific profile.

Fradelizi, Madiman, Marsiglietti, and Zvavitch (2018) investigate Schneider's index and Hausdorff nonconvexity of Minkowski averages in arbitrary normed spaces. Their qualitative and general quantitative results do not state this cross-polytope skeleton profile. The known exact finite thresholds for the skeleta of a **simplex** under repeated equal-weight self-averaging concern a different polytope and a different Minkowski operation; they do not imply the stated all-real-\(\lambda\) result. Similarly, van Hintum (2026) studies sharp contraction under repeated Minkowski averaging rather than a fixed convexifier.

## Limitations

The result uses the intrinsic \(\ell_1\) metric, coordinate-dependent support structure, and a cross-polytope convexifier. No formula is asserted for Euclidean Hausdorff distance, arbitrary polytopes, arbitrary convexifying bodies, or cross-polytope skeleta under repeated equal-weight self-averaging. The result provides a natural exact family, not a universal threshold over all compact sets. The literature comparison remains best-knowledge rather than independent historical-priority certification.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, first publicly submitted 2026-10-19. https://arxiv.org/abs/2610.26744 .
2. Mark Meyer, *Measuring the convexity of compact sumsets with the Schneider non-convexity index*, 2025. https://link.springer.com/article/10.1186/s13660-025-03356-w .
3. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, EMS Surveys in Mathematical Sciences **5** (2018), 1–64, DOI:10.4171/EMSS/26; open preprint https://arxiv.org/abs/1704.05486 .
4. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1, 2026. https://arxiv.org/abs/2606.10815 .
5. Rolf Schneider, *A measure of convexity for compact sets*, Pacific Journal of Mathematics **58** (1975), 617–625.
