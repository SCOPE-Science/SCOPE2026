# A symmetry-breaking three-cycle guarantee for antiphase Ricker competition

## Finding

For every \(L>2\), the family
\[
T_{L,c}(x,y)=\bigl(Rxe^{-x-cy},\;Rye^{-cx-y}\bigr),\qquad R=e^{(1+c)L},
\]
with \(c>0\), has a positive coexistence equilibrium at \((L,L)\). Define \(t_L\in(0,1)\) by
\[
\frac{\operatorname{artanh}(t_L)}{t_L}+\frac1{1-t_L^2}=L,
\qquad c_*(L)=1-\frac{2\operatorname{artanh}(t_L)}{Lt_L}.
\]
The defining equation has exactly one root; \(0<c_*(L)<1-2/L\).

**Theorem.** For every \(L>2\) and every \(0<c<c_*(L)\), the map \(T_{L,c}\) has at least **three distinct positive primitive period-two orbits whose two species move in opposite directions**. One has equal amplitudes, while the other two have unequal amplitudes and are exchanged by swapping the species. The coupling \(c_*(L)\) is the unique point of derivative \(-1\) on the equal-amplitude scalar branch. This is a sufficient full-interval multiplicity theorem, not a complete census above the threshold.

## Assumptions and scope

We use positive real state variables, positive equal intraspecific coefficients (normalized to one), equal cross-interaction coefficient \(c\), equal intrinsic multiplier \(R\), and real \(L>2\). A *strictly antiphase primitive two-cycle* is an unordered pair of distinct positive states with changes in the coordinates of opposite nonzero signs. The two species-exchanged unequal-amplitude cycles are counted as distinct spatial orbits, not as different starting phases of one orbit.

## Proof

**1. Exact reduction.** Adding the logarithmic growth equations over a two-cycle shows that the midpoint of each coordinate is \(L\). Thus any strictly antiphase cycle can be written (after choosing the phase of the first species) as
\[
(L+u,L-w)\longleftrightarrow(L-u,L+w),\qquad 0<u,w<L.
\]
Using \(\log[(L-u)/(L+u)]=-2\operatorname{artanh}(u/L)\), the two map equations are **equivalent**, not just necessary, to
\[
A_L(u)=cw,\qquad A_L(w)=cu,\qquad
A_L(v)=v-2\operatorname{artanh}(v/L).
\]
All these equations make sense on \((0,L)\). Conversely each positive pair satisfying them constructs an exact cycle; neither state is a fixed point because \(u,w>0\).

**2. Uniqueness and positivity of the threshold.** Set
\[
\Phi(t)=\frac{\operatorname{artanh}t}{t}+\frac1{1-t^2},\quad 0<t<1.
\]
Both summands increase strictly, \(\Phi(0+)=2\), and \(\Phi(1-)=+\infty\). Thus every \(L>2\) determines one \(t_L\). Since \(\operatorname{artanh}(t)/t<1/(1-t^2)\), the equation \(\Phi(t_L)=L\) gives
\[
0<\frac{1/(1-t_L^2)-\operatorname{artanh}(t_L)/t_L}{L}=c_*(L).
\]
Moreover \(\operatorname{artanh}(t_L)/t_L>1\), so \(c_*(L)<1-2/L\).

**3. Equal-amplitude branch and its exact threshold.** Fix \(0<c<1-2/L\), and define \(f(v)=A_L(v)/c\). The ratio
\[
\frac{2\operatorname{artanh}(v/L)}{v}
\]
increases continuously from \(2/L\) to infinity, so there is a unique \(q\in(0,L)\) such that \(f(q)=q\), or equivalently \(2\operatorname{artanh}(q/L)/q=1-c\). This produces the equal-amplitude antiphase orbit. Differentiating gives
\[
f'(q)=\frac{1-2/[L(1-(q/L)^2)]}{c},\qquad
f'(q)+1=\frac{2-\Phi(q/L)}{c}.
\]
Since \(q\) increases strictly as \(c\) decreases, \(f'(q)=-1\) occurs only when \(q=Lt_L\), equivalently \(c=c_*(L)\). For all \(0<c<c_*(L)\), \(f'(q)<-1\).

