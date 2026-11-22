# Parity-sharp lattice width and Lucas-number minimum directions of weighted directed-cycle simplices

## Finding

For integers \(n\ge3\) and \(w\ge2\), let \(e_0,\ldots,e_{n-1}\) denote the coordinate basis, with indices taken modulo \(n\), and put
\[
P_{n,w}=\operatorname{conv}\{e_i+w e_{i+1}:0\le i<n\}\subset\{x\in\mathbb R^n:\textstyle\sum_i x_i=w+1\}.
\]
Use the intrinsic affine lattice \(\mathbb Z^n\cap\operatorname{aff}(P_{n,w})\), and let \(\operatorname{lw}(P)\) be its lattice width, the smallest width of a nonconstant integral affine functional. Then
\[
\operatorname{lw}(P_{n,w})=\begin{cases}w-1,&n\text{ even},\\w,&n\text{ odd}.\end{cases}
\]
Moreover, all primitive minimum-width dual directions (considered modulo additive constants and reversal of sign) are characterized exactly:

- When \(n\) is even, there is exactly **one** unoriented direction: the alternating binary vector \((0,1,0,1,\ldots,0,1)\).
- When \(n\) is odd, minimum-width direction lines correspond bijectively to the **nonempty independent vertex sets of the cycle** \(C_n\). The indicator of the independent set is the unique member of the direction line whose entries are binary and contain no cyclically adjacent ones.

Hence the number \(D_n\) of unoriented minimum-width directions is
\[
D_n=\begin{cases}1,&n\text{ even},\\L_n-1,&n\text{ odd},\end{cases}
\qquad L_0=2,\quad L_1=1,\quad L_{n+2}=L_{n+1}+L_n.
\]
For fixed \(w\), the number of optimal slab normals therefore alternates between a single line in even coordinate order and exponentially many lines in odd coordinate order.

## Assumptions and scope

The integers satisfy \(n\ge3\) and \(w\ge2\). The cyclic shift matrix \(C\) has \(Ce_i=e_{i+1}\). Its edge-vertex matrix is \(I+wC\), with determinant \(1-(-w)^n\ne0\); thus the stated points are affinely independent and \(P_{n,w}\) is an \((n-1)\)-simplex. The affine-lattice difference group is \(\{z\in\mathbb Z^n:\sum z_i=0\}\). Every integral functional on it can be represented by an integer coefficient vector \(u\in\mathbb Z^n\), uniquely modulo integer multiples of \((1,\ldots,1)\). An unoriented direction further identifies \(u\) and \(-u\). Binary vectors with both digits are primitive in this dual lattice.

## Proof

**1. Universal extremal-coordinate bound.** For a nonconstant integer direction \(u=(u_0,\ldots,u_{n-1})\), let \(m=\min_i u_i\), \(M=\max_i u_i\), \(\Delta=M-m\ge1\), and
\[
f_i=u_i+w u_{i+1}.
\]
This is the value of the functional on vertex \(e_i+w e_{i+1}\); hence its width is \(\max_i f_i-\min_i f_i\). If \(u_j=M\), then \(f_{j-1}\ge m+wM\). If \(u_k=m\), then \(f_{k-1}\le M+wm\). Therefore
\[
\max_i f_i-\min_i f_i\ge(w-1)\Delta.\tag{1}
\]
The coordinate indicator \(u=e_0\) has width \(w\). When \(n\) is even, the alternating binary vector has consecutive vertex values \(1,w\) and width \(w-1\). Thus (1) gives the exact even-order minimum and the odd-order upper bound \(w\).

**2. Binary directions.** Suppose \(\Delta=1\). Subtracting the constant \(m\), let \(u_i\in\{0,1\}\) with both digits present. Its cyclic directed transitions include both \(0\to1\) and \(1\to0\). The corresponding vertex values are \(w\) and \(1\), while the equal transitions \(0\to0\) and \(1\to1\) have values \(0\) and \(w+1\). Therefore the width is \(w-1\) precisely when every adjacent pair is unequal; otherwise it is \(w\) if exactly one type of equal pair occurs, and \(w+1\) if both types occur. A fully alternating cyclic word exists exactly at even \(n\). At odd \(n\), at least one equal pair occurs, so every binary nonconstant direction has width at least \(w\), with equality precisely when it avoids either \(00\) or \(11\) cyclically.

