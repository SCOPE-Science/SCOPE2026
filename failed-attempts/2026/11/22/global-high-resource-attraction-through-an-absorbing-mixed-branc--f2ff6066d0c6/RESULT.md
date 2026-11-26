# Global high-resource attraction through an absorbing mixed branch in a two-maxima map

## Finding

For \(\alpha>0\), let \(\Phi_\alpha:[1/2,1)^2\to[1/2,1)^2\) be the map

\[
\Phi_\alpha(x,y)=\left(
\frac{\max\{\alpha x(1-y),1-x\}}{\alpha x(1-y)+1-x},
\frac{\max\{\alpha y(1-x),1-y\}}{\alpha y(1-x)+1-y}
\right).
\]

**Theorem (global winner–loser attraction in the high-resource range).** For every real \(\alpha\ge4\) and every initial pair \((x_0,y_0)\in[1/2,1)^2\) with \(x_0\ne y_0\), the orbit converges to one of two asymmetric fixed points. If \(x_0>y_0\), then

\[
\lim_{n\to\infty}(x_n,y_n)=\left(1-\frac{1}{\alpha(\alpha-1)^2},1-\frac1\alpha\right).
\]

For \(x_0<y_0\), interchange the coordinates. Moreover, after finitely many iterates the first component always chooses its \(\alpha x(1-y)\) branch and the second always chooses its \(1-y\) branch (with indices interchanged when \(x_0<y_0\)). Thereafter the orbit converges geometrically. In the odds coordinates and weighted norm given in the proof, a valid uniform contraction factor for every \(\alpha\ge4\) is \(55/64\), after entry into a fixed explicit trapping rectangle.

## Assumptions and scope

The variables \(x,y\) are maxima of two normalized two-component distributions, hence lie in \([1/2,1)\); the endpoint \(1\) is excluded so odds remain strictly positive. The result covers every unequal initial pair in this domain, including ties at \(1/2\) for one individual maximum. The parameter \(\alpha\) is constant in time and satisfies \(\alpha\ge4\). No assumption of genericity, random initial data, or proximity to an attractor is made. The diagonal \(x=y\), other resource regimes and the underlying position labels of the two-component distributions are outside the claimed off-diagonal convergence theorem. When a maximum-selection expression ties, either branch gives the same numerical state.

## Proof

By interchange symmetry assume \(x_0>y_0\). Define the positive odds

\[
u=\frac{1-x}{x},\quad v=\frac{1-y}{y},\quad r=\frac uv,\quad b=v.
\]

Initially \(0<r<1\) and \(0<b\le1\). The two odds before taking the smaller of a quantity and its reciprocal are

\[
A=\frac{r(1+b)}\alpha,\qquad B=\frac{1+rb}{\alpha r}.
\]

