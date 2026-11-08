# Two exact entropy anchors at critical resonances of the Lawnik–Berezowski M-map

## Finding
For the Lawnik–Berezowski piecewise-quadratic interval family, two geometrically distinguished postcritically finite parameters have exact topological entropies:
\[
h_{\mathrm{top}}(f_{p_L})=\log(2+\sqrt{2}),\qquad h_{\mathrm{top}}(f_{p_R})=\log(1+\sqrt{3}).
\]
The first is the unique \(p_L\in(1/4,1/2)\) solving \(4p_L^3-4p_L+1=0\), and the second is the unique \(p_R\in(1/4,1/2)\) solving \(4p_R^3-4p_R^2+4p_R-1=0\). These are the two natural contacts of the central critical value with an outer critical point. At both contacts the complete monotonic-lap sequence satisfies an exact second-order recurrence.

## Assumptions and scope
Let \(p\in(1/4,1/2)\) and \(f_p:[0,1]\to[0,1]\) be the continuous map
\[
f_p(x)=\begin{cases}
\frac{x}{p}\bigl(2-\frac{x}{p}\bigr),&0\le x\le\frac12,\\
\frac{1-x}{p}\bigl(2-\frac{1-x}{p}\bigr),&\frac12\le x\le1.
\end{cases}
\]
Its ordered turning points are \(p,1/2,1-p\); their images are \(1,h(p),1\), where
\[
h(p)=\frac{4p-1}{4p^2}.
\]
The endpoints map to zero. Let \(L_n(f_p)\) denote the number of maximal intervals on which \(f_p^n\) is strictly monotone. The entropy is the ordinary topological entropy of the continuous map on the compact interval; no distribution of initial data or floating-point discretization is assumed.

## Proof
**Critical-contact parameters.** Algebra gives
\[
h(p)-p=-\frac{4p^3-4p+1}{4p^2},\qquad
h(p)-(1-p)=\frac{4p^3-4p^2+4p-1}{4p^2}.
\]
The left numerator is strictly decreasing on \((1/4,1/2)\), positive at \(1/4\) and negative at \(1/2\). The right numerator is strictly increasing on this interval, negative at \(1/4\) and positive at \(1/2\). Hence both roots exist uniquely. At the first, \(f_{p_L}(1/2)=p_L\); at the second, \(f_{p_R}(1/2)=1-p_R\). In each case these images subsequently visit \(1\), then the fixed endpoint \(0\), so the critical orbit is finite.

**Exact Markov partitions.** At each contact take four closed intervals, overlapping only at endpoints:
\[
I_1=[0,p],\ I_2=[p,1/2],\ I_3=[1/2,1-p],\ I_4=[1-p,1].
\]
Every restriction is strictly monotone. The outer intervals each map onto the whole unit interval. The two inner intervals both map onto \([p,1]\) at the left contact, and onto \([1-p,1]\) at the right contact. Thus the source-row/target-column incidence matrices are exactly
\[
A_L=\begin{pmatrix}1&1&1&1\\0&1&1&1\\0&1&1&1\\1&1&1&1\end{pmatrix},\quad
A_R=\begin{pmatrix}1&1&1&1\\0&0&0&1\\0&0&0&1\\1&1&1&1\end{pmatrix}.
\]
Since the partition endpoints map to partition endpoints and each branch covers exactly the indicated consecutive partition atoms, allowable length-\(n\) Markov cylinders correspond to maximal strict monotonicity intervals of \(f_p^n\). More explicitly, a new boundary of these cylinders in the interior of an old one is a pullback of one of the three turning points; there the corresponding iterate has a strict local extremum. Therefore two neighboring cylinders are not incorrectly counted as distinct laps, and none is missing. Consequently, with \({\bf1}\) the four-component all-ones vector,
\[
L_n(f_{p_L})={\bf1}^{\mathsf T}A_L^{n-1}{\bf1},\qquad
L_n(f_{p_R})={\bf1}^{\mathsf T}A_R^{n-1}{\bf1}\quad(n\ge1).
\]
**Recurrences and entropy.** Direct matrix multiplication yields \(L_1=4\), \(L_2=14\) for the first case, and \(L_1=4\), \(L_2=10\) for the second; the characteristic polynomials are, respectively,
\[
\det(zI-A_L)=z^2(z^2-4z+2),\qquad \det(zI-A_R)=z^2(z^2-2z-2).
\]
Cayley–Hamilton, or the rank-two column structure, gives the complete recurrences
\[
L_{n+2}(f_{p_L})=4L_{n+1}(f_{p_L})-2L_n(f_{p_L}),\qquad
L_{n+2}(f_{p_R})=2L_{n+1}(f_{p_R})+2L_n(f_{p_R})
\]
for every integer \(n\ge1\). These positive sequences have exponential growth rates \(2+\sqrt2\) and \(1+\sqrt3\), since in each case the coefficient of the dominant root is strictly positive. The Misiurewicz–Szlenk lap-number formula for a continuous piecewise monotone interval map identifies topological entropy as \(\lim_{n\to\infty}n^{-1}\log L_n\), giving the asserted values.

## Verification
Run `python checker.py` with SymPy installed. It verifies the two algebraic critical-contact equations, uniqueness of the roots by exact rational root counts and derivative signs, the two exact characteristic polynomials, and eleven terms of each lap recurrence. The infinite lap formulas follow from the proof, not from the finite tests. The first four lap counts are \((4,14,48,164)\) and \((4,10,28,76)\).

## Relationship to prior work
Lawnik and Berezowski (2022) introduced and explored this exact M-map, giving numerical bifurcation and Lyapunov evidence; the four-branch formulas and original dynamical motivation are theirs. Misiurewicz and Szlenk established the general lap-growth method for piecewise-monotone entropy. Here the additional conclusions are two natural postcritically finite parameter identifications, their full transition matrices, exact all-iterate lap recurrences, and two algebraic topological-entropy values. These are not consequences of the originating paper's finite numerical Lyapunov plots alone.

## Limitations
No formula for the whole parameter interval, no global parameter monotonicity, no invariant density, and no claim about chaotic cryptographic security is made. Topological entropy does not equal a typical Lyapunov exponent in general. The proofs are specific to the two stated critical-contact values. Unindexed equivalent calculations remain a publication-priority risk; an independent mathematical review has not been performed.

## References
1. M. Lawnik and M. Berezowski, *New Chaotic System: M-Map and Its Application in Chaos-Based Cryptography*, Symmetry **14** (2022), 895, DOI: 10.3390/sym14050895 (first public 2022-04-27).
2. M. Misiurewicz and W. Szlenk, *Entropy of piecewise monotone mappings*, Studia Mathematica **67** (1980), DOI: 10.4064/sm-67-1-45-63.
