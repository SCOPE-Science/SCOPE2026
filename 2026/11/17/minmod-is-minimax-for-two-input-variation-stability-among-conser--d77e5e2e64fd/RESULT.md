# Minmod is minimax for two-input variation stability among conservative cubic Hermite limiters

## Finding

Let \(y=(y_j)_{j\in\mathbb Z}\) be real data with finite discrete variation
\[
V_d(y)=\sum_{j\in\mathbb Z}|y_{j+1}-y_j|<\infty,\qquad \delta_j(y)=y_{j+1}-y_j.
\]
For a slope selector \(\phi:\mathbb R^2\to\mathbb R\), assign the knot derivatives \(m_j(y)=\phi(\delta_{j-1}(y),\delta_j(y))\) and interpolate each interval by the unique cubic Hermite polynomial matching the two endpoint values and derivatives. Denote the resulting \(C^1\) piecewise cubic by \(\mathcal H_\phi y\).

Define the *conservative affine-exact limiter class* \(\mathscr L\) by these conditions for every real pair \((a,b)\):

1. \(\phi(a,a)=a\) (affine reproduction).
2. If \(ab\le0\), then \(\phi(a,b)=0\).
3. If \(ab>0\), then \(\phi(a,b)\) has their common sign and \(|\phi(a,b)|\le\min(|a|,|b|)\).

No differentiability or symmetry is required of arbitrary members of this class. Write
\[
L(\phi)=\sup_{V_d(y-z)>0}
\frac{\operatorname{Var}_{\mathbb R}(\mathcal H_\phi y-\mathcal H_\phi z)}{V_d(y-z)},
\]
allowing \(L(\phi)=+\infty\) if a selector is discontinuous or otherwise unstable.

**Theorem.** Every \(\phi\in\mathscr L\) satisfies \(\operatorname{Var}_{\mathbb R}(\mathcal H_\phi y)=V_d(y)\) for every finite-variation sample sequence. Nevertheless,
\[
\boxed{\inf_{\phi\in\mathscr L}L(\phi)=L(\operatorname{minmod})=\frac{43}{27}.}
\]
Here \(\operatorname{minmod}(a,b)\) is the common-sign input of smaller absolute value when \(ab>0\), and zero otherwise. The exact constant is **attained** for this selector by two finite-variation signals whose secants differ at one edge only. No uniqueness of the minimizing selector is asserted.

## Assumptions and scope

