# Joint fibers and quadratic support of consecutive Engel outputs in three-dimensional simple Lie algebras

## Finding
Let \(q\) be any odd prime power and let \(L=\mathfrak{sl}_2(\mathbb F_q)\), with \(Q(U)=-\det U\) and its polar form \(B(U,V)=\operatorname{tr}(UV)\). For each \((X,Y)\in L^2\), set
\[
Z=[X,[X,Y]],\qquad W=[X,Z]=[X,[X,[X,Y]]].
\]
For **each prescribed pair** \((Z,W)\in L^2\), the exact number \(N_q(Z,W)\) of ordered input pairs producing it is the following disjoint complete rule:

1. If \(Z=W=0\), then \(N_q(Z,W)=2q^4-q^2\). If \(Z=0\) and \(W\ne0\), the fiber is empty.
2. If \(Z\ne0\) and \(Q(Z)=0\), then \(N_q(Z,0)=(q-1)q^2\); for each \(\lambda\in\mathbb F_q^\times\), \(N_q(Z,\lambda Z)=q^2\). Every other \(W\) has an empty fiber.
3. If \(Q(Z)\ne0\), then \(N_q(Z,W)=q\) exactly when \(B(Z,W)=0\) and \(Q(W)\ne0\), and \(N_q(Z,W)=0\) otherwise.

The joint image has **exactly**
\[
1+q(q^2-1)\bigl(1+(q-1)^2\bigr)
\]
points. It is much smaller than the ambient \(q^6\) pairs. The joint distribution genuinely refines each single-depth Engel fiber: for a prescribed nonzero isotropic \(Z\), the conditional value \(W=0\) has probability \(1/2\), and each of the \(q-1\) nonzero multiples \(W=\lambda Z\) has probability \(1/(2(q-1))\). For nonisotropic \(Z\), \(W\) is uniform on the nonisotropic vectors in the two-dimensional orthogonal plane \(Z^\perp\).

## Assumptions and scope
All matrices are traceless \(2\times2\) matrices over a finite field of odd cardinality \(q\ge3\). Brackets mean the ordinary Lie bracket \([U,V]=UV-VU\), and all input/output matrices are labeled, not taken modulo conjugacy. A zero quadratic value does not force a zero vector. \(N_q(Z,W)\) counts *ordered* pairs \((X,Y)\). Characteristic two and arbitrary coefficient rings are not asserted.

## Proof
**1. Matrix identities.** By the Cayley–Hamilton identity and polarization, traceless matrices satisfy
\[
X^2=Q(X)I,\qquad XY+YX=B(X,Y)I.
\]
Direct multiplication gives
\[
\operatorname{ad}_X^2Y=4Q(X)Y-2B(X,Y)X,
\qquad \operatorname{ad}_X^3Y=4Q(X)\operatorname{ad}_XY.
\]
Consequently \(\operatorname{ad}_X^2\) is zero if \(X=0\), has rank one with image \(\mathbb F_qX\) when \(X\ne0\) is isotropic, and has rank two with image \(X^\perp\) when \(Q(X)\ne0\). In these three cases, a nonempty \(Y\)-fiber has respectively \(q^3\), \(q^2\), or \(q\) points. The bilinear form \(B\) is nondegenerate in odd characteristic.

**2. Zero first output.** Every triple bracket following \(Z=0\) is also zero. The zero output receives \(q^3\) input choices from \(X=0\), \((q^2-1)q^2\) from nonzero isotropic \(X\), and \((q^3-q^2)q\) from nonisotropic \(X\). Since \(Q=0\) has exactly \(q^2\) vectors in the split three-dimensional quadratic space \(L\), their sum is \(2q^4-q^2\).

**3. Isotropic nonzero first output.** Fix \(Z\ne0\) with \(Q(Z)=0\). For isotropic \(X\), the rank-one image condition forces \(X\) to be a nonzero scalar multiple of \(Z\); there are \(q-1\) such \(X\), each giving \(q^2\) input values \(Y\) and \(W=0\). For nonisotropic \(X\), necessarily \(B(X,Z)=0\). By conjugating the nilpotent \(Z\) in \(\operatorname{GL}_2(\mathbb F_q)\), assume \(Z=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). Every orthogonal \(X\) has shape \(\begin{psmallmatrix}a&b\\0&-a\end{psmallmatrix}\), with \(Q(X)=a^2\). When \(a\ne0\), the subsequent bracket is \(W=[X,Z]=2aZ\). Thus each prescribed \(W=\lambda Z\ne0\) fixes \(a=\lambda/2\), allows \(q\) choices of \(b\), and each of these has \(q\) allowable values of \(Y\). This gives \(q^2\). Isotropic \(X\) cannot give nonzero \(W\), and nonisotropic \(X\) cannot give \(W=0\).

