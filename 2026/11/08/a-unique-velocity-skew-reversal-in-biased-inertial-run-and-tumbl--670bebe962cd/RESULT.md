# A unique velocity-skew reversal in biased inertial run-and-tumble confinement

## Finding
For a harmonically confined inertial swimmer whose propulsion switches asymmetrically between two velocities, every stationary centered third-order moment can be calculated explicitly. A sharp contrast emerges: the position and mixed position–velocity third cumulants have fixed signs, whereas the *velocity* third cumulant changes sign once, at a stiffness depending only on the total orientation-switching rate, and not on its bias or the strength of independent thermal noise.

For the model and variables below, put
\[
H=(b+2)(q+1)(b+q^2+q)(4b+q^2+2q).
\]
Then the complete central third-order tensor, with \(Y=X-\delta/b\), is
\[
\begin{aligned}
\mathbb E[Y^3]&=-\frac{4\delta(1-\delta^2)(5bq+2b+2q^3+8q^2+10q+4)}{bH},\\
\mathbb E[Y^2V]&=0,\\
\mathbb E[YV^2]&=-\frac{4\delta(1-\delta^2)q(b+q^2+4q+2)}{H},\\
\mathbb E[V^3]&=\frac{4\delta(1-\delta^2)q^2(3b-2q-2)}{H}.
\end{aligned}
\]
For \(\delta>0\), the first and third expressions are strictly negative, while velocity skew changes sign uniquely at \(b=2(q+1)/3\), from negative below to positive above. For \(\delta<0\) every strict sign is reversed; for \(\delta=0\), all four expressions vanish. The critical stiffness lies strictly above \(1/4\), so the reversal is confined to the underdamped regime.

## Assumptions and scope
Consider the stationary dynamics
\[
 dX_t=V_t\,dt,\qquad dV_t=(-V_t-bX_t+\sigma_t)\,dt+\sqrt{2T}\,dW_t,
\]
where \(b>0\), \(T\ge0\), \(W\) is a two-sided standard Brownian motion independent of \(\sigma\), and \(\sigma\in\{-1,+1\}\) changes \(+1\to-1\) at rate \(\alpha>0\) and \(-1\to+1\) at rate \(\beta>0\). Define \(q=\alpha+\beta\) and \(\delta=(\beta-\alpha)/q\); hence \(q>0\), \(-1<\delta<1\). These units set inertial damping and propulsion amplitude equal to one. The trap is strictly harmonic and the driving two-state chain is autonomous.

The stable drift matrix \(A=\begin{psmallmatrix}0&1\\-b&-1\end{psmallmatrix}\) is Hurwitz for every \(b>0\). Starting the chain in its unique equilibrium, the stochastic convolution over the infinite past gives a unique stationary solution with finite moments of all orders: the telegraph contribution is bounded by an integrable matrix exponential and the independent Brownian contribution is Gaussian. Stationarity gives \(\mathbb E X=\delta/b\), \(\mathbb E V=0\). Define \(Y=X-\delta/b\) and \(S=\sigma-\delta\).

## Proof
The centered process satisfies \(dY=V\,dt\), \(dV=(-V-bY+S)\,dt+\sqrt{2T}\,dW\). The stationary two-state chain has \(\mathbb E[S]=0\), \(\mathbb E[S^2]=1-\delta^2\), and generator \(LS=-qS\). Moreover its two possible values imply the exact algebraic identity \(S^2=(1-\delta^2)-2\delta S\).

Set \(M_{ij}=\mathbb E[Y^iV^j]\) and \(N_{ij}=\mathbb E[Y^iV^jS]\), for integers \(i,j\ge0\). Stationarity of the joint Markov generator gives, for all pairs with finite degree,
\[
\begin{aligned}
0={}&iM_{i-1,j+1}-jM_{ij}-bjM_{i+1,j-1}+jN_{i,j-1}+Tj(j-1)M_{i,j-2},\\
0={}&iN_{i-1,j+1}-(j+q)N_{ij}-bjN_{i+1,j-1}\\
&\quad+j\big[(1-\delta^2)M_{i,j-1}-2\delta N_{i,j-1}\big]+Tj(j-1)N_{i,j-2},
\end{aligned}
\]
where terms multiplied by zero are omitted. Here \(M_{00}=1\), \(N_{00}=0\), and all degree-one \(M\)'s vanish. These equations also follow directly by Itô's formula and the two-state generator, with polynomial stationarity justified by finite moments.

