# The 285 Zariski chambers of a one-nodal quartic del Pezzo resolution

## Finding
Let \(X\) be the blow-up of \(\mathbb P^2_{\mathbb C}\) at five distinct points with exactly one collinear triple. Write \(z_r(X)\) for the number of Zariski chambers of the big cone whose negative part has exactly \(r\) irreducible components; the nef chamber has \(r=0\). Then
\[
\sum_{r\geq 0} z_r(X)t^r=1+13t+58t^2+112t^3+87t^4+14t^5.
\]
In particular, there are exactly \(285\) chambers, independently of the point positions subject to the stated incidence condition. In the anticanonically truncated cone-volume convention of Bauer--Schmitz, exactly \(178\) chambers have finite volume and \(107\) have infinite volume, with respective support polynomials
\[
Z_{\rm fin}(t)=1+12t+46t^2+72t^3+43t^4+4t^5,
\]
\[
Z_{\rm inf}(t)=t+12t^2+40t^3+44t^4+10t^5.
\]
The finite/infinite assertion concerns *chamber volumes* in a fixed linear slice, not the number of chambers; all chamber counts above are finite.

## Assumptions and scope
Work over \(\mathbb C\). Relabel the points so that \(p_1,p_2,p_3\) lie on a line and there is no other triple of collinear points. Set \(H\) equal to the pullback of a plane line and \(E_i\) equal to the exceptional divisor over \(p_i\). The intersection pairing is \(H^2=1\), \(E_i^2=-1\), \(H\cdot E_i=0\), and \(E_i\cdot E_j=0\) for distinct indices. The anticanonical class is \(-K_X=3H-\sum_{i=1}^5E_i\), with square \(4\). The unique \((-2)\)-curve is \(R=H-E_1-E_2-E_3\). The class \(-K_X\) is nef: given any nonexceptional irreducible plane curve \(C\), choose a reducible cubic through the five points, consisting of three lines and sharing no component with \(C\). (For a line \(C\), choose a pairing of four marked points avoiding it; for higher-degree \(C\), any such three-line cubic works.) Bezout then gives \(3\deg C\geq\sum_i\operatorname{mult}_{p_i}C\). Nefness and square \(4>0\) imply bigness. The anticanonical morphism contracts \(R\) to an \(A_1\) point.

By a Zariski chamber we mean the region of the big cone with a fixed support of the negative part of the Zariski decomposition. As in Bauer--Funke--Neumann, chambers (including the empty-support nef chamber) correspond bijectively to negative-definite reduced configurations of irreducible negative curves, including the empty configuration. For volume, use the normalized Lebesgue measure on \(\overline\Sigma\cap\{D:(-K_X)\cdot D\leq 1\}\) in the Neron--Severi real vector space, as in Bauer--Schmitz.

## Proof
**1. The complete negative-curve list.** Since \(-K_X\) is nef, adjunction gives \(C^2=2p_a(C)-2+(-K_X)\cdot C\) with \(p_a(C)\geq0\); therefore any irreducible curve with negative self-intersection has either \((C^2,(-K_X)\cdot C)=(-1,1)\) or \((-2,0)\). For a nonexceptional curve \(C=dH-\sum m_iE_i\), all \(m_i\) are nonnegative. In the first case \(\sum m_i=3d-1\) and \(\sum m_i^2=d^2+1\); Cauchy--Schwarz gives \((3d-1)^2\leq5(d^2+1)\), hence \(d\leq2\). If \(d=2\) all five multiplicities are one, requiring an irreducible conic through the five points. Such a conic cannot exist: a conic containing three distinct collinear points contains their line as a component. For \(d=1\) the nonexceptional \((-1)\)-curves are exactly the strict transforms of ordinary two-point lines, excluding the three pairs among \(\{1,2,3\}\). In the second case, \(\sum m_i=3d\) and \(\sum m_i^2=d^2+2\), so \(9d^2\leq5(d^2+2)\) and \(d\leq1\); the only possibility is the strict transform of the unique triple line. Adding the five exceptional curves yields precisely thirteen negative curves:
\[
E_1,\ldots,E_5,\quad L_{i4},L_{i5}\ (i=1,2,3),\quad L_{45},\quad R,
\]
where \(L_{ij}=H-E_i-E_j\). Twelve have square \(-1\); \(R\) has square \(-2\).

**2. Negative-definite supports.** Two distinct \((-1)\)-curves in a negative-definite support must be disjoint: the principal \(2\times2\) intersection submatrix with off-diagonal a positive integer is not negative definite. If \(R\) is included together with \(k\) mutually disjoint \((-1)\)-curves that meet \(R\) once, the Schur complement of the negative identity block is \(-2+k\); thus negative definiteness requires \(k\leq1\). Here \(R\) meets precisely \(E_1,E_2,E_3,L_{45}\). These conditions are sufficient because the other chosen \((-1)\)-curves are pairwise disjoint and orthogonal to \(R\).

