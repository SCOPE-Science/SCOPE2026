# A twofold stationary-moment fold and three-moment identifiability in a finite-tumble harmonic particle

## Finding

For the one-dimensional harmonically trapped run-and-tumble particle with a genuine zero-propulsion tumble state, **three consecutive even stationary position moments (second, fourth and sixth) identify both positive internal switching rates uniquely**, when the trap relaxation and active speed are known. By contrast, the second and fourth moments have a sharply classified **two-to-one region**: different finite run/tumble rate pairs can yield the same two moments. The result determines the complete admissibility and multiplicity classification of the first two moments and proves that the sixth moment eliminates all finite-rate ambiguities.

Write \(Y=bX/v\) and \(m_{2j}=\mathbb E[Y^{2j}]\), and define the dimensionless rates \(a=\gamma_R/b\) and \(c=\gamma_T/b\). With
\[
s=m_2,\qquad q=\frac{m_4}{3m_2},\qquad \rho=\frac{m_6}{5m_4},\qquad A_s=\frac{1-s}{s},
\]
all physical rate pairs satisfy \(0<s<1\), \(0<a<A_s\), and
\[
c=\frac{as(1+a)}{1-s(1+a)},\qquad q=q_s(a)=\frac{2+s(a+1)(a-2)}{(a+3)[a+2-2s(a+1)]},
\]
\[
\rho=\rho_s(a)=\frac{4+s(a+1)(a-4)}{(a+5)[a+4-4s(a+1)]}.
\]
For each fixed \(s\in(0,1)\), \(q_s\) decreases strictly to a unique minimum \(q_*(s)\) at \(a=a_*(s)\), then increases strictly to the excluded limiting value \(q_\infty(s)=s/(1+2s)\). In particular, the number of *finite positive* rate pairs consistent with \((s,q)\) is
\[
\begin{array}{c|c}
\text{condition}&\text{number of rate pairs}\\ \hline
q_*(s)<q<q_\infty(s)&2\\
q=q_*(s)&1\\
q_\infty(s)\le q<1/3&1\\
\text{all other }q&0.
\end{array}
\]
Here \(a_*(s)\) is uniquely specified as the root in \((0,A_s)\) of
\[
(5s^2-3s)a^2+(10s^2-12s+2)a+5(1-s)^2=0,
\]
and \(q_*(s)=q_s(a_*(s))\). The **full triple** \((s,q,\rho)\) is injective on \(a,c>0\).

An exact twofold witness is
\[
(a,c)=\left(\frac34,\frac{21}4\right),\qquad
(a',c')=\left(\frac{11}{15},\frac{143}{30}\right).
\]
Both pairs have \(m_2=1/2\) and \(m_4=29/80\), but their sixth moments are respectively \(1073/3680\) and \(7627/26144\). Thus the third even moment carries genuinely new identifying information.

## Assumptions and scope

Let \(b,v,\gamma_R,\gamma_T>0\). A stationary particle \(X_t\in\mathbb R\) evolves by
\[
\dot X_t=-bX_t+vS_t,
\]
where \(S_t\) is an independent-rate continuous-time Markov chain on \(\{-1,0,+1\}\): each run state \(\pm1\) jumps to the tumble state \(0\) at rate \(\gamma_R\), and \(0\) jumps to each run state \(\pm1\) at rate \(\gamma_T/2\). There is no translational Brownian forcing, tumble-state propulsion, directional bias or state-dependent trap relaxation. The two rates are unknown, while \(b\) and \(v\) are independently calibrated. Observations are exact stationary ensemble moments, not finite-sample estimates. Rates \(\gamma_R\) and \(\gamma_T\) need not be equal. All assertions are for every pair of finite strictly positive switching rates and every \(b,v>0\).

The stationary law is well-defined and unique: under a stationary irreducible internal chain the pullback solution \(Y_t=\int_{-\infty}^t e^{-(t-u)}S_u\,du\) exists, is supported on \([-1,1]\), and synchronous coupling contracts any difference of particle positions exponentially. The dimensionless time unit is \(b^{-1}\). Symmetry under \((Y,S)\mapsto(-Y,-S)\) makes all odd stationary moments vanish.

