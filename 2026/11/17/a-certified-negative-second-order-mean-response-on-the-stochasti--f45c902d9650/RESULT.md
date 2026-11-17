# A certified negative second-order mean response on the stochastic logistic four-cycle

## Finding

Consider independent uniform random variables \(\xi_n\sim\mathrm{Unif}[-1,1]\) and the parametric-noise logistic recurrence
\[
X_{n+1}=\left(\frac72+\varepsilon\xi_n\right)X_n(1-X_n).
\]
Let \(p_0,p_1,p_2,p_3\) be the attracting, prime-period-four cycle of the deterministic map \(f(x)=\tfrac72 x(1-x)\), ordered so that \(p_0\in(0.500884210307217,0.500884210307219)\) and \(p_{j+1}=f(p_j)\), indices modulo four. There exist \(\varepsilon_0>0\) and four pairwise disjoint compact intervals \(I_j\) around \(p_j\), with \(0<I_j<1\), such that for each \(0\le\varepsilon<\varepsilon_0\) all allowed random maps send \(I_j\) into \(I_{j+1}\). On \(I=\bigcup_{j=0}^3 I_j\) the Markov chain has a unique invariant probability \(\mu_\varepsilon\), and its stationary average satisfies
\[
\int_I x\,d\mu_\varepsilon(x)=\frac14\sum_{j=0}^3p_j+B\varepsilon^2+o(\varepsilon^2),
\qquad -0.548<B<-0.546.
\]
In particular, every sufficiently small nonzero parametric-noise amplitude strictly lowers this localized stationary mean relative to the deterministic attracting four-cycle. The coefficient is uniquely specified by the exact finite linear recurrences below, and numerical evaluation gives \(B\approx-0.54709428061716\).

## Assumptions and scope

All independent noises are uniform on \([-1,1]\), and the map parameter is therefore uniform on \([7/2-\varepsilon,7/2+\varepsilon]\). The limiting statement is as \(\varepsilon\downarrow0\). The invariant probability is unique **on the four-phase trapping set** \(I\), not on the entire closed unit interval: the extinction measure concentrated at \(0\) is also invariant. The intervals can be fixed independently of sufficiently small \(\varepsilon\); no claim is made for large noise, other deterministic parameter values, or all initial populations.

Define \(\lambda=7/2\), \(a_j=\lambda(1-2p_j)\), and \(c_j=p_j(1-p_j)\). Let the four-periodic vectors \(v_j,b_j\) be the unique solutions of
\[
v_{j+1}=a_j^2v_j+c_j^2,\qquad
b_{j+1}=a_jb_j-\lambda v_j,\qquad
v_{j+4}=v_j,\quad b_{j+4}=b_j.
\]
Then the exact response coefficient is
\[
B=\frac1{12}\sum_{j=0}^3 b_j.
\]
The denominators governing uniqueness are \(1-\prod_{j=0}^3a_j^2\) and \(1-\prod_{j=0}^3 a_j\), both nonzero.

## Proof

**1. Certified attracting prime four-cycle.** With \(\lambda=7/2\), the rational bracket \([500884210307217/10^{15},500884210307219/10^{15}]\) has opposite signs for \(f^4(x)-x\) at its endpoints; the signs are positive at the left and negative at the right. Iterating this bracket gives four disjoint intervals strictly inside \((0,1)\). The exact interval calculation in `checker.py` bounds their derivative product by
\[
-0.031<\prod_{j=0}^3a_j<-0.030.
\]
Thus a fixed point of \(f^4\) lies in the bracket, the four phase points are distinct, and the four-return map contracts near it. This is a hyperbolically attracting prime four-cycle.

**2. Local random invariant probability.** Since the product of absolute one-step derivatives is below one, select positive neighborhood radii \(r_j\) such that \(|a_j|r_j<r_{j+1}\) cyclically. By continuity, shrinking all radii and choosing \(\varepsilon_0>0\) yields pairwise disjoint phase intervals \(I_j=[p_j-r_j,p_j+r_j]\subset(0,1)\), mapped into the next interval by every parameter in the prescribed noise support. For each fixed four-phase block, the composition of any four admissible maps is a uniform strict contraction on \(I_j\). Iterating independent blocks backwards therefore defines a unique stationary random fixed point in each phase. The induced four-step transition is contractive in the Wasserstein coupling, hence has a unique invariant distribution in each \(I_j\). The one-step chain cyclically permutes these four distributions and has their unique equal-weight mixture \(\mu_\varepsilon\).

