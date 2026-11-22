# A sharp middle-room activation threshold for end-to-end air cleaning on a three-room path

## Finding

Consider three equal-volume, perfectly mixed rooms in a chain, with symmetric adjacent-room exchange rate \(k>0\), baseline pollutant-loss rate \(v\geq0\) in every room, a constant source of strength \(q>0\) in room 1, and an exposure receptor in room 3. Extra removal rates \(x_1,x_2,x_3\geq0\) can be purchased continuously with fixed total rate \(x_1+x_2+x_3=F>0\). The unique allocation minimizing the steady receptor concentration is as follows.

Define the critical budget
\[
F_{\mathrm c}=\sqrt{v^2+4kv}-v.
\]
If \(0<F\leq F_{\mathrm c}\), then
\[
(x_1^*,x_2^*,x_3^*)=(F/2,0,F/2).
\]
If \(F>F_{\mathrm c}\), define
\[
u=\frac{F+k-3(v+k)+\sqrt{\big(F+k+3(v+k)\big)^2-12k^2}}{6}.
\]
Then
\[
(x_1^*,x_2^*,x_3^*)=(u,F-2u,u),\qquad F/3<u<F/2.
\]
In particular, when \(v>0\), the connecting room receives **no** additional filtration for budgets at or below the strictly positive critical value and a strictly positive but smaller rate than either endpoint above it. When \(v=0\), \(F_{\mathrm c}=0\) and every positive budget funds all three rooms. The rule is independent of source strength \(q\).

A two-room chain, with the same equal-volume/exchange/removal assumptions and an endpoint source and endpoint receptor, instead always splits every positive filtration budget equally between its two rooms. Thus three rooms are the first chain length permitting a budget-driven activation of a previously unfiltered *intermediate* room in this model.

## Assumptions and scope

The spatial domain is exactly the undirected three-vertex path \(1-2-3\), with fixed uniform room volumes normalized to one. Concentrations \(c_i(t)\) obey the linear mass-balance system
\[
\frac{\mathrm dc}{\mathrm dt}=q e_1-M(x)c,\qquad
M(x)=vI+k\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}
+\operatorname{diag}(x_1,x_2,x_3),
\]
where \(q,k,F>0\), \(v\geq0\), \(x_i\geq0\), and \(\sum_i x_i=F\). The only objective is the unique steady-state concentration in room 3, \(c_3^*\). These rates are not discrete device counts. The background sink \(v\) and exchange \(k\) are not changed by filtration; there are no delayed transport, outdoor concentration, filter saturation, or flow-field feedback effects.

Since \(F>0\) and the path is connected, \(M(x)\) is positive definite even for \(v=0\): for nonzero \(z\),
\[
z^\mathsf{T}M(x)z=v\sum_i z_i^2+k\big((z_1-z_2)^2+(z_2-z_3)^2\big)+\sum_i x_i z_i^2>0.
\]
Consequently the steady state \(c^*=qM(x)^{-1}e_1\) exists uniquely for every admissible allocation.

## Proof

**1. Endpoint-to-endpoint transfer reduces to one determinant.** Let \(a=v+k\), \(b=v+2k\). Direct cofactor expansion of the tridiagonal matrix gives
\[
D(x)=\det M(x)=(a+x_1)(b+x_2)(a+x_3)-k^2(2a+x_1+x_3)
\]
and
\[
(M(x)^{-1})_{31}=\frac{k^2}{D(x)},\qquad
c_3^*(x)=\frac{qk^2}{D(x)}.
\]
The determinant is strictly positive, so minimizing steady receptor concentration is equivalent to maximizing \(D(x)\).

**2. The endpoint allocations are necessarily equal.** At fixed \(x_2\), the sum \(x_1+x_3=F-x_2\) is fixed. The subtractive term in \(D(x)\) is then fixed; the remaining product \((a+x_1)(a+x_3)\) is uniquely maximized at \(x_1=x_3\), by the elementary square identity
\[
\left(a+\frac{x_1+x_3}{2}\right)^2-(a+x_1)(a+x_3)=\frac{(x_1-x_3)^2}{4}.
\]
As \(b+x_2>0\), every global optimizer must have \(x_1=x_3=u\) and \(x_2=F-2u\) for \(0\leq u\leq F/2\).