Solving the first-degree balance yields
\[
N_{10}=\frac{1-\delta^2}{b+q^2+q},\qquad
N_{01}=\frac{q(1-\delta^2)}{b+q^2+q}.
\]
Define \(D=(q+1)(b+q^2+q)(4b+q^2+2q)\). The degree-two mixed moments needed at the next step are
\[
\begin{aligned}
N_{02}&=-\frac{4\delta(1-\delta^2)q(b+q^2+q)}{D},\\
N_{11}&=-\frac{2\delta(1-\delta^2)q(3q+2)}{D},\\
N_{20}&=-\frac{4\delta(1-\delta^2)(3q+2)}{D}.
\end{aligned}
\]
Since \(D\) includes \(b+q^2+q\), the first displayed line simplifies by cancellation. Now the degree-three \(M\) equations give
\[
M_{21}=0,\quad
M_{12}=\frac{N_{02}+2N_{11}}{b+2},\quad
M_{03}=\frac{2(N_{02}-bN_{11})}{b+2},\quad
M_{30}=\frac{2M_{12}+N_{20}}b.
\]
Substitution and collection over \(H=(b+2)D\) gives the four claimed formulas. The \(T\)-dependent terms in the degree-three \(M\) equations contain centered first-degree moments and vanish. Alternatively, the stationary process decomposes into an independent telegraph-driven response plus a centered Gaussian linear response, whose cumulants of order three vanish.

Every factor of \(H\) is strictly positive in the declared domain, and \(5bq+2b+2q^3+8q^2+10q+4\) and \(b+q^2+4q+2\) are strictly positive. Hence the only possible nontrivial cubic-sign transition is the simple root \(3b-2(q+1)=0\), unique for each \(q>0\) and independent of \(\delta\ne0\) and \(T\ge0\). For the homogeneous oscillator, underdamping means \(b>1/4\); because \(2(q+1)/3>2/3\), the transition always lies in this regime. The proof covers the threshold itself, both signs of bias, and the limiting case \(T=0\).

## Verification
The included `check.py` is a standalone Python 3 standard-library checker. It constructs and solves the stationary generator's exact-rational linear systems of degrees one, two and three rather than substituting the target formulas into the balance equations. On seven rational stiffnesses, three rate totals, five orientation biases and two thermal-noise intensities, it passed 1,096 exact-rational assertions. It also performed twelve independent finite-resolution causal impulse-response quadratures of the telegraph third-cumulant convolution; all agreed with the formulas to the documented tolerance. These finite checks test the algebra but do not prove the infinite parameter classification, which rests on the generator derivation and strict-positive-factor arguments above.

At \(b=2\), \(q=1\), \(\delta=1/3\), the exact central third moments in the displayed order are \(-19/297,0,-1/33,2/297\). With \(q=1\), the unique velocity-skew threshold is \(b=4/3\). The third moment at that threshold is zero without the other nonzero third cumulants vanishing; it is therefore not a claim of a Gaussian joint law.

## Relationship to prior work
Dutta, Kundu, Sabhapandit and Basu (2024) study a harmonically confined inertial run-and-tumble particle with *symmetric* orientation dynamics, including its moment equations, but do not state the asymmetric-bias cubic tensor or its sharp velocity-skew threshold. Patel and Chaudhuri (2024) consider an active Brownian particle with continuous angular diffusion, a different propulsion process. Pawula (1987) provides a general moment expression for dichotomous-noise-driven oscillators and may provide substantial methodological antecedents: its abstract is accessible but its complete article could not be inspected, so detailed overlap and publication priority with that work remain unresolved. Gitterman and Shapiro (2011) study asymmetric dichotomous *multiplicative random-mass* noise and mean response, rather than bounded additive propulsion and the present stationary cubic-sign classification.

The specific contribution assessed here is not the existence of a generator-moment method. It is the exact stationary cubic-tensor sign classification for biased additive telegraph propulsion, especially the bias- and temperature-independent unique velocity-skew reversal in an inertial harmonic trap.

## Limitations
The claim assumes two Markov orientation states, positive finite switching rates, linear stable confinement and independent additive Gaussian translational noise. Neither a general nonlinear trap nor non-Markovian switching nor higher-dimensional turning dynamics is covered. A sign of a third moment does not characterize the full density, irreversibility, or an estimator's performance. Publication priority relative to uninspected complete historical literature remains unresolved.

## References
1. Dutta, Kundu, Sabhapandit and Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension* (first arXiv public version 2024-06-10), https://arxiv.org/abs/2406.06120 .
2. Patel and Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance* (2024), https://arxiv.org/abs/2404.01107 .
3. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Physical Review A **35** (1987) 3102–3108, https://doi.org/10.1103/PhysRevA.35.3102 .
4. M. Gitterman and I. Shapiro, *Stochastic Resonance in a Harmonic Oscillator with Random Mass Subject to Asymmetric Dichotomous Noise*, Journal of Statistical Physics **144** (2011) 139–149, https://doi.org/10.1007/s10955-011-0240-9 .
