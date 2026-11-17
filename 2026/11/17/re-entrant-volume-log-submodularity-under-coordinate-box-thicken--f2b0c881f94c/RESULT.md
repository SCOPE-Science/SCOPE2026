# Re-entrant volume log-submodularity under coordinate-box thickening of a four-zonotope

## Finding
Let \(e_1,e_2,e_3,e_4\) be the standard basis of \(\mathbb R^4\), let \(d_{ij}=e_i-e_j\), and write \(Z(g_1,\ldots,g_m)=\sum_j[0,g_j]\). Fix the six-generator zonotope and the two test segments
\[
A=Z(e_1,e_2,e_3,d_{24},d_{34},e_1-e_2-e_3),\qquad
B=[0,d_{14}],\qquad C=[0,d_{23}].
\]
For \(a,b,c,d\ge0\), let the coordinate-box thickening be
\[
H(a,b,c,d)=A+[0,ae_1]+[0,be_2]+[0,ce_3]+[0,de_4]
\]
and define its **volume log-submodularity defect**
\[
\Delta(H)=|H|\,|H+B+C|-|H+B|\,|H+C|.
\]
All volumes are ordinary four-dimensional Lebesgue volumes; positive defect means failure of the log-submodularity inequality. The complete four-weight defect is the following explicit polynomial:
\[
\begin{aligned}
\Delta(H(a,b,c,d))={}&-a^2(b-c)^2-4a^2\\
&+2ad(b^2+c^2)+6ad(b+c)+4ad+8a(b+c)+8abc\\
&-d^2\bigl(b^2+c^2+4(b+c)+8\bigr)\\
&+8bc+8(b+c)-4d+4.
\end{aligned}
\]
In particular this formula gives the **exact sign criterion** for every nonnegative axis-aligned box, including degenerate boxes.

The canonical two-block family, whose equal side lengths follow the disjoint coordinate supports of the two test directions, is
\[
H_{u,v}=H(u,v,v,u),\qquad u,v\ge0.
\]
Its defect factors unexpectedly simply:
\[
\boxed{\quad\Delta(H_{u,v})=2\bigl((u+2)^2v(v+2)-2(u+1)(2u-1)\bigr).\quad}
\]
This gives a sharp phase diagram. For \(0\le u<1/2\), the defect is strictly positive for all \(v\ge0\); at \(u=1/2\), equality occurs exactly when \(v=0\). For every \(u>1/2\), set
\[
v_*(u)=\frac{\sqrt{5u^2+6u+2}}{u+2}-1.
\]
Then \(\Delta(H_{u,v})<0\) for \(0\le v<v_*(u)\), equals zero at \(v=v_*(u)\), and is strictly positive for \(v>v_*(u)\). The boundary \(v_*(u)\) increases strictly from zero to \(\sqrt5-1\); in particular, \(v\ge\sqrt5-1\) forces strict failure for all finite \(u\ge0\).

The defect is **re-entrant under nested Minkowski additions**:
\[
\Delta(H_{0,0})=4>0,\qquad
\Delta(H_{1,0})=-8<0,\qquad
\Delta(H_{1,1})=46>0,
\]
although \(H_{0,0}\subset H_{1,0}\subset H_{1,1}\). Conversely, isotropic cubical thickening never repairs the inequality: for \(t\ge0\),
\[
\boxed{\quad\Delta(H_{t,t})=2(t^4+6t^3+8t^2+6t+2)>0.\quad}
\]
For every ambient dimension \(D\ge4\), Cartesian product with any positive-volume convex body in \(\mathbb R^{D-4}\), keeping \(B,C\) in the first four coordinates, preserves the same defect-sign classification.

## Assumptions and scope
The original generator list \(A\), the directions \(B,C\), and the coordinate axes are fixed as displayed. Every thickening parameter is real and nonnegative. The full-dimensionality of \(A\) is immediate from the independent vectors \(e_1,e_2,e_3,d_{24}\). A degenerate coordinate segment of length zero is permitted. Replacing \([0,ae_i]\) by the centered segment \([-ae_i/2,ae_i/2]\) merely translates the zonotope and does not change any volume. The finding is an exact parameter-family statement, not a universal claim about all zonoids or all choices of regularizing bodies.

## Proof
**1. Determinant expression and polynomiality.** For any spanning list of generators \(g_1,\dots,g_m\in\mathbb R^4\), its zonotope volume is
\[
|Z(g_1,\dots,g_m)|=\sum_{1\le i_1<i_2<i_3<i_4\le m}
\left|\det(g_{i_1},g_{i_2},g_{i_3},g_{i_4})\right|.
\]
This follows by the standard zonotope decomposition into parallelotopes, with multiplicity accounted for by maximal minors. When the four coordinate vectors are adjoined with nonnegative coefficients \(a,b,c,d\), each minor uses each adjoined column at most once. Its absolute value is an integer times a squarefree monomial in \(a,b,c,d\). Therefore all four required volumes are multiaffine integer polynomials, valid on the *entire* nonnegative orthant, with no hidden sign chambers.

