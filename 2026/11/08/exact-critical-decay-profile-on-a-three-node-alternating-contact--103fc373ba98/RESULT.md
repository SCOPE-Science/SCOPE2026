# Exact critical decay profile on a three-node alternating-contact SIS path

## Finding

For the deterministic continuous-time susceptible–infected–susceptible (SIS) nodewise mean-field dynamics on the three-node path with only edge \(1\!\!\leftrightarrow\!\!2\) active for one half-period and only edge \(2\!\!\leftrightarrow\!\!3\) active for the next, the linear threshold has an exact scalar form. More substantially, **at this threshold every nonzero nonnegative infection state has the same phase-dependent reciprocal-time asymptotic profile, with an explicitly evaluable positive amplitude coefficient**. Below threshold all infection states vanish; above threshold a unique strictly positive periodic endemic state attracts every nonzero state.

Write \(F(x)=\operatorname{arcosh}((1+\cosh x)/2)\). With infection rate \(\beta>0\), recovery rate \(\gamma>0\), and each active edge held for \(h>0\), the principal linear growth rate is
\[
\Lambda(h)=-\gamma+\frac{F(\beta h)}h.
\]
If \(1/\sqrt2<\gamma/\beta<1\), there is a unique \(h_c>0\) with \(\Lambda(h_c)=0\). At that value, put \(T=2h_c\), let \(\Phi(t,s)\) denote the linear fundamental matrix, and normalize the strictly positive right and left Perron vectors \(Mv=v\), \(w^{\mathsf T}M=w^{\mathsf T}\) of \(M=\Phi(T,0)\) by \(\sum_i v_i=1\) and \(w^{\mathsf T}v=1\). Define \(z(t)=\Phi(t,0)v\) and \(w(t)=\Phi(T,t)^{\mathsf T}w\), both extended periodically. Then every \(p(0)\in[0,1]^3\setminus\{0\}\) satisfies
\[
\lim_{t\to\infty}\left\|t\,p(t)-\frac{T}{q}z(t\bmod T)\right\|=0,
\qquad q=\beta\int_0^T w(t)^{\mathsf T}\operatorname{diag}(z(t))A(t)z(t)\,dt>0.
\]
Here and below the limit is in the sense of the norm of the difference to the periodic expression at the actual phase \(t\bmod T\); it does not assert a constant-vector limit independent of phase.

The integral is an elementary **closed expression**, not a numerical prescription. Set \(r=e^{-\gamma h_c}\), \(c=\cosh(\beta h_c)\), and \(s=\sinh(\beta h_c)\). The neutral identity \(F(\beta h_c)=\gamma h_c\) gives \(c=r+r^{-1}-1\), and hence \(B=rs/(1-r)=r^2s/(1-rc)\). Then
\[
 v=\frac{(r,B,1)^{\mathsf T}}{r+B+1},\qquad
 w=\frac{(1,B,r)^{\mathsf T}}{(1,B,r)v}.
\]
With \(D=\beta-\gamma\), \(E=3\beta+\gamma\), \(J_+=(e^{Dh_c}-1)/D\), \(J_-=(1-e^{-Eh_c})/E\), \(J_c=(J_++J_-)/2\) and \(J_s=(J_+-J_-)/2\),
\[
\boxed{q=2\beta(w_1+w_2)\left[\frac{v_1^2+v_2^2}{2}J_s+v_1v_2J_c\right].}
\]
The restriction \(\gamma/\beta<1\) ensures \(D>0\). In particular, the coefficient is finite and positive.

## Assumptions and scope

The model is the continuous-time deterministic nodewise mean-field (NIMFA) equation
\[
\dot p_i=-\gamma p_i+\beta(1-p_i)\sum_{j=1}^3A_{ij}(t)p_j,\quad i=1,2,3,
\quad p_i(0)\in[0,1],
\]
with \(A(t+2h)=A(t)\), \(A(t)=A_1\) for \(0\le t\bmod 2h<h\), and \(A(t)=A_2\) for \(h\le t\bmod2h<2h\), where
\[
 A_1=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
 A_2=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]
The vector field is continuous within each half-period, piecewise continuous in time, and forward-invariant on \([0,1]^3\). No stochastic-individual epidemic or random-contact assertion is made. The critical asymptotic assertion concerns \(1/\sqrt2<\gamma/\beta<1\) and \(h=h_c\); for other ratios, \(\Lambda\) has a fixed sign at every finite \(h>0\).

## Proof