**4. Additional cycles from an intermediate-value argument.** The function \(A_L\) is positive for sufficiently small positive \(v\), strictly concave for \(0<v<L\), and has a unique positive zero \(z\in(0,L)\) in addition to the zero at the origin, because its derivative starts positive, decreases strictly and tends to \(-\infty\). In fact \(q<z\). On \((0,q)\) we have \(f(v)>v>0\). Define \(H(v)=f(f(v))-v\) wherever \(f(v)<z\). Since \(f'(0)=(1-2/L)/c>1\), \(H(v)>0\) for all sufficiently small positive \(v\). Also \(H'(q)=f'(q)^2-1>0\), so wherever \(H\) is defined near \(q\) it is strictly negative immediately to its left.

If \(f(v)<z\) throughout \((0,q)\), continuity gives a zero \(u\in(0,q)\). Otherwise let \(v_0\) be the first point where \(f(v_0)=z\); it exists with \(0<v_0<q\), and \(H(v_0)=f(z)-v_0=-v_0<0\), while \(H\) is continuous on \([0,v_0]\). In either case an intermediate-value zero \(u\in(0,q)\) exists with \(w=f(u)\in(0,z)\) and \(f(w)=u\). Since \(f(v)>v\) for \(0<v<q\), we have \(w>u\). If \(w<q\), then \(u=f(w)>w\), a contradiction. Hence \(0<u<q<w<z<L\).

Thus the unequal positive amplitudes \((u,w)\) solve \(A_L(u)=cw\), \(A_L(w)=cu\), and so does \((w,u)\). They provide the two distinct species-exchanged primitive antiphase orbits. Neither equals the equal-amplitude orbit because \(u\ne w\); the two unequal orbits cannot coincide, since their high-first-species states have distinct first-coordinate amplitudes. This proves the three-orbit guarantee for all stated parameters. \(\square\)

## Verification

The exact reduction and intermediate-value proof above supply the universal statement. A supplementary high-precision checker in `verify_antiphase.py` reconstructs the analytic threshold, both unequal-amplitude solutions, the equal-amplitude solution, and all three two-step map identities for two parameter choices. The finite tests cannot prove the universal theorem. Invoke `python verify_antiphase.py` with Python and `mpmath` installed.

## Relationship to prior work

Goldar et al. (2026) study the same two-species Ricker map, equilibrium bifurcations and selected period-two orbits, but do not supply this full-parameter lower bound of three distinct antiphase cycles in the equal-coupling family. Kulakov, Neverova and Frisman (2022) analyze phase multistability and pitchfork and saddle-node transitions, chiefly through numerical nullcline iteration; their relevant sections do not give this implicit analytic coupling boundary or the all-\(L\) three-orbit guarantee. Prior general analytic criteria that guarantee the existence of a single antiphase orbit do not imply a count of three. The contribution is an explicit rigorous multiplicity region, not the discovery of antiphase oscillation or symmetry breaking as qualitative phenomena.

## Limitations

The number **at least three** is not claimed to be exact. We do not assert nonexistence of unequal-amplitude antiphase cycles for \(c\ge c_*(L)\), or determine the stability, basins or period-four dynamics. The threshold is exact for the multiplier on the equal-amplitude scalar branch only. The theorem treats exactly symmetric growth and competition with \(L>2\); no corresponding assertion is made for unequal interactions. A prior general theorem that implies the three-orbit guarantee would affect historical priority; no such coverage was found in the sources examined, but that is not a proof of novelty.

## References

1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society (first public 2026-09-16), DOI: 10.1155/ddns/7255117.
2. M. Kulakov, G. Neverova, and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics 10 (2022), 1076, DOI: 10.3390/math10071076.