**4. Nonisotropic first output.** Fix \(Q(Z)\ne0\). The image condition for \(Z\) forces \(X\in Z^\perp\) and \(Q(X)\ne0\). Necessarily \(B(Z,W)=0\). Restricted to \(Z^\perp\), the map \(\operatorname{ad}_Z\) is invertible, since \(\operatorname{ad}_Z^2\) equals multiplication by \(4Q(Z)\) there. Hence there is precisely one candidate
\[
X=-\frac{[Z,W]}{4Q(Z)}.
\]
The polarization determinant identity \(Q([Z,W])=B(Z,W)^2-4Q(Z)Q(W)\) gives \(Q(X)=-Q(W)/(4Q(Z))\). Thus the candidate is admissible exactly when \(Q(W)\ne0\). Every admissible \(X\) has \(q\) preimages under \(\operatorname{ad}_X^2\), proving the third row and excluding all other cases.

**5. Image cardinality and exhaustive consistency.** There are \(q^2-1\) nonzero isotropic \(Z\), each permitting \(q\) values of \(W\). For \(Q(Z)\ne0\), if \(Q(Z)\) is a square, \(Z^\perp\) has \((q-1)^2\) nonisotropic vectors; if it is a nonsquare, \(Z^\perp\) has \(q^2-1\). The numbers of such \(Z\) are respectively \(q(q^2-1)/2\) and \(q(q-1)^2/2\), giving \(q(q^2-1)(q-1)^2\) admissible nonisotropic-output pairs. Adding the unique zero pair and the isotropic contribution gives the stated support count. Summing the exact fiber sizes over the entire output support gives \(q^6\), the total number of input pairs. In particular, summing over \(W\) gives the previously known single-output two-Engel counts at each \(Z\), but does not determine these joint fibers.

## Verification
The standalone script `verify_joint.py` enumerates *every* ordered input pair and *every* prescribed output pair over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\). It implements the bracket by matrix coefficients rather than by the proof's adjoint-square formula, and implements \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) directly. It compares all \(q^6\) output-fiber sizes to the theorem and checks the total mass and support count. Run `python verify_joint.py`; the exact captured output is `verify_joint_output.txt`. Finite tests corroborate but do not substitute for the proof in the preceding section.

## Relationship to prior work
The classical study by Bandman–Gordeev–Kunyavskii–Plotkin gives dominance and image/surjectivity results for Lie polynomials, including Engel monomials, rather than a complete simultaneous prescribed-target distribution for two adjacent output depths. Roy–Singh studies Engel-map surjectivity and lifting over local rings; its fiber discussions concern existence and lifting for single Engel outputs, not exact *joint* finite-field multiplicities. The single-output two-Engel prescribed-target count for this Lie algebra is already known and is **not** claimed as new: it is recovered by summing the second-coordinate fibers. The new content here is the joint image/support criterion, each nonzero second-coordinate fiber, and the corresponding conditional laws. These statements are not implied by the marginal distributions alone.

## Limitations
No result is asserted in characteristic two, where the polar form and inverse of four behave differently. The argument does not classify all pairs up to simultaneous conjugacy, higher-dimensional simple Lie algebras, or the analogous maps over valuation rings. Independent review of priority and proof remains necessary; an unindexed older joint-fiber computation cannot be ruled out. This is an exact finite-field theorem for the specified two coordinate functions, not a claim about general Engel map fibers.

## References
- T. Bandman, N. Gordeev, B. Kunyavskii, E. Plotkin, *Equations in simple Lie algebras*, arXiv:1012.4106 (first public version 2010-12-18), https://arxiv.org/abs/1012.4106.
- A. Roy, A. Singh, *Surjectivity of Engel Maps over trace zero matrices in* \(M_2(\mathcal O)\), arXiv:2607.21171 (2026-07-23), https://arxiv.org/abs/2607.21171.
