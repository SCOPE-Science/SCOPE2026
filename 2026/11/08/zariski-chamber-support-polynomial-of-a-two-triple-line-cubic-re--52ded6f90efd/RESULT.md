# Zariski-chamber support polynomial of a two-triple-line cubic resolution

## Finding
Let \(k=\mathbb C\), and choose six distinct points \(p_1,\ldots,p_6\in\mathbb P^2_k\) such that \(p_1,p_2,p_3\) lie on a line \(\ell_A\), while \(p_4,p_5,p_6\) lie on a distinct line \(\ell_B\), with \(\ell_A\cap\ell_B\) none of the six points. Let \(X\) be the blow-up of these six points. The two strict transforms of the special lines are intersecting \((-2)\)-curves; the anticanonical model is a cubic surface with one \(A_2\) singularity.

For \(0\le j\le6\), let \(z_j(X)\) denote the number of Zariski chambers whose negative part has support consisting of exactly \(j\) irreducible curves; the nef chamber has empty support. Then
\[
Z_X(t)=\sum_{j=0}^{6}z_j(X)t^j
=1+17t+100t^2+281t^3+401t^4+255t^5+37t^6.
\]
In particular, \(X\) has exactly \(1092\) Zariski chambers, and the largest possible support has six components. The asserted distribution holds for every configuration satisfying the stated hypotheses.

## Assumptions and scope
All geometry is over \(\mathbb C\). The two groups of three points are on distinct lines and their intersection is not a blown-up point. There are no further collinear triples: any line through two points of one group is the already specified special line, while a line through points from both groups contains only those two marked points. Let \(H\) denote the pullback of the line class and \(E_i\) the six exceptional divisors. Intersection numbers are \(H^2=1\), \(H\cdot E_i=0\), and \(E_i\cdot E_j=-\delta_{ij}\). The canonical class is \(K_X=-3H+\sum_{i=1}^{6}E_i\).

A Zariski chamber is counted by its support in the negative part of a big divisor's Zariski decomposition, equivalently by its negative-definite reduced curve support, including the empty support for the nef chamber [1, Proposition 1.1]. This statement concerns the smooth blow-up (the minimal resolution), not the singular cubic's divisor group.

## Proof
**1. The complete negative-curve list.** Put
\[
R_A=H-E_1-E_2-E_3,\qquad R_B=H-E_4-E_5-E_6.
\]
These are irreducible \((-2)\)-curves with \(R_A\cdot R_B=1\). Also there are the six exceptional \((-1)\)-curves \(E_i\) and nine \((-1)\)-curves \(L_{ij}=H-E_i-E_j\), where \(1\le i\le3\) and \(4\le j\le6\).

There are no other negative curves. Indeed, let \(C\) be a negative irreducible curve other than these two strict transforms or an exceptional curve. Its image is an irreducible plane curve of degree \(d\ge1\), with multiplicities \(m_i\ge0\) at the blown-up points. Bezout with the two distinct special lines yields \(\sum_{i=1}^{3}m_i\le d\) and \(\sum_{i=4}^{6}m_i\le d\). Thus \((-K_X)\cdot C=3d-\sum_i m_i\ge d\). By adjunction and the nonnegativity of arithmetic genus,
\[
-2\le C^2+K_X\cdot C\le -1-d.
\]
Hence \(d\le1\). For \(d=1\), the same inequalities force \(C^2=-1\) and \((-K_X)\cdot C=1\), so the line passes through exactly two marked points from opposite groups. Such lines are exactly the nine \(L_{ij}\). Therefore the list has precisely \(17\) negative curves. These inequalities also show that \(-K_X\) is nef; since \((-K_X)^2=3\), it is big. The only anticanonical degree-zero curves are \(R_A,R_B\), which meet in an \(A_2\) chain. The standard weak-del-Pezzo anticanonical contraction identifies the resulting cubic singularity type [3,4].

**2. Negative-definite supports.** Among the fifteen \((-1)\)-curves, any pair intersecting in one point has a singular \(2\times2\) intersection matrix, so it cannot occur in a negative-definite support. Accordingly, selected \((-1)\)-curves must be pairwise disjoint. Exceptional curves are pairwise disjoint. A cross-line \(L_{ij}\) intersects \(E_i\) and \(E_j\) once, and two distinct cross-lines intersect once exactly when their row and column indices are both different. Thus any nonempty pairwise-disjoint selection of the nine cross-lines lies entirely in one row or one column of the \(3\times3\) grid.

