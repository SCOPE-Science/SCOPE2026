# A sharp half-rotation locking window and a parameter-cap crossover in the quadratic sine-circle map

## Finding
Consider the degree-one circle lift introduced by Mugnaine, Sales, Szezech and Viana,
\[
 F_{a,b,\Omega}(x)=x+a\bigl[1-(\Omega-b\sin(2\pi x))^2\bigr],
 \qquad 0\le a\le1,\quad -1\le\Omega\le1.
\]
Fix \(0\le |\Omega|<1/\sqrt2\), put \(d=1-\Omega^2\) and
\[
 S(\Omega)=\sqrt{1+\frac{4\pi^2\Omega^4}{d^2}}.
\]
For every sufficiently small nonzero \(b\), the parameters producing a lifted half-rotation (a point with \(F_{a,b,\Omega}^{2}(x)=x+1\)) form exactly one closed interval \([a_-(b,\Omega),a_+(b,\Omega)]\) inside \((0,1)\). Its endpoints are analytic even functions of \(b\) locally, and
\[
 \boxed{a_\pm(b,\Omega)=\frac{1}{2d}
       +\frac{1\pm S(\Omega)}{4d^2}b^2+O_\Omega(b^4).}
\]
Consequently its exact leading width is
\[
 \boxed{a_+-a_-=\frac{S(\Omega)}{2d^2}b^2+O_\Omega(b^4).}
\]
At every interior parameter there are exactly two distinct primitive period-two orbits, one attracting and one repelling; each endpoint supports precisely one neutral period-two orbit, with a nondegenerate saddle-node of the two cycles. Outside the interval there is no lifted half-rotation orbit. At \(\Omega=0\), the interval is **exact**, for all sufficiently small \(|b|>0\):
\[
 \boxed{[a_-,a_+]=\left[\frac12,\frac{1}{2(1-b^2)}\right].}
\]

The physical cap \(a\le1\) has a sharp crossover as \(\Omega\) approaches \(\Omega_c=1/\sqrt2\). For each sufficiently small \(0<|b|\), there is a unique \(\Omega_*(b)\) near \(\Omega_c\) so that a physical half-rotation orbit exists for \(0\le|\Omega|\) sufficiently close to \(\Omega_c\) exactly on the side \(|\Omega|\le\Omega_*(b)\), with
\[
 \boxed{\Omega_*(b)=\frac1{\sqrt2}+
 \frac{\sqrt{1+4\pi^2}-1}{2\sqrt2}\,b^2+O(b^4).}
\]
Thus nonzero coupling creates a previously forbidden open strip \(\Omega_c<|\Omega|<\Omega_*(b)\) with half-rotation locking for some physically admissible \(a\). At equality the unique admissible half-rotation orbit is neutral and occurs at \(a=1\).

## Assumptions and scope
Here \(F\) denotes the real lift, with \(F(x+1)=F(x)+1\); periodic points are counted modulo one. A half-rotation point is a point satisfying the **specified lift equation** \(F^2(x)=x+1\), not merely a period-two point with an arbitrary lift displacement. Throughout the theorem \(b\ne0\) is sufficiently small, depending on the fixed \(\Omega\) in the first part and uniformly in a sufficiently small neighborhood of \(\Omega_c\) in the final part. The map then has positive derivative and is an orientation-preserving analytic circle diffeomorphism near the locking interval. The notation \(O_\Omega(b^4)\) denotes a bound for fixed \(\Omega\); uniformity as \(\Omega\) tends to other parameter boundaries is not asserted. The physical parameter cap \(a\le1\) is part of the model, not an artificial restriction introduced after the calculation.

## Proof
**1. Exact harmonic form.** Let \(d=1-\Omega^2\). Elementary trigonometry gives
\[
 F(x)=x+\alpha+\beta\sin(2\pi x)+\gamma\cos(4\pi x),
 \quad \alpha=a(d-b^2/2),\quad\beta=2a\Omega b,\quad\gamma=ab^2/2.
\]
The identities \(F_{a,-b,\Omega}(x+1/2)=F_{a,b,\Omega}(x)+1/2\) and its analogue upon changing the sign of \(\Omega\) reduce the proof to \(b>0\), \(\Omega\ge0\) for orbit counts and endpoint values. Put \(a_0=1/(2d)\), and parameterize \(a=a_0+cb^2\). Write \(t=2\pi x\) and \(B=2a_0\Omega=\Omega/d\). A Taylor expansion of both composition steps, uniformly with the first two spatial derivatives for bounded \(c\), gives
\[
 F^2(x)-x-1=b^2\bigl[2dc-a_0+a_0\cos(2t)-\pi B^2\sin(2t)\bigr]+O(b^3).
 \tag{1}
\]
The \(O(b)\) contribution cancels because the unperturbed half-rotation changes the sign of the first harmonic. The quadratic first-harmonic interaction is the \(-\pi B^2\sin(2t)\) term, while the explicit second harmonic contributes \(a_0\cos(2t)\). Their resultant nonconstant amplitude is \(a_0S(\Omega)>0\).

