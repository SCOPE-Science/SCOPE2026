# Four one-sided concentrations separate diffusion, loss, drift and release under two known flows

## Finding

A known, permanent point source on a line is observed in two *quasi-steady* flow conditions. The imposed velocity offsets \(u_1>u_2\) are known, but the common dispersion coefficient \(D>0\), first-order loss rate \(\lambda>0\), residual drift \(w\in\mathbb R\), and constant source intensity \(Q>0\) are unknown. At both flow conditions, measure concentration at the same two known positions \(0<x_a<x_b\). **The resulting four scalar measurements determine all four unknowns globally and uniquely**, and four are minimal among point observations confined to these two flow conditions and the positive half-line.

The four measured concentrations \(c_{ia}=C_i(x_a)>0\), \(c_{ib}=C_i(x_b)>0\), for \(i=1,2\), are compatible with *some* strictly positive \(D,\lambda,Q\) and real \(w\) if and only if the following conditions hold. Define

\[
 k_i=\frac{\log(c_{ia}/c_{ib})}{x_b-x_a},\qquad
 A_i=c_{ia}e^{k_ix_a},\qquad R=\frac{A_1}{A_2}.
\]

The exact necessary-and-sufficient feasible-data inequalities are

\[
 0<k_1<k_2,\qquad \frac{k_1}{k_2}<R<\frac{k_2}{k_1}.
\]

For feasible data, write \(\Delta=k_2-k_1>0\), \(V=u_1-u_2>0\), and

\[
 z=\frac{Rk_2-k_1}{1+R}.
\]

Then the **explicit inverse** is

\[
 D=\frac{Vz}{\Delta^2},\qquad
 \lambda=k_1k_2\left(\frac{V}{\Delta}-D\right),
\]
\[
 w=\frac{u_1k_1-u_2k_2}{\Delta}-D(k_1+k_2),\qquad
 Q=A_1\left(\frac{Vk_2}{\Delta}-D\Delta\right).
\]

In contrast, at a *single* flow condition even an exact complete curve \(C_i(x)\) for every \(x>0\) leaves a two-parameter family of distinct physical parameter quadruples. If only three point observations at the two available flow conditions are allowed, local nonidentifiability remains at every strictly feasible parameter point.

## Assumptions and scope

The source position is known and set to \(x=0\). In each condition \(i=1,2\), the steady concentration \(C_i:\mathbb R\to[0,\infty)\) is the unique decaying distributional solution of

\[
 D C_i''-(w+u_i)C_i'-\lambda C_i+Q\delta_0=0,
 \qquad \lim_{x\to\pm\infty}C_i(x)=0.
\]

The positive constants \(D,\lambda,Q\) are *unchanged between conditions*, as is \(w\). Only the known additive advection offset \(u_i\) is changed; it can have either sign, and the total advection \(w+u_i\) can also have either sign. One-dimensional effective dispersion includes longitudinal mixing, not a claim about a physically unbounded coastline. Observations are exact concentrations, not detection-only flags or unknown-gain readouts. Each condition is assumed to settle to its own steady state despite the tidal motivation. No finite-depth, boundary, variable-source, time-dependent tidal, or measurement-noise claim is made.

## Proof

**1. Green functions and the two measured invariants.** Write \(v_i=w+u_i\) and

\[
 S_i=\sqrt{v_i^2+4D\lambda},\quad
 k_i=\frac{S_i-v_i}{2D}>0,\quad
 r_i=\frac{S_i+v_i}{2D}>0.
\]

The differential equation away from the source has characteristic roots \(-k_i\) and \(r_i\). Decay at the two infinities, continuity at the point source, and the jump condition \(D[C_i'(0+)-C_i'(0-)]=-Q\) give the unique full-line solution

\[
 C_i(x)=\frac Q{S_i}
 \begin{cases}e^{-k_ix},&x\ge 0,\\ e^{r_ix},&x<0.\end{cases}
\]

Therefore the two positive-side measurements per condition determine exactly \(k_i\) and \(A_i=Q/S_i\), as stated above. The characteristic equation gives

\[
 Dk_i^2+(w+u_i)k_i-\lambda=0.
\]

Since \(k(v)=(\sqrt{v^2+4D\lambda}-v)/(2D)\) is strictly decreasing in \(v\), the known ordering \(u_1>u_2\) forces \(0<k_1<k_2\).

**2. Algebraic elimination.** Subtracting the two characteristic equations and using \(\Delta=k_2-k_1\), \(V=u_1-u_2\), gives the exact identities

\[
 w=\frac{u_1k_1-u_2k_2}{\Delta}-D(k_1+k_2),\qquad
 \lambda=k_1k_2\left(\frac V\Delta-D\right).
\]

Using \(S_i=v_i+2Dk_i\) yields

\[
 S_1=\frac{Vk_2}{\Delta}-D\Delta,\qquad
 S_2=\frac{Vk_1}{\Delta}+D\Delta.
\]

Since \(A_i=Q/S_i\), one has the *amplitude identity*

\[
 R=\frac{A_1}{A_2}=\frac{S_2}{S_1}
 =\frac{k_1+z}{k_2-z},\qquad
 z=\frac{D\Delta^2}{V}.
\]

The strict assumptions \(D>0\) and \(\lambda>0\) are equivalent, given \(0<k_1<k_2\), to \(0<z<\Delta\). The map \(z\mapsto(k_1+z)/(k_2-z)\) is strictly increasing, with endpoint limits \(k_1/k_2\) and \(k_2/k_1\). This proves necessity of the data inequalities and uniquely solves for \(z\), thus for \(D,\lambda,w,Q\).

