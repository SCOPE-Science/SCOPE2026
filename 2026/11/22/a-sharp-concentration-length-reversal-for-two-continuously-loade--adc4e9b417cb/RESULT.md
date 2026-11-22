# A sharp concentration–length reversal for two continuously loaded saturating river reaches

## Finding

Consider two advective river reaches with different nutrient half-saturation concentrations but the same constant lateral nutrient input and the same maximum uptake rate. The lower-affinity reach has half-saturation constant \(K\), the higher-affinity reach has \(L\), and \(K>L>0\). In a continuous, completely deterministic one-pass model with positive source \(s\) greater than saturating removal capacity \(k\), **a fixed length of the lower-affinity reach has one sharp critical length of the higher-affinity reach**. Below this critical length, the best upstream–downstream order switches exactly once as incoming concentration rises; at and beyond the critical length, one order wins at every positive incoming concentration.

More precisely, let \(F_H^t(x)\) be the unique flow for residence time \(t\ge0\) of
\[
\dot C=s-\frac{kC}{H+C},\qquad C(0)=x\ge0,
\]
where \(H>0\), \(s>k>0\). Fix \(K>L>0\) and residence time \(a>0\) of reach \(K\). For each residence time \(b>0\) of reach \(L\), compare the outlet concentrations
\[
Q_{KL}(x;b)=F_L^b(F_K^a(x)),\qquad
Q_{LK}(x;b)=F_K^a(F_L^b(x)).
\]
There exists exactly one critical \(b_c>0\), given implicitly and reproducibly in the proof, with the following exhaustive classification:

* If \(0<b<b_c\), there is exactly one \(x_*(b)>0\). The order \(K\) then \(L\) uniquely minimizes outlet concentration for \(0\le x<x_*(b)\), while \(L\) then \(K\) does so for \(x>x_*(b)\); the two outputs tie precisely at \(x=x_*(b)\). Moreover \(x_*(b)\) is strictly decreasing in \(b\).
* At \(b=b_c\), the two orders tie at \(x=0\), and \(L\) then \(K\) uniquely minimizes outlet concentration for every \(x>0\).
* At \(b>b_c\), the order \(L\) then \(K\) uniquely minimizes outlet concentration for every \(x\ge0\).

These assertions hold for all real parameters in the stated open domain, not only a numerical example. The first limit of the switching concentration, as \(b\downarrow0\), is a finite strictly positive explicit implicit root, while \(x_*(b)\downarrow0\) as \(b\uparrow b_c\).

## Assumptions and scope

The scalar coordinate \(t\) is travel or residence time, not calendar time. Both reaches are idealized steady one-dimensional, plug-flow compartments: no dispersion, hydraulic feedback, dynamic biomass, input changes between reaches, removal of lateral water, or upstream/downstream asymmetry other than the prescribed ordering. Both reaches have the **same** continuous additive source concentration rate \(s>0\) and the **same** maximal Michaelis–Menten/Monod uptake rate \(k>0\), but different positive half-saturation concentrations \(K>L\). The strict regime \(s>k\) guarantees strictly increasing concentration along either reach and is essential to the present theorem. Flow maps include the lateral source while the water traverses each reach; an impulsive addition inserted between zero-source finite-step removal maps is a different model. Both reach durations \(a,b\) are held fixed when comparing the two orders. The input concentration \(x\) may be zero and ranges over all nonnegative reals. The objective is minimum concentration at the end of the second reach, not cumulative removal, a downstream time integral, or a real-world operational prescription.

All flow solutions are global and strictly increasing in input because the right-hand side is positive and smooth on nonnegative concentrations. Every property below is exact under these assumptions.

## Proof

**Step 1: Exact flow coordinates.** Write \(w=s-k>0\), and let \(f_H(c)=s-kc/(H+c)=(sH+wc)/(H+c)>0\). Define the strictly increasing primitive
\[
\Psi_H(c)=\int_0^c\frac{du}{f_H(u)}
=\frac{c}{w}-\frac{kH}{w^2}\log\!\left(1+\frac{wc}{sH}\right),\qquad c\ge0.
\]
It maps \([0,\infty)\) bijectively onto \([0,\infty)\), and the exact flow is uniquely specified by
\[
\Psi_H(F_H^t(c))=\Psi_H(c)+t.
\]
In particular both flows increase strictly in their initial concentration and in positive residence time.