**3. Second-order response.** Uniform contraction of the four-step compositions also makes their stationary pullback points twice continuously differentiable with respect to \(\varepsilon\) near zero, with derivatives uniformly bounded over all bounded noise sequences. Consequently, in stationary phase \(j\), one can write uniformly in the noise realization
\[
X_j=p_j+\varepsilon U_j+\varepsilon^2W_j+o(\varepsilon^2).
\]
Expanding the actual recurrence yields
\[
U_{j+1}=a_jU_j+c_j\xi_j,
\qquad
W_{j+1}=a_jW_j-\lambda U_j^2+(1-2p_j)U_j\xi_j.
\]
The stationary \(U_j\) depends only on past noise and is independent of the fresh \(\xi_j\). With \(\mathbb E\xi_j=0\) and \(\mathbb E\xi_j^2=1/3\), its expectation vanishes and the periodic second moment satisfies \(3\mathbb E U_j^2=v_j\). The cross term in the \(W\) equation has expectation zero. Thus \(3\mathbb E W_j=b_j\), and averaging the four phase means proves the displayed coefficient \(B=\sum_jb_j/12\). This expansion is a theorem for the localized invariant probability, not an inference from finite simulations.

**4. Rigorous sign.** `checker.py` performs exact rational interval propagation from the two rational root endpoints, solves the periodic variance recurrence through the four-return multiplier, then solves the periodic mean recurrence. The resulting interval for \(B\) lies strictly inside \((-548/1000,-546/1000)\). Both bounds are exact-rational inequalities; the printed decimal is explanatory only. Hence \(B<0\). Since the remainder is \(o(\varepsilon^2)\), the mean is strictly smaller for every sufficiently small positive \(\varepsilon\).

## Verification

The standalone Python 3 file `checker.py` uses only the standard-library `fractions.Fraction` class, with rational interval arithmetic. Run `python3 checker.py` beside this document. Its assertions certify the root-sign bracket, the hyperbolic four-return multiplier and the sign interval for the coefficient. Algebraic differentiability and uniqueness arguments in the proof are analytic and are not delegated to the finite computation; the checker does not verify the existence of a global stationary distribution for all positive initial values.

## Relationship to prior work

Cruz, Wei, Hardin and Radunskaya, *Long-term Averages of the Stochastic Logistic Map* (arXiv:2206.03849, first public 2022-06-08), Section 3.4 and Conjecture 4.1, present numerical evidence that parametric noise decreases the average in the attracting period-four regime, following rigorous period-one and period-two results. Their period-four sign is explicitly a conjecture, not claimed here as an independently invented observation. The result above proves that conjectured direction locally at the natural rational parameter \(\lambda=7/2\) and gives a certified quadratic response coefficient.

Ayers and Radunskaya, *Noisy Fixed Points* (arXiv:2403.13116), prove asymptotic stability in a distinct chaotic parameter range \((3.87,4)\), not the period-four response coefficient. Sato, Doan, Lamb and Rasmussen (arXiv:1811.03994) study additive-noise stochastic bifurcations near period three, not this parametric-noise mean response. General stochastic perturbation/linear-response techniques are standard and not claimed as new; the concrete parameter-four-cycle sign certificate is the asserted contribution.

## Limitations

The theorem is local in noise amplitude and localized in state space. It does not resolve Conjecture 4.1 for all attracting period-four parameters or across the entire period-doubling cascade. An unindexed paper may contain an equivalent coefficient; search absence alone is not proof of publication priority. The formula also does not settle whether every initial \(x\in(0,1)\) enters the four-phase trapping set. No independently performed audit is claimed.

## References

- M. Cruz, A. Wei, J. Hardin, A. Radunskaya, *Long-term Averages of the Stochastic Logistic Map*, arXiv:2206.03849 (2022; revised 2023), https://arxiv.org/html/2206.03849v3, Section 3.4, Conjecture 4.1, and Appendix A.
- K. Ayers, A. Radunskaya, *Noisy Fixed Points: Stability of the Invariant Distribution of the Random Logistic Map*, arXiv:2403.13116 (2024), https://arxiv.org/abs/2403.13116.
- Y. Sato, T. S. Doan, J. S. W. Lamb, M. Rasmussen, *Dynamical characterization of stochastic bifurcations in a random logistic map*, arXiv:1811.03994 (2018), https://arxiv.org/abs/1811.03994.
