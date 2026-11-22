# Sharp two-input variation sensitivity of centered maximal averaging on a four-vertex path

## Finding

Let \(P_4\) be the unweighted path with vertices \(1,2,3,4\), and for \(f\in[0,\infty)^4\) define the centered graph-ball maximal map
\[
(\mathcal Mf)_i=\max_{r\in\{0,1,2,3\}}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}f_j,
\qquad B(i,r)=\{j\in\{1,2,3,4\}:|i-j|\le r\}.
\]
For any real vector \(h\), put \(V(h)=\sum_{i=1}^{3}|h_{i+1}-h_i|\). Then the exact two-input bound is
\[
V(\mathcal Mf-\mathcal Mg)\le\frac{11}{6}\,V(f-g)
\qquad\text{for every }f,g\in[0,\infty)^4.
\]
The coefficient \(11/6\) is optimal and **attained**, for example at \(f=(0,26,25,21)\) and \(g=(0,26,26,22)\).

## Assumptions and scope

Edges have unit length; vertex averages use unit masses. Balls are intersected with the finite vertex set, rather than completed using exterior zero-padding. There is no periodic identification. The input vectors are coordinatewise nonnegative, so the usual maximal average of \(|f|\) coincides with the displayed formula. Differences \(f-g\) are unrestricted real vectors. The seminorm \(V\) ignores constants; the map is translation-equivariant on the nonnegative domain whenever the translated vector remains admissible.

## Proof

Averaging choices at the four vertices, after duplicate radii are deleted, are respectively
\[
\begin{array}{c|l}
1& \{1\},\{1,2\},\{1,2,3\},\{1,2,3,4\}\\
2& \{2\},\{1,2,3\},\{1,2,3,4\}\\
3& \{3\},\{2,3,4\},\{1,2,3,4\}\\
4& \{4\},\{3,4\},\{2,3,4\},\{1,2,3,4\}.
\end{array}
\]
Index these choices from zero. Each branch choice \(a=(a_1,a_2,a_3,a_4)\) defines a row-stochastic rational matrix \(A_a\), with exactly \(4\cdot3\cdot3\cdot4=144\) possibilities. Write \(s^{(j)}_i=\mathbf 1_{i>j}\), \(j=1,2,3\). Since \(A_a\mathbf1=\mathbf1\), the identity
\[
h=h_1\mathbf1+\sum_{j=1}^3(h_{j+1}-h_j)s^{(j)}
\]
shows that
\[
V(A_ah)\le\bigl(\max_j V(A_as^{(j)})\bigr)V(h).
\]
A complete exact-rational enumeration of these 144 matrices gives the columnwise maxima
\[
\max_a V(A_as^{(1)})=\frac32,\quad
\max_a V(A_as^{(2)})=2,\quad
\max_a V(A_as^{(3)})=\frac32.
\]
Moreover, the **only** choice with \(\max_j V(A_as^{(j)})>11/6\) is \(a=(3,0,0,3)\), whose coefficient equals \(2\). All remaining 143 branch matrices have seminorm at most \(11/6\). These finite assertions are verified with `checker.py`, using rational arithmetic, explicit enumeration of all row choices, and no optimization tolerance.

The exceptional branch cannot be active at any nonconstant input \(x\). Indeed, let \(\bar x=(x_1+x_2+x_3+x_4)/4\). If the four-point average is maximal at vertex 1, comparison with the \(\{1,2,3\}\) ball gives \(x_4\ge\bar x\). If it is maximal at vertex 4, comparison with \(\{2,3,4\}\) gives \(x_1\ge\bar x\). If the singleton averages are maximal at vertices 2 and 3, comparison with their four-point averages gives \(x_2,x_3\ge\bar x\). The four inequalities force \(x_1=x_2=x_3=x_4=\bar x\).

For any \(f,g\) in the nonnegative cone, the segment \(x(t)=g+t(f-g)\), \(0\le t\le1\), stays in the cone. The coordinatewise maximum of finitely many affine forms is piecewise affine along this segment. Away from finitely many possible tie-break points, its derivative is a matrix \(A_a(f-g)\) with \(A_a\) active at \(x(t)\). Wherever \(x(t)\) is nonconstant, the exceptional branch is excluded; the previous bound yields \(V((\mathcal Mx(t))')\le(11/6)V(f-g)\). If \(x(t)\) is constant throughout a subinterval, its derivative is constant in space and has zero variation. Integrating the three adjacent differences and applying the integral triangle inequality proves the global bound, including tied inputs and end points.

Finally, direct evaluation at the stated pair gives
\[
\mathcal Mf=(18,26,25,24),\qquad
\mathcal Mg=(37/2,26,26,74/3),
\]
so \(f-g=(0,0,-1,-1)\), \(V(f-g)=1\), and
\[
\mathcal Mf-\mathcal Mg=(-1/2,0,-1,-2/3),\qquad
V(\mathcal Mf-\mathcal Mg)=\frac{11}{6}.
\]
This proves exact attainment, not merely sharpness in a limit.

## Verification

Run `python3 checker.py` using only the Python standard library. It enumerates **all 144** row-selection matrices, exactly computes each of their three step-response variations via `fractions.Fraction`, identifies the sole inadmissible norm-\(2\) branch, evaluates the explicit attaining pair, and performs 10,000 seeded exact-rational two-input tests. The finite enumeration is exhaustive for the stated matrices; random tests are supplementary and are not used to prove the universal theorem. The exclusion lemma and line-segment integration provide the noncomputational universal steps.

## Relationship to prior work

Madrid's discrete maximal variation inequalities (first public preprint 2015-12-13) and González-Riquelme–Madrid's finite-graph maximal-variation results address principally a *single input* \(V(\mathcal Mf)/V(f)\), not the present *two-input* \(V(\mathcal Mf-\mathcal Mg)/V(f-g)\). The latter paper gives general continuity statements with a full anchored BV norm, but does not specify this sharp coefficient for the four-vertex path. Liu–Zhang (2022) treats directed finite-graph maximal operators and their single-input variation norms. Previously indexed exact pairwise moduli on stars and complete graphs do not imply the path case: the four-vertex path is neither a star nor a complete graph, and the ball families differ. Indexed Hilbert-norm calculations on this path concern a different norm. Accordingly the specific sharp two-input path result is not implied by the inspected statements. The historical uniqueness assessment is qualified by the possibility of unindexed equivalent results.

## Limitations

The result is restricted to the nonnegative cone of the **unweighted open path with exactly four vertices** and to adjacent first-difference variation. It does not cover larger paths, weighted vertex masses, directed/periodic graphs, or the absolute-value maximal map on arbitrary signed input pairs. The complete-mask certificate is computationally finite and exact, but no claim of computer-independent formal verification or external audit is made. Mathematical priority is subject to earlier inaccessible or unindexed equivalent literature.

## References

1. J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112v1, 13 December 2015. https://arxiv.org/abs/1512.04112
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for Maximal Operators on Finite Graphs*, arXiv:2005.03146v3, 2020. https://arxiv.org/abs/2005.03146
3. F. Liu and X. Zhang, *Variation Inequalities for the Hardy–Littlewood Maximal Function on Finite Directed Graphs*, Mathematics 10 (2022), 950. https://doi.org/10.3390/math10060950
