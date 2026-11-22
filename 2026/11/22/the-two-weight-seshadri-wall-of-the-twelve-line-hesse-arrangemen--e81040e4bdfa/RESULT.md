# The two-weight Seshadri wall of the twelve-line Hesse arrangement

## Finding
Let \(\mathcal H\) be the classical twelve-line Hesse arrangement over \(\mathbb C\), with nine ordinary quadruple points \(Q\) and twelve ordinary double points \(N\). Give every point of \(Q\) a real weight \(\alpha>0\) and every point of \(N\) a real weight \(\beta>0\). The weighted multipoint Seshadri constant of \(\mathcal O_{\mathbb P^2}(1)\) is exactly
\[
\boxed{\varepsilon(\alpha,\beta)=\frac1{\max\{3\alpha+2\beta,\,4\beta\}}.}
\]
For \(\beta<3\alpha/2\), precisely the twelve original Hesse lines compute the constant; for \(\beta>3\alpha/2\), precisely nine distinct **non-arrangement** lines, each containing four nodes, compute it. At \(\beta=3\alpha/2\), both line families compute the constant; no assertion that they exhaust the minimizers on the wall is made.

The Seshadri ray is volume-saturating for exactly this weight ratio. On the blow-up of all twenty-one marked points, the primitive integral class
\[
F=12H-2\sum_{q\in Q}E_q-3\sum_{p\in N}E_p
\]
is nef, satisfies \(F^2=0\), and is orthogonal to the twenty-one line strict transforms: twelve with self-intersection \(-4\) and nine with self-intersection \(-3\).

## Assumptions and scope
Work throughout over \(\mathbb C\), and fix a primitive cube root of unity \(\omega\). Set
\[
\mathcal H=V\left(xyz\prod_{i,j=0}^2(x+\omega^iy+\omega^jz)\right)\subset\mathbb P^2.
\]
The sets of marked points are
\[
Q=\{(0:1:-\gamma),(1:0:-\gamma),(1:-\gamma:0):\gamma^3=1\},
\]
\[
N=\{(1:0:0),(0:1:0),(0:0:1)\}\cup
\{(1:a:b):a^3=b^3=1\}.
\]
For every reduced irreducible plane curve \(C\) meeting \(Q\cup N\), put
\[
A(C)=\sum_{q\in Q}\operatorname{mult}_q(C),\quad
B(C)=\sum_{p\in N}\operatorname{mult}_p(C),\quad
\rho_{\alpha,\beta}(C)=\frac{\deg C}{\alpha A(C)+\beta B(C)}.
\]
The weighted constant is the infimum of \(\rho_{\alpha,\beta}(C)\) over these curves. A point not on \(C\) contributes multiplicity zero. Only positive real weights and the fixed twenty-one-point support are asserted; there is no statement about arbitrary nonuniform weights, different arrangements, or characteristic three.

Let \(\mathcal G\) consist of the nine lines
\[
x-\omega^iy=0,\qquad x-\omega^iz=0,\qquad y-\omega^iz=0\qquad (i=0,1,2).
\]
They are different from all components of \(\mathcal H\). Each original line has exactly three points of \(Q\) and two points of \(N\). Every line of \(\mathcal G\) has exactly four points of \(N\) and no points of \(Q\). Each node is on exactly three lines of \(\mathcal G\), and each quadruple point is on exactly four lines of \(\mathcal H\).

## Proof
**Incidence.** In the displayed coordinates, a quadruple point on a coordinate axis is also on precisely three factors \(x+\omega^iy+\omega^jz\), and a point \((1:a:b)\) with \(a^3=b^3=1\) is on exactly two such factors, since the three summands must be the three different cube roots of unity. The three coordinate vertices lie on two coordinate axes each. This gives the incidence counts for \(\mathcal H\). Every node \((1:a:b)\) lies on one line in each of the three families defining \(\mathcal G\); each vertex lies on the three lines of one family. No quadruple point lies on a line of \(\mathcal G\), because its two nonzero coordinates have ratio \(-\gamma\), not a cube root of unity. The twenty-one points and the complete singular support of \(\mathcal H\) are also established in [1, §4.1].

**Bézout bounds.** Let \(C\) be any irreducible curve of degree \(d\) different from every line in \(\mathcal H\cup\mathcal G\). At a marked point on a line, local intersection multiplicity is at least the multiplicity of \(C\). Summing Bézout over the twelve original lines and then the nine additional lines yields
\[
12d\ge 4A(C)+2B(C),\qquad 9d\ge 3B(C).
\]
Thus \(A(C)\le3d-B(C)/2\) and \(0\le B(C)\le3d\). If \(\beta\le\alpha/2\), then
\[
\alpha A(C)+\beta B(C)\le3\alpha d <(3\alpha+2\beta)d.
\]
If \(\alpha/2\le\beta\le3\alpha/2\), then
\[
\alpha A(C)+\beta B(C)
\le(3\alpha/2+3\beta)d\le(3\alpha+2\beta)d.
\]
If \(\beta\ge3\alpha/2\), the same intermediate bound is at most \(4\beta d\). All these bounds are strict compared with the active maximum whenever \(\beta\ne3\alpha/2\), since in the second range \(3\alpha/2+3\beta<3\alpha+2\beta\) for \(\beta<3\alpha/2\), and in the third range \(3\alpha/2+3\beta<4\beta\) for \(\beta>3\alpha/2\).

