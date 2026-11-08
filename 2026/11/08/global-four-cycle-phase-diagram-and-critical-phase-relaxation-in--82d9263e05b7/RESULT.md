# Global four-cycle phase diagram and critical phase relaxation in a negative-feedback limit map

## Finding

For every \(m,b>0\), consider the map
\[
 F_{m,b}(x,y)=\left(y,\frac{b}{1+x^m}\right),\qquad (x,y)\in(0,\infty)^2.
\]
There is exactly one fixed point \(E=(u,u)\), where \(u+u^{m+1}=b\). If \(0<m\leq1\), or \(m>1\) with \(b<b_c(m)=m(m-1)^{-1-1/m}\), every positive trajectory converges to \(E\). The same global convergence holds at \(b=b_c(m)\). At that boundary the fixed point has multipliers \(i\) and \(-i\), giving a neutral 1:4 resonance; nevertheless convergence is global. For every initial point \((x,y)\), put \(\sigma_x=\operatorname{sgn}(x-u)\) and \(\sigma_y=\operatorname{sgn}(y-u)\). With
\[
 A_m=u\sqrt{\frac{3}{m^2-1}},\qquad
 R=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
for each \(j\in\{0,1,2,3\}\) one has the global four-phase law
\[
 \lim_{n\to\infty}\sqrt n\,\left(F_{m,b}^{4n+j}(x,y)-E\right)
 =A_m R^j(\sigma_x,\sigma_y)^\top.
\]
This includes initial points on either exceptional axis, with the corresponding sign set to zero.

For \(m>1\), \(b>b_c(m)\), there are unique numbers \(0<L<u<H\) satisfying \(h(L)=H\) and \(h(H)=L\), where \(h(t)=b/(1+t^m)\). Besides \(E\) there are exactly two primitive four-cycles, and no other periodic orbits:
\[
 \mathcal A:\ (L,L)\mapsto(L,H)\mapsto(H,H)\mapsto(H,L)\mapsto(L,L),
\]
\[
 \mathcal S:\ (u,L)\mapsto(L,u)\mapsto(u,H)\mapsto(H,u)\mapsto(u,L).
\]
The first is attracting; the second has one expanding and one contracting four-step direction. Every point off the coordinate axes \(x=u\) and \(y=u\) is attracted to \(\mathcal A\) in its four-phase itinerary; every point on exactly one such axis approaches \(\mathcal S\), and their intersection is \(E\). Thus the unique physical probability (relative to planar Lebesgue measure) is the uniform orbit measure of \(\mathcal A\) above threshold and \(\delta_E\) at and below threshold. Above threshold all invariant Borel probabilities are convex combinations of the uniform measures on \(\mathcal A\), \(\mathcal S\), and \(\delta_E\); at and below threshold the only invariant Borel probability is \(\delta_E\).

## Assumptions and scope

The real power \(x^m\) is evaluated only for \(x>0\); both parameters are strictly positive. All statements concern the exactly specified \(\tau\to\infty\) *rational limit* of the tropically discretized feedback system, not a finite-step-size map and not its distinct max-plus limit. Convergence to a cycle means convergence of the four residue subsequences to the corresponding orbit points. A physical probability is one whose basin of convergence of empirical measures has positive planar Lebesgue measure.

## Proof

**1. Coordinate decoupling and scalar recurrence.** Set \(h(t)=b/(1+t^m)\). Direct composition gives
\[
 F^2(x,y)=(h(x),h(y)),\qquad F^4(x,y)=(h^2(x),h^2(y)).
\]
The scalar map \(h\) is positive and strictly decreasing. Its fixed point is the unique positive root of \(u+u^{m+1}=b\). The map \(h^2\) is strictly increasing and bounded, so for any \(v>0\) its iterates form a monotone bounded sequence (increasing if \(h^2(v)>v\), decreasing if the reverse holds), converging to a fixed point of \(h^2\). Every periodic point of \(h^2\) is therefore fixed. Thus every periodic point of \(F\) is fixed by \(F^4\): it has period one or four; no primitive period-two points can occur because \(h\) has just one fixed point.

**2. Unique scalar two-cycle and sharp threshold.** Suppose \(L<H\), \(h(L)=H\), and \(h(H)=L\). Subtracting the two equations gives
\[
 H-L=LH\bigl(H^{m-1}-L^{m-1}\bigr).
\]
For \(m\leq1\) this is impossible. For \(m>1\), set \(L=re^{-s}\), \(H=re^s\), \(s>0\). The exchange equations are equivalent to
\[
 r^m=\frac{\sinh s}{\sinh((m-1)s)},\quad
 b=B_m(s):=
 \frac{(\sinh s)^{1/m}\sinh(ms)}{(\sinh((m-1)s))^{1+1/m}}.
\]
Conversely, these formulas give a positive two-cycle for every \(s>0\). The function \(Q(t)=t\coth t\) for \(t>0\) is strictly increasing and strictly convex, since
\[
 Q'(t)=\frac{\sinh t\cosh t-t}{\sinh^2t}>0,\qquad
 Q''(t)=2\operatorname{csch}^2t\,(Q(t)-1)>0.
\]
Logarithmic differentiation yields
\[
 m s\frac{B_m'(s)}{B_m(s)}
 =Q(s)+mQ(ms)-(m+1)Q((m-1)s).
\]
If \(1<m<2\), both \(Q(s)>Q((m-1)s)\) and \(Q(ms)>Q((m-1)s)\), making the derivative positive. If \(m\geq2\), convexity at \((m-1)s=[s+(m-2)ms]/(m-1)\) implies that the expression is bounded below by \(2[Q(ms)-Q(s)]/(m-1)>0\). Thus \(B_m\) is strictly increasing. Its endpoint limits are
\[
 B_m(0+)=m(m-1)^{-1-1/m}=b_c(m),\qquad B_m(+\infty)=+\infty.
\]
For \(m=2\), this reduces to the explicit law \(b_c(2)=2\), \(LH=1\), and \(L,H=(b\mp\sqrt{b^2-4})/2\) for \(b>2\), giving exact counterparts of the previously tabulated logarithmic cycle coordinates. This proves existence and uniqueness of the scalar primitive two-cycle exactly above \(b_c(m)\). At its birth the two points coincide with the unique fixed point \(u=(m-1)^{-1/m}\).

**3. Basin and multiplier classification.** For \(b>b_c(m)\), the fixed points of \(h^2\) are exactly \(L,u,H\). The derivative at the scalar two-cycle is
\[
 \mu=h'(L)h'(H)
 =\left(\frac{m\sinh s}{\sinh(ms)}\right)^2\in(0,1),
\]
because \(\sinh(ms)>m\sinh s\) for \(m>1\) and \(s>0\). The fixed-point derivative has magnitude \(d=m u^m/(1+u^m)>1\), by \(u>(m-1)^{-1/m}\) for \(b>b_c\). Hence \((h^2)'(L)=(h^2)'(H)=\mu<1\) and \((h^2)'(u)=d^2>1\). The continuous function \(h^2(v)-v\) has no other zeros, is positive near zero, and is negative for sufficiently large \(v\); the signs therefore alternate across these simple zeros. Monotone bounded iteration gives
\[
 \lim_{n\to\infty}h^{2n}(v)=
 \begin{cases}L,&v<u,\\u,&v=u,\\H,&v>u.\end{cases}
\]
Below threshold there is only the scalar fixed point, so every scalar and planar trajectory converges to \(u\) and \(E\). At threshold the same holds: the sole fixed point of the increasing bounded map \(h^2\) is \(u\). The identity for \(F^4\) then gives all nine period-four fixed points in the supercritical case, partitioned into the fixed point and the two stated four-cycles. The stable four-cycle has four-step eigenvalues \((\mu,\mu)\); the other has \((\mu,d^2)\). The basins follow from the scalar limit law.

**4. Critical four-phase law.** At \(b=b_c(m)\), write \(x=u(1+z)\), so the normalized scalar map is
\[
 g(1+z)=\frac{m}{m-1+(1+z)^m}.
\]
Expansion at zero gives
\[
 g(1+z)=1-z+\frac{3-m}{2}z^2-\frac{(m-7)(m-2)}6 z^3+O(z^4),
\]
so direct composition gives
\[
 g^2(1+z)=1+z-\frac{m^2-1}{6}z^3+O(z^4).
\]
For \(z_n=g^{2n}(1+z_0)-1\ne0\), monotonicity of \(h^2\) preserves its sign and the global convergence above gives \(z_n\to0\). Consequently
\[
 \frac1{z_{n+1}^2}-\frac1{z_n^2}
 =\frac{m^2-1}{3}+O(|z_n|).
\]
Cesàro averaging proves \(nz_n^2\to3/(m^2-1)\). The exact-zero trajectory remains zero. Apply this independently to the two coordinates of \(F^{4n}\). The Jacobian of \(F\) at the critical fixed point equals \(R\). Its four finite iterates are differentiable, and the error from linearizing around \(E\) is \(O(\|F^{4n}(x,y)-E\|^2)\). Multiplication by \(\sqrt n\) makes that error vanish, proving the four-phase formula for every initial point.

**5. Invariant probabilities.** Every positive orbit approaches the finite periodic set specified above. Conversely, if a point is recurrent under \(F\), one may select a returning subsequence whose iteration counts are all congruent modulo four. That subsequence converges to a point of the classified periodic set, so recurrence forces the original point itself to belong to that set. Poincaré recurrence then forces every invariant Borel probability to be supported on the identified finite periodic set. Invariance makes its weights uniform along each cycle. The basin partition shows that the attracting four-cycle has full planar Lebesgue measure above threshold (the two exceptional axes are null); below and at threshold all empirical distributions converge to \(\delta_E\). This proves the invariant and physical-measure assertions.

## Verification

The accompanying standalone `verification.py` uses the Python 3 standard library. Running `python3 verification.py` completed 391 checks: exact rational four-cycle transitions and multipliers; exact cubic-return Taylor coefficients for nine integer exponents; exchange equations and multipliers for noninteger and integer exponents; finite-time critical-rate comparisons; and the four-step composition identity. Tests are finite corroboration, not proof of universal parameter or measure statements. The displayed analytical argument establishes the quantified assertions.

## Relationship to prior work

Gibo and Ito (2015) introduced the underlying negative-feedback discretization and studied the onset of oscillations. Ohmori and Yamazaki's preprint (first public May 10, 2023) addresses discrete and max-plus negative-feedback models. Yamazaki and Ohmori (2023), in the openly readable full article, write the exact rational \(\tau\to\infty\) map as their equation (11), and numerically report eight four-step fixed points for \(m=2,b=10\), grouped into stable and unstable four-cycles. Those constructions and the example are prior art, not claimed here. Their discussion does not supply the present all-parameter one-to-three ergodic-measure transition, complete basin partition, hyperbolic parametrization, or the global signed critical four-phase relaxation limit.

## Limitations

Only the exactly defined infinite-time-step rational map on the positive quadrant is classified. No conclusion is claimed about finite \(\tau\), about the different max-plus map, or about rate of convergence to an attracting cycle away from the critical parameter. The earliest full text of the May 2023 preprint and the 2015 founding paper could not be independently read in full; publication-priority comparison with those versions remains a residual risk. The mathematical review described in the companion review file is not an independent external audit.

## References

- S. Gibo and H. Ito, "Discrete and ultradiscrete models for biological rhythms comprising a simple negative feedback loop," *Journal of Theoretical Biology* **378** (2015), 89–95, DOI: `10.1016/j.jtbi.2015.04.024`.
- S. Ohmori and Y. Yamazaki, "Dynamical properties of discrete negative feedback models," arXiv:`2305.05908`, first publicly posted 2023-05-10.
- Y. Yamazaki and S. Ohmori, "Emergence of ultradiscrete states due to phase lock caused by saddle-node bifurcation in discrete limit cycles," *Progress of Theoretical and Experimental Physics* **2023** (8), 081A01, DOI: `10.1093/ptep/ptad099`, especially §3(vi), equations (11)–(12) and Table 1.