**Step 2: A single-hump displacement.** Use the coordinate \(z=\Psi_L(c)\), so the \(L\)-reach map is exactly translation \(z\mapsto z+b\). Define
\[
H_a(z)=\Psi_L\!\bigl(F_K^a(\Psi_L^{-1}(z))\bigr),\qquad
\delta(z)=H_a(z)-z,
\]
and the positive speed ratio \(r(c)=f_K(c)/f_L(c)\). Differentiation through the flows gives
\[
H_a'(z)=\frac{r(F_K^a(c))}{r(c)},\qquad c=\Psi_L^{-1}(z).
\]
The rational ratio has the exact divided difference, valid for \(y>c\ge0\),
\[
r(y)-r(c)=\frac{k(K-L)(y-c)\,[sKL-wcy]}{(K+c)(K+y)(sL+wc)(sL+wy)}.
\]
All displayed denominator factors are strictly positive. Since \(F_K^a(c)>c\) for \(a>0\), the sign of \(\delta'(z)\) is precisely the sign of \(sKL-wcF_K^a(c)\). The function \(c\mapsto cF_K^a(c)\) strictly increases continuously from zero to infinity. Thus exactly one \(c_0>0\) solves
\[
c_0F_K^a(c_0)=\frac{sKL}{w},\qquad z_0=\Psi_L(c_0)>0,
\]
and \(\delta\) is strictly increasing on \([0,z_0]\) and strictly decreasing on \([z_0,\infty)\) (with derivative zero only at \(z_0\)).

**Step 3: Endpoint asymptotics and the critical reach length.** Because \(f_K(c)>f_L(c)\) for all finite \(c\ge0\), strict comparison of solutions yields \(F_K^a(0)>F_L^a(0)\). Hence
\[
\delta(0)=\Psi_L(F_K^a(0))>\Psi_L(F_L^a(0))=a.
\]
As \(c\to\infty\), both speeds \(f_H(c)\to w\), so by the flow identity, uniformly over a fixed travel time \(a\),
\[
\delta(z)=\int_0^a\frac{f_K(C_K(u;c))}{f_L(C_K(u;c))}\,du\longrightarrow a,
\]
where \(C_K(u;c)=F_K^u(c)\); this integral identity follows by differentiation of \(\Psi_L\) along the \(K\)-flow. Since \(\delta(z_0)>\delta(0)>a\) and \(\delta\) decreases strictly from its maximum to \(a\), there is exactly one \(b_c>z_0\) satisfying
\[
\boxed{\delta(b_c)=\delta(0)}.
\]
This is a well-defined, finite, positive and globally unique critical residence time.

**Step 4: Full ordering classification.** Applying the two orders in the \(z\)-coordinate, and subtracting the outlet for \(K\) then \(L\) from that for \(L\) then \(K\), gives
\[
D_b(z)=H_a(z+b)-\bigl(H_a(z)+b\bigr)=\delta(z+b)-\delta(z).
\]
The sign of this difference is identical to the sign of \(Q_{LK}(x;b)-Q_{KL}(x;b)\), because \(\Psi_L\) is increasing. For \(0<b<b_c\), we have \(D_b(0)>0\) (since \(\delta\) rises to one maximum and returns through its starting value only at \(b_c\)). Whenever \(z+b\le z_0\), strict increase of \(\delta\) gives \(D_b(z)>0\); whenever \(z\ge z_0\), strict decrease gives \(D_b(z)<0\). If \(z<z_0<z+b\), then
\[
D_b'(z)=\delta'(z+b)-\delta'(z)<0.
\]
Consequently there is exactly one zero \(z_*(b)>0\), necessarily straddling \(z_0\), and the sign changes from positive to negative. Its corresponding physical input is \(x_*(b)=\Psi_L^{-1}(z_*(b))\). If \(b=b_c\), the only zero is at \(z=0\), and the difference is negative at all \(z>0\). If \(b>b_c\), then \(D_b(0)<0\) and the same three interval comparisons show \(D_b(z)<0\) for all \(z\ge0\).

**Step 5: Strict motion of the inlet threshold.** At any interior zero with \(0<b<b_c\), necessarily \(z_*<z_0<z_*+b\). The implicit-function derivatives are
\[
\frac{\partial D_b}{\partial z}=\delta'(z_*+b)-\delta'(z_*)<0,
\qquad
\frac{\partial D_b}{\partial b}=\delta'(z_*+b)<0.
\]
Thus \(dz_*/db=-(\partial_b D_b)/(\partial_z D_b)<0\), and the monotone change of coordinate gives strict decrease of \(x_*(b)\). As \(b\downarrow0\), Rolle's theorem and the unique zero of \(\delta'\) force \(z_*(b)\to z_0\); as \(b\uparrow b_c\), continuity and the sole boundary zero force \(z_*(b)\to0\). This completes the proof, including every boundary and equality case.

## Verification

