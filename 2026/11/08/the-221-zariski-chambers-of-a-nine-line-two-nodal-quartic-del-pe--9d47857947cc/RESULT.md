# The 221 Zariski chambers of a nine-line two-nodal quartic del Pezzo resolution

## Finding
Let \(p_0,p_1,p_2,p_3,p_4\) be distinct complex points in \(\mathbb P^2\) with \(p_0,p_1,p_2\) on one line \(L_A\), \(p_0,p_3,p_4\) on a different line \(L_B\), and no further triple collinearity. Let \(X\) be their ordinary (not infinitely near) blow-up. The anticanonical model of \(X\) is a quartic del Pezzo surface with precisely two \(A_1\) singularities and nine lines (the nine-line, rather than eight-line, \(2A_1\) type).

Define \(z_{r,s}\) to be the number of Zariski chambers in the big cone of \(X\) whose negative support contains exactly \(r\) irreducible curves, of which exactly \(s\) are \((-2)\)-curves. Then
\[
\begin{aligned}
\sum_{r,s} z_{r,s}t^r u^s={}&1+9t+26t^2+30t^3+13t^4+t^5\\
&+u(2t+18t^2+46t^3+38t^4+4t^5)\\
&+u^2(t^2+8t^3+16t^4+8t^5).
\end{aligned}
\]
In particular, there are exactly \(221\) Zariski chambers, with support-size polynomial
\[
1+11t+45t^2+84t^3+67t^4+13t^5.
\]
For the anticanonically truncated chamber volumes of Bauer--Schmitz, exactly \(80\) chambers have finite volume and \(141\) have infinite volume. Exactly \(33\) chambers have both \((-2)\)-curves in their negative support. The results are constant within the stated geometric incidence family.

## Assumptions and scope
Work over \(\mathbb C\). The blown-up points are distinct and no infinitely near blow-up is involved. There are precisely the two triple-point lines specified above. The definition of a Zariski chamber is the chamber decomposition of the big cone by the negative support of Zariski decompositions; the empty support is the nef chamber. For volumes, use the lattice-normalized Lebesgue measure on \(N^1(X)_{\mathbb R}\) truncated by \((-K_X)\cdot D\le 1\), as defined in Bauer--Schmitz. The statement concerns only the nine-line quartic \(2A_1\) type; the distinct eight-line quartic \(2A_1\) type is not covered.

## Proof
**Step 1: full negative-curve classification.** Let \(H\) be the pullback of a projective line and \(E_i\) the exceptional curves. The canonical class is \(K_X=-3H+\sum_{i=0}^4 E_i\), so \((-K_X)^2=4\). Let \(A=H-E_0-E_1-E_2\) and \(B=H-E_0-E_3-E_4\), the strict transforms of the two triple-point lines. Each has square \(-2\), anticanonical intersection zero, and \(A\cdot B=0\). All \(E_i\) have square \(-1\).

Suppose \(C\) is an irreducible curve other than an exceptional curve, \(A\), or \(B\). Writing \([C]=dH-\sum_i m_iE_i\) with \(d\ge1\) and \(m_i\ge0\), Bézout with the two distinct lines gives \(m_0+m_1+m_2\le d\) and \(m_0+m_3+m_4\le d\). Hence
\[
(-K_X)\cdot C=3d-\sum_{i=0}^4m_i\ge d+m_0\ge1.
\]
Thus \(-K_X\) is nef, and since its square is \(4\), it is big. By adjunction, \(2p_a(C)-2=C^2+K_X\cdot C\ge-2\). If \(C^2<0\), it follows that \((-K_X)\cdot C=1\) and \(C^2=-1\). The displayed Bézout bound now forces \(d=1\) and \(m_0=0\); the anticanonical equation forces \(\sum_i m_i=2\). An irreducible line through two of the four points \(p_1,p_2,p_3,p_4\) is not \(A\) or \(B\) precisely when it joins one point from \(\{p_1,p_2\}\) to one from \(\{p_3,p_4\}\). Therefore the remaining negative curves are exactly the four strict transforms \(K_{13},K_{14},K_{23},K_{24}\), with \(K_{ij}=H-E_i-E_j\). In total there are nine \((-1)\)-curves and two disjoint \((-2)\)-curves, and the anticanonical model contracts exactly \(A,B\).

**Step 2: negative-definite supports.** The known Zariski-chamber correspondence identifies the chambers with the empty support and the nonempty sets of negative curves having negative-definite intersection matrix. Any two distinct selected \((-1)\)-curves must have intersection zero: if their intersection is positive, their two-by-two principal matrix is not negative definite. Thus the selected \((-1)\)-curves form a pairwise disjoint set \(S\). The only intersections between a root and the \((-1)\)-curves are
\[
A\cdot E_i=1\quad(i=0,1,2),\qquad B\cdot E_i=1\quad(i=0,3,4);
\]
all other root-to-\((-1)\) intersections vanish. For selected roots \(R\subseteq\{A,B\}\), write \(M\) for the zero-one incidence matrix between \(R\) and \(S\). The support intersection matrix, ordered with \(S\) first, is
\[
\begin{pmatrix}-I&M^{\!T}\\M&-2I\end{pmatrix}.
\]
The Schur complement criterion says that it is negative definite exactly when \(2I-MM^{\!T}\) is positive definite. For just \(A\), this means at most one of \(E_0,E_1,E_2\) is selected; for just \(B\), at most one of \(E_0,E_3,E_4\) is selected. For both roots it means \(E_0\) is absent and at most one of \(E_1,E_2\) and at most one of \(E_3,E_4\) is selected: indeed \(\{E_0,A,B\}\) already has a singular intersection matrix, whereas without \(E_0\) the Schur complement is diagonal. These criteria are both necessary and sufficient.