The grid is the whole uniform integer line; data and data differences are real and have finite discrete variation. The continuous total variation is \(\int_{\mathbb R}|f'(x)|\,dx\) for these piecewise \(C^1\) interpolants. Additive constants in the input have no effect on either seminorm. The slope rule is local, translation-independent, and satisfies the three stated conditions. These are stricter than the general monotonicity conditions allowing endpoint slopes up to three times neighboring secants.

## Proof

**1. Hermite basis and one-input shape preservation.** On cell \([j,j+1]\), with \(t=x-j\in[0,1]\), set
\[
H(t)=3t^2-2t^3,\quad A(t)=t(1-t)^2,\quad B(t)=t^2(t-1).
\]
The interpolant is
\[
(\mathcal H_\phi y)(j+t)=y_j+\delta_j(y)H(t)+m_j(y)A(t)+m_{j+1}(y)B(t).
\]
For a nonzero secant \(d=\delta_j(y)\), the two knot slopes have its sign and magnitudes at most \(|d|\). Differentiating and rearranging gives
\[
P'(t)=m_j(1-t)^2+m_{j+1}t^2+
[6d-2m_j-2m_{j+1}]t(1-t).
\]
Each term has the sign of \(d\), as the bracket has magnitude at least \(2|d|\) with that sign. If \(d=0\), both endpoint derivatives are zero. Every cell therefore has variation exactly \(|d|\), and summing gives the claimed equality of one-input variations.

**2. Universal lower bound.** Fix \(0<\varepsilon<1\), and take two secant sequences that vanish outside a finite interval. Let the original consecutive secants at indices \((-2,-1,0,1,2,3)\) be \((0,1,1,1,1,0)\). Change only secant \(0\) from \(1\) to \(1-\varepsilon\) for the second input, keeping one common initial datum. The difference of the sampled data has discrete variation \(\varepsilon\).

Affine reproduction gives original derivatives \(m_0=m_1=1\). The conservative cap makes both perturbed derivatives \(\widetilde m_0,\widetilde m_1\le1-\varepsilon\). On cells \([-1,0]\) and \([1,2]\), the two cubic differences consist of a constant plus respectively \((1-\widetilde m_0)B(t)\) and \((1-\widetilde m_1)A(t)\). Since
\[
\int_0^1 |A'(t)|\,dt=\int_0^1 |B'(t)|\,dt=\frac8{27},
\]
these cells contribute at least \(8\varepsilon/27\) each. The middle cell has endpoint difference \(\varepsilon\), so its variation is at least \(\varepsilon\) whatever the curvature. Other cells contribute nonnegative variation. Thus every rule in the class has a two-input amplification of at least \(1+16/27=43/27\).

**3. Minmod upper bound.** The minmod map is continuous and piecewise linear. Along the data line segment \(y_s=z+s(y-z)\), its derivative, wherever defined, is either zero or one of the two secant derivatives. Hence the derivative of its knot value has the form \(a_j(s)\Delta_{j-1}+b_j(s)\Delta_j\), where \(\Delta_j=\delta_j(y-z)\), and \(a_j,b_j\in[0,1]\) are selectors. Substitution into the cellwise Hermite formula shows that the coefficient of \(\Delta_j\) in the *spatial derivative* of the homotopy velocity on cell \(j\) is
\[
K_{p,q}(t)=H'(t)+pA'(t)+qB'(t),\qquad 0\le p,q\le1.
\]
At the four vertices of this coefficient square, these functions are respectively
\[
6t(1-t),\quad (1-t)(1+3t),\quad t(4-3t),\quad1.
\]
They are nonnegative on \([0,1]\) and integrate to one, so \(\int_0^1|K_{p,q}|=1\) by convexity for any \(p,q\in[0,1]\). The same input secant \(\Delta_j\) contributes on each adjacent cell through at most one \(A'\) or \(B'\) kernel, with absolute integral \(8/27\). Integrating over the homotopy and summing cell variations gives
\[
\operatorname{Var}(\mathcal H_{\minmod}y-\mathcal H_{\minmod}z)
\le\sum_j\left(1+\frac8{27}+\frac8{27}\right)|\Delta_j|
=\frac{43}{27}V_d(y-z).
\]
For infinite sequences, first truncate the summable secant differences and pass to the limit; the same uniform bound controls all tails. Nondifferentiable branches of minmod are handled by its absolutely continuous, piecewise-affine restriction to every data segment.

**4. Sharpness for minmod.** With the secants in step 2, the perturbed minmod derivatives at knots \(0,1\) are exactly \(1-\varepsilon\). Therefore the middle-cell difference has spatial derivative of fixed sign and variation exactly \(\varepsilon\); the adjacent Hermite bumps have variation \(8\varepsilon/27\) each. All other cells have zero variation of the difference. The quotient is exactly \(43/27\) for every \(0<\varepsilon<1\), completing the proof.

## Verification

The standalone program `check_minimax.py` uses exact rational identities for the \(4/27\) cubic bump height, the \(8/27\) bump variation and the \(43/27\) coefficient. It checks the four extreme central derivative kernels, gives four exact rational single-secant witnesses, and numerically integrates 6,000 random rational data pairs by locating derivative-polynomial roots. All checks completed successfully. The random tests are corroboration only: universal optimality follows from the analytical lower and upper bounds above. To reproduce, run `python check_minimax.py` with standard Python.

## Relationship to prior work

The archived report by Hyman (1982; journal publication 1983) derives conditions on cubic Hermite knot derivatives that preserve monotonicity and discusses qualitative input sensitivity near extrema. The full text portions inspected contain a wider factor-three slope cap and algorithmic shape comparisons, but no sharp two-input bounded-variation minimax theorem. Williamson and Rasch (1987), Section 2, compare local derivative choices under shape constraints; their inspected treatment addresses monotonicity and interpolation accuracy rather than this perturbation norm. Edelman and Micchelli (1987) investigate which pairs of endpoint slopes admit monotone or convex interpolants, a distinct *single-curve feasibility* problem. Classical minmod finite-volume reconstructions likewise address one-input total-variation-diminishing conditions, which do not imply the two-input coefficient here.

A separately established sharp coefficient \(59/27\) for harmonic-mean cubic Hermite interpolation concerns a different slope selector. Indeed the signed harmonic mean at positive secants \(1,4\) is \(8/5>1\), so that method violates the present conservative unit-cap hypothesis. Its exact coefficient neither proves nor subsumes the universal lower bound or the minmod optimum. Literature search does not establish historical uniqueness; priority relative to potentially unindexed equivalent norm results remains qualified.

## Limitations

The minimax property holds only among **local conservative unit-capped affine-exact** slope rules. It does not extend to all monotone cubic interpolants (which can admit larger derivatives), general nonuniform grids, other spline degrees, multidimensional schemes or finite endpoint rules. It does not assert that minmod is the unique minimizer or an optimal approximation scheme for smooth data. The explicit witness is a nonlinear perturbation comparison, not a time-stepping TVD statement. Historical equivalents may exist outside the inspected literature. There has been no independent scientific audit.

## References

- J. M. Hyman, *Accurate Monotonicity-Preserving Cubic Interpolation*, Report LA-8796-MS (issued February 1982), archival copy: https://digital.library.unt.edu/ark:/67531/metadc1070768/ ; journal version *SIAM Journal on Scientific and Statistical Computing* 4 (1983), 645–654, https://doi.org/10.1137/0904045 (explicit public online date July 14, 2006).
- D. L. Williamson and P. J. Rasch, *Shape Preserving Interpolators for Semi-Lagrangian Transport* (1987), especially Section 2, https://www.ecmwf.int/sites/default/files/elibrary/1987/13110-shape-preserving-interpolators-semi-lagrangian-transport.pdf .
- A. Edelman and C. A. Micchelli, *Admissible Slopes for Monotone and Convex Interpolation*, Numerische Mathematik 51 (1987), 441–458, https://math.mit.edu/~edelman/publications/admissible_slopes.pdf .
- F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM Journal on Scientific and Statistical Computing 5 (1984), 300–304, https://doi.org/10.1137/0905021 .