**Sharpness and minimizers.** An original Hesse line has weighted multiplicity sum \(3\alpha+2\beta\), whereas a line in \(\mathcal G\) has sum \(4\beta\). These give both upper bounds and attain the larger reciprocal denominator. Together with the strict off-family bounds just proved, this establishes the formula and the claimed complete minimizing-line classification away from the wall. On the wall both families attain equality, but the proof does not rule out unrelated irreducible minimizers.

**Unique volume-saturating ray.** Let \(X\to\mathbb P^2\) be the blow-up of \(Q\cup N\) and let \(H\) denote the pullback of a line. By the curve characterization of Seshadri constants, the class
\[
H-\varepsilon(\alpha,\beta)\left(\alpha\sum_Q E_q+\beta\sum_N E_p\right)
\]
is nef. Its square is
\[
1-\frac{9\alpha^2+12\beta^2}{\max\{3\alpha+2\beta,4\beta\}^2}.
\]
In the first chamber the numerator of the difference of squares is \(4\beta(3\alpha-2\beta)\), and in the second chamber it is \(4\beta^2-9\alpha^2\); both are nonnegative and vanish precisely when \(\beta=3\alpha/2\). At this unique wall the displayed nef class is \(F/12\). Direct intersection calculations give \(F^2=144-9\cdot4-12\cdot9=0\), \(F\cdot\widetilde L=12-2\cdot3-3\cdot2=0\) for each \(L\in\mathcal H\), and \(F\cdot\widetilde G=12-3\cdot4=0\) for each \(G\in\mathcal G\). Their self-intersections are \(1-5=-4\) and \(1-4=-3\), respectively. The integral coefficients of \(F\) have greatest common divisor one, so \(F\) is primitive. \(\square\)

## Verification
The accompanying dependency-free Python 3 program `check_hesse_weighted.py` performs arithmetic exactly in \(\mathbb Z[\omega]/(\omega^2+\omega+1)\). It checks the stated twenty-one points are distinct, every pair of original lines intersects at one of them, all twelve original-line and nine extra-line incidences, and a set of exact rational checks on the two-dimensional Bézout polytope and volume inequality. Execute `python3 check_hesse_weighted.py`; the program exits unsuccessfully if any assertion fails. The proof above establishes the inequalities for all positive real weights and all irreducible curves; finite numerical tests are supplemental and not substituted for the infinite argument.

## Relationship to prior work
Dumnicki–Farnik–Hanumanthu–Harbourne–Pokora–Roé–Tutaj-Gasińska [1, Theorem 1.2 and §4.1] prove the **equal-weight** value \(1/5\) for this twelve-line arrangement and explicitly list its nine quadruple and twelve double points. The present formula specializes to \(1/5\) when \(\alpha=\beta=1\), but its chamber switch to nine non-arrangement four-node lines, strict minimizing-family classification, and unique isotropic nef ray are extra statements not contained in that scalar assertion. Janasz–Pokora [2, Example 3.5] study a **distinct arrangement of twelve conics**, using lines from the dual Hesse arrangement and a twenty-one-point support; their set of nine higher-multiplicity points differs from \(Q\), and their equal-weight result does not determine the formula here. Pokora [3, §3] treats ordinary unweighted special point arrangements and general Bézout techniques; no orbit-weighted Hesse formula is given. These mathematical distinctions do not establish absolute priority; possible specialized nef-cone calculations outside the inspected literature remain a residual risk.

## Limitations
The theorem does not describe every irreducible minimizer at the exact wall, assert effectivity or semiampleness of \(F\), classify the full nef cone, or treat fields of positive characteristic. Exact incidence checking and literature searching cannot establish novelty in unindexed publications.

## References
1. M. Dumnicki, Ł. Farnik, K. Hanumanthu, B. Harbourne, P. Pokora, J. Roé, H. Tutaj-Gasińska, *Seshadri constants of singular loci of line arrangements with at most twelve lines*, arXiv:2611.03797v1 (first public 2026-11-02), https://arxiv.org/pdf/2611.03797.
2. M. Janasz and P. Pokora, *On Seshadri constants and point-curve configurations*, arXiv:2004.04043v1 (2020), https://arxiv.org/pdf/2004.04043.
3. P. Pokora, *Seshadri constants and special configurations of points in the projective plane*, arXiv:1711.09364 (first public 2017), https://arxiv.org/pdf/1711.09364.