**Step 3: exact generating functions.** Among the nine \((-1)\)-curves, \(E_0\) meets none of the others. The curves \(K_{13},K_{14},K_{23},K_{24}\) have an intersection of one exactly for the two opposite pairs \(\{K_{13},K_{24}\}\) and \(\{K_{14},K_{23}\}\). Further, \(K_{ij}\) meets \(E_i,E_j\) and no other exceptional curve. Choose a subset \(Q\) of the four crossing-line curves avoiding both opposite pairs. Choose any subset \(T\) of the exceptional curves \(E_1,\ldots,E_4\) whose indices do not occur in \(Q\), and independently decide whether \(E_0\) is present. Give each selected \((-1)\)-curve weight \(t\), then apply the root restrictions from Step 2, giving an additional factor \(tu\) for each selected root. This finite sum over \(Q,T\), and the \(E_0\)-choice gives the three coefficient polynomials:
\[
\begin{aligned}
F_0(t)&=1+9t+26t^2+30t^3+13t^4+t^5,\\
F_1(t)&=2t+18t^2+46t^3+38t^4+4t^5,\\
F_2(t)&=t^2+8t^3+16t^4+8t^5.
\end{aligned}
\]
Here \(F_s(t)\) counts supports with exactly \(s\) selected roots. Equivalently, the computable combinatorial sum is: sum \(t^{|Q|+|T|+e+|R|}u^{|R|}\) over admissible \(Q\), \(T\) as above, \(e\in\{0,1\}\), and \(R\subseteq\{A,B\}\), with \(e+|T\cap\{1,2\}|\le1\) when \(A\in R\), \(e+|T\cap\{3,4\}|\le1\) when \(B\in R\), and \(e=0\) when \(R=\{A,B\}\). This description also gives a short self-contained reconstruction of each coefficient, rather than relying on a numerical eigenvalue calculation.

Setting \(t=u=1\) gives \(221\). Setting \(u=0,t=1\) gives \(80\). Supports with at least one root number \(221-80=141\), and supports with both roots number \(F_2(1)=33\). The maximum support size is five.

**Step 4: finite versus infinite truncated volume.** Bauer--Schmitz's chamber-volume criterion says that any chamber whose negative support contains a curve of self-intersection below \(-1\) has infinite truncated volume. Conversely, a support consisting of disjoint \((-1)\)-curves has finite volume when the nef-cone slice of the simultaneous blow-down is bounded. The blow-down remains anticanonically big (its anticanonical square increases from \(4\)) and has finitely generated effective cone, so its nef-cone slice is bounded. Therefore the finite-volume chambers are exactly the \(80\) root-free chambers, leaving \(141\) of infinite volume.

## Verification
Run `python3 verify_chambers.py` from the directory containing the two files. The script uses only the Python standard library. It reconstructs the eleven curve classes and their exact integral intersection matrix, tests all \(2^{11}=2048\) possible supports by Sylvester's criterion with exact rational determinants, and independently implements the crossing-line/exceptional-curve combinatorial sum with root restrictions. Both methods return the same bivariate support distribution. The recorded output in `verify_output.txt` ends with `ALL_CHECKS_PASSED`. The symbolic Bézout/adjunction argument is needed to establish that the tested curve list is exhaustive; a finite subset test alone would not prove this geometric fact.

## Relationship to prior work
Bauer--Funke--Neumann, arXiv:0912.0958 (first public version 2009-12-04), established the negative-definite-support method and reported \(393\) Zariski chambers for the smooth quartic del Pezzo surface (five points in general position). That general theorem underlies Step 2, and its smooth number is not claimed here. Bauer--Schmitz, arXiv:1205.3817 (2012-05-16), established the chamber-volume finiteness criterion used in Step 4. Derenthal, arXiv:math/0604194 (first public version 2006-04-10), Table 6, distinguishes the quartic \(2A_1\) types with nine and eight geometric lines, but computes Cox rings and does not tabulate their Zariski-chamber root-support polynomials. The new calculation here is restricted to the nine-line type, obtained by the two specified ordinary triple collinearities.

## Limitations
The classification is over \(\mathbb C\), for ordinary blow-ups in the stated incidence class only. It does not determine the chamber polynomial for the distinct eight-line \(2A_1\) model or other singularity types. Counts are exact conditional on the established Zariski-chamber correspondence; they do not give the individual finite chamber volumes. No claim of an exhaustive historical-priority proof is made: unlocated specialized chamber tables, including inaccessible older thesis material, remain a possible overlap risk.

## References
1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (2009), https://arxiv.org/abs/0912.0958.
2. T. Bauer, D. Schmitz, *Volumes of Zariski chambers*, arXiv:1205.3817 (2012), https://arxiv.org/abs/1205.3817.
3. U. Derenthal, *Singular del Pezzo surfaces whose universal torsors are hypersurfaces*, arXiv:math/0604194 (2006 initial preprint; revised 2013), https://arxiv.org/abs/math/0604194.
4. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (2012), https://arxiv.org/abs/1204.4373.