**1. Exact threshold and simplicity.** The linearization at zero has half-period propagators \(e^{-\gamma h}e^{\beta h A_1}\) and \(e^{-\gamma h}e^{\beta h A_2}\). Writing \(c=\cosh(\beta h)\) and \(s=\sinh(\beta h)\), their undamped product is
\[
 H=e^{\beta h A_2}e^{\beta h A_1}=
 \begin{pmatrix}c&s&0\\cs&c^2&s\\s^2&cs&c\end{pmatrix}.
\]
Using \(s^2=c^2-1\), its characteristic polynomial is \((X-1)(X^2-(c^2+2c-1)X+1)\). Hence the eigenvalues of the full propagator \(M=e^{-2\gamma h}H\) are \(e^{-2\gamma h}\) and \(e^{-2\gamma h\pm2F(\beta h)}\). Both the half-step maps together connect all three vertices, so \(M\) is primitive (indeed strictly positive in sufficient powers) and its largest multiplier is simple. Direct differentiation yields
\[
F'(x)=\sqrt{\frac{\cosh x+1}{\cosh x+3}},\qquad F''(x)>0\quad(x>0).
\]
Consequently \(F(x)/x\) strictly increases from \(1/\sqrt2\) to \(1\). This proves the unique crossover and all stated off-critical signs. Notice that this linear threshold is an instance of the established temporal-network propagator method; it is not asserted as a new general spectral principle.

**2. Nonlinear dynamics away from criticality.** The Poincaré map \(\mathcal P:[0,1]^3\to[0,1]^3\) is order-preserving and maps every nonzero vector to a strictly positive vector after a bounded number of periods. For \(0<\alpha<1\) and \(x\gg0\), its strict subhomogeneity \(\mathcal P(\alpha x)\gg\alpha\mathcal P(x)\) follows by comparing \(\alpha p(t;x)\) with the solution from \(\alpha x\): the latter satisfies a strictly larger cooperative vector field because the quadratic loss is multiplied by \(\alpha^2\) rather than \(\alpha\). For \(\rho(M)<1\), nonlinear solutions are componentwise bounded above by \(\Phi(t,0)p(0)\), and converge exponentially to zero. For \(\rho(M)>1\), sufficiently small positive multiples of the Perron eigenvector form strict subsolutions under \(\mathcal P\), while \((1,1,1)\) is a supersolution. Monotone iteration yields an interior fixed point, hence a strictly positive periodic endemic solution. If two interior fixed points differed, scaling one against the other until first contact and using strong order preservation with strict subhomogeneity would contradict maximality of the scale factor. The same lower–upper squeezing, after every nonzero trajectory becomes positive, proves global convergence to this unique periodic orbit.

**3. Global critical extinction.** At \(\rho(M)=1\), the periodic adjoint \(w(t)\gg0\) obeys \(\dot w(t)=-(-\gamma I+\beta A(t))^{\mathsf T}w(t)\). Along any nonlinear orbit,
\[
\frac{d}{dt}[w(t)^{\mathsf T}p(t)]=
-\beta w(t)^{\mathsf T}\operatorname{diag}(p(t))A(t)p(t)\le0.
\]
For every nonzero state there is a positive time interval within a complete period on which an active adjacent pair is strictly infected, so this derivative is strictly negative there. The continuous period-time decrease and compactness of \([0,1]^3\) force the weighted quantity at successive periods to approach zero: otherwise a convergent subsequence with positive limit would have a strictly positive loss over one period, contrary to convergence of the weighted sequence. Since \(w(0)\gg0\), the entire state converges to zero; the uniform flow bounds between period samples extend the conclusion to all real times.

**4. Nonlinear critical amplitude.** Smooth dependence of the half-step flows gives, uniformly for small \(x\),
\[
\mathcal P(x)=Mx-\beta\int_0^T\Phi(T,t)\operatorname{diag}(\Phi(t,0)x)A(t)\Phi(t,0)x\,dt+O(\|x\|^3).
\]
At criticality the other two multipliers of \(M\) are strictly inside the unit circle. Define \(r_n=w^{\mathsf T}p(nT)>0\), and decompose \(p(nT)=r_n v+y_n\) with \(w^{\mathsf T}y_n=0\). The stable-complement recursion is contractive up to quadratic forcing, while \(r_n\downarrow0\) with \(r_{n+1}/r_n\to1\). Indeed, \(\|p(nT)\|\le Cr_n\) by positivity of \(w\), so in a norm with stable-complement contraction \(\theta<1\), the ratio \(d_n=\|y_n\|/r_n\) satisfies \(d_{n+1}\le(\theta d_n+Cr_n)/(1-Cr_n)\), and therefore \(d_n\to0\). Thus \(p(nT)/r_n\to v\). Projecting the quadratic Taylor expansion with \(w^{\mathsf T}\) gives
\[
 r_{n+1}=r_n-q r_n^2+o(r_n^2),
\]
with the stated integral for \(q>0\). Taking reciprocal differences yields \(1/r_{n+1}-1/r_n\to q\), and hence \(nr_n\to1/q\). Evolving during a bounded phase \(0\le t<T\) gives \(p(nT+t)=r_n z(t)+o(r_n)\) uniformly in \(t\), which yields \(t p(t)\to (T/q)z(t\bmod T)\) in the asserted phase-dependent sense.

