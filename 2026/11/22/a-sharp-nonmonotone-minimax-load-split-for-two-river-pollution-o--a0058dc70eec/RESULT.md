# A sharp nonmonotone minimax load split for two river pollution outfalls

## Finding

**Theorem (global minimax split and unique geometric transition).** Consider two outfalls at downstream travel times \(0\) and \(d>0\), supplying nonnegative biochemical oxygen-demand (BOD) increments totaling \(L>0\). Let \(w\in[0,1]\) be the upstream fraction. In the initially oxygen-saturated, no-settling Streeter–Phelps model with deoxygenation coefficient \(k>0\) and reaeration coefficient exactly \(2k\), write \(q=e^{-kd}\), so \(0<q<1\). The normalized dissolved-oxygen deficit is
\[
F_w(u)=w\left(e^{-u}-e^{-2u}\right)+(1-w)\mathbf 1_{\{u\ge kd\}}\left(e^{-(u-kd)}-e^{-2(u-kd)}\right),\qquad u\ge0.
\]
Set \(M(w,q)=\sup_{u\ge0}F_w(u)\). For every \(q\in(0,1)\), its **unique** minimizer on \([0,1]\) is
\[
w_*(q)=\begin{cases}
\dfrac{1}{2(1-q)},&0<q\le\dfrac13,\\[3pt]
\dfrac{1}{1+q},&\dfrac13\le q<1,
\end{cases}\qquad
\min_{0\le w\le1}M(w,q)=\begin{cases}
\dfrac{1}{8(1-q)},&0<q\le\dfrac13,\\[3pt]
\dfrac{q}{(1+q)^2},&\dfrac13\le q<1.
\end{cases}
\]
The two formulas agree at \(q=1/3\). As the separation increases from zero to infinity, the optimal upstream fraction rises strictly from the limiting value \(1/2\) to its maximum \(3/4\) at the **unique** switching separation \(kd=\log3\), then falls strictly to the limiting value \(1/2\). This nonmonotone optimal allocation is a global, not merely local, classification.

For \(0<q\le1/3\), the optimal profile has two equal global deficit maxima: one at \(u=\log2\) and one at \(u=\log[2(1-q)/q]\). For \(1/3<q<1\), it has a unique global maximum at \(u=\log[(1+q)/q]\); the upstream-only reach does not attain that value. Thus the threshold also marks the appearance of a second active worst-deficit location, although it need not mark every change in the total number of local maxima.

## Assumptions and scope

The flow is a uniform one-dimensional plug-flow river with constant downstream velocity, uniform strictly positive decay coefficient \(k\), and reaeration coefficient \(2k\). Upstream initial oxygen deficit is zero. The two BOD increments enter without direct instantaneous oxygen shock, flow dilution or change in reaction parameters. The assigned load \(L\) is a concentration-equivalent BOD input budget; the first and second increases are \(wL\) and \((1-w)L\). There is no settling, dispersion, photosynthetic forcing, sediment demand, or saturation clipping. Oxygen deficit is the difference between oxygen saturation and dissolved oxygen. The objective considers the entire unbounded downstream reach, not a finite list of compliance points. Physical feasibility of positive dissolved oxygen can be maintained by choosing a sufficiently small common load scale \(L\) without changing the optimal fraction.

For the underlying BOD concentration \(B\) and oxygen deficit \(D\), on each open reach the equations are \(B'=-kB\) and \(D'=kB-2kD\), with prime denoting derivative in travel time. At the second outfall, \(B\) jumps by \((1-w)L\), whereas \(D\) is continuous. Therefore \(D(t)=L F_w(kt)\). Rates with a different reaeration-to-deoxygenation ratio are **not** classified by this theorem.

## Proof

**1. Exact objective as two quadratic peaks.** Put \(z=e^{-u}\), so upstream of the second outfall \(z\in(q,1]\) and the deficit is \(w(z-z^2)\). Downstream \(z\in(0,q]\) and the deficit is
\[
F_w(u)=Az-Bz^2,\qquad A=w+\frac{1-w}{q},\quad B=w+\frac{1-w}{q^2}.
\]
Both coefficients are strictly positive, and the downstream quadratic is strictly concave. Its maximum occurs at \(z=A/(2B)\) when this lies in \((0,q]\), otherwise at \(z=q\). The upstream piece is \(w(z-z^2)\), which is at most \(w/4\). The two expressions agree continuously at \(u=kd\).