The cross-lines are disjoint from both \(R_A\) and \(R_B\). The root \(R_A\) meets just the exceptional curves of the first triple; \(R_B\) meets just those of the second triple. Let \(r\) and \(s\) be the numbers of selected exceptional curves in those groups. Schur complementation of the diagonal \(-I\) block of the selected \((-1)\)-curves shows that adding only \(R_A\) yields a negative-definite matrix if and only if \(r\le1\), and adding only \(R_B\) if and only if \(s\le1\). If both roots are added, their Schur complement is
\[
\begin{pmatrix}-2+r&1\\1&-2+s\end{pmatrix};
\]
it is negative definite exactly when \(r+s\le1\). This exhausts every possible support.

**3. Exact support polynomial.** For a fixed disjoint cross-line selection leaving \(a\) available exceptional curves from the first group and \(b\) from the second, define
\[
F_{a,b}(t)=\sum_{r=0}^{a}\sum_{s=0}^{b}
\binom ar\binom bs t^{r+s}
\bigl[1+t(\mathbf1_{r\le1}+\mathbf1_{s\le1})+t^2\mathbf1_{r+s\le1}\bigr].
\]
The three terms in the brackets represent respectively selecting no roots, exactly one root, and both roots. The disjoint cross-line choices consist of the empty set; nine single edges; nine two-edge row selections and nine two-edge column selections; and three complete rows and three complete columns. Hence
\[
Z_X(t)=F_{3,3}(t)+9tF_{2,2}(t)
+9t^2\bigl(F_{2,1}(t)+F_{1,2}(t)\bigr)
+3t^3\bigl(F_{2,0}(t)+F_{0,2}(t)\bigr).
\]
Expanding gives the coefficients in the finding, whose sum is \(1092\). Bauer--Funke--Neumann's chamber/support correspondence [1, Proposition 1.1] proves that this counts all Zariski chambers, not merely a family of potential supports. This completes the proof.

## Verification
Execute `python3 verify_chambers.py` from the directory containing this document. The standalone script independently constructs the complete \(17\times17\) intersection matrix from divisor classes, enumerates all \(2^{17}=131072\) subsets (pruning only those with an intersecting pair of \((-1)\)-curves), tests negative definiteness by exact rational Schur elimination, and checks the separate binomial formula. The expected output is included in `verification_output.txt`; it ends in `ALL_CHECKS_PASSED`.

This finite enumeration is exhaustive only because the proof has classified **all** negative curves. It is not being used to infer that curve classification from finitely many computations.

## Relationship to prior work
The general negative-definite-support correspondence and the count \(2764\) for the blow-up of six general points are due to Bauer--Funke--Neumann [1]. Bauer--Schmitz [2] improve the general matrix-enumeration algorithm and analyze smooth-del-Pezzo and Segre--Schur examples. Derenthal--Joyce--Teitler [3] treat nef-cone **volumes** for generalized del Pezzo surfaces and their ADE root configurations, not the exact cardinalities by negative-support size. Lubbes [4] classifies ADE root subsystems, including \(A_2\) for degree three, but does not state this support polynomial. The present result supplies the full incidence-based enumeration for the specified two-triple-line configuration; it does not assert novelty of the general chamber algorithm, the \(A_2\) configuration, or the negative-curve classification framework.

## Limitations
Historical priority of the exact coefficients remains provisional, since a specialized older table could conceivably contain them. The result is a complete exact invariant for the specified geometric family, not a classification of all weak del Pezzo root types or of chamber volumes. The symbolic verifier provides reproducible exact finite checking; independent mathematical review is not represented as having occurred.

## References
[1] T. Bauer, M. Funke and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958, first public version 2009-12-04. https://arxiv.org/abs/0912.0958

[2] T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, first public version 2012-04-19. https://arxiv.org/abs/1204.4373

[3] U. Derenthal, M. Joyce and Z. Teitler, *The nef cone volume of generalized Del Pezzo surfaces*, arXiv:math/0703202, first public version 2007-03-07. https://arxiv.org/abs/math/0703202

[4] N. Lubbes, *Algorithms for singularities and real structures of weak Del Pezzo surfaces*, arXiv:1302.6678, first public version 2013-02-27. https://arxiv.org/abs/1302.6678
