# An exact persistence window from desynchronizing two-patch population control

## Finding
For a positive two-patch population system with fixed, patch-specific periodic removal fractions, simultaneous control **uniquely minimizes** the principal annual growth multiplier among all relative offsets of the two pulses. Exactly half-period spacing **uniquely maximizes** that multiplier. The statement holds without equal dispersal rates, equal patch growth rates, or equal removal fractions. The excess trace has the exact factorization
\[
\operatorname{tr}Q_\tau-\operatorname{tr}Q_0
=\frac{(1-p_1)(1-p_2)bc\,e^{(a+d)T/2}}{\chi^2}
\sinh(\chi\tau)\sinh(\chi(T-\tau)),
\quad \chi=\sqrt{(a-d)^2/4+bc}.
\]
For a simultaneously controlled population below its extinction threshold, this formula gives either stability at every offset, a single neutral midpoint, or **one exact open interval of offsets causing population persistence**. A completely rational Floquet certificate realizes extinction for simultaneous control and persistence for midpoint-staggered control with precisely the same intervention fractions and frequency.

## Assumptions and scope
Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) be a constant real matrix with \(b,c>0\); \(a,d\in\mathbb R\). Let \(T>0\), \(0<p_1,p_2<1\), and \(0\le\tau\le T\). There are two spatially coupled population abundances \(u=(u_1,u_2)^\top\in\mathbb R_{\ge0}^2\). Between interventions they satisfy either the linear system \(\dot u=Au\), or the nonlinear common-crowding system
\[
\dot u=Au-\kappa(u_1+u_2)u,\qquad \kappa>0.
\]
At integer multiples of \(T\), the first population is multiplied by \(p_1\) and the second is unchanged; a time \(\tau\) later, the second is multiplied by \(p_2\) and the first is unchanged. Write \(D_1=\operatorname{diag}(p_1,1)\) and \(D_2=\operatorname{diag}(1,p_2)\). A pulse at \(\tau=0\) or \(T\) coincides modulo the period with the other pulse. Census states are taken immediately before the first pulse, so the one-period linear map is
\[
Q_\tau=e^{A(T-\tau)}D_2e^{A\tau}D_1.
\]
Set \(\theta=(a+d)/2\), \(\delta=(a-d)/2\), \(\chi=\sqrt{\delta^2+bc}>0\),
\[
C=\frac{(1-p_1)(1-p_2)bc\,e^{\theta T}}{\chi^2}>0,\qquad H=\sinh^2(\chi T/2).
\]
Growth or decline means the principal Floquet multiplier \(\rho(Q_\tau)\) is respectively above or below one; at equality the linear dynamics are critical. Statements about global persistence below concern only the specified shared-crowding nonlinear completion, not general nonlinear growth laws or climate-dependent multistage vector models.

## Proof
**Trace, determinant, and unique optimum.** The matrix exponential is
\[
e^{At}=e^{\theta t}\left[\cosh(\chi t)I+\frac{\sinh(\chi t)}{\chi}(A-\theta I)\right].
\]
To verify the nontrivial trace factorization, put \(s=T-\tau\), \(c_t=\cosh(\chi t)\), and \(s_t=\sinh(\chi t)\). Direct multiplication gives
\[
\begin{aligned}
e^{-\theta T}\operatorname{tr}Q_\tau
={}&(p_1+p_2)c_sc_\tau
+\frac{\delta(p_1-p_2)}\chi(c_ss_\tau+s_sc_\tau)\\
&+\frac{(p_1+p_2)\delta^2+(1+p_1p_2)bc}{\chi^2}s_ss_\tau.
\end{aligned}
\]
At \(\tau=0\), the corresponding trace is
\[
e^{-\theta T}\operatorname{tr}Q_0=(p_1+p_2)\cosh(\chi T)
+\frac{\delta(p_1-p_2)}\chi\sinh(\chi T).
\]
Using the addition formulas for \(\sinh\) and \(\cosh\) and \(\chi^2=\delta^2+bc\), the difference reduces to exactly \((1-p_1)(1-p_2)bc\,s_ss_\tau/\chi^2\) after multiplication by \(e^{\theta T}\). Independently, the determinant is offset-independent:
\[
\det Q_\tau=p_1p_2e^{(a+d)T}=:h>0.
\]
Every \(Q_\tau\) is entrywise positive because \(b,c,T,p_1,p_2>0\). Its two eigenvalues are distinct and positive (positive discriminant and positive determinant); the larger is
\[
\rho(Q_\tau)=\frac{\operatorname{tr}Q_\tau+\sqrt{(\operatorname{tr}Q_\tau)^2-4h}}2.
\]
At fixed \(h\) this expression is strictly increasing in the trace. The product of the two positive hyperbolic sines is zero exactly at the endpoints and strictly increases to the midpoint before strictly decreasing thereafter, since
\[
\sinh(\chi\tau)\sinh(\chi(T-\tau))
=\tfrac12[\cosh(\chi T)-\cosh(\chi(T-2\tau))].
\]
Thus simultaneous pulses minimize the growth multiplier, and the midpoint uniquely maximizes it among the nonsynchronous offsets.

