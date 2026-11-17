# Global critical predator clearance and a sign-changing logarithmic clock in an exponential ratio-response flow

## Finding
Consider the positive planar predator–prey system
\[
\dot u=u(1-u)-a v\exp(-\alpha v/u),\qquad
\dot v=dv\bigl(\exp(-\alpha v/u)-1\bigr),
\]
where \(a,\alpha,d>0\) and \(0<a\leq\alpha d\). The predator fecundity is exactly equal to its mortality \(b=d\); time and densities are those of the nondelayed, nondimensional model. For **every** \(u(0),v(0)>0\), the unique forward solution exists for all \(t\geq0\) and converges to \((1,0)\). Moreover,
\[
\lim_{t\to\infty}t\,v(t)=\frac1{d\alpha},\qquad
\lim_{t\to\infty}t[1-u(t)]=\frac{a}{d\alpha},
\]
and there is a finite real constant \(C=C(u(0),v(0);a,\alpha,d)\) such that
\[
\boxed{\frac1{v(t)}=d\alpha t+\left(a-\frac\alpha2\right)\log t+C+o(1).}
\]
The logarithmic coefficient changes sign at \(a=\alpha/2\). This cancellation is available within the stated global-attraction regime when \(d\geq1/2\); both signs occur there for every fixed \(d>1/2\). At cancellation, \(1/v(t)-d\alpha t\) has a finite limit.

## Assumptions and scope
The flow is the nondelayed reduction of the exponential ratio-dependent Holling-type-III model. The original two-rate formulation is \(\dot u=u(1-u)-a v\exp(-\alpha v/u)\), \(\dot v=b v\exp(-\alpha v/u)-d v\); this theorem fixes the nonhyperbolic invasion equality \(b=d\), with all constants positive and the **structural** bound \(a\leq\alpha d\). The bound is exactly the condition that \(z\mapsto(d+a z)\exp(-\alpha z)\) is nonincreasing for \(z\geq0\). No claim is made that it is a necessary or maximal condition for global attraction. The result concerns strictly positive initial populations, not initial states on the singular axis \(u=0\), and does not apply automatically to delayed or stochastic versions of the model.

## Proof
**1. Positivity and boundedness.** The transformation \(z=v/u>0\) is legitimate while \(u>0\). For positive initial data, \(u\) obeys
\[
\dot u=u\{1-u-a z\exp(-\alpha z)\}.
\]
The bracket is locally bounded, because \(z\exp(-\alpha z)\leq1/(\alpha e)\), so positive \(u\) cannot reach zero in finite time. Likewise \(v>0\) and \(\dot v\leq0\), and
\(\dot u\leq u(1-u)\). Hence \(u(t)\leq R(t)\), where \(\dot R=R(1-R)\), \(R(0)=u(0)\). Both populations remain bounded and the solution is global. The explicit logistic comparison also gives
\[
\int_0^\infty (u(t)-1)_+\,dt<\infty,\qquad \limsup_{t\to\infty}u(t)\leq1.
\]

