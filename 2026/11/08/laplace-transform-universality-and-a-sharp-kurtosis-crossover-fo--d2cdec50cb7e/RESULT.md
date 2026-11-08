# Laplace-transform universality and a sharp kurtosis crossover for trapped run–rest particles

## Finding
Consider an alternating run–rest particle in a one-dimensional harmonic trap, in dimensionless units,
\[
\dot X_t=-X_t+V_t.
\]
Each cycle has a run of independent duration \(R\sim\operatorname{Exp}(a)\), \(a>0\), with velocity \(V=\varepsilon\), where \(\varepsilon=\pm1\) is resampled fairly and independently at the beginning of every run. It is followed by a rest of duration \(T\ge0\), when \(V=0\). The rest durations are independent and identically distributed, independent of the runs and signs, with finite strictly positive mean \(\mu=\mathbb E T\). Put \(t_j=\mathbb E[e^{-jT}]\) for \(j=2,4\). There is a unique stationary position law, supported on \([-1,1]\). Its second and fourth moments depend on the **entire rest-duration distribution only through \(\mu,t_2,t_4\)**, via the explicit finite formulas in the proof.

For the first non-memoryless phase-type rest law \(T=T_1+T_2\), where the two independent stages have \(\operatorname{Exp}(b)\) durations, \(b>0\), the stationary moments are
\[
M_2=\frac{b}{(a+1)(2a+b)},\qquad
M_4=\frac{3b(b+2)^2}{(a+1)(a+3)(2a+b)(2ab+2a+b^2+4b+4)}.
\]
The fourth cumulant \(K_4=M_4-3M_2^2\) is
\[
K_4=\frac{6b\,P_a(b)}{(a+1)^2(a+3)(2a+b)^2(2ab+2a+b^2+4b+4)},
\]
where
\[
P_a(b)=-b^3-(2a+4)b^2+(3a^2+a-4)b+4a(a+1).
\]
For every \(a>0\), this cubic has **exactly one positive, simple root** \(b_*(a)\). Thus the stationary position law has positive fourth cumulant for \(0<b<b_*(a)\), zero cumulant at \(b=b_*(a)\), and negative fourth cumulant for \(b>b_*(a)\).

For an exponential rest of the **same mean**, with rate \(c=b/2\), the unique fourth-cumulant threshold is
\[
c_*(a)=\frac{\sqrt{5a^2+8a+4}-a-2}{2}.
\]
The sharp comparison is
\[
\boxed{\frac{b_*(a)}2<c_*(a)\quad\text{for every }a>0.}
\]
Thus replacing an exponential rest by a two-stage Erlang rest at fixed mean shifts the positive-to-negative fourth-cumulant crossing to a strictly **lower** mean-rest exit rate. This is a statement about normalized fourth-moment shape, not a thermodynamic phase transition or a claim about all distributional modalities.

## Assumptions and scope
All rates and durations in the above statement are dimensionless. In physical units, with trap relaxation rate \(\kappa>0\), run speed \(v>0\), and run-exit and Erlang-stage rates \(\gamma_R,\gamma_T>0\), put \(a=\gamma_R/\kappa\), \(b=\gamma_T/\kappa\) and rescale position by \(v/\kappa\). The fourth cumulant scales by \((v/\kappa)^4\), so its sign is unaffected. The rest duration \(T\) in the general statement is measured in units of \(1/\kappa\). Runs, rests and newly chosen directions are independent across cycles. There is no translational thermal noise, no moving trap, and no interaction between particles.

## Proof
**1. Embedded stationary law.** Write \(Y\) for position at the start of a run, and \(Z\) for position immediately after it. The cycle recurrence is
\[
Z=e^{-R}Y+\varepsilon(1-e^{-R}),\qquad
Y'=e^{-T}Z.
\]
The multiplier \(e^{-(R+T)}\) is in \((0,1)\) almost surely, with negative mean logarithm \(-1/a-\mu\). Standard backward iteration of this contractive random affine recursion constructs a unique stationary \(Y\), independent of the next cycle, with \(|Y|\le1\). Stationary cycle occupation gives the unique stationary continuous-time position law. Sign symmetry makes all odd moments vanish.

**2. Run-end and run-beginning moments.** For \(j\ge1\), define \(r_j=\mathbb E[e^{-jR}]=a/(a+j)\), and set
\[
u_2=1-2r_1+r_2,\quad
u_{22}=r_2-2r_3+r_4,\quad
u_4=1-4r_1+6r_2-4r_3+r_4.
\]
Explicitly, \(u_2=2/[(a+1)(a+2)]\), \(u_{22}=2a/[(a+2)(a+3)(a+4)]\), and \(u_4=24/[(a+1)(a+2)(a+3)(a+4)]\). Let \(y_j=\mathbb E[Y^j]\) and \(z_j=\mathbb E[Z^j]\). Expansion over the independent sign gives
\[
y_2=t_2(r_2y_2+u_2),\qquad
y_4=t_4(r_4y_4+6u_{22}y_2+u_4).
\]
Therefore
\[
y_2=\frac{t_2u_2}{1-t_2r_2},\quad
y_4=\frac{t_4(6u_{22}y_2+u_4)}{1-t_4r_4},\quad
z_2=r_2y_2+u_2,\quad
z_4=r_4y_4+6u_{22}y_2+u_4.
\]
All denominators are positive because \(0\le t_j\le1\) and \(0<r_j<1\).

