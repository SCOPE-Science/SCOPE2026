# Shifted Ehrhart symmetry and a sharp log-concavity threshold for weighted directed-cycle simplices

## Finding
Let \(n\ge3\) and write indices modulo \(n\). For positive integer vertex weights \(w_1,\ldots,w_n\), consider the lattice polytope
\[
P_{\mathbf w}=\operatorname{conv}\{v_i=e_i+w_{i+1}e_{i+1}:1\le i\le n\}\subset\mathbb R^n.
\]
When \(1-(-1)^n\prod_iw_i\ne0\), this is an \((n-1)\)-simplex whose proper faces have no nonvertex lattice points. Its Ehrhart numerator satisfies the *shifted reciprocal* law
\[
h_n^*=0,\qquad h_j^*=h_{n-j}^*\quad(1\le j\le n-1).
\]
For the equally weighted five-cycle with integer weight \(w\ge2\), this determines its complete Ehrhart numerator:
\[
h^*_{5,w}(t)=1+\binom{w}{4}(t+t^4)+\frac{w(w-1)(11w^2+5w+6)}{24}(t^2+t^3).
\]
The coefficients are log-concave **if and only if** \(w\ge7\), a sharp finite threshold within a family that fails the integer decomposition property for every such weight.

## Assumptions and scope
All lattice points use the integral lattice in the affine span of the polytope, and Ehrhart coefficients satisfy
\[
\sum_{m\ge0}|mP\cap\mathbb Z^n|t^m=\frac{h^*(t)}{(1-t)^n}.
\]
For nonuniform weights the determinant condition excludes the degenerate even cycle with every weight one; odd cycles are always nondegenerate. Log-concavity refers to all interior adjacent coefficient inequalities \(h_j^{*2}\ge h_{j-1}^*h_{j+1}^*\), allowing zeros. The five-cycle coefficients are displayed for integer \(w\ge2\) only. The initiating weighted-cycle literature includes Nanduri–Roy (2025), while the later 2026 preprint is used only for claim comparison and attribution.

## Proof
**1. The simplex and boundary.** Let \(M\) be the matrix with columns \(v_i\). The cyclic determinant expansion is
\[
\det M=1-(-1)^n\prod_{i=1}^nw_i.
\]
Thus the columns are linearly independent under the hypothesis and form affinely independent points. In any convex combination \(x=\sum_i\lambda_i v_i\), with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\), if one barycentric coefficient \(\lambda_i\) is zero and \(x\) is integral, its \((i+1)\)-st coordinate is \(x_{i+1}=\lambda_{i+1}+w_{i+1}\lambda_i=\lambda_{i+1}\). Hence \(\lambda_{i+1}\) is an integer in \([0,1]\). It is therefore zero or one. If one, \(x\) is a vertex; otherwise propagate around the cycle, forcing every coefficient to vanish, impossible. Thus every nonvertex integer point is interior. More strongly, applying the same argument to a fundamental parallelepiped with coefficients in \([0,1)\), any integer point with a zero coefficient forces all coefficients zero.

**2. Shifted reciprocity.** Form the half-open fundamental parallelepiped of the integral generators \((v_i,1)\):
\[
\Pi=\left\{\sum_{i=1}^n\lambda_i(v_i,1):0\le\lambda_i<1\right\}.
\]
Its lattice-point height enumerator is the Ehrhart numerator. By Step 1, every nonzero lattice point of \(\Pi\) has each \(\lambda_i\in(0,1)\). Complementing these coefficients gives another integral point in \(\Pi\), because both the original point and \(\sum_i(v_i,1)\) are integral; the involution changes the integral height from \(j\) to \(n-j\). The origin contributes the unique height-zero point, and no point has height \(n\). This proves the asserted shifted coefficient symmetry, for arbitrary permissible weights.

**3. Complete five-cycle lattice count.** Now take all five weights equal to \(w\ge2\). Every point of \(P\) has coordinate sum \(w+1\). The boundary argument shows all its nonvertex lattice points have strictly positive integer coordinates. Conversely, for \(w\ge4\), any integer point \(x\) with \(x_i\ge1\) and \(\sum_i x_i=w+1\) belongs to the simplex. To see this without an enumeration, put \(S e_i=e_{i+1}\), so
\[
M^{-1}=\frac{I-wS+w^2S^2-w^3S^3+w^4S^4}{1+w^5}.
\]
Write \(x=\mathbf1+y\) with \(y_i\ge0\) and \(\sum_i y_i=w-4\). Every coordinate of \(M^{-1}x\) is bounded below by
\[
\frac1{w+1}-\frac{(w-4)w^3}{1+w^5}
=\frac{1+3w^4+4w^3}{(w+1)(1+w^5)}>0.
\]
Here we use that every entry of \(M^{-1}\) is at least \(-w^3/(1+w^5)\). The barycentric coefficients sum to one, so they prove membership. For \(w=2,3\), no positive integral composition of sum \(w+1\) into five coordinates exists. Consequently
\[
|P\cap\mathbb Z^5|=5+\binom w4,
\]
using the convention \(\binom w4=0\) for \(w<4\).