**2. Global ratio decay.** Differentiating \(z=v/u\) exactly gives
\[
\dot z=z\{u-1+f(z)-d\},\qquad f(z)=(d+a z)\exp(-\alpha z).
\]
As \(f'(z)=\exp(-\alpha z)(a-\alpha d-\alpha a z)<0\) for every \(z>0\) under \(a\leq\alpha d\), we have \(f(z)<d\) for \(z>0\). Put \(J(t)=\int_0^t(u(s)-1)_+ds\) and \(Z(t)=z(t)\exp[-J(t)]\). Then
\[
\dot Z/Z=f(z)-d+(u-1)-(u-1)_+\leq f(z)-d<0.
\]
Thus \(Z\) is decreasing and has a nonnegative limit. Since \(J(t)\) converges, a strictly positive limit of \(Z\) would force \(z\) to approach a positive value, making \(\dot Z/Z\) bounded above by a negative constant for large time. This is impossible. Hence \(z(t)\to0\). The prey equation is now squeezed, for every sufficiently small \(\varepsilon>0\), between the scalar logistic growth fields \(u(1-\varepsilon-u)\) and \(u(1-u)\) after a finite time. Therefore \(u(t)\to1\), and \(v(t)=u(t)z(t)\to0\).

**3. Leading critical amplitudes.** Write \(E(z)=\exp(-\alpha z)\). The exact reciprocal derivative is
\[
\frac{d}{dt}\frac1v=d\frac{1-E(z)}v=d\frac{1-E(z)}z\frac1u\longrightarrow d\alpha.
\]
Its integral implies \(t v(t)\to1/(d\alpha)\). Setting \(w=1-u\) gives
\[
\dot w=-u w+a v E(z),\qquad
\frac{d}{dt}(w/v)=-[u+d(E(z)-1)]\,(w/v)+a E(z).
\]
The coefficient of \(w/v\) approaches \(-1\) and the forcing approaches \(a\); the elementary variation-of-constants formula yields \(w/v\to a\). This proves the second critical amplitude.

**4. Second-order control.** Let \(H=w-a v\). Direct substitution, without a center-manifold approximation, gives the exact identity
\[
\dot H=-uH+a v[(1-d)E(z)+d-u].
\]
The already proved \(w/v\to a\) and \(z\to0\) imply the bracket is \(O(v)\). Therefore \(\dot H=-uH+O(v^2)\). Since \(u\to1\), \(v(t)\sim1/(d\alpha t)\), and \(v'(t)/v(t)\to0\), variation of constants gives \(H=O(v^2)\): for large \(T\), take \(u\geq1/2\) and \(|v'/v|\leq1/8\), and bound the forcing convolution by a constant multiple of \(v(t)^2\). The initial homogeneous term decreases exponentially. Consequently
\[
1-u=a v+O(v^2),\quad \frac1u=1+a v+O(v^2).
\]

**5. The finite logarithmic renormalization.** Expanding the **exact** reciprocal derivative at \(z=v/u\to0\), with the preceding controlled remainder, yields
\[
\frac{d}{dt}\frac1v=d\alpha+d\alpha\left(a-\frac\alpha2\right)v+O(v^2).
\]
Because \(v(t)\sim1/(d\alpha t)\), integration first gives \(1/v=d\alpha t+O(\log t)\). It follows that \(v(t)-1/(d\alpha t)=O(\log t/t^2)\), an integrable error, and \(v^2\) is integrable. Integrating once more shows that the derivative of \(1/v-d\alpha t-(a-\alpha/2)\log t\) is integrable at infinity. This proves the existence of the finite \(C\) and the displayed full expansion. No limit-cycle assumption or local-basin restriction is used.

## Verification
Run `python check.py` with Python, SymPy, NumPy and SciPy. The script independently checks the symbolic derivative of \(f\), the exact \(H\)-identity, and the reciprocal-derivative expansion; it also numerically integrates three admissible parameter choices \((\alpha,d)=(1,1)\) with \(a=0.2,0.5,0.9\) to time \(10^5\), checking the two leading amplitudes and a finite-difference estimate of the logarithmic coefficient. All scripted checks passed at preparation. Finite diagnostics are **not** proofs of the global or asymptotic assertions; the five analytic steps above supply them.

## Relationship to prior work
Blyuss, Kyrychko and Kyrychko (2021) introduced the exponential ratio-dependent response and analyzed equilibria and stochastic/delay effects; their nondelayed case has the prey-only invasion threshold. Blyuss, Kyrychko and Blyuss (2022) analyzed extinction directions via a Briot–Bouquet transformation and Lambert-W roots. Those studies establish model context and standard equilibrium properties, but the inspected texts do not give global critical attraction for the monotone-ratio regime, the exact inverse-time amplitudes or the sign-changing logarithmic correction at \(b=d\). A published mathematical record on a Lambert-fold extinction direction addresses a **different** regime: its positive extinction-ratio equilibria require \((d+a z)e^{-\alpha z}=d+1\) at some \(z>0\), which cannot occur under the present condition \(a\leq\alpha d\), where the left side is at most \(d\). Similarly, results for fear–refuge flows and discrete predator–prey maps concern different equations, not parameter transformations of this flow. Searches do not establish exhaustive novelty; unindexed equivalent results are possible.

## Limitations
The condition \(a\leq\alpha d\) is sufficient, not claimed necessary, for global attraction. The asymptotic is for strictly positive initial data, and its finite constant \(C\) depends on those data; there is no closed formula claimed for \(C\). This does not settle the global phase portrait outside the monotone-ratio regime, nor delay, demographic noise, or the complementary \(b\ne d\) cases.

## References
1. K. B. Blyuss, S. N. Kyrychko and Y. N. Kyrychko, *Time-delayed and stochastic effects in a predator–prey model with ratio dependence and Holling type III functional response*, *Chaos* **31** (2021), 073141, https://doi.org/10.1063/5.0055623. Lawful author-manuscript copy: https://sro.sussex.ac.uk/id/eprint/102126/.
2. K. B. Blyuss, Y. N. Kyrychko and O. B. Blyuss, *Complex dynamics near extinction in a predator-prey model with ratio dependence and Holling type III functional response*, *Frontiers in Applied Mathematics and Statistics* **8** (2022), 1083815, https://doi.org/10.3389/fams.2022.1083815. Preprint: https://arxiv.org/abs/2305.04053.
