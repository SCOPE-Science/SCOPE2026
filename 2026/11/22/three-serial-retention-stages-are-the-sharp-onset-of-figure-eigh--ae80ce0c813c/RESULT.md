# Three serial retention stages are the sharp onset of figure-eight discharge–response loops under positive quadratic supply

## Finding

A positively forced scalar retention cascade can produce a genuine figure-eight response-versus-discharge loop *without any nonmonotone instantaneous source law or multiple environmental sources*. This first becomes possible at three serial first-order stages: for one or two stages, no strictly positive retention rates permit an interior self-intersection under the assumptions below. For three **equal-rate** stages there is a single, sharp, bounded frequency window in which one transverse interior crossing occurs.

Write \(\rho=\varepsilon/q\in(0,1)\), \(x=(\omega/\lambda)^2>0\), and
\[
R(x)=\frac{|3-x|(1+4x)^3}{|3-4x|(1+x)^3},\qquad R(3/4):=+\infty.
\]
Exactly two values \(x_-(\rho)\in(3/4,3)\) and \(x_+(\rho)\in(3,\infty)\) solve \(R(x)=\rho\). The three-stage periodic curve has **exactly one transverse interior self-intersection** precisely when \(x_-(\rho)<x<x_+(\rho)\). It has none for the other parameter values. Within these one-, two-, and equal-rate three-stage cases, no additional isolated interior self-intersection occurs.

At the internal frequency \(\omega=\sqrt3\,\lambda\) the two lobes have exactly equal and opposite signed areas. Although the complete signed loop integral vanishes, each lobe has the nonzero absolute area
\[
\mathcal A_{\rm lobe}=\frac{12\sqrt3}{2197}\,\varepsilon^3.
\]
For the rational example \(q=2,\varepsilon=1,\lambda=1\), the frequency-squared window has \(x_-=2.873444346802\ldots\) and \(x_+=3.135890435960\ldots\); the point \(x=3\) lies strictly within it.

## Assumptions and scope

Choose an integer stage count \(n\ge1\), positive rates \(\lambda_j>0\), and forcing constants \(q>\varepsilon>0\), \(\omega>0\). The positive, single-peaked periodic environmental driver (over one cycle) is
\[
Q(t)=q+\varepsilon\cos(\omega t).
\]
The **monotone** instantaneous mobilization rule is \(f(Q)=Q^2\) on the strictly positive forcing range. The response is the final component of the stable, linear serial filter
\[
\dot z_1=\lambda_1[Q(t)^2-z_1],\qquad
\dot z_j=\lambda_j(z_{j-1}-z_j),\quad 2\le j\le n.
\]
There is a unique globally attracting periodic solution. The parametric response curve is \(\Gamma:t\mapsto(Q(t),z_n(t))\) over \(0\le\omega t<2\pi\). An *interior transverse double point* means two distinct phases in this half-open interval having the same pair \((Q,z_n)\), discharge strictly between \(q-\varepsilon\) and \(q+\varepsilon\), and nonparallel tangent vectors. Such a curve with one interior transverse double point and two lobes is called a figure-eight here. No physical concentration normalization, river geometry, or sediment mass-balance calibration is implied.

For the complete three-stage frequency classification take \(n=3\) and \(\lambda_1=\lambda_2=\lambda_3=\lambda\). The one- and two-stage exclusion holds for **all** positive, potentially unequal rates.

## Proof

**1. Exact harmonics.** Write \(\theta=\omega t\). Since
\[
Q^2=q^2+\frac{\varepsilon^2}{2}+2q\varepsilon\cos\theta+\frac{\varepsilon^2}{2}\cos2\theta,
\]
the cascade transfer function at harmonic \(k\) is
\[
H_n(k)=\prod_{j=1}^n\frac{\lambda_j}{\lambda_j+ik\omega}.
\]
The periodic output has the exact form
\[
z_n(\theta)=q^2+\frac{\varepsilon^2}{2}+A\cos\theta+B\sin\theta+D\cos2\theta+E\sin2\theta,
\]
where
\[
A=2q\varepsilon\operatorname{Re}H_n(1),\quad B=-2q\varepsilon\operatorname{Im}H_n(1),\quad
D=\frac{\varepsilon^2}{2}\operatorname{Re}H_n(2),\quad E=-\frac{\varepsilon^2}{2}\operatorname{Im}H_n(2).
\]
A scalar first-order stable filter multiplies a positive-frequency sinusoid by \(\lambda_j/(\lambda_j+ik\omega)\), so these identities follow either by complex exponentials or by substitution into the ODEs. Constant input passes through unchanged.