## Proof

**1. Stationary moment recurrence.** In dimensionless time, let \(R_n=\mathbb E[Y^n\mathbf 1_{\{|S|=1\}}]\), \(T_n=\mathbb E[Y^n\mathbf 1_{\{S=0\}}]\), and \(H_n=\mathbb E[Y^n S]\). The generator applied to these bounded polynomial observables yields, for every integer \(n\ge1\),
\[
(n+a)R_n=nH_{n-1}+cT_n,\quad (n+c)T_n=aR_n,\quad (n+a)H_n=nR_{n-1}.
\]
The invariant internal-chain probabilities give \(R_0=c/(a+c)\). For \(k\ge1\), eliminating \(T_{2k}\) and \(H_{2k-1}\) gives
\[
R_{2k}=\frac{(2k-1)(2k+c)}{(2k-1+a)(2k+a+c)}R_{2k-2},
\qquad m_{2k}=\frac{2k+a+c}{2k+c}R_{2k}.
\]
In particular,
\[
m_2=\frac{c}{(a+c)(a+1)},
\]
\[
m_4=\frac{3c(c+2)}{(a+c)(a+1)(a+3)(a+c+2)},
\]
\[
m_6=\frac{15c(c+2)(c+4)}{(a+c)(a+1)(a+3)(a+5)(a+c+2)(a+c+4)}.
\]
These equations derive directly from the stationary Markov generator and do not assume a density formula or an asymptotic closure.

**2. Exact two-moment feasibility.** Fix any observed \(s=m_2\). Since \(m_2=\{c/(a+c)\}/(a+1)\), positivity of both rates is equivalent to \(0<s<1\) and \(0<a<A_s=(1-s)/s\), with
\[
c=\frac{as(1+a)}{1-s(1+a)}.
\]
Substitute this into \(q=m_4/(3m_2)\) to obtain \(q_s(a)\) stated above. All denominators are strictly positive in the physical interval, because \(s(a+1)<1\). Direct differentiation gives
\[
q_s'(a)=-\frac{2N_s(a)}{(a+3)^2[a+2-2s(a+1)]^2},
\]
\[
N_s(a)=(5s^2-3s)a^2+(10s^2-12s+2)a+5(1-s)^2.
\]
At the endpoints,
\[
N_s(0)=5(1-s)^2>0,\qquad
N_s(A_s)=-\frac{(1-s)^2}{s}<0.
\]
Since \(N_s\) is a polynomial of degree at most two, these opposite endpoint signs allow **exactly one simple crossing** in \((0,A_s)\) (two crossings would restore the same endpoint sign). Consequently \(q_s\) has exactly one strict minimum and no other turning point. The endpoint limits are \(\lim_{a\downarrow0}q_s(a)=1/3\) and \(\lim_{a\uparrow A_s}q_s(a)=s/(1+2s)\), the latter being smaller than \(1/3\). Neither endpoint is a finite positive two-rate model. The displayed 0/1/2 classification follows from strict monotonicity on the two branches and the intermediate value theorem.

**3. The sixth moment removes every finite ambiguity.** Suppose two distinct admissible run-rate ratios \(x\ne y\), both in \((0,A_s)\), produce identical \(s,q,\rho\). The equality of \(q_s(x)\) and \(q_s(y)\), after clearing strictly positive denominators and dividing by \(x-y\), gives
\[
(5s^2-3s)xy+(5s^2-6s+1)(x+y)+5(1-s)^2=0. \tag{1}
\]
Similarly, the equality of \(\rho_s(x)\) and \(\rho_s(y)\) gives
\[
(9s^2-3s)xy+(9s^2-10s+1)(x+y)+9(1-s)^2=0. \tag{2}
\]
The determinant of this linear system in \(xy\) and \(x+y\) is \(-8s^2(s-1)\ne0\). Solving (1)--(2) gives
\[
xy=\frac{A_s^2}{2},\qquad x+y=\frac{3A_s}{2}.
\]
Thus \(\{x,y\}=\{A_s/2,A_s\}\), which is impossible because the point \(A_s\) lies strictly outside the admissible open interval. Hence \(x=y\); the variance identity then gives the same \(c\), proving injectivity of the triple of stationary even moments. Given actual moments, recovery is constructive: solve the quadratic equation \(q_s(a)=q\), retain only roots \(0<a<A_s\), compute \(c\) from the variance, and select the unique candidate with the observed \(\rho\).

