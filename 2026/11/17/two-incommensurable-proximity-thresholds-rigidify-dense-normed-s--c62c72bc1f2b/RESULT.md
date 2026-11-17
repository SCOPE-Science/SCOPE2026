# Two incommensurable proximity thresholds rigidify dense normed-space maps

## Finding

**Two-threshold rigidity theorem.** Let \(X,Y\) be nonzero real normed vector spaces, and let \(A\subset X\) and \(B\subset Y\) be norm-dense subsets. Fix \(a,b>0\). Suppose a bijection \(f:A\to B\) preserves both strict proximity relations in both directions: for all \(x,y\in A\) and \(r\in\{a,b\}\),
\[
\|x-y\|_X<r\quad\Longleftrightarrow\quad\|f(x)-f(y)\|_Y<r.
\]
If \(a/b\notin\mathbb Q\), then \(f\) preserves **every** pairwise distance. It therefore extends uniquely to a surjective real-affine isometry between the completions \(\widehat X\) and \(\widehat Y\). If \(X,Y\) are Banach spaces, this extension is defined on \(X\) and takes values in \(Y\).

The irrationality hypothesis is universally sharp: if \(a/b\in\mathbb Q\), there is a non-affine increasing homeomorphism of the real line preserving both strict proximity relations (indeed, all thresholds in the positive integer span of a common unit).

## Assumptions and scope

The hypothesis concerns a **bijection between norm-dense subsets**, not an a priori continuous or approximately isometric map. Threshold comparisons are strict, not comparisons of equal distances. The same numerical radii are used in source and target. The spaces may have different dimensions, may be incomplete, and need not be strictly convex, smooth, separable, reflexive, or finite-dimensional. The zero-dimensional case is excluded solely to allow the ray argument below; the only possible bijection between dense subsets of two zero spaces is trivial.

For a dense subset \(A\) of a normed space, put
\[
R_r^A(x,y)\iff\|x-y\|<r,\qquad C_r^A(x,y)\iff\|x-y\|\le r,
\]
with \(r>0\). Write \(R_r^A(x)=\{z\in A:\|z-x\|<r\}\).

## Proof

**1. Positive sums of open thresholds.** On every norm-dense \(A\) and for \(r,s>0\),
\[
R_{r+s}^A=R_r^A\circ R_s^A.
\]
One inclusion follows by the triangle inequality. For the converse, if \(\|x-y\|<r+s\), choose a point on the line segment from \(x\) to \(y\) with its two distances strictly below \(r\) and \(s\). The two strict inequalities persist on an open neighborhood of this point, which contains a point of \(A\). Since \(f\) and \(f^{-1}\) preserve relational compositions, preservation of \(R_a\) and \(R_b\) implies preservation of \(R_{ma+nb}\) for all integers \(m,n\ge0\) with \(m+n>0\).

**2. Positive differences yield closed thresholds.** For every \(r>s>0\), and every \(x,y\in A\),
\[
C_{r-s}^A(x,y)
\quad\Longleftrightarrow\quad
R_s^A(y)\subseteq R_r^A(x).
\tag{1}
\]
Indeed, if \(\|x-y\|\le r-s\), every \(z\) with \(\|z-y\|<s\) has \(\|z-x\|<r\). Conversely, if \(d=\|x-y\|>r-s\), then \(d>0\). Choose \(t\) strictly between \(\max\{0,r-d\}\) and \(s\), and set \(z_0=y+t(y-x)/d\). Then \(\|z_0-y\|=t<s\) but \(\|z_0-x\|=d+t>r\). Density provides \(z\in A\) sufficiently close to \(z_0\) to retain both strict inequalities. Thus the inclusion in (1) fails. A bijection carrying each of the open-ball families onto the corresponding target families preserves their inclusion relations, so any preserved pair \(R_r,R_s\) with \(r>s\) determines and preserves \(C_{r-s}\). Taking \(r=2s\) also shows that preservation of \(R_s\) implies preservation of \(C_s\).

**3. All integer-combination closed thresholds.** Let
\[
H=\{ma+nb:m,n\in\mathbb Z\}.
\]
For each \(h\in H\) with \(h>0\), the relation \(C_h\) is preserved: if \(h=ma+nb\) with \(m,n\ge0\), Step 1 gives \(R_h\), hence Step 2 gives \(C_h\). Otherwise \(h\) is a positive difference of two nonnegative integer multiples of \(a\) and \(b\), so Steps 1 and 2 give \(C_h\) directly. This reasoning applies identically in \(A\) and \(B\); no completeness is needed.