A standalone standard-library Python checker, `verify.py`, independently calculates the exact flow maps by monotone inversion of the primitive in Step 1. It checks the sign of the original outlet difference against the conjugated displacement and tests the predicted one-crossover and all-input-order regimes on an explicit example and 450 seeded random parameter configurations. Run `python verify.py` from the extracted file directory. It reports `VERIFY_OK assertions= 2331` on the reviewed implementation. The numerical tests are diagnostic and do not replace Steps 1–5, which establish the all-parameter theorem.

In particular, for \((s,k,K,L,a)=(2,1,4,1,1)\), the unique turning point and critical length are, respectively,
\[
z_0\approx1.4180063940,\qquad b_c\approx8.1850904349.
\]
At \(b=1\), the unique inlet crossover is \(x_*(1)\approx1.5621163377\); the \(K\)-first order is better below this inlet value, and the \(L\)-first order is better above. For \(b>b_c\), the \(L\)-first order is better for every nonnegative inlet concentration. These numbers are obtained from the exact implicit equations by bisection, not used as an infinite-domain correctness certificate.

## Relationship to prior work

Covino, McGlynn and Baker (2010) studied nutrient retention and saturation kinetics in consecutive stream reaches and measured reach-to-reach biological uptake differences; their full accessible article addresses stream-network retention and empirical uptake, not this continuous two-order, concentration-versus-residence-time theorem. O'Brien and collaborators (2007) analyzed the saturation hypothesis in streams and considered Michaelis–Menten uptake as a candidate mechanism, but noted that the observed system need not follow that law. Neither empirical result asserts the exact deterministic threshold proved here.

An accessible mathematical result, *A two-index ordering law for serial saturating nutrient-removal reaches* (2026), proves a general ordering criterion for **discrete finite-step removal maps without continuous inflow**. Its stated assumptions explicitly exclude exact continuous plug-flow dynamics and intermediate nutrient additions. Another accessible result, *Sharp three-stage stormwater exposure ordering with continued pollutant supply* (2026), proves switching thresholds for **three stages of linear exponential wash-off** and an **integrated receiving-pool exposure** objective. Its two-stage observation is not a theorem for the nonlinear continuously loaded Monod flow here. The current single-hump speed-ratio argument is needed for the present claim; neither closest result implies it by a parameter substitution or reduction. The older finite-step source-addition double-reversal result concerns a discrete concentration jump between stages rather than a continuous input along both reaches and likewise does not settle this theorem.

General scalar-flow comparison and rearrangement are known techniques; only this sharp joint inlet-and-length phase diagram is proposed as a research finding. Earlier hydrological optimization papers on mixed tanks or reactor volume allocation could contain a stronger related theorem, and inaccessible full texts leave historical-priority uncertainty. No claim of unconditional global novelty or independent expert assessment is made.

## Limitations

The regime \(s>k\) is specifically source-dominated, so the stream concentration increases rather than decreases along every reach. The result does not apply unchanged at \(s\le k\), with different external inputs or maximal uptake rates by reach, nonzero diffusion, concentration-dependent lateral loading, branching networks, unequal hydraulics, or biomass feedback. The exact crossover is a statement about a highly stylized mathematical comparison, not an empirical recommendation for rearranging physical river reaches. Neither the numerical checker nor unsuccessful database searches establish originality; an earlier general noncommuting-flow theorem may subsume the result. Independent literature-priority and scientific audit remain open.

## References

1. T. P. Covino, B. L. McGlynn, and M. A. Baker (2010), “Separating physical and biological nutrient retention and quantifying uptake kinetics from ambient to saturation in successive mountain stream reaches,” *J. Geophys. Res.: Biogeosciences* 115, G04010. First online 2010-10-08. https://doi.org/10.1029/2009JG001263
2. J. M. O'Brien et al. (2007), “The saturation of N cycling in Central Plains streams: \(^{15}\mathrm N\) experiments across a broad gradient of nitrate concentrations,” *Biogeochemistry*. First online 2007-03-23. https://doi.org/10.1007/s10533-007-9073-7
3. “A two-index ordering law for serial saturating nutrient-removal reaches” (2026), published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-two-index-ordering-law-for-serial-saturating-nutrient-removal--15d05df5ff61/RESULT.md
4. “Sharp three-stage stormwater exposure ordering with continued pollutant supply” (2026), published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-three-stage-stormwater-exposure-ordering-with-continued-po--056749ef0302/RESULT.md
5. A. Prazeres (1995), “Optimal design of n membrane reactors in series using Michaelis–Menten kinetics,” *Can. J. Chem. Eng.* 73. https://doi.org/10.1002/cjce.5450730617 (abstract inspected; full text inaccessible)