**5. Elementary evaluation of \(q\).** Reflection \(R(p_1,p_2,p_3)=(p_3,p_2,p_1)\) conjugates the first and second half-period vector fields. Uniqueness of the normalized positive critical neutral mode implies \(z(t+h)=Rz(t)\) and \(w(t+h)=Rw(t)\). Solving the half-period eigenvector relations gives the displayed \(v,w\). On the first half, \(w_1(t)+w_2(t)=e^{(\gamma-\beta)t}(w_1+w_2)\) and
\[
 z_1(t)z_2(t)=e^{-2\gamma t}\left[\frac{v_1^2+v_2^2}{2}\sinh(2\beta t)+v_1v_2\cosh(2\beta t)\right].
\]
Since the nonlinear loss on that half is \(\beta(w_1(t)+w_2(t))z_1(t)z_2(t)\), symmetry doubles this integral. Integrating exponentials \(e^{(\beta-\gamma)t}\) and \(e^{-(3\beta+\gamma)t}\) exactly gives the claimed \(J_s,J_c\) expression. Positivity also follows directly from the strictly positive integrand on each open half-period.

## Verification

The standalone file `verify.py` requires Python 3 with SymPy, NumPy, and SciPy. Run `python verify.py`. It checks the monodromy characteristic polynomial and strict-derivative formula symbolically; at \((\beta,\gamma)=(1,4/5)\) it computes \(h_c\approx3.0349084276605\), verifies positive normalized left and right eigenvectors, confirms the closed-form \(q\) equals high-order quadrature of its defining integral, and numerically checks the \(n^{-1}\) Poincaré decay after 1500 full periods. The computed coefficient is \(q\approx1.924264168024\). Numerical trajectories corroborate but do not prove the infinite-time result, which follows from Steps 3–4.

## Relationship to prior work

General infection-propagator formulas for temporal SIS networks, and the broad observation that longer temporal contacts can facilitate endemicity, appear in Speidel, Klemm, Eguíluz and Masuda (2016) and Valdano and collaborators (2015, 2017). The exact spectral threshold here is an illustrative special calculation within that earlier framework. Persoons, Sensi, Prasse and Van Mieghem (first public 2023) study time-scale separation for time-varying NIMFA, but not the critical three-node phase law. Cai, Nie and Holme (first public 2023) analyze activity-driven SIS temporal criticality with stochastic contact correlations rather than this deterministic path. Ait Rami and collaborators (2013) establish broad stability and periodic-orbit principles for switched SIS systems; Prasse and Van Mieghem (2020) analyze a near-threshold time-independent NIMFA system. These results cover portions of the surrounding general theory, but do not in their examined statements provide the displayed phase-specific nonlinear amplitude. This note's specifically assessed contribution is the **global, phase-resolved critical \(t^{-1}\) law and closed model-specific nonlinear coefficient**, with the off-critical global classification as context. A similar inverse-time *exponent* in a different epidemic system is not by itself an originality claim.

## Limitations

This is a deterministic nodewise approximation, not the finite-population stochastic SIS Markov chain; the latter can become extinct regardless of a mean-field positive periodic state. The positive periodic solution's entire nonlinear orbit has no elementary formula asserted. The critical asymptotic is local in the rate ratio in the sense that critical \(h_c\) exists only for \(1/\sqrt2<\gamma/\beta<1\), but holds for every nonzero admissible infection state at that critical parameter. No finite stochastic outbreak probability, finite-size noise scaling, or arbitrary switching-graph generalization is proved. Publication-priority uncertainty remains for unindexed equivalent formulations or general critical-asymptotic theorems with a direct ready-made specialization.

## References

- Persoons, R., Sensi, M., Prasse, B., Van Mieghem, P., *Transition from time-variant to static networks: timescale separation in NIMFA SIS epidemics*, arXiv:2305.12446, first public 2023-05-21. https://arxiv.org/abs/2305.12446
- Ait Rami, M., Bokharaie, V. S., Mason, O., Wirth, F. R., *Stability Criteria for SIS Epidemiological Models under Switching Policies*, arXiv:1306.0135, first public 2013-06-01. https://arxiv.org/abs/1306.0135
- Prasse, B., Van Mieghem, P., *Time-dependent solution of the NIMFA equations around the epidemic threshold*, Journal of Mathematical Biology (2020). https://doi.org/10.1007/s00285-020-01542-6
- Cai, C.-R., Nie, Y.-Y., Holme, P., *The nature of epidemic criticality in temporal networks*, arXiv:2311.12175, first public 2023-11-20. https://arxiv.org/abs/2311.12175
- Speidel, L., Klemm, K., Eguíluz, V. M., Masuda, N., *Temporal interactions facilitate endemicity in the susceptible-infected-susceptible epidemic model*, arXiv:1602.00859, first public 2016-02-02. https://arxiv.org/abs/1602.00859
- Valdano, E., Ferreri, L., Poletto, C., Colizza, V., *Analytical computation of epidemic threshold on temporal networks*, arXiv:1406.4815. https://arxiv.org/abs/1406.4815
- Valdano, E., Re Fiorentin, M., Poletto, C., Colizza, V., *Epidemic Threshold in Continuous-Time Evolving Networks*, arXiv:1706.05968. https://arxiv.org/abs/1706.05968
- Sanatkar, M. R. et al., *Epidemic threshold of an SIS model in dynamic switching networks*, arXiv:1501.02472. https://arxiv.org/abs/1501.02472