**4. Density and affine extension.** If \(a/b\notin\mathbb Q\), the positive elements of the additive group \(H\) are dense in \((0,\infty)\). For fixed \(x,y\in A\), the two nonnegative numbers \(d_X=\|x-y\|_X\) and \(d_Y=\|f(x)-f(y)\|_Y\) satisfy
\[
d_X\le h\quad\Longleftrightarrow\quad d_Y\le h
\qquad\text{for every }h\in H,\ h>0.
\]
If these numbers differed, a positive \(h\in H\) strictly between them would contradict the equivalence. Therefore \(d_X=d_Y\) for all pairs. An isometry on the dense set \(A\) extends uniquely by completion, and its range is the whole of \(\widehat Y\), since the extension has closed range containing the dense set \(B\). The Mazur–Ulam theorem makes this surjective metric isometry affine.

**5. Sharpness at rational ratios.** Suppose \(a/b=p/q\) with positive relatively prime integers \(p,q\), and define \(\delta=a/p=b/q\). On \(\mathbb R\), set
\[
g(k\delta+u)=k\delta+\frac{u^2}{\delta},
\qquad k\in\mathbb Z,\quad 0\le u<\delta.
\]
It is a strictly increasing bijection with \(g(x+n\delta)=g(x)+n\delta\) for every integer \(n\). For each positive integer \(n\), monotonicity and this translation identity imply
\[
|x-y|<n\delta\quad\Longleftrightarrow\quad|g(x)-g(y)|<n\delta.
\]
In particular it preserves the two thresholds \(a=p\delta\) and \(b=q\delta\). But \(g(\delta/2)=\delta/4\), so it is not an isometry. This shows that commensurable thresholds cannot force universal rigidity, even on a complete one-dimensional space.

## Verification

Each nonstandard inference is proved above: the open-relation composition uses normed-space segments and density, while the inclusion identity (1) uses extendable normed-space rays and a strict inequality that survives approximating points in a dense subset. The arithmetic density step applies to arbitrary irrational ratios. The completion extension uses only the established exact distance preservation; the proof does not infer an infinite statement from sample calculations.

Run the standalone exact-rational supplementary checker using `python3 check.py`. It checks a nonlinear rational-ratio witness at \(a=6/5\), \(b=9/5\), \(\delta=3/5\), testing \(362404\) proximity comparisons and \(6321\) translation identities. This finite experiment corroborates the example but is not used to justify the universal theorem.

## Relationship to prior work

Wang, Tang, and Luo [1] study **single-scale** step-isometries and geometry-dependent rigidity of dense subsets. Their Lemma 5.11 supplies a unit-scale nonlinear real-line example, and Lemma 6.1 uses an open-ball inclusion to recover closed integer-radius balls on a whole space. In contrast, the theorem here requires only **two strict threshold relations**, uses norm-density directly, imposes no geometry on the norm, and identifies the arithmetic condition that makes all metric distances recoverable. The single-scale theorems do not imply this uniform two-scale criterion on spaces with nonisometric step-isometries.

Balister and coauthors [2] classify one-scale step-isometries of finite-dimensional normed spaces using their \(\ell_\infty\)-summands, and Balogh, Walters, and Zsák [3] establish one-scale rigidity for strictly convex reflexive spaces. Neither stated theorem gives rigidity on every normed space under two incommensurable thresholds. Exact-distance preservation results of Aleksandrov–Beckman–Quarles type address a different hypothesis: the present hypotheses **do not assume either radius is an exactly preserved distance**.

## Limitations

The result is about **strict**, **bidirectional** threshold preservation by a **bijection** on a **dense subset**. It does not cover sparse subsets, one-way adjacency-preservers, noisy threshold observations, or general metric spaces lacking linear segments and outward ray extensions. When \(a/b\) is rational, counterexamples show only that universal rigidity fails; some individual normed spaces can remain rigid. The proof is complete under its stated assumptions, but bibliographic priority against unindexed two-scale proximity results requires independent literature review. No independent audit has been performed.

## References

1. R. Wang, L. Tang, J. Luo, *Step-isometries on Banach spaces*, arXiv:2611.09463v1 (first public 2026-11-06), https://arxiv.org/html/2611.09463v1. Especially Sections 1, 5–6, Lemmas 5.11 and 6.1.
2. P. Balister, B. Bollobás, K. Gunderson, I. Leader, M. Walters, *Random Geometric Graphs and Isometries of Normed Spaces*, arXiv:1504.05324v1 (2015-04-21), https://arxiv.org/pdf/1504.05324. Especially Introduction and Theorems 4–5.
3. J. Balogh, M. Walters, A. Zsák, *Random Geometric Graphs in Reflexive Banach Spaces*, arXiv:2409.04237v1 (2024-09-06), https://arxiv.org/pdf/2409.04237. Especially Introduction and Theorem 3.
4. S. Mazur and S. Ulam, *Sur les transformations isométriques d'espaces vectoriels normés*, C. R. Acad. Sci. Paris 194 (1932), 946–948 (affine-isometry theorem).