**3. Counting by support size.** Let \(t\) record each selected component. Choose a subset \(A\subset\{E_1,E_2,E_3\}\) of size \(a\) and set \(m=3-a\). Among the remaining \(2m\) curves \(L_{i4},L_{i5}\), the only intersections are between \(L_{i4}\) and \(L_{j5}\) with distinct \(i,j\). Every disjoint selection uses a single type, or exactly the two matched curves with one index, giving
\[
F_m(t)=2(1+t)^m-1+mt^2.
\]
Allowing \(E_4,E_5,L_{45}\) gives
\[
G_m(t)=(1+t)F_m(t)+2t(1+t)^m+t^2.
\]
Indeed the first term records whether \(L_{45}\) is present without \(E_4,E_5\); the other terms record one or both of \(E_4,E_5\), which exclude \(L_{45}\) and one or both cross-line types.

Without \(R\), the generating polynomial is
\[
Z_{\rm fin}(t)=\sum_{a=0}^{3}\binom3a t^aG_{3-a}(t)
=1+12t+46t^2+72t^3+43t^4+4t^5.
\]
With \(R\), at most one of \(E_1,E_2,E_3,L_{45}\) may be present. If no \(E_i\) for \(i\leq3\) is selected, the choices are counted by \(G_3(t)\); if exactly one is selected, \(L_{45}\) is forbidden and the remaining choices are counted by
\[
H_2(t)=F_2(t)+2t(1+t)^2+t^2.
\]
Thus
\[
Z_{\rm inf}(t)=t\bigl(G_3(t)+3tH_2(t)\bigr)
=t+12t^2+40t^3+44t^4+10t^5.
\]
Summing these polynomials proves the main support distribution and the total \(285\).

**4. Finite versus infinite volume.** Theorem 1.4 of Bauer--Schmitz (2012) says a chamber containing a curve of self-intersection below \(-1\) has infinite anticanonically truncated volume; a chamber supported only on disjoint \((-1)\)-curves has volume proportional to the nef-cone volume of their simultaneous contraction. That nef-cone volume is finite here: for the contraction \(\pi:X\to Y\), the pullback \(\pi^*(-K_Y)=-K_X+\sum E\) is big, because \(-K_X\) is big and the contracted curves are effective. Thus \(-K_Y\) is big, and the Bauer--Schmitz nef-volume criterion applies. Our support classification has exactly one curve of self-intersection below \(-1\), namely \(R\). Consequently the polynomial without \(R\) counts exactly finite-volume chambers and the polynomial with \(R\) counts exactly infinite-volume chambers. The nef chamber is finite because \(-K_X\) is big.

## Verification
The accompanying standard-library-only program `verify.py` independently constructs the thirteen integral divisor classes, computes their exact intersection matrix, and tests *all* \(2^{13}=8192\) subsets for negative definiteness by rational Schur-complement elimination. It compares the resulting two coefficient vectors with a separate symbolic implementation of the combinatorial formulas. Its complete output is in `verify_output.txt` and ends in `ALL_CHECKS_PASSED`. Exhaustive finite matrix enumeration checks this specified list of thirteen curves; the proof of completeness of the geometric curve list is the argument in Step 1, not a computational inference.

## Relationship to prior work
Bauer--Funke--Neumann, *Counting Zariski chambers on del Pezzo surfaces* (arXiv:0912.0958, first posted 2009-12-04), prove the negative-support/chamber correspondence and count \(393\) chambers for the **smooth** degree-four del Pezzo surface arising from five general blown-up points. Their table does not state the distribution for a blow-up with one collinear triple. The present one-nodal degeneration has \(108\) fewer chambers than that smooth model.

Bauer--Schmitz, *Volumes of Zariski chambers* (arXiv:1205.3817, first posted 2012-05-16), establish the general finite/infinite-volume criterion, but do not state the two support polynomials for this one-nodal quartic surface. Their collinear-point example requires all points collinear, unlike this configuration. Bauer--Schmitz, *Zariski chambers on surfaces of high Picard number* (arXiv:1204.4373, first posted 2012-04-19), develops a general counting algorithm, not this particular geometric census. The general structural theorems and the smooth \(393\) total are prior work, not novelty claims.

## Limitations
The theorem is stated over \(\mathbb C\); no extension of its analytic volume convention to arbitrary characteristic is asserted. The chamber count is a specialization to the natural one-nodal quartic model, not a classification for every weak del Pezzo surface. Numerical coincidences or an equivalent result in an unindexed specialist table remain possible; absence in targeted searches does not establish historical priority.

## References
- Thomas Bauer, Michael Funke, Sebastian Neumann, *Counting Zariski chambers on del Pezzo surfaces*, arXiv:0912.0958 (2009-12-04), https://arxiv.org/abs/0912.0958.
- Thomas Bauer, David Schmitz, *Volumes of Zariski chambers*, arXiv:1205.3817 (2012-05-16), https://arxiv.org/html/1205.3817v1.
- Thomas Bauer, David Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (2012-04-19), https://arxiv.org/abs/1204.4373.
