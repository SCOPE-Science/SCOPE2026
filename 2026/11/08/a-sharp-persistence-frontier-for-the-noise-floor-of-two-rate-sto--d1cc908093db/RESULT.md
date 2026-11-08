# A sharp persistence frontier for the noise floor of two-rate stochastic gradient descent

## Finding

For a scalar quadratic with persistent independent gradient noise, retaining the same two stepsizes but changing their **temporal correlation** can reverse whether their stationary mean-square error is better or worse than that of the fixed arithmetic-mean stepsize. The reversal has an exact algebraic boundary.

Let \(h>0\), \(0<\delta<1\), \(h(1+\delta)<2\), and \(0\le p<1\). Put
\[
 h_+=h(1+\delta),\qquad h_-=h(1-\delta),\qquad t=h^2(1-\delta^2).
\]
The two stepsizes are selected by a symmetric, stationary two-state Markov chain whose probability of *repeating* the previous step is \(p\). Let \(V(p)\) be the stationary mean-square iterate and \(V_0\) the stationary mean-square iterate for the constant step \(h\), with identical independent centered gradient noise of variance \(\sigma^2>0\).

**Sharp classification.** The inequality \(V(p)<V_0\) holds **if and only if**
\[
 t>2\quad\text{and}\quad 0\le p<\frac{t-2}{2(t-1)}.
\]
For \(t>2\), equality holds precisely at \(p=(t-2)/(2(t-1))\). At \(t=2\), equality also holds at \(p=0\); elsewhere in the stated domain the correlated two-rate rule has strictly larger mean-square error. In particular, the independent-fair-choice policy \(p=1/2\) always has **greater** stationary mean-square error than the constant-mean rule, whereas sufficiently alternating schedules can have **smaller** mean-square error.

There is a second exact transition: for \(0<\delta<1\), \(V(p)\) is strictly *decreasing* in persistence \(p\) when \(0<h<1\), constant in \(p\) when \(h=1\), and strictly *increasing* in \(p\) when \(1<h<2\). This classification is valid for every permitted \(\delta\) and all \(0\le p<1\).

For example, with \(h=8/5\), \(\delta=1/8\), the two steps are \(9/5\) and \(7/5\). The exact improvement threshold is \(p_c=13/76\). In units of \(\sigma^2\), the alternating, \(p=1/10\), fixed and independent-noise floors are respectively
\[
 \frac{2179}{561},\quad\frac{383}{97},\quad 4,\quad\frac{13}{3}.
\]

## Assumptions and scope

The objective is \(f(x)=x^2/2\) on \(\mathbb R\). At iteration \(k\), the oracle returns the gradient \(X_k+\xi_k\), where \((\xi_k)\) are independent of the stepsize chain and each other, with \(\mathbb E\xi_k=0\), \(\mathbb E\xi_k^2=\sigma^2\in(0,\infty)\). Gaussian noise is **not** required.

The Markov state \(S_k\in\{+,-\}\) selects step \(h_{S_k}\) in
\[
 X_{k+1}=(1-h_{S_k})X_k-h_{S_k}\xi_k.
\]
The transition probabilities are \(\Pr(S_{k+1}=S_k\mid S_k)=p\) and \(\Pr(S_{k+1}\ne S_k\mid S_k)=1-p\), with stationary marginal \(\Pr(S_k=+)=\Pr(S_k=-)=1/2\). For \(0<p<1\) the joint stationary process is ergodic. At \(p=0\), the chain alternates deterministically; a random fair starting phase gives a stationary joint distribution and the same \(V(0)\) is the arithmetic average of the two limiting phase variances for a fixed starting phase. The strict condition \(h(1+\delta)<2\) makes both scalar update multipliers strictly contractive.

The comparison uses the **same average number of oracle evaluations per step** and the same one-step stepsize marginal. It does not equate transient convergence rates, nor optimize over all adaptive schedules.

## Proof

Write \(a_\pm=1-h_\pm\), \(\alpha=a_+^2\) and \(\beta=a_-^2\), so \(0\le\alpha,\beta<1\). Let
\[
 P=\begin{pmatrix}p&1-p\\1-p&p\end{pmatrix},\qquad
 D=1-p(\alpha+\beta)+(2p-1)\alpha\beta.
\]
The determinant is strictly positive because
\[
 D=p(1-\alpha)(1-\beta)+(1-p)(1-\alpha\beta)>0.
\]
The uniform contraction implies a unique finite-second-moment stationary solution for a stationary driving chain; at \(p=0\) this is understood in the stationary random-phase sense described above. Centering follows from the independent centered noise and contraction.

