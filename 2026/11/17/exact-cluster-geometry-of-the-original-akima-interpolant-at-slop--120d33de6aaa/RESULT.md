# Exact cluster geometry of the original Akima interpolant at slope-degenerate data

## Finding

The following is a full classification of the limits of the original Akima cubic interpolant as the sampled data undergo arbitrarily small perturbations. The fact that the method can be discontinuous at a zero-weight slope configuration is known; the contribution here is the **simultaneous, all-knot cluster set** and its **exact sharp uniform and total-variation diameters**.

Let \(y=(y_j)_{j\in\mathbb Z}\) be real data on the unit integer grid and let \(d_j=y_{j+1}-y_j\) be eventually constant in each tail. At each knot \(i\), the original Akima slope is
\[
a_i(y)=\begin{cases}
\displaystyle\frac{|d_{i+1}-d_i|d_{i-1}+|d_{i-1}-d_{i-2}|d_i}{|d_{i+1}-d_i|+|d_{i-1}-d_{i-2}|},&\text{if the denominator is positive},\\[3pt]
\displaystyle\frac{d_{i-1}+d_i}{2},&\text{otherwise}.
\end{cases}
\]
Let \(\mathcal A y\) be the \(C^1\), piecewise cubic Hermite interpolant through the values \(y_i\) with knot slopes \(a_i(y)\). Define the finite critical set
\[
C(y)=\{i\in\mathbb Z:d_{i-2}=d_{i-1},\ d_i=d_{i+1},\ d_{i-1}\ne d_i\},
\qquad \Delta_i=d_i-d_{i-1}.
\]
A **cluster interpolant** is a limit in \(C^1_{\mathrm{loc}}(\mathbb R)\) of \(\mathcal A y^{(k)}\) for some real data sequences \(y^{(k)}\) with eventually constant secants and \(y^{(k)}_j\to y_j\) for every integer \(j\). Denote the collection by \(\mathscr K(y)\).

For every \(y\) as above, the cluster set is exactly the finite-dimensional box
\[
\boxed{\mathscr K(y)=\left\{\mathcal A y+\sum_{i\in C(y)}\left(\theta_i-\frac{d_{i-1}+d_i}{2}\right)\psi_i:\ \theta_i\in [\min(d_{i-1},d_i),\max(d_{i-1},d_i)]\right\}.}
\]
Here \(\psi_i\) is supported on \([i-1,i+1]\) and equals \(t^3-t^2\) at \(i-1+t\) and \(t(1-t)^2\) at \(i+t\) for \(0\le t\le1\). **Every choice of the parameters is simultaneously realizable**, even when several singular knots share the same vanishing secant-difference weights. The sets of open supports of the \(\psi_i\) do not overlap.

