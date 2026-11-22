# Sharp frequency-reversal capacity of positive parallel catchment pathways

## Finding

**Theorem (sharp reversal capacity and realization).** Fix an integer \(m\ge2\), distinct relaxation times \(0<\tau_1<\cdots<\tau_m\), and a strictly positive discharge-weight vector \(q=(q_1,\ldots,q_m)\). Each unit pathway is driven by the same small-amplitude harmonic input and obeys
\[
\tau_j\dot z_j+z_j=\cos(\omega t),\qquad \omega>0.
\]
Use its unique periodic solution and put \(Q(t)=Q_0+\eta\sum_j q_jz_j(t)\), \(C(t)=C_0+\eta\sum_j c_jz_j(t)\), where \(c_j>0\) and \(\eta>0\). Define signed concentration–discharge loop area by \(\mathcal A(\omega)=\oint Q\,dC\), with positive sign denoting counterclockwise traversal of the \((Q,C)\) plane.

For nonproportional strictly positive \(c\) and \(q\), the sign of \(\mathcal A(\omega)\) can reverse at **no more than \(m-2\) distinct positive forcing frequencies**. For \(m=2\) it cannot reverse. This bound is sharp for every \(m\ge3\) in a strong prescribed-frequency sense: for **every** chosen set of \(m-2\) distinct frequencies \(\omega_1,\ldots,\omega_{m-2}>0\), there exists a strictly positive \(c\), with the original fixed \(q\) and \(\tau\), for which these are exactly the sign-reversal frequencies, all simple. In fact every real polynomial of degree at most \(m-2\) can be realized, up to an arbitrarily small positive scalar, as the frequency-polynomial numerator of the signed area.

Thus observing \(r\) distinct orientation reversals as forcing frequency changes demands at least \(r+2\) distinct first-order response pathways **within this model**, without implying that distinct physical pathways can be uniquely recovered from field data.

## Assumptions and scope

All weights \(q_j,c_j\), time constants \(\tau_j\), and frequencies are real and strictly positive, with the time constants pairwise distinct. The dynamics are uncoupled, stable first-order linear reservoirs receiving a *common* sinusoidal forcing. The outputs are two different affine combinations of their periodic states; concentrations can be kept positive by choosing \(C_0>\eta\sum_j c_j\) and discharge by \(Q_0>\eta\sum_j q_j\), since \(|z_j(t)|\le1\). They are idealized linear **response signals**, not a mass-conserving ratio of pollutant mass to water discharge. The oriented ellipse is followed for one period after all transients have vanished. The frequency \(\omega\) is varied while all pathway weights and time constants remain fixed. No stochastic forcing, state-dependent chemical kinetics, nonlinear mixing, or observed storm hydrographs are assumed.

## Proof

**1. Exact area and polynomial bound.** The periodic response is
\[
z_j(t)=\frac{\cos(\omega t)+\omega\tau_j\sin(\omega t)}{1+\omega^2\tau_j^2}.
\]
Writing \(s=\omega^2\) and using \(\int_0^{2\pi} \cos^2\theta\,d\theta=\int_0^{2\pi}\sin^2\theta\,d\theta=\pi\) yields
\[
\mathcal A(\omega)=\pi\eta^2\omega\sum_{1\le i<j\le m}\frac{(q_i c_j-q_j c_i)(\tau_j-\tau_i)}{(1+s\tau_i^2)(1+s\tau_j^2)}.
\]
Set
\[
D(s)=\prod_{k=1}^m(1+s\tau_k^2),\qquad
N_c(s)=\sum_{i<j}(q_i c_j-q_j c_i)(\tau_j-\tau_i)\prod_{k\ne i,j}(1+s\tau_k^2).
\]
Then \(\mathcal A(\omega)=\pi\eta^2\omega N_c(s)/D(s)\). The denominator is positive for \(s\ge0\), and \(N_c\) has degree at most \(m-2\). Unless the polynomial is identically zero, there can therefore be at most \(m-2\) distinct positive zeros, hence at most as many positive-frequency orientation reversals.

**2. Rigidity of zero area.** Define the real rational functions
\[
H_q(z)=\sum_{j=1}^m\frac{q_j}{1+\tau_jz},\qquad
H_c(z)=\sum_{j=1}^m\frac{c_j}{1+\tau_jz}.
\]
Because \(q_j>0\), \(\operatorname{Re}H_q(i\omega)=\sum_jq_j/(1+\omega^2\tau_j^2)>0\). If \(N_c\equiv0\), the area identity means \(H_c(i\omega)/H_q(i\omega)\) is real for every \(\omega>0\). The quotient \(R(z)=H_c(z)/H_q(z)\) has real coefficients and therefore satisfies \(R(i\omega)=R(-i\omega)\) for infinitely many arguments. Rational identity gives \(R(z)=R(-z)\).