**2. Exhaustive crossing test.** Equal discharge at distinct phases in one cycle requires \(\theta\) and \(2\pi-\theta\), with \(0<\theta<\pi\). Their response difference is
\[
z_n(\theta)-z_n(2\pi-\theta)=2\sin\theta\,[B+2E\cos\theta].
\]
Thus there is an interior double point exactly if \(E\ne0\) and \(|B|<2|E|\), except that \(B=E=0\) gives a multiply traced curve rather than a transverse point. The unique candidate has \(\cos\theta_*=-B/(2E)\). It is transverse: as the two response branches are expressed as functions of discharge \(Q=q+\varepsilon u\), their vertical separation is \(2\sqrt{1-u^2}(B+2Eu)\), with nonzero derivative at \(u=-B/(2E)\) when \(E\ne0\). Consequently at most one interior transverse crossing is possible, and any such crossing is unique.

**3. Why two stages never suffice.** Put \(b_n(k)=-\operatorname{Im}H_n(k)\). For one stage
\[
b_1(k)=\frac{\lambda_1 k\omega}{\lambda_1^2+k^2\omega^2}>0,
\]
and for two stages
\[
b_2(k)=\frac{\lambda_1\lambda_2(\lambda_1+\lambda_2)k\omega}{(\lambda_1^2+k^2\omega^2)(\lambda_2^2+k^2\omega^2)}>0.
\]
For either \(n\in\{1,2\}\), direct division yields
\[
\frac{b_n(2)}{b_n(1)}=2\prod_{j=1}^n\frac{\lambda_j^2+\omega^2}{\lambda_j^2+4\omega^2}<2.
\]
Since \(B=2q\varepsilon b_n(1)\) and \(2E=\varepsilon^2 b_n(2)\), we obtain \(|2E/B|<\varepsilon/q<1\). The crossing test is never satisfied. This proves minimality among all one- and two-stage positive serial cascades, not only equal-rate cases.

**4. Sharp three-stage window.** When all three rates equal \(\lambda\), let \(x=(\omega/\lambda)^2\). From \(H_3(k)=(1+ik\sqrt x)^{-3}\),
\[
b_3(1)=\frac{\sqrt{x}(3-x)}{(1+x)^3},\qquad
b_3(2)=\frac{2\sqrt{x}(3-4x)}{(1+4x)^3}.
\]
The necessary and sufficient strict crossing condition becomes
\[
q\frac{|3-x|}{(1+x)^3}<\varepsilon\frac{|3-4x|}{(1+4x)^3},
\]
which is \(R(x)<\rho\). For the monotonicity proof define the signed rational function
\[
G(x)=\frac{(3-x)(1+4x)^3}{(4x-3)(1+x)^3}.
\]
Its derivative is exactly
\[
G'(x)=-\frac{18(4x+1)^2(4x^2-5x+5)}{(x+1)^4(4x-3)^2}<0
\]
where defined, because \(4x^2-5x+5>0\) for all real \(x\). Now \(R(x)=-G(x)\) on \((0,3/4)\), \(R(x)=G(x)\) on \((3/4,3)\), and \(R(x)=-G(x)\) on \((3,\infty)\). Therefore \(R\) increases from \(1\) to infinity on \((0,3/4)\); decreases from infinity to \(0\) on \((3/4,3)\); and increases from \(0\) to \(16\) on \((3,\infty)\). Because \(0<\rho<1\), exactly two admissible roots exist, one in each of the latter intervals. The strict inequality holds exactly between them, proving the complete classification. At either boundary root the candidate collision reaches extreme discharge, so it is not an interior transverse crossing.

**5. Signed-area cancellation with nonzero lobes.** The complete oriented loop integral is
\[
\oint_\Gamma z_3\,dQ=-\pi\varepsilon B,
\]
by orthogonality of the first and second harmonics. At \(x=3\), \(B=0\), whereas
\[
E=\frac{\varepsilon^2}{2}\frac{2\sqrt3(3-12)}{(1+12)^3}=-\frac{9\sqrt3}{2197}\varepsilon^2\ne0.
\]
The crossing occurs at \(Q=q\) (\(\theta=\pi/2\) and \(3\pi/2\)). The paired-branch response difference is \(4E\sin\theta\cos\theta\); integrating its absolute value against \(|dQ|=\varepsilon\sin\theta\,d\theta\) on either half-cycle discharge interval gives
\[
\mathcal A_{\rm lobe}=4\varepsilon|E|\int_0^{\pi/2}\sin^2\theta\cos\theta\,d\theta
=\frac{4\varepsilon|E|}{3}
=\frac{12\sqrt3}{2197}\varepsilon^3.
\]
Their orientation signs are opposite, proving an exactly zero net area with nonzero geometric hysteresis. Every step is an identity on the exact periodic solution.

