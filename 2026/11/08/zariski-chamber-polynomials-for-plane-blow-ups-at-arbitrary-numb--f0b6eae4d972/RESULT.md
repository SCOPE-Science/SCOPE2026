# Zariski-chamber polynomials for plane blow-ups at points on a smooth conic

## Finding

Let \(n\ge 7\) be an integer, and let \(X_n\) be the blow-up of \(\mathbb P^2_{\mathbb C}\) at **any** \(n\) distinct points lying on a single smooth conic. The result determines the number of Zariski chambers of the big cone, refined by the size of the negative support and by whether that support contains the strict transform \(Q\) of the conic.

For \(m\ge 1\), put
\[
T_m(t)=1+m\big((1+t)^{m-1}-1\big)-\binom{m}{2}t+\binom{m}{3}t^3,
\qquad T_0(t)=1.
\]
Define
\[
\boxed{F_n(t)=\sum_{m=0}^{n}\binom nm t^{n-m}T_m(t)},
\qquad
\boxed{G_n(t)=t\sum_{m=5}^{n}\binom nm t^{n-m}T_m(t)}.
\]
Then \(F_n(t)\) enumerates **all chambers not containing \(Q\)**, and \(G_n(t)\) enumerates **all chambers containing \(Q\)**, with the coefficient of \(t^r\) counting supports with exactly \(r\) irreducible negative curves. The nef chamber is the constant term of \(F_n\).

Under the anticanonically truncated chamber-volume convention of Bauer--Schmitz, **every one of the \(F_n(1)\) chambers has finite volume, and every one of the \(G_n(1)\) chambers has infinite volume**. In particular,
\[
\boxed{F_n(1)=2^n+n3^{n-1}-n2^{n-1}-\binom n2 2^{n-2}+\binom n3 2^{n-3}},
\]
\[
\boxed{F_n(1)+G_n(1)=2F_n(1)-\left(1+n+2\binom n2+8\binom n3+27\binom n4\right)}.
\]
The first three new cases are:

| Blown-up points | Finite-volume chambers | Infinite-volume chambers | Total chambers |
| ---: | ---: | ---: | ---: |
| \(7\) | \(4671\) | \(3396\) | \(8067\) |
| \(8\) | \(16728\) | \(14325\) | \(31053\) |
| \(9\) | \(58025\) | \(53869\) | \(111894\) |

Every negative support has at most \(n\) components. In particular **finite chamber counts persist for arbitrarily large \(n\)**, even though blowing up nine or more very general points is known to produce infinitely many negative curves and Zariski chambers.

## Assumptions and scope

All surfaces are smooth complex projective surfaces. The centers of blowing up are \(n\ge7\) **distinct ordinary points**, with no infinitely near centers, all on one smooth irreducible conic. No general-position requirement along the conic is imposed. Set \(H=\pi^*\mathcal O_{\mathbb P^2}(1)\), write \(E_i\) for the exceptional curves, \(L_{ij}=H-E_i-E_j\) for the strict transforms of the secant lines through two centers, and \(Q=2H-\sum_i E_i\) for the strict transform of the conic.

A Zariski chamber is counted by the support of the negative part of the Zariski decomposition of a big real divisor. The chamber of empty support is included. Chamber volume means the Lebesgue volume after truncation by \((-K_{X_n})\cdot D\le1\), with the Picard-lattice covolume normalization described in Bauer--Schmitz; only the finite/infinite dichotomy is asserted here, not numerical volumes.

## Proof

**1. There are no hidden negative curves.** Each \(E_i\) and each \(L_{ij}\) is a \((-1)\)-curve, and \(Q^2=4-n<0\). The secant line through two distinct points of a smooth conic contains no third chosen center, by Bézout. Suppose an irreducible negative curve \(D\) is neither exceptional nor \(Q\), and let \(\overline D\) be its plane image of degree \(d\ge1\), with multiplicities \(m_i\) at the centers. Since \(\overline D\ne Q\), Bézout with the smooth conic gives
\[
\sum_i m_i\le 2d.
\]
The arithmetic genus of the irreducible strict transform is nonnegative, so
\[
\sum_i m_i(m_i-1)\le(d-1)(d-2).
\]
Consequently
\[
D^2=d^2-\sum_i m_i^2
\ge d^2-(d-1)(d-2)-2d=d-2.
\]
If \(d\ge2\), this is nonnegative, contrary to the assumed negativity. If \(d=1\), the line meets the conic in at most two centers and is negative precisely when it is one of the \(L_{ij}\). Therefore the **complete** set of negative curves is
\[
\{E_i:1\le i\le n\}\;\cup\;\{L_{ij}:1\le i<j\le n\}\;\cup\;\{Q\}.
\]
This argument needs only Bézout and the arithmetic-genus formula; no classification of higher-degree exceptional curves is assumed.

**2. Determine negative-definite supports.** Distinct \((-1)\)-curves in a negative-definite support cannot meet: any pair with positive integral intersection has a non-negative determinant in the corresponding \(2\times2\) principal submatrix. The relevant intersections are
\[
E_i\cdot L_{jk}={\bf1}_{i\in\{j,k\}},\qquad
L_{ij}\cdot L_{kl}=1-|\{i,j\}\cap\{k,l\}|\quad((i,j)\ne(k,l)),
\]
\[
Q\cdot L_{ij}=0,\qquad Q\cdot E_i=1,\qquad Q^2=-(n-4).
\]
Choose a set \(I\subseteq\{1,\ldots,n\}\) of \(r\) exceptional curves. Any selected secant lines must have both endpoints outside \(I\), and their corresponding pairs of endpoints must intersect pairwise. If \(Q\) is absent, this condition is necessary and sufficient: the intersection matrix is then diagonal with all entries \(-1\).

