# A sharp recolonization threshold for bathtub-shaped regional extinction hazard

## Finding
Let \(N_t\in\{0,1,2,3}\) count occupied habitats in the completely connected three-habitat continuous-time extinction–colonization model. Each occupied patch empties at rate \(1\); every ordered occupied-to-empty edge causes recolonization at rate \(c\ge0\). The empty state is absorbing. Suppose \(\Pr(N_0=1)=\Pr(N_0=3)=1/2\), \(\Pr(N_0=2)=0\), with a uniformly chosen singleton site when \(N_0=1\). For \(\tau=\inf\{t\ge0:N_t=0}\) define
\[
 S_c(t)=\Pr(\tau>t),\qquad h_c(t)=-\frac{S_c'(t)}{S_c(t)}.
\]
**Theorem.** For every \(0\le c<1\), there exists precisely one \(t_*(c)>0\) such that \(h_c\) is strictly decreasing on \([0,t_*(c)]\) and strictly increasing on \([t_*(c),\infty)\). For every \(c\ge1\), \(h_c\) is strictly decreasing on \([0,\infty)\), including the boundary \(c=1\). In both regimes \(h_c(t)\) tends to the smallest positive eigenvalue of the killed generator. No homogeneous complete-graph system with one or two habitats and nonempty initial state can have a nonmonotone extinction hazard, for any \(c\ge0\).

At \(c=0\), the unique minimum is at
\[
 t_*(0)=-\log\!\left(\frac{8-2\sqrt7}3\right).
\]
At \(c=1\), the extinction survival function is an exact positive mixture of just two exponentials, so the equality case has no interior minimum.

## Assumptions and scope
The result concerns the **first** attainment of total empty occupancy, with no spontaneous immigration from the empty state. The homogeneous local extinction clock has rate \(1\). Recolonization clocks are independent and additive over ordered occupied-to-empty edges. There are no common environmental shocks, density-dependent recovery, local within-patch population counts or observation errors. Time is measured in units of the inverse local extinction rate. For local extinction rate \(e>0\) and per-edge colonization rate \(r\), the threshold becomes \(r=e\) by time rescaling. The special initial mixture is part of the theorem, not a statement for every three-habitat initial law.

## Proof
**1. Killed count generator.** For occupancy count \(k\) the rate \(k\to k-1\) is \(k\) and the rate \(k\to k+1\) is \(c k(3-k)\). In the transient-state order \((1,2,3)\), the subgenerator and initial row law are
\[
 T_c=\begin{pmatrix}-1-2c&2c&0\\2&-2-2c&2c\\0&3&-3\end{pmatrix},\qquad
 w=(1/2,0,1/2).
\]
Consequently \(S_c(t)=w e^{tT_c}\mathbf 1\), positive for every finite \(t\). The finite state system absorbs almost surely, since from every nonempty state a sequence of extinctions has positive probability, and the state space is finite.

**2. The exact resolvent.** Direct adjugate expansion gives
\[
 \int_0^\infty e^{-zt}S_c(t)\,dt=\frac{V_c(z)}{D_c(z)},
\]
\[
 D_c(z)=z^3+(6+4c)z^2+(11+8c+4c^2)z+6,
\]
\[
 V_c(z)=z^2+\frac{11+8c}2z+\frac{17+14c+8c^2}2.
\]
The nonzero off-diagonal rates make \(-T_c\) similar to a symmetric irreducible Jacobi matrix when \(c>0\), and its three positive eigenvalues are therefore distinct. At \(c=0\), they are \(1,2,3\), also distinct. Denote them \(0<\alpha_c<\beta_c<\gamma_c\). Partial fractions have a unique representation
\[
 S_c(t)=a_c e^{-\alpha_ct}+b_c e^{-\beta_ct}+d_c e^{-\gamma_ct}.
\]
The residues depend continuously on \(c\ge0\). At \(c=0\), independent local extinctions give
\[
 S_0(t)=2e^{-t}-\frac32e^{-2t}+\frac12e^{-3t},
\]
so \((a_0,b_0,d_0)=(2,-3/2,1/2)\).

**3. Unique spectral sign switch.** Exact elimination yields
\[
 \operatorname{Res}_z(D_c,V_c)=-(c-1)(4c^2+5c+6).
\]
A residue can vanish only if the corresponding simple pole is canceled by \(V_c\). The only nonnegative parameter permitting cancellation is \(c=1\). There
\[
 D_1(z)=(z+3)(z^2+7z+2),\quad V_1(z)=\frac12(z+3)(2z+13).
\]
The canceled eigenvalue \(3\) lies strictly between \(\alpha_1=(7-\sqrt{41})/2\) and \(\gamma_1=(7+\sqrt{41})/2\). Since \(S_1(0)=1\) and \(-S'_1(0)=1/2\) lies strictly between \(\alpha_1\) and \(\gamma_1\), the remaining two residues are positive. At \(c=1\), the resultant zero is simple and the eigenvalue \(3\) and canceled numerator factor are both simple, so the middle residue has a simple zero, changing sign. By continuity and the absence of any other nonnegative resultant zero,
\[
 a_c>0,\quad d_c>0\ \text{for all }c\ge0,\qquad
 b_c<0\ (0\le c<1),\ b_1=0,\ b_c>0\ (c>1).
\]
These are assertions about *spectral expansion coefficients*, not probabilities; a negative middle coefficient is compatible with \(S_c(t)>0\).

**4. Hazard derivative and its zeros.** Differentiation of the three-mode formula gives
\[
 S_c(t)^2 h_c'(t)=-\sum_{i<j}u_i u_j(\lambda_i-\lambda_j)^2 e^{-(\lambda_i+\lambda_j)t},
\]
where \(u=(a_c,b_c,d_c)\) and \(\lambda=(\alpha_c,\beta_c,\gamma_c)\). For \(c\ge1\), every nonzero spectral coefficient is positive, and at least two are positive; therefore \(h_c'(t)<0\) at every finite \(t\).

For \(0\le c<1\), write the right side multiplied by \(e^{(\alpha_c+\beta_c)t}\) as
\[
 F(t)=P-Me^{-ut}+Re^{-vt},\quad P,M,R>0,\quad 0<u=\gamma_c-\beta_c<v=\gamma_c-\alpha_c.
\]
The derivative \(F'(t)=Mu e^{-ut}-Rv e^{-vt}\) is either always positive or changes sign only once from negative to positive. Thus \(F\) can decrease at first and then increase, but cannot have an interior local maximum. Independently the initial distribution gives
\[
 h_c'(0)=\frac14-\left(\frac12+c\right)=-\frac14-c<0.
\]
Because \(b_c<0\), the slowest term in the derivative identity is \(-(\beta_c-\alpha_c)^2 a_c b_c e^{-(\alpha_c+\beta_c)t}\), so \(h_c'(t)>0\) for all sufficiently large \(t\). It follows that \(F\), and hence \(h_c'\), has exactly one positive zero, with negative sign before and positive sign after it. Since \(a_c>0\) is the slow-mode coefficient, the hazard converges to \(\alpha_c\), from below for \(c<1\) and from above for \(c\ge1\).

**5. Sharp habitat-number minimum.** With one habitat, \(S(t)\) is exponential. With two homogeneous habitats the transient count generator is
\[
 T_{2}=\begin{pmatrix}-1-c&c\\2&-2\end{pmatrix}.
\]
Its eigenvalues \(\lambda_-<\lambda_+\) are distinct and positive even at \(c=0\). For *every* initial distribution over the nonempty configurations, symmetry lets the survival function be written \(S(t)=A e^{-\lambda_-t}+B e^{-\lambda_+t}\), with real coefficients. Therefore
\[
 S(t)^2h'(t)=-(\lambda_+-\lambda_-)^2 AB e^{-(\lambda_-+\lambda_+)t},
\]
which has a constant sign (or vanishes identically). No one- or two-habitat example can have a hazard with an interior turning point. The three-habitat construction exhibits one for every \(0\le c<1\), proving minimality.

## Verification
The included \(verify.py\) independently constructs the seven nonempty *labeled* three-habitat states, projects onto occupancy count, and compares \(e^{tQ}\) to the independently written \(T_c\) generator. It also symbolically verifies the resolvent, characteristic polynomial, resultant, critical cancellation and special-case hazard derivative. Run using Python with the dependencies in \(requirements.txt\): \(\texttt{python verify.py}\). Its latest replay passed all symbolic assertions and \(56\) vector comparisons (\(168\) count-state values) over seven colonization rates and eight times. Finite tests check implementation consistency; the proof above establishes the statements for the full infinite time and rate ranges.

## Relationship to prior work
The motivating biological issue is the "mega-patch" problem of hiding extinction and recolonization events by aggregating occupied sites (Cavanaugh et al., first online February 1, 2014). Extinction-time tail assumptions are discussed empirically by Drake (2014), and the classical quasi-stationary framework by Dickman and Vidigal (2002). Generalized mixtures yielding bathtub-shaped hazards are developed by Navarro, Guillamón and Ruiz (first online December 3, 2008). The present claim is *not* that mixed systems can exhibit bathtub hazards, which is established background. Its distinct content is the exact \(c=1\) sign transition, monotonicity on the whole opposite side, equality case, and three-habitat minimality for a **recolonizing** finite contact-metapopulation process. This is an analytic theoretical benchmark, not an empirical assertion.

## Limitations
The colonization and extinction model has fixed homogeneous independent exponential clocks, no recolonization from the absorbing empty state, an exceptional half-singleton/half-full initial distribution, and only a complete graph. Neither the sharp \(c=1\) threshold nor minimality is asserted for all three-site graphs, initial occupancy mixtures, environmental shocks, spatially heterogeneous rates or stochastic biodiversity outcomes. The source comparison does not constitute an independent historical-priority certification; a plausible generalized-mixture reference was not accessible in complete text.

## References
1. Cavanaugh, K. C., Siegel, D. A., Raimondi, P. T. & Alberto, F. (2014), *Patch definition in metapopulation analysis: a graph theory approach to solve the mega-patch problem*, Ecology 95, 316–328; first online 2014-02-01. https://doi.org/10.1890/13-0221.1
2. Drake, J. M. (2014), *Tail probabilities of extinction time in a large number of experimental populations*, Ecology 95, 1119–1126. https://doi.org/10.1890/13-1107.1
3. Navarro, J., Guillamón, A. & Ruiz, M. d. C. (2009), *Generalized mixtures in reliability modelling: Applications to the construction of bathtub shaped hazard models and the study of systems*, Applied Stochastic Models in Business and Industry 25, 323–337; first online 2008-12-03. https://doi.org/10.1002/asmb.750
4. Dickman, R. & Vidigal, R. (2002), *Quasi-stationary distributions for stochastic processes with an absorbing state*, Journal of Physics A 35, 1147–1166; arXiv version 2001-10-26. https://arxiv.org/abs/cond-mat/0110557
