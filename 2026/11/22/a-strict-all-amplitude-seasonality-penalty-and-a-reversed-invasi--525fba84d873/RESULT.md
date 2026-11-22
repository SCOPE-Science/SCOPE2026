# A strict all-amplitude seasonality penalty and a reversed invasion verdict for host–vector epidemics

## Finding
For the strictly vector-mediated host–vector infection linearization with constant positive loss rates and constant transmission coefficients, every positive, nonconstant periodic vector-abundance profile decreases the principal Floquet invasion exponent **strictly** below the exponent for its time-averaged vector population, without a small-amplitude restriction. The difference equals an explicit nonnegative variance defect. There is moreover a smooth, biologically compatible periodic population for which the averaged system permits local invasion but the actual periodic system forbids it, with a rational, non-numerical negative bound.

Precisely, for positive \(a,d,b,c\), a period \(T>0\), and a positive \(T\)-periodic \(C^1\) abundance \(V\), define
\[
A(t)=\begin{pmatrix}-a&b\\cV(t)&-d\end{pmatrix},\qquad
\Lambda(V)=\frac1T\log\rho(\Phi_V(T)),\qquad
\bar V=\frac1T\int_0^T V(t)\,dt,
\]
where \(\Phi_V(0)=I\) and \(\Phi'_V=A(t)\Phi_V\). Write \(s=a+d\) and \(Q(t)=\frac{(a-d)^2}{4}+bcV(t)\). There is a positive \(T\)-periodic \(C^1\) function \(r\) (defined canonically in the proof) for which
\[
\boxed{\Lambda(V)=-\frac{s}{2}+\bar r,\qquad
\Lambda(\bar V)-\Lambda(V)
=\frac{\operatorname{Var}_T(r)}{\sqrt{\bar Q}+\bar r}\ge0.}
\]
Equality holds **if and only if** \(V\) is constant. Here \(\operatorname{Var}_T(r)=T^{-1}\int_0^T(r-\bar r)^2\,dt\). Thus even when the temporal mean itself is at the constant-environment invasion threshold, every nonconstant profile has a negative invasion exponent.

For \(Q(t)=Q_0+q\sin(\omega t)\), with \(0<q<Q_0\) and \(\omega>0\), the variance identity also implies the all-amplitude quantitative bound
\[
\boxed{\Lambda(V)\le -\frac{s}{2}+\sqrt{Q_0}-
\frac{q^2}{4\sqrt{Q_0}\bigl(\omega+2\sqrt{Q_0+q}\bigr)^2}.}
\]

## Assumptions and scope
The model is the infected-host/infected-vector subsystem obtained by linearizing a host SIR–vector SI model at a disease-free state with constant susceptible-host density; \(a\) is host recovery, \(d\) vector mortality, \(b\) the positive vector-to-host coefficient times disease-free susceptible-host density, and \(cV(t)\) the time-dependent host-to-vector contact coefficient. Incidence is standard linear at zero infection, without vertical transmission or a low-infection shrinking adjustment. These hypotheses are a specified case of the 2026 prescribed-vector framework of Isnel et al. [1, Appendix A]. The linear stability/invasion assertion refers to the infected directions at the disease-free periodic state; it does not assert nonlinear endemic persistence.

For the source's no-vertical-transmission demographic admissibility, impose in addition \(V'(t)+dV(t)\ge0\). The comparison theorem is valid whether or not this additional inequality is imposed, and the constructed witness below satisfies it strictly.

## Proof
**1. Positive Floquet mode.** Strict positivity of the off-diagonal entries ensures that the period evolution matrix \(\Phi_V(T)\) is strictly positive. Perron–Frobenius therefore supplies a solution \((H(t),I(t))\) strictly positive for all \(t\), with \((H(t+T),I(t+T))=e^{\Lambda T}(H(t),I(t))\). Integrating the logarithmic derivative of either component gives \(\Lambda>-a\) and \(\Lambda>-d\).