**2. Short or intermediate separation: \(1/3\le q<1\).** Set \(w_1=1/(1+q)\) and \(u_1=\log[(1+q)/q]>kd\). Direct substitution shows that the two single-source responses coincide at this fixed downstream point:
\[
e^{-u_1}-e^{-2u_1}=e^{-(u_1-kd)}-e^{-2(u_1-kd)}=\frac{q}{(1+q)^2}=:m_1.
\]
Hence \(F_w(u_1)=m_1\) **for every** allocation \(w\), establishing \(M(w,q)\ge m_1\). At \(w=w_1\), the downstream quadratic has \(A=2/(1+q)\), \(B=1/q\), and vertex \(z=q/(1+q)\), so its maximum is exactly \(m_1\). The upstream maximum is at most \(w_1/4=1/[4(1+q)]\le m_1\) exactly when \(q\ge1/3\). Thus \(w_1\) attains the lower bound globally. For uniqueness, at the **fixed** interior point \(u_1\),
\[
F_w'(u_1)=\frac{1-q}{(1+q)^2}\bigl(1-(1+q)w\bigr).
\]
If \(w\ne w_1\), this derivative is nonzero, so some point arbitrarily near \(u_1\) has deficit strictly greater than \(F_w(u_1)=m_1\). Every other allocation is therefore strictly inferior.

**3. Long separation: \(0<q<1/3\).** Put \(w_2=1/[2(1-q)]\), \(m_2=1/[8(1-q)]\), and \(u_2=\log[2(1-q)/q]\). Since \(q<1/3<1/2\), the upstream quadratic reaches its peak \(w_2/4=m_2\) at \(u=\log2<kd\). At \(w=w_2\), the downstream quadratic has \(A=1/(2q)\), \(B=(1-q)/(2q^2)\), vertex \(z=q/[2(1-q)]<q\), and maximum \(m_2\). Thus \(M(w_2,q)=m_2\).

Any allocation \(w>w_2\) has upstream deficit at \(u=\log2\) strictly larger than \(m_2\). For \(w<w_2\), evaluate instead at the **fixed** downstream time \(u_2\). The downstream-source response exceeds the upstream-source response there by
\[
\left(e^{-(u_2-kd)}-e^{-2(u_2-kd)}\right)-\left(e^{-u_2}-e^{-2u_2}\right)=\frac{1-3q}{4(1-q)}>0.
\]
Moving load from the first outfall to the second consequently raises the deficit at \(u_2\) strictly above \(F_{w_2}(u_2)=m_2\). Therefore \(w_2\) is again the unique global minimizer. The equality \(q=1/3\) is already covered by Step 2 and both closed forms agree there.

**4. Geometry and active worst locations.** On \(q\in[1/3,1)\), \(w_*=1/(1+q)\) decreases strictly with increasing \(q\); on \((0,1/3]\), \(w_*=1/[2(1-q)]\) increases strictly with increasing \(q\). Since \(q=e^{-kd}\) strictly decreases with separation, the fraction first rises then falls, attaining \(3/4\) only at \(kd=\log3\). The limiting values are both \(1/2\). The active downstream quadratic has a strict unique vertex in both branches; the upstream curve attains the same global value exactly for \(q\le1/3\), proving the stated active-location classification.

**5. Example.** At \(q=1/4\), equivalently \(kd=\log4\), the unique optimum is \(w_*=2/3\) and the worst normalized oxygen deficit is \(1/6\). All-upstream or all-downstream loading gives worst deficit \(1/4\). The optimized allocation therefore reduces the model's worst deficit by exactly one third relative to placing the entire load at either outfall.

## Verification

The included `verify.py` executes with `python3 verify.py` and uses only exact rational arithmetic in the Python standard library. With \(q\) rational it computes the **actual global** maximum on both reaches analytically as maxima of rational quadratic expressions and checks the candidate formulas against thousands of other rational allocations and randomized rational parameters. The observed output on the supplied file is `PASS: 16432 exact-rational assertions`. This is finite corroboration; Steps 1–4 supply the proof for every real \(q\in(0,1)\), not a deduction from enumeration. No external data or particular river calibration is required.