Conversely, if the two strict inequalities hold, the displayed \(z\) lies in \((0,\Delta)\), so the reconstructed \(D,\lambda,Q\) are all positive. The reconstructed \(S_1,S_2\) are positive, their ratios give exactly the supplied \(A_1/A_2\), and the formula for \(Q\) gives both amplitudes. The positive characteristic roots are exactly the supplied \(k_i\). The Green function then returns all four observed concentrations. Hence the conditions are sufficient, and the solution is unique.

**3. Sharpness of four readings.** For a single fixed flow offset \(u\), its *entire* positive-side concentration curve yields at most \((A,k)\), since \(C(x)=Ae^{-kx}\). For any freely chosen \(D,\lambda>0\), set

\[
 w=\frac\lambda k-Dk-u,\qquad
 Q=A\left(Dk+\frac\lambda k\right).
\]

These distinct quadruples all produce the same full positive-side curve. With at most three scalar readings at two fixed conditions, either one condition has no readings (then only one curve is probed) or the counts are \(2+1\) or \(1+2\). In the \(2+1\) case, the pair fixes \((k_1,A_1)\), while the single reading in the other condition fixes only \(A_2e^{-k_2x}\). Vary \(k_2\) slightly around its true value, choose \(A_2\) to preserve that reading, and apply the inverse formulas. The strict feasibility inequalities persist under a small variation, producing a nonconstant one-parameter family with the same three readings. The \(1+2\) case is symmetric. Therefore no three-point design using these two conditions can identify all four parameters at every interior point.

**4. Exact positive witness.** Take \(u_1=1\), \(u_2=-1\), \(D=1/2\), \(\lambda=3\), \(w=3/2\), and \(Q=7\). Then for \(x>0\),

\[
 C_1(x)=2e^{-x},\qquad C_2(x)=\frac{14}{5}e^{-2x}.
\]

For measurements at \(x_a=1\), \(x_b=2\) this gives \(k_1=1\), \(k_2=2\), \(A_1=2\), \(A_2=14/5\), and \(R=5/7\). The inverse recovers the displayed quadruple exactly, and \(1/2<5/7<2\).

## Verification

Run `python3 verify.py` using only the Python standard library. The checker includes an exact rational inversion of the witness, 12,000 seeded forward/inverse numerical cases, equation/jump identities, and a concrete three-reading ambiguity. Its reported checks are supplementary only; the mathematical proof is the exact Green-function calculation, strict monotonicity and explicit ambiguity family above. The script was run from this package with the result `PASS: 120012 assertions`.

## Relationship to prior work

Baetscher et al. (2024) measured marine environmental-DNA concentration changes with distance and incoming/outgoing tides, using species-specific qPCR and statistical regressions; they did not state or prove the present simultaneous four-parameter inverse theorem. Kim (2020) studies analytic forward solutions of the linear convection–diffusion–reaction–source equation, not the minimum two-condition measurement design and exact feasible-data interval here. El Badia, Ha-Duong and Hamdi (2005) study recovery of an unknown *source position and time-dependent strength* from full time traces, with the transport coefficients specified as part of their model; their identifiability result does not imply the present unknown-coefficient inversion from four steady one-sided scalars. Andrle, Ben Belgacem and El Badia (2011) study moving-source identification from two stations on opposite sides of the source; their full text was not available for direct comparison, so historical priority against uninspected parts of that work remains open.

An exact steady Green function and the algebra of exponential decay are classical and not claimed as inventions. The submitted contribution is their combined sharp *two-flow, common-source, four-unknown* identifiability/feasibility/minimality classification, rather than a claim of a new transport equation.

## Limitations

The model idealizes each changing tidal phase as a separately equilibrated, homogeneous, full-line steady state, while real tides change continuously. Source intensity, loss and dispersion must remain common to both states; if tide alters source shedding, dilution/gain calibration, mixing, temperature-dependent loss or boundaries, the inversion need not apply. The result is global structural identifiability for exact measurements, not a claim of uniform conditioning: recovery becomes sensitive when the slopes become nearly equal. It provides no statistical efficiency, uncertainty interval, or field validation. The closest source-identification literature includes some material that could not be inspected in full; independent historical-priority and external mathematical audits have not been performed.

## References

1. Baetscher, D. S., Pochardt, M. R., Barry, P. D., and Larson, W. A. (2024), “Tide impacts the dispersion of eDNA from nearshore net pens in a dynamic high-latitude marine environment,” *Environmental DNA* 6(2), e533. First online 12 March 2024. https://doi.org/10.1002/edn3.533
2. Kim, A. S. (2020), “Complete analytic solutions for convection-diffusion-reaction-source equations without using an inverse Laplace transform,” *Scientific Reports* 10, 8040. https://doi.org/10.1038/s41598-020-63982-w
3. El Badia, A., Ha-Duong, T., and Hamdi, A. (2005), “Identification of a point source in a linear advection–dispersion–reaction equation: application to a pollution source problem,” *Inverse Problems* 21, 1121. https://doi.org/10.1088/0266-5611/21/3/020
4. Andrle, M., Ben Belgacem, F., and El Badia, A. (2011), “Identification of moving pointwise sources in an advection–dispersion–reaction equation,” *Inverse Problems* 27, 025007. https://doi.org/10.1088/0266-5611/27/2/025007