**3. Full stationary moments by cycle occupation.** For a run aged \(s<R\), position is \(e^{-s}Y+\varepsilon(1-e^{-s})\); for a rest aged \(s<T\), it is \(e^{-s}Z\). The renewal-reward formula divides the mean integrated moments per cycle by \(1/a+\mu\). Integrating over the exponential run survival function, and using \(\int_0^\infty e^{-as}(1-e^{-s})^2ds=u_2/a\), \(\int_0^\infty e^{-(a+2)s}(1-e^{-s})^2ds=u_{22}/a\), and \(\int_0^\infty e^{-as}(1-e^{-s})^4ds=u_4/a\), gives
\[
\begin{aligned}
M_2&=\frac{y_2/(a+2)+u_2/a+(1-t_2)z_2/2}{1/a+\mu},\\
M_4&=\frac{y_4/(a+4)+6u_{22}y_2/a+u_4/a+(1-t_4)z_4/4}{1/a+\mu}.
\end{aligned}
\]
This proves the claimed three-number dependence on the rest law. No uncomputed long-time limit is used: the stationary moments are ordinary time-occupation moments of an ergodic regenerative system.

**4. Two-stage Erlang reduction.** Here \(\mu=2/b\), \(t_2=(b/(b+2))^2\), and \(t_4=(b/(b+4))^2\). Substitution and exact rational reduction give the displayed \(M_2,M_4,K_4\). For the exponential rest of rate \(c\), substitute \(\mu=1/c\), \(t_j=c/(c+j)\): the fourth cumulant has the sign of
\[
E_a(c)=a^2+a-(a+2)c-c^2.
\]
Its positive root is the stated \(c_*(a)\).

**5. Uniqueness and strict ordering.** For \(a>0\), \(P_a(0)=4a(a+1)>0\), while \(P_a(b)\to-\infty\). Its nonzero coefficient signs, in descending powers of \(b\), have exactly one sign change regardless of the sign of \(3a^2+a-4\). Descartes' rule of signs thus gives exactly one positive root counted with multiplicity, hence the root is simple and all asserted signs follow. The exact polynomial identity
\[
P_a(2c)=(6c+4)E_a(c)-2c^2(a+c)
\]
implies \(P_a(2c_*(a))=-2c_*(a)^2[a+c_*(a)]<0\). Since \(P_a\) changes sign only at \(b_*(a)\), necessarily \(b_*(a)<2c_*(a)\). This completes the proof.

## Verification
The accompanying standard-library script `verify.py` constructs the full finite-state generator for phase-type rests with one, two or three exponential stages, and independently solves its stationary polynomial-moment balance equations over exact rational numbers. It compares these with the general renewal-reward formulas in **90** parameter/stage cases, verifies the specialized first- and second-stage formulas, and checks the exact threshold-comparison polynomial identity in 30 further rational cases. Three additional rational root brackets are tested. Execute with `python3 verify.py` from the extracted package directory. These finite tests check the calculations; the all-parameter and arbitrary-rest-distribution conclusions are proved above.

## Relationship to prior work
Sun, Ye and Chen (2026) obtain exact conditional steady-state position distributions for a harmonically confined run-and-tumble model with **exponentially distributed run and tumble lifetimes**. Sun, Ye and Podgornik (first publicly posted 2024) give an exact characteristic function and moment method for that same exponential-duration model. Both furnish essential comparison formulas, but their run–rest time law is memoryless and does not provide the finite-mean arbitrary-rest three-Laplace-statistic reduction or the Erlang-2/mean-matched-exponential threshold comparison. Farago and Smith (2024) treat a different non-Markovian model with an arbitrary **time between reorientations** and nonzero propulsion throughout; their numerical steady-state framework has no independent zero-velocity residence phase. These scopes differ in the actual stochastic dynamics, not merely in notation.

## Limitations
The sharp boundary classifies the **fourth cumulant**, not the number of density peaks, distributional stochastic dominance, relaxation rates, or a macroscopic phase transition. The random-rest universality requires independent finite-mean rest durations, exponentially distributed runs, and independent symmetric resampling of direction. This theorem does not address heavy-tailed infinite-mean rests or correlated cycle parameters. Publication-priority assessment is limited to the accessible indexed and primary sources listed below; an unindexed more general formula could cover some of these deductions.

## References
- A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1 (first public October 18, 2026), https://arxiv.org/abs/2610.24961 .
- A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (first public September 1, 2024), https://arxiv.org/abs/2409.00578 .
- O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576 (first public January 3, 2024), https://arxiv.org/abs/2401.01576 .