Set \(z_\pm=\mathbb E[X_k^2\mathbf1_{\{S_k=\pm\}}]\) in stationarity. Independence and conditional centering of the fresh noise give the exact equations
\[
 \begin{pmatrix}z_+\\z_-\end{pmatrix}
 =P^{\mathsf T}\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix}
 \begin{pmatrix}z_+\\z_-\end{pmatrix}
 +\frac{\sigma^2}{2}P^{\mathsf T}
 \begin{pmatrix}h_+^2\\h_-^2\end{pmatrix}.
\]
Inverting this \(2\times2\) linear system yields
\[
 V(p)=z_++z_-=
 \frac{\sigma^2\big[h_+^2+h_-^2+(1-2p)(\beta h_+^2+\alpha h_-^2)\big]}{2D}.
\]
The constant-step recursion has stationary second moment \(V_0=\sigma^2h/(2-h)\). Direct expansion, using \(t=h^2(1-\delta^2)\), factors the difference into
\[
 \boxed{V(p)-V_0=
 \frac{2\sigma^2 h^2\delta^2[2-t+2p(t-1)]}{(2-h)D}.}
\]
All factors outside the square bracket are strictly positive. For \(0<t<1\), the bracket decreases with \(p\) but stays at least \(t>0\); for \(1\le t<2\) it is positive. At \(t=2\) it equals \(2p\); for \(t>2\) it changes sign exactly at \((t-2)/(2(t-1))\). This proves every strict inequality and equality case.

Differentiating the explicit rational formula with respect to the probability \(p\), with \(h,\delta\) held fixed, yields
\[
 \boxed{\frac{dV}{dp}=
 \frac{8\sigma^2\delta^2h^4(1-\delta^2)(h-1)}{D^2}.}
\]
This proves the persistence-monotonicity transition. At \(p=1/2\), successive steps are independent fair choices and the stationary moment simplifies to
\[
 V(1/2)=\frac{\sigma^2h(1+\delta^2)}{2-h(1+\delta^2)},\qquad
 V(1/2)-V_0=
 \frac{2\sigma^2 h\delta^2}{(2-h)[2-h(1+\delta^2)]}>0.
\]
Both denominators are positive because \(h(1+\delta)<2\). Substitution of the rational example gives the four displayed rational values and \(p_c=13/76\).

## Verification

The standalone file `verify.py` (Python 3 with SymPy) checks by exact symbolic cancellation the stationary linear-system solution, the variance-difference factorization, derivative, fair-independent specialization, and positivity decomposition. It additionally verifies the four rational example values and the exact frontier, and performs 240 independent numerical conditional-moment recurrences. Run `python verify.py` in a directory containing the standalone file. The test run completed **250 assertions** successfully. The exact symbolic identities corroborate, but do not replace, the mathematical proof above.

## Relationship to prior work

Gürbüzbalaban, Hu, Şimşekli and Zhu (2023) study tail indices and moment conditions of SGD with cyclic, random and Markovian stepsizes. Their Markovian and cyclic results are principally for stochastic linear-regression Hessians and do not give the present fixed-curvature, additive-noise, exact stationary risk comparison or persistence frontier. The present calculation is not claimed as a new general method for Markov-modulated linear recursions.

Goujaud, Scieur, Dieuleveut, Taylor and Pedregosa (2022) analyze deterministic convergence acceleration from cyclical stepsizes, primarily with heavy-ball momentum and spectral gaps; this does not give a stationary gradient-noise error comparison. Chen, Mou and Maguluri (2021) address small-*constant*-stepsize stationary limits, not the exact finite-step Markov-correlation threshold. The general conditional-moment method is classical; the contributed result is the all-parameter sharp ordering and its two transitions for this natural two-rate design.

## Limitations

The result is scalar, quadratic, and requires fresh centered finite-variance gradient noise independent of stepsize selection, symmetric binary Markov switching, and individually stable positive steps. It compares stationary **iterate** mean squares, not excess risks for arbitrary nonlinear objectives, not generalization error, and not tail indices. It does not assert optimality among arbitrary time-varying or adaptive rules. Publication precedence outside inspected sources remains possible; independent external scientific assessment has not been performed.

## References

- M. Gürbüzbalaban, Y. Hu, U. Şimşekli, and L. Zhu, *Cyclic and Randomized Stepsizes Invoke Heavier Tails in SGD than Constant Stepsize* (first posted February 10, 2023), https://arxiv.org/abs/2302.05516 .
- B. Goujaud, D. Scieur, A. Dieuleveut, A. B. Taylor, and F. Pedregosa, *Super-Acceleration with Cyclical Step-sizes*, PMLR 151 (2022), https://proceedings.mlr.press/v151/goujaud22a.html .
- Z. Chen, S. Mou, and S. T. Maguluri, *Stationary Behavior of Constant Stepsize SGD Type Algorithms: An Asymptotic Characterization* (first posted November 11, 2021), https://arxiv.org/abs/2111.06328 .