The exact updated odds are \(u'=\min\{A,A^{-1}\}\) and \(v'=\min\{B,B^{-1}\}\). Since \(0<r<1\), \(0<b\le1\) and \(\alpha\ge4\), one has \(A<2/\alpha\le1/2\), hence \(u'=A\) at every step provided the order remains strict.

**Step 1: finite entry into the mixed branch.** If \(B<1\), then \(v'=B\) and therefore

\[
r'=r^2\frac{1+b}{1+rb},\qquad b'=\frac{1+rb}{\alpha r}.
\]

Consequently

\[
0<\frac{r'}r=\frac{r(1+b)}{1+rb}\le\frac{2r}{1+r}\le\frac{2r_0}{1+r_0}<1
\]

as long as the unmixed choice \(B<1\) persists. In particular, if it persisted indefinitely then \(r_n\to0\) geometrically. Yet \(r<1/\alpha\) implies \(B>1\), contradicting perpetual \(B<1\). Thus a first \(B\ge1\) step occurs in finite time. Strict ordering is preserved during unmixed steps since \(r'<r<1\).

If \(B\ge1\), including equality, the two new odds yield the **mixed map**

\[
F_\alpha(r,b)=\biggl(\frac{(1+rb)(1+b)}{\alpha^2},\,\frac{\alpha r}{1+rb}\biggr).
\]

Since \(0<r<1\) and \(0<b\le1\), its output obeys \(0<r'\le4/\alpha^2\) and \(0<b'\le1\), with \(r'<1\). Define the closed rectangle \(D_\alpha=[0,4/\alpha^2]\times[0,1]\). Every point in \(D_\alpha\) satisfies \(\alpha r\le4/\alpha\le1\le1+rb\); thus \(B\ge1\) there, and the mixed formula remains the actual maxima dynamics. For \((r,b)\in D_\alpha\),

\[
0\le F_{\alpha,1}(r,b)\le\frac{2(1+4/\alpha^2)}{\alpha^2}\le\frac4{\alpha^2},\qquad 0\le F_{\alpha,2}(r,b)\le\frac4\alpha\le1.
\]

Therefore \(D_\alpha\) is forward-invariant and the mixed choice is permanent after the first entry. This proves the eventual branch assertion without any appeal to numerical simulations.

**Step 2: uniform contraction.** The sharper bound \(2(1+4/\alpha^2)/\alpha^2\le5/32\) gives the forward-invariant absorbing rectangle

\[
D_\alpha^{\rm s}=[0,R_\alpha]\times[0,1],\quad R_\alpha=\min\{5/32,4/\alpha^2\}.
\]

Indeed, \(F_\alpha(D_\alpha)\subset D_\alpha^{\rm s}\subset D_\alpha\), and invariance follows. Its Jacobian is

\[
DF_\alpha(r,b)=\begin{pmatrix}
\dfrac{b(1+b)}{\alpha^2}&\dfrac{1+r+2rb}{\alpha^2}\\[3pt]
\dfrac\alpha{(1+rb)^2}&-\dfrac{\alpha r^2}{(1+rb)^2}
\end{pmatrix}.
\]

Use \(\|(\delta r,\delta b)\|_\alpha=\max\{2\alpha|\delta r|,|\delta b|\}\). The induced weighted operator norm is bounded by the largest of the two weighted row sums. Everywhere in \(D_\alpha^{\rm s}\), using \(0\le r\le R_\alpha\), \(0\le b\le1\),

\[
\begin{aligned}
S_1&\le\frac2{\alpha^2}+\frac2\alpha(1+3R_\alpha)
\le\frac{2}{16}+\frac12\biggl(1+\frac{15}{32}\biggr)=\frac{55}{64},\\
S_2&\le\frac12+\alpha R_\alpha^2\le\frac12+\frac{16}{\alpha^3}\le\frac34.
\end{aligned}
\]

The nonnegative rectangle is convex, so the mean-value inequality gives

\[
\|F_\alpha(z)-F_\alpha(\widetilde z)\|_\alpha
\le\frac{55}{64}\|z-\widetilde z\|_\alpha
\]

for every \(z,\widetilde z\in D_\alpha^{\rm s}\). Banach's fixed-point theorem yields one attracting fixed point in that rectangle and geometric convergence from every point eventually entering it. Notice this establishes global convergence within the entire off-diagonal half-domain, rather than merely local stability of a predetermined candidate.

**Step 3: identify the limit.** Direct substitution into \(F_\alpha\) verifies its positive fixed point is

\[
b_*=\frac1{\alpha-1},\qquad
r_*=\frac{\alpha-1}{\alpha(\alpha-1)^2-1}.
\]

Recover \(x=1/(1+rb)\) and \(y=1/(1+b)\), giving

\[
x_*=1-\frac1{\alpha(\alpha-1)^2},\qquad
y_*=1-\frac1\alpha.
\]

The formulas lie in the asserted domain and have \(x_*>y_*\). Continuity of the odds-to-state conversion, with bounded derivative on the trapping rectangle, transfers geometric convergence to \((x_n,y_n)\). Interchanging the two players proves the other strict ordering. \(\square\)

## Verification

The proof above is an infinite-time argument. The accompanying `checker.py` is a supplementary, non-exhaustive stress test, not a substitute for the contraction proof. It checks the original maxima map and the mixed-coordinate formula with exact rational arithmetic in 700 independently sampled unequal starting states at \(\alpha\in\{4,5,6,10,100\}\), verifies strict mixed-branch persistence for four successive steps, and checks 1500 numerical trajectories for convergence at six resource values. Symbolic expressions for all four entries of the Jacobian, the attracting fixed point, and the physical-coordinate conversion are checked with SymPy. To reproduce: `python checker.py` with Python 3 and SymPy installed. The check prints three `PASS` lines; no claim of an exhaustive parameter or orbit census is made.

## Relationship to prior work

Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1 (first made public 9 November 2026), introduced exactly this maxima map, proved the relevant order-preservation and the existence and **local** stability of the winner–loser fixed points for \(\alpha>2\), and reported global attraction on the off-diagonal based on numerical evidence. The additional assertion proved here is a **global** basin theorem for the entire parameter half-line \(\alpha\ge4\), with a finite absorbing mixed branch and a uniform analytic contraction rate. The fixed-point formulas and the model itself are prior results, not new claims.

The general max-recurrence literature includes Papaschinopoulos, Schinas and Hatzifilippidis, *Global behavior of the solutions of a max-equation and of a system of two max-equations* (2003), DOI 10.1023/A:1022833112788, covering broader classes of max difference equations. Its publicly accessible abstract does not specify this normalized two-maxima map; the complete article was not available in the inspected public sources. The present proof is specialized to the exact rational normalization and branch geometry above; no general novelty claim about max-type systems is made.

## Limitations

The constant \(4\) is a **sufficient** high-resource cutoff from the uniform trapping estimates and is not asserted to be the optimal threshold. The previously proposed global convergence assertion over the full interval \(2<\alpha<4\) is not settled here. The diagonal \(x=y\), boundary points with either maximum exactly \(1\), physical labels of the maxima, robustness to perturbed update rules, and arbitrary numbers of resource positions are not classified. The explicit factor \(55/64\) holds only after the finite transient in the stated weighted odds norm, not necessarily on the original coordinate space at time zero. No independent mathematical validation has been performed.

## References

1. O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1, 9 November 2026. https://arxiv.org/abs/2611.13318
2. G. Papaschinopoulos, C. J. Schinas, V. Hatzifilippidis, *Global behavior of the solutions of a max-equation and of a system of two max-equations*, Journal of Computational Analysis and Applications **5** (2003), 237–254. https://doi.org/10.1023/A:1022833112788