**3. Exclusion of nonbinary minimizers.** At even \(n\), a direction of width \(w-1\) satisfies \(\Delta=1\) by (1), so it is one of the alternating binary directions, which are negatives modulo constants. At odd \(n\), if \(w\ge3\), inequality (1) excludes \(\Delta\ge2\) because \(2(w-1)>w\). For \(w=2\), (1) excludes \(\Delta\ge3\). It remains to rule out an odd cyclic direction with \(\Delta=2\) and width \(2\). Subtract its minimum so its entries belong to \(\{0,1,2\}\) and both \(0,2\) occur. Applying the two inequalities from step 1 to indices attaining \(2\) and \(0\) shows \(\max f_i\ge4\) and \(\min f_i\le2\). Width \(2\) would force every \(f_i\) into \([2,4]\). The only permitted adjacent transitions \((u_i,u_{i+1})\) would then be
\[
(0,1),\ (0,2),\ (1,1),\ (2,0),\ (2,1).
\]
Any appearance of digit \(1\) forces all following entries to equal \(1\), by the permitted outgoing transitions, and hence all cyclic entries to be \(1\), contrary to \(\Delta=2\). With digits \(0,2\) alone, the only permitted transitions alternate \(0\to2\to0\), which is impossible for odd \(n\). Thus \(\Delta=1\) for all minimum-width directions at odd \(n\), including \(w=2\). This finishes the sharp width formula and complete binary classification.

**4. Direction census.** At odd \(n\), a binary cyclic word attaining width \(w\) has exactly one of the two adjacency types \(00,11\). Identifying a direction with its negative modulo constants sends the word to its binary complement and exchanges the forbidden adjacency type. Hence each unoriented line has a unique representative with no cyclically adjacent ones, and this representative must contain at least one \(1\). These are precisely the nonempty independent vertex sets of \(C_n\). Writing \(F_0=0,F_1=1\) for Fibonacci numbers, the number of independent sets of \(C_n\), including the empty set, is \(F_{n+1}+F_{n-1}=L_n\): split according to whether a fixed vertex is absent or present, leaving paths of lengths \(n-1\) and \(n-3\). Removing the empty set proves \(D_n=L_n-1\). For even \(n\), step 3 already gives \(D_n=1\).

## Verification

Run `python3 verify_width.py` using Python 3 standard library. The checker exhaustively inspects every primitive, constant-normalized integer direction with coordinate range at most three for \(3\le n\le8\) and \(2\le w\le5\). It verifies the claimed lower bounds, exact equality characterization, and number of unoriented directions: 306,168 bounded direction instances and 352 minimum-width instances. This is a finite consistency test, not a substitute for steps 1–4 of the proof, and it is not exhaustive in unbounded dimension, weight, or coefficient range.

## Relationship to prior work

Biermann, Lin and O'Keefe introduce vertex-weighted oriented-graph edge polytopes and study their integer decomposition property, including uniform-weight cycles. Their definition yields exactly the vertex vectors above for a naturally directed uniform-weight cycle, but their cycle results concern decomposition and normality rather than lattice width or complete minimizing normal directions. Doolittle, Katthän, Nill and Santos study lattice width for a distinct family of circulant simplices, with generator \((1,m,0,\ldots,0,-m)\); their width theorem does not directly cover the two-term nonnegative generator \((1,w,0,\ldots,0)\). The integer-affine and cyclic conventions in both papers were compared explicitly. The present classification is not an inference from their stated results. Priority under other terminology remains a risk, and no claim of exhaustive historical uniqueness is made.

## Limitations

The theorem concerns constant integral vertex weight and the naturally oriented cycle, not arbitrary orientations or nonuniform weights. The direction census is for the intrinsic integer affine lattice, not Euclidean normal lengths; the latter define a different optimization. The finite checker cannot certify the universal theorem independently. A full historical priority audit has not been performed.

## References

1. Jennifer Biermann, Kuei-Nuan Lin, Augustine O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs*, arXiv:2611.17047v1, first posted 2026-11-12, https://arxiv.org/html/2611.17047v1 .
2. Joseph Doolittle, Lukas Katthän, Benjamin Nill, Francisco Santos, *Empty simplices of large width*, arXiv:2103.14925 (2021); *Forum of Mathematics, Sigma* 13 (2025), e21, https://doi.org/10.1017/fms.2024.131 .
