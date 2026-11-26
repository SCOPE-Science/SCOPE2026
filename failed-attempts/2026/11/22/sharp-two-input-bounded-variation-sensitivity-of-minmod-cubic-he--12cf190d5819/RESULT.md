# Sharp two-input bounded-variation sensitivity of minmod cubic Hermite interpolation

## Finding

For every integer \(n\ge2\) and \(0\le\lambda\le3\), the continuous \(C^1\), piecewise-cubic Hermite interpolant \(H_{n,\lambda}\) with interior minmod knot slopes scaled by \(\lambda\), and zero endpoint slopes, preserves the total variation of each real nodal input exactly. Nevertheless, its attained sharp two-input Lipschitz factor from discrete first variation to continuous bounded variation is
\[
K_n(\lambda)=1+\frac{8\lambda}{27}\min\{2,n-2\}.
\]
Thus \(K_2=1\), \(K_3=1+8\lambda/27\), and \(K_n=1+16\lambda/27\) for \(n\ge4\). At unit scale, the factors are respectively \(1\), \(35/27\), and \(43/27\). Moreover, for any \(n\ge3\), the nonnegative interval \(0\le\lambda\le3\) is the maximal real parameter interval on which exact variation preservation holds for every input.

## Assumptions and scope

Let the knots be \(0,1,\ldots,n-1\). For \(y\in\mathbb R^n\), define \(\delta_i=y_{i+1}-y_i\), \(0\le i<n-1\), and
\[
\operatorname{mm}(a,b)=\begin{cases}
\operatorname{sgn}(a)\min\{|a|,|b|\},&ab>0,\\
0,&ab\le0.
\end{cases}
\]
The nodal derivatives are \(m_0=m_{n-1}=0\) and \(m_i=\lambda\operatorname{mm}(\delta_{i-1},\delta_i)\) for \(1\le i\le n-2\). With \(0\le t\le1\), set
\[
S(t)=3t^2-2t^3,\quad U(t)=t(1-t)^2,\quad W(t)=-t^2(1-t),
\]
and let the polynomial on the \(i\)-th cell be
\[
H_{n,\lambda}y(i+t)=y_i+\delta_iS(t)+m_iU(t)+m_{i+1}W(t).
\]
This has value \(y_i\) and derivative \(m_i\) at every knot. Write \(V_d(y)=\sum_{i=0}^{n-2}|\delta_i|\) and \(V_c(g)=\int_0^{n-1}|g'(x)|\,dx\) for continuous piecewise \(C^1\) functions. The norm statement is
\[
\sup_{V_d(y-z)>0}\frac{V_c(H_{n,\lambda}y-H_{n,\lambda}z)}{V_d(y-z)}=K_n(\lambda).
\]
Additive constants do not change either seminorm.

## Proof

**1. Each input has its original variation.** On every cell with \(\delta_i\ne0\), the ratios \(m_i/\delta_i\) and \(m_{i+1}/\delta_i\) are in \([0,\lambda]\); if \(\delta_i=0\), both slopes vanish. For \(0\le\lambda\le3\), the normalized cell polynomial is a convex combination of the four corner shapes \(S\), \(S+3U\), \(S+3W\), and \(S+3U+3W\). Their derivatives are, respectively,
\[
6t(1-t),\quad3(1-t)^2,\quad3t^2,\quad3(1-2t)^2,
\]
all nonnegative on \([0,1]\). Therefore each cell is monotone between its endpoint values, so \(V_c(H_{n,\lambda}y)=V_d(y)\).

**2. Reduce every two-input difference to local step columns.** The function \(\operatorname{mm}\) is continuous and piecewise linear in its two arguments, with the three local choices \(0\), the first input, or the second input. Consequently, \(y\mapsto H_{n,\lambda}y\) is a continuous finite-piecewise-linear map, taking values in the space of continuous piecewise cubics. On each linearity region, every interior knot slope independently selects \(0\), \(\lambda\delta_{i-1}\), or \(\lambda\delta_i\). Since these maps preserve constants, the operator seminorm from \(V_d\) is the largest norm of an individual unit-step column, with one \(\delta_j=1\) and all other input first differences zero. Indeed any difference vector is the sum of its step increments, and the integral absolute-derivative norm is subadditive.

For a step at edge \(j\), only the two adjacent knot slopes can depend on the step. Write their selector flags as \(a,b\in\{0,1\}\). The central cubic is \(S+\lambda aU+\lambda bW\), whose variation is exactly \(1\) by step 1 and the four-corner derivative argument. The optional left neighboring cell is a pure multiple of \(W\), and the optional right neighboring cell is a pure multiple of \(U\). The extrema are \(\max U=4/27\) at \(t=1/3\) and \(\min W=-4/27\) at \(t=2/3\), while both vanish at the cell endpoints. Thus
\[
V_c(U)=V_c(W)=\frac8{27},\qquad
V_c(\text{step column})=1+\frac{8\lambda}{27}(a+b).
\]
For \(n=2\), neither neighboring knot is interior; for \(n=3\), at most one exists; for \(n\ge4\), at most two exist. This yields \(K_n(\lambda)\) as a universal local-region bound. To pass from local regions to arbitrary real input pairs, traverse the straight line from \(y\) to \(z\); the output is an absolutely continuous, finite-piecewise-affine path and its derivative almost everywhere obeys the same bound. Integrating the derivative in the BV norm gives the claimed global inequality. A path along a region boundary follows by continuous perturbation.

**3. Sharpness by explicit input pairs.** For \(n=2\), any nonconstant difference is extremal. For \(n=3\), take the nodal first differences \((1,2)\); for \(n\ge4\), take \((2,1,2,\ldots,2)\). Let \(y_0=0\) and form \(y\) by cumulative summation. For \(n=3\), place a step of height \(1/4\) after knot \(0\), and for \(n\ge4\) place the step after knot \(1\), obtaining \(z\). The selected interior minmod inputs remain the unique smaller positive first difference \(\delta_j\), both in the original and perturbed inputs. The difference of the two interpolants is therefore precisely the unit-step column times \(1/4\), with one active adjacent slope for \(n=3\) and two for \(n\ge4\). Its ratio equals the upper bound. The same witnesses work for every \(\lambda\in[0,3]\), including both endpoints.

**4. Sharp parameter interval for one-input shape preservation.** For \(n\ge3\) use nodal values beginning \((0,1,2)\) and, if necessary, continue with unit differences. The first cubic has normalized derivative \(S'+\lambda W'\), which is negative close to \(t=0\) when \(\lambda>3\) and negative close to \(t=1\) when \(\lambda<0\). Its cell variation strictly exceeds its unit nodal increment, proving failure of universal exact variation preservation outside \([0,3]\).

## Verification

A standalone standard-library Python program, `check.py`, tests the four exact polynomial derivative identities, the rational extremal values of \(U,W\), exhaustive formal selector masks for dimensions \(2\) through \(9\) at five scales, actual attaining real input pairs for dimensions \(2\) through \(29\), randomized rational-input pairs, and variation failure for negative or greater-than-three scale. It computes cubic variation by subdividing at real stationary points. The universal conclusion and sharpness for all dimensions come from the proof above, not from the finite tests. Run `python3 check.py` in the same directory.

## Relationship to prior work

Huynh's 1991 technical memorandum gives the Hermite formula, the minmod limiter, and the monotonicity condition permitting endpoint slope ratios up to three; its *stability* discussion concerns continuity of limiter choices, not this exact two-input BV operator norm. Earlier foundational papers by Fritsch–Carlson and Fritsch–Butland focus on monotonicity and construction of shape-preserving cubics. Related analyses of linear Catmull–Rom interpolation and discontinuous affine minmod reconstruction concern different output operators and do not imply the present \(C^1\) Hermite sharp coefficient. Here the main invariant is variation **of the difference of two separately interpolated signals**, as opposed to variation of either interpolated input.

## Limitations

The result is for finite real samples on a uniform unit mesh, a zero-derivative endpoint convention, the two-argument minmod selector, and the precisely defined scale range. It does not apply without further analysis to nonuniform meshes, periodic endpoint conventions, harmonic-mean limiters, vector-valued curves, other BV seminorms, or subsequent time evolution. The manuscript establishes mathematics but does not assert independent certification or comprehensive historical priority.

## References

1. H. T. Huynh, *Accurate Monotone Cubic Interpolation*, NASA Technical Memorandum 103789, March 1991, https://ntrs.nasa.gov/citations/19910011517 ; full text https://ntrs.nasa.gov/api/citations/19910011517/downloads/19910011517.pdf .
2. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis **17** (1980), 238–246, https://doi.org/10.1137/0717021 .
3. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM Journal on Scientific and Statistical Computing **5** (1984), 300–304, https://doi.org/10.1137/0905021 .