## Verification

The separately included standard-library Python checker (`checker.py`) verifies the polynomial identity for \(G'\) with exact rational coefficients, the two sample quartic equations and rational root brackets, the first/second harmonic coefficients, branch-crossing signs, the signed-area and per-lobe formula, and an independent sampled phase-curve diagnostic. The numerical sampling is a **diagnostic**, not proof of any universal assertion; the algebra above proves all quantified claims. A direct reproducible command is `python3 checker.py`.

For the example \(q=2\), \(\varepsilon=1\), \(\lambda=1\), the exact root equations are \(44x^4-93x^3-87x^2-25x-3=0\) for \(x_-\) and \(124x^4-297x^3-267x^2-65x-3=0\) for \(x_+\), each with its location interval proved above. The displayed decimals are illustrative only.

## Relationship to prior work

Hydrologic observations have long identified clockwise, counterclockwise, and figure-eight sediment–discharge loops. Hassan et al. (2023) experimentally compared sediment feeding timing under an event hydrograph; Waite et al. (2023) measured concentration–discharge hysteresis in a large river. Zhang et al. (2021) built an empirically fitted sediment-availability–transport model generating multiple loop forms, including figure-eight loops. The suspended-sediment review first released on 2024-12-31 explicitly classifies figure-eight patterns and discusses why scalar signed indices can mask complex shapes. These are **strong prior demonstrations that figure-eight loops themselves are known**, not novelty claimed here. The exact three-stage minimality, all-frequency interval, and two-lobe cancellation for the specific positive quadratic input and stable serial filter are the narrowly assessed classification.

Nash-cascade and first-order linear-reservoir transfer functions, Fourier decomposition, second-harmonic parametric curves and signed-area integrals are standard tools; none is claimed as new. Related mathematical results on multi-stage impulse-response peak counts concern a different object (number of temporal runoff crests rather than self-crossings against discharge). The possibility that a prior general harmonic-curve or filter theorem subsumes this exact classification remains a historical-priority risk; a targeted literature search is not a proof of uniqueness.

## Limitations

The input is strictly sinusoidal and positive, unlike most real isolated hydrographs. Quadratic source law and the linear time-invariant cascade are idealizations; physical storage, sediment supply and channel evolution may not obey them. The full three-stage classification assumes identical stage rates, while the one/two-stage impossibility allows arbitrary positive rates. The output is a transported-response proxy rather than a field-validated suspended-sediment concentration. No empirical calibration, causal attribution of observed figure-eight loops, uncertainty propagation, or classification for arbitrary nonlinear sources or networks is provided. An independently performed audit and external historical-priority determination are absent.

## References

1. Hassan, M. A., Li, W., Viparelli, E., An, C., and Mitchell, A. J. (2023), *Influence of Sediment Supply Timing on Bedload Transport and Bed Surface Texture During a Single Experimental Hydrograph in Gravel Bed Rivers*, Water Resources Research, DOI: https://doi.org/10.1029/2023WR035406 (first public release 2023-12-12).
2. Waite, T., et al. (2023), *River Geomorphology Affects Biogeochemical Responses to Hydrologic Events in a Large River Ecosystem*, Water Resources Research, DOI: https://doi.org/10.1029/2022WR033662.
3. Zhang, T., et al. (2021), *Constraining Dynamic Sediment-Discharge Relationships in Cold Environments: The Sediment-Availability-Transport (SAT) Model*, Water Resources Research, DOI: https://doi.org/10.1029/2021WR030690.
4. Jing, T., Zeng, Y., Fang, N., Dai, W., and Shi, Z., *A Review of Suspended Sediment Hysteresis* (first publicly released 2024-12-31), Water Resources Research, DOI: https://doi.org/10.1029/2024WR037216.
5. Zeman, M., et al. (2025), *Distribution of Time Scales Induces Slow Dynamics and Elastic Hysteresis in Sandstones*, DOI: https://doi.org/10.1007/s00603-025-04668-5 (related harmonic hysteresis mechanisms; a different material model).