The diameter of this set of limiting interpolants, in the uniform metric and in total variation of differences, is exactly
\[
\boxed{\operatorname{diam}_{\infty}\mathscr K(y)=\frac4{27}\max_{i\in C(y)}|\Delta_i|,\qquad
\operatorname{diam}_{\mathrm{TV}}\mathscr K(y)=\frac{16}{27}\sum_{i\in C(y)}|\Delta_i|.}
\]
The maximum of an empty set and the sum over an empty set are defined to be zero. More precisely, for any \(F,G\in\mathscr K(y)\), the total variation \(\operatorname{Var}(F-G)=\int_{\mathbb R}|(F-G)'(x)|\,dx\) is finite, and these diameters are attained by two corner members of the cluster box. The Akima interpolation operator is continuous at \(y\), from coordinatewise data convergence to \(C^1_{\mathrm{loc}}\), **if and only if** \(C(y)\) is empty.

For a single corner with left and right secant slopes \(a\ne b\), the full range of limiting knot derivatives is \([a,b]\), the sharp curve-value ambiguity is \(4|a-b|/27\), and the sharp variation ambiguity is \(16|a-b|/27\). In particular, a nonnegative, nondecreasing ramp data sequence with secants \(0\) to its left and \(1\) to its right has strictly positive limiting ambiguity despite arbitrarily small nonnegative, nondecreasing perturbations.

## Assumptions and scope

The grid spacing is one, data and interpolants are real, and secants are constant outside a finite set of indices. The underlying data may have affine rather than constant tails; the difference of any two cluster interpolants has compact support, so its uniform norm and total variation are well defined. Perturbations need only converge at each fixed grid site; the explicit realizing perturbations can be chosen with finite support in the secant difference and converge at every site. The topology for the output cluster set is \(C^1_{\mathrm{loc}}\), not global \(C^1\) convergence of arbitrary perturbations.

The zero-denominator convention is the arithmetic mean of adjacent secants. No end-knot extrapolation convention is involved. This is the original, **not** the modified-Akima rule.

## Proof

**1. Pointwise knot-slope cluster intervals.** Put \(g_j=|d_{j+1}-d_j|\). The knot-slope expression can be written as a convex combination of \(d_{i-1}\) and \(d_i\) with coefficients \(g_i/(g_{i-2}+g_i)\) and \(g_{i-2}/(g_{i-2}+g_i)\). If the denominator at the limiting data is positive, the knot slope is continuous. If the denominator is zero but \(d_{i-1}=d_i\), every such convex combination, including the zero-denominator fallback, converges to the common value. The only possibly nonunique limits are at \(i\in C(y)\), where the cluster interval is contained in the segment joining the two adjacent secants. That interval is nondegenerate because \(\Delta_i\ne0\).

**2. Simultaneous attainability.** Fix arbitrary numbers \(t_i\in[0,1]\) for all \(i\in C(y)\). It suffices to prescribe positive, vanishing magnitudes \(g^{(k)}_j\) for originally zero adjacent secant differences, so that
\[
\frac{g_{i-2}^{(k)}}{g_{i-2}^{(k)}+g_i^{(k)}}\longrightarrow t_i\quad(i\in C(y)).
\]
Make a graph whose vertices are the gap indices used in these ratios and whose edges join \(i-2\) to \(i\) for each critical \(i\). Each edge changes the index by two; on any finite subset of the integers this graph is a disjoint union of paths, with no cycles. Along each path prescribe positive ratios recursively: for \(0<t_i<1\), use \(g_{i-2}/g_i=t_i/(1-t_i)\); for \(t_i=0\) use the ratio \(\varepsilon\), and for \(t_i=1\) use \(\varepsilon^{-1}\). Rescale every connected component by a common positive factor tending to zero sufficiently quickly. This achieves all required limiting ratios simultaneously.

To realize these magnitudes by actual secants, begin at a fixed index and integrate the adjacent secant increments \(d_{j+1}^{(k)}-d_j^{(k)}\). Keep every originally nonzero increment unchanged; at originally zero gaps choose an increment with the prescribed small magnitude. Only finitely many such increments need be modified. The resulting secants converge to the base secants on any fixed index range. If desired, one extra small compensating increment beyond the affected region makes the perturbed secants coincide with the base secants in both tails. Integrating once more gives data \(y^{(k)}\) converging at each knot. The weights at critical sites have exactly the prescribed limiting ratios, and hence their slope limits are
\[
\theta_i=(1-t_i)d_{i-1}+t_i d_i.
\]
Every interval choice is therefore realized. All other knot slopes converge uniquely by Step 1.

**3. Hermite representation and exact box.** On each unit cell, let \(t=x-j\in[0,1]\). The cubic Hermite formula is
\[
(\mathcal Ay)(j+t)=(2t^3-3t^2+1)y_j+(-2t^3+3t^2)y_{j+1}
+t(1-t)^2a_j(y)+(t^3-t^2)a_{j+1}(y).
\]
A change in only knot derivative \(a_i\) by a scalar \(c\) changes precisely the two adjacent cubic pieces by \(c\psi_i\). Since the limiting data values equal \(y\), Step 2 and linearity in the knot derivatives give the displayed exact cluster box. If two critical indices were consecutive, the first would force \(|d_i-d_{i-1}|>0\), while criticality of the second would force that same difference to vanish. Thus critical indices differ by at least two and the open interiors of their bump supports do not overlap.

**4. Sharp metric diameters.** For \(H_{10}(t)=t(1-t)^2\), the derivative is \((1-t)(1-3t)\), so its maximum on \([0,1]\) is \(4/27\), at \(t=1/3\), and its variation on that cell is \(8/27\). For \(H_{11}(t)=t^3-t^2\), the derivative is \(t(3t-2)\), so its absolute minimum magnitude is \(4/27\), at \(t=2/3\), and its cell variation is \(8/27\). Therefore
\[
\|\psi_i\|_\infty=4/27,\qquad \operatorname{Var}(\psi_i)=16/27.
\]
Because the open supports are pairwise disjoint, for arbitrary scalars \(c_i\),
\[
\left\|\sum_i c_i\psi_i\right\|_\infty=\frac4{27}\max_i|c_i|,
\qquad
\operatorname{Var}\left(\sum_i c_i\psi_i\right)=\frac{16}{27}\sum_i|c_i|.
\]
The maximal differences between any two independent choices of \(\theta_i\) are \(|\Delta_i|\), and simultaneous opposite corner choices are realizable by Step 2. This proves both diameter formulas. If \(C(y)\) is empty there is a unique cluster point, namely \(\mathcal Ay\), and the map is continuous; otherwise at least one nonzero bump gives multiple cluster points, proving the stated if-and-only-if criterion.

## Verification

Execute `python3 verify_akima_clusters.py` in a standard Python 3 environment. It uses no third-party packages. Exact rational tests establish the Hermite extrema and total variation. Randomized independent checks test slope limits at thousands of piecewise-affine secant profiles; exact rational two-corner constructions verify simultaneous ratio control, and dense sampling checks total-variation additivity. Outputs from the executed copy:

```
EXACT_HERMITE_BUMP_MAXIMUM_AND_VARIATION_PASS 4/27 16/27
ALL_REGULAR_SLOPES_AND_CRITICAL_INTERVALS_PASS 3000
SIMULTANEOUS_TWO_CORNER_RATIO_ATTAINMENT_PASS 504
INDEPENDENT_CONTINUUM_BUMP_VARIATION_STRESS_PASS
ALL_AKIMA_CLUSTER_GEOMETRY_CHECKS_PASS
```

These computations do **not** certify the infinite quantifiers; Steps 1–4 provide the unrestricted proof, including simultaneous attainability for every finite critical set.

## Relationship to prior work

Akima's 1970 construction and the subsequent 1989 USGS exposition already give the weighted knot-slope rule and midpoint convention. Moler and Ionita's 2019 full technical exposition **explicitly demonstrates discontinuity** of the original Akima interpolant under a machine-epsilon perturbation of a zero-weight corner. Thus neither the qualitative instability nor the fallback rule is claimed here as new. The earlier published sharp \(2/27\) range-defect analysis for monotone inputs concerns the interpolant's excursion outside the **single-input data range**, rather than the geometry of **all limits under vanishing perturbations**.

The present claim is specifically the simultaneous independence of all critical-knot limit slopes, the complete product-box representation of the cluster set, the exact \(4/27\) uniform diameter and the exact \(16/27\) total-variation diameter with sums across every corner. The 2019 one-corner example does not give those all-configuration conclusions, and the range-defect theorem controls a different extremal quantity. A historical equivalent may remain unindexed; see limitations.

## Limitations

The theorem uses uniform unit spacing and the original Akima slope rule with the standard midpoint fallback. No assertion is made for modified Akima, nonuniform grids, multidimensional interpolation, arbitrary finite-endpoint conventions or quantitative estimates at nonzero perturbation size. The \(C^1_{\mathrm{loc}}\) topology is essential; there is no claim that every pointwise-convergent global data perturbation produces a globally uniformly convergent interpolant.

The 1970 article's original publisher PDF and the 1969 predecessor report were not retrievable in full; the defining formula was independently checked in the full 1989 USGS exposition, full 2019 technical article and current scientific software documentation. These access limits leave residual historical-priority uncertainty. The 1969 report is indexed only with year precision in the consulted record, so October 1, 1970 is the earliest precisely day-verified date among the inspected sources defining the exact rule, not a claim that the method was first publicly disclosed on that day.

## References

1. H. Akima, *A New Method of Interpolation and Smooth Curve Fitting Based on Local Procedures*, Journal of the ACM **17** (1970), 589–602, https://doi.org/10.1145/321607.321609 (published October 1, 1970).
2. G. I. Evenden, *Review of Three Cubic Spline Methods in Graphics Applications*, U.S. Geological Survey Open-File Report 89-19 (1989), sections 5.2 and Appendix Listing 2, https://pubs.usgs.gov/of/1989/0019/report.pdf.
3. C. Moler and C. Ionita, *Makima Piecewise Cubic Interpolation* (April 29, 2019), https://blogs.mathworks.com/cleve/2019/04/29/makima-piecewise-cubic-interpolation/ (especially the original Akima zero-weight example).
4. SciPy documentation, *Akima1DInterpolator*, https://docs.scipy.org/doc/scipy-1.13.1/reference/generated/scipy.interpolate.Akima1DInterpolator.html (defining weights and the modified variant).
5. *The uniform Akima interpolant has sharp monotone range defect \(2/27\)* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-uniform-akima-interpolant-has-sharp-monotone-range-defect-2--4f68318a3dd5 (previously published, different norm and claim).