**4. Volume and other coefficients.** The ambient affine lattice is \(\sum_i x_i=w+1\). Its normalized simplex volume is
\[
V=\frac{\det M}{w+1}=\frac{w^5+1}{w+1}=w^4-w^3+w^2-w+1.
\]
The standard Ehrhart identities give \(h_0^*=1\), \(h_1^*=|P\cap\mathbb Z^5|-5=A_w\), and \(\sum_jh_j^*=V\). Shifted reciprocity yields \(h_4^*=h_1^*=A_w\) and \(h_3^*=h_2^*=B_w\). Hence
\[
B_w=\frac{V-1-2A_w}{2}=\frac{w(w-1)(11w^2+5w+6)}{24}.
\]
No finite enumeration is being used to infer an infinite polynomial identity.

**5. Sharp threshold.** For \(w\ge2\),
\[
B_w-A_w=\frac{5w^2(w^2-1)}{12}>0.
\]
Thus the five-term sequence \((1,A_w,B_w,B_w,A_w)\) is log-concave precisely when \(A_w^2\ge B_w\). For \(w=2,3\), \(A_w=0<B_w\). For real \(w>3\), the ratio
\[
\frac{B_w}{A_w}=\frac{11w^2+5w+6}{(w-2)(w-3)}
\]
is strictly decreasing, with derivative \(-60(w^2-2w-1)/((w-2)^2(w-3)^2)<0\), while \(A_w\) is strictly increasing. At integer \(w=6\), \(A_w=15\) and \(B_w=540\), so log-concavity fails. At \(w=7\), \(A_w=35\) and \(B_w=1015\), so \(A_w^2=1225>B_w\). These comparisons establish the exact integer cutoff.

## Verification
The accompanying `verify.py` independently enumerates lattice points in the first two dilations for integer weights \(2\le w\le9\) using exact integer barycentric inequalities. It checks the resulting first and second coefficients against the formulas, the determinant/volume sum, the predicted shift symmetry, and the threshold over further integer weights. The analytic arguments above, not the finite tests, establish the general theorems. Run `python3 verify.py` from the extracted package directory.

## Relationship to prior work
Nanduri and Roy (2025) study toric ideals and naturally oriented weighted cycles, fixing the generating exponent-vector convention used here, but do not derive the Ehrhart numerator or its sharp log-concavity threshold. Nill (2026) establishes eventual real-rootedness at sufficiently large lattice width in a fixed dimension, a qualitative general theorem with no explicit five-cycle cutoff. Biermann, Lin and O'Keefe (first posted November 12, 2026) prove the unit-dilate lattice-point description of uniformly weighted directed cycles (Proposition 3.10) and the failure of their integer decomposition property (Theorem 4.5); both facts are explicitly credited. The present proof independently derives its needed lattice-point count, and the claimed contribution is restricted to the all-weight shifted Ehrhart symmetry, the complete five-cycle numerator and the exact threshold \(w=7\). Prior work on unweighted directed **root** polytopes (vertices are differences of basis vectors) concerns a different lattice model and does not imply the weighted positive-exponent result.

## Limitations
This result treats a single directed cycle and says nothing about arbitrary directed graphs or arbitrary weights' log-concavity. The log-concavity cutoff is for **five** vertices; no general threshold is asserted for other cycle sizes. The known broad boundary-parallelepiped reciprocity argument is a standard tool, not claimed as a novel general lattice-simplex principle. Unindexed earlier specialized Ehrhart computations remain a historical-priority risk; independent external review has not been performed.

## References
- R. Nanduri and T. K. Roy, *On robust toric ideals of weighted oriented graphs*, arXiv:2504.15200 (first posted 2025-04-21), https://arxiv.org/abs/2504.15200.
- B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635 (first posted 2026-08-04), https://arxiv.org/abs/2608.03635.
- J. Biermann, K.-N. Lin and A. O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs*, arXiv:2611.17047 (first posted 2026-11-12), https://arxiv.org/abs/2611.17047.