**4. A genuinely finite twofold example.** Substitution of both displayed rational rate pairs into the three moment formulas gives identical \(m_2=1/2\), \(m_4=29/80\), while \(m_6=1073/3680\) versus \(7627/26144\). These are distinct positive finite rates, so the two-moment ambiguity is not a fictitious zero-rate or infinite-rate boundary effect. In particular two consecutive even moments cannot guarantee global identifiability, whereas three do.

## Verification

Run `python verify_moments.py` using Python 3 and SymPy. The checker independently assembles the full three-state Markov generator, recursively solves the exact rational stationary conditional-moment equations through degree six for thirty positive rational rate pairs, and compares them with the three closed formulas. It also checks the rate-elimination identities, both cross-difference equations, the derivative and endpoint expressions, the twofold rational witness, and several numerical fold locations. Its current output is **117 passed algebraic, rational and diagnostic checks**. The general theorem is proved above; finite checks alone do not establish the assertions for arbitrary rates. The program and this proof require no external numerical data.

## Relationship to prior work

Sun, Ye and Podgornik (arXiv:2409.00578, first public release September 1, 2024) provide the finite-tumble harmonic particle model, a complete one-dimensional stationary density, and its forward moment-generating expressions. Those results are essential antecedents: the three stationary moments themselves are not claimed as new. The present finding is the inverse-moment multiplicity theorem—the **complete global two-moment fold** and **finite-rate uniqueness from the sixth moment**—which is not stated in that work and requires additional elimination, root-counting and injectivity arguments.

Basu, Majumdar, Rosso, Sabhapandit and Schehr (arXiv:1910.10083) study the related symmetric three-state model with equal run and tumble rates, a one-parameter subfamily that does not exhibit the two-rate inverse problem. Frydel (arXiv:2309.12537) treats stationary moments of run-and-tumble oscillators, emphasizing the always-running model and dimension dependence, not two separate positive run and tumble residence rates. Ceccarelli, Browning and Baker (arXiv:2605.13504) study structural identifiability of a different three-state constant-velocity jump process from trajectories or time-dependent population density, not finite stationary spatial moments in a harmonic trap. These scopes do not give the specific two-to-one region or three-moment reconstruction theorem. Broader or unindexed equivalent inverse formulas are a remaining originality risk.

## Limitations

All parameter identifications are structural and exact: measurement noise, finite-sample consistency, confidence intervals and numerical conditioning are not treated. Close to the fold \(a=a_*(s)\), a two-moment inverse is necessarily ill-conditioned; the result does not establish a uniform stable numerical inverse for three moments, especially near zero/infinite-rate boundaries. An independent calibration of \(b\) and \(v\) is required: absent this, the result identifies only dimensionless rates and scaled moments. The theorem does not cover translational diffusion, velocity persistence through tumbles, correlated reorientation, higher dimensions, nonharmonic traps or zero/infinite rate limits.

## References

1. Aoran Sun, Fangfu Ye, Rudolf Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first posted 2024-09-01. https://arxiv.org/abs/2409.00578
2. Urna Basu, Satya N. Majumdar, Alberto Rosso, Sanjib Sabhapandit, Gregory Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). https://arxiv.org/abs/1910.10083
3. Derek Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537 (2023). https://arxiv.org/abs/2309.12537
4. Arianna Ceccarelli, Alexander P. Browning, Ruth E. Baker, *Structural identifiability of partially-observed stochastic processes: from single-particle trajectories to total particle density data*, arXiv:2605.13504 (2026). https://arxiv.org/abs/2605.13504
