# The isosceles metric James constant coincides with the metric James constant
## Finding
For every real Banach space \(X\) with \(\dim X\ge 2\), let the classical James constant be
\[
J(X)=\sup_{x,y\in S_X}\min\{\lVert x+y\rVert,\lVert x-y\rVert\}.
\]
Chen--Yang--Liu--Li define the isosceles metric James-type constant
\[
J_2(X)=\sup\left\{\frac{\lVert x+y\rVert}{1+\lVert x+y\rVert}:x,y\in S_X,\ x\perp_I y\right\},
\]
where \(x\perp_I y\) means \(\lVert x+y\rVert=\lVert x-y\rVert\). Then
\[
J_2(X)=\frac{J(X)}{1+J(X)}.
\]
Moreover, the metric James-type constant \(J_1\) from the same paper satisfies the same formula, so
\[
J_2(X)=J_1(X)
\]
for every real Banach space in the defining scope.

## Assumptions and scope
The scalar field is real and \(\dim X\ge2\). No finite-dimensionality, reflexivity, strict convexity, smoothness, or attainment of any supremum is assumed.

The result concerns only the exact relation among \(J\), \(J_1\), and \(J_2\). It does not identify the later constant \(J_3\), nor does it assert any new formula for \(J_4\).

## Proof
Set
\[
f(t)=\frac{t}{1+t},\qquad t\ge0.
\]
The function \(f\) is continuous and strictly increasing.

A standard isosceles representation of the James constant is
\[
J(X)=\sup\{\lVert x+y\rVert:x,y\in S_X,\ x\perp_I y\}.
\]
This representation is stated explicitly in the later literature on isosceles-orthogonal James profiles and is the same representation underlying the comparison made in the defining paper.

Therefore
\[
\begin{aligned}
J_2(X)
&=\sup_{x,y\in S_X,\ x\perp_I y} f(\lVert x+y\rVert)\\
&=f\left(\sup_{x,y\in S_X,\ x\perp_I y}\lVert x+y\rVert\right)\\
&=f(J(X))
=\frac{J(X)}{1+J(X)}.
\end{aligned}
\]
The middle equality does not require an extremizing pair. The upper inequality follows from monotonicity. For the reverse inequality, choose admissible pairs with \(\lVert x+y\rVert\) tending to the supremum and use continuity of \(f\).

For completeness, the same monotonicity argument gives the exact formula for the source paper's first metric James-type constant. For fixed \(x,y\in S_X\),
\[
\min\{f(\lVert x+y\rVert),f(\lVert x-y\rVert)\}
=f\left(\min\{\lVert x+y\rVert,\lVert x-y\rVert\}\right).
\]
Taking suprema gives
\[
J_1(X)=f(J(X)).
\]
Thus \(J_1(X)=J_2(X)\) identically.

## Verification
The proof was checked against the defining 2022 paper at the definitions of \(J_1\) and \(J_2\) and at Theorem 8, which gives only the coarser comparison
\[
\frac{J(X)}{3}\le J_2(X)\le\frac{J(X)}{2}.
\]
The exact identity is compatible with both bounds because \(\sqrt2\le J(X)\le2\) implies
\[
\frac{J(X)}{3}\le\frac{J(X)}{1+J(X)}\le\frac{J(X)}{2}.
\]
It is also compatible with the source's Hilbert-space value \(J_2=2-\sqrt2\), since \(J=\sqrt2\) there.

The critical nontrivial input is the all-space isosceles representation of \(J(X)\); a later full-text treatment states it explicitly as a lemma. No numerical experiment or finite enumeration is used.

## Relationship to prior work
The 2022 defining paper introduces \(J_2\), describes it as a James-type constant obtained by imposing isosceles orthogonality, proves the Hilbert value, and establishes only the two-sided estimate above. The same paper treats \(J_1\) separately. It does not state that \(J_2\) is exactly \(J/(1+J)\), nor that \(J_1\) and \(J_2\) coincide for every Banach space.

A later treatment of isosceles-orthogonal Takahashi profiles states the exact representation
\[
J(X)=\sup\{\lVert x+y\rVert:x,y\in S_X,\ x\perp_I y\},
\]
which turns the defining optimization for \(J_2\) into a continuous monotone reparameterization. Targeted searches for the exact \(J_2\) formula, for the equality \(J_1=J_2\), and for equivalent isosceles-metric formulations did not locate a covering statement.

## Limitations
The originality assessment is necessarily limited by indexing: an obscure or unindexed source may have noticed the same short consequence. The result is structural rather than computational. It does not claim that the definitions of \(J_1\) and \(J_2\) are identical pointwise; only their suprema coincide universally.

## References
1. B. Chen, Z. Yang, Q. Liu, Y. Li, “Some New James Type Geometric Constants in Banach Spaces,” *Symmetry* 14 (2022), 405. DOI: 10.3390/sym14020405. Published 18 February 2022.
2. D. Sain, S. Ghosh, K. Paul, “On isosceles orthogonality and some geometric constants in a normed space,” *Aequationes Mathematicae* 97 (2023), 147–160. DOI: 10.1007/s00010-022-00909-y. Published online 1 September 2022.
3. “Isosceles-Orthogonal Takahashi–von Neumann–Jordan-Type Constants in Banach Spaces,” *Axioms* 15 (2026), 684; Lemma 1 records the all-space isosceles representation of the James constant.
