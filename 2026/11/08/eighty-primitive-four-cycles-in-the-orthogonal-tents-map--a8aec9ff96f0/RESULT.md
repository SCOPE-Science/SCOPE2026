# Eighty primitive four-cycles in the orthogonal tents map

## Finding
On the flat torus \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), define \(f(t)=2\min(t,1-t)\) for canonical \(0\le t<1\), and
\[
H(x,y)=\bigl(u,\{y+f(u)\}\bigr),\qquad u=\{x+f(y)\},
\]
where braces denote fractional part. The map has **exactly 80 distinct primitive period-four orbits**, consisting of 320 distinct points of least period four. Exactly 64 of these cycles avoid every nondifferentiability line during their orbits and are hyperbolic: 32 have fourth-return trace \(-574\), 16 have trace \(578\), and 16 have trace \(178\). The remaining 16 primitive period-four cycles encounter a shear switching line, so a single classical derivative trace is not assigned to them. All 80 cycles are isolated. The four known one-dimensional period-two families are not counted as period-four cycles.

## Assumptions and scope
The torus map is the composition of the two continuous orthogonal tent shears with slope magnitude 2, at the symmetric cusp parameter. A primitive period-four orbit has four distinct torus points, with \(H^4(p)=p\) and \(H^2(p)\ne p\). A regular orbit avoids \(y=0,1/2\) and the intermediate horizontal shear value \(u=0,1/2\), modulo one, for each of four iterations. These conditions concern the complete torus, including points on the edges of the canonical half-open square.

## Proof
The triangular horizontal and vertical shear operations partition the closed unit square into finitely many convex rational polygons on each fixed itinerary. On each polygon the fourth iterate has an affine integer-linear lift \(p\mapsto Ap+b\). Subdivide by the sign of \(y-1/2\), the integer translation of the horizontal shear (0 or 1), the sign of \(u-1/2\), and the integer translation of the vertical shear (0 or 1). Intersect at each choice with its four corresponding rational closed half-planes. Dropping zero-area faces is complete because the boundaries are covered by closures of adjacent full-dimensional cells; on the torus the map is continuous. Direct exact clipping produces \(15,97,515,2337\) full-dimensional cells after one through four iterations, respectively. Each generation covers the entire square and has total exact area one.

For each fourth-step cell solve \((I-A)p=b\). Exactly 2328 cells have nonsingular \(I-A\), and nine are singular. There are 574 cell-incidence solutions among the nonsingular cells, with 347 distinct representatives in the closed square. Identifying opposite torus boundaries produces exactly 336 distinct nonsingular-cell solution representatives fixed by the fourth iterate, all checked by direct exact fractional arithmetic against the globally defined map. Of these representatives, 16 have period dividing two (and may belong to the previously known line families); the other 320 have least period four.

For every singular cell, solve the two affine fixed equations along its polygon. Four cells have incompatible equations, one compatible line misses its polygon, and the other four give exactly the familiar period-two line segments, with endpoints \((1/2,1/4)\) to \((3/4,0)\), \((3/4,1/2)\) to \((1,1/4)\), \((0,3/4)\) to \((1/4,1)\), and \((1/4,1/2)\) to \((1/2,3/4)\). Their second iterate equals the identity on each segment: this follows from the affine branch formulas after checking both endpoints and an interior point. Thus no singular cell contributes a primitive four-cycle. In particular no positive-dimensional family of primitive period-four points is overlooked.

To treat the canonical edges independently, restrict the fourth-step affine formulas to \(x=0\) and \(y=0\), solve the one-variable return equations allowing each resulting coordinate to equal 0 or 1 before torus identification, and verify all candidates under the global map. This yields 23 boundary fixed points, all already in the 336-point census; no entire boundary interval is fixed. In particular four canonical points overlooked by a naive half-open-only affine solve are included by identifying the right/top-edge lifts. This step is essential for the exact count.

Since every primitive period-four orbit has four points, the 320 points form exactly 80 orbits. On regular orbits the Jacobian per step is
\[
\begin{pmatrix}1&a\\b&1+ab\end{pmatrix},\quad a,b\in\{-2,2\},
\]
with determinant one. Exact multiplication along all 320 primitive-period-four points gives 128 points of trace \(-574\), 64 of trace \(578\), 64 of trace \(178\), and 64 at switching orbits where the derivative is not defined. Traces are constant along each smooth cycle by cyclic matrix multiplication, yielding respectively 32,16,16 regular hyperbolic cycles and 16 switching cycles. The regular traces have absolute value exceeding two, proving hyperbolicity. Every fourth-return fixed point outside the known period-two segments lies on a nonsingular affine cell, so these primitive cycles are isolated even at switching boundaries.

## Verification
Execute `python3 checker.py` with Python 3 and no third-party libraries. It builds the full four-step rational polygon partition, solves fixed-point equations, identifies torus edges, verifies all 336 isolated fourth-iterate points, excludes the four period-two segments, and checks the exact orbit and trace counts. The computation uses unbounded integers and rational fractions, not floating-point tolerances. The proof of exhaustiveness is the finite affine subdivision of the entire torus; mere sampling would not suffice. The checker prints all aggregate counts and fails on discrepancies. The independent review of this mathematical claim is not yet performed.

## Relationship to prior work
Myers Hill, Sturman and Wilson introduced the orthogonal non-monotonic shear family and studied hyperbolicity, elliptic islands and mixing in their 2021 preprint. Their 2023 treatment of the symmetric orthogonal tents cusp establishes polynomial correlation decay and explicitly identifies four two-periodic line segments. Neither inspected treatment supplies the complete primitive fourth-period point count with its differentiability and trace partition. The two-periodic segments are existing prior results and are not claimed as new. The complete four-cycle census is logically distinct from their correlation-decay conclusions and from the general density of periodic points. A search of related published mathematical records identified no equivalent fourth-period census; this is not proof against unindexed literature.

## Limitations
This classification concerns the unperturbed slope-two orthogonal tents map, not an open parameter neighborhood and not higher periods. Nonsmooth periodic orbits are enumerated but not assigned a differentiable monodromy matrix or a stability type. The classification is finite and exact; no global dynamical zeta function or long-period asymptotic is claimed. Literature-priority assessment remains subject to inaccessible or unindexed results; no independent mathematical audit has been performed.

## References
- J. Myers Hill, R. Sturman and M. C. T. Wilson, *Exponential Mixing by Orthogonal Non-Monotonic Shears*, arXiv:2112.05463 (first posted 2021-12-10); *Physica D* 434 (2022), 133224. https://arxiv.org/abs/2112.05463
- J. Myers Hill, R. Sturman and M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515 (first posted 2023-03-15). https://arxiv.org/abs/2303.08515