If \(Q\) is present, the only non-diagonal block is the block on \(Q\) and the \(r\) chosen exceptional curves,
\[
\begin{pmatrix}-(n-4)&\mathbf1^T\\ \mathbf1&-I_r\end{pmatrix}.
\]
Its Schur complement against \(-I_r\) is \(-(n-4)+r\). Thus the support is negative definite **if and only if** \(r<n-4\), equivalently at least five labels remain for the secant-line choices. All line blocks are diagonal and orthogonal to this block. By Bauer--Funke--Neumann's chamber/support correspondence, every one of these supports occurs as the support of a big divisor's negative part, and no other supports occur.

**3. Count intersecting secant-edge families.** On \(m\) remaining labels, a pairwise-intersecting family of unordered pairs is either a star (all pairs share one fixed vertex) or, in the exceptional three-edge case, a triangle. To see this, choose two edges sharing one vertex. If any third edge avoids that vertex, it must join their other endpoints, making a triangle and forbidding a fourth distinct edge. The empty family contributes one. Summing all nonempty stars gives \(m((1+t)^{m-1}-1)\), but each singleton edge is counted twice, so subtract \(\binom m2t\); add the \(\binom m3\) triangles in degree three. This proves the displayed formula for \(T_m(t)\), including its special definition for \(m=0\).

There are \(\binom nm\) ways to leave exactly \(m\) labels for the line family, and the other \(n-m\) labels contribute exceptional curves and hence the factor \(t^{n-m}\). With \(Q\) present there is an additional \(t\), and the Schur-complement condition forces \(m\ge5\). This proves both \(F_n(t)\) and \(G_n(t)\).

**4. Evaluate and classify chamber volumes.** Setting \(t=1\) and using binomial convolution yields
\[
F_n(1)=2^n+n3^{n-1}-n2^{n-1}-\binom n2 2^{n-2}+\binom n3 2^{n-3}.
\]
Since \(T_0(1),\ldots,T_4(1)\) are \(1,1,2,8,27\), the total formula follows immediately. Finally, \(-K_{X_n}=3H-\sum_iE_i=H+Q\) is big because \(H\) is big and \(Q\) is effective. The volume theorem of Bauer--Schmitz identifies chambers containing any curve of self-intersection less than \(-1\) as infinite-volume and gives finite volume for those supported entirely on disjoint \((-1)\)-curves when \(-K\) is big. Here \(Q\) is the unique curve with self-intersection at most \(-2\). Hence precisely the \(G_n(1)\) chambers have infinite volume.

## Verification

The standalone, standard-library-only script `verify/conic_verify.py` provides independent finite checks of the combinatorial formula. Its backtracking generates intersecting edge families by testing edge compatibility, rather than using the star/triangle count. It then enumerates exceptional-curve choices independently and compares the resulting support-size polynomials with the closed expressions. For \(n=7\) it also reconstructs actual geometric intersection matrices and tests the relevant definiteness claims by exact rational \(LDL^T\) elimination. It checks the closed total-count formula through \(n=19\).

Running `python3 verify/conic_verify.py` produces the attached `verify/output.txt`, ending in `ALL_CHECKS_PASSED`. The finite tests are corroboration; the proof for **all** \(n\ge7\) rests on the explicit negative-curve and combinatorial arguments above.

## Relationship to prior work

Bauer, Funke and Neumann (2009, arXiv:0912.0958), Proposition 1.1, established the negative-definite-support correspondence used here. Their tabulation addresses del Pezzo surfaces blown up at at most eight points in general position; it does not give the two conic-support polynomials for arbitrarily large \(n\). The known six-point-on-conic cubic-resolution calculation lies outside this claim's \(n\ge7\) range and does not imply its uniform closed forms.

Bauer and Schmitz (2012, arXiv:1205.3817) proved the general finite/infinite-volume criterion and studied blow-ups whose centers lie on a **line**, as well as infinitely near points; the volume criterion is not asserted as new. The new finite/infinite counts depend on the independently established conic-support classification. Rams and Szemberg (2014, arXiv:1411.4178) analyzed when Zariski chambers agree with numerical Weyl chambers; their criterion neither enumerates the present supports nor gives the closed count.

Bauer and Schmitz (2012, arXiv:1204.4373) developed a faster principal-submatrix enumeration algorithm, with application to the Segre--Schur quartic and general-position del Pezzo tables; it does not give the present unbounded conic family’s closed formulas.

The distinctive outcome is a **closed formula for every \(n\ge7\)** and a complete volume dichotomy in this geometric family. This includes arbitrary \(n\ge9\), in marked contrast to blow-ups at very general centers, for which the chamber count is infinite.

## Limitations

Only distinct points on one smooth conic over \(\mathbb C\) are treated. The result concerns the chamber-support polynomial and whether volumes are finite; it does not compute the numerical volume of individual finite chambers or the entire stable-base-locus fan. Historical priority against specialized tables, theses, or equivalent unpublished formulas remains to be assessed independently. All code checks are finite, and no independent scientific audit has been performed.

## References

1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958, first publicly submitted 2009-12-04. https://arxiv.org/abs/0912.0958
2. T. Bauer, D. Schmitz, *Volumes of Zariski chambers*, arXiv:1205.3817, first publicly submitted 2012-05-16. https://arxiv.org/abs/1205.3817
3. S. Rams, T. Szemberg, *When are Zariski chambers numerically determined?*, arXiv:1411.4178, first publicly submitted 2014-11-15. https://arxiv.org/abs/1411.4178
4. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, first publicly submitted 2012-04-19. https://arxiv.org/abs/1204.4373