**3. Uniqueness on the remaining interval.** On this one-dimensional family,
\[
D(u)=(a+u)^2(b+F-2u)-2k^2(a+u),
\]
\[
D'(u)=2\left[(a+u)(F+k-3u)-k^2\right].
\]
Write \(H=\operatorname{diag}(1,-2,1)\). Differentiating \(\log\det M\) twice along \(u\) yields
\[
\frac{\mathrm d^2}{\mathrm du^2}\log D(u)
=-\operatorname{tr}\big[(M(u)^{-1/2}H M(u)^{-1/2})^2\big]<0.
\]
The inequality is strict because the matrix between parentheses is a nonzero symmetric matrix. Hence \(\log D\) is strictly concave: its derivative decreases strictly, and there is exactly one maximizing point, possibly a boundary point. Furthermore,
\[
\frac{D'(0)}2=(v+k)(F+k)-k^2=(v+k)F+kv>0.
\]
Therefore the maximum cannot be at \(u=0\).

**4. Exact middle-room activation boundary.** At the other boundary,
\[
D'(F/2)=\frac{4kv-2vF-F^2}{2}.
\]
This quantity is nonnegative precisely when \(F\leq\sqrt{v^2+4kv}-v\). Strict concavity of \(\log D\) then gives the unique optimum \(u=F/2\), i.e. no middle-room allocation, including equality at the threshold. Above this value \(D'(F/2)<0\), whereas \(D'(0)>0\), so the unique optimum is the interior root of \(D'(u)=0\). Solving the quadratic gives exactly the positive-radical expression stated in the finding.

At an interior root,
\[
F-3u=\frac{k^2}{v+k+u}-k<0,
\]
since \(v+u>0\). Thus \(u>F/3\); the interior constraint gives \(u<F/2\). Hence \(0<x_2=F-2u<u\), establishing the strict relative allocation ordering.

**5. Minimal chain-length comparison.** For two rooms, the end-to-end transfer is proportional to the reciprocal of
\[
(v+k+x_1)(v+k+F-x_1)-k^2.
\]
This concave quadratic is uniquely maximized at \(x_1=F/2\) for every \(F>0\). A one-room chain has no intermediate room; a two-room chain cannot exhibit middle-room exclusion. The three-room transition in Steps 1–4 is therefore the first such support transition within the equal-volume path family.

## Verification

The standalone standard-library program `verify.py` tests the tridiagonal determinant against independent determinant expansion, verifies the end-to-end inverse entry, checks exact rational instances and a nonzero threshold, compares the optimizer against 49,500 randomly sampled feasible allocations, tests the endpoint-balancing identity, and checks the stationary equation on interior solutions. On execution it reported **PASS, 54,269 assertions**. These computations are supplementary tests, not substitutes for the proof above.

For the exact illustrative parameters \(k=1\), \(v=1/2\), \(F=2\), the threshold is \(F_{\mathrm c}=1\), and
\[
(x_1^*,x_2^*,x_3^*)=
\left(\frac{\sqrt{177}-3}{12},\frac{15-\sqrt{177}}6,\frac{\sqrt{177}-3}{12}\right)
\approx(0.858678,0.282644,0.858678).
\]
With \(q=1\), the optimal steady concentration in room 3 is approximately \(0.0929066\). To reproduce the supplementary checks, run `python3 verify.py` alongside this document.

## Relationship to prior work

Antonopoulos, Dillon, and Gall (2024) motivate steady-state removal-rate models by assessing the efficacy of a fixed central HVAC filter and a portable air cleaner in a wildfire-smoke setting. Their experimental model uses a single well-mixed zone and does not optimize a continuously divisible three-room removal budget. Kikumoto and Ooka (first online November 23, 2022) derive an adjoint approach to air-cleaner *placement*, including a one-dimensional example with a single cleaner and spatially distributed source and receptor locations; they do not state the three-compartment, three-rate threshold above. Earlier three-room impulse-response placement comparisons concern one full-strength cleaner at selected positions and a time-dependent objective, rather than the present steady-state allocation across all rooms. General positive-definite matrix log-determinant concavity supplies the uniqueness tool used in Step 3 but does not itself state the model-specific explicit activation threshold or endpoint ordering.

The claim is limited to the stated source–receptor, symmetric-exchange, and equal-cost model. Searches of mathematical records and primary literature have not identified a statement covering the entire phase classification, but absence from the inspected corpus is not a proof of worldwide priority.

## Limitations

The model assumes an ideal divisible removal-rate budget with identical linear rate costs, not a discrete number of cleaners; equal room volumes; stationary, symmetric pairwise mixing; no flow-field changes when a cleaner is installed; and concentration at one downstream receptor as the sole target. It does not predict outcomes in actual multizone homes, account for transient concentrations or inhaled dose, or prescribe location choices for wildfire exposure. General multi-room graphs, unequal exchange rates, other sources, and other exposure objectives are not classified. The analytic result establishes no priority over uninspected or inaccessible historical work; an independent external audit has not been performed.

## References

1. Antonopoulos, C., Dillon, H. E., and Gall, E. (2024). *Experimental and Modeled Assessment of Interventions to Reduce PM2.5 in a Residence during a Wildfire Event.* Pollutants **4**, 26–41. First online January 28, 2024. https://doi.org/10.3390/pollutants4010003 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC10863606/ .
2. Kikumoto, H., and Ooka, R. (2023 journal volume; first online November 23, 2022). *Study on influence of air cleaner on room dispersion field and its optimal placement using adjoint concentration.* Japan Architectural Review **6**, e12318. https://doi.org/10.1002/2475-8876.12318 .
3. Walker, I. S., Lessa, B. D., and Lozinsky, C. H. (2024). *Compartmentalization and ventilation system impacts on air and contaminant transport for multifamily buildings.* International Journal of Ventilation **23**. https://doi.org/10.1080/14733315.2024.2333669 . General supporting background; full text was not accessible in the comparison.
