# A sharp height-24 screen for the eight-dimensional spherical view-obstruction constant

## Finding

For a positive integer vector \(v=(v_1,\ldots,v_8)\), define its squared spherical view-obstruction distance by
\[
d_8(v)=\min_{t\in\mathbb R}\sum_{i=1}^8
\operatorname{dist}(t v_i-\tfrac12,\mathbb Z)^2.
\]
The exact bounded-height maximum is
\[
\boxed{\max_{v\in\{1,\ldots,24\}^8}d_8(v)=\frac8{17}.}
\]
Equality holds **if and only if** \(v\) is a coordinate permutation of
\[
(1,2,3,4,5,7,9,11)
\quad\text{or}\quad
(2,4,6,8,10,14,18,22).
\]
In particular, among primitive positive integer directions in this box, the first vector gives the unique maximizing permutation orbit. For the unrestricted constant \(\Delta_8=\sup_{v\in\mathbb Z_{>0}^8}d_8(v)\), this gives the rigorous lower bound
\[
\boxed{\Delta_8\ge\frac8{17}.}
\]
No assertion is made that this is the unrestricted maximum.

## Assumptions and scope

The metric is Euclidean squared distance to the half-integer lattice, with the same normalization as Kahlon's arXiv:2610.37711. Every coordinate is a positive integer between \(1\) and \(24\), inclusive; repeated coordinates and nonprimitive vectors are included in the finite optimization. All real parameters \(t\) are allowed. The count is over sorted vectors only after exploiting coordinate-permutation invariance. The cap \(24\) is the same speed cap used in the direct six-dimensional validation described in Section 6.4 of the motivating paper, now applied to the first unclassified dimension, eight.

## Proof

**Exact cell formula.** The squared distance is periodic with period \(1\), and symmetric under \(t\mapsto1-t\). It suffices to consider \(0\le t\le\tfrac12\). Divide this interval at all rational breakpoints \(k/v_i\) within it. On an open cell, set \(u_i=\lfloor tv_i\rfloor\), constant throughout the cell, and write
\[
Q=\sum_i v_i^2,\quad B=\sum_i v_i(2u_i+1),\quad C=\sum_i(2u_i+1)^2.
\]
The squared distance on that cell is the quadratic
\[
Q t^2-Bt+\frac C4.
\]
Its unrestricted real minimum is \((QC-B^2)/(4Q)\). The minimum of these values over the finitely many cells is **exactly** \(d_8(v)\), even if the minimizing point of a particular quadratic lies outside its cell. Indeed, each quadratic is the distance to one fixed half-integral lattice centre, hence is everywhere at least the distance to the nearest centre; its global minimum cannot be smaller than \(d_8(v)\). Conversely, at a global minimizing parameter, one adjacent cell's chosen centre is a nearest centre, so the minimum of that cell's quadratic is at most \(d_8(v)\). Both inequalities give equality. This also handles breakpoint minima without using floating-point tolerances.

**The explicit lower-bound direction.** For \(v_*=(1,2,3,4,5,7,9,11)\), one has \(Q=306\). In increasing order of its sixteen open cells within \([0,\tfrac12]\), the integer numerators \(QC-B^2\) are exactly
\[
684,800,620,576,764,752,716,764,848,620,716,608,684,944,1052,576.
\]
Their minimum is \(576\), so \(d_8(v_*)=576/(4\cdot306)=8/17\). The minimizing parameters in \([0,\tfrac12]\) are \(t=8/51\) and \(t=25/51\). For every positive integer \(h\), substituting \(t\mapsto ht\) proves \(d_8(hv)=d_8(v)\); the doubled direction therefore also attains \(8/17\).