**2. Scalar periodic Riccati equation.** Eliminate \(I=(H'+aH)/b\) from the infected system. Then \(H''+sH'+(ad-bcV)H=0\). Setting \(y=e^{st/2}H\) gives
\[
y''=Q(t)y,\qquad Q(t)>0.
\]
Let \(\gamma=\Lambda+s/2>0\). The function \(y\) is strictly positive and obeys \(y(t+T)=e^{\gamma T}y(t)\), and the same identity holds for \(y'\). Since \(y''=Qy>0\), its derivative is strictly increasing. Thus \((e^{\gamma T}-1)y'(t)=y'(t+T)-y'(t)>0\), proving \(y'(t)>0\). Define \(r=y'/y>0\). It is periodic, and
\[
r'=Q-r^2,\qquad \bar r=\gamma=\Lambda+s/2.
\]
Average the Riccati equation to obtain \(\overline{r^2}=\bar Q\), equivalently \(\bar r^2+\operatorname{Var}_T(r)=\bar Q\). For constant abundance \(\bar V\), the Perron eigenvalue is \(\Lambda(\bar V)=-s/2+\sqrt{\bar Q}\). Taking the difference and rationalizing gives the stated exact variance defect. If the defect vanishes, \(r\) is constant, so \(Q=r^2\) and \(V\) is constant. The converse is immediate.

**3. Explicit sinusoidal penalty.** Suppose \(Q(t)=Q_0+q\sin\omega t\). At a maximum of the periodic positive \(r\), the Riccati equation gives \(r_{\max}^2=Q(t_{\max})\le Q_0+q\). Multiply \(r'=Q-r^2\) by \(\sin\omega t\), then average and integrate by parts:
\[
\frac q2=-\omega\overline{(r-\bar r)\cos\omega t}
+\overline{(r-\bar r)(r+\bar r)\sin\omega t}.
\]
By Cauchy–Schwarz and \(0<r,\bar r\le r_{\max}\), the absolute value of the right side is at most \((\omega+2r_{\max})\sqrt{\operatorname{Var}_T(r)/2}\). Hence
\[
\operatorname{Var}_T(r)\ge\frac{q^2}{2(\omega+2\sqrt{Q_0+q})^2}.
\]
Use \(\sqrt{Q_0}+\bar r\le2\sqrt{Q_0}\) in the variance-defect formula to obtain the quantitative bound.

**4. Exact smooth threshold reversal.** Take \(a=d=b=c=1\), \(T=2\pi\), and
\[
V(t)=\frac{1001}{1000}+\frac14\sin t.
\]
This is strictly positive and meets demographic compatibility because \(V'+V=1001/1000+(\cos t+\sin t)/4\ge1001/1000-\sqrt2/4>0\). Its mean is \(1001/1000\), and the constant-mean Perron exponent satisfies
\[
0<\Lambda(\bar V)=\sqrt{\frac{1001}{1000}}-1<\frac1{2000}.
\]
Here \(Q_0=1001/1000\), \(q=1/4\), and \(\sqrt{Q_0+q}<9/8\). Also \(\sqrt{Q_0}<1001/1000\). The rigorous penalty estimate implies
\[
\Lambda(V)<\frac1{2000}-\frac{250}{169\cdot1001}
=-\frac{330831}{338338000}<-\frac9{10000}<0.
\]
Therefore the temporal-mean model grows in the infected directions but the true periodic one decays exponentially. All displayed bounds are exact algebraic inequalities; no eigenvalue computation is used to prove the sign reversal.

## Verification
The standalone standard-library script `verify.py` checks the rational inequalities, the positivity of the demographic source, the closed-form constant-environment threshold, and integrates the period fundamental matrix numerically for corroboration. Its numerical Floquet value at the witness is approximately \(-0.00264495219\), safely below the proven \(-0.0009\) bound. Numerical checks illustrate the result only; the global inequality for arbitrary positive periodic profiles is established by the above proof.

## Relationship to prior work
The October 19, 2026 prescribed-vector framework of Isnel et al. [1] supplies the linear infection model and demographic-compatibility condition, and studies frozen-time reproduction indices, finite-time epidemic emergence, and a separate nonlinear shrinking adjustment. It does not establish the exact all-amplitude arithmetic-mean Floquet comparison or the smooth source-admissible threshold reversal. Bacaër [2] and Khong, Carmona and Gandon [3] already establish small-seasonality *decrease* of vector-borne epidemic reproduction numbers in related models; the direction of the seasonality effect is therefore not claimed as new. The result here strengthens a specifically defined constant-coefficient host–vector setting to arbitrary positive waveforms and exact strictness, gives a Riccati-variance equality, a nonperturbative sine penalty, and a fully exact sign-reversal witness. Clairambault, Gaubert and Perthame [4] give general geometric-mean lower bounds for cooperative periodic systems, not this arithmetic-mean upper bound. Breda, De Reggi and Ripoll [5] provide computation of periodic reproduction numbers, rather than this waveform-independent closed inequality.

## Limitations
This is a theorem about local linear epidemic invasion only. It assumes exactly one time-varying infection coefficient via vector abundance, fixed host recovery and vector mortality, fixed susceptible host density, and no vertical infection or shrinking adjustment. Allowing periodic biting, both transmission directions, or mortality can reverse comparison directions. The Floquet exponent is not numerically identical to the periodic basic reproduction number, although the linear invasion-threshold signs correspond under standard assumptions. Historical priority was checked against accessible sources, not proved exhaustively: Bacaër's 2007 full text remained inaccessible; its accessible abstract states only a second-order small-sinusoid approximation. An independent mathematical audit has not been performed.

## References
[1] L. Isnel, J. Papaïx, O. Bonnefon, S. Soubeyrand and L. Roques, *When vector abundance constrains vector-borne transmission: inside epidemic dynamics within a prescribed population* (2026), first posted 2026-10-19, https://arxiv.org/abs/2610.25971.

[2] N. Bacaër, *Approximation of the basic reproduction number R0 for vector-borne diseases with a periodic vector population*, Bull. Math. Biol. (2007), https://doi.org/10.1007/s11538-006-9166-9.

[3] V. H. Khong, P. Carmona and S. Gandon, *Seasonality and the persistence of vector-borne pathogens*, J. R. Soc. Interface (2023), https://doi.org/10.1098/rsif.2023.0470.

[4] J. Clairambault, S. Gaubert and B. Perthame, *An inequality for the Perron and Floquet eigenvalues of monotone differential systems and age structured equations* (2007), https://arxiv.org/abs/0704.3820.

[5] D. Breda, S. De Reggi and J. Ripoll, *On the numerical computation of R0 in periodic environments* (2025), https://arxiv.org/abs/2509.00847.
