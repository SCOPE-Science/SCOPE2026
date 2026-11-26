# Sharp period-two multiplicity and bistability in a fixed-point-free quadratic gap map

## Finding
For every \(a,b,c\in(0,1)\), the two-branch map below has at most **three distinct primitive period-two orbits**. The bound is sharp: at \((a,b,c)=(1/5,1/10,17/200)\) it has exactly three, **two linearly attracting and one repelling**. All three orbits and their multipliers are specified by an exact quartic reduction. In particular, two attracting cycles coexist in an open parameter region although there are no fixed points anywhere on the state interval.

## Assumptions and scope
Consider the map \(F:[0,1]\to[0,1]\),
\[
F(x)=\begin{cases}1-(1-a)\left(\frac{b-x}{b}\right)^2,&0\le x\le b,\\ c\left(\frac{x-b}{1-b}\right)^2,&b<x\le1,\end{cases}
\qquad a,b,c\in(0,1).
\]
This is the exponent-\(2\) member of the polynomial family introduced in Lawnik–Moysis–Volos (2023), Equation (15). The value at the switching point \(x=b\) belongs to the **left** branch, so \(F(b)=1\). "Primitive period two" means a pair of distinct states \((x,y)\) with \(F(x)=y\), \(F(y)=x\). Stability means that the derivative of the smooth local second iterate at the orbit is strictly below or above one in modulus, respectively. No claims are made about longer periods, global basins, topological entropy, or cryptographic security.

## Proof
**1. Branch order and all possible two-cycles.** On the left branch \(F(x)>x\): the difference is a concave quadratic in \(x\), positive at both endpoints \(x=0\) and \(x=b\). On the open right branch \(F(x)<x\): the difference extends to a convex quadratic on \([b,1]\), strictly negative at its endpoints, hence also in its interior. Thus no fixed point exists. If \(x<y\) is a primitive period-two orbit, its forward upward step must start in the left branch and its downward step in the right: \(0\le x\le b<y\le1\). Every two-cycle has exactly this order.

**2. Exact bijection with a quartic.** Set \(t=(b-x)/b\), so \(0\le t\le1\). The two-cycle equations become
\[
x=b(1-t),\quad y=1-(1-a)t^2,\quad
H(t):=\frac{c}{(1-b)^2}\bigl((1-b)-(1-a)t^2\bigr)^2-b(1-t)=0.
\]
The additional and necessary condition is \(y>b\); under it, \(H(t)=0\) is exactly \(F(y)=x\). Conversely, every such admissible root gives exactly one primitive period-two orbit, and distinct roots give distinct orbits. Boundary points \(t=0\) are permitted if the equations hold, but inadmissible roots with \(y\le b\) are excluded.

**3. A global three-orbit upper bound.** Direct differentiation gives
\[
H'(t)=b-\frac{4c(1-a)}{(1-b)^2}\,t\bigl((1-b)-(1-a)t^2\bigr),\qquad
H''(t)=-\frac{4c(1-a)}{(1-b)^2}\bigl((1-b)-3(1-a)t^2\bigr).
\]
For \(t\ge0\), \(H''\) changes sign at most once, from negative to positive. Consequently \(H'\) decreases then increases, and has at most two zeros on \([0,1]\). Rolle's theorem implies that \(H\) has at most three distinct zeros there, hence at most three primitive two-cycles. The quartic is never identically zero since its leading coefficient is strictly positive.

**4. Exact sharpness witness.** Take \((a,b,c)=(1/5,1/10,17/200)\). Then \(a>b\), so every \(t\in[0,1]\) satisfies \(y=1-(1-a)t^2\ge a>b\), and no root is discarded by admissibility. The quartic reduces to
\[
H(t)=\frac{1088t^4-2448t^2+1620t-243}{16200}.
\]
Its exact signs are
\[
H(0)=-\frac3{200}<0,\qquad H(1/4)=\frac{53}{64800}>0,\qquad H(3/5)=-\frac{87}{125000}<0,\qquad H(1)=\frac{17}{16200}>0.
\]
Therefore there is a root in each of the three disjoint intervals \((0,1/4)\), \((1/4,3/5)\), and \((3/5,1)\). Step 3 shows there can be no others.

**5. Stability and openness.** On a two-cycle, the second-return multiplier equals
\[
m(t)=F'_R(y)F'_L(x)=\frac{4c(1-a)t(y-b)}{b(1-b)^2}>0,\qquad H'(t)=b\bigl(1-m(t)\bigr).
\]
The three sign-changing roots of the displayed quartic are simple: otherwise their odd algebraic multiplicities would sum to at least five, impossible for degree four. The first and third have positive \(H'\), and the middle has negative \(H'\). Hence the first and third have \(0<m<1\) and are locally attracting, while the middle has \(m>1\) and is repelling. By the implicit-function theorem, the three simple orbits, their branch inequalities, and their hyperbolic types persist throughout a nonempty open neighborhood of this rational parameter triple. This proves sharpness and coexistence.

## Verification
The independent-of-third-party-dependencies script `verify_period2.py` checks the exact rational quartic coefficients, all four sign values, and each two-cycle's admissibility and return multiplier by 95 exact rational bisections per root. Execute `python3 verify_period2.py`; expected leading line is `EXACT_RATIONAL_THREE_PERIOD_TWO_ORBITS_AND_TWO_SINKS_OK`. Analytically, the upper bound and stability conclusions follow from Steps 1–5, not from finite bisection.

## Relationship to prior work
Lawnik, Moysis, and Volos introduced this polynomial no-equilibrium family and proved absence of fixed points for exponents at least one. Their analysis emphasizes parameter-space plots of Lyapunov exponents, phase diagrams, and applications to pseudorandom generation. The present statement addresses a distinct exact question: the maximum number and simultaneous stability types of the first possible periodic orbits. The classical piecewise-**affine** gap-map literature analyzes period-two cycles, but its affine return equations do not establish the sharp cubic-derivative bound or the three-cycle coexistence in this quadratic family. A subsequent paper by some of the same authors studies a different projection construction of no-fixed-point maps; its potential relevance is acknowledged, without claiming priority beyond inspected material.

## Limitations
The quartic criterion characterizes primitive period-two cycles only. It does not classify higher periods or invariant measures, nor does it imply that every initial condition converges to one of the two locally attracting cycles. The exact rational witness establishes an open region of bistability, not a complete bifurcation diagram in all three parameters. While the cited source's relevant mathematical statements were checked, an equivalent formulation in more general discontinuous-map theory may exist; independent priority review remains outstanding.

## References
1. M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, DOI: [10.3390/sym15071311](https://doi.org/10.3390/sym15071311), especially Equation (15), Lemma 1, Figures 3–5 (first public release 27 June 2023).
2. S. J. Hogan, L. Higham, T. C. L. Griffin, *Dynamics of a piecewise linear map with a gap*, Proc. R. Soc. A **463** (2007), 49–65, DOI: [10.1098/rspa.2006.1735](https://doi.org/10.1098/rspa.2006.1735).
3. M. Lawnik, L. Moysis, M. S. Baptista, C. Volos, *Discrete one-dimensional piecewise chaotic systems without fixed points*, Nonlinear Dynamics **112** (2024), 6679–6693, DOI: [10.1007/s11071-024-09349-6](https://doi.org/10.1007/s11071-024-09349-6).