**Complete offset-dependent extinction threshold.** Assume \(\rho(Q_0)<1\), and define \(\Delta=\det(I-Q_0)=1-\operatorname{tr}Q_0+h>0\), \(L=\Delta/C>0\). Then \(0<h<1\). Since the smaller eigenvalue stays below one, \(\rho(Q_\tau)\lessgtr1\) precisely when \(\det(I-Q_\tau)\gtrless0\). The trace identity gives
\[
\det(I-Q_\tau)=\Delta-C\sinh(\chi\tau)\sinh(\chi(T-\tau)).
\]
If \(L>H\), all offsets have principal multiplier below one. If \(L=H\), only \(\tau=T/2\) is critical and all other offsets have multiplier below one. If \(0<L<H\), put
\[
\tau_\pm=\frac12\left[T\pm\frac1\chi
\operatorname{arcosh}\left(\cosh(\chi T)-2L\right)\right].
\]
The expression inside \(\operatorname{arcosh}\) lies strictly between \(1\) and \(\cosh(\chi T)\); hence \(0<\tau_-<T/2<\tau_+<T\). The principal multiplier is greater than one precisely on \((\tau_-,\tau_+)\), equal to one at the endpoints, and below one elsewhere. This is both necessary and sufficient.

**Nonlinear population interpretation.** Let \(\Phi_\tau(t)\) denote the positive linear evolution from the census just before the first pulse to the time \(t\in(0,T)\), including pulses occurring before \(t\). Write the positive row vector
\[
k_\tau^\top=\int_0^T\mathbf1^\top\Phi_\tau(s)\,ds.
\]
The common-crowding equation has the exact integrating-factor solution between and across pulses,
\[
u(t)=\frac{\Phi_\tau(t)u_0}{1+\kappa\int_0^t\mathbf1^\top\Phi_\tau(s)u_0\,ds}.
\]
Consequently the census Poincare map is \(F_\tau(u)=Q_\tau u/(1+\kappa k_\tau^\top u)\) and its \(n\)-fold iterate is
\[
F_\tau^n(u)=\frac{Q_\tau^n u}{1+\kappa\sum_{j=0}^{n-1}k_\tau^\top Q_\tau^j u}.
\]
Let \(v\gg0\) be any Perron eigenvector of \(Q_\tau\). If \(\rho(Q_\tau)<1\), every nonzero nonnegative orbit converges exponentially to extinction. If \(\rho(Q_\tau)>1\), every nonzero nonnegative orbit converges to the unique positive periodic orbit, whose census state is
\[
u_* =\frac{\rho(Q_\tau)-1}{\kappa k_\tau^\top v}\,v.
\]
At equality, there is no positive periodic state, and every nonzero nonnegative orbit has the sharp critical census law
\[
\lim_{n\to\infty}nF_\tau^n(u)=\frac{v}{\kappa k_\tau^\top v}.
\]
These follow by the spectral decomposition of the strictly positive two-by-two matrix and summing its Perron component. Positivity of \(Q_\tau\) ensures that every nonzero nonnegative initial vector has a strictly positive Perron projection. The within-period trajectory is obtained by substituting the corresponding census state in the explicit integrating-factor formula.

