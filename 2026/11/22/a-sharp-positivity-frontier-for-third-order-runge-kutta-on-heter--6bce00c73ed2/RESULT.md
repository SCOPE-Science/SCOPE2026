# A sharp positivity frontier for third-order Runge–Kutta on heterogeneous directed triangles

## Finding
Let \(a,b,c>0\). For the continuous-time Markov generator of a one-way directed three-cycle (row convention),
\[
Q=\begin{pmatrix}-a&a&0\\0&-b&b\\c&0&-c\end{pmatrix},
\qquad P(h)=I+hQ+\frac{h^2}{2}Q^2+\frac{h^3}{6}Q^3,\quad h\ge0.
\]
The polynomial step is exactly the end-step produced by the classical explicit three-stage, third-order SSP Runge–Kutta method applied to \(u'=Qu\). Set
\[
S=a+b+c,\quad M=\max\{a,b,c\},\quad D=abc,\quad H=\frac3S,
\]
and introduce
\[
r(z)=1-z+\frac{z^2}{2}-\frac{z^3}{6},\qquad
G(h)=r(Mh)+\frac{Dh^3}{6},\qquad \Phi=G(H).
\]
**Complete sharp classification.** If \(\Phi\ge0\), \(P(h)\) is entrywise nonnegative precisely for \(0\le h\le H\). If \(\Phi<0\), \(G\) has exactly one root \(h_*\) in \((0,H)\), and \(P(h)\) is entrywise nonnegative precisely for \(0\le h\le h_*\). For every \(h>H\), each of the three counter-directed transitions is negative, so positivity never returns. All same-direction transitions are strictly positive for \(h>0\); among the diagonal entries the first to become negative always corresponds to a state with maximum exit rate \(M\).

This is a two-regime, all-positive-rate exact positivity horizon; the threshold is a simple expression or the unique indicated cubic root, never an unqualified numerical approximation. In the natural one-parameter family \((a,b,c)=(t,1,1)\), \(t\ge1\), the regime switches at the unique root \(t_c>1\) of
\[
4t_c^3-6t_c^2-9t_c-16=0,\qquad t_c\approx2.80835414560089.
\]
For \(1\le t\le t_c\) the sharp horizon is \(3/(t+2)\); for \(t>t_c\), the strictly smaller horizon is the unique root of \(G\) below \(3/(t+2)\). Except in the uniform-rate case, this positivity horizon strictly exceeds the universal forward-Euler/SSP guarantee \(1/M\).

## Assumptions and scope
There are exactly three states, with cyclic one-way transitions of positive arbitrary real rates \(a,b,c\). Matrices act on column observables by \(u'=Qu\), and \(Q\) has zero **row** sums. Equivalently, row probability distributions evolve by right multiplication with \(P(h)\). Every assertion is entrywise and concerns the completed numerical step, not the sign of internal stage vectors, numerical stability against arbitrary perturbations, or floating-point rounding.

The third-order RK scheme has linear stability polynomial \(R(z)=1+z+z^2/2+z^3/6\), hence \(P(h)=R(hQ)\). Since \(P(h)\mathbf1=\mathbf1\), nonnegative entries are equivalent to a stochastic end-step in the row convention.

## Proof
**1. All nine entries.** Let \((x,y,z)\) be any cyclic permutation of \((a,b,c)\), with state \(i\) having exit rate \(x\), its successor having exit rate \(y\), and its predecessor having exit rate \(z\). Direct expansion of the first three matrix powers gives
\[
\begin{aligned}
P_{ii}(h)&=r(xh)+\frac{Dh^3}{6},\\
P_{i,i+1}(h)&=\frac{xh}{6}\bigl(6-3(x+y)h+(x^2+xy+y^2)h^2\bigr),\\
P_{i,i+2}(h)&=\frac{xyh^2}{6}(3-Sh),
\end{aligned}
\]
with indices modulo three. The expansion is exact, including the return circuit \(D\) in the diagonals.

**2. Only two possible obstructions.** For positive \(x,y\), the discriminant of the forward-transition quadratic is
\[
9(x+y)^2-24(x^2+xy+y^2)=-15x^2-6xy-15y^2<0.
\]
With positive leading coefficient and constant term, the quadratic is strictly positive for every real \(h\). Thus the forward entries are strictly positive whenever \(h>0\). The three reverse entries are simultaneously nonnegative exactly for \(0\le h\le H=3/S\), and strictly negative after \(H\).

Moreover,
\[
r'(z)=-\frac{(z-1)^2+1}{2}<0 \quad(z\in\mathbb R).
\]
The same positive return term \(Dh^3/6\) occurs in each diagonal entry, so for \(h>0\) the smallest diagonal equals \(G(h)=r(Mh)+Dh^3/6\). In particular an earliest diagonal failure is always at a fastest-exit state, irrespective of cyclic ordering.

**3. Exact single-crossing theorem inside the reverse-edge interval.** Write \(t=h/H\), \(x=M/S\in[1/3,1)\), and use the degree-three Bernstein basis. A direct coefficient conversion gives
\[
G(Ht)= (1-t)^3+3(1-x)t(1-t)^2
 +3\left(1-2x+\frac32x^2\right)t^2(1-t)+\Phi t^3.
\]
The first three Bernstein coefficients are strictly positive for \(x\in[1/3,1)\), since
\[
1-x>0,\qquad 1-2x+\frac32x^2=\frac13+\frac32(x-2/3)^2>0.
\]
When \(\Phi\ge0\), this representation proves \(G(h)>0\) for \(0\le h<H\) and \(G(H)=\Phi\ge0\), including the boundary case of a zero diagonal.

When \(\Phi<0\), transform \(t=u/(1+u)\) for \(u>0\), obtaining
\[
(1+u)^3G\!\left(\frac{Hu}{1+u}\right)
=1+3(1-x)u+3\left(1-2x+\frac32x^2\right)u^2+\Phi u^3.
\]
Its coefficient signs are \(+,+,+,-\) in ascending order, so Descartes' rule applied in descending order gives exactly one positive real root, counting multiplicity. The polynomial is positive at \(u=0\) and negative for sufficiently large \(u\), making that root simple and its sign transition unique. Mapping back establishes \(G(h)>0\) below the one root \(h_*\in(0,H)\) and \(G(h)<0\) above it through \(H\). Thus there is one initial closed positivity interval in either regime; no later positivity is possible because reverse entries are negative for all \(h>H\).

**4. Explicit one-parameter boundary and comparison with SSP.** For \((a,b,c)=(t,1,1)\) with \(t\ge1\), substitute \(S=t+2\), \(M=t\), \(D=t\) into \(\Phi\), yielding
\[
\Phi=-\frac{4t^3-6t^2-9t-16}{2(t+2)^3}.
\]
The numerator is negative at \(t=1\), becomes positive for large \(t\), and its derivative \(12t^2-12t-9\) is positive for every \(t\ge3/2\). On \([1,3/2]\) the numerator is negative (indeed it decreases until its unique positive turning point), so there is exactly one root for \(t\ge1\). This proves the specified phase transition.

Forward Euler is nonnegative exactly for \(0\le h\le1/M\). Since \(S\le3M\), \(H\ge1/M\), with equality precisely when all three rates are equal. At \(h=1/M\), every reverse transition is nonnegative and
\[
G(1/M)=r(1)+\frac{D}{6M^3}=\frac13+\frac{D}{6M^3}>0.
\]
If the rates are not all equal, then \(1/M<H\) and continuity together with the strict sign frontier proves that the sharp RK3 endpoint positivity horizon is strictly larger than the forward-Euler limit.

## Verification
The standalone `verify.py` requires only Python 3's standard library. Run `python3 verify.py` in the extracted package directory; success prints `VERIFY_OK exact_checks 11797 rate_triples 343`. It reconstructs the cubic polynomial directly from exact rational matrix powers for all 343 integer rate triples \((a,b,c)\in\{1,\ldots,7\}^3\), checks closed-form entries, row sums, reverse-edge cutoff, maximal-rate diagonal obstruction, branch tests, and exact-rational brackets on the interior root when present. These finite checks do **not** prove the assertions for arbitrary positive real rates; the displayed identities, discriminant, Bernstein representation, and single-root argument supply that proof.

For a concrete comparison, at rates \((2,1,1)\) the frontier is \(h=3/4\), while the forward-Euler guarantee is only \(1/2\). At rates \((3,1,1)\) the diagonal obstruction dominates: \(\Phi=-11/250<0\), so the exact frontier is the unique root of \(G\) below \(3/5\).

## Relationship to prior work
The fundamental SSP analysis of Gottlieb, Shu and Tadmor gives the usual sufficient positivity condition by convex forward-Euler steps (and explicitly documents the three-stage, third-order method). It does not give an exact all-rate stochasticity horizon for this specific directed triangular Markov generator. In particular, the proven strict improvement beyond \(1/M\) concerns **completed-step** positivity only, not the universal SSP coefficient or intermediate-stage positivity.

Horváth's 2004/2005 analysis determines class-uniform positivity thresholds for Runge–Kutta schemes and discusses invariant cones and selected initial vectors. Its full 16-page text was inspected. The results use quantifiers over classes of right-hand sides and fixed schemes rather than the present exact entrywise, all-rate characterization of a particular irreducible three-cycle. Neither class-uniform threshold nor scalar stability alone entails the two-regime boundary proved here.

Nüßlein, Ranocha and Ketcheson study *adaptable endpoint weights* for SSPRK(3,3), including an equal-rate three-state absorbing pure-birth example and a sharp feasibility barrier for a **second-order adjustable-weight family**. That is not a fixed third-order stability polynomial on a closed, heterogeneous, irreducible cycle. Closely related exact research on Crank–Nicolson for heterogeneous directed cycles concerns a rational Cayley update rather than this degree-three explicit RK polynomial; its fastest-exit mechanism is acknowledged, and is not claimed newly in general. A separate published RK3 calculation on complete multipartite **undirected** diffusion graphs cannot imply the orientation-specific formulas here.

## Limitations
The theorem is exact in real arithmetic, only for three-state one-way cycles, and only for the completed classical RK3 step. It makes no claim about all three-state Markov generators with bidirectional or additional arcs, other RK polynomials, order accuracy at large steps, contractivity in nonstandard norms, stagewise positivity, or practical time-step adaptivity. The positivity frontiers are non-reentrant on this generator class, but this does not establish that property for other networks. Equivalent specializations in older Runge–Kutta positivity literature remain a bibliographic-priority risk; the closest inspected texts have different claims or quantifiers. Independent validation of this mathematical result has not been performed.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, first online 2 February 2001. https://doi.org/10.1137/S003614450036757X ; author's accessible full PDF: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, available online 27 October 2004. https://doi.org/10.1016/j.apnum.2004.08.026
3. S. Nüßlein, H. Ranocha and D. I. Ketcheson, *Positivity-Preserving Adaptive Runge–Kutta Methods*, arXiv:2005.06268v1 (13 May 2020). https://arxiv.org/abs/2005.06268
4. *A sharp three-state feasibility barrier for second-order adaptive SSPRK(3,3) weights*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-three-state-feasibility-barrier-for-second-order-adaptiv--1180efbbc2f7
5. *A fastest-exit positivity frontier for Crank–Nicolson on directed cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-fastest-exit-positivity-frontier-for-crank-nicolson-on-directe--d34a4ad012e9
