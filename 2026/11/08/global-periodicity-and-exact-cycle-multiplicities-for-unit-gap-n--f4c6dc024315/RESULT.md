# Global periodicity and exact cycle multiplicities for unit-gap nonlinear lattice rotations

## Finding

For each integer \(b\ge 1\), consider the integer-lattice map
\[
\Phi_b(x,y)=\bigl(x+(2b+1)(y-s(x))+b,\ y-s(x)\bigr),\qquad
s(x)=\begin{cases}1,&x\ge0,\\-1,&x<0.\end{cases}
\]
**Every point** of \(\mathbb Z^2\) lies on a periodic orbit. Its complete least-period spectrum is
\[
\{4(2b+1)m:m\in\mathbb Z_{\ge1}\},
\]
and **exactly \(m\) distinct cycles** have least period \(4(2b+1)m\). Each such cycle meets the positive horizontal ray \(S=\{(x,0):x\in\mathbb Z_{\ge0}\}\) in exactly \(2b+1\) points. The primitive period of the first-return map to \(S\) is exactly \(2b+1\) at every point.

## Assumptions and scope

The domain is the entire integer lattice, with no boundedness restriction. The sign at \(x=0\) is \(+1\). The parameter \(b\) is an integer at least one; put \(a=2b+1\). The inverse exists because \(x'=x+ay'+b\) determines \(x=x'-ay'-b\), then \(y=y'+s(x)\). Consequently, all primitive cycles counted below are distinct orbits of a bijection.

For each integer \(m\ge1\), define
\[
A_m=\frac{(m-1)(a(m-1)+1)}2,\quad
O_m=\{A_m,\ldots,A_m+m-1\},\quad
E_m=\{A_m+m,\ldots,A_{m+1}-1\}.
\]
Here \(A_1=0\), \(A_{m+1}-A_m=am-b\), and \(|E_m|=b(2m-1)\). These sets partition the ray coordinates \(\mathbb Z_{\ge0}\) into successive, disjoint finite blocks.

## Proof

**Lemma 1 (all points meet the ray).** Suppose a forward orbit stayed in \(x\ge0\) forever. Then every iterate subtracts one from \(y\), so \(y\to-\infty\) linearly and the increments \(ay'+b\) force \(x\to-\infty\) quadratically, a contradiction. Likewise, an orbit staying in \(x<0\) has \(y\to+\infty\), forcing \(x\to+\infty\). Thus some transition from \(x<0\) to \(x\ge0\) occurs. At that transition the new vertical coordinate must be nonnegative: if \(y'\le-1\), then \(x'=x+ay'+b\le-1-a+b<0\). From \(y'\ge0\), as long as the orbit is in \(x\ge0\), successive increments of \(x\) until \(y=0\) are \(ay''+b\ge b>0\). Hence it reaches \(S\) without leaving the positive half-plane. This applies to every forward orbit.

**Lemma 2 (exact first-return map and return times).** For \(x=A_m+u\), where \(0\le u<am-b\), direct iteration of the two affine branches gives the first-return coordinate \(R(x)\) and the number \(\ell(x)\) of steps as
\[
(R(x),\ell(x))=\begin{cases}
(x+4bm,\ 4m),&0\le u<m,\\
(x-(2m-1),\ 4m-2),&m\le u<am-b.
\end{cases}
\]
To verify the **first** return, for the initial \(m\) positive-half-plane steps the position is
\[
y_j=-j,\qquad x_j=x+bj-\frac{aj(j+1)}2,\quad 0\le j\le m.
\]
The endpoints \(x_0\ge0\), \(x_{m-1}=u\ge0\), and concavity imply \(x_j\ge0\) for \(0\le j<m\); then \(x_m=u+b-am\le-1\). Under the negative branch \(y\) increases by one per step, while \(x\) is a convex quadratic in the negative-branch step count. In particular
\[
x_{3m-2}=u-m-a(m-1)-b<0,\qquad x_{3m-1}=u-m.
\]
Both endpoints of the negative-branch segment until time \(3m-2\) are negative, so convexity proves all its intervening positions are negative. For \(u\ge m\), time \(3m-1\) is the first nonnegative return of \(x\), with \(y=m-1\); it takes a further \(m-1\) steps in the nonnegative half-plane to reach \(y=0\), giving \(4m-2\). For \(u<m\), time \(3m-1\) is still negative, and at time \(3m\), \(x_{3m}=u-m+am+b>0\) and \(y=m\); a further \(m\) steps give \(4m\). All these final increments are positive, so the indicated return is the first. Summing \(\Delta x=ay'+b\) over the three phases yields precisely the two stated coordinate shifts. The edge case \(m=1\) follows from the same formulas, interpreting empty intermediate ranges as empty.

**Lemma 3 (exact return cycles).** For each \(m\ge1\) and \(t\in\{0,\ldots,m-1\}\), start at \(x=A_m+t\in O_m\). Its first \(b\) return-map iterates are
\[
R^i(x)=A_{m+1}+(m+1)+(b-i)(2m+1)+t,\qquad1\le i\le b,
\]
all belonging to \(E_{m+1}\). Its next \(b\) iterates are
\[
R^{b+j}(x)=A_m+m+(b-j)(2m-1)+(m-1)+t,\qquad1\le j\le b,
\]
all belonging to \(E_m\). The next iterate returns to \(A_m+t\). Every displayed point except the starting point is even-type, so the least return period is exactly \(2b+1\).

These orbits exhaust the return map. Indeed, partition each \(E_m\) into \(b\) adjacent blocks of length \(2m-1\), with relative block coordinate \(v\in\{0,\ldots,2m-2\}\). The segment \(0\le v\le m-2\) of each block (empty at \(m=1\)) occurs among the first \(b\) images of representatives from \(O_{m-1}\), and the complementary segment \(m-1\le v\le2m-2\) occurs among the last \(b\) images from \(O_m\). The formulas above give these identifications exactly; they are disjoint and cover every integer. Thus every point in \(S\) lies on one and only one of the listed return cycles.

**Lemma 4 (least plane periods).** Along the return cycle emanating from \(O_m\), the return-flight times are \(4m\) once, \(4m+2\) exactly \(b\) times (the points in \(E_{m+1}\)), and \(4m-2\) exactly \(b\) times (the points in \(E_m\)). Their sum is
\[
4m+b(4m+2)+b(4m-2)=4m(2b+1).
\]
A shorter plane period would induce a shorter first-return period at the starting point on \(S\), which Lemma 3 excludes. Conversely, Lemma 1 guarantees every plane point eventually meets \(S\); the map is bijective and all points of \(S\) are periodic, so the original point lies on the same finite periodic orbit. Since \(O_m\) has exactly \(m\) points, and each return orbit contains exactly one such point, there are exactly \(m\) plane cycles of period \(4m(2b+1)\). This proves the theorem. \(\square\)

## Verification

The standalone pure-integer program `CHECK.py` reconstructs the full first return by direct iteration of \(\Phi_b\), compares it with Lemma 2, checks return-map orbit distinctness, checks the sum of exact return times, and verifies primitive plane periods directly on selected layers. It checks \(b\in\{1,2,3,4,5,6,10,17\}\), all layers \(1\le m\le19\), every ray coordinate in each tested layer, and direct primitive periods for \(1\le m\le5\). The program reports `EXACT_INTEGER_RETURN_AND_CYCLE_CHECK_OK 22160`. The infinite statements are proved in the preceding lemmas and are not inferred from these finite checks.

## Relationship to prior work

Alwani and Vivaldi introduced this same two-parameter lattice family, constructed an infinite interval-exchange first-return map, and established periodicity on a set of full density when the reduced parameter is odd. They explicitly formulated the **all-orbits periodicity statement as a conjecture**, rather than a theorem, and gave a general first-return interval formula consistent with Lemma 2. Here the unit-gap relation \(a-2b=1\) yields an explicit exact return-cycle decomposition and an exact plane-period multiplicity law, strengthening density-one periodicity to every lattice point in this one-parameter family. The present statement is a special-parameter solution, not a claim about the general two-parameter conjecture.

## Limitations

Only integer \(b\ge1\) with \(a=2b+1\) are classified. There is no assertion for other parameter pairs, perturbations, or continuous extensions. The source proves a full-density theorem, not the present global classification; nevertheless, an equivalent unpublished or unindexed specialization could affect priority. The computation is a reproducibility check, not a substitute for the proof or an independent audit.

## References

- F. Alwani and F. Vivaldi, *Nonlinear Rotations on a Lattice*, arXiv:1709.08904 (first posted September 26, 2017), later *Journal of Difference Equations and Applications* 24 (2018), DOI: 10.1080/10236198.2018.1459592.