**An exact reversal certificate.** Set
\[
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad T=\log 2,
\quad p_1=p_2=\frac{12}{25},\quad\kappa>0.
\]
With simultaneous control, \(e^{AT}=\begin{pmatrix}5/4&3/4\\3/4&5/4\end{pmatrix}\), so \(Q_0=(12/25)e^{AT}\), whose principal multiplier is \(24/25<1\). At half-period separation, \(e^{AT/2}=(2\sqrt2)^{-1}\begin{pmatrix}3&1\\1&3\end{pmatrix}\), whence
\[
Q_{T/2}=\begin{pmatrix}711/1250&111/200\\333/1250&133/200\end{pmatrix},
\quad \operatorname{tr}Q_{T/2}=\frac{6169}{5000},
\quad \det Q_{T/2}=\frac{144}{625}.
\]
Therefore \(\det(I-Q_{T/2})=-17/5000<0\) and \(\rho(Q_{T/2})>1\). More precisely, \(\Delta=19/625\), \(C=169/625\), and \(H=1/8\), so the persistence interval has **exact endpoints**
\[
\tau_\pm=\tfrac12[\log 2\pm\operatorname{arcosh}(693/676)].
\]
Thus the synchronized nonlinear system goes extinct from every nonzero nonnegative initial population, while the otherwise identical half-staggered system tends to one strictly positive periodic population profile. Every sign in this reversal is exact rational arithmetic.

## Verification
Run `python3 verify.py`. It verifies the rational reversal (all four entries, characteristic quantities and strict inequalities), the analytic trace/determinant identity over multiple independent asymmetric two-patch parameter choices and offsets, positivity of the predicted stability ordering, and the exact equality of the midpoint hyperbolic maximum. Finite numerical tests support the algebra but do not replace the complete algebraic and Perron–Frobenius proofs above. The analytic results apply to all real parameter values satisfying the stated inequalities; the code tests only selected values.

## Relationship to prior work
Bhowmick, Irwin, Lopez, Fritz, and Lee Smith (2025) investigate patch-connected *Culex* population dynamics and spatially coordinated interventions, including pulsed spraying, by numerical simulations in a weather- and stage-dependent model. Their work motivates comparing patchwise pulse timings. The present theorem studies a distinct, analytically solvable constant-coefficient, two-abundance abstraction and neither analyzes nor claims a theorem for their full multistage system. Gao, Lietman, Dong, and Porco (2017) already show the qualitative advantage of synchronized mass treatment in a homogeneous epidemic model; that qualitative principle is not claimed new. Terry (2010) studies independently planned culling on two patches of a delay-structured pest population; that work derives eradication sufficient conditions and explicitly discusses simultaneous culling, but does not state the sharp formula for varying the relative timing of two fixed-strength diagonal removals. Georgescu, Dimitriu, and Sinclair (2010) use Floquet theory for dispersing two-patch pests with biological releases offset from joint pesticide spraying. Their pulse configuration and invasion criterion do not state this pair of independently timed patch-removal matrices or the sharp midpoint stability window. Courcelle, MacDonald, and Patel (2026) provide general periodic-pulse permanence theory; here the contribution is an explicit all-parameter trace comparison and exactly solvable phase threshold. Standard positive-matrix and Floquet facts are treated as established tools, not new discoveries.

## Limitations
The statements require fixed \(A\) with strictly positive off-diagonal coefficients, exactly one fixed removal fraction per patch per period, and no seasonal drift in the between-pulse generator. The global nonlinear conclusion requires precisely shared scalar quadratic crowding. It does not apply without proof to independent logistic crowding, multiple life stages, time-varying weather, stochastic individual outcomes, or epidemiological control budgets in which pulse efficacy changes with timing. The sharp equivalence at the threshold concerns the chosen deterministic map. Prior art on operator products or independently timed spatial interventions may imply part of the exact formula; this remains an originality risk pending independent review.

## References
1. S. Bhowmick, P. Irwin, K. Lopez, M. L. Fritz, and R. L. Smith, *A mathematical model of Culex population abundance and the impact of vector control interventions in a patchy environment* (first public December 9, 2025), arXiv:2512.08842. https://arxiv.org/abs/2512.08842
2. D. Gao, T. M. Lietman, C. Dong, and T. C. Porco, *Mass drug administration: the importance of synchrony*, Mathematical Medicine and Biology (2017), DOI:10.1093/imammb/dqw005. https://www.math.miami.edu/~dzgao/Gao%20et%20al-MMB2016.pdf
3. P. Georgescu, G. Dimitriu, and K. Sinclair, *Impulsive control of an integrated pest management model with dispersal between patches* (2010), DOI:10.1142/S0218339010003561. https://math.etti.tuiasi.ro/pg/papers/JBS10.pdf
4. Courcelle, MacDonald, and Patel, *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses* (2026), arXiv:2609.09343. https://arxiv.org/abs/2609.09343
5. A. J. Terry, *Impulsive culling of a structured population on two patches*, Journal of Mathematical Biology 61 (2010), 843–875, DOI:10.1007/s00285-009-0325-0. https://www.researchgate.net/publication/41089669_Impulsive_culling_of_a_structured_population_on_two_patches