**2. Exact parameter profile and orbit census.** For any fixed \(\Omega<\Omega_c\), choose \(|b|\) so small that \(1-(\Omega-b\sin t)^2>0\), \(F'(x)>0\) for all \(a\in[0,1]\), and \(F_{1,b,\Omega}^2(x)-x>1\) uniformly in \(x\). In this range, \(a\mapsto F_{a,b,\Omega}^2(x)-x\) is strictly increasing, since both stage increments grow with \(a\) and the intermediate map is increasing in its spatial argument. It is zero at \(a=0\) and greater than one at \(a=1\). Thus for every \(x\) there is one and only one \(a=\mathcal A_b(x)\in(0,1)\) satisfying \(F^2(x)=x+1\). The implicit-function theorem gives a smooth, periodic parameter profile.

Solving (1) for the parameter uniformly in \(C^2\) yields
\[
 \mathcal A_b(x)=a_0+\frac{b^2}{2d}
 \bigl[a_0-a_0\cos(4\pi x)+\pi B^2\sin(4\pi x)\bigr]+O(b^3).
 \tag{2}
\]
After division by \(b^2\), the derivative of (2) has exactly four simple zeros per circle period (two maxima and two minima). Uniform \(C^2\) convergence and the implicit-function theorem preserve exactly those four critical points for all sufficiently small nonzero \(b\), with no additional extrema.

The two maxima have exactly the same value, as do the two minima. Indeed, for every \(x\) let \(a=\mathcal A_b(x)\) and \(y(x)=F_{a,b,\Omega}(x)\) modulo one. Then \(F_a^2(y)=y+1\), so \(\mathcal A_b(y(x))=\mathcal A_b(x)\). The map \(x\mapsto y(x)\) is a near-half-turn orientation-preserving diffeomorphism and sends each critical point to its distinct orbit partner, preserving whether it is a maximum or minimum. Thus the range of \(\mathcal A_b\) is one interval; its two boundary values each occur at precisely one primitive period-two orbit. In the strict interior, a regular value has four preimages, paired into exactly two primitive period-two orbits. Since \(F\) is orientation preserving, the derivative of \(F^2\) at the four crossings alternates across one, making one orbit attracting and the other repelling. At the endpoints, the nondegenerate extrema of \(\mathcal A_b\) give ordinary saddle-node multiplier-one collisions. Moreover, every such return advances by one lift unit and is therefore truly primitive period two.

**3. Window coefficients and evenness.** The amplitude of the nonconstant term in (1) is \(a_0S\), so the critical values of (2) have second-order coefficients \((a_0\pm a_0S)/(2d)=(1\pm S)/(4d^2)\). All ingredients are real analytic in \(b\) after scaling the critical equations by \(b^2\). The half-turn conjugacy for \(b\mapsto-b\) preserves the endpoint values and makes each analytic endpoint even. Therefore every apparent cubic remainder vanishes, giving the displayed \(O(b^4)\) remainders.

**4. Exact symmetric slice.** If \(\Omega=0\), then \(F(x+1/2)=F(x)+1/2\). Passing to the quotient by the half-turn, a lifted rotation number \(1/2\) corresponds to rotation number one and therefore to a fixed point of the quotient. Thus half-rotation occurs if and only if \(F(x)=x+1/2\) for some \(x\). Since its increment is \(a(1-b^2\sin^2(2\pi x))\), the exact range condition is \(a(1-b^2)\le1/2\le a\), yielding the stated endpoints and, by the preceding profile argument, the same two-cycle census.

**5. The physical cap and its crossover.** Extend the implicit profile \(\mathcal A_b\) locally to parameters \(a\) slightly larger than one near \(\Omega_c\). The same strictly positive parameter derivative, extrema, and analytic endpoint branches apply uniformly. The lower endpoint has
\[
 a_-(b,\Omega)=\frac1{2(1-\Omega^2)}+
 \frac{1-S(\Omega)}{4(1-\Omega^2)^2}b^2+O(b^4).
\]
At \(\Omega_c\), its leading value is one and its derivative with respect to \(\Omega\) is \(2\sqrt2>0\). Hence the equation \(a_-(b,\Omega)=1\) has one local solution \(\Omega_*(b)\). Substituting \(\Omega=\Omega_c+\kappa b^2\), \(S(\Omega_c)=\sqrt{1+4\pi^2}\), yields \(\kappa=(S(\Omega_c)-1)/(2\sqrt2)\), which is strictly positive. In the small neighborhood considered, physical half-rotation is possible if and only if the lower endpoint is at most one, proving the sharp crossover. At the equality its only admissible parameter is \(a=1=a_-\), supporting one neutral orbit.

## Verification
The standalone standard-library script `check_tongue.py` numerically solves the **original two-step lift equation** independently of the series formulas. It checks window extrema, partner equality, second-order coefficients, the exactly solvable symmetric slice, the two-cycle census and multipliers, and the physical-cap crossover for multiple small nonzero couplings. Run `python3 check_tongue.py`; it reports `PASS: 93 finite boundary, profile, and stability consistency tests`. A symbolic expansion of the original two-step equations independently confirmed (1). These finite checks are corroboration only; the complete small-parameter theorem follows from the analytic argument.

## Relationship to prior work
Mugnaine, Sales, Szezech and Viana introduced this precise map in 2022, with numerical bifurcation and multistability analyses and explicit **period-one** saddle-node conditions; these conditions do not determine the half-rotation tongue. The published same-map analysis *Exact two-stage loss of invertibility in a quadratic sine-circle map* determines critical points of the lift (derivative zero), whereas the present theorem treats the separate equation \(F^2(x)=x+1\), exact two-cycle count and a physical parameter-cap crossover. The related *Quadratic Arnold-tongue onset from complementary Fourier harmonics* concerns two distinct frequencies and denominator \(q\ge3\), explicitly excluding the repeated-frequency \(q=2\) interaction here. The *Exact half-resonance tongue width and strict normalized narrowing in the sine circle map* concerns a **single** harmonic and measures detuning differently; its exact formula does not imply the combination of explicit second harmonic, constrained forcing parameter and the sharp \(\Omega_c\) crossover. General circle-map normal-form theory explains why rational tongues arise, but the specific coefficient, exact symmetric slice, and physical-cap expansion above are not among those stated results.

## Limitations
All the nontrivial interval statements are local in \(b\) near zero; no all-coupling formula, later resonance bifurcation, global basin classification, or positive-entropy claim is asserted. For the physical-cap crossover, uniqueness is local in \(\Omega\) near \(\Omega_c\), not across the entire \([-1,1]\) parameter range. Outside a period-two window, other rotation numbers and periodicities may occur. An equivalent specialization of broad normal-form results and unindexed literature could affect publication priority. The accessible abstract, but not the full text, of the related 2025 nontwist-circle paper was checked and remains a source-access risk. No independent audit is claimed.

## References
1. M. Mugnaine, M. R. Sales, J. D. Szezech Jr. and R. L. Viana, *Dynamics, multistability, and crisis analysis of a sine-circle nontwist map*, Physical Review E **106** (2022), 034203, first verified release 2022-09-06, DOI: https://doi.org/10.1103/PhysRevE.106.034203. Full author manuscript: https://fisica.ufpr.br/viana/artigos/2022/PhysRevE.106.034203.pdf.
2. *Exact two-stage loss of invertibility in a quadratic sine-circle map*, publicly accessible scientific result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-two-stage-loss-of-invertibility-in-a-quadratic-sine-circle--254e1a10099c.
3. *Quadratic Arnold-tongue onset from complementary Fourier harmonics*, publicly accessible scientific result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-quadratic-arnold-tongue-onset-from-complementary-fourier-harmoni--721f62609418.
4. *Exact half-resonance tongue width and strict normalized narrowing in the sine circle map*, publicly accessible scientific result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-half-resonance-tongue-width-and-strict-normalized-narrowin--29dcfa7c1806.
5. R. Simile Baroni et al., *Global dynamics and asymmetric fractal dimension in a nontwist circle map*, Chaos **35** (2025), 023122, DOI: https://doi.org/10.1063/5.0238699 (abstract inspected; full text not available).