Let \(D_0(z)=\prod_j(1+\tau_jz)\) and \(P_q(z)=D_0(z)H_q(z)\). The function \(H_q(x)\) is strictly decreasing on each real interval avoiding its distinct negative poles \(-1/\tau_j\), since \(H_q'(x)=-\sum_j q_j\tau_j/(1+\tau_jx)^2<0\). Between any two successive poles it goes from \(+\infty\) to \(-\infty\), hence has one simple negative zero. These are all \(m-1\) zeros of the degree-\(m-1\) polynomial \(P_q\). Thus all possible poles of \(R=P_c/P_q\) are negative real numbers. But an even rational function cannot have a pole at a negative point without one at the opposite positive point. Hence all poles are removable and \(R\) is a polynomial. As both \(P_c\) and \(P_q\) have degree at most \(m-1\), while \(P_q\) has degree exactly \(m-1\), \(R\) must be constant. Comparing residues at the distinct poles of \(H_q\) and \(H_c\) gives \(c_j=\lambda q_j\) for every \(j\).

Conversely, proportional weights trivially give \(N_c\equiv0\). Therefore the real-linear map \(c\mapsto N_c(s)\) has kernel precisely \(\operatorname{span}(q)\), of dimension one.

**3. Sharp arbitrary-frequency realization.** The codomain of that map is the \((m-1)\)-dimensional space of real polynomials of degree at most \(m-2\). Rank–nullity applied to the \(m\)-dimensional weight space and the one-dimensional kernel establishes surjectivity. Given distinct prescribed positive frequencies, choose a real vector \(v\) satisfying
\[
N_v(s)=\prod_{\ell=1}^{m-2}(s-\omega_\ell^2).
\]
For sufficiently small \(\varepsilon>0\), every entry of \(c=q+\varepsilon v\) is positive, while \(N_c=\varepsilon N_v\), because \(N_q\equiv0\). The given roots are positive, distinct, simple, and exhaust all possible roots. Since the denominator stays positive, the signed area changes sign at every one, proving sharpness. The same argument works for any target polynomial of degree at most \(m-2\).

**4. Exact examples.** For \(m=3\), take
\[
(\tau_1,\tau_2,\tau_3)=(1,2,4),\quad q=(1,1/2,1),\quad c=(1/2,1,1/2).
\]
Direct expansion yields \(N_c(s)=-3/4+(21/2)s\), so the unique reversal occurs at \(\omega=1/\sqrt{14}\): clockwise below and counterclockwise above. For \(m=4\), choose
\[
\tau=(1,2,3,4),\quad q=(1,1,1,1),\quad c=(469/760,373/475,519/3800,1).
\]
The numerator is exactly \(N_c(s)=s^2-(5/2)s+1=(s-1/2)(s-2)\); the signed area switches twice, at \(\omega=1/\sqrt2\) and \(\omega=\sqrt2\).

## Verification

Run `python3 checker.py` with Python 3 using only its standard library. The checker constructs the area numerator from exact rational arithmetic, confirms both displayed polynomials and their rational roots, checks that sample surjectivity matrices have rank \(m-1\) for \(2\le m\le10\), and directly integrates the periodic loop numerically for selected frequencies in the two-, three-, and four-pathway cases. The test run passed 48 assertions/comparisons. These finite tests are *illustrations and algebra checks*; the preceding rank and interlacing arguments establish the universal theorem without any finite-enumeration inference.

## Relationship to prior work

Concentration–discharge hysteresis has been analyzed to infer flow pathways and nutrient transport. Evans and Davies (1998) study different hysteresis forms using two- and three-component runoff mixing; Hornberger, Scanlon, and Raffensperger (2001) emphasize the effects of hydrological and chemical timescales; Outram et al. (2014) analyze observed nutrient responses across storm events; Lloyd et al. (2016) investigate the robustness of empirical hysteresis indices. These studies motivate the question, but the materials inspected do not establish the present **frequency-indexed, linear-reservoir polynomial root count and positive-weight realization theorem**. In particular, the distinction from the earlier two-versus-three-component result is between loop **shape within an event** and the number of **direction reversals across changing forcing frequencies** for fixed model parameters. Complete text of Evans–Davies (1998) and Hornberger et al. (2001) was not available for final comparison, so historical priority is provisional. This result is an exact conditional mathematical statement, not a claim that the model is fitted to those catchments.

## Limitations

The result does not give an inverse reconstruction of the number of actual physical runoff paths: the \(r+2\) statement is a necessary bound *within the assumed shared-input first-order model*. It does not apply to non-sinusoidal single storm events, unequal inputs between pathways, finite transient windows, nonlinear concentration-as-mass-over-flow, distinct pole multiplicities, or changing pathway weights. Even if the signed area is zero at one frequency, the two output time series may be nonconstant and in phase; no within-cycle figure-eight is predicted because each steady single-frequency plot is an ellipse or degenerate line. The exact rank argument requires positive discharge weights and distinct relaxation times. The mathematical correctness is supported by the proof and reproducible arithmetic; no independent scientific audit or literature-priority certification has been performed.

## References

1. Evans, C. and Davies, T. D. (1998). *Causes of concentration/discharge hysteresis and its potential as a tool for analysis of episode hydrochemistry*. Water Resources Research 34, 129–137. https://doi.org/10.1029/97WR01881
2. Hornberger, G. M., Scanlon, T. M. and Raffensperger, J. P. (2001). *Modelling transport of dissolved silica in a forested headwater catchment: the effect of hydrological and chemical time scales on hysteresis in the concentration–discharge relationship*. Hydrological Processes 15, 2029–2038. https://doi.org/10.1002/hyp.254
3. Outram, F. N., et al. (2014). *High-frequency monitoring of nitrogen and phosphorus response in three rural catchments to the end of the 2011–2012 drought in England*. Hydrology and Earth System Sciences 18, 3429–3448. https://doi.org/10.5194/hess-18-3429-2014
4. Lloyd, C. E. M., Freer, J. E., Johnes, P. J., and Collins, A. L. (2016). *Technical Note: Testing an improved index for analysing storm discharge–concentration hysteresis*. Hydrology and Earth System Sciences 20, 625–632. https://doi.org/10.5194/hess-20-625-2016