## Relationship to prior work

The first-order Streeter–Phelps equation and linear superposition are classical (Streeter and Phelps, 1925), so neither is claimed here. Loucks, ReVelle and Lynn (1967) established linear-programming methods for minimizing wastewater-treatment costs under stream oxygen standards; their published abstract does not provide this fixed-total, entire-reach exact minimax allocation. Arbabi, Elzinga and ReVelle (1974) proved general convexity properties of critical oxygen deficits and proposed a linear approximation; such convexity underlies optimization but **does not by itself identify** the sharp separation \(\log3\), the two explicit minimizers, or the reentrant nonmonotonicity. Jamal's full 1986 thesis develops nonlinear numerical optimization of permissible loadings in a tidal river, with a different constraint and objective. Bhargava (2007) studies multi-outfall sag profiles with settling, but the full article could not be accessed to rule out every relevant specialization. Tyagi, Aggarwal and Sinha (2014) model multiple pollution sources and settling/dispersion without this fixed-load minimax formula.

A related published mathematical analysis of two delayed Streeter–Phelps responses establishes a sharp *count of local oxygen-deficit maxima* and reentrant double-sag regimes. Its theorem explicitly does not decide which peak is globally worst and does not optimize a fixed total load. The present claim instead uniquely minimizes the **global largest deficit**, yields an exact load-fraction law for every separation, and identifies where the equal active worst locations appear. This is a difference of mathematical statements, not merely a change of title or variables. The two claims use the same kernel and are complementary, not asserted to be independent or historically priority-proven.

## Limitations

This result is a sharp benchmark for a two-outfall linear model with exactly twice-as-fast reaeration; it does not prove a formula for arbitrary independent rate ratios, physical feasibility for arbitrary high BOD load, or optimal wastewater-management regulations. Field data, variable flow, direct mixing dilution, background deficits, benthic oxygen demand, temperature and seasonality can alter the optimal split. Earlier general water-quality management literature, especially Liebman and Lynn (1966), Loucks et al. (1967), Arbabi et al. (1974), and Bhargava (2007), could contain an equivalent specialized implication outside the inspected accessible material. Full-text access to some relevant works was unavailable, so historical priority remains provisional. Neither numerical tests nor source-search failures constitute novelty certification.

## References

- H. W. Streeter and E. B. Phelps (1925), *A Study of the Pollution and Natural Purification of the Ohio River, III*, U.S. Public Health Bulletin 146. Public-domain scan: https://udspace.udel.edu/server/api/core/bitstreams/6f57c427-5f4f-4435-9d8c-87e3c8c02a66/content .
- D. P. Loucks, C. S. Revelle and W. R. Lynn (1967), *Linear Programming Models for Water Pollution Control*, Management Science 14(4), B166–B181. First publisher-listed release 1 December 1967. https://doi.org/10.1287/mnsc.14.4.B166 .
- M. Arbabi, J. Elzinga and C. ReVelle (1974), *The Oxygen Sag Equation: New properties and a linear equation for the critical deficit*, Water Resources Research 10(5), 921–929. https://doi.org/10.1029/WR010i005p00921 .
- I. Jamal (1986), *Optimal allocation of 'BOD' loadings in a tidal river*, University of British Columbia thesis. https://doi.org/10.14288/1.0096653 .
- D. S. Bhargava (2007 first online; 2008 print), *Dissolved oxygen sag analysis for a settling fields overlapping type multi-wastewater-outfall*, The Environmentalist 28, 128–136. https://doi.org/10.1007/s10669-007-9120-x .
- B. Tyagi, S. Aggarwal and D. Sinha (2014), *Analysis of DO sag for Multiple Point Sources*, Mathematical Theory and Modeling 4(3). https://www.academia.edu/51499107/Analysis_of_DO_sag_for_Multiple_Point_Sources .
- *Reentrant double-sag regimes for two separated biochemical oxygen-demand sources* (published mathematical note, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-reentrant-double-sag-regimes-for-two-separated-biochemical-oxyge--92e4f7efeacb .