**Exhaustiveness and uniqueness within the box.** By permutation invariance, each vector in \(\{1,\ldots,24\}^8\) is represented by exactly one nondecreasing eight-tuple. There are exactly
\[
\binom{24+8-1}{8}=\binom{31}{8}=7{,}888{,}725
\]
such tuples, including all repetitions and all nonprimitive cases. The standalone file `verify_view8.cpp` enumerates each of these tuples once, calculates every cell minimum using integers, compares rational scores by cross multiplication, and records **all** maximizers. Its exact output is two sorted tuples, \(v_*\) and \(2v_*\), and maximum \(8/17\). No vector is omitted, since the recursion chooses each subsequent coordinate from the preceding coordinate through \(24\). Event times are ordered and grouped by integer cross products. At an event \(t=k/v_i\), the updates are \(B\leftarrow B+2v_i\) and \(C\leftarrow C+8k\). All score calculations use signed 64-bit integers, and all rational comparisons use signed 128-bit integer cross products. The largest input coordinate is \(24\), so \(Q\le4608\) and \(0\le B,C\le Q\) on the scanned half-period; these quantities and their products are far below the relevant integer limits. The code plus the exact cell formula constitute a finite exhaustive proof of the displayed height-24 maximum and its complete equality set.

## Verification

From the self-contained source files supplied alongside this result, execute:

```sh
c++ -O2 -std=c++17 verify_view8.cpp -o verify_view8
./verify_view8 24
python3 verify_view8_independent.py
```

The first program enumerates all \(7{,}888{,}725\) sorted vectors at height at most \(24\); it returns the exact maximum and both equality cases, without rounding. The second program independently evaluates rational minimizers **clipped to their cells**, rather than using the unconstrained minimizer to choose the answer. It agrees with the projection formula for the proposed maximizer, for every sorted height-\(7\) vector, and for 300 deterministic larger vectors. The explicit sixteen-cell list above provides a further human-checkable certificate for the lower bound.

## Relationship to prior work

Kahlon, *The View-Obstruction Problem for Spheres in Dimensions Six and Seven* (arXiv:2610.37711, first public version 26 October 2026), proves the exact unrestricted constants for dimensions six and seven. His Section 2 gives the general cell evaluation formula used as background here; Section 6.4 reports direct screening at speed cap \(24\) in dimension six, and Remark 7.3 explicitly identifies a candidate eight-dimensional threshold as a natural next step. The source neither states nor certifies the height-24 eight-dimensional optimum or its equality classification. The present result is a complete finite-range evaluation, not a new solution of the unrestricted eight-dimensional problem.

Henze and Malikiosis, *On the covering radius of lattice zonotopes and its relation to view-obstructions and the lonely runner conjecture* (arXiv:1609.01939), develop a related covering-radius framework primarily for cube-obstruction and zonotope questions; it does not state this eight-dimensional Euclidean squared-distance computation. Older work by Cusick and by Dumir, Hans-Gill, and Wilker establishes earlier dimensions or general formulations. An earlier independent computation of this bounded-height instance may exist and would affect priority.

## Limitations

The bound \(v_i\le24\) is essential to the **upper** assertion and to the equality classification. There is no proof that \(\Delta_8\le8/17\), no unrestricted uniqueness theorem, and no claim that a search beyond height \(24\) cannot find a better direction. This finite screen does not prove a global classification. Reproducibility of the bounded census follows from the included integer-arithmetic source; the numerical discovery strategy is irrelevant to the proof. Historical priority and full global optimality remain unverified.

## References

1. V. Kahlon, *The View-Obstruction Problem for Spheres in Dimensions Six and Seven*, arXiv:2610.37711v1 (26 October 2026), revised v2 (30 October 2026), https://arxiv.org/html/2610.37711v2.
2. M. Henze and R.-D. Malikiosis, *On the covering radius of lattice zonotopes and its relation to view-obstructions and the lonely runner conjecture*, arXiv:1609.01939 (2016), https://arxiv.org/abs/1609.01939.
3. V. C. Dumir, R. J. Hans-Gill, and J. B. Wilker, *The view-obstruction problem for spheres in* \(\mathbb R^5\), *Monatshefte für Mathematik* 122 (1996), 21–34, https://doi.org/10.1007/BF01298453.