**2. Four-weight identity.** Evaluate the maximal minors for the generator lists \(A\), \(A+B\), \(A+C\), and \(A+B+C\), always with the four coordinate-box segments adjoined. The accompanying dependency-free `verify.py` reconstructs all four polynomial coefficient dictionaries from the displayed integer vectors and checks their product difference coefficient-by-coefficient. The resulting difference is exactly the four-weight polynomial stated in Finding. The constant terms of the four volumes are respectively \(14,30,26,56\), giving \(14\cdot56-30\cdot26=4\), consistent with the published unthickened example. Because the polynomials were derived from *all* four-by-four minors, the coefficient identity proves the formula for arbitrary real nonnegative weights, not merely the test values.

**3. Independent two-block reconstruction.** Substituting \((a,b,c,d)=(u,v,v,u)\) into the four volume polynomials yields
\[
\begin{aligned}
|H_{u,v}|={}&u^2v^2+6u^2v+8u^2+4uv^2+20uv+22u+4v^2+16v+14,\\
|H_{u,v}+B|={}&u^2v^2+6u^2v+8u^2+6uv^2+32uv+38u+8v^2+32v+30,\\
|H_{u,v}+C|={}&u^2v^2+8u^2v+14u^2+4uv^2+28uv+40u+4v^2+24v+26,\\
|H_{u,v}+B+C|={}&u^2v^2+8u^2v+14u^2+6uv^2+44uv+68u+8v^2+48v+56.
\end{aligned}
\]
Their determinant expression and the four-weight coefficient calculation are independently reproducible using the included script. Multiplying the first and fourth, subtracting the product of the second and third, and collecting terms gives the boxed two-block factorization.

**4. Sharp sign boundary.** Since \(v(v+2)\ge0\), the factorization is strictly positive for \(u<1/2\). For \(u=1/2\), it vanishes only at \(v=0\). For \(u>1/2\), the expression is strictly increasing in \(v\ge0\) and its unique nonnegative root is the stated \(v_*(u)\). Its monotonicity and limiting value follow by writing
\[
v_*(u)=\sqrt{1+\frac{2(u+1)(2u-1)}{(u+2)^2}}-1
\]
and differentiating the fraction: its derivative is \(2(7u+4)/(u+2)^3>0\), and the fraction tends to \(4\). The re-entrant sign examples and isotropic formula result from the same exact identity. For a Cartesian product with a full-dimensional body of volume \(q>0\), each relevant volume is multiplied by \(q\), so the defect is multiplied by \(q^2>0\).

## Verification
Run `python3 verify.py` with ordinary Python; no nonstandard dependencies or external files are needed. It enumerates all four-by-four minors using 24-term exact integer determinants, builds the four multiaffine volume polynomials, verifies each of the 22 nonzero four-variable defect coefficients, verifies the complete four two-block volume coefficient dictionaries and the factorized defect, and independently checks 81 two-block rational parameter combinations plus seven anisotropic rational parameter combinations. The packaged verifier passed, reporting `PASS 103 assertion groups 22 nonzero four-variable defect monomials`. Finite evaluations are supplementary; the exhaustive minor enumeration together with the algebraic sign proof establishes the stated continuum of parameter values.

## Relationship to prior work
Skorupinski, *Zonoid volumes are not log-submodular* (arXiv:2608.07702, first version 2026-08-07), exhibited exactly the unthickened six-generator base and test segments, proving the positive defect \(4\). That example and the underlying four-volume determinant identity are prior work. The present claim concerns the previously unstated effect of *adding independent coordinate-box segments to the base*, including an exact four-variable defect, a sharp two-block sign boundary, and a nonmonotone nested regularization chain. Previously recorded analyses varied the exceptional generator's scale or direction, or varied the two test directions against a fixed base; none of these operations is Minkowski box thickening of the base. Work on Rayleigh volume polynomials by Fradelizi and collaborators gives general context but not the explicit box phase boundary here.

## Limitations
This is a self-review exact family computation, not an independently audited theorem. It does not assert that coordinate-box regularization of *every* non-Rayleigh zonotope has re-entrant behavior. The full four-weight polynomial provides an exact sign test but no closed classification of the topology of its four-dimensional sign chambers; the phase classification is complete only on the natural two-block slice. Published mathematical records may contain unindexed equivalent calculations. In particular, the complete text of Fradelizi et al., arXiv:2608.12681, was unavailable through the available access path, so no full-document noncoverage claim is made for that paper.

## References
1. R. Skorupinski, *Zonoid volumes are not log-submodular*, arXiv:2608.07702v1 (2026-08-07), https://arxiv.org/html/2608.07702.
2. M. Fradelizi, A. Hubard, A. Manui, C. S. Ndiaye, S. Wang, and A. Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681v1 (2026-08-13), https://arxiv.org/abs/2608.12681.
3. G. Averkov, K. von Dichter, and I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v2 (2026-10-20 revision), https://arxiv.org/abs/2608.14909.
4. M. Fradelizi, M. Madiman, M. Meyer, and A. Zvavitch, *On the volume of the Minkowski sum of zonoids*, J. Funct. Anal. 286 (2024), 110247.
